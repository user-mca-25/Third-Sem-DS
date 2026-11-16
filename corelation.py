import pandas as pd
import matplotlib.pyplot as plt
import scipy

df = pd.read_csv("student_performance.csv")

print("Attendence",df["Attendance"].corr(df["Final_Score"]))
print("Attendence",df["Attendance"].corr(df["Final_Score"], method= 'spearman'))

print("internet",df["Internet_Hours"].corr(df["Final_Score"]))
print("internet",df["Internet_Hours"].corr(df["Final_Score"], method= 'spearman'))


plt.scatter(df["Study_Hours"],df["Final_Score"])
plt.xlabel("Study_Hours")
plt.ylabel("Score")
plt.show()
