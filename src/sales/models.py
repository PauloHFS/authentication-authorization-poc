""""Sales models."""
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship

from src.database import BaseModel


class Client(BaseModel):
    """"Client model."""
    __tablename__ = "client"

    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, ForeignKey(
        "organization.id"), nullable=False)

    name = Column(String, unique=True, nullable=False)

    organization = relationship(
        "Organization", back_populates="clients")
    sales = relationship("Sale", back_populates="client", order_by="sale.id")

    updated_at = Column(DateTime, default=func.now, onupdate=func.now)
    created_at = Column(DateTime, default=func.now)


class Sale(BaseModel):
    """Sale model."""
    __tablename__ = "sale"

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("client.id"), nullable=False)

    description = Column(String, nullable=False)
    total = Column(Integer, nullable=False)

    client = relationship("Client", back_populates="sales")

    updated_at = Column(DateTime, default=func.now, onupdate=func.now)
    created_at = Column(DateTime, default=func.now)
