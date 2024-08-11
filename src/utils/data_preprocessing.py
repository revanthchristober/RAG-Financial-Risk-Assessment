# src/utils/data_processing.py

import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Performs basic data cleaning."""
    df = df.dropna()
    df = df[df['financial_metric'] > 0]
    return df
