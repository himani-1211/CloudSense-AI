from sqlalchemy.orm import Session

from app.cloud.aws.models import AWSAccount
from app.integrations.schemas import (
    AIRecommendation,
    IntegrationItem,
    IntegrationSummary,
    IntegrationsSummary,
)
from app.models.user import User


def get_integrations_summary(
    db: Session,
    current_user: User,
) -> IntegrationsSummary:
    """
    Returns the integrations overview for the authenticated user.
    """

    aws_account = (
        db.query(AWSAccount)
        .filter(AWSAccount.owner_id == current_user.id)
        .first()
    )

    integrations = [
        IntegrationItem(
            name="Amazon Web Services",
            category="Cloud Provider",
            status="Connected" if aws_account else "Not Connected",
        ),
        IntegrationItem(
            name="Microsoft Azure",
            category="Cloud Provider",
            status="Coming Soon",
        ),
        IntegrationItem(
            name="Google Cloud",
            category="Cloud Provider",
            status="Coming Soon",
        ),
        IntegrationItem(
            name="Oracle Cloud",
            category="Cloud Provider",
            status="Coming Soon",
        ),
    ]

    connected = sum(
        integration.status == "Connected"
        for integration in integrations
    )

    summary = IntegrationSummary(
        connected=connected,
        available=len(integrations),
        healthy=connected,
        sync_rate="100%" if connected else "0%",
    )

    if aws_account:
        ai_recommendation = AIRecommendation(
            title="AWS Connected Successfully",
            description=(
                "Your AWS account is connected and ready for monitoring. "
                "CloudSense AI is currently optimized for AWS. "
                "Support for Microsoft Azure, Google Cloud and Oracle Cloud "
                "will be available in upcoming releases."
            ),
        )
    else:
        ai_recommendation = AIRecommendation(
            title="Connect AWS",
            description=(
                "Connect your AWS account to enable infrastructure discovery, "
                "operations monitoring, AI-powered insights and reporting. "
                "Additional cloud providers will be supported in future updates."
            ),
        )

    return IntegrationsSummary(
        summary=summary,
        integrations=integrations,
        ai_recommendation=ai_recommendation,
    )