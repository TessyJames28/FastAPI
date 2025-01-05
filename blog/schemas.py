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

    