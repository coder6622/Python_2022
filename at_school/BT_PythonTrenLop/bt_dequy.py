# todo: a Tinh n!
def GiaiThua(n):
    if n == 0:
        return 1
    return n * GiaiThua(n - 1)


# print(GiaiThua(10))


# todo: b Fibonanci

def TinhFibonaci(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    return TinhFibonaci(n - 1) + TinhFibonaci(n - 2)


# todo:  c Tong cac so le
def TinhTongCacSoLe(n):
    print(n)
    if n == 0:
        return 0
    elif n & 1 == 0:
        return TinhTongCacSoLe(n - 1)

    return n + TinhTongCacSoLe(n - 1)


print(TinhTongCacSoLe(10))

# todo: tong cac so le trong mang
danh_sach_can_tinh = [1, 4, 9, 6, 3, 2, 9, 5, 9, 3, 4, 5]


def TinhTongCacSoLeTrongMang(danh_sach):
    if len(danh_sach) == 0:
        return 0
    phan_tu_cuoi = len(danh_sach) - 1
    a = danh_sach[phan_tu_cuoi]
    if a & 1 == 0:
        danh_sach.pop()
        return TinhTongCacSoLeTrongMang(danh_sach)

    danh_sach.pop()
    return a + TinhTongCacSoLeTrongMang(danh_sach)


print(TinhTongCacSoLeTrongMang(danh_sach_can_tinh))
