from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    # fetch blog with id = id
    return {'data': 'blog list'}


@app.get('/blog/{id}')
def show(id:int): #id:int ensures the id inly accepts int and not string
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id):
    # fetch comments of blog with id = id
    return {'data': {'1', '2'}}