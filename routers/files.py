from fastapi import APIRouter,Depends,HTTPException,UploadFile,File,Body,Form
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.functions import mode
from enum import Enum
import schemas,models
from database import SessionLocal, engine
from passlib.context import CryptContext
import hashing
from database import get_db
import oauth2,cloudinary
from typing import List
from schemas import Caption

router = APIRouter(prefix='/files')

@router.post('/',response_model=schemas.File,tags=['file'])
def upload(cap:str = Form(...) , file: UploadFile = File(...) ,db: Session = Depends(get_db), get_current_user: schemas.TokenData = Depends (oauth2.get_current_user)):
    result = cloudinary.uploader.upload(file.file)
    url = result.get("url")
    new_image = models.Images(caption=cap, url= url , user_id = get_current_user.id)
    db.add(new_image)
    db.commit()
    db.refresh(new_image)
    return new_image

@router.get('/',response_model= List[schemas.File],tags=['file'])
def getfile(db: Session = Depends(get_db)):
    return db.query(models.Images).all()