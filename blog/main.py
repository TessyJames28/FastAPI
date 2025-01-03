from fastapi import FastAPI


app = FastAPI()


@app.post('/blog')
def create(title, body):
    return {'data': {'title': title, 'body': body}}