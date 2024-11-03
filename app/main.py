from fastapi import FastAPI
from app.api import prediction_routes


app = FastAPI(title="tpAchat FastAPI")

# Inclure les routes de predictions
app.include_router(prediction_routes.router)

