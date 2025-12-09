# Fraud Prediction Deployment API

This repository hosts the FastAPI service used to deploy the fraud detection machine learning model.  
It provides real-time fraud prediction using the trained Decision Tree model and optimized probability threshold.

---

## What This API Does

- Accepts **multiple transaction records**  
- Loads your trained model, threshold, and selected features  
- Returns:  
  - Fraud probability  
  - Final fraud / not-fraud classification  
  - Threshold used  

---

## Repository Structure

```
fraud-prediction-deployment/
│
├── main.py                       # FastAPI application
├── final_decision_tree_model.pkl # Trained ML model
├── fraud_best_threshold.pkl      # Tuned probability threshold
├── selected_features.pkl         # Feature list used during training
├── requirements.txt              # Dependencies
├── render.yaml                   # Render cloud deployment file
└── README.md
```

---

## API Endpoint

### **POST /predict**

Send multiple records:

```json
{
  "items": [
    {
      "feature1": 32.5,
      "feature2": 0.12,
      "feature3": 1
    }
  ]
}
```

### **Example Response**

```json
{
  "predictions": [
    {
      "fraud_probability": 0.87,
      "final_prediction": "Fraud",
      "threshold_used": 0.42
    }
  ]
}
```

---

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
uvicorn main:app --reload
```

View documentation at:

```
http://127.0.0.1:8000/docs
```

---

# Deployment (Render)

The `render.yaml` file enables:

- Automatic builds from GitHub  
- FastAPI server startup using Uvicorn  
- Free-tier cloud hosting  

Your live API will be available at:

```
https://your-service-name.onrender.com
```
# Test the Fraud Detection API (Try It on Google Colab)

You can easily test the deployed Fraud Detection API using Google Colab, Jupyter Notebook, or any Python environment that supports requests.

Just copy and run the code below:


import requests

API_URL = "https://fraud-project.onrender.com/predict"

# Sample batch of 5 transactions
transactions = [
    { "is_high_amount": 0.0, "cust_total_transactions": 2048.0, "time_of_day": 0.0, "category": 10.0, "cust_total_fraud": 8.0, "cust_fraud_rate": 0.00390625 },
    { "is_high_amount": 1.0, "cust_total_transactions": 2048.0, "time_of_day": 3.0, "category": 10.0, "cust_total_fraud": 8.0, "cust_fraud_rate": 0.00390625 },
    { "is_high_amount": 0.0, "cust_total_transactions": 2048.0, "time_of_day": 0.0, "category": 10.0, "cust_total_fraud": 50.0, "cust_fraud_rate": 0.00390625 },
    { "is_high_amount": 0.0, "cust_total_transactions": 2048.0, "time_of_day": 0.0, "category": 10.0, "cust_total_fraud": 8.0, "cust_fraud_rate": 0.390625 },
    { "is_high_amount": 0.0, "cust_total_transactions": 2048.0, "time_of_day": 0.0, "category": 10.0, "cust_total_fraud": 8.0, "cust_fraud_rate": 0.5390625 }
]

payload = {"items": transactions}

# Send POST request to the API
response = requests.post(API_URL, json=payload)

# Display result
if response.status_code == 200:
    print("✅ API Response:")
    print(response.json())
else:
    print(f"❌ Error {response.status_code}: {response.text}")
