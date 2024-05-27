"""Models for the auth module."""
from sqlalchemy import Column, DateTime, Integer, String, func
from sqlalchemy.orm import relationship

from src.database import BaseModel


class User(BaseModel):
    """User model."""
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)

    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    updated_at = Column(DateTime, default=func.now, onupdate=func.now)
    created_at = Column(DateTime, default=func.now)

    memberships = relationship("Membership", back_populates="user")
