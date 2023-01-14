
import pandas as pd

df = pd.read_csv('datasets/Automobile_data.csv')

# print(df)
# todo: 
# print(df.dtypes)
# print(df.describe())
# print(df.memory_usage())
# print(df.info())

# print(df.columns)


congtyXeOToMatNhat = df.loc[df.price == df.price.max(),['company', 'price']]
print(congtyXeOToMatNhat)


company_car = df.groupby('company')
toyotaDf = company_car.get_group("toyota")
# print(toyotaDf)


# print(df.company.value_counts())

print(company_car[['company', 'price']].mean('price'))
