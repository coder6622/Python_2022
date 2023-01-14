
import pandas as pd

df = pd.read_csv('datasets/titanic.csv')
# print(df)

# print(df.isna().any())


df2 = df.dropna(axis=0)
print(df2)

print(df.shape, df2.shape)

df3 = pd.concat((df, df.iloc[:3]))
print(df3)
