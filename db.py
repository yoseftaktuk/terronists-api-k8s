import pandas as pd
import models
from pymongo import MongoClient
import os
import csv
from fastapi import UploadFile
import io
from dotenv import load_dotenv

load_dotenv()
class Mongo_connection:
    def __init__(self):  
        try:  
            self.client = MongoClient(
                host=os.getenv('MONGO_HOST','mongo'),
                port=27017,
                username=os.getenv('MONGO_USERNAME','admin'),
                password=os.getenv('MONGO_PASSWORD', 'secretpass'),
                authSource=os.getenv('ONGO_AUTH_SOURCE', 'admin')
            )
        
            self.db = self.client[os.getenv('MONGO-DB','threat_db')]
            self.collection = self.db['top_threats']
        except ConnectionError as e:
            return {'messegs': str(e)}

    def inser_all(self, data):
        for item in data:
            self.collection.insert_one(item)





def get_data(data):
    db = pd.DataFrame(data)
    top_terrorist = []
    for i in range(5):
        top_terrorist.append(db[i])   
    return top_terrorist   
    
   
    
   

def valid_3(data: list):
    count = {}
    new_terroris_list = []
    new_terroris_dict = {}
    for i in range(5):
        models.Terrorist(name=data[i][0])
        models.Terrorist(location=data[i][2])
        models.Terrorist(danger_rate=data[i][1])
        new_terroris_dict['name'] = data[i][0]
        new_terroris_dict['location'] = data[i][2]
        new_terroris_dict['danger_rate'] = data[i][1]
        new_terroris_list.append(new_terroris_dict)
    count['count'] = len(new_terroris_list)
    count['top'] = new_terroris_list  
    

    
def upload_csv(file: UploadFile):
    # Validate that the uploaded file is a CSV
    if file.content_type != "text/csv":
         return {"error": "File must be a CSV"}


    # Read file bytes
    content = file.file.read().decode("utf-8")

    # Parse CSV
    reader = csv.reader(io.StringIO(content))
    header = next(reader)
    rows = list(reader)
        

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "total_rows": len(rows),
        "columns": header,
        "data": rows,
        "message": f"Successfully processed CSV with {len(rows)} rows"
    }