from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.post('/top-threats')
def post_top_5():
    pass