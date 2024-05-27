from pydantic import BaseModel


class ClientBase(BaseModel):
    """Client base schema."""
    name: str
