from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.core.database import get_db
from app.infrastructure.schemas import InfrastructureSummary
from app.infrastructure.service import get_infrastructure_summary
from app.models.user import User

router = APIRouter(
    prefix="/infrastructure",
    tags=["Infrastructure"],
)


@router.get(
    "/summary",
    response_model=InfrastructureSummary,
    summary="Get infrastructure summary",
)
def infrastructure_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> InfrastructureSummary:
    """
    Returns the infrastructure overview for the authenticated user.
    """

    return get_infrastructure_summary(
        db=db,
        current_user=current_user,
    )