"""
Builds the AI Copilot's knowledge base vector index.

Run this whenever knowledge_base/*.md files are added or changed:

    python -m app.ai_copilot.rag.build_index

Requires AWS credentials with Bedrock access available via the default
boto3 credential chain (environment variables or shared AWS config) -
this is a one-time/admin build step, separate from any CloudSense
tenant's connected AWS account, because the knowledge base is shared
content, not per-user data.

Pass --dry-run to validate document loading and chunking without calling
Bedrock (useful for checking the content pipeline without AWS access).
"""

import argparse
import sys

from app.ai_copilot.rag.chunker import chunk_documents
from app.ai_copilot.rag.documents import load_documents
from app.ai_copilot.rag.embeddings import build_system_bedrock_client, embed_with_client
from app.ai_copilot.rag.vector_store import VectorStore


def main() -> None:

    parser = argparse.ArgumentParser(description="Build the AI Copilot knowledge base index.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Load and chunk documents without calling Bedrock or writing an index.",
    )
    args = parser.parse_args()

    documents = load_documents()

    if not documents:
        print("No knowledge base documents found.", file=sys.stderr)
        sys.exit(1)

    chunks = chunk_documents(documents)

    print(f"Loaded {len(documents)} documents -> {len(chunks)} chunks.")

    if args.dry_run:
        for chunk in chunks:
            print(f"  [{chunk.provider}] {chunk.title} ({chunk.chunk_id})")
        return

    client = build_system_bedrock_client()

    embeddings = []

    for index, chunk in enumerate(chunks, start=1):
        print(f"Embedding {index}/{len(chunks)}: {chunk.title}")
        embeddings.append(embed_with_client(client, chunk.text))

    store = VectorStore.build(chunks=chunks, embeddings=embeddings)
    store.save()

    print(f"Saved index with {len(chunks)} vectors.")


if __name__ == "__main__":
    main()
