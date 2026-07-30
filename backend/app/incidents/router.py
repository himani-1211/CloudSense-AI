from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.core.database import get_db
from app.incidents.schemas import IncidentsSummary
from app.incidents.service import get_incidents_summary
from app.models.user import User

router = APIRouter(
    prefix="/incidents",
    tags=["Incidents"],
)


@router.get(
    "/summary",
    response_model=IncidentsSummary,
    summary="Get incidents summary",
)
def incidents_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> IncidentsSummary:
    """
    Returns the incidents overview for the authenticated user.
    """

    return get_incidents_summary(
        db=db,
        current_user=current_user,
    )