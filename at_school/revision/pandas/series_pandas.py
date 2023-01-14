
import pandas as pd

# df = pd.read_csv("");

# print(pd.__version__)



# s1 = pd.Series()

# print(s1)

# s2 = pd.Series([1,2,3,4,5])
# print(s2)

# print(s2.index)

# s3 = pd.Series([1,2,3,4,5], index= [10,20,30,40,50])
# print(s3)
# # todo:  tạo mảng điểm vs index kiểu chuỗi
# scores = pd.Series([3.2,4.5,2.6,5,3.8], index=['Bob', 'Gorge', 'Alex', 'Fiona', 'Sarah'])
# print(scores)

# # todo: in mảng điểm kiểu chuỗi
# print(scores.index)

# todo: tạo series bằng dictionary
d = {'Bob': 3.2, 'Gorge': 4.5, 'Alex': 2.6, 'Fiona': 5,'Sarah': 3.8}

s4 = pd.Series(d)

print(s4)
print(s4.index) # todo: xem key
print(s4.values) # todo: xem giá trị




