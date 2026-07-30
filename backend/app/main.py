from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.core.database import engine, Base
from app.models.user import User

from app.auth.router import router as auth_router
from app.dashboard.router import router as dashboard_router
from app.operations.router import router as operations_router
from app.incidents.router import router as incidents_router
from app.infrastructure.router import router as infrastructure_router
from app.integrations.router import router as integrations_router
from app.ai_copilot.router import router as ai_copilot_router
from app.reports.router import router as reports_router
from app.settings.router import router as settings_router

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

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(aws_router)
app.include_router(dashboard_router)
app.include_router(operations_router)
app.include_router(incidents_router)
app.include_router(infrastructure_router)
app.include_router(integrations_router)
app.include_router(ai_copilot_router)
app.include_router(reports_router)
app.include_router(settings_router)

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