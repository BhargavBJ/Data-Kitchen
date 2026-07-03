from engine.process_dataset import process_dataset
def preview(file_name):
    dataset = process_dataset(file_name)
    print(f'Rows: {dataset.shape[0]}')
    print(f'Columns: {dataset.shape[1]}')
    return dataset

print(preview("sources/csv/customers.csv"))