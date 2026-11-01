#!/usr/bin/env python3
"""Vẽ đồ thị quan hệ (Hình 3.1, 3.2) bằng đường THẲNG trên lưới, giống cách vẽ của báo cáo mẫu.

Bố cục: ủ mô phỏng đặt 25 nút vào ô lưới sao cho ít giao cắt nhất, không có cung đi xuyên nút khác,
các cung hướng về bên phải khi có thể. Đồ thị này KHÔNG phẳng (kiểm bằng networkx), nên số giao cắt tối thiểu > 0;
kết quả (số giao cắt) được in ra và ghi vào tools/bo_cuc_dothi.json. Vị trí được lưu để chạy lại ra cùng một hình.

Chạy:  python3 tools/ve_dothi.py            (dùng bố cục đã lưu; chưa có thì tìm mới)
       DOTHI_MOI=1 python3 tools/ve_dothi.py (tìm lại bố cục từ đầu)
Cần Graphviz (`neato`) trong PATH."""
import json
import math
import multiprocessing as mp
import os
import random
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
CACHE = os.path.join(HERE, 'bo_cuc_dothi.json')
HINH = os.path.join(HERE, '..', 'hinh')

# nửa kích thước hộp nút theo đơn vị ô lưới (đủ rộng cho hộp có tên ở Hình 3.2)
HX, HY = 0.46, 0.30
W_HIT = 900.0                  # phạt mỗi lần cung đi xuyên hộp một nút khác (tinh chỉnh dùng mức rất cao)
CUNG_MIN = 1.15                # độ dài tối thiểu của một cung (ô lưới) để còn thấy mũi tên
GOC_MIN = 22.0                 # góc tối thiểu (độ) giữa hai cung cùng nút


def doc_do_thi():
    import dothi
    R = dothi.run()
    idx = {n: i + 1 for i, n in enumerate(R['nodes'])}
    E, role, loops = [], set(), []
    for i, j, kind, fk, f, b in dothi.arcs(R):
        if i == j:
            loops.append(idx[i])
            continue
        E.append((idx[i], idx[j]))
        if fk and fk[2] == 'NHANVIEN':
            role.add((idx[i], idx[j]))
    return R, idx, E, role, loops


def _ccw(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def _cat(p1, p2, p3, p4):
    d1, d2 = _ccw(p3, p4, p1), _ccw(p3, p4, p2)
    d3, d4 = _ccw(p1, p2, p3), _ccw(p1, p2, p4)
    return d1 * d2 < 0 and d3 * d4 < 0


def _xuyen_hop(p, q, c):
    """Đoạn p-q có cắt hình chữ nhật tâm c (nửa cạnh HX, HY) không (Liang–Barsky)."""
    x0, y0 = p[0] - c[0], p[1] - c[1]
    dx, dy = q[0] - p[0], q[1] - p[1]
    t0, t1 = 0.0, 1.0
    for pp, qq in ((-dx, x0 + HX), (dx, HX - x0), (-dy, y0 + HY), (dy, HY - y0)):
        if pp == 0:
            if qq <= 0:
                return False
        else:
            r = qq / pp
            if pp < 0:
                if r > t1:
                    return False
                t0 = max(t0, r)
            else:
                if r < t0:
                    return False
                t1 = min(t1, r)
    return t1 - t0 > 1e-9


def chi_phi(pos, E, n_nodes, chi_tiet=False):
    cross = hit = 0
    ang = 0.0
    length = rev = 0.0
    seg = [(pos[a], pos[b]) for a, b in E]
    for i in range(len(E)):
        a1, b1 = E[i]
        for j in range(i + 1, len(E)):
            a2, b2 = E[j]
            if a1 in (a2, b2) or b1 in (a2, b2):
                continue
            if _cat(seg[i][0], seg[i][1], seg[j][0], seg[j][1]):
                cross += 1
    for i, (a, b) in enumerate(E):
        p, q = seg[i]
        d = math.hypot(p[0] - q[0], p[1] - q[1])
        length += d + (600.0 * (CUNG_MIN - d) if d < CUNG_MIN else 0.0)
        if q[0] < p[0]:
            rev += 1
        for n in range(1, n_nodes + 1):
            if n != a and n != b and _xuyen_hop(p, q, pos[n]):
                hit += 1
    inc = {}
    for a, b in E:
        inc.setdefault(a, []).append(pos[b])
        inc.setdefault(b, []).append(pos[a])
    for n, others in inc.items():
        c = pos[n]
        v = [(o[0] - c[0], o[1] - c[1]) for o in others]
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                m = math.hypot(*v[i]) * math.hypot(*v[j])
                if m < 1e-9:           # hai nút trùng tọa độ
                    ang += 5.0
                    continue
                cs = max(-1.0, min(1.0, (v[i][0] * v[j][0] + v[i][1] * v[j][1]) / m))
                g = math.degrees(math.acos(cs))
                if g < GOC_MIN:
                    ang += (GOC_MIN - g) / GOC_MIN
    tong = 400 * cross + W_HIT * hit + 150 * ang + length + 2.0 * rev
    if chi_tiet:
        return tong, cross, hit, ang, length, rev
    return tong


def _goc_nut(pos, n, nb):
    c = pos[n]
    v = [(pos[o][0] - c[0], pos[o][1] - c[1]) for o in nb[n]]
    t = 0.0
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            m = math.hypot(*v[i]) * math.hypot(*v[j])
            if m < 1e-9:               # hai nút trùng tọa độ
                t += 5.0
                continue
            cs = max(-1.0, min(1.0, (v[i][0] * v[j][0] + v[i][1] * v[j][1]) / m))
            g = math.degrees(math.acos(cs))
            if g < GOC_MIN:
                t += (GOC_MIN - g) / GOC_MIN
    return t


def chi_phi_cuc_bo(pos, E, n_nodes, S, moved, nb):
    """Phần chi phí chỉ phụ thuộc các cung S (cạnh nối với nút đã đổi chỗ) và các nút đã đổi chỗ."""
    tong = 0.0
    Sset = set(S)
    seg = {i: (pos[E[i][0]], pos[E[i][1]]) for i in range(len(E)) if i in Sset or True}
    for i in S:
        a1, b1 = E[i]
        p, q = seg[i]
        for j in range(len(E)):
            if j == i or (j in Sset and j < i):
                continue
            a2, b2 = E[j]
            if a1 in (a2, b2) or b1 in (a2, b2):
                continue
            if _cat(p, q, seg[j][0], seg[j][1]):
                tong += 400
        d = math.hypot(p[0] - q[0], p[1] - q[1])
        tong += d + (600.0 * (CUNG_MIN - d) if d < CUNG_MIN else 0.0)
        if q[0] < p[0]:
            tong += 2.0
        for n in range(1, n_nodes + 1):
            if n != a1 and n != b1 and _xuyen_hop(p, q, pos[n]):
                tong += W_HIT
    for n in moved:
        for j in range(len(E)):
            if j in Sset:
                continue
            a, b = E[j]
            if n != a and n != b and _xuyen_hop(seg[j][0], seg[j][1], pos[n]):
                tong += W_HIT
    cand = set(moved)
    for n in moved:
        cand.update(nb[n])
    for n in cand:
        tong += 150 * _goc_nut(pos, n, nb)
    return tong


def bo_cuc_dau(E, n_nodes, cols, rows, rnd):
    """Bố cục lực kéo (lực kéo (spring)) quy về ô lưới gần nhất, rồi để ủ mô phỏng tinh chỉnh."""
    import networkx as nx
    G = nx.Graph()
    G.add_nodes_from(range(1, n_nodes + 1))
    G.add_edges_from(E)
    p = nx.spring_layout(G, seed=rnd.randint(0, 10**6), k=1.2, iterations=300)
    xs = [v[0] for v in p.values()]
    ys = [v[1] for v in p.values()]
    sx = (max(xs) - min(xs)) or 1
    sy = (max(ys) - min(ys)) or 1
    pos, used = {}, set()
    order = sorted(p, key=lambda n: rnd.random())
    for n in order:
        fx = (p[n][0] - min(xs)) / sx * (cols - 1)
        fy = (p[n][1] - min(ys)) / sy * (rows - 1)
        best = None
        for c in range(cols):
            for r in range(rows):
                if (c, r) in used:
                    continue
                d = (c - fx) ** 2 + (r - fy) ** 2
                if best is None or d < best[0]:
                    best = (d, (c, r))
        pos[n] = best[1]
        used.add(best[1])
    return pos


def u_mo_phong(args):
    global W_HIT
    seed, cols, rows, E, n_nodes, steps = args[:6]
    init = args[6] if len(args) > 6 else None
    if len(args) > 7:
        W_HIT = args[7]
    T0 = args[8] if len(args) > 8 else 300.0
    rnd = random.Random(seed)
    cells = [(c, r) for c in range(cols) for r in range(rows)]
    nodes = list(range(1, n_nodes + 1))
    inc = {n: [] for n in nodes}
    nb = {n: [] for n in nodes}
    for i, (a, b) in enumerate(E):
        inc[a].append(i)
        inc[b].append(i)
        nb[a].append(b)
        nb[b].append(a)
    pos = dict(init) if init else bo_cuc_dau(E, n_nodes, cols, rows, rnd)
    cur = chi_phi(pos, E, n_nodes)
    best, best_pos = cur, dict(pos)
    T1 = 2.0
    used = {v: k for k, v in pos.items()}
    for s in range(steps):
        T = T0 * (T1 / T0) ** (s / steps)
        n = rnd.choice(nodes)
        old = pos[n]
        m = None
        if rnd.random() < 0.3:
            m = rnd.choice(nodes)
            if m == n:
                continue
            moved = (n, m)
            S = sorted(set(inc[n]) | set(inc[m]))
        else:
            if rnd.random() < 0.6:
                c = (min(cols - 1, max(0, old[0] + rnd.randint(-2, 2))), min(rows - 1, max(0, old[1] + rnd.randint(-2, 2))))
            else:
                c = rnd.choice(cells)
            if c in used:
                continue
            moved = (n,)
            S = inc[n]
        truoc = chi_phi_cuc_bo(pos, E, n_nodes, S, moved, nb)
        if m is None:
            pos[n] = c
        else:
            pos[n], pos[m] = pos[m], pos[n]
        sau = chi_phi_cuc_bo(pos, E, n_nodes, S, moved, nb)
        d = sau - truoc
        if d <= 0 or rnd.random() < math.exp(-d / T):
            cur += d
            if m is None:
                del used[old]
                used[c] = n
            else:
                used[pos[n]] = n
                used[pos[m]] = m
            if cur < best - 1e-9:
                best, best_pos = cur, dict(pos)
        else:
            if m is None:
                pos[n] = old
            else:
                pos[n], pos[m] = pos[m], pos[n]
    return chi_phi(best_pos, E, n_nodes), best_pos, cols, rows


def tim_bo_cuc(E, n_nodes, thu=((6, 6), (7, 5), (6, 5), (7, 6)), nhan=4, steps=150000):
    jobs = []
    seed = 1
    for cols, rows in thu:
        for _ in range(nhan):
            jobs.append((seed, cols, rows, E, n_nodes, steps, None, 6000.0, 300.0))
            seed += 1
    with mp.Pool(min(len(jobs), os.cpu_count() or 4)) as pool:
        res = pool.map(u_mo_phong, jobs)
    res.sort(key=lambda x: x[0])
    return res


def _chong(pos, n, nb_nodes):
    """Số nút chồng hộp với nút n (tọa độ thực, đơn vị ô lưới)."""
    c = 0
    for m in range(1, nb_nodes + 1):
        if m != n and abs(pos[m][0] - pos[n][0]) < 2 * HX + 0.04 and abs(pos[m][1] - pos[n][1]) < 2 * HY + 0.04:
            c += 1
    return c


def u_mo_phong_thuc(args):
    """Ủ mô phỏng trên tọa độ thực (ô lưới không còn là số nguyên): dịch nhẹ từng nút để loại cung xuyên nút
    mà giữ số giao cắt thấp. Xuất phát từ bố cục lưới đã lưu."""
    global W_HIT
    seed, cols, rows, E, n_nodes, steps, init, w_hit, T0 = args
    W_HIT = w_hit
    rnd = random.Random(seed)
    nodes = list(range(1, n_nodes + 1))
    inc = {n: [] for n in nodes}
    nb = {n: [] for n in nodes}
    for i, (a, b) in enumerate(E):
        inc[a].append(i)
        inc[b].append(i)
        nb[a].append(b)
        nb[b].append(a)
    pos = {n: (float(p[0]), float(p[1])) for n, p in init.items()}
    cur = chi_phi(pos, E, n_nodes)
    best, best_pos = cur, dict(pos)
    T1 = 1.0
    for s in range(steps):
        T = T0 * (T1 / T0) ** (s / steps)
        n = rnd.choice(nodes)
        old = pos[n]
        sig = 0.15 + 0.5 * rnd.random()
        c = (min(cols - 1, max(0, old[0] + rnd.gauss(0, sig))), min(rows - 1, max(0, old[1] + rnd.gauss(0, sig))))
        pos[n] = old
        truoc = chi_phi_cuc_bo(pos, E, n_nodes, inc[n], (n,), nb) + 20000 * _chong(pos, n, n_nodes)
        pos[n] = c
        sau = chi_phi_cuc_bo(pos, E, n_nodes, inc[n], (n,), nb) + 20000 * _chong(pos, n, n_nodes)
        d = sau - truoc
        if d <= 0 or rnd.random() < math.exp(-d / T):
            cur += d
            if cur < best - 1e-9:
                best, best_pos = cur, dict(pos)
        else:
            pos[n] = old
    return chi_phi(best_pos, E, n_nodes), best_pos, cols, rows


def tinh_chinh(pos, E, n_nodes, cols, rows, nhan=8, steps=120000, t0=120.0):
    """Ủ mô phỏng trên tọa độ thực, nhiều hạt giống, xuất phát từ bố cục đã lưu; phạt xuyên nút rất cao (6000)."""
    jobs = [(2000 + k, cols, rows, E, n_nodes, steps, pos, 6000.0, t0) for k in range(nhan)]
    with mp.Pool(min(len(jobs), os.cpu_count() or 4)) as pool:
        res = pool.map(u_mo_phong_thuc, jobs)
    res.sort(key=lambda x: x[0])
    for best, p, c, r in res[:4]:
        _, cross, hit, ang, ln, rev = chi_phi(p, E, n_nodes, True)
        print(f'tinh chỉnh: chi phí {best:.1f} | giao cắt {cross} | xuyên nút {hit} | góc hẹp {ang:.2f}')
    return res[0][1]


def rong_nhan(ten, so_nut, co_chu):
    """Bề rộng hộp (inch) của nhãn hai dòng: dòng dài nhất; Helvetica chữ hoa ~0,124 inch mỗi ký tự ở cỡ 14."""
    return 0.124 * max(len(ten), len(str(so_nut))) * co_chu / 14.0 + 0.18


CO_CHU_TEN = 12                # cỡ chữ (pt) trong hộp của hình có tên


def vi_tri_inch(R, idx, pos, cols, rows, so, px_ten=2.1):
    """Tọa độ (inch) và nửa kích thước hộp của các nút. Cả hai hình nhân vị trí ô lưới với cùng một tỉ lệ ngang/dọc
    (phép co giãn đều giữ nguyên các giao cắt); hình có tên dùng ô rộng hơn vì hộp chứa tên quan hệ."""
    if so:
        px, py, half = 1.45, 1.0, (0.31, 0.31)
    else:
        px, py, half = px_ten, 0.95, None
    xy, hf = {}, {}
    for n in R['nodes']:
        c, r = pos[idx[n]]
        xy[n] = (c * px, (rows - 1 - r) * py)
        hf[n] = half if half else (rong_nhan(n, idx[n], CO_CHU_TEN) / 2, 0.26)
    return xy, hf


def kiem_hinh(R, E, idx, xy, half):
    """Kiểm tra trên tọa độ thật (inch): số cặp cung giao nhau và số cung đi xuyên hộp nút khác."""
    global HX, HY
    ten = {v: k for k, v in idx.items()}
    P = {k: xy[ten[k]] for k in ten}
    cross = hit = 0
    for i in range(len(E)):
        for j in range(i + 1, len(E)):
            a1, b1 = E[i]
            a2, b2 = E[j]
            if a1 in (a2, b2) or b1 in (a2, b2):
                continue
            if _cat(P[a1], P[b1], P[a2], P[b2]):
                cross += 1
    luu = (HX, HY)
    try:
        for a, b in E:
            for n in P:
                if n in (a, b):
                    continue
                HX, HY = half[ten[n]]
                if _xuyen_hop(P[a], P[b], P[n]):
                    hit += 1
    finally:
        HX, HY = luu
    return cross, hit


def _chi_phi_inch(P, half, E):
    """Chi phí trên tọa độ thật (inch): giao cắt, cung xuyên hộp nút khác, hộp chồng nhau."""
    global HX, HY
    cross = hit = chong = 0
    for i in range(len(E)):
        for j in range(i + 1, len(E)):
            a1, b1 = E[i]
            a2, b2 = E[j]
            if a1 in (a2, b2) or b1 in (a2, b2):
                continue
            if _cat(P[a1], P[b1], P[a2], P[b2]):
                cross += 1
    luu = (HX, HY)
    try:
        for a, b in E:
            for n in P:
                if n in (a, b):
                    continue
                HX, HY = half[n]
                if _xuyen_hop(P[a], P[b], P[n]):
                    hit += 1
    finally:
        HX, HY = luu
    ks = list(P)
    for i in range(len(ks)):
        for j in range(i + 1, len(ks)):
            m, n = ks[i], ks[j]
            if abs(P[m][0] - P[n][0]) < half[m][0] + half[n][0] + 0.04 and abs(P[m][1] - P[n][1]) < half[m][1] + half[n][1] + 0.04:
                chong += 1
    return 400 * cross + 6000 * hit + 20000 * chong, cross, hit, chong


def nudge(R, E, idx, xy, half, buoc=0.2, tam=0.85, luot=4):
    """Dịch từng nút một chút (tối đa `tam` inch) để loại cung đi xuyên nút trên tọa độ thật, không làm tăng giao cắt."""
    ten = {v: k for k, v in idx.items()}
    P = {k: xy[ten[k]] for k in ten}
    h = {k: half[ten[k]] for k in ten}
    goc = dict(P)
    offs = [(i * buoc, j * buoc) for i in range(-4, 5) for j in range(-4, 5) if abs(i * buoc) <= tam and abs(j * buoc) <= tam]
    cur = _chi_phi_inch(P, h, E)[0]
    for _ in range(luot):
        doi = False
        for n in list(P):
            vi_tri = P[n]
            tot = (cur + 0.0, vi_tri)
            for dx, dy in offs:
                P[n] = (goc[n][0] + dx, goc[n][1] + dy)
                v = _chi_phi_inch(P, h, E)[0] + 2.0 * math.hypot(dx, dy)
                if v < tot[0] - 1e-9:
                    tot = (v, P[n])
            P[n] = tot[1]
            if tot[1] != vi_tri:
                doi = True
            cur = _chi_phi_inch(P, h, E)[0]
        if not doi:
            break
    return {ten[k]: P[k] for k in P}


def ve(R, N, entry, fname, so=False):
    """Vẽ một hình đồ thị: so=True là nút tròn ghi số (Hình 3.1); so=False là hộp có tên (Hình 3.2)."""
    _, idx, E, role, loops = doc_do_thi()
    data = json.load(open(CACHE, encoding='utf-8'))
    pos = {int(k): tuple(v) for k, v in data['pos'].items()}
    cols, rows = data['cols'], data['rows']
    xy, half = vi_tri_inch(R, idx, pos, cols, rows, so)
    if not so:
        ten_ = {v: k for k, v in idx.items()}
        cr_ref = kiem_hinh(R, E, idx, *vi_tri_inch(R, idx, pos, cols, rows, False, 2.4))[0]
        for px in [1.4 + 0.05 * i for i in range(0, 21)]:
            xy_t, half_t = vi_tri_inch(R, idx, pos, cols, rows, False, px)
            P_ = {k: xy_t[ten_[k]] for k in ten_}
            h_ = {k: half_t[ten_[k]] for k in ten_}
            tp, cr, ht, ch = _chi_phi_inch(P_, h_, E)
            if ht == 0 and ch == 0 and cr <= cr_ref:
                xy, half = xy_t, half_t
                print(f'{fname}: chọn bề ngang ô lưới {px:.2f} inch')
                break
    cross0, hit0 = kiem_hinh(R, E, idx, xy, half)
    cross, hit = cross0, hit0
    if hit0 > 0:                       # chỉ dịch nút khi còn cung xuyên nút, và chỉ nhận nếu tốt hơn
        xy2 = nudge(R, E, idx, xy, half)
        c2, h2 = kiem_hinh(R, E, idx, xy2, half)
        if (h2, c2) < (hit0, cross0):
            xy, cross, hit = xy2, c2, h2
    print(f'{fname}: trước khi dịch nút: giao cắt {cross0}, xuyên nút {hit0}')
    print(f'{fname}: giao cắt {cross} | cung xuyên nút {hit} (tọa độ thật, đơn vị inch)')
    L = ['digraph G {', '  graph [splines=line, pad=0.25, outputorder=edgesfirst];',
         '  edge [color="#333333", arrowsize=0.9];']
    if so:
        L.append('  node [shape=circle, style=filled, fillcolor="#dae8fc", color="#6c8ebf", fontname="Helvetica", fontsize=20, width=0.62, fixedsize=true];')
    else:
        L.append(f'  node [shape=box, style="filled,rounded", fillcolor="#dae8fc", color="#6c8ebf", fontname="Helvetica", fontsize={CO_CHU_TEN}, margin="0.06,0.05"];')
    for n in R['nodes']:
        k = idx[n]
        x, y = xy[n][0] * 72, xy[n][1] * 72
        extra = ', penwidth=3, color="#d9480f"' if n in entry else ''
        lab = f'{k}' if so else f'{k}\\n{n}'
        L.append(f'  "{n}" [label="{lab}", pos="{x:.1f},{y:.1f}!"{extra}];')
    ten = {v: k for k, v in idx.items()}
    for a, b in E:
        gray = ' [color="#999999"]' if (a, b) in role else ''
        L.append(f'  "{ten[a]}" -> "{ten[b]}"{gray};')
    for k in loops:
        L.append(f'  "{ten[k]}" -> "{ten[k]}";')
    L.append('}')
    base = os.path.join(HINH, fname)
    open(base + '.dot', 'w', encoding='utf-8').write('\n'.join(L))
    fmts = ('png',) if so else ('svg', 'png')
    for fmt in fmts:
        extra = [f'-Gdpi={170 if so else 130}'] if fmt == 'png' else []
        subprocess.run(['neato', '-n', f'-T{fmt}', *extra, base + '.dot', '-o', f'{base}.{fmt}'], check=True)


def main():
    R, idx, E, role, loops = doc_do_thi()
    n_nodes = len(idx)
    if os.environ.get('DOTHI_MOI') or not os.path.exists(CACHE):
        res = tim_bo_cuc(E, n_nodes)
        for best, p, c, r in res[:6]:
            _, cross, hit, ang, ln, rev = chi_phi(p, E, n_nodes, True)
            print(f'lưới {c}x{r}: chi phí {best:.1f} | giao cắt {cross} | xuyên nút {hit} | góc hẹp {ang:.2f} | dài {ln:.1f} | ngược {rev}')
        best, p, c, r = res[0]
        json.dump({'cols': c, 'rows': r, 'cost': best, 'pos': {str(k): list(v) for k, v in p.items()},
                   'ghi_chu': 'Bố cục đồ thị quan hệ; đặt DOTHI_MOI=1 để tìm lại, DOTHI_TINH=1 để tinh chỉnh.'},
                  open(CACHE, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    data = json.load(open(CACHE, encoding='utf-8'))
    pos = {int(k): tuple(v) for k, v in data['pos'].items()}
    if os.environ.get('DOTHI_TINH'):
        pos = tinh_chinh(pos, E, n_nodes, data['cols'], data['rows'])
        data['pos'] = {str(k): list(v) for k, v in pos.items()}
        data['cost'] = chi_phi(pos, E, n_nodes)
        json.dump(data, open(CACHE, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    _, cross, hit, ang, ln, rev = chi_phi(pos, E, n_nodes, True)
    print(f'bố cục đã lưu: lưới {data["cols"]}x{data["rows"]} | giao cắt {cross} | xuyên nút {hit} | góc hẹp {ang:.2f}')


if __name__ == '__main__':
    main()
