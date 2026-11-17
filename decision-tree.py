import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree

df = pd.DataFrame({
    "SID": list(range(1, 31)),

    "Study_Hours": [
        "H", "L", "H", "L", "H", "M", "M", "L", "H", "M",
        "H", "L", "M", "H", "L", "H", "M", "L", "H", "M",
        "L", "H", "M", "H", "L", "M", "H", "L", "M", "H"
    ],

    "Attendance": [
        "H", "H", "L", "L", "H", "H", "M", "L", "H", "M",
        "H", "L", "H", "H", "M", "H", "M", "L", "H", "M",
        "L", "H", "M", "H", "L", "H", "H", "M", "L", "H"
    ],

    "Previous_Result": [
        "H", "L", "H", "L", "H", "M", "M", "L", "H", "M",
        "H", "L", "M", "H", "L", "H", "M", "L", "H", "M",
        "L", "H", "M", "H", "L", "M", "H", "L", "M", "H"
    ],

    "Performance": [
        "Pass", "Fail", "Pass", "Fail", "Pass", "Pass", "Pass", "Fail", "Pass", "Pass",
        "Pass", "Fail", "Pass", "Pass", "Fail", "Pass", "Pass", "Fail", "Pass", "Pass",
        "Fail", "Pass", "Pass", "Pass", "Fail", "Pass", "Pass", "Fail", "Pass", "Pass"
    ]
})

X = df[["Study_Hours", "Attendance", "Previous_Result"]]
y = df["Performance"]

ob = OrdinalEncoder(categories=[["L", "M" , "H"]] * 3)
X[["Study_Hours", "Attendance", "Previous_Result"]] = ob.fit_transform(X)

X_Train, X_Test, Y_Train, Y_Test = train_test_split(
    X, y, random_state=42, train_size=0.9, stratify=y
)

model = DecisionTreeClassifier(criterion="gini", random_state=42)
model.fit(X_Train, Y_Train)

print("Test Accuracy:", model.score(X_Test, Y_Test))
print(export_text(model, feature_names=list(X.columns)))

plt.figure(figsize=(8, 5))
plot_tree(
    model,
    feature_names=list(X.columns),
    class_names=list(model.classes_),
    filled=True,
)
plt.show()
