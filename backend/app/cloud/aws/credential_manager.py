import boto3
from sqlalchemy.orm import Session

from app.cloud.aws.models import AWSAccount
from app.cloud.encryption import decrypt
from app.models.user import User


def get_authenticated_client(
    service_name: str,
    db: Session,
    current_user: User,
):
    aws_account = (
        db.query(AWSAccount)
        .filter(AWSAccount.owner_id == current_user.id)
        .first()
    )

    if aws_account is None:
        raise Exception("No AWS account connected.")

    return boto3.client(
        service_name=service_name,
        aws_access_key_id=aws_account.access_key,
        aws_secret_access_key=decrypt(
            aws_account.encrypted_secret_key
        ),
        region_name=aws_account.region,
    )