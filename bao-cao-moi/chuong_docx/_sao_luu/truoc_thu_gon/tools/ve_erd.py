#!/usr/bin/env python3
"""Vẽ ERD theo phong cách báo cáo mẫu (draw.io): thực thể chữ nhật vàng, mối kết hợp oval cam, mối kết hợp có thuộc tính oval xanh,
đường thẳng, bản số (min,max) cạnh thực thể. Vị trí các nút đặt tay trong tools/bo_cuc_erd.py; hình nhóm cắt từ cùng bố cục.
Chạy:  python3 tools/ve_erd.py"""
import os
import sys

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import erd
from bo_cuc_erd import ENT_POS, MKH_POS, REL_POS, NV_BAR, WAY, SIZE

HINH = os.path.join(HERE, '..', 'hinh')
S = 2                      # siêu lấy mẫu rồi thu nhỏ để nét mịn
F_REG = '/System/Library/Fonts/Supplemental/Arial Unicode.ttf'
F_BOLD = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
YEL, YEL_B = (255, 242, 204), (214, 182, 86)
ORG, ORG_B = (255, 230, 204), (215, 155, 0)
BLU, BLU_B = (218, 232, 252), (108, 142, 191)
INK = (40, 40, 40)


def font(sz, bold=False):
    return ImageFont.truetype(F_BOLD if bold else F_REG, int(sz * S))


def clip_rect(cx, cy, w, h, tx, ty):
    """Giao của đoạn từ tâm (cx,cy) tới (tx,ty) với biên chữ nhật."""
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0:
        return cx, cy
    k = min((w / 2) / abs(dx) if dx else 1e9, (h / 2) / abs(dy) if dy else 1e9)
    return cx + dx * k, cy + dy * k


def clip_ell(cx, cy, w, h, tx, ty):
    dx, dy = tx - cx, ty - cy
    d = ((dx / (w / 2)) ** 2 + (dy / (h / 2)) ** 2) ** 0.5 or 1
    return cx + dx / d, cy + dy / d


class Hinh:
    def __init__(self, W, H):
        self.W, self.H = W, H
        self.im = Image.new('RGB', (W * S, H * S), 'white')
        self.d = ImageDraw.Draw(self.im)
        self.labels = []

    def line(self, pts, col=INK, w=1.6):
        self.d.line([(x * S, y * S) for x, y in pts], fill=col, width=int(w * S), joint='curve')

    def text(self, x, y, s, sz=14, bold=False, fill=INK, halo=False):
        f = font(sz, bold)
        tw = self.d.textlength(s, font=f)
        th = sz * S
        if halo:
            self.d.rectangle((x * S - tw / 2 - 2 * S, y * S - th / 2 - S, x * S + tw / 2 + 2 * S, y * S + th / 2 + S), fill='white')
        self.d.text((x * S - tw / 2, y * S - th * 0.62), s, font=f, fill=fill)

    def rect(self, cx, cy, w, h, label, fill=YEL, border=YEL_B, sz=20):
        self.d.rectangle(((cx - w / 2) * S, (cy - h / 2) * S, (cx + w / 2) * S, (cy + h / 2) * S), fill=fill, outline=border, width=2 * S)
        self._lines(cx, cy, label, sz, True)

    def ell(self, cx, cy, w, h, label, fill, border, bold=False, sz=15):
        self.d.ellipse(((cx - w / 2) * S, (cy - h / 2) * S, (cx + w / 2) * S, (cy + h / 2) * S), fill=fill, outline=border, width=2 * S)
        self._lines(cx, cy, label, sz, bold)

    def _lines(self, cx, cy, label, sz, bold):
        parts = label.split('\n')
        for i, p in enumerate(parts):
            self.text(cx, cy + (i - (len(parts) - 1) / 2) * (sz + 3), p, sz, bold)

    def save(self, path, box=None):
        im = self.im
        if box:
            x0, y0, x1, y1 = [int(v * S) for v in box]
            im = im.crop((x0, y0, x1, y1))
        im = im.resize((im.width // S, im.height // S), Image.LANCZOS)
        im.save(path, dpi=(150, 150))


def size_of(txt, sz, bold=True, pad=34):
    im = Image.new('RGB', (10, 10))
    f = font(sz, bold)
    return max(ImageDraw.Draw(im).textlength(t, font=f) for t in txt.split('\n')) / S + pad


def nen(vals, cap):
    """Hàm nén toạ độ: khoảng cách giữa hai giá trị liền nhau tối đa `cap` (giữ thứ tự và độ thẳng hàng)."""
    a = sorted({round(v, 1) for v in vals})
    mp, cur = {a[0]: a[0]}, a[0]
    for u, v in zip(a, a[1:]):
        cur += min(v - u, cap)
        mp[v] = cur

    def f(v):
        if v <= a[0]:
            return v - a[0] + mp[a[0]]
        if v >= a[-1]:
            return v - a[-1] + mp[a[-1]]
        for u, w in zip(a, a[1:]):
            if u <= v <= w:
                return mp[u] + (v - u) * (mp[w] - mp[u]) / (w - u)
    return f


def ve(keep, name, cap=None, only_nv=False):
    global ENT_POS, MKH_POS, REL_POS, WAY
    saved = (ENT_POS, MKH_POS, REL_POS, WAY)
    if cap:
        xs_ = [p[0] for n, p in ENT_POS.items() if n in keep] + [p[0] for n, p in MKH_POS.items() if n in keep]
        ys_ = [p[1] for n, p in ENT_POS.items() if n in keep and n != 'NHANVIEN'] + [p[1] for n, p in MKH_POS.items() if n in keep]
        fx, fy = nen(xs_, cap[0]), nen(ys_, cap[1])
        nx = fx(ENT_POS['NHANVIEN'][0]) if 'NHANVIEN' in keep else 0
        ENT_POS = {n: (fx(p[0]), fy(p[1])) for n, p in ENT_POS.items()}
        if 'NHANVIEN' in keep:
            import erd as _e
            lane_x = [ENT_POS[r[1]][0] for r in _e.relationships() if r[2] == 'NHANVIEN' and r[1] in keep and r[1] in ENT_POS]
            lane_x += [MKH_POS[r[1]][0] for r in _e.relationships() if r[2] == 'NHANVIEN' and r[1] in keep and r[1] in MKH_POS]
            ENT_POS['NHANVIEN'] = (max(lane_x) + 520, ENT_POS['NHANVIEN'][1])
        MKH_POS = {n: (fx(p[0]), fy(p[1])) for n, p in MKH_POS.items()}
        REL_POS = {k: (fx(p[0]), fy(p[1])) for k, p in REL_POS.items()}
        WAY = {}
    try:
        return _ve(keep, name, only_nv)
    finally:
        ENT_POS, MKH_POS, REL_POS, WAY = saved


def _ve(keep, name, only_nv=False):
    ents = {n: p for n, p in ENT_POS.items() if n in keep}
    mkh = erd.mkh_card()
    rels = [r for r in erd.relationships() if r[1] in keep and (r[2] in keep) and r[1] in ENT_POS | MKH_POS and r[2] in ENT_POS | MKH_POS]
    if only_nv:
        rels = [r for r in rels if r[2] == 'NHANVIEN']
    # kích thước khung
    xs, ys = [], []
    for n, (x, y) in {**{k: (v[0], v[1]) for k, v in ents.items()}, **{k: v for k, v in MKH_POS.items() if k in keep}}.items():
        xs.append(x); ys.append(y)
    for k, v in REL_POS.items():
        pass
    x0, y0, x1, y1 = min(xs) - 160, min(ys) - 90, max(xs) + 160, max(ys) + 90
    W, H = int(max(xs) + 220), int(max(ys) + 140)
    g = Hinh(W, H)
    # tâm và kích thước các nút
    node = {}
    for n, p in ents.items():
        x, y = p[0], p[1]
        lab = erd.SHORT[n]
        w = size_of(lab, 20)
        h = 52
        if n in SIZE:
            w, h = SIZE[n]
        if n == 'NHANVIEN' and NV_BAR:
            lanes = [ENT_POS[r[1]][1] for r in rels if r[2] == 'NHANVIEN' and r[1] in ENT_POS] + \
                    [MKH_POS[r[1]][1] for r in rels if r[2] == 'NHANVIEN' and r[1] in MKH_POS]
            lanes += [MKH_POS[m][1] for m in MKH_POS if m in keep and 'NHANVIEN' in [e for e, _ in erd.mkh_card()[m]]]
            lo, hi = min(lanes) - 90, max(lanes) + 90
            w, h = 130, max(hi - lo, 160)
            y = (lo + hi) / 2
        node[n] = (x, y, w, h, 'rect', lab)
    for n, (x, y) in MKH_POS.items():
        if n in keep:
            lab = erd.SHORT[n].replace(' ', '\n', 1) if len(erd.SHORT[n]) > 14 else erd.SHORT[n]
            node[n] = (x, y, size_of(lab, 17) + 34, 66, 'mkh', lab)
    rel_nodes = []
    seen = {}
    for verb, child, parent, bc, bp, cols in rels:
        key = (child, parent, verb)
        if child not in node or parent not in node:
            continue
        if key in REL_POS:
            rx, ry = REL_POS[key]
        elif child == parent:
            rx, ry = node[child][0], node[child][1] + node[child][3] / 2 + 80
        elif parent == 'NHANVIEN' and NV_BAR:
            cx_, cy_, cw_ = node[child][0], node[child][1], node[child][2]
            nvl = [r for r in rels if r[1] == child and r[2] == 'NHANVIEN']
            idx = [r[0] for r in nvl].index(verb)
            rx = (cx_ + cw_ / 2 + node[parent][0] - node[parent][2] / 2) / 2
            ry = cy_ + (idx - (len(nvl) - 1) / 2) * 62
        else:
            (x1_, y1_), (x2_, y2_) = node[child][:2], node[parent][:2]
            rx, ry = (x1_ + x2_) / 2, (y1_ + y2_) / 2
        rel_nodes.append((key, rx, ry, verb, bc, bp))
    # ---- vẽ đường
    def attach(nid, tx, ty, lane_y=None):
        x, y, w, h, kind, lab = node[nid]
        if lane_y is not None and kind == 'rect' and h > 200:
            yy = min(max(lane_y, y - h / 2 + 12), y + h / 2 - 12)
            return (x - w / 2 if tx < x else x + w / 2), yy
        if kind == 'rect':
            return clip_rect(x, y, w, h, tx, ty)
        return clip_ell(x, y, w, h, tx, ty)
    for key, rx, ry, verb, bc, bp in rel_nodes:
        child, parent, _ = key
        if child == parent:
            x, y, w, h = node[child][:4]
            for dxo, card in ((-w / 4, bc), (w / 4, bp)):
                a = (x + dxo, y + h / 2)
                e2 = clip_ell(rx, ry, size_of(verb, 16, False, 28), 50, a[0], a[1])
                g.line([a, e2])
                g.labels.append((a, e2, card))
            continue
        for end, card in ((child, bc), (parent, bp)):
            way = WAY.get((key, end), [])
            tx, ty = (way[0] if way else (rx, ry))
            a = attach(end, tx, ty, lane_y=ry)
            ew = size_of(verb, 16, False, 28)
            pts = [a] + list(way)
            last = pts[-1]
            e2 = clip_ell(rx, ry, ew, 50, last[0], last[1])
            g.line(pts + [e2])
            g.labels.append((a, pts[1] if len(pts) > 1 else e2, card))
    for n, (a, b) in ((n, tuple(mkh[n])) for n in mkh if n in node and (not only_nv or any(e == 'NHANVIEN' for e, _ in mkh[n]))):
        for e, card in mkh[n]:
            if e in node:
                mx, my = node[n][:2]
                way = WAY.get((n, e), [])
                tx, ty = (way[-1] if way else (mx, my))
                p1 = attach(e, tx, ty, lane_y=my)
                first = way[0] if way else p1
                p2 = clip_ell(mx, my, node[n][2], node[n][3], first[0], first[1])
                g.line([p2] + list(way) + [p1])
                g.labels.append((p1, (way[-1] if way else p2), card))
    # ---- nút
    for key, rx, ry, verb, bc, bp in rel_nodes:
        g.ell(rx, ry, size_of(verb, 16, False, 28), 50, verb, ORG, ORG_B, False, 16)
    for n, (x, y, w, h, kind, lab) in node.items():
        if kind == 'mkh' and only_nv and not any(e == 'NHANVIEN' for e, _ in mkh[n]):
            continue
        if kind == 'rect':
            g.rect(x, y, w, h, lab)
        else:
            g.ell(x, y, w, h, lab, BLU, BLU_B, True, 17)
    for (a, b, card) in g.labels:
        dx, dy = b[0] - a[0], b[1] - a[1]
        ln = (dx * dx + dy * dy) ** 0.5 or 1
        d = 24
        g.text(a[0] + dx / ln * d, a[1] + dy / ln * d - (8 if abs(dx) > abs(dy) else 0), card, 15, True, (20, 20, 20), halo=True)
    bx0 = min(v[0] - v[2] / 2 for v in node.values())
    by0 = min(v[1] - v[3] / 2 for v in node.values())
    bx1 = max(v[0] + v[2] / 2 for v in node.values())
    by1 = max(v[1] + v[3] / 2 for v in node.values())
    for key, rx, ry, verb, bc, bp in rel_nodes:
        bx0, bx1, by0, by1 = min(bx0, rx - 90), max(bx1, rx + 90), min(by0, ry - 40), max(by1, ry + 40)
    g.save(os.path.join(HINH, name + '.png'), box=(max(bx0 - 50, 0), max(by0 - 50, 0), min(bx1 + 50, W), min(by1 + 50, H)))
    return W, H


def main():
    ve(set(erd.ENTITIES) | set(erd.MKH), 'erd_tong_quat')
    for k, (ten, ents) in erd.GROUPS.items():
        keep = set(ents)
        keep |= {m for m in erd.MKH if m in ents or all(e in ents for e, _ in erd.mkh_card()[m])}
        if k == '8':     # hình "trách nhiệm": chỉ các mối kết hợp tới NHÂN VIÊN
            ve(keep, f'erd_nhom{k}', cap=(380, 120), only_nv=True)
        else:
            ve(keep, f'erd_nhom{k}', cap=(330, 190))
    print('đã vẽ erd_tong_quat và', len(erd.GROUPS), 'hình nhóm')


if __name__ == '__main__':
    main()
