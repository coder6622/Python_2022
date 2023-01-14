import pandas as pd


df = pd.read_csv('Datasets/titanic.csv')

# print(df)

print(df.shape)

print(df.columns)

ages = df['Age']

# print(ages)
# print(type(ages))
# print(ages.mean())
# print(ages.max())

# print(df[['Name', 'Age']])

# print(df.iloc[1, [1,2,3,4]])
# print(df.iloc[0])

print(df.iloc[:5, :3])
print(df.iloc[[0, -1], -3:])


print(df.loc[(df['Sex'] == 'female') & (df['Age'] > 35)])
