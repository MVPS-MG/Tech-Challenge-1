from fastapi import APIRouter

from src.models.churnModel import ChurnPrediction, CustomerFeatures
from src.services.churn_service import predict_customer

router = APIRouter()


@router.post("/predict", response_model=ChurnPrediction)
def predict(customer: CustomerFeatures):
    return predict_customer(customer)
