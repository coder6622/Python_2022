class PhanSo:
    def __init__(self, tu: int, mau: int):
        # if(mau > 0):
        # else:
        self.tu = tu
        self.mau = mau

    # def rutGon(self):

    def __add__(self, phanSo2):
        kq = PhanSo(0, 1)
        kq.tu = self.tu * phanSo2.mau + self.mau * phanSo2.tu
        kq.mau = self.mau * phanSo2.mau
        return kq

    def __str__(self):
        return f"{self.tu} / {self.mau}"

    # def congPhanSo(self):


#   todo: + , - , * , / , rut gon


phanso = PhanSo(3, 1)

print(phanso.__add__(PhanSo(2, 3)))
# print(phanso.__str__())
