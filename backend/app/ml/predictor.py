import joblib
import numpy as np

model = joblib.load("app/ml/model.pkl")

def predict_loan(data):
    features = np.array([[data["age"], data["income"], data["loan_amount"], data["credit_score"]]])
    prediction = model.predict_proba(features)[0][1]  # probability of approval
    return round(prediction * 100, 2)
