# To run this main.py, we will have to execute: 'uvicorn blog.main:app --reload'

# Also we will be discussing about 'Response Status Code' which is a parameter specified in:
# decorator of the function, Example: @app.get('/', status_code=201)

"""
Method 2: use built-in module of fastapi called 'status'

Example usage:

from fastapi import status

@app.get('/', status_code = status.HTTP_201_CREATED)

# Now this is used in case you are unaware of the status codes fro different scenrios,
# So I simply typed 'create' and it auto-completed for me, suggessting the status code to be 201. 

"""

# Note: The 'tags' argument within the decorator is just for refactoring & proper viewing purpose only,
#       It will not hamper any other working/structure of code.

from typing import List # To get multiple blogs w/o 'ids' in Response Model

from fastapi import Response # To bypass default status_code mentioned in decorator of function

from fastapi import FastAPI

from fastapi import status

from fastapi import HTTPException # Direct way to reduce line 102 and 103 to a single statement 

from fastapi import Depends # Used to show dependency of a Function Argument

from . import schemas # To bring in the Class Defined in the Schemas
from . import models
from sqlalchemy.orm import Session # Used in the 2nd Parameter of create_db function
from .database import SessionLocal, engine

from .hashing import Hash # Importing Class for Password Hashing

models.Base.metadata.create_all(engine) # This line basically updates the 'TablePlus'app automatically 

"""responsible for generating the database tables based on the models you've defined. 
   It ensures that the database schema aligns with your application's data models. 
   This is typically done when setting up a new database or when you've made changes to your models,
   and need to update the database schema."""

# create_all(engine): This is a method provided by SQLAlchemy. 
#                     It instructs SQLAlchemy to create the database tables that are associated with the models defined in your application. 
#                     The engine parameter is the database engine to which the tables will be connected.

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog', status_code=201, tags=['Blogs'])                                 # We have passed 'status_code' as a parameter too.
def create(request: schemas.Blog, db: Session = Depends(get_db)):   # Note that we have written 'schemas.Blog here'
    new_blog = models.Blog(title=request.title, body=request.body)  # This line creates a new instance of the Blog model with the title and body provided in the request.
    db.add(new_blog)                                                # This adds the newly created Blog object to the database session. At this point, the object is in a "pending" state within the session.
    db.commit()                                                     # This commits the transaction to the database, which means that the changes (in this case, adding the new blog) are actually written to the database.
    db.refresh(new_blog)                                            # This ensures that the object's state is synchronized with the database. It's useful when you want to make sure the object has the most up-to-date information from the database after a commit.
    return new_blog


"""
def get_db():
    
This function provides a database session using a context manager.
It yields the database session to the caller.
The purpose of using a context manager with yield is to ensure that the session is properly managed,
and automatically closed when it's no longer needed.

"""

# Now lets try getting all the blogs from the database:

@app.get('/blog', response_model=List[schemas.ShowBlog2], tags=['Blogs']) # The response_model here has a 'List', because this function returns all the blogs.
def all(db: Session = Depends(get_db)): # This Parameter is nothing but just the Database Instance
    blogs = db.query(models.Blog).all() # This statement would generate/execute an SQL Query and we will get all the blogs
    return blogs

# So the above function returns ALL blogs as the GET Request Output

# Now lets create a GET Request to return a particular Blog

# Case I (Response Code for NULL not handled)

"""
@app.get('/blog/{id}', status_code=200)
def show(id, db: Session = Depends(get_db)): # As discussed earlier, we pass Path Parameter as an Argument too, here 'id'
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blog # it returns 'null' in case there is no blog with mentioned id

"""

# Case II (Response Code for NULL handled)

# Handling the Response Code for 'null', which is '200' by default.

@app.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog, tags=['Blogs']) # So we passed Response Model (a pydantic model / schema) as a parameter too.
def show(id, response: Response ,db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND # Now this status code (i.e. 404) bypasses '200'
        return {'detail': f'Blog with the id {id} is not available'}
    return blog


# line 102 and 103 can be replaced by:
# raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
#                     detail = f'Blog with the id {id} is not available')


# Deleting a Blog: '@app.delete()'

@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Blogs']) # Note that this is a delete request, hence '@app.delete()'
def destroy(id, db: Session = Depends(get_db)):

    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')

    blog.delete(synchronize_session=False) # Delete Query
    db.commit() # Commit the changes made in the db
    return 'done'

# Updating a Blog: '@app.put()'

@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['Blogs'])
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):

    blog = db.query(models.Blog).filter(models.Blog.id == id).update(request)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
    
    blog.update(request) 
    db.commit()
    return 'updated successfully'

# CREATING A USER

# But you will notice that the password is not 'Hashed', so lets work on that too:
# for that we have installed 'passlib'

@app.post('/user', tags=['Users'])
def create_user(request: schemas.User, db: Session = Depends(get_db)): # Herein the request is of type 'User' whose schema is defined in schemas.py
        
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password)) # Simply using 'Hash' named Class defined in hashing.py
    db.add(new_user)
    db.commit()
    db.refresh(new_user) # It is necessary to pass this argument
    return new_user

# Method 2: (Not an elegant way of writing code though), We add the following lines if code


""" pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto') """ 

# It sets up a CryptContext object configured to use the bcrypt hashing algorithm for securely hashing and verifying passwords. 
# It also has automatic handling for deprecated hashing algorithms.
# initialised outside the function.

""" hashedPassword = pwd_cxt.hash(request.password) """
""" new_user = models.User(name=request.name, email=request.email, password=hashedPassword) """ # This will initiate the addition of new_user

# Now, we want just the username and email to be displayed, and not the password and id,
# For that as done earlier, we will have to create a Response Model, hence the SCHEMA (because its a Pydantic thing)

@app.post('/user_email', response_model=schemas.ShowUser, tags=['Users']) # Added Response Model as a parameter
def create_user(request: schemas.User, db: Session = Depends(get_db)): 
        
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password)) 
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Another similar example to demonstrate Get Request usage with Response Model (to get jyst the username and the email)

@app.get('/user/{id}', response_model=schemas.ShowUser, tags=['Users'])
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found')
    
    return user