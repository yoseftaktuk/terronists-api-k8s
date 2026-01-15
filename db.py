import pandas as pd
import models
from pymongo import MongoClient

class Mongo_connection:
    def __init__(self):    
        self.client = MongoClient(
            host='mongo-0.mongo',
            port=27017,
            username='admin',
            password='secretpass',
            authSource='admin'
        )
        self.db = self.client['threat_db']
        self.collection = self.db['collection_name']

    def inser_all(self, data):
        for item in data:
            self.collection.insert_one(item)





def get_data(data):
    db = pd.read_csv(data)
    db.sort_values(by='danger_rate').head()
    top_terrorist = []
    for i in range(5):
        top_terrorist.append(db.values[i])
    print(top_terrorist[0])    
    return top_terrorist   
    
   
    

a = get_data("terrorists_data.csv")   

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
    print(count)    

    
