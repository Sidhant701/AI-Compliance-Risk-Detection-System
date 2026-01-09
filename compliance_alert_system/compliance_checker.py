import re
from compliance_keywords import HIGH_RISK_KEYWORDS, MEDIUM_RISK_KEYWORDS
from ml_risk_model import predict_ml_risk

def calculate_risk_score(high_hits, medium_hits):
    score = 0
    score += len(high_hits) * 40
    score += len(medium_hits) * 15
    return min(score, 100)

def check_compliance(text):
    text = text.lower()
    high_hits, medium_hits = [], []

    for k in HIGH_RISK_KEYWORDS:
        if re.search(rf"\b{re.escape(k)}\b", text):
            high_hits.append(k)

    for k in MEDIUM_RISK_KEYWORDS:
        if re.search(rf"\b{re.escape(k)}\b", text):
            medium_hits.append(k)

    rule_score = calculate_risk_score(high_hits, medium_hits)
    ml_label, ml_confidence = predict_ml_risk(text)

    final_score = int((rule_score * 0.6) + (ml_confidence * 0.4))

    if final_score >= 70:
        risk = "🚨 HIGH RISK"
    elif final_score >= 30:
        risk = "⚠️ MEDIUM RISK"
    else:
        risk = "✅ LOW RISK"

    return risk, final_score, high_hits + medium_hits, ml_label


def main():
    print("=== AI Compliance Risk Detection System ===")
    text = input("Enter communication text:\n> ")

    risk, score, reasons, ml_label = check_compliance(text)

    print("\n--- Result ---")
    print(f"Risk Level     : {risk}")
    print(f"Risk Score     : {score}/100")
    print(f"ML Prediction  : {ml_label}")

    if reasons:
        print("Flagged Keywords:")
        for r in reasons:
            print(f" - {r}")
    else:
        print("No risky keywords detected.")


if __name__ == "__main__":
    main()
