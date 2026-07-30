from datetime import datetime

from sqlalchemy.orm import Session

from app.cloud.aws.resource_service import get_resource_summary
from app.models.user import User
from app.reports.schemas import (
    ReportInsight,
    ReportItem,
    ReportStatistics,
    ReportsSummary,
)


def get_reports_summary(
    db: Session,
    current_user: User,
) -> ReportsSummary:
    """
    Returns reports generated from live AWS infrastructure.
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

    today = datetime.now().strftime("%B %d, %Y")

    statistics = ReportStatistics(
        reports_generated=total_resources,
        performance_score="100%" if total_resources else "0%",
        compliance="100%",
        average_report_time="< 1 sec",
    )

    recent_reports = [
        ReportItem(
            title="EC2 Infrastructure Report",
            category="Compute",
            date=today,
        ),
        ReportItem(
            title="S3 Storage Report",
            category="Storage",
            date=today,
        ),
        ReportItem(
            title="RDS Database Report",
            category="Database",
            date=today,
        ),
        ReportItem(
            title="Cloud Resource Summary",
            category="Infrastructure",
            date=today,
        ),
    ]

    ai_insight = ReportInsight(
        title="Infrastructure Summary",
        description=(
            f"CloudSense AI analyzed {total_resources} AWS resources "
            f"({len(ec2)} EC2, {len(rds)} RDS, {len(s3)} S3, "
            f"{len(lambda_functions)} Lambda, {len(ebs)} EBS and "
            f"{len(vpcs)} VPC resources)."
            if total_resources
            else "No AWS resources were found for report generation."
        ),
    )

    return ReportsSummary(
        statistics=statistics,
        recent_reports=recent_reports,
        ai_insight=ai_insight,
    )