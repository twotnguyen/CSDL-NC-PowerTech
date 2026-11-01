#!/usr/bin/env python3
"""Sơ đồ quan hệ tổng quát 26 bảng trên một trang A4 dọc, kiểu Toad Data Modeler.

Graphviz đi đường cho 26 bảng rất rối, nên ở đây đặt bảng cố định và khai báo tay từng đường vuông góc.
Các bảng có khóa ngoại tới NHANVIEN gom vào một trục dọc; bảng có hai khóa ngoại tới NHANVIEN vẽ chung một nhánh.
Chạy xong in số giao cắt và kiểm đủ mọi khóa ngoại của lược đồ.
"""
import os
import sys

from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import luoc_do
from ve_bang import fkcols, kieu
from ve_erd import font

R = luoc_do.improved()
HINH = os.path.join(HERE, '..', 'hinh')
CO, DONG, DAU, DEM = 10, 26, 30, 6          # cỡ chữ (font() nhân đôi thành 20 px), cao dòng, cao đầu bảng, lề trong
XANH_DAU, VIEN, NET = (189, 215, 238), (91, 127, 166), (58, 95, 143)
COT = [['NHACUNGCAP', 'CHITIETPHIEUNHAP', 'ANHMATHANG', 'SERIMATHANG', 'MATHANG', 'GIATRITHONGSO', 'DINHNGHIATHONGSO', 'LOAIHANG',
        'THUONGHIEU', 'CHITIETTRA'],
       ['PHIEUNHAP', 'HANGCOSERI', 'CHITIETDONHANG', 'PHIEUBAOHANH', 'LANNHANLAI', 'HOSODOITRA', 'KHOANHOAN', 'GIAODICHKHO'],
       ['KHACHHANG', 'TAIKHOAN', 'NHANVIEN', 'MAGIAMGIA', 'DONHANG', 'THANHTOAN', 'PHIEUGIAO', 'LANGIAO']]
LE, KHE, GIA = 90, [210, 230], 30           # lề trái, bề rộng khe giữa các cột, cách giữa hai bảng trong cột


class B:
    def __init__(self, n):
        r = R[n]
        fk = fkcols(n)
        self.n, self.dong = n, []
        for ten, typ, nl, _ in r['attrs']:
            pk, f = ten in r['pk'], ten in fk
            mau, tag = ((192, 0, 0), '(PK)') if pk and not f else ((31, 78, 180), '(PFK)') if pk else ((46, 125, 50), '(FK)') if f else ((0, 0, 0), '')
            if not pk and not f and nl == 'NULL':
                mau = (128, 128, 128)
            self.dong.append((ten, kieu(typ), 'NN' if nl == 'NN' else '', tag, mau))
        f_ = font(CO)
        self.cot = [max(f_.getlength(d[k]) for d in self.dong) + 14 for k in range(4)]
        self.w = max(sum(self.cot) + 2 * DEM, font(CO, True).getlength(n) + 30)
        self.h = DAU + DONG * len(self.dong) + 8

    def y(self, ten_hoac_so):
        k = ten_hoac_so if isinstance(ten_hoac_so, int) else [d[0] for d in self.dong].index(ten_hoac_so)
        return self.t + DAU + DONG * k + DONG / 2 + 2

    @property
    def phai(self):
        return self.x + self.w

    @property
    def day(self):
        return self.t + self.h

    @property
    def tx(self):
        return self.x + self.w / 2

    def ve(self, d):
        d.rectangle([self.x, self.t, self.phai, self.day], fill='white', outline=VIEN, width=2)
        d.rectangle([self.x + 2, self.t + 2, self.phai - 2, self.t + DAU], fill=XANH_DAU)
        d.text((self.tx, self.t + DAU / 2 + 1), self.n, font=font(CO, True), fill='black', anchor='mm')
        for k, dg in enumerate(self.dong):
            x = self.x + DEM
            for j in range(4):
                d.text((x, self.y(k)), dg[j], font=font(CO), fill=dg[4], anchor='lm')
                x += self.cot[j]


def bo_cuc():
    T = {n: B(n) for n in R}
    rong = [max(T[n].w for n in c) for c in COT]
    X, x = [], LE
    for i, w in enumerate(rong):
        X.append(x)
        x += w + (KHE[i] if i < len(KHE) else 0)
    W = x + 90
    cao = {i: sum(T[n].h for n in c) + GIA * (len(c) - 1) for i, c in enumerate(COT)}
    for i, c in enumerate(COT):
        y = 0
        for n in c:
            T[n].t, T[n].x = y, X[i] + (rong[i] - T[n].w) / 2
            y += T[n].h + GIA
    return T, X, rong, W


def tuyen(T, X, rong):
    """(bảng con, bảng cha, liền/đứt, điểm...): điểm đầu ở bảng con, điểm cuối ở bảng cha."""
    k = lambda i, t: X[i] + rong[i] + t          # vị trí dọc trong khe sau cột i
    g = lambda n: T[n]
    D = []
    ml = X[0] - 24                               # các vệt ở lề trái
    mr = X[2] + rong[2] + 24                     # các vệt ở lề phải

    def ngang(c, c_dong, p, p_dong, xt=None, net=False):
        """ra sườn bảng con, đi dọc ở xt, vào sườn bảng cha; không có xt thì đi thẳng."""
        a, b = g(c), g(p)
        ya, yb = a.y(c_dong), b.y(p_dong) if xt is not None else a.y(c_dong)
        if xt is None:
            xa, xb = (a.phai, b.x) if b.tx > a.tx else (a.x, b.phai)
        else:
            xa, xb = a.phai if xt >= a.phai else a.x, b.phai if xt >= b.phai else b.x
        D.append((c, p, net, [(xa, ya), (xb, ya)] if xt is None else [(xa, ya), (xt, ya), (xt, yb), (xb, yb)]))

    def doc(c, p, net=False):
        a, b = g(c), g(p)
        D.append((c, p, net, [(a.tx, a.t), (a.tx, b.day)] if b.t < a.t else [(a.tx, a.day), (a.tx, b.t)]))

    # hàng hóa: cột trái
    lh = g('LOAIHANG')
    D.append(('LOAIHANG', 'LOAIHANG', False, [(lh.phai - 110, lh.t), (lh.phai - 110, lh.t - 17), (lh.phai - 40, lh.t - 17), (lh.phai - 40, lh.t)]))
    doc('DINHNGHIATHONGSO', 'LOAIHANG')
    doc('GIATRITHONGSO', 'DINHNGHIATHONGSO', True)
    doc('GIATRITHONGSO', 'MATHANG', True)
    doc('SERIMATHANG', 'MATHANG')
    ngang('ANHMATHANG', 'MaSP', 'MATHANG', 1, ml)
    ngang('CHITIETPHIEUNHAP', 'MaSP', 'MATHANG', 3, ml - 26)
    ngang('MATHANG', 'MaLoai', 'LOAIHANG', 0, ml)
    ngang('MATHANG', 'MaTH', 'THUONGHIEU', 0, ml - 26)
    # nhập, seri
    ngang('CHITIETPHIEUNHAP', 'MaPN', 'PHIEUNHAP', 7, k(0, 40), True)
    ngang('PHIEUNHAP', 'MaNCC', 'NHACUNGCAP', 1, k(0, 80))
    ngang('HANGCOSERI', 'MaPN', 'CHITIETPHIEUNHAP', 3, k(0, 120))
    ngang('HANGCOSERI', 'MaSeri', 'SERIMATHANG', 0, k(0, 160), True)
    doc('HANGCOSERI', 'CHITIETDONHANG')
    ngang('CHITIETDONHANG', 'MaSP', 'MATHANG', 6, k(0, 90))
    ngang('GIAODICHKHO', 'MaSP', 'MATHANG', 9, k(0, 190))
    # bảo hành
    doc('PHIEUBAOHANH', 'CHITIETDONHANG')
    ngang('PHIEUBAOHANH', 'MaSeri', 'HANGCOSERI', 6, k(0, 40))
    ngang('CHITIETTRA', 'MaSeri', 'HANGCOSERI', 5, k(0, 66))
    # đổi trả, hoàn tiền
    doc('LANNHANLAI', 'HOSODOITRA')
    doc('KHOANHOAN', 'HOSODOITRA')
    ngang('CHITIETTRA', 'MaHS', 'HOSODOITRA', 2, k(0, 40), True)
    ngang('KHOANHOAN', 'MaPhieuBH', 'PHIEUBAOHANH', 11, k(0, 140))
    # bán hàng: cột phải
    doc('TAIKHOAN', 'KHACHHANG')
    doc('DONHANG', 'MAGIAMGIA')
    doc('THANHTOAN', 'DONHANG')
    doc('LANGIAO', 'PHIEUGIAO', True)
    ngang('PHIEUGIAO', 'MaDH', 'DONHANG', 13, mr)
    ngang('DONHANG', 'MaKH', 'KHACHHANG', 2, mr + 26)
    ngang('CHITIETDONHANG', 'MaDH', 'DONHANG', 1, k(1, 50), True)
    ngang('HOSODOITRA', 'MaDH', 'DONHANG', 9, k(1, 170))
    ngang('KHOANHOAN', 'MaTT', 'THANHTOAN', 3, k(1, 60))
    # trục NHANVIEN
    nv = g('NHANVIEN')
    xt = k(1, 115)
    nhanh = []
    for n, dong in (('PHIEUNHAP', 'MaNV'), ('PHIEUBAOHANH', 'MaNV'), ('LANNHANLAI', 'MaNV'), ('HOSODOITRA', 'MaNV'), ('KHOANHOAN', 'MaNV'), ('GIAODICHKHO', 'MaNV')):
        nhanh.append((n, [(g(n).phai, g(n).y(dong)), (xt, g(n).y(dong))]))
    for n, dong in (('DONHANG', 'MaNV'), ('THANHTOAN', 'MaNV'), ('PHIEUGIAO', 'MaNV'), ('LANGIAO', 'MaNV')):
        nhanh.append((n, [(g(n).x, g(n).y(dong)), (xt, g(n).y(dong))]))
    for c, ds in nhanh:
        D.append((c, 'NHANVIEN', False, ds))
    ys = [p[-1][1] for _, p in nhanh] + [nv.y(4)]
    D.append(('*', '*', False, [(xt, min(ys)), (xt, max(ys))]))
    D.append(('*', 'NHANVIEN', False, [(xt, nv.y(4)), (nv.x, nv.y(4))]))
    doc('TAIKHOAN', 'NHANVIEN')
    doc('MAGIAMGIA', 'NHANVIEN')
    return D, [p[-1] for _, p in nhanh] + [(xt, nv.y(4))]


def net_dut(d, a, b, w):
    import math
    L = math.hypot(b[0] - a[0], b[1] - a[1])
    if L == 0:
        return
    ux, uy = (b[0] - a[0]) / L, (b[1] - a[1]) / L
    t = 0
    while t < L:
        e = min(t + 11, L)
        d.line([(a[0] + ux * t, a[1] + uy * t), (a[0] + ux * e, a[1] + uy * e)], fill=NET, width=w)
        t += 18


def dem_cat(D):
    doan = []
    for c, p, _, ds in D:
        for a, b in zip(ds, ds[1:]):
            doan.append((c, p, a, b))
    ds = []
    for i, (c1, p1, a, b) in enumerate(doan):
        for c2, p2, e, f in doan[i + 1:]:
            if (c1, p1) == (c2, p2) or 'NHANVIEN' == p1 == p2 or {p1, p2} <= {'*', 'NHANVIEN'}:
                continue
            ng = a[1] == b[1]
            if ng == (e[1] == f[1]):
                continue
            (h1, h2), (v1, v2) = ((a, b), (e, f)) if ng else ((e, f), (a, b))
            if min(h1[0], h2[0]) < v1[0] < max(h1[0], h2[0]) and min(v1[1], v2[1]) < h1[1] < max(v1[1], v2[1]):
                ds.append((c1, p1, c2, p2))
    return ds


def xuyen_bang(D, T):
    ds = []
    for c, p, _, dd in D:
        for a, b in zip(dd, dd[1:]):
            for n, t in T.items():
                x1, x2, y1, y2 = min(a[0], b[0]), max(a[0], b[0]), min(a[1], b[1]), max(a[1], b[1])
                if x1 < t.phai and x2 > t.x and y1 < t.day and y2 > t.t:
                    ds.append((c, p, n))
    return ds


def main():
    T, X, rong, W = bo_cuc()
    D, tram = tuyen(T, X, rong)
    tren, duoi = min(b.t for b in T.values()) - 40, max(b.day for b in T.values()) + 40
    H = int(duoi - tren)
    im = Image.new('RGB', (int(W), H), 'white')
    d = ImageDraw.Draw(im)
    for b in T.values():
        b.t -= tren
    D = [(c, p, n, [(x, y - tren) for x, y in ds]) for c, p, n, ds in D]
    for b in T.values():
        b.ve(d)
    for c, p, net, ds in D:
        for a, e in zip(ds, ds[1:]):
            (d.line([a, e], fill=NET, width=3) if net else net_dut(d, a, e, 3))
        ax, ay = ds[1][0] - ds[0][0], ds[1][1] - ds[0][1]
        L = abs(ax) + abs(ay) or 1
        ux, uy = ax / L, ay / L
        x, y = ds[0]
        if c != '*':
            for s in (-1, 0, 1):
                d.line([(x + ux * 14, y + uy * 14), (x - uy * 9 * s, y + ux * 9 * s)], fill=NET, width=2)
        bx, by = ds[-2][0] - ds[-1][0], ds[-2][1] - ds[-1][1]
        L = abs(bx) + abs(by) or 1
        ux, uy = bx / L, by / L
        x, y = ds[-1]
        if p != '*' and (p != 'NHANVIEN' or c == '*' or x != T['NHANVIEN'].x and T['NHANVIEN'].t <= y <= T['NHANVIEN'].day):      # nhánh dừng ở trục thì không có gạch đầu
            d.line([(x + ux * 9 - uy * 9, y + uy * 9 + ux * 9), (x + ux * 9 + uy * 9, y + uy * 9 - ux * 9)], fill=NET, width=3)
    for x, y in tram:
        d.ellipse([x - 6, y - tren - 6, x + 6, y - tren + 6], fill=NET)
    # chú thích ở góc trống
    x, y = X[0], T['CHITIETTRA'].day + 40
    f = font(CO)
    d.text((x, y), 'Chú thích', font=font(CO, True), fill='black')
    for k, (t, m) in enumerate([('PK: khóa chính', (192, 0, 0)), ('PFK: vừa khóa chính vừa khóa ngoại', (31, 78, 180)), ('FK: khóa ngoại', (46, 125, 50)),
                                ('Xám: cột cho phép rỗng', (128, 128, 128)), ('NN: NOT NULL', (0, 0, 0))]):
        d.text((x, y + 30 + 26 * k), t, font=f, fill=m)
    y2 = y + 30 + 26 * 5 + 8
    d.line([(x, y2 + 12), (x + 60, y2 + 12)], fill=NET, width=3)
    d.text((x + 70, y2), 'FK nằm trong khóa chính', font=f, fill='black')
    net_dut(d, (x, y2 + 40), (x + 60, y2 + 40), 3)
    d.text((x + 70, y2 + 28), 'FK còn lại', font=f, fill='black')
    d.ellipse([x + 24, y2 + 62, x + 36, y2 + 74], fill=NET)
    d.text((x + 70, y2 + 56), 'Trục gom FK tới NHANVIEN', font=f, fill='black')
    im.save(os.path.join(HINH, 'sodo_quanhe_tong.png'))

    # đủ mọi khóa ngoại: mỗi cặp (con, cha) có đường vẽ
    co = {(c, p) for c, p, _, _ in D}
    can = {(n, p) for n in R for _, p, _ in R[n]['fks']}
    thieu = can - co
    assert not thieu, thieu
    assert not co - can - {('*', 'NHANVIEN'), ('*', '*')}, co - can
    cat = dem_cat(D)
    print('khung', im.size, '| đường', len(D), '| cặp FK', len(can), '| giao cắt', len(cat), '| xuyên bảng', xuyen_bang(D, T))
    for x in cat:
        print('  ', x)


if __name__ == '__main__':
    main()
