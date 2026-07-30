from botocore.exceptions import ClientError, NoCredentialsError
from sqlalchemy.orm import Session

from app.cloud.aws.client import get_aws_client
from app.cloud.aws.models import AWSAccount
from app.cloud.aws.schemas import (
    AWSConnectRequest,
    AWSConnectResponse,
)
from app.cloud.encryption import encrypt
from app.exceptions.cloud import InvalidAWSCredentialsException
from app.models.user import User


def connect_aws(
    data: AWSConnectRequest,
    db: Session,
    current_user: User,
) -> AWSConnectResponse:
    try:
        sts = get_aws_client(
            service_name="sts",
            access_key=data.access_key,
            secret_key=data.secret_key,
            region=data.region,
        )

        identity = sts.get_caller_identity()

        account_id = identity["Account"]
        user_arn = identity["Arn"]

        # Check if this AWS account is already connected
        existing_account = (
            db.query(AWSAccount)
            .filter(
                AWSAccount.account_id == account_id,
                AWSAccount.owner_id == current_user.id,
            )
            .first()
        )

        if existing_account is None:
            aws_account = AWSAccount(
                account_id=account_id,
                user_arn=user_arn,
                access_key=data.access_key,
                encrypted_secret_key=encrypt(data.secret_key),
                region=data.region,
                owner_id=current_user.id,
            )

            db.add(aws_account)
            db.commit()

        return AWSConnectResponse(
            account_id=account_id,
            user_arn=user_arn,
            region=data.region,
            message="AWS connection successful.",
        )

    except (ClientError, NoCredentialsError):
        raise InvalidAWSCredentialsException()

def get_aws_status(
    db: Session,
    current_user: User,
):
    account = (
        db.query(AWSAccount)
        .filter(AWSAccount.owner_id == current_user.id)
        .first()
    )

    return {
        "connected": account is not None
    }