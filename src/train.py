"""Treino do modelo baseline a partir dos módulos de src/.

Uso: python -m src.train
"""

from pathlib import Path

import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from src.preprocessing import (
    build_preprocessing_pipeline,
    clean_raw_data,
    load_raw_data,
    split_features_target,
)

RANDOM_STATE = 42
DATA_PATH = Path("data") / "telco_customer_churn_original.xlsx"
MODEL_PATH = Path("models") / "champion_model.joblib"


def train_baseline():
    df = clean_raw_data(load_raw_data(DATA_PATH))
    X, y = split_features_target(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=RANDOM_STATE, stratify=y
    )

    model = Pipeline(
        [
            ("preprocessing", build_preprocessing_pipeline()),
            (
                "classifier",
                LogisticRegression(max_iter=1000, random_state=RANDOM_STATE),
            ),
        ]
    )
    model.fit(X_train, y_train)

    y_proba = model.predict_proba(X_test)[:, 1]
    f1 = f1_score(y_test, model.predict(X_test))
    auc = roc_auc_score(y_test, y_proba)
    print(f"F1-score: {f1:.4f} | AUC-ROC: {auc:.4f}")

    MODEL_PATH.parent.mkdir(exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"Modelo salvo em {MODEL_PATH}")

    return model


if __name__ == "__main__":
    train_baseline()
