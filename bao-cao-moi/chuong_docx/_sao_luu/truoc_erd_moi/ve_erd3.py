#!/usr/bin/env python3
"""Vẽ ERD theo kiểu báo cáo mẫu: các nút xếp trên lưới đều, mỗi mối kết hợp là một oval nằm đúng giữa đoạn thẳng nối hai thực thể,
đường nối ngang hoặc dọc càng nhiều càng tốt, bản số đặt trên đường sát thực thể (nền trắng), không giao cắt, không xuyên nút.

Nút (thực thể, mối kết hợp có thuộc tính) đặt vào ô lưới; oval mối kết hợp khóa ngoại không phải nút của bố cục mà là điểm giữa cạnh.
Bố cục ban đầu là bản vẽ phẳng trên lưới nguyên (Chrobak-Payne); sau đó ủ mô phỏng, chỉ nhận bước không làm phát sinh giao cắt.

Chạy:  python3 tools/ve_erd3.py [tên hình ...]      (ERD_MOI=1 để bỏ bố cục đã lưu)
"""
import json
import math
import os
import random
import sys

import networkx as nx
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import erd
from ve_erd import BLU, BLU_B, HINH, ORG, ORG_B, Hinh, clip_ell, clip_rect, size_of

PX, PY = 330.0, 118.0        # bước lưới (px)
SAMPLES = 24
LAB_OFF = 30                 # bản số cách biên thực thể (px)
GAP = 62                     # chỗ trống mỗi bên oval để đặt bản số
THETA = 18                   # góc tối thiểu giữa hai đường cùng nút (độ)
CACHE = os.path.join(HERE, 'bo_cuc_erd3.json')

# những mối kết hợp với NHÂN VIÊN giữ trong hình tổng quát (phần còn lại vẽ ở hình "trách nhiệm")
NV_GIU = {'LANGIAO', 'TAIKHOAN', 'DONHANG', 'PHIEUGIAO'}


class Nut:
    def __init__(self, ten, loai, nhan, w, h):
        self.ten, self.loai, self.nhan, self.w, self.h = ten, loai, nhan, w, h


def dung(keep, nv_chon=False, chi_nv=False):
    """Trả về (nút, cạnh bố cục, mối kết hợp). cạnh: dict(u, v, ovals=[(verb, the_u, the_v)], oval|None)."""
    mk = erd.mkh_card()
    nuts = {}
    for n in erd.ENTITIES:
        if n in keep:
            lab = erd.SHORT[n]
            nuts[n] = Nut(n, 'E', lab, max(size_of(lab, 15) + 26, 96), 40)
    for n in erd.MKH:
        if n in keep and (not chi_nv or any(e == 'NHANVIEN' for e, _ in mk[n])):
            lab = erd.SHORT[n].replace(' ', '\n', 1) if len(erd.SHORT[n]) > 14 else erd.SHORT[n]
            nuts[n] = Nut(n, 'M', lab, size_of(lab, 13) + 30, 54)
    canh = {}                                   # (u,v) đã sắp thứ tự -> dict
    def them(u, v, **kw):
        k = tuple(sorted((u, v)))
        c = canh.setdefault(k, dict(u=k[0], v=k[1], ovals=[], mkh=[]))
        for key, val in kw.items():
            c[key].append(val)
    for n in list(nuts):
        if nuts[n].loai == 'M':
            for e, card in mk[n]:
                if e in nuts and (not nv_chon or e != 'NHANVIEN' or n in NV_GIU):
                    them(n, e, mkh=(n, e, card))
    for verb, child, parent, bc, bp, cols in erd.relationships():
        if child not in nuts or parent not in nuts:
            continue
        if chi_nv and parent != 'NHANVIEN':
            continue
        if nv_chon and parent == 'NHANVIEN' and child not in NV_GIU:
            continue
        if child == parent:                     # quan hệ tự thân: oval là nút riêng nối với thực thể bằng hai đường
            r = f'tt_{child}_{verb}'
            nuts[r] = Nut(r, 'S', verb, size_of(verb, 13, False, 26), 36)
            them(r, child, mkh=(r, child, (bc, bp)))
            continue
        them(child, parent, ovals=(verb, child, parent, bc, bp))
    # nút bị cô lập (mất hết cạnh) thì bỏ
    dung_ = {x for c in canh.values() for x in (c['u'], c['v'])}
    nuts = {k: v for k, v in nuts.items() if k in dung_}
    for c in canh.values():
        if len(c['ovals']) >= 2:
            for t in (c['u'], c['v']):
                if nuts[t].loai == 'E':
                    nuts[t].w, nuts[t].h = max(nuts[t].w, 150), max(nuts[t].h, 20 + 22 * len(c['ovals']) + 14 * (len(c['ovals']) - 1))
    # thực thể có rất nhiều đường nối vẽ to hơn
    for n, u in nuts.items():
        d = sum(1 for c in canh.values() if n in (c['u'], c['v']) for _ in range(max(1, len(c['ovals']) + len(c['mkh']))))
        if u.loai == 'E' and d > 6:
            u.w, u.h = max(u.w, 30 + 12 * d), max(u.h, 40 + 7 * d)
    return nuts, canh


class BoCuc:
    def __init__(self, nuts, canh):
        self.ten = list(nuts)
        self.idx = {n: i for i, n in enumerate(self.ten)}
        self.nuts, self.canh = nuts, list(canh.values())
        n, ne = len(self.ten), len(self.canh)
        self.W = np.array([nuts[t].w for t in self.ten], float)
        self.H = np.array([nuts[t].h for t in self.ten], float)
        self.E = np.array([(self.idx[c['u']], self.idx[c['v']]) for c in self.canh])
        self.isrect = np.array([nuts[t].loai == 'E' for t in self.ten])
        # kích thước oval ở giữa mỗi cạnh (0 nếu không có oval); nhiều oval song song -> dùng oval rộng nhất, cao theo số oval
        self.OW = np.zeros(ne)
        self.OH = np.zeros(ne)
        for k, c in enumerate(self.canh):
            if c['ovals']:
                m_ = len(c['ovals'])
                self.OW[k] = max(size_of(o[0], 13, False, 26) for o in c['ovals']) * (m_ if m_ > 1 else 1) + 14 * (m_ - 1)
                self.OH[k] = 36 * m_ + 10 * (m_ - 1)
        self.share = np.zeros((ne, ne), bool)
        tri = []
        for i in range(ne):
            for j in range(i + 1, ne):
                s = set(self.E[i]) & set(self.E[j])
                if s:
                    self.share[i, j] = self.share[j, i] = True
                    tri.append((i, j, next(iter(s))))
        self.tri = np.array(tri) if tri else None
        self.not_inc = np.ones((ne, n), bool)
        for k, (a, b) in enumerate(self.E):
            self.not_inc[k, a] = self.not_inc[k, b] = False
        self.ts = np.linspace(0.05, 0.95, SAMPLES)
        self.has_oval = self.OW > 0

    # ---- hình học
    def _r(self, i, ux, uy):
        ax, ay = np.abs(ux) + 1e-9, np.abs(uy) + 1e-9
        hw, hh = self.W[i] / 2, self.H[i] / 2
        rr = np.minimum(hw / ax, hh / ay)
        re = 1.0 / np.sqrt((ux / hw) ** 2 + (uy / hh) ** 2 + 1e-12)
        return np.where(self.isrect[i], rr, re)

    def chi_phi(self, P, muc_tieu, chi_tiet=False):
        x, y = P[:, 0], P[:, 1]
        a, b = self.E[:, 0], self.E[:, 1]
        x1, y1, x2, y2 = x[a], y[a], x[b], y[b]
        orient = lambda ax, ay, bx, by, cx, cy: (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)
        X1, Y1, X2, Y2 = x1[:, None], y1[:, None], x2[:, None], y2[:, None]
        Q1x, Q1y, Q2x, Q2y = x1[None, :], y1[None, :], x2[None, :], y2[None, :]
        cross = ((orient(X1, Y1, X2, Y2, Q1x, Q1y) * orient(X1, Y1, X2, Y2, Q2x, Q2y) < 0) &
                 (orient(Q1x, Q1y, Q2x, Q2y, X1, Y1) * orient(Q1x, Q1y, Q2x, Q2y, X2, Y2) < 0) & ~self.share)
        n_cross = int(cross.sum() // 2)
        self.n_cross_last = n_cross
        ln = np.hypot(x2 - x1, y2 - y1) + 1e-9
        ux, uy = (x2 - x1) / ln, (y2 - y1) / ln
        # đoạn nhìn thấy và chỗ cần cho oval + bản số
        ra, rb = self._r(a, ux, uy), self._r(b, -ux, -uy)
        vis = ln - ra - rb
        ov_half = np.where(self.has_oval, 1.0 / np.sqrt((ux / (self.OW / 2 + 1e-9)) ** 2 + (uy / (self.OH / 2 + 1e-9)) ** 2 + 1e-12), 0.0)
        need = np.where(self.has_oval, 2 * ov_half + 2 * GAP, 2 * GAP * 0.6)
        pen_vis = float((np.maximum(0, need - vis) ** 2).sum())
        # góc giữa hai cạnh cùng nút
        pen_ang = 0.0
        if self.tri is not None:
            ci, cj, cn = self.tri[:, 0], self.tri[:, 1], self.tri[:, 2]
            ei, ej = self.E[ci], self.E[cj]
            oi = np.where(ei[:, 0] == cn, ei[:, 1], ei[:, 0])
            oj = np.where(ej[:, 0] == cn, ej[:, 1], ej[:, 0])
            v1x, v1y, v2x, v2y = x[oi] - x[cn], y[oi] - y[cn], x[oj] - x[cn], y[oj] - y[cn]
            cs = (v1x * v2x + v1y * v2y) / (np.hypot(v1x, v1y) * np.hypot(v2x, v2y) + 1e-9)
            ang = np.degrees(np.arccos(np.clip(cs, -1, 1)))
            pen_ang = float((np.maximum(0, THETA - ang) ** 2).sum())
        # chồng nút
        dx = (self.W[:, None] + self.W[None, :]) / 2 + 14 - np.abs(x[:, None] - x[None, :])
        dy = (self.H[:, None] + self.H[None, :]) / 2 + 14 - np.abs(y[:, None] - y[None, :])
        ov = (dx > 0) & (dy > 0)
        np.fill_diagonal(ov, False)
        n_ov = int(ov.sum() // 2)
        # cạnh đi xuyên nút khác
        px = x1[:, None] + (x2 - x1)[:, None] * self.ts[None, :]
        py = y1[:, None] + (y2 - y1)[:, None] * self.ts[None, :]
        inside = ((np.abs(px[:, :, None] - x[None, None, :]) < (self.W / 2 + 6)[None, None, :]) &
                  (np.abs(py[:, :, None] - y[None, None, :]) < (self.H / 2 + 6)[None, None, :]))
        n_thru = int((inside.any(axis=1) & self.not_inc).sum())
        # oval giữa cạnh: không chồng nút, không chồng oval khác, không bị cạnh khác đi qua
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        ok = np.nonzero(self.has_oval)[0]
        n_ovl = 0
        if len(ok):
            ow, oh = self.OW[ok], self.OH[ok]
            ddx = (ow[:, None] + self.W[None, :]) / 2 + 4 - np.abs(mx[ok][:, None] - x[None, :])
            ddy = (oh[:, None] + self.H[None, :]) / 2 + 4 - np.abs(my[ok][:, None] - y[None, :])
            n_ovl += int(((ddx > 0) & (ddy > 0)).sum())
            ddx = (ow[:, None] + ow[None, :]) / 2 + 6 - np.abs(mx[ok][:, None] - mx[ok][None, :])
            ddy = (oh[:, None] + oh[None, :]) / 2 + 6 - np.abs(my[ok][:, None] - my[ok][None, :])
            m = (ddx > 0) & (ddy > 0)
            np.fill_diagonal(m, False)
            n_ovl += int(m.sum() // 2)
            ine = ((np.abs(px[:, :, None] - mx[ok][None, None, :]) < (ow / 2 + 4)[None, None, :]) &
                   (np.abs(py[:, :, None] - my[ok][None, None, :]) < (oh / 2 + 4)[None, None, :])).any(axis=1)
            ine[ok, np.arange(len(ok))] = False
            n_ovl += int(ine.sum())
        # độ dài, hướng ưu tiên ngang/dọc, khung hình
        pen_len = float((ln / PX).sum())
        pen_dir = float((np.minimum(np.abs(ux), np.abs(uy)) * np.minimum(ln, 400) / 100.0).sum())
        W_ = (x + self.W / 2).max() - (x - self.W / 2).min()
        H_ = (y + self.H / 2).max() - (y - self.H / 2).min()
        pen_box = (W_ * H_) / (PX * PY) * 3.0 + 150.0 * abs(math.log((W_ / H_) / muc_tieu))
        c = (6000 * n_cross + 3000 * n_thru + 3000 * n_ov + 1500 * n_ovl + 0.02 * pen_vis + 30 * pen_ang
             + 30 * pen_len + 12 * pen_dir + pen_box)
        if chi_tiet == 'loi':
            bad = set()
            for i_, j_ in zip(*np.nonzero(np.triu(cross))):
                bad.update(self.E[i_]); bad.update(self.E[j_])
            return c, sorted(bad)
        if chi_tiet:
            return c, dict(cross=n_cross, thru=n_thru, ov=n_ov, ovl=n_ovl, vis=int((vis < need - 8).sum()), W=W_, H=H_)
        return c


def khoi_tao(bc):
    G = nx.Graph()
    G.add_nodes_from(range(len(bc.ten)))
    G.add_edges_from(map(tuple, bc.E))
    ok, emb = nx.check_planarity(G)
    assert ok, 'đồ thị không phẳng'
    pos = nx.combinatorial_embedding_to_pos(emb)
    return np.array([pos[i] for i in range(len(bc.ten))], float)      # toạ độ ô lưới nguyên


def toi_uu(bc, muc_tieu, seed, so_buoc, C0, tmax=60.0):
    rnd = random.Random(seed)
    n = len(bc.ten)
    C = C0.copy()
    to_px = lambda C_: C_ * np.array([PX, PY])
    cur = bc.chi_phi(to_px(C), muc_tieu)
    nb = [[] for _ in range(n)]
    for a, b in bc.E:
        nb[a].append(b); nb[b].append(a)
    best, bestC = cur, C.copy()
    occ = {tuple(c) for c in C}
    for it in range(so_buoc):
        t = 1.0 - it / so_buoc
        T = tmax * t ** 2 + 0.5
        r = rnd.random()
        if r < 0.22:                           # bước khối: dịch mọi nút từ ngưỡng k trở đi một ô (nén hoặc nới cột/hàng)
            ax = rnd.randrange(2)
            ngu = np.unique(C[:, ax])
            k = ngu[rnd.randrange(len(ngu))]
            d = -1 if rnd.random() < 0.8 else 1
            Q = C.copy()
            Q[C[:, ax] >= k, ax] += d
            if len({tuple(c) for c in Q}) < n:
                continue
            c2 = bc.chi_phi(to_px(Q), muc_tieu)
            if bc.n_cross_last > 0:
                continue
            if c2 < cur or rnd.random() < math.exp(-(c2 - cur) / T):
                C, cur = Q, c2
                occ = {tuple(c) for c in C}
                if cur < best:
                    best, bestC = cur, C.copy()
            continue
        i = rnd.randrange(n)
        old = tuple(C[i])
        r = rnd.random()
        if r < 0.55 and nb[i]:
            cen = C[nb[i]].mean(axis=0)
            new = (round(cen[0] + rnd.randint(-2, 2)), round(cen[1] + rnd.randint(-2, 2)))
        elif r < 0.9:
            new = (old[0] + rnd.randint(-2, 2), old[1] + rnd.randint(-2, 2))
        else:
            new = (old[0] + rnd.choice((-1, 1)) * rnd.randint(1, 6), old[1])
        if new == old:
            continue
        swap = None
        if new in occ:
            j = next(k for k in range(n) if tuple(C[k]) == new)
            swap = j
        Q = C.copy()
        Q[i] = new
        if swap is not None:
            Q[swap] = old
        c2 = bc.chi_phi(to_px(Q), muc_tieu)
        if bc.n_cross_last > 0:
            continue
        if c2 < cur or rnd.random() < math.exp(-(c2 - cur) / T):
            C, cur = Q, c2
            occ = {tuple(c) for c in C}
            if cur < best:
                best, bestC = cur, C.copy()
    return best, bestC


# --------------------------------------------------------------------------------------------------
def diem_noi(u, cx, cy, tx, ty):
    return clip_rect(cx, cy, u.w, u.h, tx, ty) if u.loai == 'E' else clip_ell(cx, cy, u.w, u.h, tx, ty)


def ve(bc, C, ten):
    nuts = bc.nuts
    P = C * np.array([PX, PY])
    xs = P[:, 0] - (P[:, 0] - bc.W / 2).min() + 50
    ys = P[:, 1] - (P[:, 1] - bc.H / 2).min() + 50
    pos = {n: (xs[i], ys[i]) for i, n in enumerate(bc.ten)}
    Wp = int((xs + bc.W / 2).max() + 50)
    Hp = int((ys + bc.H / 2).max() + 50)
    g = Hinh(Wp, Hp)
    ovals, nhan = [], []
    for c in bc.canh:
        u, v = c['u'], c['v']
        (ux_, uy_), (vx_, vy_) = pos[u], pos[v]
        dx, dy = vx_ - ux_, vy_ - uy_
        ln = math.hypot(dx, dy) or 1
        nx_, ny_ = -dy / ln, dx / ln                       # pháp tuyến để dời các đường song song
        m = len(c['ovals'])
        if c['mkh']:
            for (a_, b_, card) in c['mkh']:
                if isinstance(card, tuple):                # quan hệ tự thân: oval nối với thực thể bằng hai đường song song
                    ent, ov_ = nuts[b_], nuts[a_]
                    ex, ey = pos[b_]
                    ox, oy = pos[a_]
                    ngang = abs(oy - ey) <= abs(ox - ex)
                    for sgn, cc in zip((-1, 1), card):
                        if ngang:
                            yy = ey + sgn * min(ent.h / 2 - 9, 12)
                            xo = ox + (-1 if ox > ex else 1) * (ov_.w / 2) * math.sqrt(max(0.0, 1 - ((yy - oy) / (ov_.h / 2)) ** 2))
                            xe = ex + (ent.w / 2 if ox > ex else -ent.w / 2)
                            g.line([(xo, yy), (xe, yy)])
                            nhan.append((((xe + (30 if ox > ex else -30)), yy), cc, True))
                        else:
                            xx = ex + sgn * min(ent.w / 4, 30)
                            yo = oy + (-1 if oy > ey else 1) * (ov_.h / 2) * math.sqrt(max(0.0, 1 - ((xx - ox) / (ov_.w / 2)) ** 2))
                            ye = ey + (ent.h / 2 if oy > ey else -ent.h / 2)
                            g.line([(xx, yo), (xx, ye)])
                            nhan.append(((xx, ye + (28 if oy > ey else -28)), cc, True))
                    continue
                pa = pos[a_]
                pb = pos[b_]
                p1 = diem_noi(nuts[a_], pa[0], pa[1], pb[0], pb[1])
                p2 = diem_noi(nuts[b_], pb[0], pb[1], pa[0], pa[1])
                g.line([p1, p2])
                d = math.hypot(p1[0] - p2[0], p1[1] - p2[1]) or 1
                nhan.append(((p2[0] + (p1[0] - p2[0]) / d * LAB_OFF, p2[1] + (p1[1] - p2[1]) / d * LAB_OFF), card, False))
        for k, (verb, child, parent, bc_, bp_) in enumerate(c['ovals']):
            kc = abs(nx_) * max(size_of(o[0], 13, False, 26) for o in c['ovals']) + abs(ny_) * 36 + 12
            off = (k - (m - 1) / 2) * kc
            sx, sy = nx_ * off, ny_ * off
            cu = (ux_ + sx, uy_ + sy)
            cv = (vx_ + sx, vy_ + sy)
            pu = diem_thoat(nuts[u], pos[u], cu, cv)
            pv = diem_thoat(nuts[v], pos[v], cv, cu)
            g.line([pu, pv])
            mid = ((pu[0] + pv[0]) / 2, (pu[1] + pv[1]) / 2)
            ovals.append((mid, verb))
            d = math.hypot(pu[0] - pv[0], pu[1] - pv[1]) or 1
            tu, tv = (bc_, bp_) if child == u else (bp_, bc_)
            nhan.append(((pu[0] + (pv[0] - pu[0]) / d * LAB_OFF, pu[1] + (pv[1] - pu[1]) / d * LAB_OFF), tu, False))
            nhan.append(((pv[0] + (pu[0] - pv[0]) / d * LAB_OFF, pv[1] + (pu[1] - pv[1]) / d * LAB_OFF), tv, False))
    for (mx, my), verb in ovals:
        g.ell(mx, my, size_of(verb, 13, False, 26), 36, verb, ORG, ORG_B, False, 13)
    for n in bc.ten:
        x, y = pos[n]
        u = nuts[n]
        if u.loai == 'E':
            g.rect(x, y, u.w, u.h, u.nhan, sz=15)
        elif u.loai == 'M':
            g.ell(x, y, u.w, u.h, u.nhan, BLU, BLU_B, True, 13)
        else:
            g.ell(x, y, u.w, u.h, u.nhan, ORG, ORG_B, False, 13)
    for (x, y), t, _ in nhan:
        g.text(x, y, t, 13, True, (20, 20, 20), halo=True)
    g.save(os.path.join(HINH, ten + '.png'), box=(0, 0, Wp, Hp))
    return pos, ovals


def diem_thoat(u, c, p0, p1):
    """Giao của tia từ p0 (nằm trong nút u, tâm c) về phía p1 với biên nút u; nếu p0 ngoài nút thì cắt theo đường tâm."""
    dx, dy = p1[0] - p0[0], p1[1] - p0[1]
    rx, ry = p0[0] - c[0], p0[1] - c[1]
    a, b = u.w / 2, u.h / 2
    if u.loai == 'E':
        if abs(rx) > a or abs(ry) > b:
            return diem_noi(u, c[0], c[1], p1[0], p1[1])
        ts = [((a if dx > 0 else -a) - rx) / dx] if dx else []
        ts += [((b if dy > 0 else -b) - ry) / dy] if dy else []
        t = min(ts)
    else:
        A = (dx / a) ** 2 + (dy / b) ** 2
        B = 2 * (rx * dx / a ** 2 + ry * dy / b ** 2)
        Cc = (rx / a) ** 2 + (ry / b) ** 2 - 1
        disc = B * B - 4 * A * Cc
        if disc < 0 or Cc > 0:
            return diem_noi(u, c[0], c[1], p1[0], p1[1])
        t = (-B + math.sqrt(disc)) / (2 * A)
    return (p0[0] + dx * t, p0[1] + dy * t)


def doc_cache():
    try:
        return json.load(open(CACHE, encoding='utf-8'))
    except (OSError, ValueError):
        return {}


def lam_hinh(ten, keep, muc_tieu, nv_chon=False, chi_nv=False, so_buoc=None, moi=False):
    nuts, canh = dung(keep, nv_chon, chi_nv)
    bc = BoCuc(nuts, canh)
    n = len(bc.ten)
    so_buoc = so_buoc or int(4000 + 4000 * n)
    cache = doc_cache().get(ten)
    if cache and not moi and set(cache) == set(bc.ten):
        C = np.array([cache[t] for t in bc.ten], float)
    else:
        C = khoi_tao(bc)
        # nén ban đầu: chia nhỏ lưới bằng cách giữ nguyên, SA sẽ kéo lại gần nhau
        best = None
        for s in range(2):
            c, Cs = toi_uu(bc, muc_tieu, 7 + s, so_buoc, C)
            if best is None or c < best[0]:
                best = (c, Cs)
        C = best[1]
        for r in range(8):
            c, d = bc.chi_phi(C * np.array([PX, PY]), muc_tieu, True)
            if d['thru'] == 0 and d['ov'] == 0 and d['ovl'] == 0 and d['vis'] == 0:
                break
            c, C = toi_uu(bc, muc_tieu, 50 + r, so_buoc, C, tmax=25.0)
    c, d = bc.chi_phi(C * np.array([PX, PY]), muc_tieu, True)
    pos, ovals = ve(bc, C, ten)
    print(f'{ten}: {n} nút, {len(bc.canh)} cạnh | giao cắt {d["cross"]}, xuyên nút {d["thru"]}, chồng nút {d["ov"]}, chồng oval {d["ovl"]}, '
          f'đoạn ngắn {d["vis"]} | khung {int(d["W"])}x{int(d["H"])}')
    if d['cross'] == 0 and d['thru'] == 0 and d['ov'] == 0 and d['ovl'] == 0:
        ca = doc_cache()
        ca[ten] = {t: [int(C[i, 0]), int(C[i, 1])] for i, t in enumerate(bc.ten)}
        json.dump(ca, open(CACHE, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    return d


def main(chon=None):
    tat_ca = set(erd.ENTITIES) | set(erd.MKH)
    viec = [('erd_tong_quat', tat_ca, 0.72, True, False)]
    for k, (ten, ents) in erd.GROUPS.items():
        keep = set(ents) | {m for m in erd.MKH if m in ents or all(e in ents for e, _ in erd.mkh_card()[m])}
        viec.append((f'erd_nhom{k}', keep, 1.0, k == '3', k == '7'))
    for ten, keep, mt, nvc, cnv in viec:
        if chon and ten not in chon:
            continue
        lam_hinh(ten, keep, mt, nv_chon=nvc, chi_nv=cnv, moi=bool(os.environ.get('ERD_MOI')))


if __name__ == '__main__':
    main(set(sys.argv[1:]) or None)
