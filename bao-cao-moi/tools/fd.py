"""Thư viện phụ thuộc hàm theo bài giảng và giáo trình CSDL-NC (Văn Như Bích): bao đóng, phủ tối thiểu 3 bước,
tìm khóa theo N/TG/D, dạng chuẩn, chiếu PTH, bảo toàn PTH, bảo toàn thông tin (bảng a/b).

Mọi hàm chỉ tính toán; không ghi file. Thuộc tính là chuỗi (ví dụ 'MaSP'); một PTH là (frozenset vế trái, frozenset vế phải).
"""
import itertools


def parse(strs):
    """['A,B -> C,D'] -> [(frozenset({'A','B'}), frozenset({'C','D'}))]"""
    out = []
    for s in strs:
        l, r = s.split('->')
        out.append((frozenset(x.strip() for x in l.split(',')), frozenset(x.strip() for x in r.split(','))))
    return out


def fmt_fd(fd, order=None):
    key = (lambda a: order.index(a)) if order else (lambda a: a)
    return ','.join(sorted(fd[0], key=key)) + ' → ' + ','.join(sorted(fd[1], key=key))


def closure(X, F):
    X = set(X)
    ch = True
    while ch:
        ch = False
        for L, R in F:
            if L <= X and not R <= X:
                X |= R
                ch = True
    return X


def equivalent(F, G):
    return all(R <= closure(L, G) for L, R in F) and all(R <= closure(L, F) for L, R in G)


# ---------------------------------------------------------------- phủ tối thiểu (3 bước của bài giảng)
def min_cover(F, order):
    """Trả về (G, vết). B1 tách vế phải; B2 bỏ thuộc tính thừa ở vế trái (xét theo thứ tự cột); B3 bỏ PTH dư thừa (xét từ PTH cuối lên đầu)."""
    key = lambda a: order.index(a)
    b1 = [(L, frozenset([a])) for L, R in F for a in sorted(R, key=key)]
    trace = dict(b1=b1, b2=[], b3=[])
    G = list(b1)
    for i, (L, R) in enumerate(G):
        L2 = set(L)
        for b in sorted(L, key=key):
            if len(L2) > 1 and R <= closure(L2 - {b}, G):
                trace['b2'].append((fmt_fd((frozenset(L2), R), order), b, fmt_fd((frozenset(L2 - {b}), R), order)))
                L2 -= {b}
        G[i] = (frozenset(L2), R)
    seen, dedup = set(), []
    for fd in G:                      # PTH trùng nhau sau B2 chỉ giữ một
        if fd in seen:
            trace['b3'].append((fmt_fd(fd, order), 'trùng với một PTH đã có'))
            continue
        seen.add(fd)
        dedup.append(fd)
    G = dedup
    i = len(G) - 1                    # xét từ PTH cuối lên đầu để ưu tiên giữ các PTH của khóa chính
    while i >= 0:
        rest = G[:i] + G[i + 1:]
        cl = closure(G[i][0], rest)
        if G[i][1] <= cl:
            trace['b3'].append((fmt_fd(G[i], order), 'bỏ nó vẫn có ' + ('(%s)' if len(G[i][0]) > 1 else '%s') % ','.join(sorted(G[i][0], key=key)) + '⁺ ∋ ' + ','.join(sorted(G[i][1]))))
            G = rest
        i -= 1
    trace['b3'].reverse()
    return G, trace


# ---------------------------------------------------------------- khóa (N, TG, D)
def keys_ntd(attrs, G):
    key = lambda a: attrs.index(a)
    lhs = set().union(*[L for L, _ in G]) if G else set()
    rhs = set().union(*[R for _, R in G]) if G else set()
    N = [a for a in attrs if a not in rhs]
    TG = [a for a in attrs if a in rhs and a in lhs]
    D = [a for a in attrs if a in rhs and a not in lhs]
    U = set(attrs)
    rows, keys = [], []
    for r in range(len(TG) + 1):
        for c in itertools.combinations(TG, r):
            K = set(N) | set(c)
            cl = closure(K, G)
            if cl == U:
                status = 'siêu khóa' if any(set(k) < K for k in keys) else 'khóa'
                if status == 'khóa':
                    keys.append(tuple(sorted(K, key=key)))
            else:
                status = 'không'
            rows.append((c, tuple(sorted(K, key=key)), tuple(sorted(cl, key=key)), status))
    n_closure = closure(set(N), G)
    return dict(N=N, TG=TG, D=D, rows=rows, keys=keys, unique=(n_closure == U))


# ---------------------------------------------------------------- dạng chuẩn
def normal_form(attrs, G, keys, extra_1nf_violations=None):
    """Dạng chuẩn 1..4 (4 = BCNF) của quan hệ theo F = G; giải thích bằng chuỗi. extra_1nf_violations: danh sách thuộc tính kép."""
    U = set(attrs)
    prime = set().union(*[set(k) for k in keys])
    nonprime = [a for a in attrs if a not in prime]
    partial = []          # (tập con thật sự của khóa, thuộc tính không khóa phụ thuộc)
    for k in keys:
        for r in range(1, len(k)):
            for sub in itertools.combinations(k, r):
                got = [a for a in nonprime if a in closure(sub, G) and a not in sub]
                if got:
                    partial.append((sub, k, got))
    viol3, violbc = [], []
    for L, R in G:
        for a in R:
            if a in L or closure(L, G) == U:
                continue
            violbc.append((tuple(sorted(L)), a))
            if a not in prime:
                viol3.append((tuple(sorted(L)), a))
    if extra_1nf_violations:
        nf = 0
    elif partial:
        nf = 1
    elif viol3:
        nf = 2
    elif violbc:
        nf = 3
    else:
        nf = 4
    return dict(prime=sorted(prime, key=attrs.index), nonprime=nonprime, partial=partial, viol3=viol3, violbc=violbc,
                nf=nf)


NF_NAME = {0: 'chưa đạt 1NF', 1: '1NF', 2: '2NF', 3: '3NF', 4: 'BCNF'}


# ---------------------------------------------------------------- chiếu PTH, bảo toàn PTH
def project(F, Q, order, maxlhs=3):
    """PTH chiếu lên tập thuộc tính Q (vế trái tối đa maxlhs thuộc tính), rút gọn bằng phủ tối thiểu."""
    Qs = sorted(Q, key=order.index)
    out = []
    for r in range(1, min(maxlhs, len(Qs)) + 1):
        for X in itertools.combinations(Qs, r):
            ext = (closure(X, F) & set(Q)) - set(X)
            if ext:
                out.append((frozenset(X), frozenset(ext)))
    if not out:
        return []
    G, _ = min_cover(out, order)
    return G


def preservation(F, comps, order):
    """comps: {tên: tập thuộc tính}. Trả (F', các PTH của F không suy ra từ F')."""
    Fp = []
    for Q in comps.values():
        Fp += project(F, Q, order)
    lost = [(L, a) for L, R in F for a in R if a not in closure(L, Fp)]
    return Fp, lost


def chase(U, comps, F):
    """Bảng a/b của giáo trình (Bài 6): trả về (bảng đầu, các bước, bảng cuối, có dòng toàn a)."""
    cols = list(U)
    rows, nb = {}, 0
    for name, Q in comps.items():
        row = {}
        for c in cols:
            if c in Q:
                row[c] = 'a:' + c
            else:
                nb += 1
                row[c] = f'b{nb}'
        rows[name] = row
    first = {k: dict(v) for k, v in rows.items()}
    steps = []
    ch = True
    while ch:
        ch = False
        for L, R in F:
            for i, j in itertools.combinations(list(rows), 2):
                if all(rows[i][x] == rows[j][x] for x in L):
                    for y in sorted(R, key=cols.index):
                        u, v = rows[i][y], rows[j][y]
                        if u == v:
                            continue
                        if u.startswith('a:'):
                            old, new = v, u
                        elif v.startswith('a:'):
                            old, new = u, v
                        else:
                            old, new = (v, u) if int(v[1:]) > int(u[1:]) else (u, v)
                        for nm in rows:
                            for c in cols:
                                if rows[nm][c] == old:
                                    rows[nm][c] = new
                        steps.append((i, j, tuple(sorted(L, key=cols.index)), y, old, new))
                        ch = True
    ok = any(all(v.startswith('a:') for v in row.values()) for row in rows.values())
    return first, steps, rows, ok
