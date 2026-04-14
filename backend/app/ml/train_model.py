import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# ✅ Load dataset (make sure it has these columns)
data = pd.read_csv("data/loan_data.csv")

# ✅ Rename or create columns to match your backend
# If your dataset has similar columns, adjust these mappings
data = data.rename(columns={
    "ApplicantIncome": "income",
    "LoanAmount": "loan_amount",
    "Credit_History": "credit_score",
    "Age": "age"  # add this if dataset has 'Age' column
})

# ✅ Prepare features (must match backend)
X = data[["age", "income", "loan_amount", "credit_score"]]
y = data["Loan_Status"].apply(lambda x: 1 if x == "Y" else 0)

# ✅ Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# ✅ Save model
joblib.dump(model, "app/ml/model.pkl")
print("✅ Model trained and saved at app/ml/model.pkl")
