from pydantic import BaseModel


class OrganizationBase(BaseModel):
    """Organization base schema."""
    slug: str


class OrganizationCreate(OrganizationBase):
    """Organization create schema."""


class OrganizationUpdate(OrganizationBase):
    """Organization update schema."""


class Organization(OrganizationBase):
    """Organization schema."""
    id: int

    updated_at: str
    created_at: str

    clients: list[int]

    class Config:
        orm_mode = True
