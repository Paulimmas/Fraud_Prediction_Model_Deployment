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
