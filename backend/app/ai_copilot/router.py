from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.ai_copilot.schemas import (
    CopilotSummary,
    ChatRequest,
    ChatResponse,
)
from app.ai_copilot.service import (
    get_copilot_summary,
    chat_with_copilot,
)
from app.auth.dependencies import get_current_user
from app.core.database import get_db
from app.models.user import User

router = APIRouter(
    prefix="/ai-copilot",
    tags=["AI Copilot"],
)


@router.get(
    "/summary",
    response_model=CopilotSummary,
    summary="Get AI Copilot summary",
)
def copilot_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> CopilotSummary:
    """
    Returns the AI Copilot overview.
    """
    return get_copilot_summary(
        db=db,
        current_user=current_user,
    )


@router.post(
    "/chat",
    response_model=ChatResponse,
    summary="Chat with AI Copilot",
)
def copilot_chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> ChatResponse:
    """
    Sends a user message to the AI Copilot and returns an AI response.
    """
    return chat_with_copilot(
        request=request,
        db=db,
        current_user=current_user,
    )