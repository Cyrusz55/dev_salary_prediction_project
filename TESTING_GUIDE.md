# Testing the Fixed API

## Quick Test

### 1. Start the Server

```bash
uvicorn apps.main:app --reload --host 0.0.0.0 --port 8000
```

### 2. Using the Web Frontend

1. Navigate to **http://localhost:8000**
2. Fill in the form with any values from the available dropdowns
3. Click **"Predict Salary"**
4. Should see a salary prediction in USD ✓

### 3. Using cURL for API Testing

```bash
curl -X POST "http://localhost:8000/api/v1/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "Age": "25-34 years old",
    "EdLevel": "Bachelor'\''s degree (B.A., B.S., B.Eng., etc.)",
    "Employment": "Employed",
    "WorkExp": 5,
    "YearsCode": 8,
    "DevType": "Developer, full-stack",
    "OrgSize": "100 to 499 employees",
    "RemoteWork": "Remote",
    "Industry": "Software Development",
    "Country": "United States",
    "LanguageHaveWorkedWith": "Python;SQL;JavaScript"
  }'
```

### 4. Expected Response

```json
{
  "predicted_salary": 85000.0,
  "status": "success"
}
```

## Valid Categorical Values

### Age
- 18-24 years old
- 25-34 years old
- 35-44 years old
- 45-54 years old
- 55-64 years old
- 65 years or older
- Prefer not to say

### EdLevel
- Primary/elementary school
- Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)
- Some college/university study without earning a degree
- Associate degree (A.A., A.S., etc.)
- Bachelor's degree (B.A., B.S., B.Eng., etc.)
- Master's degree (M.A., M.S., M.Eng., MBA, etc.)
- Professional degree (JD, MD, Ph.D, Ed.D, etc.)
- Other (please specify):

### Employment
- Employed
- Independent contractor, freelancer, or self-employed
- Student
- Retired
- Not employed
- I prefer not to say

### DevType
- Developer, back-end
- Developer, front-end
- Developer, full-stack
- Developer, mobile
- Data scientist or machine learning specialist
- DevOps specialist

### OrgSize
- Less than 20 employees
- 20 to 99 employees
- 100 to 499 employees
- 500 to 999 employees
- 1,000 to 4,999 employees
- 5,000 to 9,999 employees
- 10,000 or more employees
- Just me - I am a freelancer, sole proprietor, etc.
- I don't know

### RemoteWork
- In-person
- Remote
- Hybrid (some remote, leans heavy to in-person)
- Hybrid (some in-person, leans heavy to flexibility)
- Your choice (very flexible, you can come in when you want or just as needed)

### Other Fields
- **Industry**: Free text (e.g., "Software Development", "Fintech", "Healthcare")
- **Country**: Free text (e.g., "United States", "Canada", "India")
- **LanguageHaveWorkedWith**: Semicolon-separated values (e.g., "Python;SQL;JavaScript")

## Troubleshooting

❌ **Still getting 500 error?**
- Verify all categorical values match the list above
- Check the API response detail for validation errors
- Ensure the model file exists at `models/dev_salary_model.joblib`

✅ **No errors? Working!**
- The API is functioning correctly
- Frontend is synced with backend
- Model is ready for predictions

## API Endpoints

- **GET /** - Frontend interface
- **GET /api/v1/health** - Health check
- **POST /api/v1/predict** - Make prediction (main endpoint)
- **GET /api/v1/model-info** - Model information
- **GET /docs** - Swagger API documentation

