
from sqlalchemy.orm import Session

from app.ai_copilot.llm import generate_ai_response
from app.ai_copilot.intent import detect_intent, Intent
from app.ai_copilot.aws_handler import handle_aws_intent
from app.ai_copilot.models import CopilotMessage
from app.ai_copilot.prompts import build_infrastructure_context
from app.ai_copilot.rag.retriever import retrieve_relevant_knowledge, best_match_is_confident
from app.ai_copilot.schemas import (
    SuggestedQuestion,
    ChatMessage,
    AIRecommendation,
    AIResponse,
    Capability,
    CopilotSummary,
    ChatRequest,
    ChatResponse,
)
from app.cloud.aws.resource_service import get_resource_summary
from app.models.user import User

AWS_RESOURCE_INTENTS = {
    Intent.EC2_COUNT,
    Intent.EC2_LIST,
    Intent.S3_COUNT,
    Intent.S3_LIST,
    Intent.RDS_COUNT,
    Intent.RDS_LIST,
    Intent.LAMBDA_COUNT,
    Intent.LAMBDA_LIST,
    Intent.VPC_COUNT,
    Intent.VPC_LIST,
    Intent.EBS_COUNT,
    Intent.EBS_LIST,
    Intent.SUMMARY,
}


def _save_message(
    db: Session,
    current_user: User,
    role: str,
    text: str,
    sources: list[str] | None = None,
) -> None:
    db.add(
        CopilotMessage(
            owner_id=current_user.id,
            role=role,
            text=text,
            sources=sources or [],
        )
    )
    db.commit()


def get_chat_history(
    db: Session,
    current_user: User,
    limit: int = 100,
) -> list[ChatMessage]:
    """
    Returns the user's persisted conversation, oldest first, capped to the
    most recent `limit` messages.
    """

    rows = (
        db.query(CopilotMessage)
        .filter(CopilotMessage.owner_id == current_user.id)
        .order_by(CopilotMessage.created_at.desc())
        .limit(limit)
        .all()
    )

    rows.reverse()

    return [
        ChatMessage(
            role=row.role,
            text=row.text,
            timestamp=row.created_at.strftime("%b %d, %Y %I:%M %p"),
        )
        for row in rows
    ]


def get_copilot_summary(
    db: Session,
    current_user: User,
) -> CopilotSummary:
    """
    Returns AI Copilot overview using live AWS resources.
    """

    history = get_chat_history(db=db, current_user=current_user)

    try:
        resources = get_resource_summary(
            db=db,
            current_user=current_user,
        )
        aws_connected = True
    except Exception:
        resources = {"ec2": [], "s3": [], "rds": [], "lambda": [], "ebs": [], "vpcs": []}
        aws_connected = False

    if not aws_connected:
        return CopilotSummary(
            suggested_questions=[
                SuggestedQuestion(text="What is EC2?"),
                SuggestedQuestion(text="What is the difference between S3 and EBS?"),
                SuggestedQuestion(text="Explain AWS security best practices."),
                SuggestedQuestion(text="What is Kubernetes?"),
            ],
            conversation=history or [
                ChatMessage(
                    role="assistant",
                    text=(
                        "I don't see a connected cloud account yet, so I can't analyze your "
                        "live infrastructure. You can still ask me about AWS, Azure, GCP or "
                        "Oracle Cloud concepts and best practices - or connect an AWS account "
                        "under Integrations to unlock infrastructure-aware answers and "
                        "recommendations."
                    ),
                    timestamp="Just now",
                )
            ],
            response=AIResponse(
                message="No cloud account connected yet.",
                recommendation=AIRecommendation(
                    actions=["Connect an AWS account under Integrations to get started."],
                ),
            ),
            capabilities=[
                Capability(
                    title="Infrastructure Insights",
                    description=(
                        "Connect an AWS account to unlock live infrastructure analysis."
                    ),
                ),
                Capability(
                    title="Security Recommendations",
                    description=(
                        "Retrieve AWS, Azure, GCP and Oracle Cloud best practices - "
                        "available right now, no account required."
                    ),
                ),
                Capability(
                    title="Cost & Knowledge Retrieval",
                    description=(
                        "Answers are grounded in a retrieval-augmented cloud knowledge base, "
                        "not guesswork."
                    ),
                ),
            ],
        )

    ec2 = resources["ec2"]
    s3 = resources["s3"]
    rds = resources["rds"]
    lambda_functions = resources["lambda"]
    ebs = resources["ebs"]
    vpcs = resources["vpcs"]

    total_resources = (
        len(ec2)
        + len(s3)
        + len(rds)
        + len(lambda_functions)
        + len(ebs)
        + len(vpcs)
    )

    suggested_questions = [
        SuggestedQuestion(text="Summarize my AWS infrastructure."),
        SuggestedQuestion(text="How many EC2 instances do I have?"),
        SuggestedQuestion(text="Show my S3 buckets."),
        SuggestedQuestion(text="Recommend infrastructure improvements."),
    ]

    assistant_message = (
        f"I discovered {total_resources} AWS resources in your AWS account, "
        f"including {len(ec2)} EC2 instance(s), "
        f"{len(rds)} RDS database(s), "
        f"{len(s3)} S3 bucket(s), "
        f"{len(lambda_functions)} Lambda function(s), "
        f"{len(ebs)} EBS volume(s), "
        f"and {len(vpcs)} VPC(s)."
    )

    conversation = history or [
        ChatMessage(
            role="assistant",
            text=assistant_message,
            timestamp="Just now",
        )
    ]

    actions = []

    if not ec2:
        actions.append(
            "Launch an EC2 instance to enable compute monitoring."
        )

    if not s3:
        actions.append(
            "Create an S3 bucket for storage management."
        )

    if not rds:
        actions.append(
            "Create an RDS database for database monitoring."
        )

    if total_resources:
        actions.append(
            "Enable Amazon CloudWatch metrics for deeper monitoring."
        )
        actions.append(
            "Review IAM permissions following least-privilege principles."
        )

    response = AIResponse(
        message=assistant_message,
        recommendation=AIRecommendation(
            actions=actions,
        ),
    )

    capabilities = [
        Capability(
            title="Infrastructure Insights",
            description=(
                "Analyze your live AWS infrastructure and explain what it means, "
                "not just what it is."
            ),
        ),
        Capability(
            title="Security Recommendations",
            description=(
                "Retrieve AWS, Azure, GCP and Oracle Cloud best practices and apply "
                "them to your actual environment."
            ),
        ),
        Capability(
            title="Cost & Knowledge Retrieval",
            description=(
                "Answers are grounded in a retrieval-augmented cloud knowledge base, "
                "not guesswork."
            ),
        ),
    ]

    return CopilotSummary(
        suggested_questions=suggested_questions,
        conversation=conversation,
        response=response,
        capabilities=capabilities,
    )


def _knowledge_response(
    question: str,
    infrastructure_context: str,
    db: Session,
    current_user: User,
) -> ChatResponse | None:
    """
    Answers a knowledge-style question using retrieval-augmented generation:
    relevant knowledge base chunks are retrieved, combined with live
    infrastructure context, and passed to the LLM. Returns None when no
    confident knowledge match exists, so the caller can fall through to the
    rest of the intent chain - matching the previous static-knowledge-base
    behavior.
    """

    chunks = retrieve_relevant_knowledge(
        query=question,
        db=db,
        current_user=current_user,
    )

    if not best_match_is_confident(chunks):
        return None

    answer, sources = generate_ai_response(
        user_message=question,
        infrastructure_context=infrastructure_context,
        knowledge_chunks=chunks,
        db=db,
        current_user=current_user,
    )

    if sources:
        return ChatResponse(answer=answer, sources=sources)

    # Bedrock unavailable (e.g. no AWS account connected yet): fall back to
    # returning the best-matching knowledge article directly.
    top_chunk = chunks[0]

    return ChatResponse(
        answer=top_chunk.text,
        sources=[f"Knowledge base: {top_chunk.title} ({top_chunk.provider.upper()})"],
    )


def chat_with_copilot(
    request: ChatRequest,
    db: Session,
    current_user: User,
) -> ChatResponse:
    """
    Handles one chat turn: generates the response, then persists both the
    user's message and the assistant's reply so the conversation survives
    a page reload (restored via get_chat_history / get_copilot_summary).
    """

    question = request.message.strip()

    response = _generate_chat_response(
        question=question,
        db=db,
        current_user=current_user,
    )

    _save_message(db, current_user, role="user", text=question)
    _save_message(db, current_user, role="assistant", text=response.answer, sources=response.sources)

    return response


def _generate_chat_response(
    question: str,
    db: Session,
    current_user: User,
) -> ChatResponse:
    """
    Main AI Copilot controller.

    Responsibilities:
    - Detect user intent
    - Handle greetings
    - Answer cloud knowledge questions via retrieval-augmented generation
    - Answer AWS account questions with deterministic, factual lookups
    - Provide recommendations grounded in retrieved best practices
    - Fallback to full RAG-grounded AI generation
    """

    intent = detect_intent(question)

    # ==========================================================
    # Greeting
    # ==========================================================

    if intent == Intent.GREETING:

        return ChatResponse(
            answer=(
                "Hello! 👋 I'm CloudSense AI, your AI Cloud Engineer.\n\n"
                "I can help you:\n"
                "• Learn cloud concepts across AWS, Azure, GCP and Oracle Cloud\n"
                "• Analyze your live cloud infrastructure\n"
                "• Explain issues and AWS concepts\n"
                "• Summarize your resources\n"
                "• Recommend improvements grounded in best practices\n\n"
                "How can I help you today?"
            ),
            sources=[],
        )

    # ==========================================================
    # Help
    # ==========================================================

    if intent == Intent.HELP:

        return ChatResponse(
            answer=(
                "Here are some things you can ask me:\n\n"
                "📘 Knowledge\n"
                "• What is EC2? What is Azure Blob Storage?\n"
                "• Explain Lambda\n"
                "• How do I create an EC2 instance?\n\n"
                "☁ AWS Account\n"
                "• Show my EC2 instances\n"
                "• List my S3 buckets\n"
                "• Infrastructure summary\n\n"
                "💡 Recommendations\n"
                "• Recommend improvements\n"
                "• Cost optimization tips\n"
                "• Security recommendations"
            ),
            sources=[],
        )

    # ==========================================================
    # Thanks
    # ==========================================================

    if intent == Intent.THANKS:

        return ChatResponse(
            answer=(
                "You're welcome! 😊 Feel free to ask anything "
                "about your cloud infrastructure or cloud concepts in general."
            ),
            sources=[],
        )

    # ==========================================================
    # Goodbye
    # ==========================================================

    if intent == Intent.GOODBYE:

        return ChatResponse(
            answer=(
                "Goodbye! 👋 Have a great day, and happy cloud engineering!"
            ),
            sources=[],
        )

    # ==========================================================
    # Live infrastructure (used by nearly every remaining branch)
    #
    # Discovery raises when no AWS account is connected yet. That must not
    # block pure knowledge questions (which previously worked standalone),
    # so a missing connection degrades to an explicit "not connected"
    # context instead of failing the whole request.
    # ==========================================================

    try:
        resources = get_resource_summary(
            db=db,
            current_user=current_user,
        )
        aws_connected = True
    except Exception:
        resources = {"ec2": [], "s3": [], "rds": [], "lambda": [], "ebs": [], "vpcs": []}
        aws_connected = False

    infrastructure_context = (
        build_infrastructure_context(resources)
        if aws_connected
        else "No cloud account is currently connected - live infrastructure data is unavailable."
    )

    # ==========================================================
    # Knowledge Questions (RAG)
    # ==========================================================

    if intent == Intent.KNOWLEDGE:

        knowledge_response = _knowledge_response(
            question=question,
            infrastructure_context=infrastructure_context,
            db=db,
            current_user=current_user,
        )

        if knowledge_response:
            return knowledge_response

    # ==========================================================
    # AWS Discovery (deterministic - exact counts/lists, no LLM)
    # ==========================================================

    if intent in AWS_RESOURCE_INTENTS:

        if not aws_connected:
            return ChatResponse(
                answer=(
                    "I don't see a connected AWS account yet, so I can't check your live "
                    "infrastructure. Connect one under Integrations and I'll be able to answer "
                    "this from your real resources."
                ),
                sources=[],
            )

        aws_answer = handle_aws_intent(
            intent=intent,
            resources=resources,
        )

        if aws_answer:

            return ChatResponse(
                answer=aws_answer,
                sources=["Live AWS infrastructure"],
            )

    # ==========================================================
    # Recommendations (RAG, grounded in best-practice knowledge + infra)
    # ==========================================================

    if intent == Intent.RECOMMENDATION:

        chunks = retrieve_relevant_knowledge(
            query=question,
            db=db,
            current_user=current_user,
        )

        answer, sources = generate_ai_response(
            user_message=question,
            infrastructure_context=infrastructure_context,
            knowledge_chunks=chunks,
            db=db,
            current_user=current_user,
        )

        if sources:
            return ChatResponse(answer=answer, sources=sources)

        # Bedrock unavailable: fall back to general best-practice guidance.
        return ChatResponse(
            answer=(
                "Here are a few recommendations based on general cloud best practices:\n\n"
                "• Remove unused resources.\n"
                "• Enable monitoring (e.g. CloudWatch).\n"
                "• Review IAM permissions.\n"
                "• Enable backups for databases.\n"
                "• Use Auto Scaling where applicable.\n"
                "• Enable encryption for storage services.\n\n"
                "Connect an AWS account with Bedrock access for recommendations tailored "
                "to your actual infrastructure."
            ),
            sources=[f"Knowledge base: {chunk.title} ({chunk.provider.upper()})" for chunk in chunks],
        )

    # ==========================================================
    # AI Fallback (RAG - retrieval + live infrastructure + LLM)
    # ==========================================================

    knowledge_chunks = retrieve_relevant_knowledge(
        query=question,
        db=db,
        current_user=current_user,
    )

    answer, sources = generate_ai_response(
        user_message=question,
        infrastructure_context=infrastructure_context,
        knowledge_chunks=knowledge_chunks,
        db=db,
        current_user=current_user,
    )

    return ChatResponse(
        answer=answer,
        sources=sources,
    )
