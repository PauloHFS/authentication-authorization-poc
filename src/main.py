from typing import Union

from fastapi import FastAPI

from src.auth.router import router as auth_router
from src.database import BaseModel, engine

BaseModel.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router)
