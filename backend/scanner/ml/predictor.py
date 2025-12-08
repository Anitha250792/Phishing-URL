# backend/scanner/ml/predictor.py
import random

def predict_url(url):
    suspicious_keywords = ["login", "verify", "free", "gift", "secure", "bank"]

    score = 0
    for word in suspicious_keywords:
        if word in url.lower():
            score += 25

    score += random.randint(5, 20)
    score = min(score, 100)

    if score > 70:
        verdict = "Malicious"
        reason = "Multiple phishing patterns detected."
    elif score > 40:
        verdict = "Suspicious"
        reason = "Some phishing indicators found."
    else:
        verdict = "Safe"
        reason = "No known phishing patterns detected."

    return verdict, score, reason
