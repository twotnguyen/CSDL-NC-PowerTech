#!/usr/bin/env python3
"""Mục 10: biểu diễn lược đồ 39 quan hệ thành đồ thị quan hệ (thuật toán B1-B7, Bài 10 giáo trình 2015).

Chạy:  python3 bao-cao/tools/dothi.py
Đầu vào: luoc_do_39.py (khóa chính, khóa ngoại, cột cho phép rỗng, bản số; sinh từ lược đồ mục 7 sau các thay đổi của mục 9).
Quy ước áp dụng (xem 10.3 trong báo cáo):
  - Mỗi quan hệ dùng khóa chính làm khóa ưu tiên (giáo trình 10.4.2).
  - Hai cột là cùng một thuộc tính khi chúng nối với nhau bằng khóa ngoại; trừ ba trường hợp là vai trò riêng:
    khóa ngoại tới NHANVIEN (không thuộc khóa chính), HOSODOITRA.MaKH và PHIEUBAOHANH.MaKH.
  - Cung A -> B bị coi là thừa (PTH_Thừa) khi B đạt được qua cung A -> H và đường đó bắt buộc
    (không rỗng) hoặc khóa của B nằm trong khóa của H.
"""
import os, sys
from itertools import combinations
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from luoc_do_39 import ATTRS, NULLS, KEY, FKS, CARD, GROUPS


def is_role(rel, cols, tgt):
    if tgt == 'NHANVIEN' and not set(cols) <= set(KEY[rel]):
        return True
    return rel in ('HOSODOITRA', 'PHIEUBAOHANH') and tgt == 'KHACHHANG'


def run():
    parent = {}

    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for r in ATTRS:
        for c in ATTRS[r]:
            find((r, c))
    roles = set()
    for rel, cols, tgt, tcols, tag in FKS:
        if rel == tgt:
            continue
        if is_role(rel, cols, tgt):
            roles.add((rel, tuple(cols), tgt))
            continue
        for c, tc in zip(cols, tcols):
            parent[find((rel, c))] = find((tgt, tc))
    cls = lambda r, c: find((r, c))
    Q = {r: frozenset(cls(r, c) for c in ATTRS[r]) for r in ATTRS}
    K = {r: frozenset(cls(r, c) for c in KEY[r]) for r in ATTRS}
    # ---- B1.1: gộp quan hệ có khóa tương đương ----
    byk = {}
    for r in ATTRS:
        byk.setdefault(K[r], []).append(r)
    node_of, nodes = {}, []
    for r in ATTRS:
        if r in node_of:
            continue
        mem = byk[K[r]]
        for m in mem:
            node_of[m] = mem[0]
        nodes.append(mem[0])
    members = {n: [r for r in ATTRS if node_of[r] == n] for n in nodes}
    NQ = {n: frozenset().union(*[Q[m] for m in members[n]]) for n in nodes}
    NK = {n: K[members[n][0]] for n in nodes}
    label = {}
    for n in nodes:
        for m in members[n]:
            for c in ATTRS[m]:
                label.setdefault(cls(m, c), c)
    # cột rỗng được theo lớp thuộc tính của từng nút
    def nullable_cols(n, klass):
        cols = [(m, c) for m in members[n] for c in ATTRS[m] if cls(m, c) == klass]
        return any(c in NULLS[m] for m, c in cols)
    # ---- B3: nút bản lề ----
    F = [(NK[n], NQ[n]) for n in nodes]

    def closure(X):
        X = set(X)
        ch = True
        while ch:
            ch = False
            for l, rr in F:
                if l <= X and not rr <= X:
                    X |= rr
                    ch = True
        return X

    def keys_of(S):
        res = []
        for k in range(1, len(S) + 1):
            for X in combinations(sorted(S, key=str), k):
                X = frozenset(X)
                if S <= closure(X) and not any(rr <= X for rr in res):
                    res.append(X)
        return res
    pairs, hinge_nodes, b3 = 0, [], []
    for i, j in combinations(sorted(nodes), 2):
        S = set(NQ[i] & NQ[j])
        if S:
            pairs += 1
        while S:
            ks = keys_of(S)
            match = [h for h in nodes if NK[h] in ks]
            b3.append((i, j, sorted(label[c] for c in S), [sorted(label[c] for c in k) for k in ks], match))
            if not match:
                hinge_nodes.append((i, j, frozenset(set().union(*ks))))
            S -= set().union(*ks)
    hinge = {}
    for i, j, kk in hinge_nodes:
        name = 'BL(' + ', '.join(sorted(label[c] for c in kk)) + ')'
        hinge[name] = kk
    for name, kk in hinge.items():
        nodes.append(name)
        members[name] = []
        NQ[name] = kk
        NK[name] = kk
    # ---- B4: cung ----
    decl = {}
    for rel, cols, tgt, tcols, tag in FKS:
        if rel == tgt:
            continue
        i, j = node_of[rel], node_of[tgt]
        if i != j:
            decl.setdefault(i, []).append((j, (rel, tuple(cols), tgt, tag)))
    res = {}
    for i in nodes:
        pth = {}
        for j, fk in decl.get(i, []):
            pth.setdefault(j, []).append(fk)
        for j in nodes:
            if j != i and j not in pth and NK[j] <= NQ[i]:
                pth[j] = [('ngầm', None, j, None)]

        def mandatory(h):
            if h in hinge:
                return all(not nullable_cols(i, k) for k in NK[h])
            return all(not nullable_cols(i, k) for k in NK[h])
        thua = set()
        for j in pth:
            if all(fk[0] != 'ngầm' and (fk[0], fk[1], fk[2]) in roles for fk in pth[j]):
                continue
            for h in pth:
                if h != j and NK[j] <= NQ[h] and (mandatory(h) or NK[j] <= NK[h]):
                    thua.add(j)
        lk = {j for j in nodes if j != i and NK[j] <= NK[i]}
        lk_thua = {j for j in lk if any(h != j and NK[j] <= NK[h] for h in lk)}
        cung = (set(pth) - thua) | (lk - lk_thua)
        res[i] = dict(pth=pth, thua=thua, lk=lk, lk_thua=lk_thua, cung=cung)
    # ---- B5: hủy nút bản lề thừa (một cung vào, không thuộc tính ngoài khóa) ----
    removed_hinge = []
    for name in list(hinge):
        incoming = [i for i in nodes if name in res[i]['cung']]
        if len(incoming) == 1:
            removed_hinge.append(name)
    # ---- B7: cung vô hướng ----
    undirected = []
    for k in nodes:
        if k in hinge or len(members[k]) != 1:
            continue
        m = members[k][0]
        nonkey = [c for c in ATTRS[m] if c not in KEY[m]]
        incoming = [i for i in nodes if k in res[i]['cung']]
        if not nonkey and len(res[k]['cung']) == 2 and not incoming:
            a, b = sorted(res[k]['cung'])
            if NK[k] == (NK[a] | NK[b]):
                undirected.append((k, a, b))
    return dict(nodes=nodes, members=members, node_of=node_of, res=res, hinge=hinge, hinge_nodes=hinge_nodes,
                pairs=pairs, b3=b3, undirected=undirected, removed_hinge=removed_hinge, NK=NK, NQ=NQ, label=label,
                roles=roles, cls=cls, Q=Q, K=K)


def arcs(R):
    """Danh sách cung của đồ thị quan hệ: (từ, đến, loại, khóa ngoại, xuôi, ngược)."""
    out = []
    und = {k for k, a, b in R['undirected']}
    for i in R['nodes']:
        if i in und:
            continue
        x = R['res'][i]
        for j in sorted(x['cung']):
            fks = x['pth'].get(j, [])
            kind = 'PTH' if j in x['pth'] and j not in x['thua'] else 'lồng khóa'
            if j in x['pth'] and j not in x['thua'] and j in x['lk']:
                kind = 'PTH, lồng khóa'
            if not fks:
                out.append((i, j, kind, None))
            for fk in fks:
                out.append((i, j, kind, fk))
    return out


def mach_di_kep(R, maxlen=4):
    """Các cặp (nút gốc, nút đích) có từ hai mạch đi khác nhau (không đi qua cung vai trò), độ dài tối đa maxlen nút."""
    adj = {}
    for i, j, kind, fk in arcs(R):
        role = fk[0] != 'ngầm' and (fk[0], fk[1], fk[2]) in R['roles']
        if not role:
            adj.setdefault(i, []).append(j)
    found = []

    def dfs(src, n, path, acc):
        if len(path) >= maxlen:
            return
        for j in adj.get(n, []):
            if j not in path:
                acc.setdefault(j, []).append(path + [j])
                dfs(src, j, path + [j], acc)
    for s in R['nodes']:
        acc = {}
        dfs(s, s, [s], acc)
        for t, ps in acc.items():
            if len(ps) > 1:
                found.append((s, t, ps))
    return found


if __name__ == '__main__':
    R = run()
    print('nút:', len(R['nodes']), '| cặp quan hệ có giao khác rỗng:', R['pairs'])
    print('gộp B1.1:', [v for v in R['members'].values() if len(v) > 1])
    print('nút bản lề:', list(R['hinge']))
    print('bị hủy ở B5:', R['removed_hinge'])
    print('cung vô hướng (B7):', R['undirected'])
    for i in R['nodes']:
        x = R['res'][i]
        print(f"{i}: PTH={sorted(x['pth'])} thừa={sorted(x['thua'])} LK={sorted(x['lk'])} cung={sorted(x['cung'])}")
    A = arcs(R)
    print('số cung (kể cả cung song song theo vai trò):', len(A))
    for src, dst, ps in mach_di_kep(R):
        print('mạch đi kép:', src, '->', dst, ' | '.join('→'.join(p) for p in ps))
