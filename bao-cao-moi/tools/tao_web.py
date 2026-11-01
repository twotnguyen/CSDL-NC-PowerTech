#!/usr/bin/env python3
"""Ghép web/mau.html với hình, lược đồ và SQL của báo cáo thành một file web/index.html chạy được khi mở trực tiếp.

SQLite chạy trong trình duyệt bằng sql.js; dữ liệu là sql/01 và sql/02. Chạy:  python3 tools/tao_web.py [file_artifact.html]
"""
import base64
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BC = os.path.join(HERE, '..')
sys.path.insert(0, HERE)
import erd
import luoc_do

R = luoc_do.improved()
HINH = [
    ('ERD', 'erd_tong_quat', 'Hình 1.1', 'Mô hình ERD tổng quát'),
    *[('ERD', f'erd_nhom{k}', f'Hình 1.{int(k) + 1}', ten) for k, (ten, _) in erd.GROUPS.items()],
    ('Sơ đồ quan hệ', 'sodo_quanhe_tong', 'Hình 2.1', 'Sơ đồ quan hệ tổng quát sau cải tiến'),
    ('Sơ đồ quan hệ', 'sodo_quanhe_b1', 'Hình 2.2', 'Hàng hóa, ảnh và thông số'),
    ('Sơ đồ quan hệ', 'sodo_quanhe_b2', 'Hình 2.3', 'Khách hàng, nhân viên và tài khoản'),
    ('Sơ đồ quan hệ', 'sodo_quanhe_b3', 'Hình 2.4', 'Đơn hàng, thanh toán và giao hàng'),
    ('Sơ đồ quan hệ', 'sodo_quanhe_b4', 'Hình 2.5', 'Nhập hàng, số seri và kho'),
    ('Sơ đồ quan hệ', 'sodo_quanhe_b5', 'Hình 2.6', 'Đổi trả, hoàn tiền và bảo hành'),
    ('Phân rã', 'phan_ra_chitiettra', 'Hình 2.7', 'Phân rã CHITIETTRA theo MaHS → MaDH'),
    ('Phân rã', 'phan_ra_phieubaohanh', 'Hình 2.8', 'Phân rã PHIEUBAOHANH: bỏ cột MaSP'),
    ('Phân rã', 'phan_ra_hangcoseri', 'Hình 2.9', 'Phân rã HANGCOSERI thành bốn thành phần'),
    ('Phân rã', 'phan_ra_4nf', 'Hình 2.10', 'Từ quan hệ lưu chung ảnh và thông số đến 4NF'),
    ('Use Case', 'usecase_tong_quat', 'Hình 2.11', 'Use Case tổng quát'),
    ('Use Case', 'usecase_doi_tuong_ngoai', 'Hình 2.12', 'Quản lý đối tượng ngoài'),
    ('Use Case', 'usecase_danh_muc', 'Hình 2.13', 'Quản lý danh mục cơ bản'),
    ('Use Case', 'usecase_nghiep_vu', 'Hình 2.14', 'Quản lý nghiệp vụ'),
    ('Use Case', 'usecase_tim_kiem', 'Hình 2.15', 'Tìm kiếm'),
    ('Use Case', 'usecase_thong_ke', 'Hình 2.16', 'Thống kê'),
    ('Lưu đồ', 'luudo_don_hang', 'Hình 2.17', 'Tình trạng đơn hàng'),
    ('Lưu đồ', 'luudo_doi_tra', 'Hình 2.18', 'Đổi trả hàng, hoàn tiền'),
    ('Lưu đồ', 'luudo_bao_hanh', 'Hình 2.19', 'Tiếp nhận và xử lý bảo hành'),
    ('Lưu đồ', 'luudo_kho', 'Hình 2.20', 'Ba nhóm hàng trong kho'),
    ('Đồ thị', 'do_thi_quan_he_chinh', 'Hình 3.1', 'Đồ thị quan hệ, phần chính'),
    ('Đồ thị', 'do_thi_quan_he', 'Hình 3.2', 'Đồ thị quan hệ đầy đủ: 25 nút, 43 cung'),
]


def doc(*p):
    return open(os.path.join(BC, *p), encoding='utf-8').read()


def anh(ten):
    b = open(os.path.join(BC, 'hinh', ten + '.png'), 'rb').read()
    return 'data:image/png;base64,' + base64.b64encode(b).decode()


def bo_the(s):
    return re.sub(r'<[^>]+>', '', s).replace('**', '').replace('`', '').strip()


def hang(md, sau, truoc=None):
    """Các hàng bảng Markdown trong đoạn từ tiêu đề sau tới tiêu đề truoc."""
    a = md.index(sau)
    b = md.index(truoc, a) if truoc else len(md)
    ra = []
    for l in md[a:b].splitlines():
        if l.startswith('|') and not re.match(r'^\|[\s:|-]+\|$', l):
            ra.append([bo_the(c) for c in l.strip().strip('|').split('|')])
    return ra[1:]


def duong():
    ra = []
    for m in re.finditer(r'-- Đường (\d+): ([^\n]+)\n-- ([^\n]+)\n-- Số dòng trên dữ liệu minh họa: (\d+)[^\n]*\n(.*?;)', doc('sql', '03_truy_van_cac_duong_truy_xuat.sql'), re.S):
        ra.append(dict(so=int(m[1]), mach=[x.strip() for x in m[2].split('→')], yNghia=m[3].strip(), dong=int(m[4]), sql=m[5].strip()))
    assert len(ra) == 61, len(ra)
    return ra


def khai_thac():
    ra = []
    for m in re.finditer(r'-- (K\d): ([^\n]+)\n-- Con đường: ([^\n]+)\n-- Số dòng trên dữ liệu minh họa: (\d+)[^\n]*\n(.*?;)\s*(?=\n-- K\d|\Z)', doc('sql', '04_truy_van_khai_thac.sql'), re.S):
        ra.append(dict(ma=m[1], ten=m[2].strip(), duong=m[3].strip(), dong=int(m[4]), sql=m[5].strip()))
    assert len(ra) == 9, len(ra)
    return ra


def bang():
    md = doc('chuong', '02_chuong2.md')
    dc = {h[1]: dict(khoa=h[2], truoc=h[3], sau=h[4]) for h in hang(md, '2.3.9 Đánh giá lược đồ sau cải tiến', '## 2.4 ')}
    assert len(dc) == 26, len(dc)
    ra = []
    for n in luoc_do.ORDER_IMPROVED:
        r = R[n]
        fk = {}
        for cols, cha, _ in r['fks']:
            for c in cols:
                fk[c] = cha
        ra.append(dict(ten=n, loai=r.get('loai', ''), moTa=r.get('ten', ''), tanTu=r.get('tantu', ''), rangBuoc=r.get('rangbuoc', ''), **dc[n],
                       cot=[dict(ten=a[0], kieu=a[1], rong=a[2] == 'NULL', y=a[3], pk=a[0] in r['pk'], fk=fk.get(a[0])) for a in r['attrs']]))
    return ra


def cung():
    md = doc('chuong', '03_chuong3.md')
    ban_so = hang(md, 'Bước 4: Tạo cung', '**Bước 5')
    ban_so = [h for h in ban_so if len(h) == 4 and h[0].startswith('Q')]
    nghia = {h[0]: h[1:] for h in hang(md, '3.2.2 Con đường truy xuất cơ bản', '3.2.3 Các con đường') if '→' in h[0]}
    so = {}
    for h in ban_so:
        m = re.match(r'Q(\d+)\.(\d+): (.+?) → (.+)', h[0])
        k = f'{m[1]} → {m[2]}'
        so[k] = dict(cung=k, di=m[3], den=m[4], quanHe=h[1], xuoi=h[2], nguoc=h[3], yXuoi=nghia.get(k, ['', ''])[0], yNguoc=nghia.get(k, ['', ''])[1])
    assert len(so) == 43, len(so)
    return list(so.values())


def tao():
    data = dict(hinh=[dict(nhom=a, ma=b, so=c, ten=d, src=anh(b)) for a, b, c, d in HINH], bang=bang(), cung=cung(), duong=duong(), khaiThac=khai_thac(),
                taoBang=doc('sql', '01_tao_bang.sql'), duLieu=doc('sql', '02_du_lieu_minh_hoa.sql'))
    mau = open(os.path.join(BC, 'web', 'mau.html'), encoding='utf-8').read()
    # </script> trong chuỗi dữ liệu sẽ cắt thẻ script nên phải thoát
    than = mau.replace('/*DATA*/null', json.dumps(data, ensure_ascii=False).replace('</', '<\\/'))
    trang = '<!doctype html>\n<html lang="vi">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n</head>\n<body>\n' + than + '\n</body>\n</html>\n'
    open(os.path.join(BC, 'web', 'index.html'), 'w', encoding='utf-8').write(trang)
    if len(sys.argv) > 1:
        open(sys.argv[1], 'w', encoding='utf-8').write(than)
    print('web/index.html', round(len(trang) / 1048576, 1), 'MB |', len(data['hinh']), 'hình,', len(data['bang']), 'bảng,', len(data['cung']), 'cung,', len(data['duong']), 'đường,', len(data['khaiThac']), 'truy vấn K')


if __name__ == '__main__':
    tao()
