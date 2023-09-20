# The intended task of this directory is to 'refactor' routers.

from sqlalchemy.orm import Session
from fastapi import status, HTTPException
from .. import models, schemas

# Definitions of the endpoints.

def get_all(db: Session):
    blogs = db.query(models.Blog).all() 
    return blogs

def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body)  
    db.add(new_blog)                                                
    db.commit()                                                     
    db.refresh(new_blog)                                            
    return new_blog

def destroy(id: int, db: Session):

    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).update(request)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
    blog.update(request) 
    db.commit()
    return 'updated successfully'

def show(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Blog with id {id} not found')
    return blog