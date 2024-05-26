# Notice that in the decorators of the endpoints, its 'router.get' and not 'app.get'

from fastapi import APIRouter

import database, schemas
from sqlalchemy.orm import Session
from fastapi import Depends

# Required import for the refactoring of Router
from repository import user

router = APIRouter(
    prefix="/user",    
    tags=['Users']      
)

get_db = database.get_db

@router.post('/user')
def create_user(request: schemas.User, db: Session = Depends(get_db)): 
    return user.create(request, db)

@router.get('/user/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)

@router.post('/user_email', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)): 
    return user.useremail(request, db)