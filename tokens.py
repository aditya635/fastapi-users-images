from logging import error
from fastapi.exceptions import HTTPException
from jose import JWTError, jwt
from datetime import time,timedelta,datetime
from typing import Optional
from fastapi import Depends
from schemas import TokenData
from dotenv import load_dotenv
import os
load_dotenv()

SECRET_KEY = os.environ['KEYS']
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(credentials_exception,token: str ):
    try:
        payload:str = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id:str = payload.get("sub")
        if id is None:
            raise credentials_exception
        token_data = TokenData(id=int(id))
        return token_data
    except JWTError:
        raise credentials_exception