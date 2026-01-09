import joblib
from pathlib import Path

# Load model files relative to this file so the module works regardless of current working directory.
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "risk_model.pkl"
VECTORIZER_PATH = BASE_DIR / "vectorizer.pkl"

try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
except FileNotFoundError as e:
    # Provide a clearer error message with instructions to the user.
    raise FileNotFoundError(
        f"{e}. Expected model files at '{BASE_DIR}'.\n"
        "Generate them by running 'train_model.py' from the 'compliance_alert_system' folder "
        "or place 'risk_model.pkl' and 'vectorizer.pkl' into that folder.")


def predict_ml_risk(text):
    X = vectorizer.transform([text])
    prob = model.predict_proba(X)[0]
    label = model.predict(X)[0]

    confidence = int(max(prob) * 100)
    risk_label = "High Risk" if label == 1 else "Low Risk"

    return risk_label, confidence
