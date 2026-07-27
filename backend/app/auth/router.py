from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.user import (
    UserCreate,
    UserResponse,
    Token,
)

from app.auth.service import (
    create_user,
    login_user,
)

from app.auth.dependencies import get_current_user
from app.models.user import User
from app.schemas.user import UserResponse
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201
)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(db, user)
  

@router.post(
    "/login",
    response_model=Token,
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    return login_user(
        db,
        form_data.username,
        form_data.password,
    )

@router.get("/me", response_model=UserResponse)
def get_me(
    current_user: User = Depends(get_current_user),
):
    return current_user