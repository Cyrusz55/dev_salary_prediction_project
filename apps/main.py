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
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://YOUR_GITHUB_USERNAME.github.io"],  # Your GitHub Pages URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router, prefix="/api/v1")

@app.on_event("startup")
def startup_event():
    from huggingface_hub import hf_hub_download
    os.makedirs("models", exist_ok=True)

    try:
        # Try to download model from HuggingFace
        model_path = hf_hub_download(
            repo_id="YOUR_HF_USERNAME/salary-model",
            filename="dev_salary_model.joblib",
            cache_dir="models"
        )
        print(f"Model downloaded from HuggingFace: {model_path}")
    except Exception as e:
        print(f"Could not download from HuggingFace: {e}")
        print("Attempting fallback: loading local model or training...")
        if not os.path.exists("models/dev_salary_model.joblib"):
            print("No Model found. Running initial training...")
            import pandas as pd
            from machine_learning.machine_learning import train_model
            try:
                df = pd.read_csv("data/clean/dev_salary_clean.csv")
                train_model(df)
            except FileNotFoundError:
                print("Warning: Training data not found. API will fail without model.")

    start_scheduler()
@app.get("/")
def root():
    html_path = "frontend/index.html"

    if os.path.exists(html_path):
        return FileResponse(html_path)
    return {"message": "Developer salary prediction model is running"}