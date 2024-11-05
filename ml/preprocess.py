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

def preprocess_data(data):
    """Simplified preprocessing: handle missing values and basic normalization."""
    # Fill missing values with the mean for simplicity
    data.fillna(data.mean(), inplace=True)
    print("Missing values filled.")

    # Normalize numerical features using min-max normalization
    if not data.empty:
        data['feature1'] = (data['feature1'] - data['feature1'].min()) / (data['feature1'].max() - data['feature1'].min())
        data['feature2'] = (data['feature2'] - data['feature2'].min()) / (data['feature2'].max() - data['feature2'].min())
        print("Features normalized.")
    else:
        print("No data to normalize.")

    return data

def save_processed_data(data):
    """Saves the preprocessed data to a new CSV file."""
    data.to_csv(processed_file_path, index=False)
    print(f"Preprocessed data saved to {processed_file_path}")

if __name__ == "__main__":
    # Load existing data
    data = load_data()

    # Preprocess data
    preprocessed_data = preprocess_data(data)

    # Save the processed data
    save_processed_data(preprocessed_data)
