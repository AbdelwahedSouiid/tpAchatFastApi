from fastapi import APIRouter
from app.services.prediction_service import PredictionService
from app.schemas.prediction import PredictionRequest


router = APIRouter(prefix="/predicion")  # Préfixe pour toutes les routes d'utilisateurs
prediction_service = PredictionService()  # Instanciation du service utilisateur

@router.post("/predict", summary="Create a user")
async def predict(prediction: PredictionRequest):
    return await prediction_service.make_prediction(prediction)

