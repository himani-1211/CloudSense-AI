from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.core.database import get_db
from app.integrations.schemas import IntegrationsSummary
from app.integrations.service import get_integrations_summary
from app.models.user import User

router = APIRouter(
    prefix="/integrations",
    tags=["Integrations"],
)


@router.get(
    "/summary",
    response_model=IntegrationsSummary,
    summary="Get integrations summary",
)
def integrations_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> IntegrationsSummary:
    """
    Returns the integrations overview for the authenticated user.
    """

    return get_integrations_summary(
        db=db,
        current_user=current_user,
    )