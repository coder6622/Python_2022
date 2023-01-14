
import pandas as pd

df = pd.read_csv('Datasets/data_01.csv', skiprows=1, names=['a', 'b', 'c', 'd'])
# print(df)



df2 = pd.read_csv('Datasets/data_02.csv', header=None, names=['fname', 'lname', 'course', 'score'])
# print(df2)

df3 = pd.read_csv('Datasets/data_03.csv', sep='|')
# print(df3)
# print(len(df3.columns))

df4 = pd.read_csv('Datasets/data_04.csv', comment='#', sep='\t')
# print(df4)

df5 = pd.read_csv('Datasets/data_05.csv', skiprows=3)
print(df5)