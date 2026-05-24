# FastAPI Development Server Startup Script
# This script starts the FastAPI server with uvicorn in development mode

# Ensure we're in the project directory
Set-Location -Path (Split-Path -Parent $MyInvocation.MyCommand.Path)

# Activate virtual environment (assumes .venv folder)
if (Test-Path ".\.venv\Scripts\Activate.ps1") {
    & ".\.venv\Scripts\Activate.ps1"
}

# Start the server
Write-Host "Starting Developer Salary Prediction API..." -ForegroundColor Green
Write-Host "Frontend will be available at: http://localhost:8000" -ForegroundColor Cyan
Write-Host "API documentation at: http://localhost:8000/docs" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

# Run uvicorn with the FastAPI app
uvicorn apps.main:app --reload --host 0.0.0.0 --port 8000

