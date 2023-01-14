
import pandas as pd

df = pd.read_csv('datasets/employees.csv')

# print(df)

print(df.columns)

df.rename({'First Name': 'First_Name', 'Bonus %': 'Bonus'}, axis=1,inplace=True )
print(df)


df['Bonus2'] = df.Bonus.round()
print(df)