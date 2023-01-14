
import pandas as pd

df1 = pd.DataFrame()

print(type(df1))

print(df1)

print(df1.columns) # todo: in column
print(df1.index) # todo: in hàng



# todo: create dataframe from list nested
students_list = [
  ['Bob', 'William', 26, 'Computer Engineering', 86], ['Emma', 'Johnson', 23, 'Math', 92], 
  ['Sarah', 'Smith', 22, 'Chemistry', 95]
]
# students_df = pd.DataFrame(students_list)
students_df = pd.DataFrame(students_list, columns=['First_Name', 'Last_name', 'Age', 'Major', 'Score'], index=['bob@mail.com', 'Emma@mail.com', 'Sarah@mail.com'])
# print(students_df)


# todo: create dataframe from dictionary
students_dict = {
        'First_Name': ['Bob', 'Emma', 'Sarah'],
        'Last_Name': ['William', 'Johnson', 'Smith'],
        'Age': [26,23,22],
        'Major': ['Computer Engineering', 'Math', 'Chemistry'],
        'Score': [86,92,95],
      }

students_df2 = pd.DataFrame(students_dict)
# students_df2 = pd.DataFrame(students_dict, columns=['First_name', 'Age', 'City'])
print(students_df2)

# print(students_df2.columns)
# print(students_df2.index)
# print(students_df.index)

# print(students_df.shape) # todo: đếm số hàng và số cột (3 row, 5 column)

# print(students_df.head(2)) # todo: in 2 dòng đầu 
# print(students_df.tail(1)) # todo: in 1 dòng cuối
print(students_df)

print(students_df.info()) # todo: in kiểu dữ liệu ra và thông tin các cột ra (memory useage, dtypes,...)


print(students_df.describe()) # todo: xem một số thông tin cơ bản (tiêu chuẩn trung bình độ lệch, phần trăm của các cột số,...)




