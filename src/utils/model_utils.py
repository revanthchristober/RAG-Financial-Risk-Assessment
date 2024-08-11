# src/utils/model_utils.py

import joblib

def load_model(model_path: str):
    """Loads a pre-trained model."""
    try:
        model = joblib.load(model_path)
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

def save_model(model, model_path: str):
    """Saves a trained model."""
    try:
        joblib.dump(model, model_path)
        print(f"Model saved at {model_path}")
    except Exception as e:
        print(f"Error saving model: {e}")
