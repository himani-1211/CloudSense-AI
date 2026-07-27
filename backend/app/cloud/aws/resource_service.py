from sqlalchemy.orm import Session

from app.cloud.aws.discovery import discover_resources
from app.models.user import User


def list_ec2_instances(
    db: Session,
    current_user: User,
):
    resources = discover_resources(
        db=db,
        current_user=current_user,
    )

    return resources["ec2"]

def list_s3_buckets(
    db: Session,
    current_user: User,
):
    resources = discover_resources(
        db=db,
        current_user=current_user,
    )

    return resources["s3"]

def list_vpcs(
    db: Session,
    current_user: User,
):
    resources = discover_resources(
        db=db,
        current_user=current_user,
    )

    return resources["vpcs"]

def list_iam_users(
    db: Session,
    current_user: User,
):
    resources = discover_resources(
        db=db,
        current_user=current_user,
    )

    return resources["iam"]

def list_lambda_functions(
    db: Session,
    current_user: User,
):
    return discover_resources(db, current_user)["lambda"]


def list_rds_instances(
    db: Session,
    current_user: User,
):
    return discover_resources(db, current_user)["rds"]


def list_ebs_volumes(
    db: Session,
    current_user: User,
):
    return discover_resources(db, current_user)["ebs"]