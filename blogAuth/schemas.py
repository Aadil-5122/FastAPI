# We have written the Schema of the Class 

# Pydantic Models are called 'Schemas' as defined here,
# SQLalchemy Models are simply called 'Models' as defined in models.py

from pydantic import BaseModel

from blogAuth.database import Base

class Blog(BaseModel):
    title: str
    body: str

class ShowBlog(Blog): 
    
    class Config():
        orm_mode = True

class ShowBlog2(BaseModel): 
    
    title: str 
    
    class Config():
        orm_mode = True

class User(BaseModel): 
    
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    
    name: str
    email: str

    class Config():
        orm_mode = True

# For Login Details

class Login(BaseModel):
    username: str
    password: str

# For JWT Generation

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None

