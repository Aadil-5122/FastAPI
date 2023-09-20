# Notice that in the decorators of the endpoints, its 'router.get' and not 'app.get'

from fastapi import APIRouter

from fastapi import Depends, status
from .. import schemas, database
from typing import List
from sqlalchemy.orm import Session

# Required import for the refactoring of Router
from .. repository import blog

# For Authenticating an Endpoint
from .. import oauth2

get_db = database.get_db

router = APIRouter(
    prefix="/blog",     
    tags=['Blogs']     
)

# Lets authenticate the following endpoints
# Carefully look at the added function argument of each endpoint (The only point of difference)

# In the backend, everything is controlled by the 'oauth2.py' and pydantic schemas 'TokenData' and 'Token'

@router.get('/', response_model=List[schemas.ShowBlog2]) 
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)): 
    return blog.get_all(db)

@router.post('/', status_code=201,)                 
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):   
    return blog.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT) 
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog) 
def show(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id, db)