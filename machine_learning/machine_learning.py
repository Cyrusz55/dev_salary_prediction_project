import os
import joblib
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
import matplotlib.pyplot as plt
import xgboost
MODEL_PATH = "models/dev_salary_model.joblib"
TARGET_COL = 'ConvertedCompYearly'
NUM_COLS  = ['WorkExp', 'YearsCode']
CAT_COLS = ['Age', 'EdLevel', 'Employment', 'DevType', 'OrgSize', 'RemoteWork', 'Industry', 'Country', 'LanguageHaveWorkedWith']
high_card_cols = ['DevType', 'Country', 'LanguageHaveWorkedWith']
low_card_cols = ['Age', 'EdLevel', 'Employment', 'OrgSize', 'RemoteWork', 'Industry']
def get_X_y(df: pd.DataFrame):
    X = df[NUM_COLS + CAT_COLS]
    y = np.log1p(df[TARGET_COL])  # Transform target to log scale (matches notebook)
    return X, y
def build_pipeline():
    num_pipeline = Pipeline(
        steps = [
            ('imputer', SimpleImputer(strategy='median')),
            ("scaler", StandardScaler()),
        ]
    )
    high_card_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OrdinalEncoder(
            handle_unknown='use_encoded_value',
            unknown_value=-1
        ))
    ])
    # low cardinality pipeline
    low_card_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(handle_unknown='ignore',
                                  drop='first',
                                  sparse_output=False,
                                  min_frequency=1))
    ])
    preprocessor = ColumnTransformer([
        ('num', num_pipeline, NUM_COLS),
        ('high_card', high_card_pipeline, high_card_cols),
        ('low_card', low_card_pipeline, low_card_cols)
    ])
    model = Pipeline(
        steps = [
            ('preprocessor', preprocessor),
            ('xgb', xgboost.XGBRegressor(
                n_estimators=1200,
                max_depth=2,
                learning_rate=0.15,
                subsample=0.9,
                colsample_bytree=0.5,
                min_child_weight=3,
                gamma=0.5,
                reg_alpha=5,
                reg_lambda=0,
                objective="reg:squarederror",
                random_state=42,
                verbosity=0,
            ))
        ]
    )
    return model
def train_model(df: pd.DataFrame):
    X, y = get_X_y(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = build_pipeline()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    r2 = r2_score(y_test, y_pred)
    print(f"Model Training Results (Target in Log Scale):")
    print(f"  MAE (Log Scale): {mae:.4f}")
    print(f"  RMSE (Log Scale): {rmse:.4f}")
    print(f"  R² Score: {r2:.4f}")
    print(f"\nNote: Target variable (ConvertedCompYearly) is in log scale using np.log1p()")
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")
    return model, X_test, y_test
def predict_new_salary(model, new_data: pd.DataFrame):
    return model.predict(new_data)


def load_model():
    from pathlib import Path

    # Try local first
    local_path = Path("models/dev_salary_model.joblib")
    if local_path.exists():
        return joblib.load(local_path)

    # Try HuggingFace cache
    cache_path = Path("models/models--cyrusnx--salary-model/snapshots")
    if cache_path.exists():
        # Get the latest snapshot
        snapshots = list(cache_path.glob("*/dev_salary_model.joblib"))
        if snapshots:
            return joblib.load(snapshots[0])

    raise FileNotFoundError("Model file not found")
def predict_single(input_data: dict):
    model = load_model()
    df = pd.DataFrame([input_data])
    log_prediction = model.predict(df)[0]
    # Convert from log scale back to actual salary
    actual_salary = np.expm1(log_prediction)
    return int(actual_salary)
if __name__ == "__main__":
    df = pd.read_csv("data/clean/dev_salary_clean.csv")
    train_model(df)
