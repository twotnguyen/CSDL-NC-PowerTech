#!/usr/bin/env python3
"""Sinh chương 3 (chuong/03_chuong3.md), hình đồ thị quan hệ và các file SQL truy vấn.

Đồ thị quan hệ tính bằng tools/dothi.py (thuật toán B1-B7, Bài 10) từ lược đồ sau cải tiến; con đường truy xuất là các mạch đi
từ nút vào theo chiều cung; mỗi đường có câu ngữ nghĩa và một câu SQL. Mọi câu SQL được chạy thử trên dữ liệu minh họa (sql/02).
Chạy:  python3 tools/gen_chuong3.py
"""
import json
import os
import sqlite3
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dothi
import luoc_do
import sql_gen

OUT = []
NOUN = {'LOAIHANG': 'loại hàng', 'THUONGHIEU': 'thương hiệu', 'MATHANG': 'mặt hàng', 'ANHMATHANG': 'ảnh mặt hàng',
        'DINHNGHIATHONGSO': 'thông số', 'GIATRITHONGSO': 'giá trị thông số', 'KHACHHANG': 'khách hàng', 'NHANVIEN': 'nhân viên',
        'NHACUNGCAP': 'nhà cung cấp', 'MAGIAMGIA': 'mã giảm giá', 'DONHANG': 'đơn hàng', 'CHITIETDONHANG': 'dòng đơn',
        'THANHTOAN': 'khoản thanh toán', 'PHIEUGIAO': 'phiếu giao', 'LANGIAO': 'lần giao hàng', 'PHIEUNHAP': 'phiếu nhập',
        'CHITIETPHIEUNHAP': 'dòng phiếu nhập', 'HANGCOSERI': 'chiếc hàng có seri', 'GIAODICHKHO': 'giao dịch kho',
        'HOSODOITRA': 'hồ sơ đổi trả', 'CHITIETTRA': 'dòng trả hàng', 'LANNHANLAI': 'lần nhận lại hàng',
        'KHOANHOAN': 'khoản hoàn tiền', 'PHIEUBAOHANH': 'phiếu bảo hành', 'TAIKHOAN': 'tài khoản'}
# (từ, đến) -> (cụm xuôi, cụm ngược): cụm xuôi nối sau danh từ của nút đi; cụm ngược nối sau "Từ một <nút đến> cho biết"
ARC = {
    ('MATHANG', 'LOAIHANG'): ('thuộc loại hàng nào', 'các mặt hàng của loại hàng đó'),
    ('MATHANG', 'THUONGHIEU'): ('mang thương hiệu nào', 'các mặt hàng của thương hiệu đó'),
    ('ANHMATHANG', 'MATHANG'): ('minh họa cho mặt hàng nào', 'các ảnh của mặt hàng đó'),
    ('DINHNGHIATHONGSO', 'LOAIHANG'): ('do loại hàng nào quy định', 'các thông số mà loại hàng đó quy định'),
    ('GIATRITHONGSO', 'MATHANG'): ('thuộc mặt hàng nào', 'các giá trị thông số của mặt hàng đó'),
    ('GIATRITHONGSO', 'DINHNGHIATHONGSO'): ('ứng với thông số nào', 'các mặt hàng có giá trị cho thông số đó'),
    ('DONHANG', 'KHACHHANG'): ('do khách hàng nào đặt (nếu có hồ sơ khách)', 'các đơn hàng của khách đó'),
    ('DONHANG', 'NHANVIEN'): ('do nhân viên nào lập', 'các đơn hàng do nhân viên đó lập'),
    ('DONHANG', 'MAGIAMGIA'): ('áp dụng mã giảm giá nào (nếu có)', 'các đơn đã dùng mã giảm giá đó'),
    ('CHITIETDONHANG', 'MATHANG'): ('bán mặt hàng nào', 'các dòng đơn đã bán mặt hàng đó'),
    ('CHITIETDONHANG', 'DONHANG'): ('thuộc đơn hàng nào', 'các dòng của đơn đó'),
    ('THANHTOAN', 'NHANVIEN'): ('do nhân viên nào xác nhận thu', 'các khoản thu do nhân viên đó xác nhận'),
    ('THANHTOAN', 'DONHANG'): ('trả cho đơn hàng nào', 'các lần thanh toán và đặt cọc của đơn đó'),
    ('PHIEUGIAO', 'NHANVIEN'): ('do nhân viên nào giao', 'các phiếu giao do nhân viên đó phụ trách'),
    ('PHIEUGIAO', 'DONHANG'): ('lập cho đơn hàng nào', 'phiếu giao của đơn đó (tối đa một)'),
    ('LANGIAO', 'PHIEUGIAO'): ('thuộc phiếu giao nào', 'các lần thử giao của phiếu đó (tối đa 3)'),
    ('LANGIAO', 'NHANVIEN'): ('do nhân viên nào giao', 'các lần giao do nhân viên đó thực hiện'),
    ('PHIEUNHAP', 'NHANVIEN'): ('do nhân viên kho nào lập', 'các phiếu nhập do nhân viên đó lập'),
    ('PHIEUNHAP', 'NHACUNGCAP'): ('nhận từ nhà cung cấp nào', 'các phiếu nhập từ nhà cung cấp đó'),
    ('CHITIETPHIEUNHAP', 'MATHANG'): ('nhập mặt hàng nào', 'các dòng nhập của mặt hàng đó'),
    ('CHITIETPHIEUNHAP', 'PHIEUNHAP'): ('thuộc phiếu nhập nào', 'các dòng của phiếu nhập đó'),
    ('HANGCOSERI', 'CHITIETDONHANG'): ('bán gần nhất ở dòng đơn nào', 'các chiếc hàng có seri có lần bán gần nhất ở dòng đơn đó'),
    ('HANGCOSERI', 'CHITIETPHIEUNHAP'): ('nhập về ở dòng phiếu nhập nào', 'các chiếc hàng có seri nhập ở dòng đó'),
    ('GIAODICHKHO', 'MATHANG'): ('liên quan đến mặt hàng nào', 'các giao dịch kho của mặt hàng đó'),
    ('GIAODICHKHO', 'NHANVIEN'): ('do nhân viên nào thực hiện', 'các giao dịch kho do nhân viên đó thực hiện'),
    ('HOSODOITRA', 'NHANVIEN'): ('do nhân viên nào tiếp nhận', 'các hồ sơ đổi trả do nhân viên đó tiếp nhận'),
    ('HOSODOITRA', 'DONHANG'): ('lập cho đơn hàng nào', 'các hồ sơ đổi trả của đơn đó'),
    ('CHITIETTRA', 'HANGCOSERI'): ('ghi chiếc hàng có seri nào', 'các dòng trả có chiếc hàng đó'),
    ('CHITIETTRA', 'HOSODOITRA'): ('thuộc hồ sơ đổi trả nào', 'các dòng trả của hồ sơ đó'),
    ('LANNHANLAI', 'NHANVIEN'): ('do nhân viên nào kiểm tra', 'các lần nhận lại do nhân viên đó kiểm tra'),
    ('LANNHANLAI', 'HOSODOITRA'): ('thuộc hồ sơ đổi trả nào', 'các lần nhận lại của hồ sơ đó'),
    ('KHOANHOAN', 'NHANVIEN'): ('do người quản lý nào duyệt', 'các khoản hoàn do người quản lý đó duyệt'),
    ('KHOANHOAN', 'THANHTOAN'): ('tính trên khoản thanh toán nào', 'các khoản hoàn của khoản thanh toán đó'),
    ('KHOANHOAN', 'HOSODOITRA'): ('theo hồ sơ đổi trả nào (nếu do đổi trả)', 'các khoản hoàn của hồ sơ đó'),
    ('KHOANHOAN', 'PHIEUBAOHANH'): ('theo phiếu bảo hành nào (nếu do bảo hành thu hồi)', 'các khoản hoàn của phiếu đó'),
    ('PHIEUBAOHANH', 'NHANVIEN'): ('do nhân viên nào tiếp nhận', 'các phiếu bảo hành do nhân viên đó tiếp nhận'),
    ('PHIEUBAOHANH', 'CHITIETDONHANG'): ('mua ở dòng đơn nào', 'các phiếu bảo hành của dòng đơn đó'),
    ('PHIEUBAOHANH', 'HANGCOSERI'): ('ứng với chiếc hàng có seri nào', 'các phiếu bảo hành của chiếc hàng đó'),
    ('LOAIHANG', 'LOAIHANG'): ('thuộc loại hàng cha nào', 'các loại hàng con của loại hàng đó'),
    ('TAIKHOAN', 'KHACHHANG'): ('thuộc khách hàng nào (nếu là tài khoản khách)', 'tài khoản của khách đó (tối đa một)'),
    ('TAIKHOAN', 'NHANVIEN'): ('thuộc nhân viên nào (nếu là tài khoản nhân viên)', 'tài khoản của nhân viên đó (tối đa một)'),
    ('MAGIAMGIA', 'NHANVIEN'): ('do nhân viên nào tạo', 'các mã giảm giá do nhân viên đó tạo'),
}


def w(s=''):
    OUT.append(s)


def num(R):
    return {n: i for i, n in enumerate(R['nodes'], 1)}


def nm(x):
    return '∅' if not x else '{' + ', '.join(sorted(x)) + '}'


def fk_map(R):
    """(từ, đến) -> (quan hệ con, cột, quan hệ cha) của cung."""
    m = {}
    for i, j, kind, fk, f, b in dothi.arcs(R):
        if fk and i != j:
            m[(i, j)] = fk
    return m


def paths_from(adj, n, path):
    nxt = [j for j in adj.get(n, []) if j not in path]
    if not nxt:
        yield path
        return
    for j in nxt:
        yield from paths_from(adj, j, path + [j])


def sentence(path):
    parts = [f'Cho biết {NOUN[path[0]]} {ARC[(path[0], path[1])][0]}']
    for a, b in zip(path[1:], path[2:]):
        parts.append(f'{NOUN[a]} đó {ARC[(a, b)][0]}')
    return '; '.join(parts) + '.'


def draw(R, N, entry, fname, so=False):
    """Vẽ bằng tools/ve_dothi.py: đường thẳng, bố cục lưu ở tools/bo_cuc_dothi.json (ít giao cắt, không cung xuyên nút)."""
    import ve_dothi
    ve_dothi.ve(R, N, entry, fname, so)


# Đường cho kết quả rỗng theo đúng ràng buộc nghiệp vụ (không phải lỗi): đường -> lý do
ZERO_OK = {}

K_QUERIES = [
    ('K1', 'Lịch sử mua hàng của một khách theo số điện thoại',
     'KHACHHANG ⇒ DONHANG ⇒ CHITIETDONHANG',
     """SELECT dh.SoDH, dh.ThoiDiemLap, ct.SoDongDH, ct.TenHangChot, ct.SoLuongBan, ct.DonGiaChot,
       ct.SoLuongBan * ct.DonGiaChot AS ThanhTien
FROM KHACHHANG kh
JOIN DONHANG dh ON dh.MaKH = kh.MaKH
JOIN CHITIETDONHANG ct ON ct.MaDH = dh.MaDH
WHERE kh.SDTKH = '0900000001'
ORDER BY dh.ThoiDiemLap, ct.SoDongDH;"""),
    ('K2', 'Doanh thu tiền hàng theo loại hàng trong tháng 10/2026 (không tính đơn đã hủy, chưa trừ giảm giá và hoàn tiền)',
     'CHITIETDONHANG → DONHANG; CHITIETDONHANG → MATHANG → LOAIHANG',
     """SELECT lh.TenLoai, SUM(ct.SoLuongBan * ct.DonGiaChot) AS DoanhThuTienHang
FROM CHITIETDONHANG ct
JOIN DONHANG dh ON dh.MaDH = ct.MaDH
JOIN MATHANG mh ON mh.MaSP = ct.MaSP
JOIN LOAIHANG lh ON lh.MaLoai = mh.MaLoai
WHERE dh.TinhTrangDH <> 'Đã hủy'
  AND dh.ThoiDiemLap >= '2026-10-01' AND dh.ThoiDiemLap < '2026-11-01'
GROUP BY lh.TenLoai
ORDER BY DoanhThuTienHang DESC;"""),
    ('K3', 'Số lượng hàng trong kho theo mặt hàng và nhóm kho, tính từ giao dịch kho',
     'GIAODICHKHO → MATHANG',
     """SELECT mh.TenSP, gd.NhomKho,
       SUM(CASE WHEN gd.LoaiBienDong IN ('Nhập', 'Nhận lại') THEN gd.SoLuongGD
                WHEN gd.LoaiBienDong = 'Xuất bán' THEN -gd.SoLuongGD
                ELSE 0 END) AS SoLuong
FROM GIAODICHKHO gd
JOIN MATHANG mh ON mh.MaSP = gd.MaSP
GROUP BY mh.TenSP, gd.NhomKho
ORDER BY mh.TenSP, gd.NhomKho;"""),
    ('K4', 'Truy vết một chiếc hàng theo số seri: nhập từ đâu, lần bán gần nhất cho ai',
     'SERIMATHANG ⇒ HANGCOSERI → CHITIETPHIEUNHAP → PHIEUNHAP → NHACUNGCAP; HANGCOSERI → CHITIETDONHANG → DONHANG → KHACHHANG',
     """SELECT sm.SoSeri, mh.TenSP, pn.SoPhieu, nc.TenNCC, dh.SoDH, kh.HoLotKH, kh.TenKH
FROM SERIMATHANG sm
JOIN MATHANG mh ON mh.MaSP = sm.MaSP
JOIN HANGCOSERI hs ON hs.MaSeri = sm.MaSeri
JOIN CHITIETPHIEUNHAP cp ON cp.MaPN = hs.MaPN AND cp.SoDongPN = hs.SoDongPN
JOIN PHIEUNHAP pn ON pn.MaPN = cp.MaPN
JOIN NHACUNGCAP nc ON nc.MaNCC = pn.MaNCC
LEFT JOIN CHITIETDONHANG ct ON ct.MaDH = hs.MaDH AND ct.SoDongDH = hs.SoDongDH
LEFT JOIN DONHANG dh ON dh.MaDH = ct.MaDH
LEFT JOIN KHACHHANG kh ON kh.MaKH = dh.MaKH
WHERE sm.MaSP = 2 AND sm.SoSeri = 'S1T-0001';"""),
    ('K5', 'Hồ sơ đổi trả của một đơn kèm số tiền đã hoàn',
     'HOSODOITRA ⇒ CHITIETTRA; HOSODOITRA ⇒ KHOANHOAN → THANHTOAN',
     """SELECT hd.MaHS, hd.LoaiTruongHop, ct.SoDongDH, ct.SoLuongTra, kc.SoTienHoan, tt.SoTien AS SoTienDaThu
FROM HOSODOITRA hd
JOIN CHITIETTRA ct ON ct.MaHS = hd.MaHS
LEFT JOIN KHOANHOAN kc ON kc.MaHS = hd.MaHS
LEFT JOIN THANHTOAN tt ON tt.MaTT = kc.MaTT
WHERE hd.MaDH = 2;"""),
    ('K6', 'Ai đã lập đơn, thu tiền và giao một đơn hàng, và người đó có chức vụ gì (truy trách nhiệm)',
     'DONHANG → NHANVIEN (lập); DONHANG ⇐ THANHTOAN → NHANVIEN (xác nhận thu); DONHANG ⇐ PHIEUGIAO → NHANVIEN (giao)',
     """SELECT dh.SoDH, nl.HoLotNV AS HoLotNguoiLap, nl.TenNV AS TenNguoiLap, nl.ChucVu AS ChucVuNguoiLap,
       tt.MaTT, tt.PhuongThuc, nt.HoLotNV AS HoLotNguoiThu, nt.TenNV AS TenNguoiThu,
       pg.MaGiao, ng.HoLotNV AS HoLotNguoiGiao, ng.TenNV AS TenNguoiGiao, ng.ChucVu AS ChucVuNguoiGiao
FROM DONHANG dh
LEFT JOIN NHANVIEN nl ON nl.MaNV = dh.MaNV
LEFT JOIN THANHTOAN tt ON tt.MaDH = dh.MaDH
LEFT JOIN NHANVIEN nt ON nt.MaNV = tt.MaNV
LEFT JOIN PHIEUGIAO pg ON pg.MaDH = dh.MaDH
LEFT JOIN NHANVIEN ng ON ng.MaNV = pg.MaNV
WHERE dh.SoDH = 'DH-0002';"""),
    ('K7', 'Các khoản hoàn tiền trong tháng 10/2026: ai duyệt, ai chi tiền',
     'KHOANHOAN → NHANVIEN (người duyệt, cột MaNV); KHOANHOAN → NHANVIEN (người chi, cột MaNVChi)',
     """SELECT kc.MaHoan, kc.SoTienHoan, kc.ThoiDiemDuyetHoan, nd.HoLotNV AS HoLotNguoiDuyet, nd.TenNV AS TenNguoiDuyet,
       kc.ThoiDiemChi, nc.HoLotNV AS HoLotNguoiChi, nc.TenNV AS TenNguoiChi
FROM KHOANHOAN kc
JOIN NHANVIEN nd ON nd.MaNV = kc.MaNV
LEFT JOIN NHANVIEN nc ON nc.MaNV = kc.MaNVChi
WHERE kc.ThoiDiemDuyetHoan >= '2026-10-01' AND kc.ThoiDiemDuyetHoan < '2026-11-01'
ORDER BY kc.ThoiDiemDuyetHoan;"""),
    ('K8', 'Danh sách nhân viên còn làm việc theo chức vụ',
     'NHANVIEN (tra theo thuộc tính ChucVu, không nối quan hệ khác)',
     """SELECT nv.ChucVu, nv.MaNV, nv.HoLotNV, nv.TenNV, nv.NgayVaoLam
FROM NHANVIEN nv
WHERE nv.TinhTrangNV = 'Đang làm'
ORDER BY nv.ChucVu, nv.MaNV;"""),
    ('K9', 'Phiếu bảo hành đã quá ngày hẹn trả mà chưa trả khách, kèm khách cần liên hệ',
     'PHIEUBAOHANH → CHITIETDONHANG → DONHANG → KHACHHANG',
     """SELECT bh.MaPhieuBH, bh.NgayNhan, bh.NgayHenTra, bh.TinhTrangBH, ct.TenHangChot, dh.SoDH, kh.HoLotKH, kh.TenKH, kh.SDTKH
FROM PHIEUBAOHANH bh
JOIN CHITIETDONHANG ct ON ct.MaDH = bh.MaDH AND ct.SoDongDH = bh.SoDongDH
JOIN DONHANG dh ON dh.MaDH = ct.MaDH
LEFT JOIN KHACHHANG kh ON kh.MaKH = dh.MaKH
WHERE bh.NgayTraThucTe IS NULL AND bh.NgayHenTra < '2026-11-01'
ORDER BY bh.NgayHenTra;"""),
]


def so_giao_cat():
    import json
    import ve_dothi
    _, idx, E, role, loops = ve_dothi.doc_do_thi()
    d = json.load(open(ve_dothi.CACHE, encoding='utf-8'))
    pos = {int(k): tuple(v) for k, v in d['pos'].items()}
    return ve_dothi.chi_phi(pos, E, len(idx), True)[1]


def main():
    global NCROSS
    NCROSS = so_giao_cat()
    R = dothi.run()
    A = dothi.arcs(R)
    N = num(R)
    nodes = R['nodes']
    adj = {}
    inc = {n: 0 for n in nodes}
    for i, j, kind, fk, f, b in A:
        if i != j:
            adj.setdefault(i, []).append(j)
            inc[j] += 1
    entry = [n for n in nodes if inc[n] == 0 and adj.get(n)]
    fkm = fk_map(R)
    paths = []
    for e in entry:
        for p in paths_from(adj, e, [e]):
            if len(p) >= 2:
                paths.append(p)
    # chạy thử SQL
    con = sqlite3.connect(':memory:')
    con.execute('PRAGMA foreign_keys=ON')
    con.executescript(open(os.path.join(HERE, '..', 'sql', '01_tao_bang.sql'), encoding='utf-8').read())
    con.executescript(open(os.path.join(HERE, '..', 'sql', '02_du_lieu_minh_hoa.sql'), encoding='utf-8').read())
    sqls, counts = [], []
    for p in paths:
        q = sql_gen.join_chain(p, fkm)
        c = len(con.execute(q).fetchall())
        sqls.append(q)
        counts.append(c)
    kres = []
    for k, ten, duong, q in K_QUERIES:
        rows = con.execute(q).fetchall()
        kres.append(len(rows))
    bad = [(i + 1, ' → '.join(p)) for i, (p, c) in enumerate(zip(paths, counts)) if c == 0 and tuple(p) not in ZERO_OK]
    assert not bad, bad
    assert all(c == 0 for p, c in zip(paths, counts) if tuple(p) in ZERO_OK)
    # ghi file SQL
    with open(os.path.join(HERE, '..', 'sql', '03_truy_van_cac_duong_truy_xuat.sql'), 'w', encoding='utf-8') as f:
        f.write(f'-- {len(paths)} truy vấn cho các con đường truy xuất từ {len(entry)} nút vào (sinh bằng tools/gen_chuong3.py).\n'
                '-- Mỗi truy vấn nối các quan hệ theo từng cung của đường; đã chạy thử trên dữ liệu minh họa (sql/02) và đều có kết quả, trừ đường rỗng đúng quy tắc (có ghi chú).\n\n')
        for i, (p, q, c) in enumerate(zip(paths, sqls, counts), 1):
            f.write(f'-- Đường {i}: {" → ".join(p)}\n-- {sentence(p)}\n-- Số dòng trên dữ liệu minh họa: {c}' + (f' ({ZERO_OK[tuple(p)]})' if tuple(p) in ZERO_OK else '') + f'\n{q}\n\n')
    with open(os.path.join(HERE, '..', 'sql', '04_truy_van_khai_thac.sql'), 'w', encoding='utf-8') as f:
        f.write('-- Các truy vấn khai thác theo con đường truy xuất (chương 3, mục 3.3.3). Đã chạy thử trên dữ liệu minh họa.\n\n')
        for (k, ten, duong, q), c in zip(K_QUERIES, kres):
            f.write(f'-- {k}: {ten}\n-- Con đường: {duong}\n-- Số dòng trên dữ liệu minh họa: {c}\n{q}\n\n')
    draw(R, N, entry, 'do_thi_quan_he_ten')
    draw(R, N, entry, 'do_thi_quan_he', so=True)
    # ---------------------------------------------------------------- viết chương
    w('# CHƯƠNG 3: KẾT QUẢ THỰC NGHIỆM')
    w()
    w(f'Chương này biểu diễn lược đồ sau cải tiến ({len(nodes) + 1} quan hệ, mục 2.3.6) thành đồ thị quan hệ theo thuật toán B1–B7 của giáo trình, '
      'nêu các con đường truy xuất và ngữ nghĩa của từng con đường, rồi viết truy vấn SQL cho các con đường đó. Phép tính do '
      f'`tools/dothi.py` đối chiếu; các truy vấn đều đã chạy thử trên dữ liệu minh họa nhỏ (`sql/02_du_lieu_minh_hoa.sql`, {len(nodes) + 1} bảng, không '
      'vi phạm khóa ngoại) và đều trả về ít nhất một dòng.')
    w()
    w('## 3.1 ĐỒ THỊ QUAN HỆ')
    w()
    w('**Quy ước áp dụng** (giáo trình cho phép nhiều đồ thị cho cùng một lược đồ; mục 10.4):')
    w()
    w('- **Q1.** Mỗi quan hệ dùng khóa chính làm khóa ưu tiên (giáo trình 10.4.2: khi cài đặt chọn một khóa ưu tiên).')
    w('- **Q2.** Hai cột là cùng một thuộc tính khi nối nhau bằng khóa ngoại, **trừ** khóa ngoại tới NHANVIEN không thuộc khóa chính: nhân viên '
      'lập đơn, xác nhận thu, giao hàng, nhập hàng… là các vai trò khác nhau của cùng một người nên mỗi cung vai trò được giữ riêng, '
      'không bị coi là thừa. Khóa ngoại **phụ** tới NHANVIEN có tên khác MaNV (MaNVThu, MaNVXacNhan, MaNVDuyet, MaNVChi) ghi thêm một '
      'vai trò nữa của nhân viên trên cùng quan hệ; chúng cùng đích với cung của MaNV (hoặc đã có cung tới NHANVIEN) nên không vẽ thành cung song song, '
      'và được truy xuất bằng cách nối thêm cột đó (ví dụ truy vấn K7).')
    w('- **Q3.** Cung A → B bị coi là thừa (PTH_Thừa) khi B đạt được qua cung A → H mà đường đó bắt buộc (không rỗng), hoặc khóa của B nằm trong khóa của H.')
    w('- **Q4.** Khuyên (cung từ một nút về chính nó) là liên kết loại hàng cha – con (MaLoaiCha); nằm ngoài thuật toán.')
    w()
    w('**Bước 1: Biến C thành phân rã đồng nhất C_d.** Hai quan hệ có khóa tương hỗ thì gộp thành một nút. HANGCOSERI và SERIMATHANG đều có khóa '
      '{MaSeri} nên gộp; quan hệ gộp là HANGCOSERI(MaSeri, SoSeri, MaSP, MaPN, SoDongPN, MaDH, SoDongDH, TinhTrangSeri, ThoiDiemNhap), '
      'tức hình dạng ban đầu của quan hệ này. Các quan hệ còn lại giữ nguyên: **' + str(len(nodes)) + ' nút**.')
    w()
    w('**Bước 2: Tạo nút và quan hệ nút.** Mỗi quan hệ là một nút Nᵢ với Q_Nᵢ = Qᵢ:')
    w()
    for n in nodes:
        mem = R['members'][n]
        cols = []
        for m in mem:
            for a in luoc_do.improved()[m]['attrs']:
                if a[0] not in cols:
                    cols.append(a[0])
        w(f'(Q{N[n]}) {n}({", ".join(cols)}).')
    w()
    w(f'**Bước 3: Tạo nút bản lề và quan hệ nút bản lề.** Xét giao Q_ij = Qᵢ ∩ Qⱼ của mọi cặp nút; có {R["pairs"]} cặp có giao khác rỗng. Nếu khóa của '
      'Q_ij là khóa của một quan hệ nào đó thì không tạo nút bản lề (bảng 3.1).')
    w()
    w('| Qᵢ ∩ Qⱼ | Giao | Khóa của giao | Trùng khóa của | Kết luận |')
    w('|---|---|---|---|---|')
    for i, j, S, ks, match in R['b3']:
        kk = ' hoặc '.join(nm(k) for k in ks)
        mt = ', '.join(f'Q{N[m]}' for m in match) or '—'
        w(f'| Q{N[i]} ∩ Q{N[j]} | {nm(S)} | {kk} | {mt} | {"không tạo" if match else "tạo nút bản lề"} |')
    w()
    w('*Bảng 3.1: Giao các cặp quan hệ nút*')
    w()
    w('**Kết luận:** ' + ('không tạo nút bản lề nào.' if not R['hinge'] else f'tạo {len(R["hinge"])} nút bản lề: {", ".join(R["hinge"])}.'))
    w()
    w('**Bước 4: Tạo cung và quan hệ cung.** Với mỗi nút Nᵢ: PTH(Nᵢ) là tập các nút Nⱼ có khóa nằm trong Qᵢ; PTH_Thừa(Nᵢ) là các nút đạt được '
      'qua nút khác; LK(Nᵢ) là các nút có khóa nằm trong khóa của Nᵢ (lồng khóa); LK_Thừa(Nᵢ) là các lồng khóa đạt được qua lồng khóa khác; '
      'Cung(Nᵢ) = (PTH − PTH_Thừa) ∪ (LK − LK_Thừa).')
    w()
    w('| Nút | PTH(Nᵢ) | PTH_Thừa(Nᵢ) | LK(Nᵢ) | LK_Thừa(Nᵢ) | Cung(Nᵢ) |')
    w('|---|---|---|---|---|---|')
    ls = lambda s: ', '.join(str(N[x]) for x in sorted(s, key=nodes.index)) if s else '–'
    for n in nodes:
        x = R['res'][n]
        w(f'| {N[n]}. {n} | {ls(x["pth"])} | {ls(x["thua"])} | {ls(x["lk"])} | {ls(x["lk_thua"])} | {ls(x["cung"])} |')
    w()
    w('*Bảng 3.2: Tập cung của từng nút*')
    w()
    w(f'Từ bảng trên, mỗi nút Nⱼ ∈ Cung(Nᵢ) cho một cung có hướng cᵢⱼ từ Nᵢ đến Nⱼ với quan hệ cung Qᵢⱼ = Qᵢ[KQᵢ ∪ KQⱼ]. Có tất cả **{len(A)} quan hệ cung** '
      f'(kể cả khuyên của LOAIHANG và các cung vai trò tới NHANVIEN):')
    w()
    w('| Cung | Quan hệ cung Qᵢⱼ | Bản số xuôi (m, A, M) | Bản số ngược (m, A, M) |')
    w('|---|---|---|---|')
    imp = luoc_do.improved()
    for i, j, kind, fk, f, b in A:
        rel, cols, tgt = fk
        key = list(imp[rel]['pk'])
        attrs = key + [c for c in cols if c not in key]
        w(f'| Q{N[i]}.{N[j]}: {i} → {j} | {i}({", ".join(attrs)}) | ({", ".join(f)}) | ({", ".join(b)}) |')
    w()
    w('*Bảng 3.3: Quan hệ cung và bản số*')
    w()
    w('**Bước 5: Hủy nút bản lề thừa.** Không thực hiện vì không có nút bản lề.')
    w()
    w('**Bước 6: Mịn hóa các quan hệ nút.** Với mỗi cung Nᵢ → Nⱼ, hủy khỏi Qᵢ⁺ các thuộc tính khóa của Qⱼ không phải thuộc tính khóa của Qᵢ (chúng đã nằm ở quan hệ cung). Các nút bị thay đổi:')
    w()
    w('| Nút | Quan hệ nút sau mịn hóa | Thuộc tính chuyển sang quan hệ cung |')
    w('|---|---|---|')
    for n in nodes:
        mem = R['members'][n][0]
        fkcols = []
        for i, j, kind, fk, f, b in A:
            if i == n and fk and fk[0] in R['members'][n]:
                for c in fk[1]:
                    if c not in imp[fk[0]]['pk'] and c not in fkcols:
                        fkcols.append(c)
        if fkcols:
            cols = []
            for m in R['members'][n]:
                for a in imp[m]['attrs']:
                    if a[0] not in cols and a[0] not in fkcols:
                        cols.append(a[0])
            w(f'| {n} | {n}({", ".join(cols)}) | {", ".join(fkcols)} |')
    w()
    w('**Bước 7: Tạo cung vô hướng.** Không có nút Nₖ nào thỏa điều kiện (quan hệ chỉ gồm thuộc tính khóa, có đúng hai cung ra và không có cung vào): '
      'quan hệ nối n–n của lược đồ đều có thuộc tính riêng (GIATRITHONGSO có GiaTriTS; CHITIET* có số lượng, giá). Vì vậy không có cung vô hướng và '
      'đồ thị quan hệ chỉ có cung có hướng (hình 3.1).')
    w()
    w('![Hình 3.1: Đồ thị quan hệ của PowerTech (nút viền đậm là nút vào)](hinh/do_thi_quan_he.png)')
    w()
    w('*Hình 3.1: Đồ thị quan hệ (' + str(len(nodes)) + ' nút, ' + str(len(A)) + ' cung; cung xám là cung vai trò tới NHANVIEN; nút viền đậm là nút vào)*')
    w()
    w('Hình 3.1 chỉ ghi số thứ tự nút (tên nút ở bảng 3.2). Hình 3.2 vẽ cùng đồ thị nhưng ghi tên quan hệ để dễ đối chiếu. '
      'Đồ thị này không vẽ phẳng được (đã kiểm bằng thuật toán kiểm tra tính phẳng), nên khi mọi cung là đường thẳng vẫn còn chỗ hai cung cắt nhau. '
      'Các nút được xếp để chỉ còn ' + str(NCROSS) + ' chỗ cắt, không cung nào đi xuyên qua một nút khác; chỗ hai cung cắt nhau không phải là nút. '
      'Con số này do chương trình tìm được, chưa chứng minh là nhỏ nhất.')
    w()
    w('![Hình 3.2: Đồ thị quan hệ có tên nút](hinh/do_thi_quan_he_ten.png)')
    w()
    w('*Hình 3.2: Đồ thị quan hệ có tên nút (cùng đồ thị với hình 3.1)*')
    w()
    w('**Nhận xét về đồ thị.** (1) Có nút đạt được bằng hai mạch đi khác nhau, làm lộ ràng buộc nhất quán: từ PHIEUBAOHANH tới CHITIETDONHANG có mạch trực tiếp và mạch '
      'qua HANGCOSERI (hai mạch phải cùng mặt hàng; mạch trực tiếp là lần mua ứng với phiếu, mạch qua HANGCOSERI là lần bán gần nhất, nên khi chiếc được bán lại, người mua của phiếu phải tra theo mạch trực tiếp); từ KHOANHOAN tới DONHANG có mạch qua THANHTOAN, mạch qua HOSODOITRA và mạch qua PHIEUBAOHANH (các mạch phải cùng một đơn). '
      'Đó là ràng buộc 2 và 4 ở mục 2.3.6. (2) CHITIETTRA chỉ nối với HOSODOITRA và HANGCOSERI; dòng đơn được trả là (HOSODOITRA.MaDH, SoDongDH) nên đường từ dòng trả tới dòng đơn đi qua HOSODOITRA '
      'và cần cả MaDH lẫn SoDongDH, không phải một cung đơn. (3) NHANVIEN là nút đích của nhiều cung vai trò (lập đơn, xác nhận thu, giao, nhập, tạo mã, tài khoản…): '
      'đó là các con đường **truy trách nhiệm** từ chứng từ về người thực hiện; chức vụ ChucVu của người đó cho biết khâu họ được làm (truy vấn K6–K8). (4) Đồ thị không duy nhất: chọn khóa ưu tiên khác (ví dụ SoDH cho DONHANG) cho đồ thị khác nhưng tương đương về bảo toàn thông tin và PTH.')
    w()
    # ---------------------------------------------------------------- 3.2
    w('## 3.2 Ý NGHĨA CÁC CON ĐƯỜNG TRUY XUẤT')
    w()
    w('### 3.2.1 Nút vào')
    w()
    w(f'Theo giáo trình, nút vào là nút mà người dùng cung cấp giá trị khóa để truy xuất trực tiếp một bộ. Để liệt kê các con đường nhiều ngữ nghĩa nhất, '
      'chương này chọn **nút vào là các nút không có cung đi tới** (không quan hệ nào trỏ về nó bằng cung có hướng), vì từ nút khác chỉ đến được các nút này bằng '
      f'cách đi ngược cung (cho nhiều bộ). Có **{len(entry)} nút vào**: ' + ', '.join(f'{N[e]}. {e}' for e in entry) + '. '
      f'Từ mỗi nút vào, mọi mạch đi theo chiều cung đến nút cuối (không lặp nút) là một con đường truy xuất; tổng cộng **{len(paths)} con đường**. Các nút còn lại '
      '(KHACHHANG, DONHANG, MATHANG…) nằm trên các đường này và cũng là ngõ vào tra cứu theo khóa riêng (mục 3.4).')
    w()
    w('### 3.2.2 Con đường truy xuất cơ bản (theo từng cung)')
    w()
    w('Mỗi cung có hai con đường: xuôi theo cung (cho một bộ, (1,1,1) hoặc (0,-,1)) và ngược lại (cho n bộ). Ngữ nghĩa:')
    w()
    w('| Cung | Xuôi (từ một bộ của nút đi) | Ngược (từ một bộ của nút đến) |')
    w('|---|---|---|')
    for i, j, kind, fk, f, b in A:
        fw, bw = ARC[(i, j)]
        w(f'| {N[i]} → {N[j]} | Cho biết {NOUN[i]} {fw} ({", ".join(f)}) | Từ một {NOUN[j]} cho biết {bw} ({", ".join(b)}) |')
    w()
    w('*Bảng 3.4: Ngữ nghĩa các con đường truy xuất cơ bản*')
    w()
    w('### 3.2.3 Các con đường truy xuất dài từ nút vào')
    w()
    w('| Đường | Mạch đi | Ý nghĩa dữ liệu | Số dòng trên dữ liệu minh họa |')
    w('|---|---|---|---|')
    for i, (p, c) in enumerate(zip(paths, counts), 1):
        w(f'| {i} | {" → ".join(str(N[x]) for x in p)} | {sentence(p)} | {c} |')
    w()
    w('*Bảng 3.5: ' + str(len(paths)) + ' con đường truy xuất từ các nút vào (số là số thứ tự nút ở bảng 3.2)*')
    w()
    for i, (p, c) in enumerate(zip(paths, counts), 1):
        if tuple(p) in ZERO_OK:
            w(f'Đường {i} cho 0 dòng là **đúng quy tắc**: {ZERO_OK[tuple(p)]}.')
            w()
    # ---------------------------------------------------------------- 3.3
    w('## 3.3 CÁC TRUY VẤN BẰNG NGÔN NGỮ SQL')
    w()
    w('### 3.3.1 Quy tắc chung')
    w()
    w('Mỗi con đường truy xuất tương ứng một câu SELECT nối (JOIN) các quan hệ theo thứ tự các nút trên đường; điều kiện nối là khóa ngoại của cung '
      '(cột của nút đi bằng cột khóa của nút đến). Danh sách cột chỉ gồm khóa chính của các quan hệ trên đường (cột trùng giá trị do nối thì lấy một lần), '
      'đủ để nhận ra mỗi dòng kết quả là một bộ chứng từ nào; muốn xem thêm thông tin thì thêm cột cần thiết:')
    w()
    w('```sql')
    w('SELECT a0.<khóa chính>, a1.<khóa chính>, a2.<khóa chính>, ...')
    w('FROM   <nút vào> a0')
    w('JOIN   <nút 1>   a1 ON a0.<khóa ngoại> = a1.<khóa>')
    w('JOIN   <nút 2>   a2 ON a1.<khóa ngoại> = a2.<khóa>')
    w('...')
    w('```')
    w()
    w('Với nút HANGCOSERI (gộp từ HANGCOSERI và SERIMATHANG) câu lệnh nối thêm SERIMATHANG theo MaSeri để lấy lại đủ số seri và mặt hàng. '
      'Đã sinh **' + str(len(paths)) + ' câu lệnh**, lưu ở `sql/03_truy_van_cac_duong_truy_xuat.sql`; mỗi câu đã chạy thử và đều trả về ít nhất một dòng (cột cuối bảng 3.5).')
    w()
    w('### 3.3.2 Một số câu truy vấn của các con đường')
    w()
    pick = []
    for want in (('KHOANHOAN', 'PHIEUBAOHANH', 'CHITIETDONHANG', 'DONHANG', 'KHACHHANG'), ('KHOANHOAN', 'THANHTOAN', 'DONHANG', 'KHACHHANG'),
                 ('CHITIETTRA', 'HANGCOSERI', 'CHITIETPHIEUNHAP', 'PHIEUNHAP', 'NHACUNGCAP'), ('GIATRITHONGSO', 'DINHNGHIATHONGSO', 'LOAIHANG'),
                 ('LANGIAO', 'PHIEUGIAO', 'DONHANG', 'KHACHHANG')):
        for i, p in enumerate(paths):
            if tuple(p) == want:
                pick.append(i)
    for i in pick:
        p = paths[i]
        w(f'**Đường {i + 1}: {" → ".join(p)}**')
        w()
        w(f'Ý nghĩa: {sentence(p)}')
        w()
        w('```sql')
        w(sqls[i])
        w('```')
        w()
    w('### 3.3.3 Truy vấn khai thác theo con đường truy xuất')
    w()
    w('Các yêu cầu khai thác thực tế dùng các con đường (cả xuôi và ngược) của đồ thị. Mỗi truy vấn dưới đây ở `sql/04_truy_van_khai_thac.sql` và đã chạy thử:')
    w()
    for (k, ten, duong, q), c in zip(K_QUERIES, kres):
        w(f'**{k}. {ten}** (đường: {duong}; {c} dòng trên dữ liệu minh họa)')
        w()
        w('```sql')
        w(q)
        w('```')
        w()
    w('Ghi chú: K3 quy ước chiều biến động theo LoaiBienDong (Nhập và Nhận lại làm tăng; Xuất bán làm giảm; Chuyển nhóm cần thêm nhóm đích '
      'nên chưa tính); quy ước dấu của sổ kho chưa chốt với cửa hàng và là điểm cần xác nhận.')
    w()
    w('## 3.4 NGÕ VÀO TRA CỨU VÀ CHỈ MỤC ĐỀ XUẤT')
    w()
    w('Giáo trình Bài 9 nhấn mạnh phép kết là thao tác chính và cần chỉ mục cho cột nối. Hai nhóm chỉ mục đề xuất, suy từ đồ thị:')
    w()
    w('1. **Ngõ vào tra cứu theo khóa riêng** (người dùng cung cấp giá trị): đã có chỉ mục tự động từ UNIQUE: SKU (MATHANG), SoDH (DONHANG), SoPhieu (PHIEUNHAP), '
      'CodeMG (MAGIAMGIA), (MaSP, SoSeri) (SERIMATHANG), (MaSP, ViTriAnh) (ANHMATHANG), MaDH (PHIEUGIAO), TenDangNhap, MaKH, MaNV (TAIKHOAN). Cần thêm chỉ mục tìm khách theo SDTKH và nhân viên theo tên (TenKH, TenNV).')
    w('2. **Cột khóa ngoại của cung** nên có chỉ mục để phép nối theo chiều ngược (từ cha xuống n con) nhanh: DONHANG(MaKH), DONHANG(MaNV), CHITIETDONHANG(MaSP), '
      'THANHTOAN(MaDH), HOSODOITRA(MaDH), KHOANHOAN(MaTT), KHOANHOAN(MaHS), LANNHANLAI(MaHS), GIAODICHKHO(MaSP, ThoiDiemGD), PHIEUBAOHANH(MaDH, SoDongDH), '
      'HANGCOSERI(MaDH, SoDongDH), HANGCOSERI(MaPN, SoDongPN), và các khóa ngoại phụ tới NHANVIEN (MaNVDuyet, MaNVChi, MaNVThu, MaNVXacNhan) để tra “một nhân viên đã duyệt, chi, thu những gì”.')
    w()
    w('Khẳng định tốc độ cần đo trên dữ liệu thật; báo cáo chưa đo hiệu năng.')
    w()
    out = os.path.join(HERE, '..', 'chuong', '03_chuong3.md')
    open(out, 'w', encoding='utf-8').write('\n'.join(OUT) + '\n')
    json.dump(dict(nodes=len(nodes), arcs=len(A), entry=len(entry), paths=len(paths), zero=sum(1 for c in counts if c == 0), k=len(kres)),
              open(os.path.join(HERE, 'so_lieu_chuong3.json'), 'w'))
    print('nút', len(nodes), 'cung', len(A), 'nút vào', [N[e] for e in entry], 'đường', len(paths), 'dòng min', min(counts), 'K:', kres)


if __name__ == '__main__':
    main()
