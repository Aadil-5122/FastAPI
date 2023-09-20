# 'Models' is another name for "Table Schema"

# SQLalchemy Models are simply called 'Models' as defined here,
# Pydantic Models are called 'Schemas' as defined in schemas.py

from sqlalchemy import Column, Integer, String, ForeignKey # Required imports to create Table Schema
from .database import Base

from sqlalchemy.orm import relationship

class Blog(Base): # We are extending Base of the db in this class.
    __tablename__ = 'blogs' # We specify the tablename
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)

    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship("User", back_populates="blogs")

class User(Base): # We are extending Base of the db in this class.
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship("Blog", back_populates="creator")

    # Now, we can use this model to store users in he database

"""
ESTABLISHING A RELATIONSHIP BETWEEN A USER AND A BLOG
"""
# For Establishing a Relationship, we write as line 17, line 19 and line 26.
# Carefully analyse the usage of "User", "Blog", "creator", "blogs".
