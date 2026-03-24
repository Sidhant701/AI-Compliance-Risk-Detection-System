# AI Compliance Risk Detection System

## Overview
This project is a CLI-based AI system designed to detect compliance risks in communication text such as emails or chat messages. It simulates real-world regulatory monitoring systems used in AI-driven SaaS platforms.

## Features
- Rule-based compliance keyword detection
- AI-based risk classification using NLP
- Risk scoring system (0-100)
- Explainable alerts with flagged keywords
- CLI-based, lightweight, and fast

## Tech Stack
- Python 3.8+
- scikit-learn (TF-IDF, MultinomialNB)
- joblib (model serialization)

## How It Works
1. User inputs communication text
2. Rule-based engine checks compliance keywords
3. ML model predicts risk using NLP
4. Final risk score is computed using weighted logic
5. System outputs risk level and explanation

## Risk Scoring Logic
- Rule-based logic: 60%
- ML prediction confidence: 40%

## Setup (Windows / cmd)
1. Create a virtual environment and activate it:

```cmd
python -m venv .venv
.venv\Scripts\activate
```

2. Install dependencies:

```cmd
pip install -r requirements.txt
```

## Train the ML model (first run)
Run this once to generate `risk_model.pkl` and `vectorizer.pkl` inside `compliance_alert_system/`:

```cmd
cd compliance_alert_system
python train_model.py
```

## Run the app
```cmd
cd compliance_alert_system
python compliance_checker.py
```

## Sample Output
=== AI Compliance Risk Detection System ===
Enter communication text:
> insider information with accurate and highly confidential leak

--- Result ---
Risk Level     : 🚨 HIGH RISK
Risk Score     : 73/100
ML Prediction  : High Risk
Flagged Keywords:
 - insider information
 - confidential leak

## Notes
- The training data in `train_model.py` is intentionally tiny for demonstration.
- The ML model files are loaded relative to `ml_risk_model.py`, so it works even if you run the CLI from a different folder.
