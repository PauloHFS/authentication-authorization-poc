"""Router for authentication."""
import os
from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.auth import schemas, service, util
from src.auth.dependencies import get_current_user
from src.dependencies import get_db

SECRET_KEY = os.getenv("SECRET_KEY")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@router.post('/signin', response_model=schemas.Token)
def signin(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
           db: Session = Depends(get_db)) -> schemas.Token:
    """Signin a user and return a token."""
    user = service.signin(db, form_data)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))

    access_token = util.create_access_token(
        data={"sub": user.id, "username": user.email}, expires_delta=access_token_expires
    )

    return schemas.Token(access_token=access_token, token_type="bearer")


@router.post('/signup', response_model=schemas.User)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """Create a new user."""
    db_user = service.create_user(db, user)
    return db_user


@ router.get("/me", response_model=schemas.User)
async def read_users_me(
    current_user: Annotated[schemas.User, Depends(get_current_user)],
):
    """Endpoint to get the current user."""
    return current_user
