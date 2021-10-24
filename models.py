from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType,URLType
from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique= True)
    password = Column(String)
    images = relationship("Images",  back_populates="creator")

class Images(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    caption = Column(String)
    url = Column(URLType)
    user_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship("User", back_populates="images")
    