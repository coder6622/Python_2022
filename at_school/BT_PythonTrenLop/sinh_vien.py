from datetime import datetime


class SinhVien:
    truong = "Đại học Đà Lạt"

    def __init__(self, ma_so: int, ho_ten: str, ngay_sinh: datetime):
        self.__maSo = ma_so
        self.__hoTen = ho_ten
        self.ngaySinh = ngay_sinh

    @property
    def hoTen(self):
        return self.__hoTen

    @hoTen.setter
    def hoTen(self, ho_ten: str):
        self.__hoTen = ho_ten

    # todo: @property viet ham get
    @property
    def maSo(self):
        return self.__maSo

    # todo: @staticmethod viet ham khong lien quan den hanh vi cua doi tuong (
    #  khong can self)
    @staticmethod
    def ktMSHopLe(mssv: int):
        return len(str(mssv)) == 7

    @maSo.setter
    def maSo(self, mssv):
        if self.ktMSHopLe(mssv):
            self.__maSo = mssv

    def Xuat(self):
        print(f"{self.__maSo}\t {self.__hoTen}\t{self.ngaySinh}")

    def __str__(self) -> str:
        return f"{self.__maSo}^^^^^^{self.__hoTen}^^^^^^^{self.ngaySinh}"

    def doiTruong(self, truong_moi):
        self.truong = truong_moi

    # todo: thao tac tren bien cua lop, khong truy xuat tren bien cua doi tuong
    @classmethod
    def doiTruongChoTatCaDoiTuong(cls, truong_moi: str):
        cls.truong = truong_moi


class DanhSachSinhVien:
    def __init__(self):
        self.dssv = []

    def themSV(self, sv: SinhVien):
        self.dssv.append(sv)

    def xuat(self):
        for sv in self.dssv:
            print(sv)

    # todo: tim sv theo mssv
    def timSvTheoMSSV(self, mssv_tk: int):
        # return [sv for sv in self.dssv if sv.mssv == mssv_tk]
        return list(filter(lambda sv: sv.maSo == mssv_tk, self.dssv))

    # todo:  tim vi tri sinh vien co mssv
    def timVtSvTheoMssv(self, mssv_tk: int):
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo == mssv_tk:
                return i
        return -1

    def xoaSvTheoMssv(self, mssv_tk: int):
        vt = self.timVtSvTheoMssv(mssv_tk)
        if vt != -1:
            del self.dssv[vt]
            return 1
        return 0

    # todo: tim sinh vien ten "name"
    def timSvTheoTen(self, name_tk: str):
        return [sV for sV in self.dssv if sV.hoTen.lower().__contains__(
            name_tk.lower())
                ]

    # todo: tim sinh vien sinh truoc 15/06/2000
    def timSvSinhTruocNgay(self, ngay: datetime):
        return [sV for sV in self.dssv if sV.ngaySinh < ngay]


sv1 = SinhVien(20123232, "Hoang Long", datetime.strptime(
    "12/02/2002", "%d/%m/%Y"))
sv2 = SinhVien(234384734, "Hello world", datetime.strptime(
    "12/02/2003", "%d/%m/%Y"))
sv3 = SinhVien(437439473, "Hello world 2", datetime.strptime(
    "12/02/2005", "%d/%m/%Y"))
sv4 = SinhVien(374389473, "Hello world 3", datetime.strptime(
    "12/02/2006", "%d/%m/%Y"))
sv5 = SinhVien(232387293, "Hello world 4", datetime.strptime(
    "12/02/2007", "%d/%m/%Y"))
sv1.Xuat()
sv1.Diem = 9
print(
    sv1.hoTen
)
print(sv1.Diem)

sv1.hoTen = 'Duat'
print(sv1.hoTen)
sv1.Xuat()

print(sv1.maSo)
sv1.maSo = '9999999'

sv1.Xuat()

print(sv1)
print(sv1.__str__())

print(sv1.truong)
print(sv2.truong)

# sv1.truong = "Da Lat University"
# sv1.doiTruong("Da Lat University")
sv1.doiTruongChoTatCaDoiTuong("Da Lat University")
print(sv1.truong)
print(sv2.truong)

dssv = DanhSachSinhVien()
dssv.themSV(sv1)
dssv.themSV(sv2)
dssv.themSV(sv3)
dssv.themSV(sv4)
dssv.themSV(sv5)
dssv.xuat()

ms = 232387293
# kq = dssv.timVtSvTheoMssv(9999999)
# for sv in kq:
#     print(sv)


vt = dssv.timVtSvTheoMssv(ms)
if vt != -1:
    print(f'Sinh vien co ma so {ms} nam o vi tri thu {vt + 1} trong danh '
          f'sach')
else:
    print('Khong ton tai')

isDel = dssv.xoaSvTheoMssv(ms)
print(isDel)
if isDel:
    print('Xoa duoc')
else:
    print('Khong xoa duoc')
dssv.xuat()
kq = dssv.timSvSinhTruocNgay(datetime.strptime("12/02/2006", "%d/%m/%Y"))
print('DSSV truoc ngay')
for sv in kq:
    print(sv)

ten = "world"
print('DSSV theo ten')
kqTen = dssv.timSvTheoTen(ten)
for i in kqTen:
    print(i)

