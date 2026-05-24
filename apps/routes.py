from fastapi import APIRouter, HTTPException
import os
import joblib
import pandas as pd
import numpy as np

from apps.schemas import DevSalaryInput, PredictionResponse

from machine_learning.machine_learning import (
    load_model,
    predict_new_salary,
)

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok", "message": "API is healthy"}

@router.post("/predict", response_model=PredictionResponse)
def predict(salary: DevSalaryInput):
    try:
        model = load_model()
        new_data = pd.DataFrame([salary.model_dump()])
        # Model predicts in log scale, convert back to actual salary
        log_prediction = predict_new_salary(model, new_data)[0]
        actual_salary = np.expm1(log_prediction)  # Inverse of log1p
        return PredictionResponse(predicted_salary=float(actual_salary))
    except FileNotFoundError:
        raise HTTPException(
            status_code = 503,
            detail="Model not yet trained. Run training first.",
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/model-info")
def model_info():
    path = os.getenv("MODEL_PATH", "models/dev_salary_model.joblib")

    if not os.path.exists(path):
        return {"status": "no model found"}

    model = joblib.load(path)
    return{
        "model_type": type(model).__name__,
        "model_path": path,
    }