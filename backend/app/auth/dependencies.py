from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.auth.token_service import verify_access_token
from app.models.user import User
from app.exceptions.auth import InvalidCredentialsException

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    email = verify_access_token(token)

    if email is None:
        raise InvalidCredentialsException()

    user = db.query(User).filter(User.email == email).first()

    if user is None:
        raise InvalidCredentialsException()

    return user