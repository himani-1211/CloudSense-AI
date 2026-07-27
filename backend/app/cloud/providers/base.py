from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

from app.models.user import User


class CloudProvider(ABC):

    @abstractmethod
    def discover_resources(
        self,
        db: Session,
        current_user: User,
    ):
        """
        Discover all cloud resources for the authenticated user.
        """
        pass