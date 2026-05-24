# Developer Salary Prediction API - Startup Guide

## Quick Start

### Prerequisites
- Python 3.8+
- Virtual environment activated (`.venv`)
- Dependencies installed from `requirements.txt`

### Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Server

The fastest way to start the development server is:

```bash
python -m uvicorn apps.main:app --reload --host 0.0.0.0 --port 8000
```

Or use the full app specification:

```bash
uvicorn apps.main:app --reload --host 0.0.0.0 --port 8000
```

#### Server Arguments Explained:
- `apps.main:app` - Module path to the FastAPI application instance
- `--reload` - Auto-reload on code changes (development only)
- `--host 0.0.0.0` - Listen on all network interfaces
- `--port 8000` - Use port 8000

### Accessing the Application

Once the server starts, you'll see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete
```

**Frontend:** http://localhost:8000
**API Docs (Swagger):** http://localhost:8000/docs
**API Alternative Docs (ReDoc):** http://localhost:8000/redoc
**Health Check:** http://localhost:8000/api/v1/health

### Using Startup Scripts

**Windows (PowerShell):**
```powershell
.\run.ps1
```

**Windows (Command Prompt):**
```cmd
python -m uvicorn apps.main:app --reload --host 0.0.0.0 --port 8000
```

## Troubleshooting

### Error: `"apps.main:app --reload is giving an error"`

**Solution:** Use `python -m uvicorn` or `uvicorn` command directly:
```bash
python -m uvicorn apps.main:app --reload
```

### Model Not Found Error

When you first start the server, it will automatically:
1. Check if `models/dev_salary_model.joblib` exists
2. If not found, load `data/clean/dev_salary_clean.csv` and train the model
3. Save the trained model to `models/dev_salary_model.joblib`

This happens automatically during the app startup (one-time setup).

### Port Already in Use

If port 8000 is already in use, specify a different port:
```bash
python -m uvicorn apps.main:app --reload --port 8001
```

### Missing Dependencies

If you get import errors, reinstall dependencies:
```bash
pip install -r requirements.txt --force-reinstall
```

## API Endpoints

- **GET /** - Serves the frontend HTML
- **GET /api/v1/health** - Health check endpoint
- **POST /api/v1/predict** - Predict developer salary
- **GET /api/v1/model-info** - Get model information

## Features

✓ FastAPI with Uvicorn server
✓ XGBoost salary prediction model
✓ Interactive HTML frontend
✓ Auto-reload on code changes
✓ Swagger API documentation
✓ Automatic model training on first run
✓ Weekly retraining scheduler (Saturdays at 12:00)

## Project Structure

```
DEV_SALARY_PREDITION_PROJECT/
├── apps/              # FastAPI application
│   ├── main.py        # Main FastAPI app
│   ├── routes.py      # API endpoints
│   └── schemas.py     # Pydantic models
├── frontend/          # HTML frontend
│   └── index.html     # Prediction interface
├── machine_learning/  # ML pipeline
│   └── machine_learning.py
├── models/            # Trained models (auto-created)
├── data/              # Dataset files
├── database/          # Database module
├── requirements.txt   # Dependencies
└── scheduler.py       # APScheduler for auto-retraining
```

## Development

To make changes to the API, edit the files in the `apps/` directory. With `--reload` enabled, changes will automatically restart the server.

To retrain manually:
```python
from machine_learning.machine_learning import train_model
import pandas as pd

df = pd.read_csv("data/clean/dev_salary_clean.csv")
train_model(df)
```

