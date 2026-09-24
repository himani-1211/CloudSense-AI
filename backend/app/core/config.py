from dotenv import load_dotenv
import os


load_dotenv()


class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL")

    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60)
    )

    ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY")

    # ==========================================================
    # AWS
    # ==========================================================

    AWS_DEFAULT_REGION = os.getenv(
        "AWS_DEFAULT_REGION",
        "ap-south-1",
    )

    # ==========================================================
    # Amazon Bedrock
    # ==========================================================

    BEDROCK_MODEL_ID = os.getenv(
        "BEDROCK_MODEL_ID",
        "anthropic.claude-haiku-4-5-20251001-v1:0",
    )

    BEDROCK_MAX_TOKENS = int(
        os.getenv("BEDROCK_MAX_TOKENS", 1024)
    )

    BEDROCK_TEMPERATURE = float(
        os.getenv("BEDROCK_TEMPERATURE", 0.3)
    )

    # ==========================================================
    # AI Copilot - RAG Knowledge Base
    # ==========================================================

    BEDROCK_EMBEDDING_MODEL_ID = os.getenv(
        "BEDROCK_EMBEDDING_MODEL_ID",
        "amazon.titan-embed-text-v2:0",
    )

    RAG_EMBEDDING_DIMENSIONS = int(
        os.getenv("RAG_EMBEDDING_DIMENSIONS", 512)
    )

    RAG_TOP_K = int(
        os.getenv("RAG_TOP_K", 4)
    )

    RAG_MIN_RELEVANCE_SCORE = float(
        os.getenv("RAG_MIN_RELEVANCE_SCORE", 0.15)
    )


settings = Settings()