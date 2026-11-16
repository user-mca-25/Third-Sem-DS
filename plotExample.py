import matplotlib.pyplot as plt
import numpy as np

#simple line graph
x = np.array([1,2,3,4,5])
y = np.array([100,90,110,80,70]) 

plt.plot(x,y, marker=".",markersize=20,mfc = "red", color="orange",linestyle = "dashed")
plt.title("Customer Record")
plt.xlabel("Date")
plt.ylabel("Customers")
plt.xticks(x)
plt.yticks(y)
plt.grid(color="lightgrey", linestyle = "dotted")
plt.show()

x1 = np.array(["Monday","Tuesday","Wednesday","Thursday"])
y1 = np.array([100,200,150,180])

#bar graph

plt.bar(x1,y1,edgecolor="black")
plt.show()

#pie graph

plt.pie(y1,labels=x1,explode = [0,0,0,0.2])
plt.show()

#scatter graph

plt.scatter(x,y)
plt.show()
