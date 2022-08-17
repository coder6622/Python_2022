# todo: 1
import datetime
import sys
from math import pi

sample_string = """
Twinkle, twinkle, little star,
	How I wonder what you are!
		Up above the world so high,
		Like a diamond in the sky.
Twinkle, twinkle, little star,
	How I wonder what you are
"""
print(sample_string)

# todo: 2. Write a Python program to get the Python version you are using
print('Current version python: ', sys.version)

# todo: 3. Write a Python program to display the current date and time.
now = datetime.datetime.now()
print('Current date and time: ', now.strftime('%Y-%m-%d %H:%M:%S'))

# todo: 4.  Write a Python program which accepts the radius of a
#  circle from the user and compute the area.
r = float(input('Input radius of a circle: '))
print('Area of a circle: ', str(pi * r ** 2))
# todo: 5. Write a Python program which accepts the user's first and last
#  name and print them in reverse order with a space between them
fistName = input('Enter first name: ')
lastName = input('Enter last name: ')
print('Your name: {0} {1}'.format(lastName, fistName))

# todo: 6. Write a Python program which accepts a sequence of comma-separated
#  numbers from user and generate a list and a tuple with those numbers

sequence_numbers = input('Enter a sequence of comma-separated numbers: ')
list_sequence_numbers = sequence_numbers.split(',')
tuple_sequence_numbers = tuple(list_sequence_numbers)
print('List: ', list_sequence_numbers)
print('Tuple: ', tuple_sequence_numbers)

# todo:  Write a Python program to accept a filename from the user and print
#  the extension of that
filename = input('Enter your file name: ')
filename_extension = filename.split('.')[-1]
print('Your file name extension: ', filename_extension)

# todo: 8. Write a Python program to display the first and last colors from
#  the following list
color_list = ["Red", "Green", "White", "Black"]
print('First colors in list: ', color_list[0])
print('Last colors in list: ', color_list[-1])

# todo: 9. Write a Python program to display the examination schedule. (
#  extract
#  the date from exam_st_date)
exam_st_date = (11, 12, 2014)
print('The examination will start from: %i/ %i/ %i' % exam_st_date)

# todo: 10. Write a Python program that accepts an integer (n) and computes
#  the
#  value of n+nn+nnn
n = 5
n1 = int("%s" % n)
n2 = int("%s%s" % (n, n))
n3 = int("%s%s%s" % (n, n, n))
print('The value of n+nn+nnn: ', n1 + n2 + n3)

# todo: 11. Write a Python program to print the documents (syntax,
#  description etc.) of Python built-in function(s).
print(abs.__doc__)

# todo: 12. Write a Python program to print the calendar of a given month and
#  year. Note : Use 'calendar' module.
import calendar

m = int(input('Enter the month: '))
y = int(input('Enter the year: '))

print(calendar.month(y, m))

# todo:  13. Write a Python program to print the following 'here document'.
#  Go to the editor
sample_string = '''a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example '''

print(sample_string)

# todo: 14. Write a Python program to calculate number of days between two
#  dates.
from datetime import date

first_day = date(2014, 7, 2)
last_day = date(2014, 7, 11)

delta = last_day.day - first_day.day
print('{0} days'.format(delta))

# todo: 15. Write a Python program to get the volume of a sphere with radius 6.
from math import pi

r = 6
V = 4.0 / 3.0 * pi * r ** 3
print('The volume of a spere: ', V)


# todo: 16. Write a Python program to get the difference between a given
#  number and 17, if the number is greater than 17 return double the absolute
#  difference.

def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2


print(difference(10))
print(difference(53))


# todo: 17. Write a Python program to test whether a number is within 100 of
#  1000 or 2000

def near_thousand(n):
    return (abs(1000 - n) <= 100) or (abs(2000 - n) <= 100)


print(near_thousand(8000))
print(near_thousand(100))


# todo: 18. Write a Python program to calculate the sum of three given
#  numbers, if the values are equal then return three times of their sum

def sum_three(a, b, c):
    sum_number = a + b + c

    if a == b == c:
        sum_number = sum_number * 3

    return sum_number


print(sum_three(1, 2, 3))


# todo: 19. Write a Python program to get a new string from a given string
#  where "Is" has been added to the front. If the given string already begins
#  with "Is" then return the string unchanged.
def add_is_string(s):
    if len(s) >= 2 and s[:2] == "Is":
        return s
    return "Is " + s


print(
    add_is_string('Hello world')
)


# todo: 20. Write a Python program to get a string which is n (non-negative
#  integer) copies of a given string.

def copy_string(s, count):
    result = ""
    for i in range(count):
        result += s
    return result


print(
    copy_string('long', 10)
)

# todo: 21. Write a Python program to find whether a given number (accept
#  from the user) is even or odd, print out an appropriate message to the user.

num = int(input('Enter your number: '))
if num & 1 == 1:
    print('Odd')
else:
    print('Even')

# todo: 22. Write a Python program to count the number 4 in a given list.
list_demo = [1, 2, 3, 4, 5, 6, 3, 3, 2, 4]


def count_4(list_in):
    count = 0
    for i in range(len(list_in)):
        if list_in[i] == 4:
            count += 1

    return count


print(count_4(list_demo))


# todo: 23. Write a Python program to get the n (non-negative integer)
#  copies of the first 2 characters of a given string. Return the n copies of
#  the whole string if the length is less than 2

def copying_substring(s, amount):
    substring = ""
    if len(s) < 2:
        substring = s[:len(s)]
    else:
        substring = s[:2]

    result = ""
    for i in range(amount):
        result += substring

    return result


print(copying_substring('loc', 5))


# todo: 24. Write a Python program to test whether a passed letter is a vowel
#  or not.
def ex_24(c):
    vowels = 'long'
    return c in vowels


print(ex_24('c'))
print(ex_24('o'))

# todo: 25.  Write a Python program to check whether a specified value is
#  contained in a group of values.
list_demo = [1, 2, 3, 4, 5, 6, 7, 2, 3]


def check_contain_num(num, listIn):
    for i in range(len(listIn)):
        if listIn[i] == num:
            return True
    return False


print(check_contain_num(10, list_demo))
