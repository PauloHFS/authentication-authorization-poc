"""Organization models."""
from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer, String,
                        func)
from sqlalchemy.orm import relationship

from src.database import BaseModel


class Organization(BaseModel):
    """Organization model."""
    __tablename__ = "organization"

    id = Column(Integer, primary_key=True)

    slug = Column(String, unique=True, nullable=False)

    updated_at = Column(DateTime, default=func.now, onupdate=func.now)
    created_at = Column(DateTime, default=func.now)

    clients = relationship(
        "Client", back_populates="organization", order_by="client.id")


class Role(BaseModel):
    """Role model."""
    __tablename__ = "role"

    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, ForeignKey(
        "organization.id"), nullable=False)

    name = Column(String, nullable=False)

    updated_at = Column(DateTime, default=func.now, onupdate=func.now)
    created_at = Column(DateTime, default=func.now)

    organization = relationship("Organization", back_populates="roles")
    permissions = relationship(
        "Permission", back_populates="role", order_by="permission.id")


class Membership(BaseModel):
    """Membership model."""
    __tablename__ = "membership"

    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    organization_id = Column(Integer, ForeignKey("user.id"), primary_key=True,)
    role_id = Column(Integer, ForeignKey("role.id"), nullable=False)

    updated_at = Column(DateTime, default=func.now, onupdate=func.now)
    created_at = Column(DateTime, default=func.now)

    user = relationship("User", back_populates="memberships")
    organization = relationship("Organization", back_populates="memberships")
    role = relationship("Role", back_populates="memberships")


class Permission(BaseModel):
    """Permission model."""
    __tablename__ = "permission"

    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey("role.id"), nullable=False)

    resource = Column(String, nullable=False)
    can_create = Column(Boolean, nullable=False)
    can_read = Column(Boolean, nullable=False)
    can_update = Column(Boolean, nullable=False)
    can_delete = Column(Boolean, nullable=False)

    updated_at = Column(DateTime, default=func.now, onupdate=func.now)
    created_at = Column(DateTime, default=func.now)

    role = relationship("Role", back_populates="permissions")

    def __repr__(self):
        return f"<Permission#{self.id} - {self.resource} - C[{self.can_create}]R[{self.can_read}]|U[{self.can_update}]|D[{self.can_delete}]>"
