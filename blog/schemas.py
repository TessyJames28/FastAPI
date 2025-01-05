from pydantic import BaseModel


# Schema for the blog
class Blog(BaseModel):
    title:str
    body:str



# Schema for the formatted display of blogs. This allows the display of desired fields
class ShowBlog(BaseModel):
    title:str
    body:str

    class Config():
        orm_mode = True



# Schema for blog users
class User(BaseModel):
    name:str
    email:str
    password:str 


# Schema for the formatted display of users. This allows the display of desired fields
class ShowUser(BaseModel):
    name:str
    email:str

    class Config():
        orm_mode = True