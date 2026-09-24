import re
from collections import Counter
from dataclasses import dataclass
from functools import lru_cache

from sqlalchemy.orm import Session

from app.ai_copilot.rag.chunker import Chunk, chunk_documents
from app.ai_copilot.rag.documents import load_documents
from app.ai_copilot.rag.embeddings import embed_with_client
from app.ai_copilot.rag.vector_store import VectorStore
from app.cloud.aws.credential_manager import get_authenticated_client
from app.core.config import settings
from app.models.user import User

_WORD_PATTERN = re.compile(r"[a-z0-9]+")


@dataclass
class RetrievedChunk:
    title: str
    provider: str
    category: str
    text: str
    score: float


@lru_cache(maxsize=1)
def _load_chunks() -> tuple[Chunk, ...]:
    """
    All knowledge base chunks, used as the corpus for lexical fallback
    search and cached for the life of the process (documents only change
    on deploy).
    """

    return tuple(chunk_documents(load_documents()))


@lru_cache(maxsize=1)
def _load_vector_store() -> VectorStore | None:
    return VectorStore.load()


_TITLE_MATCH_WEIGHT = 3
_BODY_TERM_CAP = 4


def _tokenize(text: str) -> set[str]:
    return {word for word in _WORD_PATTERN.findall(text.lower()) if len(word) > 2}


def _tokenize_counts(text: str) -> Counter:
    return Counter(word for word in _WORD_PATTERN.findall(text.lower()) if len(word) > 2)


def _lexical_search(query: str, top_k: int) -> list[RetrievedChunk]:
    """
    Keyword search over the raw knowledge base corpus. Requires no
    embeddings or AWS access, so knowledge Q&A keeps working even for users
    who haven't connected a cloud account yet.

    A query word appearing in the title counts far more than one buried in
    the body, and body mentions are frequency-weighted (capped, so one very
    repetitive doc can't dominate). Plain set-overlap scoring was found to
    rank a document that merely *mentions* a term (e.g. "CloudWatch",
    which references EC2 in passing) above the document actually *about*
    that term, whenever both matched the same single query word.
    """

    query_words = _tokenize(query)

    if not query_words:
        return []

    max_possible = len(query_words) * (_TITLE_MATCH_WEIGHT + _BODY_TERM_CAP)

    scored: list[RetrievedChunk] = []

    for chunk in _load_chunks():
        title_words = _tokenize(chunk.title)
        body_counts = _tokenize_counts(chunk.text)

        raw_score = 0

        for word in query_words:
            if word in title_words:
                raw_score += _TITLE_MATCH_WEIGHT

            raw_score += min(body_counts.get(word, 0), _BODY_TERM_CAP)

        if raw_score == 0:
            continue

        scored.append(
            RetrievedChunk(
                title=chunk.title,
                provider=chunk.provider,
                category=chunk.category,
                text=chunk.text,
                score=raw_score / max_possible,
            )
        )

    scored.sort(key=lambda item: item.score, reverse=True)

    return scored[:top_k]


def _vector_search(
    query: str,
    db: Session,
    current_user: User,
    top_k: int,
) -> list[RetrievedChunk] | None:
    """
    Returns None (rather than an empty list) when vector search could not
    be attempted at all, so the caller knows to fall back to lexical search
    instead of treating "no AWS account" as "no relevant knowledge".
    """

    store = _load_vector_store()

    if store is None:
        return None

    try:
        client = get_authenticated_client(
            service_name="bedrock-runtime",
            db=db,
            current_user=current_user,
        )
        query_vector = embed_with_client(client, query)
    except Exception:
        return None

    results = store.search(query_vector, top_k)

    return [
        RetrievedChunk(
            title=chunk.title,
            provider=chunk.provider,
            category=chunk.category,
            text=chunk.text,
            score=score,
        )
        for chunk, score in results
    ]


def retrieve_relevant_knowledge(
    query: str,
    db: Session,
    current_user: User,
    top_k: int | None = None,
) -> list[RetrievedChunk]:
    """
    Retrieves the most relevant knowledge base chunks for a query.

    Prefers semantic vector search (Bedrock Titan embeddings against the
    prebuilt knowledge index) when available, and transparently degrades to
    lexical keyword search when the index hasn't been built yet or the
    current user has no working Bedrock access - so the copilot's knowledge
    layer never hard-fails just because a cloud account isn't connected.
    """

    top_k = top_k or settings.RAG_TOP_K

    results = _vector_search(query, db, current_user, top_k)

    if results is None:
        results = _lexical_search(query, top_k)

    return results


def best_match_is_confident(chunks: list[RetrievedChunk]) -> bool:
    return bool(chunks) and chunks[0].score >= settings.RAG_MIN_RELEVANCE_SCORE
