from ..database import get_db
from fastapi import APIRouter, Depends, status, Response, HTTPException
from ..schemas import Blog, ShowBlog
from sqlalchemy.orm.session import Session
from .. import models
from typing import List


router = APIRouter(
    prefix='/blog',
    tags=['blogs']
)


@router.get('', response_model=List[ShowBlog])
def get_all(db: Session = Depends(get_db)):
    # Returns all blogs
    # The use of List from typing retrieve the blog titles and body as a list
    blogs = db.query(models.Blog).all()
    return blogs


@router.post('', status_code=status.HTTP_201_CREATED)
def create(request: Blog, db:Session = Depends(get_db)):
    # Create blog based on the schema: using request body
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog) # Add to db
    db.commit() # Commit/save to db
    db.refresh(new_blog) # Refresh so as to return the newly created blog
    return new_blog


@router.delete('/{id}')
def destroy(id, db:Session = Depends(get_db)):
    # Delete an element on the db using the id
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"Blog with the id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit() # Commit changes to the db
    return Response(status_code=status.HTTP_204_NO_CONTENT) 



@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: Blog, db:Session = Depends(get_db)):
    # Update the blog based on id. request.dict() convert pydantic model into a dictionary
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"Blog with the id {id} not found")
    blog.update(request.model_dump())
    db.commit()
    return {"data": "Successfully updated"}



@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowBlog)
def get_by_id(id, db: Session = Depends(get_db)):
    # Retrieve blog based on given id
    # The response_model with the defined schema acts like the serializer on Django
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"Blog with the id {id} not found")
    return blog