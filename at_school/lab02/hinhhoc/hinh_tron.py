import math

from .hinh_hoc import HinhHoc


class HinhTron(HinhHoc):
    def __init__(self, ban_kinh: float) -> None:
        super(HinhTron, self).__init__(ban_kinh)

    @property
    def banKinh(self) -> float:
        return self.canh

    def __str__(self) -> str:
        return f"Hinh tron co ban kinh la {self.banKinh}"

    def xuat(self) -> None:
        print(f"Hinh tron co ban kinh la {self.banKinh}")

    def tinhDienTich(self) -> float:
        return math.pi * self.banKinh ** 2
