import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Path to the processed dataset
processed_file = 'ml/data/dataset.csv'  # Ensure this is correct
model_file_path = 'ml/models/trained_model.pkl'

def load_data():
    """Loads the preprocessed dataset."""
    data = pd.read_csv(processed_file)
    print("Data loaded successfully.")
    return data

def train_model(data):
    """Trains a linear regression model and saves it to a file."""
    # Assuming the dataset has two features and one target variable
    X = data[['feature1', 'feature2']]  # Adjust based on your actual feature names
    y = data['prediction']  # Adjust to your target variable name

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print("Data split into training and testing sets.")

    # Create and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)
    print("Model training completed.")

    # Make predictions
    predictions = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    print(f"Model Evaluation:\nMean Squared Error: {mse}\nR² Score: {r2}")

    # Save the trained model
    joblib.dump(model, model_file_path)
    print(f"Model saved to {model_file_path}")

if __name__ == "__main__":
    # Load the processed data
    data = load_data()

    # Train the model
    train_model(data)

