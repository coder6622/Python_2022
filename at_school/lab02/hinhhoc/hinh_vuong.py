from .hinh_chu_nhat import HinhChuNhat


class HinhVuong(HinhChuNhat):
    def __init__(self, canh: float):
        super(HinhVuong, self).__init__(canh, canh)

    @property
    def canhHV(self) -> float:
        return self.dai

    def __str__(self) -> str:
        return f"Hinh vuong co do dai canh la: {self.canhHV}"

    def xuat(self) -> None:
        print(f"Hinh vuong co do dai canh la: {self.canhHV}")

    def tinhDienTich(self) -> float:
        return self.canh ** 2
