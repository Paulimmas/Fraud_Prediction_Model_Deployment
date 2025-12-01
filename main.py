from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# -----------------------------
# Load Saved Model + Threshold + Features
# -----------------------------
model = joblib.load("final_decision_tree_model.pkl")
best_threshold = joblib.load("fraud_best_threshold.pkl")
selected_features = joblib.load("selected_features.pkl")


# -----------------------------
# Input Schema for BULK Prediction
# -----------------------------
class Transactions(BaseModel):
    items: list[dict]   # List of feature dictionaries


# -----------------------------
# FastAPI App
# -----------------------------
app = FastAPI(
    title="Fraud Detection API",
    description="API for predicting fraud from multiple transactions",
    version="1.1"
)

# -----------------------------
# Prediction Function
# -----------------------------
def predict_single(model, data_dict, threshold):
    values = []
    for feat in selected_features:
        if feat not in data_dict:
            raise ValueError(f"Missing feature '{feat}' in input data.")
        values.append(data_dict[feat])

    x = np.array(values).reshape(1, -1)
    prob = model.predict_proba(x)[0][1]
    pred = 1 if prob >= threshold else 0

    return {
        "fraud_probability": float(prob),
        "final_prediction": "Fraud" if pred == 1 else "Not Fraud",
        "threshold_used": float(threshold)
    }


# -----------------------------
# Bulk Prediction Endpoint
# -----------------------------
@app.post("/predict")
def predict(transactions: Transactions):
    results = []
    for item in transactions.items:
        result = predict_single(model, item, best_threshold)
        results.append(result)
    return {"predictions": results}
