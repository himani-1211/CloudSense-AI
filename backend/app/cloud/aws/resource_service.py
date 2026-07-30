from sqlalchemy.orm import Session

from app.cloud.aws.discovery import discover_resources
from app.models.user import User


def get_resource_summary(
    db: Session,
    current_user: User,
):
    """
    Discover AWS resources once and return a reusable summary.
    """

    resources = discover_resources(
        db=db,
        current_user=current_user,
    )

    return {
        "ec2": resources.get("ec2", []),
        "s3": resources.get("s3", []),
        "vpcs": resources.get("vpcs", []),
        "iam": resources.get("iam", []),
        "lambda": resources.get("lambda", []),
        "rds": resources.get("rds", []),
        "ebs": resources.get("ebs", []),
    }


def list_ec2_instances(
    db: Session,
    current_user: User,
):
    return get_resource_summary(
        db,
        current_user,
    )["ec2"]


def list_s3_buckets(
    db: Session,
    current_user: User,
):
    return get_resource_summary(
        db,
        current_user,
    )["s3"]


def list_vpcs(
    db: Session,
    current_user: User,
):
    return get_resource_summary(
        db,
        current_user,
    )["vpcs"]


def list_iam_users(
    db: Session,
    current_user: User,
):
    return get_resource_summary(
        db,
        current_user,
    )["iam"]


def list_lambda_functions(
    db: Session,
    current_user: User,
):
    return get_resource_summary(
        db,
        current_user,
    )["lambda"]


def list_rds_instances(
    db: Session,
    current_user: User,
):
    return get_resource_summary(
        db,
        current_user,
    )["rds"]


def list_ebs_volumes(
    db: Session,
    current_user: User,
):
    return get_resource_summary(
        db,
        current_user,
    )["ebs"]