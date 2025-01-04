from . import models
from fastapi import FastAPI, Depends
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


@app.post('/blog')
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