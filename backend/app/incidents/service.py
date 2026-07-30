from sqlalchemy.orm import Session

from app.cloud.aws.resource_service import get_resource_summary
from app.incidents.schemas import (
    IncidentSummary,
    IncidentItem,
    CurrentPriority,
    IncidentsSummary,
)
from app.models.user import User


def get_incidents_summary(
    db: Session,
    current_user: User,
) -> IncidentsSummary:
    """
    Returns incidents derived from the current AWS infrastructure.
    """

    resources = get_resource_summary(
        db=db,
        current_user=current_user,
    )

    ec2 = resources["ec2"]
    rds = resources["rds"]
    s3 = resources["s3"]

    incidents = []

    for instance in ec2:
        state = instance.get("state", "").lower()

        if state != "running":
            incidents.append(
                IncidentItem(
                    severity="High",
                    title=f"EC2 Instance {instance['instance_id']} is {state}",
                    service="EC2",
                    status="Requires Review",
                    time="Just now",
                )
            )

    for database in rds:
        status = database.get("status", "").lower()

        if status not in ("available", "running"):
            incidents.append(
                IncidentItem(
                    severity="Critical",
                    title=f"RDS Instance {database.get('db_instance_identifier', 'Unknown')}",
                    service="RDS",
                    status=status.capitalize(),
                    time="Just now",
                )
            )

    summary = IncidentSummary(
        open=len(incidents),
        critical=sum(
            1 for incident in incidents
            if incident.severity == "Critical"
        ),
        resolved_today=0,
        average_resolution="-",
    )

    if incidents:
        first = incidents[0]

        current_priority = CurrentPriority(
            title=first.title,
            description="Generated from live AWS resource discovery.",
            impact=first.severity,
            impact_description=(
                "Review this resource to restore normal operation."
            ),
        )
    else:
        current_priority = CurrentPriority(
            title="No Active Incidents",
            description=(
                "CloudSense AI did not detect any infrastructure incidents."
            ),
            impact="Low",
            impact_description=(
                f"Monitoring {len(ec2)} EC2, {len(rds)} RDS and "
                f"{len(s3)} S3 resources."
            ),
        )

    return IncidentsSummary(
        summary=summary,
        incidents=incidents,
        current_priority=current_priority,
    )