from sqlalchemy.orm import Session

from app.models.user import User

from app.cloud.aws.resources.ec2 import discover_ec2
from app.cloud.aws.resources.s3 import discover_s3
from app.cloud.aws.resources.vpc import discover_vpcs
from app.cloud.aws.resources.iam import discover_iam_users
from app.cloud.aws.resources.lambda_service import discover_lambda_functions
from app.cloud.aws.resources.rds import discover_rds_instances
from app.cloud.aws.resources.ebs import discover_ebs_volumes

def discover_resources(
    db: Session,
    current_user: User,
):
    return {
    "ec2": discover_ec2(
        db=db,
        current_user=current_user,
    ),
    "s3": discover_s3(
        db=db,
        current_user=current_user,
    ),
    "vpcs": discover_vpcs(
        db=db,
        current_user=current_user,
    ),
    "iam": discover_iam_users(
    db=db,
    current_user=current_user,
    ),
    "lambda": discover_lambda_functions(
        db=db,
        current_user=current_user,
    ),
    "rds": discover_rds_instances(
        db=db,
        current_user=current_user,
    ),
    "ebs": discover_ebs_volumes(
        db=db,
        current_user=current_user,
    ),
}