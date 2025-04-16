from fastapi import FastAPI
from app.schema import PredictionInput
from app.model import predict

app = FastAPI()

@app.post("/predict")
def get_prediction(data: PredictionInput):
    result = predict(data)
    return {"risk": int(result)}
