from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.core.database import get_db
from app.models.user import User
from app.reports.schemas import ReportsSummary
from app.reports.service import get_reports_summary

router = APIRouter(
    prefix="/reports",
    tags=["Reports"],
)


@router.get(
    "/summary",
    response_model=ReportsSummary,
    summary="Get reports summary",
)
def reports_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> ReportsSummary:
    """
    Returns the reports overview for the authenticated user.
    """

    return get_reports_summary(
        db=db,
        current_user=current_user,
    )