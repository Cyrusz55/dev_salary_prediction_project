from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = PROJECT_ROOT / 'data' / 'raw' / 'results.csv'
CLEAN_PATH = PROJECT_ROOT / 'data' / 'clean' / 'dev_salary_clean.csv'
target_col  = 'ConvertedCompYearly'

def clean_data(df: pd.DataFrame) ->pd.DataFrame:
    print(f"[clean] Starting shape: {df.shape}")

    # drop unnecessary columns
    features = ['Age', 'EdLevel', 'Employment', 'WorkExp', 'YearsCode', 'DevType', 'OrgSize', 'RemoteWork', 'Industry', 'Country', 'LanguageHaveWorkedWith']
    df_cleaned = df[features + ['ConvertedCompYearly']].copy()

    # drop rows with missing values
    df_cleaned = df_cleaned.dropna(subset=[target_col])

    print(f"[clean] Final shape: {df_cleaned.shape}")

    return df_cleaned

if __name__ == "__main__":
    df_raw = pd.read_csv(RAW_PATH)
    df_clean = clean_data(df_raw)
    df_clean.to_csv(CLEAN_PATH, index=False)
    print(f"[clean] Cleaned data saved to {CLEAN_PATH}")