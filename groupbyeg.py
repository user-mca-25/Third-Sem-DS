import pandas as pd
import numpy as np

df = pd.read_csv("student_performance.csv")

for i in df.groupby(["Department","Gender"])["Final_Score"]:
    print(i)