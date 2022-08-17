danh_sach = [5, 7, 6, 9, 14, 26, 21, 17, 44]

even_number = list(filter(lambda x: x & 1 == 0, danh_sach))
print(even_number)

# todo: b Xuat cac so le khong chia het cho 3
so_le_chia_het_3 = list(filter(lambda x:
                               (x & 1 == 1) and
                               (x % 3 != 0),
                               danh_sach))
print(so_le_chia_het_3)


# todo: c Xuat cac so nguyen to

def KTNguyenTo(n):
    if n < 1:
        return 0
    for i in range(2, n):
        if n % i == 0:
            return 0

    return 1


so_nguyen_to = list(filter(
    lambda x: KTNguyenTo(x) == 1
    , danh_sach))

print('so nguyen to la: {}'.format(so_nguyen_to))
# todo: d Tinh tong cac so nguyen to
tong_cac_so_nguyen_to = sum(so_nguyen_to)
print(tong_cac_so_nguyen_to)
