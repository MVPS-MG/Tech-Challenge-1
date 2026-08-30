"""Limpeza e pré-processamento de dados de clientes para o modelo de churn.

Reflete as decisões tomadas em notebooks/eda_baseline.ipynb (Etapa 1):
colunas com vazamento de dado (Churn Label, Churn Reason) e colunas
geográficas/irrelevantes são descartadas, e Total Charges é corrigida para
numérico. Imputação, escala e encoding ficam dentro do ColumnTransformer
retornado por build_preprocessing_pipeline, para que as estatísticas
aprendidas no treino sejam reaproveitadas de forma consistente também na
predição de uma única requisição da API.
"""

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

DROP_COLUMNS = [
    "CustomerID",
    "Count",
    "City",
    "State",
    "Country",
    "Zip Code",
    "Lat Long",
    "Latitude",
    "Longitude",
    "CLTV",
    "Churn Score",
    "Churn Label",
    "Churn Reason",
]

NUMERIC_FEATURES = ["Tenure Months", "Monthly Charges", "Total Charges"]

CATEGORICAL_FEATURES = [
    "Gender",
    "Senior Citizen",
    "Partner",
    "Dependents",
    "Phone Service",
    "Multiple Lines",
    "Internet Service",
    "Online Security",
    "Online Backup",
    "Device Protection",
    "Tech Support",
    "Streaming TV",
    "Streaming Movies",
    "Contract",
    "Paperless Billing",
    "Payment Method",
]

FEATURE_COLUMNS = NUMERIC_FEATURES + CATEGORICAL_FEATURES


def load_raw_data(path):
    return pd.read_excel(path)


def clean_raw_data(df):
    """Limpeza estrutural, igual para treino e inferência: renomeia a
    target, remove colunas de vazamento/irrelevantes e corrige o tipo de
    Total Charges (vinha como texto por causa de 11 registros em branco)."""
    df = df.copy()
    if "Churn Value" in df.columns:
        df = df.rename(columns={"Churn Value": "target"})
    df = df.drop(columns=[c for c in DROP_COLUMNS if c in df.columns])
    if "Total Charges" in df.columns:
        df["Total Charges"] = pd.to_numeric(df["Total Charges"], errors="coerce")
    return df


def split_features_target(df):
    """Separa features (apenas as colunas usadas pelo modelo) da target,
    quando presente (df de inferência não tem a coluna target)."""
    y = df["target"] if "target" in df.columns else None
    X = df[FEATURE_COLUMNS]
    return X, y


def build_preprocessing_pipeline():
    """ColumnTransformer não-ajustado: imputação (mediana/moda), escala das
    numéricas e one-hot das categóricas. Deve ser ajustado (fit) apenas nos
    dados de treino, dentro do Pipeline de modelagem."""
    numeric_pipeline = Pipeline(
        [
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )
    categorical_pipeline = Pipeline(
        [
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore", drop="first")),
        ]
    )
    return ColumnTransformer(
        [
            ("numeric", numeric_pipeline, NUMERIC_FEATURES),
            ("categorical", categorical_pipeline, CATEGORICAL_FEATURES),
        ]
    )
