import pandas as pd
import matplotlib.pyplot as plt
import scipy
# import numpy as np
import seaborn as sns

df = pd.read_csv("student_performance.csv")
df = df.select_dtypes(include="number")
df3 = pd.read_csv("student.csv")
df3 = df3.select_dtypes(include="number")
df2 = df.corr(method="spearman")
df4 = df3.corr(method="spearman")

sns.heatmap(df2, cmap='coolwarm', annot=True ,vmax=1, vmin=-1)
# sns.heatmap(df4, cmap='coolwarm', annot=True ,vmax=1, vmin=-1)
plt.hist(df["Final_Score"], bins=6)
# plt.show()
