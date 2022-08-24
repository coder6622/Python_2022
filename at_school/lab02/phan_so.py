import math


class PhanSo:
    def __init__(self, tu: int, mau: int) -> None:
        if mau == 0:
            raise ArithmeticError('Phan so khong the co mau bang 0')
        self.tu = tu
        self.mau = mau

    def rutGon(self):
        # todo: gcd: find the  the greatest common divisor of the two integers
        gcd = math.gcd(self.tu, self.mau)
        if gcd != 1:
            self.tu = self.tu // gcd
            self.mau = self.mau // gcd

    def __add__(self, other):
        result = PhanSo(0, 1)
        result.tu = self.tu * other.mau + self.mau * other.tu
        result.mau = self.mau * other.mau
        result.rutGon()
        return result

    def __sub__(self, other):
        result = PhanSo(0, 1)
        result.tu = self.tu * other.mau - self.mau * other.tu
        result.mau = self.mau * other.mau
        result.rutGon()
        return result

    def __mul__(self, other):
        result = PhanSo(0, 1)
        result.tu = self.tu * other.tu
        result.mau = self.mau * other.mau
        result.rutGon()
        return result

    def __truediv__(self, other):
        result = PhanSo(0, 1)
        result.tu = self.tu * other.mau
        result.mau = self.mau * other.tu
        result.rutGon()
        return result

    def __str__(self):
        if self.mau == 1:
            return f'{self.tu}'
        return f'{self.tu}/{self.mau}'


phanSo1 = PhanSo(1, 2)
phanSo2 = PhanSo(4, 2)
phanSo3 = PhanSo(100, 5)
phanSo4 = PhanSo(100, 100)
print(f'{phanSo1} + {phanSo2} = {phanSo1.__add__(phanSo2)} ')
print(f'{phanSo1} - {phanSo2} = {phanSo1.__sub__(phanSo2)} ')
print(f'{phanSo1} * {phanSo2} = {phanSo1.__mul__(phanSo2)} ')
print(f'{phanSo1} : {phanSo2} = {phanSo1.__truediv__(phanSo2)} ')
phanSo1.rutGon()
phanSo2.rutGon()
phanSo3.rutGon()
phanSo4.rutGon()
print(phanSo1)
print(phanSo2)
print(phanSo3)
print(phanSo4)
