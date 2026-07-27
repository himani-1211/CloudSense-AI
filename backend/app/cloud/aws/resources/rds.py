from sqlalchemy.orm import Session

from app.cloud.aws.credential_manager import get_authenticated_client
from app.models.user import User


def discover_rds_instances(
    db: Session,
    current_user: User,
):
    client = get_authenticated_client(
        service_name="rds",
        db=db,
        current_user=current_user,
    )

    response = client.describe_db_instances()

    instances = []

    for db_instance in response.get("DBInstances", []):
        instances.append(
            {
                "db_instance_identifier": db_instance["DBInstanceIdentifier"],
                "engine": db_instance["Engine"],
                "status": db_instance["DBInstanceStatus"],
            }
        )

    return instances