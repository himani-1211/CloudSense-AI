from sqlalchemy.orm import Session

from app.cloud.aws.credential_manager import get_authenticated_client
from app.models.user import User


def discover_s3(
    db: Session,
    current_user: User,
):
    s3 = get_authenticated_client(
        service_name="s3",
        db=db,
        current_user=current_user,
    )

    response = s3.list_buckets()

    buckets = []

    for bucket in response.get("Buckets", []):
        buckets.append(
            {
                "name": bucket["Name"],
                "creation_date": bucket["CreationDate"],
            }
        )

    return buckets