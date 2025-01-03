from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get('/blog')
def index(limit=10, published:bool=True, sort:Optional[str]=None):
    # fetch published blogs per limit
    # To make a parameter optional, you use the Optional keyword and pass the type and then specify value
    if published:
        return {'data': f'{limit} published blogs from the database'}
    else:
        return {'data': f'{limit} blogs from the database'}


# Get all unpublished blogs
@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'All unpublished blogs'}


# Get blogs using the blog id
@app.get('/blog/{id}')
def show(id: int): #id:int ensures the id inly accepts int and not string
    return {'data': id}



# Getgit push comments based on the blog id
@app.get('/blog/{id}/comments')
def comments(id):
    # fetch comments of blog with id = id
    return {'data': {'1', '2'}}