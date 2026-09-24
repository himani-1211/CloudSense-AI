# AI Copilot — RAG Knowledge Layer

This package is the retrieval half of the AI Copilot's "AI Cloud Engineer" design: it retrieves
relevant, cloud-agnostic technical knowledge and hands it to the LLM alongside the user's live
infrastructure data (built in `app/ai_copilot/prompts.py` from `app/cloud/aws/resource_service.py`).

## How a question gets answered

1. `documents.py` loads every `.md` file under `app/ai_copilot/knowledge_base/**`.
2. `chunker.py` splits each document into retrieval-sized chunks (most docs are short enough to stay
   as a single chunk).
3. At index-build time (`build_index.py`), each chunk is embedded via Amazon Bedrock
   (Titan Embeddings) and stored in `rag/index/` (`vector_store.py`).
4. At request time (`retriever.py`), the user's question is embedded the same way and compared
   against the stored vectors with cosine similarity.
5. `service.py` combines the retrieved chunks with live infrastructure context and calls the LLM
   (`llm.py`) to produce a grounded answer with real citations.

## Graceful degradation

Vector search requires both a built index and a working Bedrock connection for the current user
(the same AWS account already connected via Integrations). Neither is guaranteed — a brand new
user may not have connected AWS yet, and the index may not have been built. In that case:

- `retriever.py` transparently falls back to **lexical keyword search** over the same knowledge
  base documents (no embeddings, no AWS calls) — title matches are weighted higher than body
  matches so the correct document reliably wins over one that merely mentions the topic in passing.
- `service.py` falls back to returning the best-matching document verbatim, or a canned
  best-practices list for recommendations, instead of an LLM-synthesized answer.

This means knowledge Q&A works out of the box with zero AWS setup, and gets progressively better
(semantic retrieval + LLM synthesis grounded in live infrastructure) once AWS/Bedrock is connected.

## Adding knowledge

Drop a new `.md` file under `knowledge_base/<provider>/`, with a small frontmatter header:

```
---
title: Some Service Name
provider: aws | azure | gcp | oracle | cross_cloud
category: compute | storage | database | networking | security | serverless | cost | ...
---

Body content here.
```

New providers just need a new folder — nothing else keys off the AWS/Azure/GCP/Oracle list, so
adding a fifth provider needs no code changes, only documents.

After adding or editing documents, rebuild the vector index:

```
python -m app.ai_copilot.rag.build_index
```

This requires AWS credentials with Bedrock access via the default boto3 credential chain
(environment variables or shared AWS config) — intentionally *not* tied to any tenant's connected
AWS account, since the knowledge base is shared content, not per-user data. Use `--dry-run` to
validate document loading/chunking without calling Bedrock.

## Future: agentic actions

The product direction for AI Copilot is to eventually take actions on a user's infrastructure
(e.g. stopping an idle instance, applying a security group fix) with explicit user approval per
action. That is intentionally **not implemented yet** — `prompts.py`'s system prompt tells the
model to explain and recommend, not act, and no execution path exists. When that's built, it
should live alongside this package as a separate, explicitly-gated module rather than folded into
generation, so retrieval/explanation and action-taking stay independently reviewable.
