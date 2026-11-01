#!/usr/bin/env python3
"""Sơ đồ quan hệ tổng quát 26 bảng trên một trang A4 ngang, kiểu Toad Data Modeler.

Graphviz đi đường cho 26 bảng rất rối, nên ở đây đặt bảng cố định và khai báo tay từng đường vuông góc.
12 bảng có khóa ngoại tới NHANVIEN gom vào một trục ngang; bảng có hai khóa ngoại tới NHANVIEN vẽ chung một nhánh.
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
TREN = [['LOAIHANG', 'THUONGHIEU', 'DINHNGHIATHONGSO', 'GIATRITHONGSO'], ['MATHANG', 'ANHMATHANG', 'GIAODICHKHO'],
        ['SERIMATHANG', 'CHITIETPHIEUNHAP', 'PHIEUNHAP'], ['HANGCOSERI', 'CHITIETTRA', 'PHIEUBAOHANH'],
        ['CHITIETDONHANG', 'PHIEUGIAO'], ['LANGIAO'], []]
DUOI = [[], ['NHACUNGCAP'], ['LANNHANLAI'], ['HOSODOITRA', 'KHOANHOAN'], ['DONHANG'], ['MAGIAMGIA', 'THANHTOAN'], ['TAIKHOAN', 'KHACHHANG']]
KHE = [120, 120, 140, 160, 120, 110]        # bề rộng khe giữa các cột
GIA, TRUC, GIUA = 26, 42, 26                # cách giữa hai bảng trong cột, khoảng bảng tới trục, cách NHANVIEN


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
    nv = T['NHANVIEN']
    rong = [max([T[n].w for n in a + b] + ([nv.w] if i == 5 else [])) for i, (a, b) in enumerate(zip(TREN, DUOI))]
    X, x = [], 40
    for i, w in enumerate(rong):
        X.append(x)
        x += w + (KHE[i] if i < len(KHE) else 0)
    W = x + 40
    for i, (tr, du) in enumerate(zip(TREN, DUOI)):
        y = -(nv.h / 2 + GIUA) if i == 5 else -TRUC
        for n in reversed(tr):
            y -= T[n].h
            T[n].t, T[n].x = y, X[i] + (rong[i] - T[n].w) / 2
            y -= GIA
        y = nv.h / 2 + GIUA if i == 5 else TRUC
        for n in du:
            T[n].t, T[n].x = y, X[i] + (rong[i] - T[n].w) / 2
            y += T[n].h + GIA
    nv.t, nv.x = -nv.h / 2, X[5] + (rong[5] - nv.w) / 2
    return T, X, rong, W


def tuyen(T, X, rong):
    """(bảng con, bảng cha, liền/đứt, điểm...): điểm đầu ở bảng con, điểm cuối ở bảng cha."""
    k = lambda i, t: X[i] + rong[i] + t          # vị trí dọc trong khe sau cột i
    g = lambda n: T[n]
    D = []

    def ngang(c, c_dong, p, p_dong, xt=None, net=False):
        """ra sườn bảng con, đi dọc ở xt, vào sườn bảng cha; không có xt thì đi thẳng."""
        a, b = g(c), g(p)
        ya, yb = a.y(c_dong), b.y(p_dong) if xt is not None else a.y(c_dong)
        if xt is None:
            xa, xb = (a.phai, b.x) if b.tx > a.tx else (a.x, b.phai)
        else:
            xa, xb = a.phai if xt >= a.phai else a.x, b.phai if xt >= b.phai else b.x
        D.append((c, p, net, [(xa, ya), (xb, ya)] if xt is None else [(xa, ya), (xt, ya), (xt, yb), (xb, yb)]))

    def doc(c, p, net=False, x=None):
        a, b = g(c), g(p)
        x = a.tx if x is None else x
        D.append((c, p, net, [(x, a.t), (x, b.day)] if b.t < a.t else [(x, a.day), (x, b.t)]))

    # hàng hóa
    gtren = min(b.t for b in T.values()) - 26
    x0 = g('LOAIHANG').x - 26
    D.append(('DINHNGHIATHONGSO', 'LOAIHANG', False, [(g('DINHNGHIATHONGSO').x, g('DINHNGHIATHONGSO').y(1)), (x0, g('DINHNGHIATHONGSO').y(1)), (x0, g('LOAIHANG').y(0)), (g('LOAIHANG').x, g('LOAIHANG').y(0))]))
    lh = g('LOAIHANG')
    D.append(('LOAIHANG', 'LOAIHANG', False, [(lh.x + 40, lh.t), (lh.x + 40, lh.t - 20), (lh.x + 110, lh.t - 20), (lh.x + 110, lh.t)]))
    doc('GIATRITHONGSO', 'DINHNGHIATHONGSO', True)
    ngang('MATHANG', 'MaLoai', 'LOAIHANG', 0, k(0, 86))
    ngang('MATHANG', 'MaTH', 'THUONGHIEU', 0, k(0, 56))
    mh = g('MATHANG')
    yg = (mh.day + g('ANHMATHANG').t) / 2
    D.append(('GIATRITHONGSO', 'MATHANG', True, [(g('GIATRITHONGSO').phai, g('GIATRITHONGSO').y(0)), (k(0, 100), g('GIATRITHONGSO').y(0)), (k(0, 100), yg), (mh.x + 30, yg), (mh.x + 30, mh.day)]))
    doc('ANHMATHANG', 'MATHANG')
    ngang('SERIMATHANG', 'MaSP', 'MATHANG', 2, k(1, 90))
    ngang('CHITIETPHIEUNHAP', 'MaSP', 'MATHANG', 5, k(1, 60))
    ngang('GIAODICHKHO', 'MaSP', 'MATHANG', 8, k(1, 30))
    ct = g('CHITIETDONHANG')
    D.append(('CHITIETDONHANG', 'MATHANG', False, [(ct.tx, ct.t), (ct.tx, gtren), (mh.phai - 30, gtren), (mh.phai - 30, mh.t)]))
    # nhập, seri
    doc('CHITIETPHIEUNHAP', 'PHIEUNHAP', True)
    ngang('PHIEUNHAP', 'MaNCC', 'NHACUNGCAP', 0, k(1, 100))
    ngang('HANGCOSERI', 'MaSeri', 'SERIMATHANG', 0, k(2, 66), True)
    ngang('HANGCOSERI', 'MaPN', 'CHITIETPHIEUNHAP', 0, k(2, 100))
    doc('CHITIETTRA', 'HANGCOSERI')
    # bảo hành, đơn
    ngang('PHIEUBAOHANH', 'MaSeri', 'HANGCOSERI', 5, k(3, 28))
    ngang('HANGCOSERI', 'MaDH', 'CHITIETDONHANG', 0, k(3, 58))
    ngang('PHIEUBAOHANH', 'MaDH', 'CHITIETDONHANG', 1, k(3, 88))
    ngang('CHITIETDONHANG', 'MaDH', 'DONHANG', 0, k(3, 122), True)
    # đổi trả, hoàn tiền
    ngang('CHITIETTRA', 4, 'HOSODOITRA', 1, k(2, 60), True)
    ngang('LANNHANLAI', 4, 'HOSODOITRA', None)
    doc('KHOANHOAN', 'HOSODOITRA')
    ngang('HOSODOITRA', 3, 'DONHANG', None)
    ngang('KHOANHOAN', 'MaPhieuBH', 'PHIEUBAOHANH', 11, k(3, 58))
    # thanh toán, giao hàng, khách
    kh, tt = g('KHOANHOAN'), g('THANHTOAN')
    D.append(('KHOANHOAN', 'THANHTOAN', False, [(kh.phai, kh.y(9)), (tt.x, kh.y(9))]))
    ngang('THANHTOAN', 0, 'DONHANG', 14, k(4, 34))
    pg, dh = g('PHIEUGIAO'), g('DONHANG')
    D.append(('PHIEUGIAO', 'DONHANG', False, [(pg.tx + 44, pg.day), (pg.tx + 44, dh.t)]))
    ngang('LANGIAO', 'MaGiao', 'PHIEUGIAO', 0, k(4, 70), True)
    mg = g('MAGIAMGIA')
    D.append(('DONHANG', 'MAGIAMGIA', False, [(dh.phai, dh.y('MaMG')), (mg.x, dh.y('MaMG'))]))
    khach = g('KHACHHANG')
    ym = (mg.day + tt.t) / 2
    D.append(('DONHANG', 'KHACHHANG', False, [(dh.phai, dh.y(13)), (k(4, 70), dh.y(13)), (k(4, 70), ym), (k(5, 60), ym), (k(5, 60), khach.y(0)), (khach.x, khach.y(0))]))
    doc('TAIKHOAN', 'KHACHHANG')
    # các đường tới NHANVIEN
    nv = g('NHANVIEN')
    nhanh = [('GIAODICHKHO', [(g('GIAODICHKHO').tx, g('GIAODICHKHO').day), (g('GIAODICHKHO').tx, 0)]),
             ('PHIEUNHAP', [(g('PHIEUNHAP').phai, g('PHIEUNHAP').y('MaNV')), (k(2, 24), g('PHIEUNHAP').y('MaNV')), (k(2, 24), 0)]),
             ('PHIEUBAOHANH', [(g('PHIEUBAOHANH').tx, g('PHIEUBAOHANH').day), (g('PHIEUBAOHANH').tx, 0)]),
             ('PHIEUGIAO', [(pg.tx - 44, pg.day), (pg.tx - 44, 0)]),
             ('LANNHANLAI', [(g('LANNHANLAI').tx, g('LANNHANLAI').t), (g('LANNHANLAI').tx, 0)]),
             ('HOSODOITRA', [(g('HOSODOITRA').tx, g('HOSODOITRA').t), (g('HOSODOITRA').tx, 0)]),
             ('KHOANHOAN', [(kh.phai, kh.y(4)), (k(3, 28), kh.y(4)), (k(3, 28), 0)]),
             ('DONHANG', [(dh.tx - 44, dh.t), (dh.tx - 44, 0)])]
    for c, ds in nhanh:
        D.append((c, 'NHANVIEN', False, ds))
    trai = min(p[-1][0] for _, p in nhanh)
    D.append(('*', 'NHANVIEN', False, [(trai, 0), (nv.x, 0)]))
    D.append(('LANGIAO', 'NHANVIEN', False, [(g('LANGIAO').tx, g('LANGIAO').day), (g('LANGIAO').tx, nv.t)]))
    D.append(('MAGIAMGIA', 'NHANVIEN', False, [(mg.tx, mg.t), (mg.tx, nv.day)]))
    tk = g('TAIKHOAN')
    D.append(('TAIKHOAN', 'NHANVIEN', False, [(tk.x, nv.y(7)), (nv.phai, nv.y(7))]))
    D.append(('THANHTOAN', 'NHANVIEN', False, [(tt.phai, tt.y('MaNV')), (k(5, 30), tt.y('MaNV')), (k(5, 30), nv.y(8)), (nv.phai, nv.y(8))]))
    return D, [p[-1] for _, p in nhanh]


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
            if (c1, p1) == (c2, p2) or 'NHANVIEN' == p1 == p2:
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
    tren, duoi = min(b.t for b in T.values()) - 60, max(b.day for b in T.values()) + 40
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
        if p != 'NHANVIEN' or c == '*' or y != -tren:      # nhánh dừng ở trục thì không có gạch đầu
            d.line([(x + ux * 9 - uy * 9, y + uy * 9 + ux * 9), (x + ux * 9 + uy * 9, y + uy * 9 - ux * 9)], fill=NET, width=3)
    for x, y in tram:
        d.ellipse([x - 6, y - tren - 6, x + 6, y - tren + 6], fill=NET)
    # chú thích ở góc trống
    x, y = 60, T['LANNHANLAI'].t + 10
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
    assert not co - can - {('*', 'NHANVIEN')}, co - can
    cat = dem_cat(D)
    print('khung', im.size, '| đường', len(D), '| cặp FK', len(can), '| giao cắt', len(cat), '| xuyên bảng', xuyen_bang(D, T))
    for x in cat:
        print('  ', x)


if __name__ == '__main__':
    main()
