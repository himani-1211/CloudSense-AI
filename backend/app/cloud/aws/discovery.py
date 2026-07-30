from concurrent.futures import ThreadPoolExecutor
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
    """
    Discover all AWS resources in parallel.
    """

    with ThreadPoolExecutor(max_workers=7) as executor:
        futures = {
            "ec2": executor.submit(
                discover_ec2,
                db=db,
                current_user=current_user,
            ),
            "s3": executor.submit(
                discover_s3,
                db=db,
                current_user=current_user,
            ),
            "vpcs": executor.submit(
                discover_vpcs,
                db=db,
                current_user=current_user,
            ),
            "iam": executor.submit(
                discover_iam_users,
                db=db,
                current_user=current_user,
            ),
            "lambda": executor.submit(
                discover_lambda_functions,
                db=db,
                current_user=current_user,
            ),
            "rds": executor.submit(
                discover_rds_instances,
                db=db,
                current_user=current_user,
            ),
            "ebs": executor.submit(
                discover_ebs_volumes,
                db=db,
                current_user=current_user,
            ),
        }

        return {
            name: future.result()
            for name, future in futures.items()
        }