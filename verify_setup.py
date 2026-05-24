#!/usr/bin/env python
"""
Verification script for Developer Salary Prediction API setup
"""
print("=" * 60)
print("FINAL VERIFICATION OF FIXES")
print("=" * 60)

# Test 1: Imports
print("\n1. Testing imports...")
try:
    from apps.main import app
    print("   ✓ apps.main.app imported successfully")
except Exception as e:
    print(f"   ✗ Error: {e}")

try:
    from apps.routes import router
    print("   ✓ apps.routes.router imported successfully")
except Exception as e:
    print(f"   ✗ Error: {e}")

try:
    from machine_learning.machine_learning import train_model, load_model, predict_new_salary
    print("   ✓ machine_learning module imported successfully")
except Exception as e:
    print(f"   ✗ Error: {e}")

try:
    from scheduler import start_scheduler
    print("   ✓ scheduler module imported successfully")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Test 2: Check files exist
print("\n2. Checking required files...")
import os
files = [
    "data/clean/dev_salary_clean.csv",
    "frontend/index.html",
    "requirements.txt",
    "apps/main.py",
    "apps/routes.py",
    "apps/schemas.py",
]
for f in files:
    exists = os.path.exists(f)
    status = "✓" if exists else "✗"
    print(f"   {status} {f}")

# Test 3: Check dependencies
print("\n3. Checking key dependencies...")
deps = ["fastapi", "uvicorn", "pandas", "xgboost", "apscheduler"]
for dep in deps:
    try:
        __import__(dep)
        print(f"   ✓ {dep} installed")
    except ImportError:
        print(f"   ✗ {dep} NOT installed")

print("\n" + "=" * 60)
print("VERIFICATION COMPLETE")
print("=" * 60)
print("\nTo start the server, run:")
print("  python -m uvicorn apps.main:app --reload --host 0.0.0.0 --port 8000")
print("\nOr for production (no auto-reload):")
print("  python -m uvicorn apps.main:app --host 0.0.0.0 --port 8000")

