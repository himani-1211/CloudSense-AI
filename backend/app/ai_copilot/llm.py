from typing import List

from botocore.exceptions import ClientError
from sqlalchemy.orm import Session

from app.ai_copilot.prompts import build_prompt
from app.ai_copilot.rag.retriever import RetrievedChunk
from app.cloud.aws.credential_manager import get_authenticated_client
from app.core.config import settings
from app.models.user import User


def generate_ai_response(
    user_message: str,
    infrastructure_context: str,
    knowledge_chunks: List[RetrievedChunk],
    db: Session,
    current_user: User,
) -> tuple[str, List[str]]:
    """
    Generates an AI response using Amazon Bedrock, grounded in retrieved
    knowledge base articles and the user's live infrastructure.

    The Bedrock client is created using the AWS credentials already
    connected to the current CloudSense user account.
    """

    prompt = build_prompt(
        user_message=user_message,
        infrastructure_context=infrastructure_context,
        knowledge_chunks=knowledge_chunks,
    )

    sources = [f"Knowledge base: {chunk.title} ({chunk.provider.upper()})" for chunk in knowledge_chunks]
    sources.append("Live AWS infrastructure")

    try:
        bedrock = get_authenticated_client(
            service_name="bedrock-runtime",
            db=db,
            current_user=current_user,
        )

        response = bedrock.converse(
            modelId=settings.BEDROCK_MODEL_ID,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "text": prompt,
                        }
                    ],
                }
            ],
            inferenceConfig={
                "maxTokens": settings.BEDROCK_MAX_TOKENS,
                "temperature": settings.BEDROCK_TEMPERATURE,
            },
        )

        answer = (
            response["output"]["message"]["content"][0]["text"]
            .strip()
        )

        sources.append("Amazon Bedrock")

        return answer, sources

    except ClientError as exc:
        error_code = exc.response.get(
            "Error",
            {},
        ).get(
            "Code",
            "Unknown",
        )

        error_message = exc.response.get(
            "Error",
            {},
        ).get(
            "Message",
            "Unknown Bedrock error.",
        )

        return (
            "I couldn't generate an AI response from Amazon Bedrock.\n\n"
            f"AWS error: {error_code} - {error_message}",
            [],
        )

    except Exception as exc:
        return (
            "I couldn't generate an AI response right now.\n\n"
            f"Error: {str(exc)}",
            [],
        )
