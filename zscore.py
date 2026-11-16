from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("student_performance.csv")
scaler = StandardScaler()

df2 = pd.DataFrame({
    "id": ["A","B","C","D","E","F", "G"],
    "marks": [20, 30, 40 , 50 , 60 , 70 , 80]
})


df2["z_score"] = scaler.fit_transform(df2[["marks"]])
df2["cut"] = pd.cut(df2["marks"], bins=3)
df2["q_cut"] = pd.qcut(df2["marks"], q=3)

df2["z_score2"] = scaler.fit_transform(df[["Final_Score"]])
df2["cut2"] = pd.cut(df["Final_Score"], bins=3)
df2["q_cut2"] = pd.qcut(df["Final_Score"], q=3)

print(df2)
