""""Sales models."""
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship

from src.database import BaseModel
from src.organization.models import Organization


class Client(BaseModel):
    """"Client model."""
    __tablename__ = "client"

    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, ForeignKey(
        "organization.id"), nullable=False)

    name = Column(String, unique=True, nullable=False)

    organization = relationship("organization", back_populates="clients")

    updated_at = Column(DateTime, default=func.now, onupdate=func.now)
    created_at = Column(DateTime, default=func.now)


Organization.clients = relationship("client", order_by=Client.id,
                                    back_populates="organization")


class Sale(BaseModel):
    """Sale model."""
    __tablename__ = "sale"

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("client.id"), nullable=False)

    description = Column(String, nullable=False)
    total = Column(Integer, nullable=False)

    client = relationship("client", back_populates="sales")

    updated_at = Column(DateTime, default=func.now, onupdate=func.now)
    created_at = Column(DateTime, default=func.now)


Client.sales = relationship("sale", order_by=Sale.id, back_populates="client")
