from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.functions import mode
from enum import Enum
import schemas,models
from database import SessionLocal, engine
from passlib.context import CryptContext
import hashing
from database import get_db
import oauth2

router = APIRouter(prefix='/user')

@router.post('/',response_model= schemas.ShowUser,tags=['user'])
def create_user(request:schemas.User, db:Session = Depends(get_db)):
    new_user = models.User(name = request.name, email = request.email, password = hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

'''
@router.get('/{id}',response_model=schemas.ShowUser,tags=['user'])
def get_user(id:int, db: Session = Depends(get_db),get_current_user: schemas.User = Depends (oauth2.get_current_user)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404,detail="sad")
    return user
this route helps in getting a user when id is given
'''

@router.get('/',response_model=schemas.ShowUser,tags=['user'])
def get_user( db: Session = Depends(get_db),get_current_user: schemas.TokenData = Depends (oauth2.get_current_user)):
    user = db.query(models.User).filter(models.User.id == get_current_user.id).first()
    if not user:
        raise HTTPException(status_code=404,detail="sad")
    return user