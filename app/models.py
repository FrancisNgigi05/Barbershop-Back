#models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String, index=True)
    password = Column(String)
    profile = Column(String)

class UserCreate(BaseModel):
    name: str
    username: str
    email: str
    phone_number: str
    password: str
    profile: str

class UserResponse(BaseModel):
    id: int
    name: str
    username: str
    email: str
    phone_number: str
    profile: str