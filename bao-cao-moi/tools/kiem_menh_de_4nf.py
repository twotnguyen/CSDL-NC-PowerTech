# Thử mệnh đề: Q đạt BCNF, X ->> Y không hiển nhiên, X không siêu khóa => mọi khóa có thuộc tính ở cả Y\X và Z
import random, itertools
U = 'ABCD'; I = dict(zip(U, range(4)))
def subs(s):
    return [frozenset(c) for r in range(len(s) + 1) for c in itertools.combinations(s, r)]
ALL = subs(U)
def fd(r, X, a):
    d = {}
    for t in r:
        k = tuple(t[I[x]] for x in sorted(X))
        if d.setdefault(k, t[I[a]]) != t[I[a]]: return False
    return True
def sk(r, X): return all(fd(r, X, a) for a in U)
def mvd(r, X, Y):
    Z = set(U) - X - Y; s = set(r)
    for a in r:
        for b in r:
            if all(a[I[x]] == b[I[x]] for x in X):
                t = tuple(a[i] if U[i] in X or U[i] in Y else b[i] for i in range(4))
                if t not in s: return False
    return True
random.seed(1); n = kq = 0
for _ in range(300000):
    # thường xuyên dựng tích chéo để có phụ thuộc đa trị thật
    if random.random() < .5:
        xs = random.sample(range(2), 2); r = {(random.randrange(2), random.randrange(2), random.randrange(2), random.randrange(2)) for _ in range(random.randint(2, 7))}
    else:
        p = [(random.randrange(2),) for _ in range(1)]; ys = {(random.randrange(3), random.randrange(2)) for _ in range(3)}; zs = {random.randrange(3) for _ in range(2)}
        r = {(p[0][0], y[0], y[1], z) for y in ys for z in zs}
    r = list(r)
    keys = [K for K in ALL if sk(r, K) and not any(sk(r, K - {a}) for a in K)]
    if any(not sk(r, X) and not a in X and fd(r, X, a) for X in ALL for a in U): continue   # không BCNF
    for X in ALL:
        if sk(r, X): continue
        for Y in subs(set(U) - X):
            Z = set(U) - X - Y
            if not Y or not Z or not mvd(r, X, Y): continue
            n += 1
            for K in keys:
                assert K & Y and K & Z, (r, X, Y, K)
print('so truong hop MVD khong hien nhien trong quan he BCNF:', n, 'khong co phan vi du')
