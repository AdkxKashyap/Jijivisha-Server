
#loading env files
from dotenv import load_dotenv

def load_env():
    try:
        if(load_dotenv(verbose=True)=="File doesn't exist "):
            raise Exception(".env file does'nt exist")
    except Exception as err:
        return Exception(err)

load_env()