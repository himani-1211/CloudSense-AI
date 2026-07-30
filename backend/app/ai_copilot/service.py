from sqlalchemy.orm import Session

from app.ai_copilot.llm import generate_ai_response
from app.ai_copilot.prompts import build_context
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


def get_copilot_summary(
    db: Session,
    current_user: User,
) -> CopilotSummary:
    """
    Returns AI Copilot overview using live AWS resources.
    """

    resources = get_resource_summary(
        db=db,
        current_user=current_user,
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

    conversation = [
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
            description="Analyze your AWS infrastructure in real time.",
        ),
        Capability(
            title="Security Recommendations",
            description="Receive AWS security best-practice suggestions.",
        ),
        Capability(
            title="Cost Optimization",
            description="Identify opportunities to reduce cloud costs.",
        ),
    ]

    return CopilotSummary(
        suggested_questions=suggested_questions,
        conversation=conversation,
        response=response,
        capabilities=capabilities,
    )


def chat_with_copilot(
    request: ChatRequest,
    db: Session,
    current_user: User,
) -> ChatResponse:
    """
    Handles AI Copilot chat requests.
    """

    resources = get_resource_summary(
        db=db,
        current_user=current_user,
    )

    ec2 = resources["ec2"]
    s3 = resources["s3"]
    rds = resources["rds"]
    lambda_functions = resources["lambda"]
    ebs = resources["ebs"]
    vpcs = resources["vpcs"]

    context = build_context(
        ec2_count=len(ec2),
        s3_count=len(s3),
        rds_count=len(rds),
        lambda_count=len(lambda_functions),
        ebs_count=len(ebs),
        vpc_count=len(vpcs),
    )

    answer, sources = generate_ai_response(
        user_message=request.message,
        context=context,
    )

    return ChatResponse(
        answer=answer,
        sources=sources,
    )