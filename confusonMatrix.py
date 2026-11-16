import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

data = {
    "movement": [8,1,7,0,9,2,6,1,8,0],
    "whisper": [3,0,2,0,4,0,3,0,4,0],
    "cheating": [1,0,1,0,1,0,1,0,1,0]
}

df = pd.DataFrame(data)

X = df[["movement", "whisper"]]
y = df["cheating"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

TN, FP, FN, TP = cm.ravel()

print("=== Confusion Matrix ===")
print(cm)
print()
print(f"True Positive (TP) = {TP}")
print(f"False Positive (FP) = {FP}")
print(f"True Negative (TN) = {TN}")
print(f"False Negative (FN) = {FN}")
print()
print("=== Performance Metrics ===")
print(f"Accuracy = {accuracy:.2f}")
print(f"Precision = {precision:.2f}")
print(f"Recall = {recall:.2f}")
