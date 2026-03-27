import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib

TRAINING_DATA = [
    ([85, 5, 12], 2), ([90, 7, 15], 2), ([78, 4, 10], 2), ([92, 8, 18], 2),
    ([88, 6, 14], 2), ([80, 5, 11], 2), ([95, 10, 20], 2), ([76, 3, 9], 2),
    ([83, 6, 13], 2), ([87, 7, 16], 2),
    ([60, 2, 6], 1), ([65, 3, 7], 1), ([70, 2, 8], 1), ([55, 1, 5], 1),
    ([68, 3, 9], 1), ([62, 2, 6], 1), ([72, 4, 8], 1), ([58, 1, 4], 1),
    ([66, 2, 7], 1), ([74, 3, 10], 1),
    ([30, 0, 2], 0), ([25, 0, 1], 0), ([40, 1, 3], 0), ([35, 0, 2], 0),
    ([20, 0, 1], 0), ([45, 1, 4], 0), ([28, 0, 2], 0), ([38, 1, 3], 0),
    ([22, 0, 1], 0), ([42, 1, 3], 0),
]

LABEL_MAP = {0: "Reject", 1: "Maybe", 2: "Shortlist"}

def train_model():
    X = np.array([d[0] for d in TRAINING_DATA])
    y = np.array([d[1] for d in TRAINING_DATA])
    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)
    preds = model.predict(X)
    print("Accuracy:", accuracy_score(y, preds))
    print("Confusion Matrix:\n", confusion_matrix(y, preds))
    joblib.dump(model, "classifier_model.pkl")
    return model

def predict_label(model, match_score: float, years_exp: int, skill_count: int) -> str:
    features = np.array([[match_score, years_exp, skill_count]])
    label_id = model.predict(features)[0]
    return LABEL_MAP[label_id]