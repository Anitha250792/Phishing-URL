import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# ✅ Simple phishing dataset
data = {
    "url_length": [20, 35, 40, 18, 60, 70, 22, 55],
    "has_at": [0, 1, 1, 0, 1, 0, 0, 1],
    "has_dash": [0, 1, 0, 0, 1, 1, 0, 1],
    "dot_count": [1, 3, 4, 1, 5, 6, 1, 4],
    "has_https": [1, 0, 0, 1, 0, 1, 1, 0],
    "has_http": [0, 1, 1, 0, 1, 0, 0, 1],
    "digit_count": [0, 2, 3, 0, 5, 6, 0, 4],
    "label": [0, 1, 1, 0, 1, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df.drop("label", axis=1)
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

joblib.dump(model, "phishing_model.pkl")

print("✅ ML model trained and saved as phishing_model.pkl")
