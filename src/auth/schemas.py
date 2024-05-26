"""Pydantic shemas for the auth module."""
from pydantic import BaseModel


# >>>>>>>>>> User schemas >>>>>>>>>>
class UserBase(BaseModel):
    """User base schema."""
    username: str


class UserCreate(UserBase):
    """User create schema."""
    password: str


class User(UserBase):
    """User schema."""
    id: int

    class Config:
        """Pydantic config."""
        orm_mode = True
# <<<<<<<<<< User schemas <<<<<<<<<<


# >>>>>>>>>> Token schemas >>>>>>>>>>
class Token(BaseModel):
    """Token schema."""
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """Token data schema."""
    sub: int | None = None
    username: str | None = None
# <<<<<<<<<< Token schemas <<<<<<<<<<
