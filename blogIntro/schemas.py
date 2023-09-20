# We have written the Schema of the Class 

# Pydantic Models are called 'Schemas' as defined here,
# SQLalchemy Models are simply called 'Models' as defined in models.py

from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str

"""
RESPONSE MODEL: It is used if we want to hide parameters of a defined schema, 
                hence they aren't visible in the output section.
"""

class ShowBlog(Blog): # So here we extend the 'Blog' itself and not the 'BaseModel'
    
    class Config():
        orm_mode = True

# Output of the above class is that we will not see the ids

# Example 2:
class ShowBlog2(BaseModel): # So here we extend the 'BaseModel'
    
    title: str 
    
    class Config():
        orm_mode = True

# Output of the above class is that we will see only title

"""
CREATING A USER: For that we need to create a Schema for the User.
"""
class User(BaseModel): # We extend the BaseModel
    
    name: str
    email: str
    password: str

class ShowUser(BaseModel): # We extend the BaseModel
    
    name: str
    email: str

    class Config():
        orm_mode = True
