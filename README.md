# Developer Salary Prediction Project

Professional analysis and modelling pipeline to predict developer yearly compensation (USD) from survey responses.

## Project overview

This repository contains an end-to-end exploratory data analysis (EDA) and regression modelling pipeline built from a Jupyter notebook (`notebooks/book1.ipynb`). The goal is to predict developers' annual salaries ( ConvertedCompYearly ) using demographic, experience and technology-related survey features.

Key deliverables in this repository:
- EDA visualizations saved to `data/` (salary distribution, feature distributions, correlation heatmap, feature importance)
- A preprocessing and modelling pipeline implemented in the notebook
- Saved best pipeline: `notebooks/best_pipeline.pkl`
- Source helper modules in `src/`

## Files & structure

Top-level structure (relevant files/folders):

- `notebooks/book1.ipynb` – main analysis and modelling notebook
- `data/` – dataset and generated visualizations
  - `raw/results.csv` – raw survey data used for analysis
  - `salary_distribution.png`
  - `features_distribution.png`
  - `correlation_heatmap.png`
  - `feature_importance.png`
- `notebooks/best_pipeline.pkl` – serialized final pipeline produced by the notebook
- `src/` – small helper modules (`model.py`, `preprocessing.py`)
- `requirements.txt` – Python package dependencies

## Quick EDA summary

- The salary target is `ConvertedCompYearly`. Rows were filtered to remove extreme outliers and non-positive salaries.
- Salary distribution is right-skewed; a log transform of salary was used as the modelling target.
- Median salary and relationships were examined across `Country`, `YearsCodePro`, `EdLevel`, `Employment`, and languages used.
- Correlations indicate moderate positive relationships between experience / education and salary.

Preview of generated visualizations (files are in `data/`):

- Salary distribution: `data/salary_distribution.png`
- Feature distributions: `data/features_distribution.png`
- Correlation heatmap: `data/correlation_heatmap.png`
- Top feature importances for the final model: `data/feature_importance.png`

You can open these images directly from the `data/` folder or view them in the notebook outputs.

## Modelling approach

- Target transform: log1p (to reduce skew)
- Preprocessing:
  - Numerical features: median imputation + standard scaling
  - Categorical features: high-cardinality columns encoded with `OrdinalEncoder`, low-cardinality with `OneHotEncoder` (drop first)
  - Column selection with `ColumnTransformer`
- Models explored: Linear Regression, Ridge, Lasso, XGBoost (and other regressors during experimentation)
- Cross-validation: KFold (5-fold) with metrics tracked (R², MAE, RMSE, MAPE)
- Hyperparameter tuning for XGBoost via `RandomizedSearchCV` and final XGBoost pipeline exported as `best_pipeline.pkl`.

## How to run

Prerequisites:

1. Install Python 3.8+ (recommended)
2. Create a virtual environment and install dependencies:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt
```

Run the analysis notebook (recommended):

1. Start Jupyter Lab / Notebook in the repository root:

```powershell
jupyter lab
```

2. Open `notebooks/book1.ipynb` and run cells top-to-bottom. The notebook generates visualizations into `data/` and saves the final pipeline to `notebooks/best_pipeline.pkl`.

Using the saved pipeline for predictions

Example Python snippet to load the saved pipeline and run a prediction on a single sample (replace the sample values with realistic feature values matching the notebook preprocessing expectations):

```python
import joblib
import pandas as pd

# Load pipeline
pipe = joblib.load('notebooks/best_pipeline.pkl')

# Example single-row input as a dict — adjust keys to actual feature names used in the model
sample = {
	'Country': 'United States',
	'YearsCodePro': 5,
	'EdLevel': "Master's degree",
	'Employment': 'Employed full-time',
	# ... include any other features required by the pipeline
}

X_sample = pd.DataFrame([sample])
# Pipeline expects preprocessed inputs; pipeline will handle encoding/imputation
pred_log = pipe.predict(X_sample)
pred = float(np.expm1(pred_log))
print(f"Predicted annual salary (USD): ${pred:,.0f}")
```

Note: The example above assumes the pipeline was trained on columns that match your sample. Inspect `notebooks/book1.ipynb` or `src/preprocessing.py` for the exact expected feature set and transformations.

## Reproducing training (from notebook)

- Open `notebooks/book1.ipynb` and run all cells. The notebook performs data cleaning, builds the preprocessing `ColumnTransformer`, evaluates several models using `cross_validate`, performs hyperparameter search for XGBoost, and saves the tuned pipeline.

If you prefer a script-based approach, examine `src/model.py` and `src/preprocessing.py` for reusable functions (they can be adapted to a standalone training script).

## Requirements

- See `requirements.txt` for exact package versions. Typical packages used include:
  - pandas, numpy, scikit-learn, xgboost, imbalanced-learn, joblib, seaborn, matplotlib

## Results & next steps

- A tuned XGBoost pipeline was identified as the top-performing model and saved as `notebooks/best_pipeline.pkl`.
- Next improvements to try:
  - More careful handling of high-cardinality categorical encodings (target encoding / hashing)
  - Additional feature engineering (location/role normalization, interaction terms)
  - Calibration for prediction intervals and quantile regression for salary ranges
  - Deploy the saved pipeline behind a simple API for inference (FastAPI / Flask)

## License & contact

This repository is provided for educational/demo purposes. If you have questions or want help extending this project, open an issue or contact the author.

-- End of README


