#!/usr/bin/env python3
"""Vẽ ERD theo phong cách báo cáo mẫu, bố cục tự động: mọi đường nối là đoạn thẳng, không cắt nhau, không đi xuyên qua nút khác,
hai đường cùng xuất phát từ một nút không chồng lên nhau (góc tối thiểu). Mỗi hình đều là đồ thị phẳng nên luôn tồn tại cách vẽ như vậy.

Cách làm: dựng đồ thị (thực thể, mối kết hợp có thuộc tính, mối kết hợp khóa ngoại), lấy bố cục ban đầu từ spring layout,
rồi tìm kiếm cục bộ (ủ mô phỏng) để triệt tiêu giao cắt, chồng nút, đường xuyên nút và thu gọn khung hình. Kết quả được kiểm lại bằng
chính các đoạn thẳng sẽ vẽ.

Chạy:  python3 tools/ve_erd2.py [tên hình ...]   (mặc định vẽ tất cả; ví dụ: erd_nhom3)
"""
import math
import os
import random
import sys

import networkx as nx
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import erd
from ve_erd import (BLU, BLU_B, HINH, INK, ORG, ORG_B, Hinh, clip_ell, clip_rect, size_of)

MARGIN = 12          # khoảng hở tối thiểu giữa hai nút (px)
THETA_MIN = 16       # góc tối thiểu giữa hai đường cùng xuất phát từ một nút (độ)
SAMPLES = 28
VIS_MIN = 66         # đoạn nhìn thấy tối thiểu của một cạnh, đủ chỗ cho bản số
LAB_D = 24           # nhãn bản số cách biên nút (px)
LAB_W, LAB_H = 40, 17


# --------------------------------------------------------------------------------------------------
# Dựng đồ thị
# --------------------------------------------------------------------------------------------------
class Nut:
    def __init__(self, ten, loai, nhan, w, h):
        self.ten, self.loai, self.nhan, self.w, self.h = ten, loai, nhan, w, h


def dung_do_thi(keep, only_nv=False):
    mk = erd.mkh_card()
    nuts, canh = {}, []          # canh: (a, b, bản số ghi cạnh nút entity, nút mang bản số)
    for n in erd.ENTITIES:
        if n in keep:
            lab = erd.SHORT[n]
            nuts[n] = Nut(n, 'E', lab, size_of(lab, 20), 52)
    for n in erd.MKH:
        if n in keep and (not only_nv or any(e == 'NHANVIEN' for e, _ in mk[n])):
            lab = erd.SHORT[n].replace(' ', '\n', 1) if len(erd.SHORT[n]) > 14 else erd.SHORT[n]
            nuts[n] = Nut(n, 'M', lab, size_of(lab, 17) + 34, 66)
    for n in list(nuts):
        if nuts[n].loai == 'M':
            for e, card in mk[n]:
                if e in nuts:
                    canh.append((n, e, card, e))
    i = 0
    for verb, child, parent, bc, bp, cols in erd.relationships():
        if child in nuts and parent in nuts:
            if only_nv and parent != 'NHANVIEN':
                continue
            i += 1
            r = f'r{i}'
            nuts[r] = Nut(r, 'R', verb, size_of(verb, 16, False, 28), 50)
            if child == parent:       # quan hệ tự thân: một nút oval, hai đường tới hai điểm của cùng thực thể (vẽ ở hàm ve)
                canh.append((r, child, (bc, bp), child))
            else:
                canh.append((r, child, bc, child))
                canh.append((r, parent, bp, parent))
    # thực thể có rất nhiều đường nối (NHÂN VIÊN) vẽ to hơn để các đường và bản số tản ra quanh biên
    for n, u in nuts.items():
        d = sum(1 for c in canh if n in c[:2])
        if u.loai == 'E' and d > 6:
            u.w, u.h = max(u.w, 36 + 13 * d), max(u.h, 56 + 8 * d)
    # bỏ nút mối kết hợp lẻ loi (không còn đường nối)
    dung = {x for c in canh for x in c[:2]}
    nuts = {k: v for k, v in nuts.items() if k in dung}
    return nuts, canh


# --------------------------------------------------------------------------------------------------
# Hình học
# --------------------------------------------------------------------------------------------------
class BoCuc:
    def __init__(self, nuts, canh):
        self.ten = list(nuts)
        self.idx = {n: i for i, n in enumerate(self.ten)}
        self.nuts = nuts
        self.W = np.array([nuts[n].w for n in self.ten], float)
        self.H = np.array([nuts[n].h for n in self.ten], float)
        self.E = np.array([(self.idx[a], self.idx[b]) for a, b, _, _ in canh])
        self.deg = np.bincount(self.E.ravel(), minlength=len(self.ten))
        # cặp cạnh có chung nút -> kiểm góc; cặp không chung nút -> kiểm giao cắt
        ne = len(self.E)
        share = np.zeros((ne, ne), bool)
        tri = []
        for i in range(ne):
            for j in range(i + 1, ne):
                s = set(self.E[i]) & set(self.E[j])
                if s:
                    share[i, j] = share[j, i] = True
                    tri.append((i, j, next(iter(s))))
        self.share = share
        self.tri = np.array(tri)
        self.tri_i, self.tri_j, self.tri_n = (self.tri[:, 0], self.tri[:, 1], self.tri[:, 2]) if len(tri) else (None,) * 3
        self.not_inc = np.ones((ne, len(self.ten)), bool)
        for k, (a, b) in enumerate(self.E):
            self.not_inc[k, a] = self.not_inc[k, b] = False
        # chiều dài tự nhiên của từng cạnh
        w, h = self.W, self.H
        a, b = self.E[:, 0], self.E[:, 1]
        self.L0 = 0.5 * (w[a] + w[b]) * 0.45 + 0.5 * (h[a] + h[b]) * 0.6 + 58
        self.ts = np.linspace(0.04, 0.96, SAMPLES)
        self.isrect = np.array([nuts[n].loai == 'E' for n in self.ten])
        # nhãn bản số nằm cạnh nút `tai` của từng cạnh
        self.lab_n = np.array([self.idx[c[3]] for c in canh])
        self.lab_o = np.array([b if self.idx[c[3]] == a else a for (a, b), c in zip(self.E, canh)])

    def chi_phi(self, P, muc_tieu=1.0, chi_tiet=False):
        x, y = P[:, 0], P[:, 1]
        a, b = self.E[:, 0], self.E[:, 1]
        x1, y1, x2, y2 = x[a], y[a], x[b], y[b]
        # --- giao cắt giữa các cạnh không chung nút
        def orient(ax, ay, bx, by, cx, cy):
            return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)
        X1, Y1, X2, Y2 = x1[:, None], y1[:, None], x2[:, None], y2[:, None]
        Q1x, Q1y, Q2x, Q2y = x1[None, :], y1[None, :], x2[None, :], y2[None, :]
        o1 = orient(X1, Y1, X2, Y2, Q1x, Q1y)
        o2 = orient(X1, Y1, X2, Y2, Q2x, Q2y)
        o3 = orient(Q1x, Q1y, Q2x, Q2y, X1, Y1)
        o4 = orient(Q1x, Q1y, Q2x, Q2y, X2, Y2)
        cross = (o1 * o2 < 0) & (o3 * o4 < 0) & ~self.share
        n_cross = int(cross.sum() // 2)
        self.n_cross_last = n_cross
        # --- góc giữa hai cạnh chung nút
        pen_ang = 0.0
        n_ang = 0
        if self.tri_i is not None:
            ci, cj, cn = self.tri_i, self.tri_j, self.tri_n
            ei, ej = self.E[ci], self.E[cj]
            oi = np.where(ei[:, 0] == cn, ei[:, 1], ei[:, 0])
            oj = np.where(ej[:, 0] == cn, ej[:, 1], ej[:, 0])
            vx1, vy1 = x[oi] - x[cn], y[oi] - y[cn]
            vx2, vy2 = x[oj] - x[cn], y[oj] - y[cn]
            cosv = (vx1 * vx2 + vy1 * vy2) / (np.hypot(vx1, vy1) * np.hypot(vx2, vy2) + 1e-9)
            ang = np.degrees(np.arccos(np.clip(cosv, -1, 1)))
            thieu = np.maximum(0, THETA_MIN - ang)
            pen_ang = float((thieu ** 2).sum())
            n_ang = int((thieu > 0).sum())
        # --- chồng nút
        dx = (self.W[:, None] + self.W[None, :]) / 2 + MARGIN - np.abs(x[:, None] - x[None, :])
        dy = (self.H[:, None] + self.H[None, :]) / 2 + MARGIN - np.abs(y[:, None] - y[None, :])
        ov = (dx > 0) & (dy > 0)
        np.fill_diagonal(ov, False)
        pen_ov = float((np.minimum(dx, dy) * ov).sum() / 2)
        n_ov = int(ov.sum() // 2)
        # --- cạnh đi xuyên nút khác
        px = x1[:, None] + (x2 - x1)[:, None] * self.ts[None, :]
        py = y1[:, None] + (y2 - y1)[:, None] * self.ts[None, :]
        hw = (self.W / 2 + 6)[None, None, :]
        hh = (self.H / 2 + 6)[None, None, :]
        inside = (np.abs(px[:, :, None] - x[None, None, :]) < hw) & (np.abs(py[:, :, None] - y[None, None, :]) < hh)
        thru = inside.any(axis=1) & self.not_inc
        n_thru = int(thru.sum())
        # --- đoạn thấy được của cạnh và nhãn bản số
        ln = np.hypot(x2 - x1, y2 - y1) + 1e-9

        def ban_kinh(i, ux, uy):
            ax, ay = np.abs(ux) + 1e-9, np.abs(uy) + 1e-9
            hw_, hh_ = self.W[i] / 2, self.H[i] / 2
            rr = np.minimum(hw_ / ax, hh_ / ay)
            re = 1.0 / np.sqrt((ux / hw_) ** 2 + (uy / hh_) ** 2 + 1e-12)
            return np.where(self.isrect[i], rr, re)
        ux, uy = (x2 - x1) / ln, (y2 - y1) / ln
        ra, rb = ban_kinh(a, ux, uy), ban_kinh(b, -ux, -uy)
        vis = ln - ra - rb
        pen_vis = float((np.maximum(0, VIS_MIN - vis) ** 2).sum())
        ln_n, lo = self.lab_n, self.lab_o
        vx, vy = x[lo] - x[ln_n], y[lo] - y[ln_n]
        vl = np.hypot(vx, vy) + 1e-9
        vx, vy = vx / vl, vy / vl
        rn = ban_kinh(ln_n, vx, vy)
        lx, ly = x[ln_n] + vx * (rn + LAB_D), y[ln_n] + vy * (rn + LAB_D)
        ddx = LAB_W + 2 - np.abs(lx[:, None] - lx[None, :])
        ddy = LAB_H + 2 - np.abs(ly[:, None] - ly[None, :])
        lov = (ddx > 0) & (ddy > 0)
        np.fill_diagonal(lov, False)
        n_lab = int(lov.sum() // 2)
        ddx = LAB_W / 2 + self.W[None, :] / 2 - 2 - np.abs(lx[:, None] - x[None, :])
        ddy = LAB_H / 2 + self.H[None, :] / 2 - 2 - np.abs(ly[:, None] - y[None, :])
        lnode = (ddx > 0) & (ddy > 0)
        n_lnode = int(lnode.sum())
        lin = (np.abs(px[:, :, None] - lx[None, None, :]) < LAB_W / 2 + 3) & (np.abs(py[:, :, None] - ly[None, None, :]) < LAB_H / 2 + 3)
        ledge = lin.any(axis=1)
        ledge[np.arange(len(lx)), np.arange(len(lx))] = False
        n_ledge = int(ledge.sum())
        # --- độ dài cạnh và khung hình
        pen_len = float((((ln - self.L0) / 40.0) ** 2).sum())
        W_ = (x + self.W / 2).max() - (x - self.W / 2).min()
        H_ = (y + self.H / 2).max() - (y - self.H / 2).min()
        pen_box = (W_ * H_) / 4000.0 + 40.0 * abs(math.log((W_ / H_) / muc_tieu))
        c = (3000 * n_cross + 3000 * n_thru + 40 * pen_ang + 60 * pen_ov + 3000 * n_ov + pen_len * 6 + pen_box
             + 3 * pen_vis + 800 * n_lab + 800 * n_lnode + 800 * n_ledge)
        if chi_tiet == 'loi':
            bad = set()
            for i_, j_ in zip(*np.nonzero(np.triu(cross))):
                bad.update(self.E[i_]); bad.update(self.E[j_])
            for k_, n_ in zip(*np.nonzero(thru)):
                bad.update(self.E[k_]); bad.add(int(n_))
            for i_, j_ in zip(*np.nonzero(np.triu(ov))):
                bad.add(int(i_)); bad.add(int(j_))
            return c, sorted(bad)
        if chi_tiet:
            return c, dict(cross=n_cross, thru=n_thru, ang=n_ang, ov=n_ov, W=W_, H=H_, lab=n_lab + n_lnode + n_ledge)
        return c


def toi_uu(bc, muc_tieu, seed, so_buoc, P0=None, tmax=400.0, sg0=90.0, cung=False):
    rnd = random.Random(seed)
    G = nx.Graph()
    G.add_nodes_from(range(len(bc.ten)))
    G.add_edges_from(map(tuple, bc.E))
    if P0 is None:
        pos = nx.spring_layout(G, seed=seed, iterations=300)
        P = np.array([pos[i] for i in range(len(bc.ten))], float)
        dai = float(bc.L0.mean()) * (1.6 + 0.12 * math.sqrt(len(bc.ten)))
        P = P * dai * math.sqrt(len(bc.ten)) * 0.55
        P[:, 0] *= math.sqrt(muc_tieu)
        P[:, 1] /= math.sqrt(muc_tieu)
    else:
        P = P0.copy()
    nb = [list(G.neighbors(i)) for i in range(len(bc.ten))]
    cur = bc.chi_phi(P, muc_tieu)
    best, bestP = cur, P.copy()
    n = len(bc.ten)
    bad = []
    for it in range(so_buoc):
        t = 1.0 - it / so_buoc
        T = tmax * t ** 2 + 2.0
        if it % 150 == 0:
            bad = bc.chi_phi(P, muc_tieu, 'loi')[1]
        i = rnd.choice(bad) if bad and rnd.random() < 0.6 else rnd.randrange(n)
        sg = sg0 * t + 6.0
        Q = P.copy()
        r = rnd.random()
        if r < 0.35 and nb[i]:
            c = P[nb[i]].mean(axis=0)
            Q[i] = P[i] + (c - P[i]) * rnd.uniform(0.05, 0.5) + np.array([rnd.gauss(0, sg / 4), rnd.gauss(0, sg / 4)])
        elif r < 0.5:
            j = rnd.randrange(n)
            Q[i], Q[j] = P[j].copy(), P[i].copy()
        else:
            Q[i] = P[i] + np.array([rnd.gauss(0, sg), rnd.gauss(0, sg)])
        c2 = bc.chi_phi(Q, muc_tieu)
        if cung and bc.n_cross_last > 0:
            continue
        if c2 < cur or rnd.random() < math.exp(-(c2 - cur) / T):
            P, cur = Q, c2
            if cur < best:
                best, bestP = cur, P.copy()
    return best, bestP


def khoi_tao_phang(bc, don_vi=26.0, muc_tieu=1.0):
    """Bố cục ban đầu không giao cắt: vẽ đường thẳng trên lưới theo phép nhúng phẳng (Chrobak-Payne của networkx)."""
    G = nx.Graph()
    G.add_nodes_from(range(len(bc.ten)))
    G.add_edges_from(map(tuple, bc.E))
    ok, emb = nx.check_planarity(G)
    assert ok
    pos = nx.combinatorial_embedding_to_pos(emb)
    P = np.array([pos[i] for i in range(len(bc.ten))], float) * don_vi
    return P


def lam_sach(bc, P, muc_tieu, so_buoc=6000, seed=1, cung=False):
    """Giai đoạn cuối: chỉ nhận bước làm chi phí giảm (không nhiệt)."""
    rnd = random.Random(seed)
    cur = bc.chi_phi(P, muc_tieu)
    n = len(bc.ten)
    for it in range(so_buoc):
        i = rnd.randrange(n)
        sg = 25.0 * (1 - it / so_buoc) + 3.0
        Q = P.copy()
        Q[i] = P[i] + np.array([rnd.gauss(0, sg), rnd.gauss(0, sg)])
        c2 = bc.chi_phi(Q, muc_tieu)
        if cung and bc.n_cross_last > 0:
            continue
        if c2 < cur:
            P, cur = Q, c2
    return cur, P


# --------------------------------------------------------------------------------------------------
# Vẽ
# --------------------------------------------------------------------------------------------------
def diem_noi(nut, cx, cy, tx, ty):
    if nut.loai == 'E':
        return clip_rect(cx, cy, nut.w, nut.h, tx, ty)
    return clip_ell(cx, cy, nut.w, nut.h, tx, ty)


def ve(nuts, canh, P, ten):
    ids = list(nuts)
    xs = P[:, 0] - min(P[:, 0] - np.array([nuts[n].w for n in ids]) / 2) + 60
    ys = P[:, 1] - min(P[:, 1] - np.array([nuts[n].h for n in ids]) / 2) + 60
    pos = {n: (xs[i], ys[i]) for i, n in enumerate(ids)}
    W = int(max(xs + np.array([nuts[n].w for n in ids]) / 2) + 60)
    H = int(max(ys + np.array([nuts[n].h for n in ids]) / 2) + 60)
    g = Hinh(W, H)
    nhan, rieng = [], []
    for a, b, card, tai in canh:
        (ax, ay), (bx, by) = pos[a], pos[b]
        if isinstance(card, tuple):
            u = nuts[b]
            ngang = abs(ay - by) >= abs(ax - bx)
            for sgn, c in zip((-1, 1), card):
                if ngang:
                    tren = ay < by
                    pt = (bx + sgn * u.w / 3, by + (-u.h / 2 if tren else u.h / 2))
                    vt = (pt[0] + sgn * 24, pt[1] + (-16 if tren else 16))
                else:
                    trai = ax < bx
                    pt = (bx + (-u.w / 2 if trai else u.w / 2), by + sgn * u.h / 4)
                    vt = (pt[0] + (-30 if trai else 30), pt[1] + sgn * 12)
                po = diem_noi(nuts[a], ax, ay, pt[0], pt[1])
                g.line([po, pt])
                rieng.append((vt, c))
            continue
        pa = diem_noi(nuts[a], ax, ay, bx, by)
        pb = diem_noi(nuts[b], bx, by, ax, ay)
        g.line([pa, pb])
        if tai == a:
            nhan.append((pa, pb, card))
        else:
            nhan.append((pb, pa, card))
    for n in ids:
        x, y = pos[n]
        u = nuts[n]
        if u.loai == 'R':
            g.ell(x, y, u.w, u.h, u.nhan, ORG, ORG_B, False, 16)
        elif u.loai == 'M':
            g.ell(x, y, u.w, u.h, u.nhan, BLU, BLU_B, True, 17)
        else:
            g.rect(x, y, u.w, u.h, u.nhan)
    for a, b, card in nhan:
        dx, dy = b[0] - a[0], b[1] - a[1]
        ln = math.hypot(dx, dy) or 1
        g.text(a[0] + dx / ln * 24, a[1] + dy / ln * 24 - (8 if abs(dx) > abs(dy) else 0), card, 15, True, (20, 20, 20), halo=True)
    for (x, y), c in rieng:
        g.text(x, y, c, 15, True, (20, 20, 20), halo=True)
    g.save(os.path.join(HINH, ten + '.png'), box=(0, 0, W, H))
    return pos


def kiem_tra(nuts, canh, pos):
    """Kiểm bằng chính các đoạn thẳng sẽ vẽ (sau khi cắt theo biên nút): số giao cắt, đường xuyên nút, góc nhỏ nhất."""
    seg = []
    for a, b, cd, _ in canh:
        if isinstance(cd, tuple):
            continue
        (ax, ay), (bx, by) = pos[a], pos[b]
        seg.append((a, b, diem_noi(nuts[a], ax, ay, bx, by), diem_noi(nuts[b], bx, by, ax, ay)))

    def ccw(p, q, r):
        return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
    giao = 0
    for i in range(len(seg)):
        for j in range(i + 1, len(seg)):
            if {seg[i][0], seg[i][1]} & {seg[j][0], seg[j][1]}:
                continue
            p1, p2, q1, q2 = seg[i][2], seg[i][3], seg[j][2], seg[j][3]
            if ccw(p1, p2, q1) * ccw(p1, p2, q2) < 0 and ccw(q1, q2, p1) * ccw(q1, q2, p2) < 0:
                giao += 1
    xuyen = 0
    for a, b, p1, p2 in seg:
        for n, (x, y) in pos.items():
            if n in (a, b):
                continue
            u = nuts[n]
            for t in np.linspace(0.02, 0.98, 60):
                px, py = p1[0] + (p2[0] - p1[0]) * t, p1[1] + (p2[1] - p1[1]) * t
                if abs(px - x) < u.w / 2 and abs(py - y) < u.h / 2:
                    xuyen += 1
                    break
    goc = 180.0
    for n in pos:
        huong = []
        for a, b, cd, _ in canh:
            if isinstance(cd, tuple):
                continue
            if n in (a, b):
                o = b if a == n else a
                huong.append(math.atan2(pos[o][1] - pos[n][1], pos[o][0] - pos[n][0]))
        for i in range(len(huong)):
            for j in range(i + 1, len(huong)):
                d = abs(math.degrees(huong[i] - huong[j])) % 360
                goc = min(goc, min(d, 360 - d))
    return giao, xuyen, goc


CACHE = os.path.join(HERE, 'bo_cuc_erd2.json')


def doc_cache():
    try:
        import json
        return json.load(open(CACHE, encoding='utf-8'))
    except (OSError, ValueError):
        return {}


def ghi_cache(ten, bc, P):
    import json
    c = doc_cache()
    c[ten] = {n: [round(float(P[i, 0]), 1), round(float(P[i, 1]), 1)] for i, n in enumerate(bc.ten)}
    json.dump(c, open(CACHE, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)


def sach(d, lon=False):
    return d['cross'] == 0 and d['thru'] == 0 and d['ov'] == 0 and d['lab'] <= (3 if lon else 0)   # hình lớn: cho phép vài nhãn sát nhau


def lam_hinh(ten, keep, only_nv, muc_tieu, lan=3, so_buoc=None, vong=8, moi=False):
    nuts, canh = dung_do_thi(keep, only_nv)
    G = nx.Graph([(a, b) for a, b, _, _ in canh])
    assert nx.check_planarity(G)[0], f'{ten}: đồ thị không phẳng'
    bc = BoCuc(nuts, canh)
    n = len(bc.ten)
    so_buoc = so_buoc or int(1500 + 700 * n) * (2 if n > 40 else 1)
    P = None
    c0 = doc_cache().get(ten)
    if c0 and not moi and set(c0) == set(bc.ten):
        P = np.array([c0[x] for x in bc.ten], float)
    cung = n > 40          # đồ thị lớn: bắt đầu từ bố cục phẳng và không bao giờ nhận bước làm phát sinh giao cắt
    if P is None and cung:
        P0 = khoi_tao_phang(bc)
        _, P = toi_uu(bc, muc_tieu, 100, so_buoc, P0=P0, tmax=250.0, sg0=70.0, cung=True)
    elif P is None:
        ket = None
        for s in range(lan):
            c, Q = toi_uu(bc, muc_tieu, 100 + s, so_buoc)
            if ket is None or c < ket[0]:
                ket = (c, Q)
        P = ket[1]
    c, d = bc.chi_phi(P, muc_tieu, True)
    r = 0
    while not sach(d, n > 40) and r < vong:       # tinh chỉnh tiếp từ bố cục tốt nhất cho tới khi sạch
        r += 1
        c, Q = toi_uu(bc, muc_tieu, 500 + r, so_buoc, P0=P, tmax=150.0 / r, sg0=60.0, cung=cung)
        c2, Q = lam_sach(bc, Q, muc_tieu, 3000 + 30 * n, seed=r, cung=cung)
        if c2 < c:
            P = Q
        c, d = bc.chi_phi(P, muc_tieu, True)
    c, P = lam_sach(bc, P, muc_tieu, 3000 + 30 * n, seed=99) if sach(d, n > 40) else (c, P)
    _, d = bc.chi_phi(P, muc_tieu, True)
    pos = ve(nuts, canh, P, ten)
    giao, xuyen, goc = kiem_tra(nuts, canh, pos)
    print(f'{ten}: {n} nút, {len(canh)} cạnh | giao cắt {giao}, xuyên nút {xuyen}, góc nhỏ nhất {goc:.0f}°, lỗi nhãn {d["lab"]} | khung {int(d["W"])}x{int(d["H"])}')
    if giao == 0 and xuyen == 0:
        ghi_cache(ten, bc, P)
    return giao, xuyen, goc


def main(chon=None):
    tat_ca = set(erd.ENTITIES) | set(erd.MKH)
    viec = [('erd_tong_quat', tat_ca, False, 0.72)]
    for k, (ten, ents) in erd.GROUPS.items():
        keep = set(ents) | {m for m in erd.MKH if m in ents or all(e in ents for e, _ in erd.mkh_card()[m])}
        viec.append((f'erd_nhom{k}', keep, k == '8', 0.8 if k != '8' else 0.8))
    for ten, keep, only_nv, mt in viec:
        if chon and ten not in chon:
            continue
        lam_hinh(ten, keep, only_nv, mt, moi=bool(os.environ.get('ERD_MOI')))


if __name__ == '__main__':
    main(set(sys.argv[1:]) or None)
