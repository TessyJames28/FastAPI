from ..database import get_db
from fastapi import APIRouter, Depends, status
from ..schemas import Blog, ShowBlog
from ..repository import blog
from sqlalchemy.orm.session import Session
from typing import List


router = APIRouter(
    prefix='/blog',
    tags=['blogs']
)


@router.get('', response_model=List[ShowBlog])
def get_all(db: Session = Depends(get_db)):
    # Returns all blogs
    # The use of List from typing retrieve the blog titles and body as a list
    return blog.get_all(db)


@router.post('', status_code=status.HTTP_201_CREATED)
def create(request: Blog, db:Session = Depends(get_db)):
    # Create blog based on the schema: using request body
    return blog.create(request, db)


@router.delete('/{id}')
def destroy(id: int, db:Session = Depends(get_db)):
    # Delete an element on the db using the id
   return blog.destroy(id, db)



@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: Blog, db:Session = Depends(get_db)):
    # Update the blog based on id. request.dict() convert pydantic model into a dictionary
    return blog.update(id, request, db)



@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowBlog)
def get_by_id(id: int, db: Session = Depends(get_db)):
    # Retrieve blog based on given id
    # The response_model with the defined schema acts like the serializer on Django
    return blog.get_by_id(id, db)