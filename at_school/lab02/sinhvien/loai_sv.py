import enum

from .sv_chinh_quy import SinhVienChinhQuy
from .sv_phi_chinh_quy import SinhVienPhiChinhQuy


class LoaiSinhVien(enum.Enum):
    PhiCQ = SinhVienPhiChinhQuy
    ChinhQuy = SinhVienChinhQuy
