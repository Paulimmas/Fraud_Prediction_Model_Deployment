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
Here is a corrected and improved version based on your clarification:

---

## 🚀 How to Run the Fraud Prediction Test Code (Automatic Method Recommended)

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

###  Nothing to install

Google Colab already includes **requests** and **json**, so the script runs instantly.

---

If you want, I can add a screenshot-style guide or a visual workflow to make it even easier for beginners.




