from sqlalchemy.orm import Session

from app.cloud.aws.discovery import discover_resources
from app.cloud.aws.models import AWSAccount
from app.dashboard.schemas import (
    ActivityItem,
    AIInsight,
    DashboardCards,
    DashboardSummary,
    PriorityItem,
)
from app.models.user import User


def get_dashboard_summary(
    db: Session,
    current_user: User,
) -> DashboardSummary:
    """
    Returns the dashboard summary using live AWS data.
    """

    # Check whether the user has connected an AWS account.
    aws_account = (
        db.query(AWSAccount)
        .filter(AWSAccount.owner_id == current_user.id)
        .first()
    )

    connected_clouds = 1 if aws_account else 0

    priority_feed: list[PriorityItem] = []
    recent_activity: list[ActivityItem] = []

    ai_insights: list[AIInsight] = []

    if not aws_account:
        ai_insights.append(
            AIInsight(
                title="No Cloud Connected",
                description=(
                    "Connect your AWS account to start monitoring "
                    "your cloud infrastructure."
                ),
            )
        )

        return DashboardSummary(
            cards=DashboardCards(
                connected_clouds=0,
                platform_health=0.0,
                active_incidents=0,
                ai_confidence=0,
            ),
            priority_feed=priority_feed,
            recent_activity=recent_activity,
            ai_insights=ai_insights,
        )

    resources = discover_resources(
        db=db,
        current_user=current_user,
    )

    ec2_instances = len(resources.get("ec2", []))
    s3_buckets = len(resources.get("s3", []))
    rds_instances = len(resources.get("rds", []))
    lambda_functions = len(resources.get("lambda", []))
    vpcs = len(resources.get("vpcs", []))
    ebs_volumes = len(resources.get("ebs", []))

    total_resources = (
        ec2_instances
        + s3_buckets
        + rds_instances
        + lambda_functions
        + vpcs
        + ebs_volumes
    )

    # Temporary calculated health until monitoring is integrated.
    platform_health = 100.0

    if total_resources == 0:
        ai_insights.append(
            AIInsight(
                title="AWS Connected Successfully",
                description=(
                    "Your AWS account is connected, but no supported "
                    "resources were found in the selected region."
                ),
            )
        )
    else:
        ai_insights.append(
            AIInsight(
                title="Infrastructure Discovered",
                description=(
                    f"CloudSense AI discovered {total_resources} AWS "
                    "resources and is ready for monitoring."
                ),
            )
        )

    return DashboardSummary(
        cards=DashboardCards(
            connected_clouds=connected_clouds,
            platform_health=platform_health,
            active_incidents=0,
            ai_confidence=95,
        ),
        priority_feed=priority_feed,
        recent_activity=recent_activity,
        ai_insights=ai_insights,
    )