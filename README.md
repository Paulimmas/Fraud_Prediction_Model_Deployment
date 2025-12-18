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

Feature Encoding & Interpretation

This project uses numerical encodings for categorical and time-based features to enable efficient model training and inference. The official mappings used are documented below to ensure correct interpretation and reproducibility.

Time of Day (time_of_day)

The time_of_day feature represents the period of the day when a transaction occurred.
It is encoded into four discrete values based on hour ranges:

Value	Time Range	Description

| Value | Time Range        | Description              |
|-------|-------------------|--------------------------|
| 3     | 21:00 – 04:59     | Late Night / Early Morning |
| 2     | 05:00 – 11:59     | Morning                  |
| 0     | 12:00 – 16:59     | Afternoon                |
| 1     | 17:00 – 20:59     | Evening                  |


Example:
A transaction occurring at 22:30

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

---

## How to Run the Fraud Prediction Test Code (Automatic Method Recommended)

There are **two ways** to test the API:

---

### **1️Manual Method (JSON Copy-and-Paste Method)**

This method is useful if you prefer to test your API **directly inside the FastAPI Swagger UI**.

* I have already generated the **correct JSON payloads** (single and bulk).
* The user simply needs to **copy the JSON** exactly as provided.
* Then paste it inside the **“items” field** on the FastAPI interface at:

 [https://fraud-project.onrender.com/docs](https://fraud-project.onrender.com/docs)

* After pasting, click **“Execute”** to run the prediction.

This method is simple, but some users may still find JSON formatting tricky — especially beginners — which is why the automatic approach below is recommended.

### === JSON Payload for Single Fraud Prediction ===
```json
{
    "items": [
        {
            "is_high_amount": 1.0,
            "cust_total_transactions": 485.0,
            "time_of_day": 3.0,
            "category": 4.0,
            "cust_total_fraud": 4.0,
            "cust_fraud_rate": 0.008247422680412371
        }
    ]
}
```

### === JSON Payload for Bulk Fraud Prediction ===

```json
{
    "items": [
        {
            "is_high_amount": 1,
            "cust_total_transactions": 1525,
            "time_of_day": 0,
            "category": 4,
            "cust_total_fraud": 11,
            "cust_fraud_rate": 0.007213114754098361
        },
        {
            "is_high_amount": 1,
            "cust_total_transactions": 485,
            "time_of_day": 3,
            "category": 4,
            "cust_total_fraud": 4,
            "cust_fraud_rate": 0.008247422680412371
        },
        {
            "is_high_amount": 1,
            "cust_total_transactions": 1033,
            "time_of_day": 3,
            "category": 11,
            "cust_total_fraud": 8,
            "cust_fraud_rate": 0.007744433688286544
        },
        {
            "is_high_amount": 1,
            "cust_total_transactions": 1036,
            "time_of_day": 3,
            "category": 4,
            "cust_total_fraud": 7,
            "cust_fraud_rate": 0.006756756756756757
        },
        {
            "is_high_amount": 1,
            "cust_total_transactions": 2611,
            "time_of_day": 3,
            "category": 4,
            "cust_total_fraud": 12,
            "cust_fraud_rate": 0.004595940252776714
        }
    ]
}
```

---

### **2️⃣ Automatic Method (Recommended for Beginners)**

This approach uses a Python script to **send the JSON automatically** to the API — no manual formatting required.
This is the easiest and cleanest method.

---

## How to Run the Automatic Method in Google Colab

You can test the API using the code snippet directly in **Google Colab**, with **no setup and no installations** required.

### Follow these quick steps:

1. Open Google Colab:
   [https://colab.research.google.com/](https://colab.research.google.com/)

2. Click **New Notebook**.

3. Copy and paste the entire code block into a new code cell.

4. Run the cell by pressing **Shift + Enter** or clicking the **Run ▶️** button.

5. Colab will send the request automatically and print the API’s fraud prediction response.

### Single Fraud Transaction — API Prediction Test

```python
import requests
import json

# API URL
url = "https://fraud-project.onrender.com/predict"

# Single fraud JSON payload
single_payload = {
    "items": [
         {
            "is_high_amount": 1.0,
            "cust_total_transactions": 485.0,
            "time_of_day": 3.0,
            "category": 4.0,
            "cust_total_fraud": 4.0,
            "cust_fraud_rate": 0.008247422680412371
        }
    ]
}

# Send request
response = requests.post(url, json=single_payload)

# Print output nicely
print("=== Single Transaction Prediction ===")
try:
    print(json.dumps(response.json(), indent=4))
except:
    print("Error decoding API response")
    print(response.text)

```

### Bulk Fraud Transactions — Testing Batch Predictions via API
```python
import requests
import json

# API URL
url = "https://fraud-project.onrender.com/predict"

# Bulk fraud JSON payload (5 records)
bulk_payload = {
    "items": [
        {
            "is_high_amount": 1,
            "cust_total_transactions": 1525,
            "time_of_day": 0,
            "category": 4,
            "cust_total_fraud": 11,
            "cust_fraud_rate": 0.007213114754098361
        },
        {
            "is_high_amount": 1,
            "cust_total_transactions": 485,
            "time_of_day": 3,
            "category": 4,
            "cust_total_fraud": 4,
            "cust_fraud_rate": 0.008247422680412371
        },
        {
            "is_high_amount": 1,
            "cust_total_transactions": 1033,
            "time_of_day": 3,
            "category": 11,
            "cust_total_fraud": 8,
            "cust_fraud_rate": 0.007744433688286544
        },
        {
            "is_high_amount": 1,
            "cust_total_transactions": 1036,
            "time_of_day": 3,
            "category": 4,
            "cust_total_fraud": 7,
            "cust_fraud_rate": 0.006756756756756757
        },
        {
            "is_high_amount": 1,
            "cust_total_transactions": 2611,
            "time_of_day": 3,
            "category": 4,
            "cust_total_fraud": 12,
            "cust_fraud_rate": 0.004595940252776714
        }
    ]
}

# Send request
response = requests.post(url, json=bulk_payload)

# Print output nicely
print("=== Bulk (5 Transactions) Prediction ===")
try:
    print(json.dumps(response.json(), indent=4))
except:
    print("Error decoding API response")
    print(response.text)


```


