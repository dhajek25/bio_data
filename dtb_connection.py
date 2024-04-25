import os

from deta import Deta
from dotenv import load_dotenv

load_dotenv(".env")
DETA_KEY = os.getenv("DETA_KEY")

# Initialize Deta with your project key
deta = Deta(DETA_KEY)

# Create/connect a database
db = deta.Base("my_no_dtb")

def insert_result(date, result):
    return db.put({"key": date,"result": result})

def fetch_result():
    res = db.fetch()
    return res.items
