from sqlalchemy.orm import Session

from app.cloud.aws.resource_service import get_resource_summary
from app.infrastructure.schemas import (
    InfrastructureHealth,
    InfrastructureOverview,
    InfrastructureResource,
    InfrastructureSummary,
)
from app.models.user import User


def get_infrastructure_summary(
    db: Session,
    current_user: User,
) -> InfrastructureSummary:
    """
    Returns the infrastructure overview using live AWS resources.
    """

    resources = get_resource_summary(
        db=db,
        current_user=current_user,
    )

    ec2 = resources["ec2"]
    s3 = resources["s3"]
    rds = resources["rds"]
    ebs = resources["ebs"]
    lambda_functions = resources["lambda"]
    vpcs = resources["vpcs"]

    overview = InfrastructureOverview(
        cloud_providers=1,
        compute_instances=len(ec2),
        databases=len(rds),
        storage_buckets=len(s3),
    )

    infrastructure_resources = []

    for instance in ec2:
        infrastructure_resources.append(
            InfrastructureResource(
                title=instance["instance_id"],
                type="EC2 Instance",
                status=instance["state"].capitalize(),
                utilization="-",
                uptime="-",
            )
        )

    for database in rds:
        infrastructure_resources.append(
            InfrastructureResource(
                title=database.get("db_instance_identifier", "RDS Instance"),
                type="RDS",
                status=database.get("status", "Unknown").capitalize(),
                utilization="-",
                uptime="-",
            )
        )

    for bucket in s3:
        infrastructure_resources.append(
            InfrastructureResource(
                title=bucket["name"],
                type="S3 Bucket",
                status="Available",
                utilization="-",
                uptime="-",
            )
        )

    for volume in ebs:
        infrastructure_resources.append(
            InfrastructureResource(
                title=volume.get("volume_id", "EBS Volume"),
                type="EBS Volume",
                status=volume.get("state", "Available").capitalize(),
                utilization="-",
                uptime="-",
            )
        )

    for function in lambda_functions:
        infrastructure_resources.append(
            InfrastructureResource(
                title=function.get("function_name", "Lambda Function"),
                type="Lambda",
                status="Active",
                utilization="-",
                uptime="-",
            )
        )

    for vpc in vpcs:
        infrastructure_resources.append(
            InfrastructureResource(
                title=vpc.get("vpc_id", "VPC"),
                type="VPC",
                status="Available",
                utilization="-",
                uptime="-",
            )
        )

    total_resources = len(infrastructure_resources)

    overall_health = 100.0 if total_resources else 0.0

    health = InfrastructureHealth(
        overall_health=overall_health,
        average_cpu_usage=0,
        ai_recommendation=(
            "Infrastructure is connected successfully."
            if total_resources
            else "No AWS resources were discovered."
        ),
    )

    return InfrastructureSummary(
        overview=overview,
        resources=infrastructure_resources,
        health=health,
    )