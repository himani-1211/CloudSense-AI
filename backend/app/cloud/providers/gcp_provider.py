from sqlalchemy.orm import Session

from app.cloud.providers.base import CloudProvider
from app.models.user import User


class GCPProvider(CloudProvider):

    def discover_resources(
        self,
        db: Session,
        current_user: User,
    ):
        # GCP discovery will be implemented later
        return {}