from app.cloud.aws.credential_manager import get_authenticated_client
from app.models.user import User
from sqlalchemy.orm import Session


def discover_ec2(
    db: Session,
    current_user: User,
):
    ec2 = get_authenticated_client(
        service_name="ec2",
        db=db,
        current_user=current_user,
    )

    response = ec2.describe_instances()

    instances = []

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instances.append(
                {
                    "instance_id": instance["InstanceId"],
                    "state": instance["State"]["Name"],
                    "instance_type": instance["InstanceType"],
                }
            )

    return instances