from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base


class AWSAccount(Base):
    __tablename__ = "aws_accounts"

    id = Column(Integer, primary_key=True, index=True)

    account_id = Column(String, nullable=False)
    user_arn = Column(String, nullable=False)

    access_key = Column(String, nullable=False)
    encrypted_secret_key = Column(String, nullable=False)

    region = Column(String, nullable=False)

    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship(
    "User",
    back_populates="aws_accounts",
)