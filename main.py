from fastapi import FastAPI ,File, HTTPException
from fastapi import UploadFile, Query, Form
import uvicorn
import db
import shutil

app = FastAPI()

connection = db.Mongo_connection()

@app.post('/top_threats')
def post_top_5(file: UploadFile):
    data = db.upload_csv(file)
    data = db.get_data(data["data"])
    print(data)
    data = db.valid_3(data)
    connection.inser_all(data)
    return {'messeges': True}
         
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)     
        
