from datetime import timedelta
from typing import Annotated

from fastapi import (APIRouter, Depends, FastAPI, HTTPException, Response,
                     status)
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..dependencies import get_db
from . import schemas, service, util

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)
ACCESS_TOKEN_EXPIRE_MINUTES = 30


@router.post('/signin', response_model=schemas.Token)
def signin(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)) -> schemas.Token:
    user = service.signin(db, form_data)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = util.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

    return schemas.Token(access_token=access_token, token_type="bearer")


@router.post('/signup', response_model=schemas.User)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = service.create_user(db, user)
    return db_user
