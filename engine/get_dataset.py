from ingestion.csv_ingestion import load_csv
def get_dataset(source):
    return load_csv(source)