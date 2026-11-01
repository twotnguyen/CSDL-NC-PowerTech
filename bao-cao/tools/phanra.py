"""Kiểm tra phép phân rã: bảo toàn thông tin (tableau/chase) và bảo toàn phụ thuộc hàm (mục 9).

Chạy:  python3 bao-cao/tools/phanra.py
Với mỗi phép tách trong DEC: tính PTH chiếu Fi lên từng quan hệ con, kiểm tra
F' = ∪Fi ⊆ F⁺ và F ⊆ F'⁺ (bảo toàn PTH), chạy tableau (bảo toàn thông tin), tìm khóa
và dạng chuẩn của từng quan hệ con. Chỉ đọc, không ghi file.
"""
import itertools
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mincover import closure, drop_extra_lhs, drop_redundant, parse, split_rhs

# Chữ cái đặt tên như mục 4; F là phủ tối thiểu G
REL = {
    'CHITIETTRA': dict(U='ABCDE', F=['A,C->D', 'A,C->E', 'A->B']),
    'PHIEUBAOHANH': dict(U='ABCDEGHIKLMNOPQ', F=['A->B,D,E,G,H,I,K,L,M,N,O,P,Q', 'E,G->C', 'D->C']),
    'HANGCOSERI': dict(U='ABCDEGHIK', F=['A->B,D,E,G,H,I,K', 'C,B->A', 'D,E->C', 'G,H->C']),
    'HANGCOSERI_seri_toan_cuc': dict(U='ABCDEGHIK', F=['A->B,D,E,G,H,I,K', 'B->A', 'D,E->C', 'G,H->C']),
}
# Các phép tách (tên: quan hệ gốc, {quan hệ con: thuộc tính})
DEC = {
    'CHITIETTRA | phân rã': ('CHITIETTRA', {'Q1': 'AB', 'Q2': 'ACDE'}),
    'PHIEUBAOHANH | phân rã (Delobel)': ('PHIEUBAOHANH', {'Q1': 'DC', 'Q2': 'ABDEGHIKLMNOPQ'}),
    'PHIEUBAOHANH | tổng hợp (Bernstein)': ('PHIEUBAOHANH', {'R1': 'ABDEGHIKLMNOPQ', 'R2': 'EGC', 'R3': 'DC'}),
    'HANGCOSERI | phân rã (Delobel)': ('HANGCOSERI', {'Q1': 'DEC', 'Q2': 'ABDEGHIK'}),
    'HANGCOSERI | phương án C (bốn thành phần)': ('HANGCOSERI', {'Q1': 'DEC', 'Q2': 'GHC', 'Q3': 'ADEGHIK', 'Q4': 'ABC'}),
    'HANGCOSERI | tách BCNF khi seri duy nhất toàn cửa hàng': ('HANGCOSERI_seri_toan_cuc', {'Q1': 'DEC', 'Q2': 'ABDEGHIK'}),
    'HANGCOSERI | seri duy nhất toàn cửa hàng, ba thành phần': ('HANGCOSERI_seri_toan_cuc', {'Q1': 'DEC', 'Q2': 'GHC', 'Q3': 'ABDEGHIK'}),
}


def fds(strs):
    return parse(strs)


def project(F, Q, maxsize=3):
    """PTH chiếu lên tập thuộc tính Q (X tối đa maxsize thuộc tính), rút gọn thành phủ tối thiểu."""
    Q = sorted(Q)
    out = []
    for r in range(1, min(maxsize, len(Q)) + 1):
        for X in itertools.combinations(Q, r):
            ext = (closure(X, F) & set(Q)) - set(X)
            if ext:
                out.append((frozenset(X), frozenset(ext)))
    if not out:
        return []
    G, _ = drop_redundant(drop_extra_lhs(split_rhs(out)))
    return G


def preserved(F, comps):
    Fp = [fd for Q in comps.values() for fd in project(F, Q)]
    lost = [fd for fd in F for a in fd[1] if a not in closure(fd[0], Fp)]
    return not lost, Fp, lost


def chase(U, comps, F):
    """Trả về (bảng đầu, các bước, bảng cuối, có dòng toàn a không)."""
    cols = list(U)
    rows = {}
    nb = 0
    for name, Q in comps.items():
        row = {}
        for c in cols:
            if c in Q:
                row[c] = 'a' + c
            else:
                nb += 1
                row[c] = f'b{nb}'
        rows[name] = row
    first = {k: dict(v) for k, v in rows.items()}
    steps = []
    changed = True
    while changed:
        changed = False
        for L, R in F:
            names = list(rows)
            for i, j in itertools.combinations(names, 2):
                if all(rows[i][x] == rows[j][x] for x in L):
                    for y in R:
                        u, v = rows[i][y], rows[j][y]
                        if u == v:
                            continue
                        if u.startswith('a'):
                            old, new = v, u
                        elif v.startswith('a'):
                            old, new = u, v
                        else:
                            old, new = (v, u) if int(v[1:]) > int(u[1:]) else (u, v)
                        for nm in rows:
                            for c in cols:
                                if rows[nm][c] == old:
                                    rows[nm][c] = new
                        steps.append((i, j, ','.join(sorted(L)), y, old, new))
                        changed = True
    ok = any(all(v.startswith('a') for v in row.values()) for row in rows.values())
    return first, steps, rows, ok


def keys_of(attrs, F):
    U = set(attrs)
    keys = []
    for r in range(1, len(attrs) + 1):
        for c in itertools.combinations(sorted(attrs), r):
            if not any(set(k) <= set(c) for k in keys) and closure(c, F) == U:
                keys.append(c)
    return keys


def is_bcnf(Q, Fi):
    keys = keys_of(Q, Fi)
    return all(closure(L, Fi) >= set(Q) for L, R in Fi), keys


if __name__ == '__main__':
    for label, (rel, comps) in DEC.items():
        U, F = REL[rel]['U'], fds(REL[rel]['F'])
        ok_pres, Fp, lost = preserved(F, comps)
        first, steps, final, ok_ll = chase(U, comps, F)
        bc = {}
        for n, Q in comps.items():
            Fi = project(F, Q)
            b, keys = is_bcnf(Q, Fi)
            bc[n] = ('BCNF' if b else 'không BCNF', [''.join(k) for k in keys])
        print(f"{label}\n   bảo toàn thông tin={ok_ll}  bảo toàn PTH={ok_pres}  mất={[','.join(sorted(a))+'->'+','.join(sorted(b)) for a,b in lost]}\n   {bc}")
