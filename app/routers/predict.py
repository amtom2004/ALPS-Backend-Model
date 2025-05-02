from fastapi import APIRouter
from app.model import predict
from app.schema import PredictionInput

router = APIRouter()

@router.post("/predict")
def get_prediction(data: PredictionInput):
    result = predict(data)
    return {"risk": int(result)} 