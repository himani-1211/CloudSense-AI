from sqlalchemy.orm import Session

from app.cloud.aws.discovery import discover_resources
from app.cloud.providers.base import CloudProvider
from app.models.user import User


class AWSProvider(CloudProvider):

    def discover_resources(
        self,
        db: Session,
        current_user: User,
    ):
        return discover_resources(
            db=db,
            current_user=current_user,
        )