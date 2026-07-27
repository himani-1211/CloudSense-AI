from sqlalchemy.orm import Session

from app.cloud.aws.credential_manager import get_authenticated_client
from app.models.user import User


def discover_ebs_volumes(
    db: Session,
    current_user: User,
):
    client = get_authenticated_client(
        service_name="ec2",
        db=db,
        current_user=current_user,
    )

    response = client.describe_volumes()

    volumes = []

    for volume in response.get("Volumes", []):
        volumes.append(
            {
                "volume_id": volume["VolumeId"],
                "size": volume["Size"],
                "state": volume["State"],
                "volume_type": volume["VolumeType"],
            }
        )

    return volumes