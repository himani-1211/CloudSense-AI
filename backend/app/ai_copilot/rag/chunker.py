from dataclasses import dataclass

from app.ai_copilot.rag.documents import Document

MAX_CHUNK_CHARS = 900


@dataclass
class Chunk:
    chunk_id: str
    document_id: str
    title: str
    provider: str
    category: str
    text: str


def chunk_document(document: Document) -> list[Chunk]:
    """
    Splits a document into paragraph-aligned chunks bounded by MAX_CHUNK_CHARS.

    Knowledge base articles are already short (a few hundred words), so most
    documents produce exactly one chunk; this only kicks in for longer docs
    added later, keeping retrieval granular without splitting mid-sentence.
    """

    paragraphs = [p.strip() for p in document.content.split("\n\n") if p.strip()]

    chunks: list[Chunk] = []
    current_paragraphs: list[str] = []
    current_length = 0
    part = 1

    def flush():
        nonlocal current_paragraphs, current_length, part

        if not current_paragraphs:
            return

        chunks.append(
            Chunk(
                chunk_id=f"{document.id}#{part}",
                document_id=document.id,
                title=document.title,
                provider=document.provider,
                category=document.category,
                text="\n\n".join(current_paragraphs),
            )
        )

        part += 1
        current_paragraphs = []
        current_length = 0

    for paragraph in paragraphs:

        if current_length + len(paragraph) > MAX_CHUNK_CHARS and current_paragraphs:
            flush()

        current_paragraphs.append(paragraph)
        current_length += len(paragraph)

    flush()

    return chunks


def chunk_documents(documents: list[Document]) -> list[Chunk]:
    chunks: list[Chunk] = []

    for document in documents:
        chunks.extend(chunk_document(document))

    return chunks
