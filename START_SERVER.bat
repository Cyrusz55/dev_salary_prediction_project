REM Developer Salary Prediction API - Quick Start
REM Run this file to start the FastAPI server
@echo off
cd /d "%~dp0"
echo Starting Developer Salary Prediction API...
echo.
python -m uvicorn apps.main:app --reload --host 0.0.0.0 --port 8000
