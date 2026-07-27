from cryptography.fernet import Fernet

from app.core.config import settings

cipher = Fernet(settings.ENCRYPTION_KEY.encode())


def encrypt(text: str) -> str:
    """
    Encrypt plain text.
    """
    return cipher.encrypt(text.encode()).decode()


def decrypt(encrypted_text: str) -> str:
    """
    Decrypt encrypted text.
    """
    return cipher.decrypt(encrypted_text.encode()).decode()