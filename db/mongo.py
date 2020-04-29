from environs import Env
from pymongo import MongoClient



try:
    env=Env()
    env.read_env("config/env.env")
    mongo_url=env("MONGO_URL")
    print(mongo_url)
    client=MongoClient(mongo_url)
    
except Exception as err:
    print(err)

