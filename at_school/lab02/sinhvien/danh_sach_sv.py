import datetime

from .sinh_vien import SinhVien
from .sv_chinh_quy import SinhVienChinhQuy
from .sv_phi_chinh_quy import SinhVienPhiChinhQuy


class DanhSachSv:
    def __init__(self):
        self.dssv = []

    def themSV(self, *args: SinhVien):
        for sv in args:
            self.dssv.append(sv)

    def xuat(self):
        for sv in self.dssv:
            print(sv)

    def timSVTheoMs(self, ma_so: int):
        return [sinh_vien for sinh_vien in self.dssv if sinh_vien.maSo == ma_so]

    def timVTSVTheoMs(self, ma_so: int):
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo == ma_so:
                return i
        return -1

    def timSVTheoLoai(self, loai_sv):
        return [sinh_vien for sinh_vien in self.dssv if isinstance(
            sinh_vien, loai_sv)]

    # return [sinh_vien for sinh_vien in self.dssv if
    #         isinstance(sinh_vien, SinhVienPhiChinhQuy)]

    def timSVCoDiemRenLuyenTren(self, diem_rl):
        return [sinh_vien for sinh_vien in self.dssv if
                isinstance(sinh_vien, SinhVienChinhQuy) and
                sinh_vien.diemRL > diem_rl]

    def timSVTheoTrinhDoVaSinhTruocNgay(self, trinh_do: str, ngay_tk: datetime):
        return [sinh_vien for sinh_vien in self.dssv if
                isinstance(sinh_vien, SinhVienPhiChinhQuy)
                and sinh_vien.trinhDo == trinh_do
                and sinh_vien.ngaySinh < ngay_tk
                ]
