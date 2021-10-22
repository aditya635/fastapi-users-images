from fastapi import APIRouter,Depends,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.functions import mode
import schemas,models
from datetime import datetime,timedelta,time
from hashing import Hash
from tokens import create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES
from database import get_db


router = APIRouter()

@router.post('/login', response_model=schemas.Token)
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=404,detail="sad")
    
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=404,detail="inc")
    #generate jwt token 
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id),"dub":user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}