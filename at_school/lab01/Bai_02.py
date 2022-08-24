# from math import sqrt
#
#
# # todo: 1
# def sum_a_b(a, b):
#     return a + b
#
#
# def a_div_b(a, b):
#     return a / b
#
#
# def a_exponential_b(a, b):
#     return a ** b
#
#
# print(sum_a_b(3, 5))
# print(a_div_b(2, 3))
# print(a_exponential_b(2, 3))
#
# # todo: 2
#
# from math import pi
#
#
# def CaculateAreaCircle(r):
#     return pi * r ** 2
#
#
# print(CaculateAreaCircle(2))
#
#
# # todo: 3
def KTNguyenTo(n):
    if n < 1:
        return 0
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1


#
#
# def XuatCacSoNguyenTo(start, end):
#     print(f'Cac so nguyen to trong khoang [{start}, {end}] la: ')
#     for i in range(start, end):
#         if KTNguyenTo(i) == 1:
#             print("{0} ".format(i))
#
#
# XuatCacSoNguyenTo(2, 10)
#
#
# # todo: 4. Kiểm tra 1 số nguyên n có phải là số Fibonacci hay không
def CheckIsFibonaci(n):
    a = 0
    b = 1
    while a <= n:
        if n == a:
            return True
        a, b = b, a + b
    return False


# print(
#     CheckIsFibonaci(13),
#     CheckIsFibonaci(10),
#     CheckIsFibonaci(8)
# )
#
#
# # todo: 5. Tìm số Fibonacci thứ n (dùng đệ quy và không đệ quy)
# # todo: de quy
# def FindFibonaciIndexN(n):
#     if n == 0:
#         return 0
#     elif n <= 2:
#         return 1
#     return FindFibonaciIndexN(n - 1) + FindFibonaciIndexN(n - 2)
#
#
# print(
#     FindFibonaciIndexN(0),
#     FindFibonaciIndexN(1),
#     FindFibonaciIndexN(2),
#     FindFibonaciIndexN(3),
#     FindFibonaciIndexN(4),
#     FindFibonaciIndexN(5),
#     FindFibonaciIndexN(6),
#     FindFibonaciIndexN(7),
#     FindFibonaciIndexN(8),
#     FindFibonaciIndexN(9),
#     FindFibonaciIndexN(10),
#     FindFibonaciIndexN(11)
# )
#
#
# #
# #
# # # todo: khong de quy
# #
# def FindFibonaciIndexNNotRecursive(n):
#     a = 0
#     b = 1
#     if n == 0:
#         return a
#     elif n <= 2:
#         return b
#     else:
#         for i in range(1, n):
#             c = a + b
#             a = b
#             b = c
#         return b
#
#
# print(
#     FindFibonaciIndexNNotRecursive(0),
#     FindFibonaciIndexNNotRecursive(1),
#     FindFibonaciIndexNNotRecursive(2),
#     FindFibonaciIndexNNotRecursive(3),
#     FindFibonaciIndexNNotRecursive(4),
#     FindFibonaciIndexNNotRecursive(5),
#     FindFibonaciIndexNNotRecursive(6),
#     FindFibonaciIndexNNotRecursive(7),
#     FindFibonaciIndexNNotRecursive(8),
#     FindFibonaciIndexNNotRecursive(9),
#     FindFibonaciIndexNNotRecursive(10),
#     FindFibonaciIndexNNotRecursive(11),
# )
#
#
# # todo: 6. Tính tổng n số Fibonacci đầu tiên (dùng đệ quy và không đệ quy)
# # todo: de quy
# def SumFibonaciRecursive(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return FindFibonaciIndexN(n) + SumFibonaciRecursive(n - 1)
#
#
# print(
#     SumFibonaciRecursive(0),
#     SumFibonaciRecursive(1),
#     SumFibonaciRecursive(2),
#     SumFibonaciRecursive(3),
#     SumFibonaciRecursive(4),
#     SumFibonaciRecursive(5),
#     SumFibonaciRecursive(6),
#     SumFibonaciRecursive(7),
#     SumFibonaciRecursive(8),
#     SumFibonaciRecursive(9),
#     SumFibonaciRecursive(10),
#     SumFibonaciRecursive(11),
# )
#
#
# # todo: not recursive
# def SumFibonaciNotRecursive(n):
#     result = 0
#     for i in range(n + 1):
#         result += FindFibonaciIndexNNotRecursive(i)
#     return result
#
#
# print(
#     SumFibonaciNotRecursive(0),
#     SumFibonaciNotRecursive(1),
#     SumFibonaciNotRecursive(2),
#     SumFibonaciNotRecursive(3),
#     SumFibonaciNotRecursive(4),
#     SumFibonaciNotRecursive(5),
#     SumFibonaciNotRecursive(6),
#     SumFibonaciNotRecursive(7),
#     SumFibonaciNotRecursive(8),
#     SumFibonaciNotRecursive(9),
#     SumFibonaciNotRecursive(10),
#     SumFibonaciNotRecursive(11),
# )
#
#
# # todo: 7. Tính tổng căn bậc 2 của n số nguyên đầu tiên
#
#
# def SumSquareRootOf2(n):
#     if n == 0:
#         return 0
#     return sqrt(n) + SumSquareRootOf2(n - 1)
#
#
# print(
#     SumSquareRootOf2(1),
#     SumSquareRootOf2(3),
#     SumSquareRootOf2(4)
# )

# # todo: 8. Giải phương trình bậc 2: ax2 + bx + c=0
# import math
#
#
# def GiaiPTBac2(a: int, b: int, c: int):
#     if a == 0 and b == 0:
#         print('Mot trong a, b phai khac 0')
#     if a == 0:
#         print(f'Phuong trinh co nghiem la: {-c - b}')
#     else:
#         delta = b ** 2 - 4 * a * c
#         if delta < 0:
#             print("Phuong trinh vo nghiem")
#         elif delta == 0:
#             print(f"Phuong trinh co nghiem kep x1 = x2 = {-b / (2 * a)}")
#         else:
#             print("Phuong trinh co 2 nghiem phan biet: ")
#             print(f"x1= {((-b) + math.sqrt(delta)) / 2 * a}")
#             print(f"x1= {((-b) - math.sqrt(delta)) / 2 * a}")
#
#
# GiaiPTBac2(2, 6, 4)
# GiaiPTBac2(1, 1, 6)
# GiaiPTBac2(0, 1, 6)


# # todo: 9.  Tính n!
# def GiaiThua(n):
#     if n == 0:
#         return 1
#     return n * GiaiThua(n - 1)
#
#
# print(GiaiThua(9))
# print(GiaiThua(10))
# print(GiaiThua(8))


# # todo: 10. In * dạng tam giác dưới như hình bên, đầu vào là số hàng(cột)
# def InTamGiac(n):
#     for i in range(0, n):
#         print("* ", end="")
#         for j in range(1, i + 1):
#             if j == i:
#                 print('* ', end="")
#             elif i == n - 1:
#                 print('* ', end="")
#             else:
#                 print('  ', end="")
#         print("\r")
#
#
# InTamGiac(8)
# InTamGiac(9)


# # todo: 11. Đổi giờ - phút – giây: thời gian đầu vào là giây được đổi thành
# #  giờ, phút, giây. Xuất kết quả ra màn hình dưới dạng: giờ:phút:giây. Ví dụ:
# #  soGiay = 3770 thì xuất ra màn hình 1:2:50
#
# def DoiGioPhutGiay(seconds: int):
#     gio = seconds // 360
#     du = seconds - gio * 360
#     phut = du // 60
#     giay = du - phut * 60
#
#     print(f"{gio}:{phut}:{giay}")
#
#
# DoiGioPhutGiay(3770)


# todo: 12. Cho một mảng số nguyên: (nên viết 2-3 cách)
mang = [1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 19, 23]
mang1 = [4, 6, 9, 6, 3, 4, 7, 8, 9, 16, 19, 17, 13]


# todo: a) Xuât tất cả các số lẻ không chia hết cho 5
def XuatCacSoLe(mang):
    print('Cac so le la: ', end="")
    for i in range(len(mang)):
        if mang[i] & 1 == 1:
            print(mang[i], end=" ")
    print('\r')


# XuatCacSoLe(mang)


# todo: b) Xuất tất cả các số Fibonacci
def XuatFibonaci(mang):
    print('Cac so Fibonaci la: ')
    for i in range(len(mang)):
        if CheckIsFibonaci(mang[i]):
            print(mang[i], end=" ")
    print('\r')


# XuatFibonaci(mang)
# XuatFibonaci(mang1)


# todo: c) Tim so nguyen to lon nhat

