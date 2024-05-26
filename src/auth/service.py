"""Service layer for the auth module."""
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.auth import models, schemas, util


def signin(db: Session,
           form_data: OAuth2PasswordRequestForm):
    """Signin a user and return a token."""
    db_user = db.query(models.User).filter(
        models.User.username == form_data.username).first()
    if not db_user:
        return None

    (is_password_valid, updated_hash) = util.verify_password(
        form_data.password, db_user.password)

    if not is_password_valid:
        return None

    if updated_hash:
        db_user.password = updated_hash
        db.commit()

    return db_user


def create_user(db: Session,
                user: schemas.UserCreate):
    """Create a new user."""
    hashed_password = util.get_password_hash(user.password)
    db_user = models.User(username=user.username, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session,
             user_id: int):
    """Get a user by id."""
    return db.query(models.User).filter(models.User.id == user_id).first()
