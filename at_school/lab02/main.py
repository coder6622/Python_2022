# import datetime
# from sinhvien import DanhSachSv
# from sinhvien import SinhVienChinhQuy
# from sinhvien import SinhVienPhiChinhQuy
#
# sv1 = SinhVienChinhQuy(1957690, "Trần Văn A", "23/6/1999", 80)
# sv2 = SinhVienChinhQuy(1957691, "Nguyễn Văn C", "5/12/1999", 90)
# sv3 = SinhVienPhiChinhQuy(1957692, "Thái Thị Thu", "15/8/1998", "Cao đẳng", 2)
# sv4 = SinhVienPhiChinhQuy(2000324, "Trần Thanh Tâm", "27/8/2000",
#                           "Cao đẳng", 2)
# sv5 = SinhVienPhiChinhQuy(2004544, " Nguyễn Thanh Trà ", "15/8/1999",
#                           "Trung cấp", 2.5)
# sv6 = SinhVienChinhQuy(2004567, "Nguyễn Thành Nam", "7/12/1999", 69)
# sv7 = SinhVienPhiChinhQuy(2004545, "Nguyễn Thanh Thanh", "29/10/1999",
#                           "Trung cấp", 2.5)
# sv8 = SinhVienChinhQuy(2004679, "Võ Hoài Nam", "4/1/2000", 70)
#
# dssv = DanhSachSv()
# dssv.themSV(sv1, sv2, sv3, sv4, sv5, sv6, sv7, sv8)
# dssv.xuat()
#
# vt = dssv.timVTSVTheoMs(2000324)
# print(f"Sinh vien o vi tri thu {vt + 1} trong danh sach")
#
#
# # kqLoai = dssv.timSVTheoLoai("chinhquy")
# # print("Danh sach sinh vien theo loai: ")
# # for sv in kqLoai:
# #     print(sv)
#
# # diemRL = 80
# # kqDiemRL = dssv.timSVCoDiemRenLuyenTren(diemRL)
# # print(f"Danh sach sinh vien co diem ren luyen tren {diemRL} la: ")
# # for sv in kqDiemRL:
# #     print(sv)
#
# trinhDoTK = "Cao đẳng"
# ngayTK = datetime.datetime.strptime("15/8/1999", "%d/%m/%Y")
# kqTKTrinhDoNgaySinh = dssv.timSVTheoTrinhDoVaSinhTruocNgay(trinhDoTK, ngayTK)
# print(f"Danh sach sinh vien co trinh do {trinhDoTK} va sinh truoc ngay "
#       f"{ngayTK} la: ")
#
# for sv in kqTKTrinhDoNgaySinh:
#     print(sv)


from hinhhoc import DanhSachHinhHoc
from hinhhoc import HinhChuNhat
from hinhhoc import HinhTron
from hinhhoc import HinhVuong
from hinhhoc import LoaiHinh

hinhTron1 = HinhTron(3.4)
hinhTron2 = HinhTron(3.7)
hinhTron3 = HinhTron(3.6)
hinhTron4 = HinhTron(3.5)
hinhTron5 = HinhTron(3.5)
# hinhTron1.xuat()
# print(f"Ban kinh la: {hinhTron1.banKinh}")
# print(f"Dien tich hinh tron 1 la {hinhTron1.tinhDienTich()}")

hinhChuNhat1 = HinhChuNhat(3, 4)
hinhChuNhat2 = HinhChuNhat(7, 15)
hinhChuNhat3 = HinhChuNhat(4, 10)
hinhChuNhat4 = HinhChuNhat(8, 10)
hinhChuNhat5 = HinhChuNhat(20, 50)
# print(hinhChuNhat1)
# print(f'Chieu dai la: {hinhChuNhat1.chieuDai}')
# print(f'Chieu rong la: {hinhChuNhat1.chieuRong}')
# print(f"Dien tich hinh chu nhat 1 la: {hinhChuNhat1.tinhDienTich()}")

hinhVuong1 = HinhVuong(4)
hinhVuong2 = HinhVuong(5)
hinhVuong3 = HinhVuong(6)
hinhVuong4 = HinhVuong(7)
hinhVuong5 = HinhVuong(8)
# print(hinhVuong1)
# print(f"Dien tich hinh vuong 1 la: {hinhVuong1.tinhDienTich()}")

dshh = DanhSachHinhHoc()
dshh.themHinhHoc(hinhTron1, hinhTron2, hinhTron3, hinhTron4, hinhTron5)
dshh.themHinhHoc(hinhChuNhat1, hinhChuNhat2, hinhChuNhat3, hinhChuNhat4,
                 hinhChuNhat5)
dshh.themHinhHoc(hinhVuong1, hinhVuong2, hinhVuong3, hinhVuong4, hinhVuong5)

dshh.xuat()

# print(f"Hinh co dien tich lon nhat la: {dshh.timHinhCoDienTichLonNhat()}")
# print(f"Hinh co dien tich nho nhat la: {dshh.timHinhCoDienTichNhoNhat()}")
# print(f"Hinh tron nho nhat la: {dshh.timHinhTronNhoNhat()}")

# print("Danh sach sau khi sap xep giam dan theo dien tich: ")
# dshh.sapXepGiamTheoDienTich()
# dshh.xuat()

# print(f"Tong dien tich cua cac hinh la: {dshh.tinhTongDienTich()}")

# print(f"Hinh tron co dien tich lon nhat la: "
#       f"{dshh.timHinhCoDienTichLonNhatTheoLoaiHinh(LoaiHinh.HinhTron.value)}")
# print(f"Hinh vuong co dien tich lon nhat la: "
#       f"{dshh.timHinhCoDienTichLonNhatTheoLoaiHinh(LoaiHinh.HinhVuong.value)}")
# print(f"Hinh chu nhat co dien tich lon nhat la: "
#       f"{dshh.timHinhCoDienTichLonNhatTheoLoaiHinh(LoaiHinh.HinhChuNhat.value)}")
# print(f"Hinh hoc co dien tich lon nhat la: "
#       f"{dshh.timHinhCoDienTichLonNhatTheoLoaiHinh(LoaiHinh.TatCa.value)}")

# print(f'So luong hinh tron la: '
#       f'{dshh.demSoLuongHinhTheoLoaiHinh(LoaiHinh.HinhTron.value)}')
# print(f'So luong hinh chu nhat la: '
#       f'{dshh.demSoLuongHinhTheoLoaiHinh(LoaiHinh.HinhChuNhat.value)}')
# print(f'So luong hinh vuong la: '
#       f'{dshh.demSoLuongHinhTheoLoaiHinh(LoaiHinh.HinhVuong.value)}')
# print(f'So luong hinh hoc la: '
#       f'{dshh.demSoLuongHinhTheoLoaiHinh(LoaiHinh.TatCa.value)}')

print(f"So luong hinh: "
      f"{dshh.demSoLuongHinhTheoLoaiHinh(LoaiHinh.TatCa.value)}")
print(f"Vi tri dau tien cua hinh tron ban kinh 3.5 la: "
      f"{dshh.timVTDauTienCuaHinh(HinhTron(3.5))}")

print("Danh sach sau khi xoa la: ")
print(dshh.xoaHinhTaiViTri(3))
dshh.xuat()
print(f"So luong hinh con lai: "
      f"{dshh.demSoLuongHinhTheoLoaiHinh(LoaiHinh.TatCa.value)}")

dt_tk = 64
print(f"Hinh co dien tich {dt_tk} la: ")
kq_timDt = dshh.timHinhTheoDienTich(dt_tk)
for hh in kq_timDt:
    print(hh)

print(dshh.xoaHinh(HinhVuong(8)))
print(f"So luong hinh con lai: "
      f"{dshh.demSoLuongHinhTheoLoaiHinh(LoaiHinh.TatCa.value)}")

dshh.xoaHinhTheoLoai(LoaiHinh.HinhTron.value)
print(f"Danh sach sau khi xoa tat ca hinh tron: ")
dshh.xuat()
print(f"So luong hinh con lai: "
      f"{dshh.demSoLuongHinhTheoLoaiHinh(LoaiHinh.TatCa.value)}")

print('Xuat hinh theo chieu tang giam: ')
dshh.xuatHinhTheoChieuTangGiam(LoaiHinh.HinhVuong.value)

print(f'Tong dien tich hinh vuong la: '
      f'{dshh.tinhTongDTTheoKieuHinh(LoaiHinh.HinhVuong.value)}')


