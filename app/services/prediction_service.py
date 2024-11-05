from app.schemas.prediction import PredictionRequest

from ml.predict import calculate_prediction

from ml.preprocess import  load_data
class PredictionService:
    def __init__(self):
        # Simulated database (list) to store predictions
        self.predictions_db = []

    async def make_prediction(self, prediction_request: PredictionRequest):
        # Use the new calculate_prediction function for prediction
        prediction_result = calculate_prediction(prediction_request.feature1, prediction_request.feature2)

        # Create a result object with input and output
        prediction_data = {
            "feature1": prediction_request.feature1,
            "feature2": prediction_request.feature2,
            "prediction": prediction_result
        }
        # Store prediction result in the simulated database
        self.predictions_db.append(prediction_data)

        return prediction_data
