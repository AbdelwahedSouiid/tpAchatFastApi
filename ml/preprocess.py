import pandas as pd
import os

# Define the path to the CSV file
file_path = 'ml/data/dataset.csv'
processed_file_path = 'ml/data/processed_dataset.csv'

def load_data():
    """Loads data from a CSV file if it exists, otherwise returns an empty DataFrame."""
    if os.path.exists(file_path):
        data = pd.read_csv(file_path)
        print("Data loaded successfully.")
    else:
        # Create an empty DataFrame if the file does not exist
        data = pd.DataFrame(columns=['feature1', 'feature2', 'prediction_result'])
        print("No data file found. Starting with an empty dataset.")
    return data
