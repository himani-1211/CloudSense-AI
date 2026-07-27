from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserLogin
from app.core.security import hash_password, verify_password
from app.auth.token_service import create_access_token

from app.exceptions.auth import (
    UserAlreadyExistsException,
    InvalidCredentialsException,
)

from app.core.logging import logger


def create_user(db: Session, user: UserCreate):
    # Check if email already exists
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        logger.auth.warning(
            f"Duplicate registration attempt for email: {user.email}"
        )
        raise UserAlreadyExistsException()

    db_user = User(
        full_name=user.full_name,
        email=user.email,
        password_hash=hash_password(user.password),
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    logger.auth.info(
    f"New user registered successfully: {db_user.email}"
    )

    return db_user

def login_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()

    if not user:
        logger.auth.warning(
            f"Login failed. User not found: {email}"
        )
        raise InvalidCredentialsException()

    if not verify_password(password, user.password_hash):
        logger.auth.warning(
            f"Invalid password for user: {email}"
        )
        raise InvalidCredentialsException()

    token = create_access_token(
        {
            "sub": user.email
        }
    )

    logger.auth.info(
    f"User logged in successfully: {user.email}"
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }