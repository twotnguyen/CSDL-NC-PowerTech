"""Sinh mã SQL từ lược đồ: CREATE TABLE cho 25 quan hệ sau cải tiến và câu truy vấn cho từng con đường truy xuất.

Mã dùng cú pháp chuẩn chạy được trên SQL Server (dùng cho đề tài) và SQLite (dùng để kiểm tra trong báo cáo). Chuỗi tiếng Việt
trong CHECK viết không có tiền tố N; khi cài trên SQL Server nên đặt cột là NVARCHAR và thêm tiền tố N cho chuỗi.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import luoc_do

CHECKS = {
    'LOAIHANG': ['MaLoaiCha IS NULL OR MaLoaiCha <> MaLoai'],
    'MATHANG': ['GiaNiemYet > 0', 'GiaKhuyenMai IS NULL OR GiaKhuyenMai <= GiaNiemYet', 'ThoiHanBH BETWEEN 0 AND 120',
                "TinhTrangKD IN ('Đang kinh doanh', 'Ngừng kinh doanh')"],
    'ANHMATHANG': ['ViTriAnh >= 1'],
    'DINHNGHIATHONGSO': ["KieuGiaTri IN ('Chữ', 'Số', 'Có/Không')"],
    'NHANVIEN': ["TinhTrangNV IN ('Đang làm', 'Đã nghỉ')", 'NgayNghiViec IS NULL OR NgayNghiViec >= NgayVaoLam',
                 "(TinhTrangNV = 'Đã nghỉ') = (NgayNghiViec IS NOT NULL)",
                 "ChucVu IN ('Quản lý', 'Bán hàng', 'Thu ngân', 'Kỹ thuật', 'Kho', 'Giao hàng')"],
    'TAIKHOAN': ["TinhTrangTK IN ('Hoạt động', 'Bị khóa')", '(MaKH IS NULL AND MaNV IS NOT NULL) OR (MaKH IS NOT NULL AND MaNV IS NULL)'],
    'NHACUNGCAP': ["TinhTrangHT IN ('Đang hợp tác', 'Ngừng hợp tác')"],
    'MAGIAMGIA': ["LoaiGiam IN ('Phần trăm', 'Số tiền')", 'MucGiam > 0', 'NgayKetThuc IS NULL OR NgayBatDau IS NULL OR NgayKetThuc >= NgayBatDau'],
    'DONHANG': ["KenhBan IN ('Quầy', 'Trang web', 'Điện thoại', 'Tin nhắn')", 'PhiGiao >= 0', 'GiamGia >= 0',
                "TinhTrangDH IN ('Chờ xác nhận', 'Đã xác nhận', 'Đang chuẩn bị', 'Đang giao', 'Hoàn tất', 'Đã hủy')",
                "KenhBan = 'Trang web' OR MaNV IS NOT NULL"],
    'CHITIETDONHANG': ['SoLuongBan > 0', 'DonGiaChot >= 0', 'ThoiHanBHChot BETWEEN 0 AND 120'],
    'THANHTOAN': ["MaNVThu IS NULL OR PhuongThuc = 'Thu khi giao'", 'SoTien > 0', "LoaiKhoan IN ('Thanh toán', 'Đặt cọc')",
                  "KetQuaTT IN ('Thành công', 'Thất bại', 'Chờ')"],
    'PHIEUGIAO': ["TinhTrangGiao IN ('Đang giao', 'Đã giao', 'Không thành công')"],
    'LANGIAO': ['SoLan BETWEEN 1 AND 3'],
    'PHIEUNHAP': ["TinhTrangPN IN ('Nháp', 'Đã xác nhận', 'Đã hủy')",
                  '(MaNVXacNhan IS NULL) = (ThoiDiemXacNhan IS NULL)'],
    'CHITIETPHIEUNHAP': ['SoLuongNhap > 0', 'GiaNhap >= 0'],
    'HANGCOSERI': ['(MaDH IS NULL AND SoDongDH IS NULL) OR (MaDH IS NOT NULL AND SoDongDH IS NOT NULL)'],
    'GIAODICHKHO': ['SoLuongGD > 0', "NhomKho IN ('Đủ điều kiện bán', 'Chờ kiểm tra', 'Chờ xử lý')"],
    'CHITIETTRA': ['SoLuongTra > 0', 'MaSeri IS NULL OR SoLuongTra = 1'],
    'KHOANHOAN': ['SoTienHoan > 0', '(MaNVChi IS NULL) = (ThoiDiemChi IS NULL)', 'MaHS IS NULL OR MaPhieuBH IS NULL'],
    'LANNHANLAI': ['(MaNVDuyet IS NULL) = (ThoiDiemDuyet IS NULL)'],
    'PHIEUBAOHANH': ['NgayHenTra >= NgayNhan'],
}


def topo(R, order):
    done, out = set(), []

    def visit(n, stack=()):
        if n in done or n in stack:
            return
        for cols, parent, pc in R[n]['fks']:
            if parent != n:
                visit(parent, stack + (n,))
        done.add(n)
        out.append(n)
    for n in order:
        visit(n)
    return out


def ddl(R=None, order=None):
    R = R or luoc_do.improved()
    order = order or luoc_do.ORDER_IMPROVED
    L = [f'-- Lược đồ sau cải tiến của PowerTech ({len(order)} quan hệ). Sinh bằng tools/sql_gen.py từ tools/luoc_do.py.',
         '-- Tiền tệ là đồng Việt Nam (DECIMAL(15,0)). Khóa chính số nguyên tự tăng do ứng dụng cấp.', '']
    for n in topo(R, order):
        r = R[n]
        lines = []
        for a, t, nl, mean in r['attrs']:
            lines.append(f'    {a} {t} {"NOT NULL" if nl == "NN" else "NULL"}')
        lines.append(f'    CONSTRAINT PK_{n} PRIMARY KEY ({", ".join(r["pk"])})')
        nullable = {a[0] for a in r['attrs'] if a[2] == 'NULL'}
        for u in r['uniques']:
            if not nullable & set(u):
                lines.append(f'    CONSTRAINT UQ_{n}_{"_".join(u)} UNIQUE ({", ".join(u)})')
        for i, (cols, parent, pc) in enumerate(r['fks'], 1):
            lines.append(f'    CONSTRAINT FK_{n}_{"_".join(cols)} FOREIGN KEY ({", ".join(cols)}) REFERENCES {parent}({", ".join(pc)})')
        for i, ck in enumerate(CHECKS.get(n, []), 1):
            lines.append(f'    CONSTRAINT CK_{n}_{i} CHECK ({ck})')
        L.append(f'CREATE TABLE {n} (  -- {r["ten"]}')
        L.append(',\n'.join(lines))
        L.append(');')
        # cột cho phép rỗng: chỉ duy nhất trên những bộ khác rỗng (giả thiết G4), UNIQUE thường của SQL Server chặn hai giá trị NULL
        for u in r['uniques']:
            if nullable & set(u):
                L.append(f'CREATE UNIQUE INDEX UQ_{n}_{"_".join(u)} ON {n} ({", ".join(u)}) WHERE {" AND ".join(c + " IS NOT NULL" for c in u if c in nullable)};')
        L.append('')
    return '\n'.join(L)


# ------------------------------------------------------------------ SQL cho con đường truy xuất
ALIAS = {'LOAIHANG': 'lh', 'THUONGHIEU': 'th', 'MATHANG': 'mh', 'ANHMATHANG': 'am', 'DINHNGHIATHONGSO': 'dn',
         'GIATRITHONGSO': 'gt', 'KHACHHANG': 'kh', 'NHANVIEN': 'nv', 'NHACUNGCAP': 'nc', 'MAGIAMGIA': 'mg',
         'DONHANG': 'dh', 'CHITIETDONHANG': 'ct', 'THANHTOAN': 'tt', 'PHIEUGIAO': 'pg', 'LANGIAO': 'lg', 'PHIEUNHAP': 'pn',
         'CHITIETPHIEUNHAP': 'cp', 'HANGCOSERI': 'hs', 'SERIMATHANG': 'sm', 'GIAODICHKHO': 'gd', 'HOSODOITRA': 'hd',
         'CHITIETTRA': 'cr', 'LANNHANLAI': 'nl', 'KHOANHOAN': 'kc', 'PHIEUBAOHANH': 'bh', 'TAIKHOAN': 'tk'}


def join_chain(path, fk_of):
    """path: danh sách nút. fk_of[(i, j)] = (quan hệ con, cột, quan hệ cha) của cung i -> j. Trả về câu SELECT."""
    first = path[0]
    seen = {}

    def alias(n, k=0):
        base = ALIAS[n]
        c = seen.get(n, 0) + 1
        seen[n] = c
        return base if c == 1 else f'{base}{c}'
    a = {first: alias(first)}
    lines = [f'FROM {first} {a[first]}']
    if first == 'HANGCOSERI':
        lines.append(f'JOIN SERIMATHANG {ALIAS["SERIMATHANG"]} ON {ALIAS["SERIMATHANG"]}.MaSeri = {a[first]}.MaSeri')
    for i, j in zip(path, path[1:]):
        rel, cols, parent = fk_of[(i, j)]
        a[j] = alias(j)
        conds = ' AND '.join(f'{a[i]}.{c} = {a[j]}.{pc}' for c, pc in zip(cols, fk_pcols(rel, cols, parent)))
        lines.append(f'JOIN {j} {a[j]} ON {conds}')
        if j == 'HANGCOSERI':
            lines.append(f'JOIN SERIMATHANG {ALIAS["SERIMATHANG"]} ON {ALIAS["SERIMATHANG"]}.MaSeri = {a[j]}.MaSeri')
    # chỉ chọn khóa chính của mỗi quan hệ trên đường (cột nối trùng giá trị thì chỉ lấy một lần)
    R = luoc_do.improved()
    cols_sel, seen_col = [], set()
    for n in path:
        for c in R[n]['pk']:
            if c not in seen_col:
                seen_col.add(c)
                cols_sel.append(f'{a[n]}.{c}')
    return 'SELECT ' + ', '.join(cols_sel) + '\n' + '\n'.join(lines) + ';'


def fk_pcols(rel, cols, parent):
    R = luoc_do.improved()
    for c, p, pc in R[rel]['fks']:
        if tuple(c) == tuple(cols) and p == parent:
            return list(pc)
    raise KeyError((rel, cols, parent))


if __name__ == '__main__':
    out = os.path.join(HERE, '..', 'sql', '01_tao_bang.sql')
    open(out, 'w', encoding='utf-8').write(ddl())
    print('đã ghi', os.path.normpath(out))
