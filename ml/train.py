import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Path to the processed dataset
processed_file_path = 'ml/data/dataset.csv'
model_file_path = 'models/trained_model.pkl'

def load_data():
    """Loads the preprocessed dataset."""
    data = pd.read_csv(processed_file_path)
    print("Data loaded successfully.")
    return data

