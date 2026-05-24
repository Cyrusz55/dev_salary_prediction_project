from pydantic import BaseModel, Field
from typing import Literal
class DevSalaryInput(BaseModel):
    Age: Literal['18-24 years old', '25-34 years old', '35-44 years old', '45-54 years old', '55-64 years old', '65 years or older', 'Prefer not to say'] = Field(..., description="Age range of the developer")
    EdLevel: Literal["Bachelor's degree (B.A., B.S., B.Eng., etc.)", "Master's degree (M.A., M.S., M.Eng., MBA, etc.)", "Associate degree (A.A., A.S., etc.)", "Some college/university study without earning a degree", "Professional degree (JD, MD, Ph.D, Ed.D, etc.)", "Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)", "Primary/elementary school", "Other (please specify):"] = Field(..., description="Education level of the developer")
    Employment: Literal['Employed', 'Independent contractor, freelancer, or self-employed', 'Retired', 'Student', 'Not employed', 'I prefer not to say'] = Field(..., description="Employment status of the developer")
    WorkExp: int = Field(..., description="Years of work experience")
    YearsCode: int = Field(..., description="Years of coding experience")
    DevType: Literal['Developer, front-end', 'Developer, back-end', 'Developer, full-stack', 'Developer, mobile', 'Data scientist or machine learning specialist', 'DevOps specialist'] = Field(..., description="Type of developer")
    OrgSize: Literal['Less than 20 employees', '20 to 99 employees', '100 to 499 employees', '500 to 999 employees', '1,000 to 4,999 employees', '5,000 to 9,999 employees', '10,000 or more employees', 'Just me - I am a freelancer, sole proprietor, etc.', "I don't know"] = Field(..., description="Size of the organization")
    RemoteWork: Literal['Remote', 'In-person', 'Hybrid (some remote, leans heavy to in-person)', 'Hybrid (some in-person, leans heavy to flexibility)', 'Your choice (very flexible, you can come in when you want or just as needed)'] = Field(..., description="Remote work arrangement")
    Industry: str = Field(..., description="Industry in which the developer works")
    Country: str = Field(..., description="Country of residence of the developer")
    LanguageHaveWorkedWith: str = Field(..., description="Programming languages the developer has worked with (semicolon-separated)")
class PredictionResponse(BaseModel):
    predicted_salary: float = Field(..., description="Predicted salary for the developer in USD")
    status: str = "success"
