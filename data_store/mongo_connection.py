from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
CLEANED_DATA = os.getenv("CLEANED_DATA")
CLEANED_DATA_COLLECTION = os.getenv("CLEANED_DATA_COLLECTION")
RAW_DATA = os.getenv("RAW_DATA")
RAW_DATA_COLLECTION = os.getenv("RAW_DATA_COLLECTION")

def get_clean_db():
    client = MongoClient(MONGO_URI)
    db = client[CLEANED_DATA]
    if CLEANED_DATA_COLLECTION not in db.list_collection_names():
        db.create_collection(CLEANED_DATA_COLLECTION)
    return db[CLEANED_DATA_COLLECTION]

def get_raw_db():
    client = MongoClient()
    db = client[RAW_DATA]
    if RAW_DATA_COLLECTION not in db.list_collection_names():
        db.create_collection(RAW_DATA_COLLECTION)
    return db[RAW_DATA_COLLECTION]