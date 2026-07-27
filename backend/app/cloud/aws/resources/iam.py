from sqlalchemy.orm import Session

from app.cloud.aws.credential_manager import get_authenticated_client
from app.models.user import User


def discover_iam_users(
    db: Session,
    current_user: User,
):
    iam = get_authenticated_client(
        service_name="iam",
        db=db,
        current_user=current_user,
    )

    response = iam.list_users()

    users = []

    for user in response.get("Users", []):
        users.append(
            {
                "user_name": user["UserName"],
                "user_id": user["UserId"],
                "arn": user["Arn"],
                "create_date": user["CreateDate"],
            }
        )

    return users