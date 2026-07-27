import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)


LOG_FORMAT = (
    "%(asctime)s | "
    "%(levelname)s | "
    "%(name)s | "
    "%(filename)s:%(lineno)d | "
    "%(message)s"
)


def _create_logger(logger_name: str, file_name: str):
    logger = logging.getLogger(logger_name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(LOG_FORMAT)

    # Console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File
    file_handler = RotatingFileHandler(
        LOG_DIR / file_name,
        maxBytes=5 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


class LoggerManager:
    def __init__(self):
        self.app = _create_logger("app", "app.log")
        self.auth = _create_logger("auth", "auth.log")
        self.cloud = _create_logger("cloud", "cloud.log")
        self.ai = _create_logger("ai", "ai.log")
        self.error = _create_logger("error", "error.log")


logger = LoggerManager()