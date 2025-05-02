from fastapi import FastAPI
from app.routers import predict, elevation, dbcheck

app = FastAPI()

app.include_router(predict.router)
app.include_router(elevation.router)
app.include_router(dbcheck.router)

@app.get("/")
def root():
    return {"msg": "Landslide Risk Prediction API"}