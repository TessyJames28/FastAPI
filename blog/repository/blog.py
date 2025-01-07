from fastapi import HTTPException, Response, status
from sqlalchemy.orm.session import Session
from .. import models
from ..schemas import Blog


def get_all(db: Session):
    # Helper function to handle db query for blog data retrieval
    blogs = db.query(models.Blog).all()
    return blogs


def create(request: Blog, db: Session):
    # Helper function for post request to handle data storage
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog) # Add to db
    db.commit() # Commit/save to db
    db.refresh(new_blog) # Refresh so as to return the newly created blog
    return new_blog


def destroy(id: int, db: Session):
    # Helper function to handle delete operation on the db for the delete request
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"Blog with the id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit() # Commit changes to the db
    return Response(status_code=status.HTTP_204_NO_CONTENT) 


def update(id: int, request: Blog, db: Session):
    # Helper function to handle data update on the db
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"Blog with the id {id} not found")
    blog.update(request.model_dump())
    db.commit()
    return {"data": "Successfully updated"}


def get_by_id(id, db: Session):
    # Helper function that handles data retrieval based on a given id
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"Blog with the id {id} not found")
    return blog