import os
from pymongo import  MongoClient


try:
    mongo_url=os.getenv("MONGO_URL")
    client=MongoClient(mongo_url)
except Exception as err:
    print(err)

