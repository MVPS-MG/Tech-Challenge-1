import pandas as pd

from src.preprocessing import clean_raw_data


def test_clean_raw_data_drops_leakage_and_fixes_total_charges():
    df = pd.DataFrame(
        {
            "CustomerID": ["0001-AAA"],
            "Count": [1],
            "City": ["City"],
            "State": ["State"],
            "Country": ["US"],
            "Zip Code": [12345],
            "Lat Long": ["0,0"],
            "Latitude": [0.0],
            "Longitude": [0.0],
            "CLTV": [1000],
            "Churn Score": [50],
            "Churn Label": ["No"],
            "Churn Reason": [None],
            "Churn Value": [0],
            "Tenure Months": [0],
            "Total Charges": [" "],
        }
    )

    cleaned = clean_raw_data(df)

    # Colunas de vazamento de dado não podem sobrar como feature
    assert "Churn Label" not in cleaned.columns
    assert "Churn Reason" not in cleaned.columns

    # Churn Value vira a coluna target
    assert "target" in cleaned.columns
    assert "Churn Value" not in cleaned.columns

    # Total Charges em branco vira NaN numérico, pronto para o imputer
    assert pd.api.types.is_numeric_dtype(cleaned["Total Charges"])
    assert cleaned["Total Charges"].isna().all()
