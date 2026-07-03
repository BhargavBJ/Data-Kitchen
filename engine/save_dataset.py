from data_store.mongo_connection import *
from engine.process_dataset import process_dataset
def save_dataset(file_name):
    dataset = process_dataset(file_name)
    collection = get_clean_db()
    records = dataset.to_dict(orient= 'records')
    if records:
        collection.insert_many(records)
    print(f'{len(records)} documents saved')


save_dataset(r"sources\csv\customers.csv")