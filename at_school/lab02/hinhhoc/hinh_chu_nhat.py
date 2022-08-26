from .hinh_hoc import HinhHoc


class HinhChuNhat(HinhHoc):
    def __init__(self, rong: float, dai: float) -> None:
        super(HinhChuNhat, self).__init__(rong)
        self.dai = dai

    @property
    def chieuDai(self) -> float:
        return self.dai

    @property
    def chieuRong(self) -> float:
        return self.canh

    def __str__(self) -> str:
        return f"Hinh chu nhat co chieu rong: {self.chieuRong} va chieu dai:" \
               f" {self.chieuDai}"

    def xuat(self) -> None:
        print(f"Hinh chu nhat co chieu rong: {self.chieuRong} va c"
              f"hieu dai: {self.chieuDai}")

    def tinhDienTich(self) -> float:
        return self.chieuDai * self.chieuRong
