# 'Models' is another name for "Table Schema"

# SQLalchemy Models are simply called 'Models' as defined here,
# Pydantic Models are called 'Schemas' as defined in schemas.py

from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

from sqlalchemy.orm import relationship

class Blog(Base): 
    __tablename__ = 'blogs' 
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)

    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship("User", back_populates="blogs")

class User(Base): 
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship("Blog", back_populates="creator")
