from pydantic import BaseModel, Field

FIELD_TO_COLUMN = {
    "gender": "Gender",
    "senior_citizen": "Senior Citizen",
    "partner": "Partner",
    "dependents": "Dependents",
    "tenure_months": "Tenure Months",
    "phone_service": "Phone Service",
    "multiple_lines": "Multiple Lines",
    "internet_service": "Internet Service",
    "online_security": "Online Security",
    "online_backup": "Online Backup",
    "device_protection": "Device Protection",
    "tech_support": "Tech Support",
    "streaming_tv": "Streaming TV",
    "streaming_movies": "Streaming Movies",
    "contract": "Contract",
    "paperless_billing": "Paperless Billing",
    "payment_method": "Payment Method",
    "monthly_charges": "Monthly Charges",
    "total_charges": "Total Charges",
}


class CustomerFeatures(BaseModel):
    gender: str = Field(examples=["Female"])
    senior_citizen: str = Field(examples=["No"])
    partner: str = Field(examples=["Yes"])
    dependents: str = Field(examples=["No"])
    tenure_months: float = Field(examples=[12])
    phone_service: str = Field(examples=["Yes"])
    multiple_lines: str = Field(examples=["No"])
    internet_service: str = Field(examples=["Fiber optic"])
    online_security: str = Field(examples=["No"])
    online_backup: str = Field(examples=["Yes"])
    device_protection: str = Field(examples=["No"])
    tech_support: str = Field(examples=["No"])
    streaming_tv: str = Field(examples=["Yes"])
    streaming_movies: str = Field(examples=["No"])
    contract: str = Field(examples=["Month-to-month"])
    paperless_billing: str = Field(examples=["Yes"])
    payment_method: str = Field(examples=["Electronic check"])
    monthly_charges: float = Field(examples=[70.35])
    total_charges: float = Field(examples=[845.50])

class ChurnPrediction(BaseModel):
    churn_probability: float
    churn_prediction: bool
