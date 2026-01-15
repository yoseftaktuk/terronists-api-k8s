import pandas as pd
import models


def get_data(data):
    db = pd.read_csv(data)
    db.sort_values(by='danger_rate').head()
    top_terrorist = []
    for i in range(10):
        top_terrorist.append(db.values[i])
    return top_terrorist   
    
   
    

get_data("terrorists_data.csv")    
    
  