'''Start of the app'''
from fastapi import FastAPI
import models
from database import SessionLocal, engine, get_db
from passlib.context import CryptContext
from routers import user,authentication,files


app = FastAPI()

models.Base.metadata.create_all(engine)


app.include_router(files.router)
app.include_router(user.router)
app.include_router(authentication.router)