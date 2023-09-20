# Notice that in the decorators of the endpoints, its 'router.get' and not 'app.get'

from fastapi import APIRouter

from fastapi import Depends, status, HTTPException
from .. import schemas, database, models
from typing import List
from sqlalchemy.orm import Session

get_db = database.get_db

# The parameters of APIRouter below are the common parameters of each endpoint,
# Hence reducing the length of each decorator and writing it in a more elegant way.

router = APIRouter(
    prefix="/blog",     # This parameter sets the prefix of each endpoint.
    tags=['Blogs']      # This parameter sets the 'tag' to which this route would belong to.
)

@router.get('/', response_model=List[schemas.ShowBlog2]) 
def all(db: Session = Depends(get_db)): 
    blogs = db.query(models.Blog).all() 
    return blogs

@router.post('/', status_code=201)                 
def create(request: schemas.Blog, db: Session = Depends(get_db)):   
    new_blog = models.Blog(title=request.title, body=request.body)  
    db.add(new_blog)                                                
    db.commit()                                                     
    db.refresh(new_blog)                                            
    return new_blog

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT) 
def destroy(id, db: Session = Depends(get_db)):

    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')

    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):

    blog = db.query(models.Blog).filter(models.Blog.id == id).update(request)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
    
    blog.update(request) 
    db.commit()
    return 'updated successfully'

@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog) 
def show(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Blog with id {id} not found')
    return blog

