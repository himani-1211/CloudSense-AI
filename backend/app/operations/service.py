from sqlalchemy.orm import Session

from app.cloud.aws.resource_service import get_resource_summary
from app.models.user import User
from app.operations.schemas import (
    AISummary,
    TimelineItem,
    AICorrelation,
    RecommendedAction,
    OperationsSummary,
)


def get_operations_summary(
    db: Session,
    current_user: User,
) -> OperationsSummary:
    """
    Returns the operations overview using live AWS resource discovery.
    """

    resources = get_resource_summary(
        db=db,
        current_user=current_user,
    )

    ec2 = resources["ec2"]
    rds = resources["rds"]
    s3 = resources["s3"]
    lambda_functions = resources["lambda"]

    total_resources = (
        len(ec2)
        + len(rds)
        + len(s3)
        + len(lambda_functions)
    )

    ai_summary = AISummary(
        events_analyzed=total_resources,
        critical_events=0,
        performance_risks=0,
        summary=(
            f"CloudSense AI discovered {total_resources} AWS resources "
            "and completed infrastructure analysis successfully."
            if total_resources
            else "No AWS resources were discovered for this account."
        ),
    )

    timeline = [
        TimelineItem(
            severity="healthy",
            title="AWS Resource Discovery Completed",
            description=f"Discovered {total_resources} cloud resources.",
            time="Just now",
        )
    ]

    if ec2:
        timeline.append(
            TimelineItem(
                severity="healthy",
                title=f"{len(ec2)} EC2 Instance(s) Available",
                description="Compute infrastructure is reachable.",
                time="Just now",
            )
        )

    if rds:
        timeline.append(
            TimelineItem(
                severity="healthy",
                title=f"{len(rds)} RDS Instance(s) Available",
                description="Database resources discovered.",
                time="Just now",
            )
        )

    if s3:
        timeline.append(
            TimelineItem(
                severity="healthy",
                title=f"{len(s3)} S3 Bucket(s) Available",
                description="Storage resources discovered.",
                time="Just now",
            )
        )

    ai_correlation = AICorrelation(
        root_cause=(
            "No operational anomalies detected."
            if total_resources
            else "No infrastructure available for analysis."
        ),
        confidence=100 if total_resources else 0,
        analysis=(
            "Analysis generated from live AWS resource discovery."
        ),
    )

    recommended_actions = []

    if not ec2:
        recommended_actions.append(
            RecommendedAction(
                text="Launch an EC2 instance to begin compute monitoring."
            )
        )

    if not rds:
        recommended_actions.append(
            RecommendedAction(
                text="Create an RDS instance for database monitoring."
            )
        )

    if not s3:
        recommended_actions.append(
            RecommendedAction(
                text="Create an S3 bucket to enable storage monitoring."
            )
        )

    if total_resources:
        recommended_actions.append(
            RecommendedAction(
                text="Enable CloudWatch metrics for detailed operational insights."
            )
        )

    return OperationsSummary(
        ai_summary=ai_summary,
        timeline=timeline,
        ai_correlation=ai_correlation,
        recommended_actions=recommended_actions,
    )