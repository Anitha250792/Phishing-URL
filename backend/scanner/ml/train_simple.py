# backend/scanner/ml/train_simple.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from joblib import dump
from feature_extractor import extract_lexical_features
import os
import sys

# expects data/phishing.csv and data/benign.csv with a "url" column
BASE = os.path.dirname(__file__)
data_dir = os.path.join(BASE, "data")
phish = pd.read_csv(os.path.join(data_dir, "phishing.csv"))  # label=1
phish["label"] = 1
benign = pd.read_csv(os.path.join(data_dir, "benign.csv"))   # label=0
benign["label"] = 0

df = pd.concat([phish, benign]).reset_index(drop=True)

# extract features
X = []
for u in df["url"].astype(str):
    f = extract_lexical_features(u)
    X.append([f["url_length"], f["num_dots"], f["has_https"], f["has_at"], f["has_ip"], f["num_hyphens"], f["suspicious_keyword"]])
X = pd.DataFrame(X, columns=["url_length","num_dots","has_https","has_at","has_ip","num_hyphens","suspicious_keyword"])
y = df["label"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

from sklearn.metrics import classification_report
preds = model.predict(X_test)
print(classification_report(y_test, preds))

# save model and feature columns
os.makedirs(os.path.join(BASE, "models"), exist_ok=True)
dump((model, list(X.columns)), os.path.join(BASE, "models", "model.joblib"))
print("Saved model to models/model.joblib")
