from fastapi import FastAPI
from app.api.schemas.schemas import PredictionRequest

app = FastAPI()


@app.post("/predict")
def test_predict(prediction_request: PredictionRequest):

    result = "prediction fais avec succes"

    # Retourner le résultat dans le format attendu
    return {"result": result}
