from . import models
from fastapi import FastAPI, Depends, status, Response, HTTPException
from .schemas import Blog
from .database import engine, SessionLocal
from sqlalchemy.orm.session import Session


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


@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: Blog, db:Session = Depends(get_db)):
    # Create blog based on the schema: using request body
    new_blog = models.Blog(title=request.title, body=request.body) 
    db.add(new_blog) # Add to db
    db.commit() # Commit/save to db
    db.refresh(new_blog) # Refresh so as to return the newly created blog
    return new_blog



@app.get('/blog')
def get_all(db: Session = Depends(get_db)):
    # Returns all blogs
    blogs = db.query(models.Blog).all()
    return blogs



@app.get('/blog/{id}', status_code=status.HTTP_200_OK)
def get_by_id(id, response: Response, db: Session = Depends(get_db), ):
    # Retrieve blog based on given id
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f"Blog with the id {id} not found"}
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"Blog with the id {id} not found")
    return blog