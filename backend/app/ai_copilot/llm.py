from typing import List

from app.ai_copilot.prompts import build_prompt


def generate_ai_response(
    user_message: str,
    context: str,
) -> tuple[str, List[str]]:
    """
    Placeholder LLM implementation.

    Later this function will call Amazon Bedrock
    (or another LLM provider) using the generated prompt.
    """

    prompt = build_prompt(
        user_message=user_message,
        context=context,
    )

    response = (
        "CloudSense AI is currently running in demo mode.\n\n"
        "The following prompt would be sent to the LLM:\n\n"
        f"{prompt}"
    )

    sources = [
        "EC2",
        "S3",
        "RDS",
        "Lambda",
        "EBS",
        "VPC",
    ]

    return response, sources