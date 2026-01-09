from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
from pathlib import Path

data = [
    ("urgent transfer required", 1),
    ("guaranteed returns promised", 1),
    ("confidential leak of data", 1),
    ("meeting scheduled tomorrow", 0),
    ("project update shared", 0),
    ("client discussion completed", 0)
]

texts, labels = zip(*data)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

# Save model files next to this script so they are found by the application regardless of CWD.
BASE_DIR = Path(__file__).resolve().parent
joblib.dump(model, BASE_DIR / "risk_model.pkl")
joblib.dump(vectorizer, BASE_DIR / "vectorizer.pkl")

print(f"ML model trained and saved to {BASE_DIR}")
