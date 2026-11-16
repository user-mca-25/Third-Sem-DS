import matplotlib.pyplot as plt
import pandas as pd

# df = pd.Series([10,20,30,40,50,60,70,80])
df = pd.Series([10,80,50,60,20,100])

q1 = df.quantile(.25)
q3 = df.quantile(.75)
iqr = q3 - q1
lb = q1 - (1.5 * iqr)
ub = q3 + (1.5 * iqr)

print(q1,q3,iqr,lb,ub)

# plt.hist(df, bins=4, edgecolor = 'black')
plt.boxplot(df)
plt.show()