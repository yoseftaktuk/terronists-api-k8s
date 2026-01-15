from fastapi import FastAPI ,File
import uvicorn

app = FastAPI()


@app.post('/top-threats')
def post_top_5(file: File):
    pass