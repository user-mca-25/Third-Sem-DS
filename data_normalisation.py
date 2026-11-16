from sklearn.preprocessing import MinMaxScaler

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("student_performance.csv")
scaler = MinMaxScaler()
X = df["Student_ID"]
Y = scaler.fit_transform(df[["Final_Score"]])

plt.scatter(X,Y)
plt.show()