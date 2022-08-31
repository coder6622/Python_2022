class PhanSo:
    def __init__(self, tu: int, mau: int) -> None:
        if mau == 0:
            raise ArithmeticError('Phan so khong the co mau bang 0')
        self.tu = tu
        self.mau = mau
        self.rutGon()

    def tinhGiaTriCuaPhanSo(self) -> float:
        return self.tu / self.mau

    @staticmethod
    def my_gcd_1(num1: int, num2: int):
        ucln = 1
        if num1 < num2:
            num = num1
        else:
            num = num2
        for i in range(2, num + 1):
            if num1 % i == 0 and num2 % i == 0:
                ucln = i
        return ucln

    # @staticmethod
    # def my_gcd_2(num1: int, num2: int):
    #     while num1 != num2:
    #         if num1 > num2:
    #             num1 -= num2
    #         else:
    #             num2 -= num1
    #     return num1

    @staticmethod
    def my_gcd3(num1: int, num2: int):
        while num2:
            num1, num2 = num2, num1 % num2
        return num1

    def my_gcd_4(self, num1: int, num2: int):
        if num2 == 0:
            return num1
        else:
            return self.my_gcd_4(num2, num1 % num2)

    def my_gcd_5(self, num1: int, num2: int):
        if num1 == 0 or num2 == 0:
            return num1 + num2

        if num1 == num2:
            return num1

        if num1 > num2:
            return self.my_gcd_5(num1 - num2, num2)

        else:
            return self.my_gcd_5(num1, num2 - num1)

    def rutGon(self):
        # todo: gcd: find the  the greatest common divisor of the two integers
        gcd = self.my_gcd_4(self.tu, self.mau)
        if gcd != 1:
            self.tu = self.tu // gcd
            self.mau = self.mau // gcd

    def __add__(self, other):
        result = PhanSo(self.tu * other.mau + self.mau * other.tu, self.mau *
                        other.mau)
        result.rutGon()
        return result

    def __sub__(self, other):
        result = PhanSo(self.tu * other.mau - self.mau * other.tu,
                        self.mau * other.mau)
        result.rutGon()
        return result

    def __mul__(self, other):
        result = PhanSo(self.tu * other.tu, self.mau * other.mau)
        result.rutGon()
        return result

    def __truediv__(self, other):
        result = PhanSo(self.tu * other.mau, self.mau * other.tu)
        result.rutGon()
        return result

    def __str__(self):
        if self.mau == 1:
            return f'{self.tu}'
        return f'{self.tu}/{self.mau}'


class DanhSachPhanSo:
    def __init__(self):
        self.dsps = []

    def themPhanSo(self, *args: PhanSo):
        for ps in args:
            self.dsps.append(ps)

    def xuat(self):
        for ps in self.dsps:
            print(ps, end="\t")

    def demPSAm(self) -> int:
        # todo: c1
        # count = 0
        # for i in self.dsps:
        #     if i.tu // i.mau < 0:
        #         count += 1
        # return count
        # todo: c2
        return sum(
            1 for ps in self.dsps if ps.tinhGiaTriCuaPhanSo() < 0)

    def timTatCaVTPhanSoX(self, phan_so: PhanSo):
        result = []
        for i in range(len(self.dsps)):
            if self.dsps[i].tinhGiaTriCuaPhanSo() == \
                    phan_so.tinhGiaTriCuaPhanSo():
                result.append(i)
        return result

    def timPhanSoDuongNhoNhat(self) -> PhanSo:
        # nho_nhat = 23628734638746384.0
        # result = PhanSo(0, 1)
        # for ps in self.dsps:
        #     gia = ps.giaTriNguyenCuaPhanSo()
        #     if 0.0 < gia < nho_nhat:
        #         nho_nhat = gia
        #         result = ps
        # return result
        return min([ps for ps in self
                   .dsps if ps.tinhGiaTriCuaPhanSo() > 0],
                   key=lambda ps: ps.tinhGiaTriCuaPhanSo())

    @staticmethod
    def ktPhanSoAm(ps: PhanSo):
        return ps.tu * ps.mau > 0

    def tinhTongCacPhanSoAm(self) -> PhanSo:
        result = PhanSo(0, 1)
        for ps in self.dsps:
            if self.ktPhanSoAm(ps):
                result = result.__add__(ps)
        return result

    def xoaPSX(self, phan_so: PhanSo) -> None:
        # vt = self.timTatCaVTPhanSoX(phan_so)
        # n = 0
        # for i in vt:
        #     self.dsps.pop(i - n)
        #     n += 1

        for ps in self.dsps:
            if ps.tinhGiaTriCuaPhanSo() == phan_so.tinhGiaTriCuaPhanSo():
                self.dsps.remove(ps)
                print(f'\nXoa thanh cong phan so {ps}', end="")
        print('\nXoa xong')

    def xoaTatCaPSCoTuLaX(self, tu: int) -> None:
        for ps in self.dsps:
            if ps.tu == tu:
                self.dsps.remove(ps)
                print(f'\nXoa thanh cong phan so {ps}', end="")
        print('\nXoa xong')

    def sapXepPhanSo(self, reverse: bool = False) -> None:
        self.dsps.sort(key=lambda ps: ps.tinhGiaTriCuaPhanSo(),
                       reverse=reverse)

    def sapXepPhanSoTheoTu(self, reverse: bool = False) -> None:
        self.dsps.sort(key=lambda ps: ps.tu, reverse=reverse)

    def sapXepPhanSoTheoMau(self, reverse: bool = False) -> None:
        self.dsps.sort(key=lambda ps: ps.mau, reverse=reverse)


phanSo1 = PhanSo(3, 3)
phanSo2 = PhanSo(-5, 2)
phanSo3 = PhanSo(100, 5)
phanSo4 = PhanSo(100, 100)
phanSo5 = PhanSo(2, 3)
phanSo6 = PhanSo(-8, 3)
phanSo7 = PhanSo(2, 3)
phanSo8 = PhanSo(-9, 3)
phanSo9 = PhanSo(-100, 3)
phanSo10 = PhanSo(100, 4)
# print(f'{phanSo1} + {phanSo2} = {phanSo1.__add__(phanSo2)} ')
# print(f'{phanSo1} - {phanSo2} = {phanSo1.__sub__(phanSo2)} ')
# print(f'{phanSo1} * {phanSo2} = {phanSo1.__mul__(phanSo2)} ')
# print(f'{phanSo1} : {phanSo2} = {phanSo1.__truediv__(phanSo2)} ')
# phanSo1.rutGon()
# phanSo2.rutGon()
# phanSo3.rutGon()
# phanSo4.rutGon()
# print(phanSo1)
# print(phanSo2)
# print(phanSo3)
# print(phanSo4)

dsPhanSo = DanhSachPhanSo()
dsPhanSo.themPhanSo(phanSo1, phanSo2, phanSo3, phanSo4, phanSo5,
                    phanSo6,
                    phanSo7, phanSo8, phanSo9, phanSo10)
print("Danh sach phan so la: ")
dsPhanSo.xuat()
# print(f"So phan so am la: {dsPhanSo.demPSAm()}")
# print(f"Phan so duong nho nhat la: {dsPhanSo.timPhanSoDuongNhoNhat()}")

# phanSoTim = PhanSo(2, 3)
# print(f"Cac vi tri phan so {phanSoTim} la: ")
# kq = dsPhanSo.TimTatCaVTPhanSoX(phanSoTim)
# for i in kq:
#     print(i + 1, end="\t")

# print(f'Tong cac phan so am la: {dsPhanSo.tinhTongCacPhanSoAm()}')

# dsPhanSo.xoaPSX(PhanSo(2, 3))

# dsPhanSo.xoaTatCaPSCoTuLaX(20)
# print(f'\nMang sau khi xoa: ')

print('\nSau khi sap xep: ')
# todo: if true giam
#  mac dinh tang
# dsPhanSo.sapXepPhanSo()
# dsPhanSo.sapXepPhanSo(True)
# dsPhanSo.sapXepPhanSoTheoTu()
# dsPhanSo.sapXepPhanSoTheoTu(True)
# dsPhanSo.sapXepPhanSoTheoMau()
# dsPhanSo.sapXepPhanSoTheoMau(True)
dsPhanSo.xuat()
