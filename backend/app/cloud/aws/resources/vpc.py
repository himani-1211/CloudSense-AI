from sqlalchemy.orm import Session

from app.cloud.aws.credential_manager import get_authenticated_client
from app.models.user import User


def discover_vpcs(
    db: Session,
    current_user: User,
):
    ec2 = get_authenticated_client(
        service_name="ec2",
        db=db,
        current_user=current_user,
    )

    response = ec2.describe_vpcs()

    vpcs = []

    for vpc in response.get("Vpcs", []):
        vpcs.append(
            {
                "vpc_id": vpc["VpcId"],
                "cidr_block": vpc["CidrBlock"],
                "state": vpc["State"],
                "is_default": vpc["IsDefault"],
            }
        )

    return vpcs