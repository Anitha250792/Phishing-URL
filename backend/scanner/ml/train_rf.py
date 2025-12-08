# backend/scanner/ml/train_rf.py
import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score
from joblib import dump
from feature_extractor import extract_lexical_features

BASE = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE, "data")
MODEL_DIR = os.path.join(BASE, "models")
os.makedirs(MODEL_DIR, exist_ok=True)

# Expect phishing.csv and benign.csv in data/ with column "url"
phish_path = os.path.join(DATA_DIR, "phishing.csv")
benign_path = os.path.join(DATA_DIR, "benign.csv")

if not os.path.exists(phish_path) or not os.path.exists(benign_path):
    print("Place phishing.csv & benign.csv in", DATA_DIR)
    raise SystemExit(1)

phish = pd.read_csv(phish_path).assign(label=1)
benign = pd.read_csv(benign_path).assign(label=0)
df = pd.concat([phish, benign]).sample(frac=1, random_state=42).reset_index(drop=True)

# build feature matrix
rows = []
for url in df["url"].astype(str):
    f = extract_lexical_features(url)
    rows.append(f)
X = pd.DataFrame(rows)
y = df["label"]

# train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)
pred = model.predict(X_test)
probs = model.predict_proba(X_test)[:, 1]

print("Classification report:")
print(classification_report(y_test, pred))
print("ROC AUC:", roc_auc_score(y_test, probs))

# save model + columns order
dump({"model": model, "cols": list(X.columns)}, os.path.join(MODEL_DIR, "model.joblib"))
print("Saved model to", os.path.join(MODEL_DIR, "model.joblib"))
