from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.core.database import get_db
from app.models.user import User
from app.settings.schemas import SettingsSummary
from app.settings.service import get_settings_summary

router = APIRouter(
    prefix="/settings",
    tags=["Settings"],
)


@router.get(
    "/summary",
    response_model=SettingsSummary,
    summary="Get settings summary",
)
def settings_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> SettingsSummary:
    """
    Returns the settings overview for the authenticated user.
    """

    return get_settings_summary(
        db=db,
        current_user=current_user,
    )