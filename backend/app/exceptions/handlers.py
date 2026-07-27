from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.auth import (
    UserAlreadyExistsException,
    InvalidCredentialsException,
)
from app.core.logging import logger
from app.exceptions.cloud import InvalidAWSCredentialsException


async def user_already_exists_handler(
    request: Request,
    exc: UserAlreadyExistsException,
):
    logger.auth.warning(
        "Registration failed. User already exists."
    )

    return JSONResponse(
        status_code=409,
        content={
            "success": False,
            "message": "User with this email already exists.",
        },
    )


async def invalid_credentials_handler(
    request: Request,
    exc: InvalidCredentialsException,
):
    logger.auth.warning(
        "Login failed due to invalid credentials."
    )

    return JSONResponse(
        status_code=401,
        content={
            "success": False,
            "message": "Invalid email or password.",
        },
    )


async def generic_exception_handler(
    request: Request,
    exc: Exception,
):
    logger.error.exception(
        "Unhandled exception occurred."
    )

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Internal Server Error.",
        },
    )

async def invalid_aws_credentials_handler(
    request: Request,
    exc: InvalidAWSCredentialsException,
):
    logger.cloud.warning("AWS connection failed due to invalid credentials.")

    return JSONResponse(
        status_code=401,
        content={
            "success": False,
            "message": "Invalid AWS credentials.",
        },
    )