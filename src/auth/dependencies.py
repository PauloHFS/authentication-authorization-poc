import os
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from src.auth import dependencies, schemas, service
from src.dependencies import get_db

SECRET_KEY = os.getenv("SECRET_KEY")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/signin")


def get_current_user(token: Annotated[str, Depends(dependencies.oauth2_scheme)],
                     db: Session = Depends(get_db)):
    """Get the current user."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        print(token)
        payload = jwt.decode(token, SECRET_KEY)
        id: str = payload.get("sub")
        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id, email=payload.get("email"))
    except jwt.InvalidTokenError as e:
        raise credentials_exception from e
    db_user = service.get_user(db, user_id=token_data.sub)
    if db_user is None:
        raise credentials_exception
    return db_user
