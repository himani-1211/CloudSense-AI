from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.core.database import get_db
from app.dashboard.schemas import DashboardSummary
from app.dashboard.service import get_dashboard_summary
from app.models.user import User

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get(
    "/summary",
    response_model=DashboardSummary,
    summary="Get dashboard summary",
)
def dashboard_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> DashboardSummary:
    """
    Returns the dashboard summary for the authenticated user.

    Includes:
    - Dashboard cards
    - Priority feed
    - Recent activity
    - AI insights
    """
    return get_dashboard_summary(
        db=db,
        current_user=current_user,
    )