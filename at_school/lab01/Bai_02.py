# todo: 1
def sum_a_b(a, b):
    return a + b


def a_div_b(a, b):
    return a / b


def a_exponential_b(a, b):
    return a ** b


print(sum_a_b(3, 5))
print(a_div_b(2, 3))
print(a_exponential_b(2, 3))


# todo: 2

from math import pi


def CaculateAreaCircle(r):
    return pi * r ** 2


print(CaculateAreaCircle(2))

# todo: 3
def KTNguyenTo(n):
    if n < 1:
        return 0
    for i in range(2, n):
        if n % i == 0:
            return 0

    return 1


def XuatCacSoNguyenTo(start, end):
    print(f'Cac so nguyen to trong khoang [{start}, {end}] la: ')
    for i in range(start, end):
        if KTNguyenTo(i) == 1:
            print("{0} ".format(i))

XuatCacSoNguyenTo(2, 10)

# todo: 4. Kiểm tra 1 số nguyên n có phải là số Fibonacci hay không

def CheckIsFibonaci(n):
    a = 0
    b = 1
    while a <= n:
        if n == a:
            return True
        a, b = b, a + b
    return False


print(
    CheckIsFibonaci(13),
    CheckIsFibonaci(10),
    CheckIsFibonaci(8)
)


# todo: 5. Tìm số Fibonacci thứ n (dùng đệ quy và không đệ quy)
# todo: de quy
def FindFibonaciIndexN(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    return FindFibonaciIndexN(n - 1) + FindFibonaciIndexN(n - 2)


print(
    FindFibonaciIndexN(0),
    FindFibonaciIndexN(1),
    FindFibonaciIndexN(2),
    FindFibonaciIndexN(3),
    FindFibonaciIndexN(4),
    FindFibonaciIndexN(5),
    FindFibonaciIndexN(6),
    FindFibonaciIndexN(7),
    FindFibonaciIndexN(8),
    FindFibonaciIndexN(9),
    FindFibonaciIndexN(10),
    FindFibonaciIndexN(11)
)


#
#
# # todo: khong de quy
#
def FindFibonaciIndexNNotRecursive(n):
    a = 0
    b = 1
    if n == 0:
        return a
    elif n <= 2:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b


print(
    FindFibonaciIndexNNotRecursive(0),
    FindFibonaciIndexNNotRecursive(1),
    FindFibonaciIndexNNotRecursive(2),
    FindFibonaciIndexNNotRecursive(3),
    FindFibonaciIndexNNotRecursive(4),
    FindFibonaciIndexNNotRecursive(5),
    FindFibonaciIndexNNotRecursive(6),
    FindFibonaciIndexNNotRecursive(7),
    FindFibonaciIndexNNotRecursive(8),
    FindFibonaciIndexNNotRecursive(9),
    FindFibonaciIndexNNotRecursive(10),
    FindFibonaciIndexNNotRecursive(11),
)


# todo: 6. Tính tổng n số Fibonacci đầu tiên (dùng đệ quy và không đệ quy)
# todo: de quy
def SumFibonaciRecursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return FindFibonaciIndexN(n) + SumFibonaciRecursive(n - 1)


print(
    SumFibonaciRecursive(0),
    SumFibonaciRecursive(1),
    SumFibonaciRecursive(2),
    SumFibonaciRecursive(3),
    SumFibonaciRecursive(4),
    SumFibonaciRecursive(5),
    SumFibonaciRecursive(6),
    SumFibonaciRecursive(7),
    SumFibonaciRecursive(8),
    SumFibonaciRecursive(9),
    SumFibonaciRecursive(10),
    SumFibonaciRecursive(11),
)


# todo: not recursive
def SumFibonaciNotRecursive(n):
    result = 0
    for i in range(n + 1):
        result += FindFibonaciIndexNNotRecursive(i)
    return result


print(
    SumFibonaciNotRecursive(0),
    SumFibonaciNotRecursive(1),
    SumFibonaciNotRecursive(2),
    SumFibonaciNotRecursive(3),
    SumFibonaciNotRecursive(4),
    SumFibonaciNotRecursive(5),
    SumFibonaciNotRecursive(6),
    SumFibonaciNotRecursive(7),
    SumFibonaciNotRecursive(8),
    SumFibonaciNotRecursive(9),
    SumFibonaciNotRecursive(10),
    SumFibonaciNotRecursive(11),
)

# todo: 7. Tính tổng căn bậc 2 của n số nguyên đầu tiên
from math import sqrt


def SumSquareRootOf2(n):
    if n == 0:
        return 0
    return sqrt(n) + SumSquareRootOf2(n - 1)

print(
    SumSquareRootOf2(1),
    SumSquareRootOf2(3),
    SumSquareRootOf2(4)
)



