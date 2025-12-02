# Fraud Prediction Deployment API

This repository hosts the FastAPI service used to deploy the fraud detection machine learning model.  
It provides real-time fraud prediction using the trained Decision Tree model and optimized probability threshold.

---

## 🚀 What This API Does

- Accepts **multiple transaction records**  
- Loads your trained model, threshold, and selected features  
- Returns:  
  - Fraud probability  
  - Final fraud / not-fraud classification  
  - Threshold used  

---

## 📁 Repository Structure

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

## 🔌 API Endpoint

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

## ▶️ Run Locally

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

## 🌐 Deployment (Render)

The `render.yaml` file enables:

- Automatic builds from GitHub  
- FastAPI server startup using Uvicorn  
- Free-tier cloud hosting  

Your live API will be available at:

```
https://your-service-name.onrender.com
```

---

## 📘 Author

Deployment completed as part of the **DerpTech Upskilling Programme (3MTT Initiative)**.













# Fraud Detection API

A FastAPI service for predicting fraud using a Decision Tree model and threshold tuning.

## Endpoint
POST /predict

## Send JSON like:
{
  "items": [
    {
      "feature1": 0.12,
      "feature2": 50,
      "feature3": 1,
      ...
    }
  ]
}
