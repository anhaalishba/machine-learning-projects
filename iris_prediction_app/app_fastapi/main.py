from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator
import joblib
import pandas as pd

app = FastAPI(title="Iris Classification API")

# -------------------------------
# Load trained model
# -------------------------------
MODEL_PATH = "best_pipeline.pkl"
model = joblib.load(MODEL_PATH)

# -------------------------------
# Pydantic schema for input validation
# -------------------------------
class IrisInput(BaseModel):
    SepalLengthCm: float
    SepalWidthCm: float
    PetalLengthCm: float
    PetalWidthCm: float

    @validator('*')
    def check_range(cls, v):
        if not 0 < v < 10:
            raise ValueError('Value must be between 0 and 10')
        return v
# Predict endpoint
# -------------------------------
@app.post("/predict")
def predict(payload: IrisInput):
    try:
        # Convert input to DataFrame
        X = pd.DataFrame([payload.dict()])

        # Predict class
        pred = model.predict(X)[0]

        # Predict probabilities
        proba = model.predict_proba(X)[0].tolist() if hasattr(model, "predict_proba") else None
        classes = model.classes_.tolist() if hasattr(model, "classes_") else None

        return {
            "prediction": pred,
            "probabilities": dict(zip(classes, proba)) if proba is not None else None
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# -------------------------------
# Health check
# -------------------------------
@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": model is not None}
