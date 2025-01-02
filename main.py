from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    # fetch blog with id = id
    return {'data': 'blog list'}


# Get blogs using the blog id
@app.get('/blog/{id}')
def show(id: int): #id:int ensures the id inly accepts int and not string
    return {'data': id}


# Get all unpublished blogs
@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'All unpublished blogs'}


# Getgit push comments based on the blog id
@app.get('/blog/{id}/comments')
def comments(id):
    # fetch comments of blog with id = id
    return {'data': {'1', '2'}}