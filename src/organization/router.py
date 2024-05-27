from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.auth.dependencies import get_current_user
from src.auth.schemas import User as UserSchema
from src.dependencies import get_db
from src.organization import schemas, service

router = APIRouter(
    prefix="/organization",
    tags=["organization"],
    responses={404: {"description": "Not found"}},
)


@ router.post("/")
def create_organization(
    organization: schemas.OrganizationCreate,
    current_user: Annotated[UserSchema, Depends(get_current_user)],
    db: Session = Depends(get_db)

):
    """Create an organization."""
    return service.create_organization(db, current_user, organization)
