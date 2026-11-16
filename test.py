import pandas as pd
import numpy as np



df = pd.DataFrame([[1,2,3],
                  [4,5,6],
                  [7,8,9]])

print(df)

print()
print()
print()
print(df.iloc[2:3:,2:3:])

print()
print()
print()
print(df.loc[2:3:,[0,1]])


dict = {"Name":["asif","basif","sasif"],
        "Class":[1,2,3],
        "Major":["General","Hafiz","Syed"]}

df2 = pd.DataFrame(dict)

print(df2)

print()
print()
print(df2.loc[1:1:,["Class"]])

print()
print()
print(df2.ndim)


