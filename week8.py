import numpy as np
import pandas as pd 

arr = np.array([
    [2,3,4],
    [5,8,9],
    [1,5,7]
])
print("sum across rows")
print(arr.sum(axis=1))
print("sum across columns")
print(arr.sum(axis=0))
print("mean across rows")
print(arr.mean(axis=1))
print("mean across columns")
print(arr.mean(axis=0))
print("median across rows")
print(np.median(arr,axis=1))
print("median across columns")
print(np.median(arr,axis=0))

series = pd.Series([1,2,3,4,5])

print(series)

data = {
    "name" : ["faheem", "arsalan"],
    "rollNo" : [1,2],
    "Major" : ["bas.it","msc.It"]
}

df = pd.DataFrame(data)
print()
print(df)

print()
print(df.ndim)

print()
print(df.shape)

print()
print(df.size)

print(df.index)
print()

print(df.values)
print()

print(df.loc[:,["name","rollNo"]])
print()

print(df.iloc[:1:,:2:])
print()