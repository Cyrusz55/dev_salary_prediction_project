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
        print(f"DEBUG: Loading model...")
        model = load_model()
        print(f"DEBUG: Model loaded. Input: {salary.model_dump()}")
        new_data = pd.DataFrame([salary.model_dump()])
        print(f"DEBUG: DataFrame created: {new_data.columns.tolist()}")
        log_prediction = predict_new_salary(model, new_data)[0]
        print(f"DEBUG: Prediction made: {log_prediction}")
        actual_salary = np.expm1(log_prediction)
        return PredictionResponse(predicted_salary=float(actual_salary))
    except FileNotFoundError as e:
        print(f"DEBUG: FileNotFoundError: {e}")
        raise HTTPException(status_code=503, detail="Model not found")
    except Exception as e:
        print(f"DEBUG: Exception: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
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