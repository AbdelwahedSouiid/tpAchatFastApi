import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Path to the processed dataset
processed_file_path = 'ml/data/processed_dataset.csv'
model_file_path = 'models/trained_model.pkl'

def load_data():
    """Loads the preprocessed dataset."""
    data = pd.read_csv(processed_file_path)
    print("Data loaded successfully.")
    return data

def train_model(data):
    """Trains a linear regression model on the dataset."""
    # Features and target variable
    X = data[['feature1', 'feature2']]  # You may need to convert categorical features
    y = data['prediction_result']

    # Convert categorical features to numerical (if necessary)
    X = pd.get_dummies(X, columns=['feature1', 'feature2'], drop_first=True)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Model training completed.")
    print(f"Mean Squared Error: {mse}")
    print(f"R² Score: {r2}")

    return model

def save_model(model):
    """Saves the trained model to a file."""
    joblib.dump(model, model_file_path)
    print(f"Model saved to {model_file_path}")

if __name__ == "__main__":
    # Load the processed data
    data = load_data()

    # Train the model
    model = train_model(data)

    # Save the trained model
    save_model(model)
