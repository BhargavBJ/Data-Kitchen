from engine.get_dataset import get_dataset
from engine.execute_algorithms import execute_algorithms
def process_dataset(file_name):
    processed = execute_algorithms(get_dataset(file_name))
    return processed