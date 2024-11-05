import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder, StandardScaler

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
        data = pd.DataFrame(columns=['feature1', 'feature2', 'prediction'])
        print("No data file found. Starting with an empty dataset.")
    return data


def preprocess_data(data):
    """Preprocesses the data by label encoding categorical variables and normalizing numerical features."""

    # Label encoding for categorical features (e.g., feature1)
    label_encoder = LabelEncoder()
    data['feature1'] = label_encoder.fit_transform(data['feature1'])
    print("Categorical feature 'feature1' encoded.")
    data['feature2'] = label_encoder.fit_transform(data['feature2'])
    print("Categorical feature 'feature1' encoded.")

    # Identify numeric columns for scaling
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
    scaler = StandardScaler()

    # Apply scaling only to numeric columns
    data[numeric_columns] = scaler.fit_transform(data[numeric_columns])
    print(f"Numerical columns {list(numeric_columns)} normalized.")

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
