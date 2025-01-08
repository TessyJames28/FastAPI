from pydantic import BaseModel
from typing import List


# Schema for the blog
class BlogBase(BaseModel):
    title:str
    body:str


# Schema for the blog creation
class Blog(BlogBase):
    class Config():
        from_attributes = True



# Schema for blog users
class User(BaseModel):
    name:str
    email:str
    password:str 


# Schema for the formatted display of users. This allows the display of desired fields
class ShowUser(BaseModel):
    name:str
    email:str
    blogs: List[Blog] = []

    class Config():
        from_attributes = True



# Schema for the formatted display of blogs. This allows the display of desired fields
class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config():
        from_attributes = True



# Login/Authentication schema
class Login(BaseModel):
    username:str
    password:str