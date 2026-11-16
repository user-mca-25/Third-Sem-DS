import pandas as pd 
import matplotlib.pyplot as plt


df = pd.read_csv("student.csv")

plt.scatter(df["gender"],df["mark"])
plt.ylabel("Marks")

plt.show()
