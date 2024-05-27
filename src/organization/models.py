"""Organization models."""

# disable this cause of func.now()
# pylint: disable=not-callable

from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer, String,
                        func)
from sqlalchemy.orm import relationship

from src.database import BaseModel
from src.sales.models import Client  # don't remove this import


class Organization(BaseModel):
    """Organization model."""
    __tablename__ = "organization"

    id = Column(Integer, primary_key=True)

    slug = Column(String, unique=True, nullable=False)

    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    created_at = Column(DateTime, default=func.now())

    roles = relationship("Role", back_populates="organization",
                         foreign_keys="Role.organization_id")

    memberships = relationship(
        "Membership", back_populates="organization", foreign_keys="Membership.organization_id")

    clients = relationship(
        "Client", back_populates="organization", foreign_keys="Client.organization_id")


class Role(BaseModel):
    """Role model."""
    __tablename__ = "role"

    id = Column(Integer, primary_key=True)

    organization_id = Column(Integer, ForeignKey(
        "organization.id"), nullable=False)
    organization = relationship("Organization", back_populates="roles")

    name = Column(String, nullable=False)

    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    created_at = Column(DateTime, default=func.now())

    permissions = relationship(
        "Permission", back_populates="role", foreign_keys="Permission.role_id")

    memberships = relationship(
        "Membership", back_populates="role", foreign_keys="Membership.role_id")


class Membership(BaseModel):
    """Membership model."""
    __tablename__ = "membership"

    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    user = relationship("User", back_populates="memberships",
                        foreign_keys="Membership.user_id")

    organization_id = Column(Integer, ForeignKey(
        "organization.id"), primary_key=True,)
    organization = relationship(
        "Organization", back_populates="memberships", foreign_keys="Membership.organization_id")

    role_id = Column(Integer, ForeignKey("role.id"), nullable=False)
    role = relationship("Role", back_populates="memberships",
                        foreign_keys="Membership.role_id")

    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    created_at = Column(DateTime, default=func.now())


class Permission(BaseModel):
    """Permission model."""
    __tablename__ = "permission"

    id = Column(Integer, primary_key=True)

    role_id = Column(Integer, ForeignKey("role.id"), nullable=False)
    role = relationship("Role", back_populates="permissions")

    resource = Column(String, nullable=False)
    can_create = Column(Boolean, nullable=False)
    can_read = Column(Boolean, nullable=False)
    can_update = Column(Boolean, nullable=False)
    can_delete = Column(Boolean, nullable=False)

    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    created_at = Column(DateTime, default=func.now())

    def __repr__(self):
        return f"<Permission#{self.id} - {self.resource} - C[{self.can_create}]R[{self.can_read}]|U[{self.can_update}]|D[{self.can_delete}]>"
