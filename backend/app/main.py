from fastapi import FastAPI
from sqlalchemy import text

from app.core.database import engine, Base
from app.models.user import User
from app.auth.router import router as auth_router

from app.exceptions.auth import (
    UserAlreadyExistsException,
    InvalidCredentialsException,
)

from app.exceptions.handlers import (
    user_already_exists_handler,
    invalid_credentials_handler,
    generic_exception_handler,
    invalid_aws_credentials_handler,
)

from app.cloud.aws.router import router as aws_router
from app.exceptions.cloud import InvalidAWSCredentialsException


app = FastAPI(title="CloudSense AI")

app.add_exception_handler(
    UserAlreadyExistsException,
    user_already_exists_handler,
)

app.add_exception_handler(
    InvalidCredentialsException,
    invalid_credentials_handler,
)

app.add_exception_handler(
    Exception,
    generic_exception_handler,
)

app.add_exception_handler(
    InvalidAWSCredentialsException,
    invalid_aws_credentials_handler,
)

app.include_router(auth_router)
app.include_router(aws_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to CloudSense AI",
        "status": "running"
    }


@app.get("/health")
def health_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {
            "status": "healthy",
            "database": "connected"
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "database": str(e)
        }