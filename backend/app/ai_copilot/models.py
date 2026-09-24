from sqlalchemy import Column, DateTime, ForeignKey, Integer, JSON, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class CopilotMessage(Base):
    __tablename__ = "copilot_messages"

    id = Column(Integer, primary_key=True, index=True)

    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)

    role = Column(String(20), nullable=False)
    text = Column(Text, nullable=False)
    sources = Column(JSON, default=list)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), index=True)

    owner = relationship("User")
