import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder   

df = pd.DataFrame({
    "Id": ['A', 'B', 'C', 'D', 'E'],
    "Grades": ['Poor', 'Average', 'Good', 'Excellent', 'Good']
})

le = LabelEncoder()

df["Label_Encoded"] = le.fit_transform(df["Grades"])

oe = OrdinalEncoder(
    categories=[['Poor', 'Average', 'Good', 'Excellent']]
)

df["Ordinal_Encoded"] = oe.fit_transform(df[["Grades"]])

print(df)

encoded_df = pd.get_dummies(df, columns=["Grades"], dtype=int)

print(encoded_df)