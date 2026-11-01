#!/usr/bin/env python3
"""Biểu diễn lược đồ sau cải tiến thành đồ thị quan hệ theo thuật toán B1-B7 (Bài 10, giáo trình CSDL-NC 2015).

Chạy:  python3 tools/dothi.py      (in tóm tắt; chương 3 sinh bằng tools/gen_chuong3.py từ module này)
Quy ước áp dụng (nêu trong chương 3):
  Q1. Mỗi quan hệ dùng khóa chính làm khóa ưu tiên (giáo trình 10.4.2).
  Q2. Hai cột là cùng một thuộc tính khi nối nhau bằng khóa ngoại, trừ khóa ngoại tới NHANVIEN không thuộc khóa chính
      (nhân viên lập, xác nhận, giao... là các vai trò khác nhau): cung của vai trò luôn được giữ, không bị coi là thừa.
  Q3. Cung A -> B bị coi là thừa (PTH_Thừa) khi B đạt được qua cung A -> H và đường đó bắt buộc
      (không rỗng) hoặc khóa của B nằm trong khóa của H.
"""
import os
import sys
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import luoc_do

R_IMP = luoc_do.improved()
ORDER = luoc_do.ORDER_IMPROVED
ATTRS = {n: [a[0] for a in R_IMP[n]['attrs']] for n in ORDER}
NULLS = {n: [a[0] for a in R_IMP[n]['attrs'] if a[2] == 'NULL'] for n in ORDER}
KEY = {n: list(R_IMP[n]['pk']) for n in ORDER}
FKS = []
for n in ORDER:
    for cols, parent, pcols in R_IMP[n]['fks']:
        # khóa ngoại phụ tới NHANVIEN (MaNVDuyet, MaNVChi...) ghi thêm một vai trò khác của nhân viên; không vẽ thành cung riêng
        if parent == 'NHANVIEN' and list(cols) != list(R_IMP['NHANVIEN']['pk']) and cols[0] != 'MaNV':
            continue
        FKS.append((n, list(cols), parent, list(pcols)))
UNIQUE_FK = {('PHIEUGIAO', ('MaDH',)), ('TAIKHOAN', ('MaKH',)), ('TAIKHOAN', ('MaNV',))}          # khóa ngoại có ràng buộc UNIQUE: cha có tối đa một con
REQUIRE_CHILD = {('CHITIETDONHANG', ('MaDH',)), ('CHITIETPHIEUNHAP', ('MaPN',)), ('CHITIETTRA', ('MaHS',))}
MAX_CHILD = {('LANGIAO', ('MaGiao',)): '3'}


def card_of(rel, cols, parent):
    """Bản số (min, trung bình, max) đi xuôi từ con sang cha và đi ngược từ cha sang con."""
    cols = tuple(cols)
    opt = any(c in NULLS[rel] for c in cols)
    fwd = ('0', '-', '1') if opt else ('1', '1', '1')
    mn = '1' if (rel, cols) in REQUIRE_CHILD else '0'
    mx = '1' if (rel, cols) in UNIQUE_FK else MAX_CHILD.get((rel, cols), 'n')
    return fwd, (mn, '-', mx)


def is_role(rel, cols, tgt):
    return tgt == 'NHANVIEN' and not set(cols) <= set(KEY[rel])


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
    for rel, cols, tgt, tcols in FKS:
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
    # ---- B1.1: gộp các quan hệ có khóa tương đương ----
    byk = {}
    for r in ORDER:
        byk.setdefault(K[r], []).append(r)
    node_of, nodes = {}, []
    for r in ORDER:
        if r in node_of:
            continue
        mem = byk[K[r]]
        for m in mem:
            node_of[m] = mem[0]
        nodes.append(mem[0])
    members = {n: [r for r in ORDER if node_of[r] == n] for n in nodes}
    NQ = {n: frozenset().union(*[Q[m] for m in members[n]]) for n in nodes}
    NK = {n: K[members[n][0]] for n in nodes}
    label = {}
    for n in nodes:
        for m in members[n]:
            for c in ATTRS[m]:
                label.setdefault(cls(m, c), c)

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
    for i, j in combinations(nodes, 2):
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
        hinge['BL(' + ', '.join(sorted(label[c] for c in kk)) + ')'] = kk
    for name, kk in hinge.items():
        nodes.append(name)
        members[name] = []
        NQ[name] = kk
        NK[name] = kk
    # ---- B4: cung ----
    decl = {}
    selfloops = []
    for rel, cols, tgt, tcols in FKS:
        i, j = node_of[rel], node_of[tgt]
        if rel == tgt:
            selfloops.append((rel, cols, tgt, tcols))
            continue
        if i != j:
            decl.setdefault(i, []).append((j, (rel, tuple(cols), tgt)))
    res = {}
    for i in nodes:
        pth = {}
        for j, fk in decl.get(i, []):
            pth.setdefault(j, []).append(fk)
        for j in nodes:
            if j != i and j not in pth and NK[j] <= NQ[i]:
                pth[j] = [('ngầm', None, j)]

        def mandatory(h):
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
    removed_hinge = []
    for name in list(hinge):
        incoming = [i for i in nodes if name in res[i]['cung']]
        if len(incoming) == 1:
            removed_hinge.append(name)
    undirected = []
    for k in nodes:
        if k in hinge or len(members[k]) != 1:
            continue
        m = members[k][0]
        nonkey = [c for c in ATTRS[m] if c not in KEY[m]]
        incoming = [i for i in nodes if k in res[i]['cung']]
        if not nonkey and len(res[k]['cung']) == 2 and not incoming:
            a, b = sorted(res[k]['cung'], key=nodes.index)
            if NK[k] == (NK[a] | NK[b]):
                undirected.append((k, a, b))
    return dict(nodes=nodes, members=members, node_of=node_of, res=res, hinge=hinge, hinge_nodes=hinge_nodes,
                pairs=pairs, b3=b3, undirected=undirected, removed_hinge=removed_hinge, NK=NK, NQ=NQ, label=label,
                roles=roles, cls=cls, Q=Q, K=K, selfloops=selfloops)


def arcs(R):
    """Danh sách cung có hướng: (từ, đến, loại, khóa ngoại hoặc None, bản số xuôi, bản số ngược)."""
    out = []
    und = {k for k, a, b in R['undirected']}
    for i in R['nodes']:
        if i in und:
            continue
        x = R['res'][i]
        for j in sorted(x['cung'], key=R['nodes'].index):
            fks = x['pth'].get(j, [])
            kind = 'PTH' if j in x['pth'] and j not in x['thua'] else 'lồng khóa'
            if j in x['pth'] and j not in x['thua'] and j in x['lk']:
                kind = 'PTH, lồng khóa'
            if not fks:
                out.append((i, j, kind, None, ('1', '1', '1'), ('0', '-', 'n')))
            for fk in fks:
                if fk[0] == 'ngầm':
                    out.append((i, j, kind, None, ('1', '1', '1'), ('0', '-', 'n')))
                else:
                    f, b = card_of(fk[0], fk[1], fk[2])
                    out.append((i, j, kind, fk, f, b))
    for rel, cols, tgt, tcols in R['selfloops']:
        f, b = card_of(rel, cols, tgt)
        out.append((R['node_of'][rel], R['node_of'][tgt], 'khuyên', (rel, tuple(cols), tgt), f, b))
    return out


if __name__ == '__main__':
    R = run()
    print('nút:', len(R['nodes']), '| cặp quan hệ có giao khác rỗng:', R['pairs'])
    print('gộp B1.1:', [v for v in R['members'].values() if len(v) > 1])
    print('nút bản lề:', list(R['hinge']), '| bị hủy ở B5:', R['removed_hinge'])
    print('cung vô hướng (B7):', R['undirected'])
    for i in R['nodes']:
        x = R['res'][i]
        print(f"{i}: PTH={sorted(x['pth'])} thừa={sorted(x['thua'])} LK={sorted(x['lk'])} cung={sorted(x['cung'])}")
    A = arcs(R)
    print('số cung có hướng (kể cả song song theo vai trò, khuyên):', len(A))
