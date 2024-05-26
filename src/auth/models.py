"""Models for the auth module."""
from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer, String,
                        func)
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

    memberships = relationship("membership", back_populates="user")


class Organization(BaseModel):
    """Organization model."""
    __tablename__ = "organization"

    id = Column(Integer, primary_key=True)

    slug = Column(String, unique=True, nullable=False)

    updated_at = Column(DateTime, default=func.now, onupdate=func.now)
    created_at = Column(DateTime, default=func.now)

    clients = relationship("client", back_populates="organization")


class Role(BaseModel):
    """Role model."""
    __tablename__ = "role"

    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, ForeignKey(
        "organization.id"), nullable=False)

    name = Column(String, nullable=False)

    updated_at = Column(DateTime, default=func.now, onupdate=func.now)
    created_at = Column(DateTime, default=func.now)

    organization = relationship("organization", back_populates="roles")


Organization.roles = relationship("role", order_by=Role.id,
                                  back_populates="organization")


class Membership(BaseModel):
    """Membership model."""
    __tablename__ = "membership"

    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    organization_id = Column(Integer, ForeignKey("user.id"), primary_key=True,)
    role_id = Column(Integer, ForeignKey("role.id"), nullable=False)

    updated_at = Column(DateTime, default=func.now, onupdate=func.now)
    created_at = Column(DateTime, default=func.now)

    user = relationship("user", back_populates="memberships")
    organization = relationship("organization", back_populates="memberships")
    role = relationship("role", back_populates="memberships")


User.memberships = relationship("membership", order_by=Membership.organization_id,
                                back_populates="user")
Organization.memberships = relationship("membership", order_by=Membership.user_id,
                                        back_populates="organization")
Role.memberships = relationship("membership", order_by=Membership.role_id,
                                back_populates="role")


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

    role = relationship("role", back_populates="permissions")

    def __repr__(self):
        return f"<Permission#{self.id} - {self.resource} - C[{self.can_create}]R[{self.can_read}]|U[{self.can_update}]|D[{self.can_delete}]>"


Role.permissions = relationship("permission", order_by=Permission.id,
                                back_populates="role")
