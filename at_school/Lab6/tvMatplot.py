import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales_data.csv')
print(df.info())
profitList = df['total_profit'].tolist()
print(profitList)
monthList = df['month_number'].tolist()
print(monthList)

plt.figure("Bieu do doan thang")
plt.plot(monthList, profitList, linestyle='-', marker='s', color='red')
plt.xlabel('Thang')
plt.xticks(monthList)
plt.ylabel('Loi nhuan ($)')
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.title('Loi nhuan hang thang nam 2021')
plt.show()
