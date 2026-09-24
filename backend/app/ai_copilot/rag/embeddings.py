import json

import boto3

from app.core.config import settings


class EmbeddingError(Exception):
    pass


def _invoke_titan_embedding(client, text: str) -> list[float]:

    body = json.dumps(
        {
            "inputText": text[:8000],
            "dimensions": settings.RAG_EMBEDDING_DIMENSIONS,
            "normalize": True,
        }
    )

    response = client.invoke_model(
        modelId=settings.BEDROCK_EMBEDDING_MODEL_ID,
        body=body,
        accept="application/json",
        contentType="application/json",
    )

    payload = json.loads(response["body"].read())

    embedding = payload.get("embedding")

    if not embedding:
        raise EmbeddingError("Bedrock embedding response did not contain an embedding.")

    return embedding


def embed_with_client(client, text: str) -> list[float]:
    """
    Embeds a single piece of text using an already-authenticated Bedrock
    runtime client. Raised exceptions are the caller's responsibility to
    handle (e.g. falling back to lexical retrieval).
    """

    return _invoke_titan_embedding(client, text)


def build_system_bedrock_client():
    """
    Bedrock client authenticated via the default AWS credential chain
    (environment variables / shared AWS config), used for offline knowledge
    base index building. This is intentionally NOT tied to any CloudSense
    tenant's connected AWS account - the knowledge base is shared, global
    content, not per-user data.
    """

    return boto3.client(
        service_name="bedrock-runtime",
        region_name=settings.AWS_DEFAULT_REGION,
    )
