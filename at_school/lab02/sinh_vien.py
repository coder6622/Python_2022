import datetime


class SinhVien:
    truong = "Dai hoc Da Lat"

    def __init__(self, *args) -> None:
        if len(args) == 3:
            self.__maSo: int = args[0]
            self.__hoTen: str = args[1]
            self.__ngaySinh: datetime = self.dateParse(args[2])
        elif len(args) == 1:
            dong = args[0].strip().split('%')
            self.__maSo: int = dong[0]
            self.__hoTen: str = dong[1]
            self.__ngaySinh: datetime = self.dateParse(dong[2])

    @staticmethod
    def dateParse(date: str):
        return datetime.datetime.strptime(date, "%d/%m/%Y")

    @property
    def maSo(self):
        return self.__maSo

    @maSo.setter
    def maSo(self, ma_so: int):
        if self.maSoHopLe(ma_so):
            self.__maSo = ma_so

    @property
    def hoTen(self):
        return self.__hoTen

    @property
    def ngaySinh(self):
        return self.__ngaySinh

    @staticmethod
    def maSoHopLe(ma_so: int):
        return len(str(ma_so)) == 7

    @classmethod
    def doiTenTruong(cls, ten_truong: str):
        cls.truong = ten_truong

    def __str__(self):
        return f'{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}'

    def Xuat(self):
        print(f'{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}')


class DSSinhVien:
    def __init__(self):
        self.dssv = []

    def themSinhVien(self, sinh_vien: SinhVien):
        self.dssv.append(sinh_vien)

    def docFile(self, ten_file):
        f = open(ten_file)
        dong = f.readlines()
        for i in dong:
            self.dssv.append(SinhVien(i))

    def xuat(self):
        for sinh_vien in self.dssv:
            print(sinh_vien)

    def timSVTheoMS(self, ma_so):
        return [sinh_vien for sinh_vien in self.dssv if sinh_vien.maSo == ma_so]

    def timVTSVTheoMS(self, ma_so: int) -> int:
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo == ma_so:
                return i
        return -1

    def xoaSVTheoMS(self, ma_so: int) -> bool:
        vt = self.timVTSVTheoMS(ma_so)
        if vt != -1:
            del self.dssv[vt]
            return True
        return False

    def timSVTheoTen(self, ten_tk: str):
        return [sinh_vien for sinh_vien in self.dssv if
                sinh_vien.hoTen.lower().__contains__(ten_tk.lower())
                ]

    def timSVSinhTruocNgay(self, ngay_sinh: str):
        return [sinh_vien for sinh_vien in self.dssv if sinh_vien.ngaySinh <
                sinh_vien.dateParse(ngay_sinh)]

    def sapXepSVTheoHoTen(self):
        self.dssv.sort(key=lambda x: x.hoTen)


#
# sv1 = SinhVien(2014469, 'Hoang Long',
#                "06/06/2002")
#
# sv2 = SinhVien(2014468, 'Thanh Long',
#                "03/04/2002")
# sv3 = SinhVien(2012254, 'Nhat Duat',
#                "07/08/2002")
#
# sv4 = SinhVien(2014402, 'My Loc',
#                "04/04/2002")
# dsSinhVien = DSSinhVien()
# dsSinhVien.themSinhVien(sv1)
# dsSinhVien.themSinhVien(sv2)
# dsSinhVien.themSinhVien(sv3)
# dsSinhVien.themSinhVien(sv4)
#
# dsSinhVien.xuat()
# dsSinhVien.xoaSVTheoMS(2014468)
# print('Danh sach sinh vien da xoa: ')
# dsSinhVien.xuat()

# ten = 'loc'
# print(f'Sinh vien ten {ten} la: ')
# kqTimTen = dsSinhVien.timSVTheoTen(ten)
# for sv in kqTimTen:
#     print(sv)
#

# print('Danh sach sinh vien la: ')
# dsSinhVien.docFile('sinh_vien.txt')
# dsSinhVien.xuat()

# ngayTK = '06/08/2002'
# print(f'Sinh vien sinh truoc ngay {ngayTK} la: ')
# kqTimNgay = dsSinhVien.timSVSinhTruocNgay(ngayTK)
# for sv in kqTimNgay:
#     print(sv)
# print('Danh sach sau khi sap xep: ')
# dsSinhVien.sapXepSVTheoHoTen()
# dsSinhVien.xuat()
