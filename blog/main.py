from . import models
from fastapi import FastAPI
from .routers import blog, user, authLogin
from .database import engine



app = FastAPI()

# Create the tables in the database
models.Base.metadata.create_all(engine)


# Router definition
app.include_router(authLogin.router)
app.include_router(blog.router)
app.include_router(user.router)