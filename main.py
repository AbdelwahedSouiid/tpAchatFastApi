from fastapi import FastAPI
from schemas import PredictionRequest

app = FastAPI()





@app.post("/predict")
def test_predict(prediction_request: PredictionRequest):

    result = "prediction fais avec succes "

    # Retourner le résultat dans le format attendu
    return {"result": result}
