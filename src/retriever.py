# src/retriever.py

import pandas as pd

class DataRetriever:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_data(self) -> pd.DataFrame:
        """Loads data from a CSV file."""
        try:
            df = pd.read_csv(self.file_path)
            return df
        except Exception as e:
            print(f"Error loading data: {e}")
            return pd.DataFrame()
