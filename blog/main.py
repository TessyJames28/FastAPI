from . import models
from fastapi import FastAPI, Depends, status, Response, HTTPException
from .hashing import Hash
from .schemas import Blog, ShowBlog, User, ShowUser
from .database import engine, SessionLocal
from sqlalchemy.orm.session import Session
from typing import List


app = FastAPI()

# Create the tables in the database
models.Base.metadata.create_all(engine)


# The function helps to make the Session pased to the db on create func pydantic
# Thanks to the use of Depends from fastapi which allows the error-free starting of the server
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blogs'])
def create(request: Blog, db:Session = Depends(get_db)):
    # Create blog based on the schema: using request body
    new_blog = models.Blog(title=request.title, body=request.body) 
    db.add(new_blog) # Add to db
    db.commit() # Commit/save to db
    db.refresh(new_blog) # Refresh so as to return the newly created blog
    return new_blog



@app.delete('/blog/{id}', tags=['blogs'])
def destroy(id, db:Session = Depends(get_db)):
    # Delete an element on the db using the id
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"Blog with the id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit() # Commit changes to the db
    return Response(status_code=status.HTTP_204_NO_CONTENT) 



@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
def update(id, request: Blog, db:Session = Depends(get_db)):
    # Update the blog based on id. request.dict() convert pydantic model into a dictionary
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"Blog with the id {id} not found")
    blog.update(request.model_dump())
    db.commit()
    return {"data": "Successfully updated"}



@app.get('/blog', response_model=List[ShowBlog], tags=['blogs'])
def get_all(db: Session = Depends(get_db)):
    # Returns all blogs
    # The use of List from typing retrieve the blog titles and body as a list
    blogs = db.query(models.Blog).all()
    return blogs



@app.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=ShowBlog, tags=['blogs'])
def get_by_id(id, response: Response, db: Session = Depends(get_db)):
    # Retrieve blog based on given id
    # The response_model with the defined schema acts like the serializer on Django
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f"Blog with the id {id} not found"}
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"Blog with the id {id} not found")
    return blog



@app.post('/user', response_model=ShowUser, tags=['users'])
def create_user(request: User, db:Session = Depends(get_db)):
    # Function that creates new user
    hashed_pwd = Hash.bcrypt(request.password)
    new_user = models.User(name = request.name, email = request.email, password = hashed_pwd)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



@app.get('/user/{id}', response_model=ShowUser, tags=['users'])
def get_user(id, db: Session = Depends(get_db)):
    # Retrieve user based on given id
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"User with the id {id} not found")
    return user