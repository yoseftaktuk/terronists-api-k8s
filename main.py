from fastapi import FastAPI ,File, HTTPException
from fastapi import UploadFile, Query, Form
import uvicorn
import db
import shutil

app = FastAPI()

connection = db.Mongo_connection()

@app.post('/top-threats')
def post_top_5(file: UploadFile):
        try:    
            if not file.filename.lower().endswith(('.csv')):
                return 404,"Please upload csv  file."
            if file.filename.lower().endswith(".csv"):
                extension = ".csv"
            filepath = "location where you want to store file"+ extension
            with open(filepath, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            try:
                if filepath.endswith(".csv"):
                    data = db.get_data(filepath)
                    data = db.valid_3(data)
                    connection.inser_all(data)
            except:
                return 401, "File is not proper" 
        except HTTPException as e:
            return {'code': 400, "detail": "No file provided"}   
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)     
        
