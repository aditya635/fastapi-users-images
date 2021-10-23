from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()
import cloudinary,cloudinary.uploader

cloudinary.config(
    cloud_name= os.environ["CLOUD_NAME"],
    api_key= os.environ["API_KEY"],
    api_secret =os.environ["API_SECRET"]
)

SQLALCHEMY_DATABASE_URL=os.environ["SQLALCHEMY_DATABASE_URL"]

engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()