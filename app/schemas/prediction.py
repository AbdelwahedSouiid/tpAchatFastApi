from pydantic import BaseModel
# Schéma pour la requête de prédiction
class PredictionRequest(BaseModel):
    feature1: str
    feature2: str




