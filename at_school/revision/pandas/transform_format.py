
import pandas as pd

df = pd.read_csv('datasets/employees.csv')

# print(df)

# print(df.Gender.isna().sum())

print(pd.Categorical(df.Gender))