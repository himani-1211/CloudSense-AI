from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.core.database import get_db
from app.models.user import User
from app.operations.schemas import OperationsSummary
from app.operations.service import get_operations_summary

router = APIRouter(
    prefix="/operations",
    tags=["Operations"],
)


@router.get(
    "/summary",
    response_model=OperationsSummary,
    summary="Get operations summary",
)
def operations_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> OperationsSummary:
    """
    Returns the operations overview for the authenticated user.

    Includes:
    - AI Operations Summary
    - Operations Timeline
    - AI Correlation
    - Recommended Actions
    """
    return get_operations_summary(
        db=db,
        current_user=current_user,
    )