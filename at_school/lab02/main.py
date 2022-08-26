import datetime

from danh_sach_sv import DanhSachSv
from sv_chinh_quy import SinhVienChinhQuy
from sv_phi_chinh_quy import SinhVienPhiChinhQuy

sv1 = SinhVienChinhQuy(1957690, "Trần Văn A", "23/6/1999", 80)
sv2 = SinhVienChinhQuy(1957691, "Nguyễn Văn C", "5/12/1999", 90)
sv3 = SinhVienPhiChinhQuy(1957692, "Thái Thị Thu", "15/8/1998", "Cao đẳng", 2)
sv4 = SinhVienPhiChinhQuy(2000324, "Trần Thanh Tâm", "27/8/2000",
                          "Cao đẳng", 2)
sv5 = SinhVienPhiChinhQuy(2004544, " Nguyễn Thanh Trà ", "15/8/1999",
                          "Trung cấp", 2.5)
sv6 = SinhVienChinhQuy(2004567, "Nguyễn Thành Nam", "7/12/1999", 69)
sv7 = SinhVienPhiChinhQuy(2004545, "Nguyễn Thanh Thanh", "29/10/1999",
                          "Trung cấp", 2.5)
sv8 = SinhVienChinhQuy(2004679, "Võ Hoài Nam", "4/1/2000", 70)

dssv = DanhSachSv()
dssv.themSV(sv1, sv2, sv3, sv4, sv5, sv6, sv7, sv8)
dssv.xuat()

# vt = dssv.timVTSVTheoMs(2000324)
# print(f"Sinh vien o vi tri thu {vt + 1} trong danh sach")


# kqLoai = dssv.timSVTheoLoai("chinhquy")
# print("Danh sach sinh vien theo loai: ")
# for sv in kqLoai:
#     print(sv)

# diemRL = 80
# kqDiemRL = dssv.timSVCoDiemRenLuyenTren(diemRL)
# print(f"Danh sach sinh vien co diem ren luyen tren {diemRL} la: ")
# for sv in kqDiemRL:
#     print(sv)

trinhDoTK = "Cao đẳng"
ngayTK = datetime.datetime.strptime("15/8/1999", "%d/%m/%Y")
kqTKTrinhDoNgaySinh = dssv.timSVTheoTrinhDoVaSinhTruocNgay(trinhDoTK, ngayTK)
print(f"Danh sach sinh vien co trinh do {trinhDoTK} va sinh truoc ngay "
      f"{ngayTK} la: ")

for sv in kqTKTrinhDoNgaySinh:
    print(sv)
