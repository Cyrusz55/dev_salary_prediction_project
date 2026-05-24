from fastapi import FastAPI
from fastapi.responses import FileResponse
from dotenv import load_dotenv
import os
import pandas as pd

from apps.routes import router

from scheduler import start_scheduler

from machine_learning.machine_learning import train_model

load_dotenv()

app = FastAPI(
    title = "Developer Salary Prediction API",
    description = "Predicts developer salary based on profile and experience",
    version = "1.0.0",
)

app.include_router(router, prefix="/api/v1")

@app.on_event("startup")
def startup_event():
    os.makedirs("models", exist_ok=True)
    if not os.path.exists("models/dev_salary_model.joblib"):
        print("No Model found. running initial training...")
        df = pd.read_csv("data/clean/dev_salary_clean.csv")
        train_model(df)

    start_scheduler()
@app.get("/")
def root():
    html_path = "frontend/index.html"

    if os.path.exists(html_path):
        return FileResponse(html_path)
    return {"message": "Developer salary prediction model is running"}