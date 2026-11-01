"""Phủ tối thiểu theo 3 bước của bài giảng; dùng để đối chiếu lời giải tay ở mục 4.

Chạy:  python3 bao-cao/tools/mincover.py
In ra, với mỗi quan hệ có F nhiều hơn một PTH: số PTH sau B1, PTH bị loại ở B3,
kích thước phủ, F ≡ G, và số phủ khác nhau khi thử nhiều thứ tự xét B3.
Chỉ đọc, không ghi file.
"""
import random


def closure(X, F):
    X = set(X)
    changed = True
    while changed:
        changed = False
        for L, R in F:
            if L <= X and not R <= X:
                X |= R
                changed = True
    return X


def parse(fds):
    F = []
    for s in fds:
        L, R = s.split('->')
        F.append((frozenset(L.strip().split(',')), frozenset(R.strip().split(','))))
    return F


def split_rhs(F):                                   # B1
    return [(L, frozenset([a])) for L, R in F for a in sorted(R)]


def drop_extra_lhs(G):                              # B2
    out = []
    for L, R in G:
        L2 = set(L)
        for b in sorted(L):
            if len(L2) > 1 and R <= closure(L2 - {b}, G):
                L2 -= {b}
        out.append((frozenset(L2), R))
    return out


def drop_redundant(G):                              # B3
    G = list(G)
    removed = []
    i = 0
    while i < len(G):
        rest = G[:i] + G[i + 1:]
        if G[i][1] <= closure(G[i][0], rest):
            removed.append(G[i])
            G = rest
        else:
            i += 1
    return G, removed


def equivalent(F1, F2):
    return (all(R <= closure(L, F2) for L, R in F1) and
            all(R <= closure(L, F1) for L, R in F2))


def fmt(fd):
    return f"{','.join(sorted(fd[0]))}->{','.join(sorted(fd[1]))}"


RELATIONS = {
    'MATHANG': ['A->B,C,D,E,G,H,I,K,L,M', 'B->A'],
    'ANHMATHANG': ['A->B,C,D,E,G', 'B,C->A', 'B,D->A'],
    'DINHNGHIATHONGSO': ['A->B,C,D,E,G', 'B,C->A'],
    'DONHANG': ['A->B,C,D,E,G,H,I,K,L,M,N,O,P,Q,R', 'B->A'],
    'PHIEUNHAP': ['A->B,C,D,E,G,H,I', 'B->A'],
    'THANHTOAN': ['A->B,C,D,E,G,H,I,K,L', 'K,I->A'],
    'MAGIAMGIA': ['A->B,C,D,E,G,H,I,K,L', 'B->A'],
    'TAIKHOAN': ['A->B,C,D,E,G', 'B->A'],
    'HANGCOSERI': ['A->B,C,D,E,G,H,I,K', 'C,B->A', 'D,E->C', 'G,H->C'],
    'PHIEUBAOHANH': ['A->B,C,D,E,G,H,I,K,L,M,N,O,P,Q', 'E,G->C', 'D->C'],
    'PHIEUGIAO': ['A->B,C,D,E', 'B->A'],
    'CHITIETTRA': ['A,B,C->D,E', 'A->B'],
}

if __name__ == '__main__':
    random.seed(1)
    for name, fds in RELATIONS.items():
        F = parse(fds)
        b1 = split_rhs(F)
        b2 = drop_extra_lhs(b1)
        G, removed = drop_redundant(b2)
        seen = set()
        for _ in range(300):
            T = b2[:]
            random.shuffle(T)
            seen.add(frozenset(fmt(x) for x in drop_redundant(T)[0]))
        print(f"{name:18s} B1={len(b1):2d} B2 đổi={sum(x != y for x, y in zip(b1, b2))} "
              f"B3 loại={[fmt(r) for r in removed]} |G|={len(G):2d} "
              f"F≡G={equivalent(F, G)} số phủ khác nhau={len(seen)}")
