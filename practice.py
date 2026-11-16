from scipy.stats import pearsonr, norm
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x = [1,3,6,9,12]
y = [1,10,60,120,180]

print("Mean", stats.tmean(x))
print("Median", stats.scoreatpercentile(x,50))
print("Variance", stats.variation(x))
print("Standard Deviation", stats.tstd(x))

r, p = pearsonr(x,y)
print("Corelation ->",r)

df = pd.DataFrame({
    "x" : [1,3,6,9,12],
    "y" : [1,10,60,120,180]
})

df.loc[1, "x"] = 7

print("-----",df["x"])

df["z"] = ["a", "b", "c", "d", "e"]

print("Cor -> ", df["x"].corr(df["y"], method="spearman"))

x = np.linspace(-4,4,100)
y = norm.pdf(x,0,1)

plt.plot(x,y,color="red")
plt.show()

slope, interpept = np.polyfit(x, y, 1)
x_line = x
y_line = slope * x + interpept

plt.scatter(x, y)
plt.plot(x_line, y_line)
plt.show()
