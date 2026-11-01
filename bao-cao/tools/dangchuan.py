"""Xác định dạng chuẩn 2NF, 3NF, BCNF của 38 quan hệ (mục 8).

Chạy:  python3 bao-cao/tools/dangchuan.py
Đọc lược đồ ở bao-cao/07_Mo_hinh_quan_he.md, lấy phủ tối thiểu từ mincover.py cho 12 quan hệ có F nhiều PTH
(các quan hệ còn lại: khóa chính -> mọi thuộc tính), tìm mọi khóa bằng duyệt tập con,
rồi kiểm tra phụ thuộc bộ phận (2NF), vế phải không khóa (3NF) và vế trái không là siêu khóa (BCNF).
Chỉ đọc, không ghi file.
"""
import itertools
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from mincover import RELATIONS, closure, drop_extra_lhs, drop_redundant, parse, split_rhs

# Đặt tên chữ cái của mục 4 -> tên thuộc tính ở mục 7
META = {'MATHANG': {'A': 'MaSP',
             'B': 'SKU',
             'C': 'TenSP',
             'D': 'MoTa',
             'E': 'GiaNiemYet',
             'G': 'GiaKhuyenMai',
             'H': 'ThoiHanBaoHanh',
             'I': 'TinhTrangKinhDoanh',
             'K': 'CoSeri',
             'L': 'MaLoai',
             'M': 'MaTH'},
 'ANHMATHANG': {'A': 'MaAnh', 'B': 'MaSP', 'C': 'ViTri', 'D': 'DuongDan', 'E': 'LaAnhChinh', 'G': 'MoTaAnh'},
 'DINHNGHIATHONGSO': {'A': 'MaTS',
                      'B': 'MaLoai',
                      'C': 'TenTS',
                      'D': 'KieuGiaTri',
                      'E': 'DonVi',
                      'G': 'BatBuoc'},
 'DONHANG': {'A': 'MaDH',
             'B': 'SoDH',
             'C': 'ThoiDiemLap',
             'D': 'KenhBan',
             'E': 'LoaiDon',
             'G': 'MaKH',
             'H': 'MaNVBan',
             'I': 'TenNguoiNhan',
             'K': 'SDTNhan',
             'L': 'DiaChiGiao',
             'M': 'PhiGiao',
             'N': 'GiamGia',
             'O': 'MaMG',
             'P': 'TinhTrang',
             'Q': 'DieuKienCoc',
             'R': 'GhiChu'},
 'PHIEUNHAP': {'A': 'MaPN',
               'B': 'SoPhieu',
               'C': 'MaNCC',
               'D': 'MaNV',
               'E': 'ThoiDiemNhan',
               'G': 'TinhTrang',
               'H': 'SoHoaDonNCC',
               'I': 'GhiChu'},
 'THANHTOAN': {'A': 'MaTT',
               'B': 'MaDH',
               'C': 'LoaiKhoan',
               'D': 'PhuongThuc',
               'E': 'SoTien',
               'G': 'ThoiDiem',
               'H': 'KetQua',
               'I': 'MaGiaoDichNgoai',
               'K': 'DonViThanhToan',
               'L': 'MaNVXacNhan'},
 'MAGIAMGIA': {'A': 'MaMG',
               'B': 'Code',
               'C': 'TenChuongTrinh',
               'D': 'LoaiGiam',
               'E': 'MucGiam',
               'G': 'DonToiThieu',
               'H': 'GiamToiDa',
               'I': 'NgayBatDau',
               'K': 'NgayKetThuc',
               'L': 'GioiHanLuot'},
 'TAIKHOAN': {'A': 'MaTK',
              'B': 'DinhDanhDangNhap',
              'C': 'MaKH',
              'D': 'TinhTrang',
              'E': 'NgayDangKy',
              'G': 'ThoiDiemNoiHoSo'},
 'HANGCOSERI': {'A': 'MaSeri',
                'B': 'SoSeri',
                'C': 'MaSP',
                'D': 'MaPN',
                'E': 'SoDongNhap',
                'G': 'MaDH',
                'H': 'SoDongDon',
                'I': 'TinhTrang',
                'K': 'ThoiDiemNhap'},
 'PHIEUBAOHANH': {'A': 'MaPhieuBH',
                  'B': 'MaKH',
                  'C': 'MaSP',
                  'D': 'MaSeri',
                  'E': 'MaDH',
                  'G': 'SoDong',
                  'H': 'MoTaLoi',
                  'I': 'PhuKienDiKem',
                  'K': 'NgayNhan',
                  'L': 'NgayHenTra',
                  'M': 'NgayTraThucTe',
                  'N': 'TinhTrang',
                  'O': 'KetQua',
                  'P': 'LyDoTuChoi',
                  'Q': 'MaNVTiepNhan'},
 'PHIEUGIAO': {'A': 'MaGiao', 'B': 'MaDH', 'C': 'MaNVGiao', 'D': 'ThoiDiemXuat', 'E': 'TinhTrang'},
 'CHITIETTRA': {'A': 'MaHS', 'B': 'MaDH', 'C': 'SoDong', 'D': 'SoLuongTra', 'E': 'MaSeri'}}

SCHEMA_FILE = os.path.join(HERE, '..', '07_Mo_hinh_quan_he.md')
NFNAME = {1: '1NF', 2: '2NF', 3: '3NF', 4: 'BCNF'}


def read_schema():
    schema = {}
    text = open(SCHEMA_FILE, encoding='utf-8').read()
    for m in re.finditer(r'^- \*\*([A-Z_]+)\*\*\((.*)\)$', text, re.M):
        attrs, pk = [], []
        for p in re.split(r', (?=<u>|<span|[A-Za-z])', m.group(2)):
            nm = re.sub(r'<[^>]+>', '', re.sub(r'<sup>FK</sup>', '', p)).strip()
            attrs.append(nm)
            if p.startswith('<u>'):
                pk.append(nm)
        schema[m.group(1)] = (attrs, pk)
    return schema


def build_F(name, attrs, pk):
    if name in RELATIONS:
        G, _ = drop_redundant(drop_extra_lhs(split_rhs(parse(RELATIONS[name]))))
        return [(frozenset(META[name][a] for a in L), frozenset(META[name][a] for a in R)) for L, R in G]
    return [(frozenset(pk), frozenset([a])) for a in attrs if a not in pk]


def keys_of(attrs, F):
    U, keys = set(attrs), []
    for r in range(1, len(attrs) + 1):
        for c in itertools.combinations(attrs, r):
            if not any(set(k) <= set(c) for k in keys) and closure(c, F) == U:
                keys.append(c)
    return keys


def analyse(attrs, F):
    U = set(attrs)
    keys = keys_of(attrs, F)
    prime = set().union(*[set(k) for k in keys])
    nonprime = U - prime
    partial = []
    for k in keys:
        for r in range(1, len(k)):
            for sub in itertools.combinations(k, r):
                got = (closure(sub, F) - set(sub)) & nonprime
                if got:
                    partial.append((sub, sorted(got)))
    viol_bc, viol_3 = [], []
    for L, R in F:
        for a in R:
            if a not in L and closure(L, F) != U:
                viol_bc.append((tuple(sorted(L)), a))
                if a not in prime:
                    viol_3.append((tuple(sorted(L)), a))
    nf = 1 if partial else (2 if viol_3 else (3 if viol_bc else 4))
    return keys, partial, viol_3, viol_bc, nf


if __name__ == '__main__':
    counts = {}
    for name, (attrs, pk) in read_schema().items():
        keys, partial, viol3, violbc, nf = analyse(attrs, build_F(name, attrs, pk))
        counts[NFNAME[nf]] = counts.get(NFNAME[nf], 0) + 1
        if nf != 4:
            print(f"{name:14s} {NFNAME[nf]:5s} khóa={[','.join(k) for k in keys]} bộ phận={partial} 3NF={viol3} BCNF={violbc}")
    print('Tổng hợp:', counts, '-> dạng chuẩn của lược đồ =', NFNAME[min(1 if c == '1NF' else 2 if c == '2NF' else 3 if c == '3NF' else 4 for c in [k for k in counts])])
