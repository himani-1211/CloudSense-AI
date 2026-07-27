from sqlalchemy.orm import Session

from app.cloud.providers.base import CloudProvider
from app.models.user import User


class AzureProvider(CloudProvider):

    def discover_resources(
        self,
        db: Session,
        current_user: User,
    ):
        # Azure discovery will be implemented later
        return {}