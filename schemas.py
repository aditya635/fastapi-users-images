from pydantic import BaseModel
from typing import Optional,List


class ShowUser(BaseModel):
    name:str
    email:str
    class Config():
        orm_mode=True

class User(BaseModel):
    name:str
    email:str
    password:str



class Login(BaseModel):
    username:str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None