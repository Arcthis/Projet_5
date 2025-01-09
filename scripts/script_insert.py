import pandas as pd
from pymongo import MongoClient

mongo = MongoClient('mongodb://root:a1B2c3D4e5@db:27017/')
db = mongo['local']
collection = db['data']

df = pd.read_csv('/csv/healthcare_dataset.csv')

data = df.to_dict(orient='records')

collection.insert_many(data)

print("Importation terminée")