"""Tìm khóa theo thuật toán N, M, D của bài giảng và đối chiếu bằng duyệt mọi tập con (mục 5).

Chạy:  python3 bao-cao/tools/timkhoa.py
Dùng phủ tối thiểu G tính bằng mincover.py (cùng thư mục) cho 11 quan hệ có F nhiều PTH.
Chỉ đọc, không ghi file.
"""
import itertools
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mincover import RELATIONS, closure, drop_extra_lhs, drop_redundant, parse, split_rhs

ORDER = list('ABCDEGHIKLMNOPQR')


def analyse(fds):
    G, _ = drop_redundant(drop_extra_lhs(split_rhs(parse(fds))))
    U = set().union(*[L | R for L, R in G])
    lhs = set().union(*[L for L, _ in G])
    rhs = set().union(*[R for _, R in G])
    N = [a for a in ORDER if a in U and a in lhs and a not in rhs]
    M = [a for a in ORDER if a in U and a in lhs and a in rhs]
    D = [a for a in ORDER if a in U and a in rhs and a not in lhs]
    # khóa theo N, M
    supers = []
    for r in range(len(M) + 1):
        for c in itertools.combinations(M, r):
            K = set(N) | set(c)
            if closure(K, G) == U:
                supers.append(frozenset(K))
    keys_nm = {k for k in supers if not any(s < k for s in supers)}
    # khóa theo duyệt toàn bộ tập con
    attrs = [a for a in ORDER if a in U]
    keys_bf = []
    for r in range(1, len(attrs) + 1):
        for c in itertools.combinations(attrs, r):
            if not any(set(k) <= set(c) for k in keys_bf) and closure(c, G) == U:
                keys_bf.append(c)
    return N, M, D, keys_nm, {frozenset(k) for k in keys_bf}, len(supers)


if __name__ == '__main__':
    for name, fds in RELATIONS.items():
        N, M, D, k1, k2, ns = analyse(fds)
        fmt = lambda ks: sorted(''.join(a for a in ORDER if a in k) for k in ks)
        print(f"{name:18s} N={''.join(N) or '∅':3s} M={''.join(M):8s} D={''.join(D):14s} "
              f"siêu khóa(N∪M)={ns:3d} khóa={fmt(k1)}  trùng duyệt toàn bộ={k1 == k2}")
