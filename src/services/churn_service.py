from pathlib import Path

import joblib
import pandas as pd
from fastapi import HTTPException

from src.models.churnModel import FIELD_TO_COLUMN, ChurnPrediction, CustomerFeatures

MODEL_PATH = Path("models") / "champion_model.joblib"

_model = None


def get_model():
    """Carrega o modelo sob demanda (lazy), para que /health responda
    mesmo se o modelo ainda não tiver sido treinado."""
    global _model
    if _model is None:
        if not MODEL_PATH.exists():
            raise HTTPException(
                status_code=503,
                detail=(
                    f"Modelo não encontrado em {MODEL_PATH}. "
                    "Rode 'python -m src.train'."
                ),
            )
        _model = joblib.load(MODEL_PATH)
    return _model


def predict_customer(customer: CustomerFeatures) -> ChurnPrediction:
    model = get_model()
    payload = customer.model_dump()
    row = {FIELD_TO_COLUMN[field]: value for field, value in payload.items()}
    X = pd.DataFrame([row])
    churn_probability = float(model.predict_proba(X)[0, 1])
    return ChurnPrediction(
        churn_probability=round(churn_probability, 4),
        churn_prediction=churn_probability >= 0.5,
    )
