import pandas as pd

df = pd.read_csv("Automobile_data.csv")

# todo: xuat du lieu doc duoc tu tap tin
# todo: mac dinh se hien thi 5 dong dau va 5 dong cuoi
print(df)
print(df.loc[df.price > 1000, ['index', 'company', 'horsepower']])

# todo: xuat 6 dong dau tien
print(df.head(6))

# todo: xuat 7 dong cuoi
print(df.tail(7))

# df = df[['company', 'price']][df.price == df['price'].max()]
# print(df)

car_Manufactures = df.groupby('company')
toyotaDf = car_Manufactures.get_group('toyota')
print(toyotaDf)
print(car_Manufactures)
print(df['company'].value_counts())

priceDfMax = car_Manufactures[['company', 'price']].max("price")
print(priceDfMax)
priceDfAverage = car_Manufactures[['company', 'price']].mean("price")
print(priceDfAverage)
