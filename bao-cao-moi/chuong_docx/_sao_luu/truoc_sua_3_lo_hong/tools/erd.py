"""Mô hình thực thể – kết hợp (ERD): tên mối kết hợp (động từ) và bản số (min,max) suy từ lược đồ quan hệ.

Bản số ghi theo cách của giáo trình PTTK: (min,max) đặt cạnh thực thể, cho biết mỗi thể hiện của thực thể tham gia
mối kết hợp bao nhiêu lần. Ví dụ DONHANG (0,1) – Đặt – KHACHHANG (0,n): một đơn có tối đa một khách,
một khách có thể có nhiều đơn.
Dùng:  python3 tools/erd.py   (sinh hinh/erd_*.dot, .svg, .png bằng Graphviz)
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import luoc_do

# (quan hệ con, cột khóa ngoại) -> tên mối kết hợp (động từ)
VERB = {
    ('LOAIHANG', 'MaLoaiCha'): 'Thuộc nhóm lớn', ('MATHANG', 'MaLoai'): 'Phân loại', ('MATHANG', 'MaTH'): 'Mang nhãn',
    ('ANHMATHANG', 'MaSP'): 'Minh họa', ('DINHNGHIATHONGSO', 'MaLoai'): 'Quy định',
    ('DONHANG', 'MaKH'): 'Đặt', ('DONHANG', 'MaNV'): 'Lập', ('DONHANG', 'MaMG'): 'Áp dụng',
    ('THANHTOAN', 'MaDH'): 'Thu tiền cho', ('THANHTOAN', 'MaNV'): 'Xác nhận thu',
    ('PHIEUGIAO', 'MaDH'): 'Giao', ('PHIEUGIAO', 'MaNV'): 'Phụ trách giao',
    ('PHIEUNHAP', 'MaNCC'): 'Cung cấp', ('PHIEUNHAP', 'MaNV'): 'Lập phiếu nhập',
    ('HANGCOSERI', 'MaSP'): 'Là chiếc của', ('HANGCOSERI', 'MaPN,SoDongPN'): 'Nhập qua dòng',
    ('HANGCOSERI', 'MaDH,SoDongDH'): 'Bán qua dòng', ('GIAODICHKHO', 'MaSP'): 'Ghi biến động',
    ('GIAODICHKHO', 'MaNV'): 'Thực hiện', ('HOSODOITRA', 'MaDH'): 'Đề nghị trả', ('HOSODOITRA', 'MaNV'): 'Tiếp nhận đổi trả',
    ('LANNHANLAI', 'MaHS'): 'Nhận lại', ('LANNHANLAI', 'MaNV'): 'Kiểm tra', ('KHOANHOAN', 'MaTT'): 'Hoàn cho khoản thu',
    ('KHOANHOAN', 'MaHS'): 'Hoàn theo hồ sơ', ('KHOANHOAN', 'MaNV'): 'Duyệt hoàn',
    ('PHIEUBAOHANH', 'MaSeri'): 'Bảo hành chiếc', ('PHIEUBAOHANH', 'MaDH,SoDongDH'): 'Mua tại dòng',
    ('PHIEUBAOHANH', 'MaNV'): 'Tiếp nhận bảo hành',
    ('TAIKHOAN', 'MaKH'): 'Đăng ký cho', ('TAIKHOAN', 'MaNV'): 'Cấp cho',
    ('MAGIAMGIA', 'MaNV'): 'Tạo mã',
    ('THANHTOAN', 'MaNVThu'): 'Thu hộ khi giao', ('PHIEUNHAP', 'MaNVXacNhan'): 'Xác nhận phiếu nhập',
    ('LANNHANLAI', 'MaNVDuyet'): 'Duyệt hàng nhận lại', ('KHOANHOAN', 'MaNVChi'): 'Chi hoàn tiền',
}
# Mối kết hợp n-n có thuộc tính: tên quan hệ -> (tên hiển thị, hai đầu)
MKH = {
    'CHITIETDONHANG': ('Gồm', ['DONHANG', 'MATHANG']),
    'CHITIETPHIEUNHAP': ('Nhập', ['PHIEUNHAP', 'MATHANG']),
    'GIATRITHONGSO': ('Mang giá trị', ['MATHANG', 'DINHNGHIATHONGSO']),
    'CHITIETTRA': ('Trả', ['HOSODOITRA', 'CHITIETDONHANG']),
    'LANGIAO': ('Thử giao', ['PHIEUGIAO', 'NHANVIEN']),
}
ENTITIES = [n for n in luoc_do.ORDER if luoc_do.REL[n]['loai'] != 'mkh']
SHORT = {'LOAIHANG': 'LOẠI HÀNG', 'THUONGHIEU': 'THƯƠNG HIỆU', 'MATHANG': 'MẶT HÀNG', 'ANHMATHANG': 'ẢNH MẶT HÀNG',
         'DINHNGHIATHONGSO': 'ĐỊNH NGHĨA THÔNG SỐ', 'KHACHHANG': 'KHÁCH HÀNG', 'NHANVIEN': 'NHÂN VIÊN',
         'NHACUNGCAP': 'NHÀ CUNG CẤP', 'MAGIAMGIA': 'MÃ GIẢM GIÁ', 'DONHANG': 'ĐƠN HÀNG', 'THANHTOAN': 'THANH TOÁN',
         'PHIEUGIAO': 'PHIẾU GIAO', 'LANGIAO': 'LẦN GIAO', 'PHIEUNHAP': 'PHIẾU NHẬP', 'HANGCOSERI': 'HÀNG CÓ SERI',
         'GIAODICHKHO': 'GIAO DỊCH KHO', 'HOSODOITRA': 'HỒ SƠ ĐỔI TRẢ', 'LANNHANLAI': 'LẦN NHẬN LẠI',
         'KHOANHOAN': 'KHOẢN HOÀN', 'PHIEUBAOHANH': 'PHIẾU BẢO HÀNH', 'CHITIETDONHANG': 'CHI TIẾT ĐƠN HÀNG',
         'CHITIETPHIEUNHAP': 'CHI TIẾT PHIẾU NHẬP', 'GIATRITHONGSO': 'GIÁ TRỊ THÔNG SỐ', 'CHITIETTRA': 'CHI TIẾT TRẢ',
         'SERIMATHANG': 'SERI MẶT HÀNG', 'TAIKHOAN': 'TÀI KHOẢN'}
# Các bản số không suy ra được từ khóa ngoại: (quan hệ con, cột) -> (bản số phía con, bản số phía cha)
OVERRIDE = {
    ('PHIEUGIAO', 'MaDH'): ('(1,1)', '(0,1)'),
    ('TAIKHOAN', 'MaKH'): ('(0,1)', '(0,1)'),
    ('TAIKHOAN', 'MaNV'): ('(0,1)', '(0,1)'),
}
# Bản số cạnh thực thể cha khi cha bắt buộc phải có con
REQUIRE_CHILD = {('LANNHANLAI', 'MaHS'): False}


def fk_key(rel, cols):
    return (rel, ','.join(cols))


def relationships(R=None):
    """Danh sách mối kết hợp 'khóa ngoại': (tên, con, cha, bản số con, bản số cha, cột)."""
    R = R or luoc_do.REL
    out = []
    for n in luoc_do.ORDER:
        r = R[n]
        nullable = {a[0] for a in r['attrs'] if a[2] == 'NULL'}
        for cols, parent, pcols in r['fks']:
            k = fk_key(n, cols)
            if k not in VERB:
                continue
            opt = any(c in nullable for c in cols)
            child = '(0,1)' if opt else '(1,1)'
            par = '(0,n)'
            if k in OVERRIDE:
                child, par = OVERRIDE[k]
            out.append((VERB[k], n, parent, child, par, list(cols)))
    return out


def mkh_card():
    """Bản số hai đầu của các mối kết hợp có thuộc tính (tên MKH -> [(thực thể, bản số)])."""
    return {'CHITIETDONHANG': [('DONHANG', '(1,n)'), ('MATHANG', '(0,n)')],
            'CHITIETPHIEUNHAP': [('PHIEUNHAP', '(1,n)'), ('MATHANG', '(0,n)')],
            'GIATRITHONGSO': [('MATHANG', '(0,n)'), ('DINHNGHIATHONGSO', '(0,n)')],
            'CHITIETTRA': [('HOSODOITRA', '(1,n)'), ('CHITIETDONHANG', '(0,n)')],
            'LANGIAO': [('PHIEUGIAO', '(0,3)'), ('NHANVIEN', '(0,n)')]}


def dot(entities=None, title=None, rankdir='TB'):
    """Sinh mã DOT: thực thể (chữ nhật vàng), mối kết hợp (oval cam), mối kết hợp có thuộc tính (oval xanh)."""
    rels = relationships()
    mk = mkh_card()
    keep = set(entities) if entities else set(ENTITIES) | set(MKH)
    L = ['graph ERD {', f'  rankdir={rankdir}; splines=true; overlap=false; nodesep=0.15; ranksep=0.3; pad=0.15;',
         '  node [fontname="Helvetica", fontsize=13]; edge [fontname="Helvetica", fontsize=12, color="#555555"];']
    for n in ENTITIES:
        if n in keep:
            L.append(f'  "{n}" [label="{SHORT[n]}", shape=box, style=filled, fillcolor="#fff2cc", color="#d6b656"];')
    for n in MKH:
        if n in keep:
            L.append(f'  "{n}" [label="{SHORT[n]}", shape=ellipse, style=filled, fillcolor="#dae8fc", color="#6c8ebf"];')
            for e, b in mk[n]:
                if e in keep:
                    L.append(f'  "{n}" -- "{e}" [label="{b}"];')
    i = 0
    for verb, child, parent, bc, bp, cols in rels:
        if child in keep and (parent in keep or parent in MKH):
            tgt_ok = parent in keep
            if not tgt_ok:
                continue
            i += 1
            rid = f'r{i}'
            L.append(f'  "{rid}" [label="{verb}", shape=ellipse, style=filled, fillcolor="#ffe6cc", color="#d79b00"];')
            L.append(f'  "{child}" -- "{rid}" [label="{bc}"];')
            L.append(f'  "{rid}" -- "{parent}" [label="{bp}"];')
    L.append('}')
    return '\n'.join(L)


def overview():
    """ERD tổng quát chỉ gồm thực thể và các đường nối (tên mối kết hợp và bản số xem ở các hình theo nhóm) để chữ đủ lớn khi in trong một trang A4 dọc."""
    mk = mkh_card()
    L = ['graph ERD {', '  rankdir=LR; splines=true; overlap=false; nodesep=0.05; ranksep=0.15; pad=0.15;',
         '  node [fontname="Helvetica", fontsize=14]; edge [color="#555555"];']
    for n in ENTITIES:
        L.append(f'  "{n}" [label="{SHORT[n]}", shape=box, style=filled, fillcolor="#fff2cc", color="#d6b656"];')
    for n in MKH:
        L.append(f'  "{n}" [label="{SHORT[n]}", shape=ellipse, style=filled, fillcolor="#dae8fc", color="#6c8ebf"];')
        for e, _ in mk[n]:
            L.append(f'  "{n}" -- "{e}";')
    for _, child, parent, _, _, _ in relationships():
        L.append(f'  "{child}" -- "{parent}";')
    L.append('}')
    return '\n'.join(L)


GROUPS = {
    '1': ('Hàng hóa, ảnh và thông số', ['LOAIHANG', 'THUONGHIEU', 'MATHANG', 'ANHMATHANG', 'DINHNGHIATHONGSO', 'GIATRITHONGSO']),
    '2': ('Khách hàng, nhân viên và tài khoản', ['KHACHHANG', 'NHANVIEN', 'TAIKHOAN']),
    '3': ('Đặt hàng, thanh toán và giao hàng', ['KHACHHANG', 'MAGIAMGIA', 'DONHANG', 'CHITIETDONHANG', 'MATHANG', 'THANHTOAN',
                                                 'PHIEUGIAO', 'LANGIAO', 'NHANVIEN']),
    '4': ('Nhập hàng, số seri và kho', ['NHACUNGCAP', 'PHIEUNHAP', 'CHITIETPHIEUNHAP', 'MATHANG', 'HANGCOSERI', 'GIAODICHKHO',
                                         'CHITIETDONHANG', 'DONHANG']),
    '5': ('Đổi trả và hoàn tiền', ['HOSODOITRA', 'CHITIETTRA', 'LANNHANLAI', 'KHOANHOAN', 'THANHTOAN', 'DONHANG', 'CHITIETDONHANG']),
    '6': ('Bảo hành', ['PHIEUBAOHANH', 'HANGCOSERI', 'CHITIETDONHANG', 'DONHANG', 'MATHANG']),
    '7': ('Trách nhiệm: ai làm, ai duyệt từng khâu', ['NHANVIEN', 'TAIKHOAN', 'MAGIAMGIA', 'DONHANG', 'PHIEUGIAO', 'THANHTOAN',
                                                       'KHOANHOAN', 'HOSODOITRA', 'LANNHANLAI', 'PHIEUBAOHANH', 'PHIEUNHAP', 'GIAODICHKHO']),
}


def render(name, text):
    base = os.path.join(HERE, '..', 'hinh', name)
    open(base + '.dot', 'w', encoding='utf-8').write(text)
    for fmt in ('svg', 'png'):
        extra = ['-Gdpi=150'] if fmt == 'png' else []
        subprocess.run(['dot', f'-T{fmt}', *extra, base + '.dot', '-o', f'{base}.{fmt}'], check=True)


if __name__ == '__main__':
    render('erd_tong_quat', overview())
    for k, (ten, ents) in GROUPS.items():
        render(f'erd_nhom{k}', dot(ents))
    print('đã sinh hinh/erd_*.{dot,svg,png};', len(relationships()), 'mối kết hợp khóa ngoại +', len(MKH), 'mối kết hợp có thuộc tính')
