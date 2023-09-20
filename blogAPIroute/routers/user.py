# Notice that in the decorators of the endpoints, its 'router.get' and not 'app.get'

from fastapi import APIRouter

from .. import database, schemas, models
from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException
from .. hashing import Hash

# The parameters of APIRouter below are the common parameters of each endpoint,
# Hence reducing the length of each decorator and writing it in a more elegant way.

router = APIRouter(
    prefix="/user",     # This parameter sets the prefix of each endpoint.
    tags=['Users']      # This parameter sets the 'tag' to which this route would belong to.
)

get_db = database.get_db

@router.post('/user')
def create_user(request: schemas.User, db: Session = Depends(get_db)): 
        
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user) 
    return new_user

@router.post('/user_email', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)): 
        
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password)) 
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/user/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found')
    
    return user