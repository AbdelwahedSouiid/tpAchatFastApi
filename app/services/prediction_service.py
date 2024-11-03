# app/services/prediction_service.py

from app.schemas.prediction import PredictionRequest


class PredictionService:
    def __init__(self):
        # Simulated database (list) to store predictions
        self.predictions_db = []

    async def make_prediction(self, prediction_request: PredictionRequest):
        # Example prediction logic (mockup)
        # Let's assume that the prediction result is based on the length of feature1 and feature2
        feature1_length = len(prediction_request.feature1)
        feature2_length = len(prediction_request.feature2)

        # Mock prediction calculation
        prediction_result = feature1_length * 0.5 + feature2_length * 0.3

        # Create a result object with input and output
        prediction_data = {
            "feature1": prediction_request.feature1,
            "feature2": prediction_request.feature2,
            "prediction": prediction_result
        }

        # Store prediction result in the simulated database
        self.predictions_db.append(prediction_data)

        return prediction_data
