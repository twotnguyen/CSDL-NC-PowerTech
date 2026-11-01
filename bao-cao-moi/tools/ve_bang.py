#!/usr/bin/env python3
"""Sơ đồ quan hệ dạng bảng (kiểu Toad Data Modeler trong báo cáo mẫu) và sơ đồ lớp (Class Diagram) vẽ bằng Graphviz từ lược đồ sau cải tiến."""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import erd
import luoc_do

HINH = os.path.join(HERE, '..', 'hinh')
R = luoc_do.improved()
NHOM = {
    'b1': ('Hàng hóa, ảnh và thông số', ['LOAIHANG', 'THUONGHIEU', 'MATHANG', 'ANHMATHANG', 'DINHNGHIATHONGSO', 'GIATRITHONGSO'], 'TB'),
    'b2': ('Khách hàng, nhân viên và tài khoản', ['KHACHHANG', 'NHANVIEN', 'TAIKHOAN'], 'TB'),
    'b3': ('Đơn hàng, thanh toán và giao hàng', ['MAGIAMGIA', 'DONHANG', 'CHITIETDONHANG', 'THANHTOAN', 'PHIEUGIAO', 'LANGIAO'], 'TB'),
    'b4': ('Nhập hàng, số seri và kho', ['NHACUNGCAP', 'PHIEUNHAP', 'CHITIETPHIEUNHAP', 'HANGCOSERI', 'SERIMATHANG', 'GIAODICHKHO'], 'TB'),
    'b5': ('Đổi trả, hoàn tiền và bảo hành', ['HOSODOITRA', 'CHITIETTRA', 'LANNHANLAI', 'KHOANHOAN', 'PHIEUBAOHANH'], 'LR'),
}
COT = [['LOAIHANG', 'THUONGHIEU', 'DINHNGHIATHONGSO', 'GIATRITHONGSO', 'ANHMATHANG', 'NHACUNGCAP'],
       ['MATHANG', 'SERIMATHANG', 'CHITIETPHIEUNHAP', 'PHIEUNHAP', 'GIAODICHKHO'],
       ['CHITIETDONHANG', 'HANGCOSERI', 'PHIEUBAOHANH', 'CHITIETTRA', 'LANNHANLAI'],
       ['DONHANG', 'HOSODOITRA', 'KHOANHOAN', 'THANHTOAN'],
       ['KHACHHANG', 'TAIKHOAN', 'MAGIAMGIA', 'NHANVIEN', 'PHIEUGIAO', 'LANGIAO']]
TYPE = {'INT': 'Integer', 'NVARCHAR': 'Nvarchar', 'VARCHAR': 'Varchar', 'DECIMAL': 'Decimal', 'BIT': 'Bit', 'DATE': 'Date', 'DATETIME': 'Datetime'}


def kieu(t):
    base = t.split('(')[0]
    return TYPE[base] + (t[t.find('('):] if '(' in t else '')


def fkcols(n):
    return {c for cols, p, pc in R[n]['fks'] for c in cols}


def bang_html(n, stub=False):
    r = R[n]
    fk = fkcols(n)
    rows = [f'<TR><TD COLSPAN="4" BGCOLOR="#BDD7EE"><B>{n}</B></TD></TR>']
    for name, typ, nl, mean in r['attrs']:
        if stub and name not in r['pk']:
            continue
        is_pk, is_fk = name in r['pk'], name in fk
        col, tag = ('#C00000', '(PK)') if is_pk and not is_fk else ('#1F4EB4', '(PFK)') if is_pk else ('#2E7D32', '(FK)') if is_fk else ('#000000', '')
        if not is_pk and not is_fk and nl == 'NULL':
            col = '#808080'
        nn = 'NN' if nl == 'NN' else ''
        f = lambda t: f'<FONT COLOR="{col}">{t}</FONT>' if t else ' '
        rows.append(f'<TR><TD ALIGN="LEFT">{f(name)}</TD><TD ALIGN="LEFT">{f(kieu(typ))}</TD><TD>{f(nn)}</TD><TD>{f(tag)}</TD></TR>')
    if stub:
        rows.append('<TR><TD COLSPAN="4"><FONT COLOR="#808080">…</FONT></TD></TR>')
    return '<<TABLE BORDER="1" COLOR="#5B7FA6" CELLBORDER="0" CELLSPACING="0" CELLPADDING="2" BGCOLOR="white">' + ''.join(rows) + '</TABLE>>'


def ve_bang(key):
    ten, tables, rd = NHOM[key]
    keep = list(tables)
    L = ['digraph G {', f'  rankdir={rd}; splines=polyline; nodesep=0.3; ranksep=0.7; pad=0.2; newrank=true;',
         '  node [shape=plaintext, fontname="Helvetica", fontsize=10]; edge [fontname="Helvetica", fontsize=9, color="#3A5F8F", style=dashed, '
         'dir=both, arrowtail=crow, arrowhead=tee];']
    stubs = []
    edges = []
    for n in keep:
        for cols, parent, pc in R[n]['fks']:
            k = erd.fk_key(n, cols)
            verb = erd.VERB.get(k, '')
            if parent not in keep and parent not in stubs and parent != n:
                stubs.append(parent)
            edges.append((n, parent, verb))
    for n in keep:
        L.append(f'  "{n}" [label={bang_html(n)}];')
    for n in stubs:
        L.append(f'  "{n}" [label={bang_html(n, True)}];')
    seen = set()
    for c, p, v in edges:
        L.append(f'  "{c}" -> "{p}" [xlabel="{v}"];' if (c, p) not in seen else f'  "{c}" -> "{p}" [xlabel="{v}"];')
        seen.add((c, p))
    L.append('}')
    base = os.path.join(HINH, f'sodo_quanhe_{key}')
    open(base + '.dot', 'w', encoding='utf-8').write('\n'.join(L))
    subprocess.run(['dot', '-Tpng', '-Gdpi=170', base + '.dot', '-o', base + '.png'], check=True)


def ve_tong():
    """Toàn bộ lược đồ sau cải tiến trên một hình. Nét liền: khóa ngoại nằm trong khóa chính; nét đứt: còn lại (như Toad Data Modeler).
    dot tự xếp thì 26 bảng trải quá rộng, nên đặt tay theo cột rồi để neato -n2 chỉ đi đường."""
    assert sorted(sum(COT, [])) == sorted(R)
    nut = 'node [shape=plaintext, margin=0, fontname="Helvetica", fontsize=10];'
    do = subprocess.run(['dot', '-Tplain'], input='digraph{' + nut + ''.join(f'"{n}"[label={bang_html(n)}];' for n in R) + '}',
                        capture_output=True, text=True, encoding='utf-8', check=True).stdout
    sz = {p[1].strip('"'): (float(p[4]), float(p[5])) for p in map(str.split, do.splitlines()) if p[0] == 'node'}
    GX, GY = 0.75, 0.3
    cao = max(sum(sz[n][1] for n in c) + GY * (len(c) - 1) for c in COT)
    pos, x = {}, 0
    for c in COT:
        w = max(sz[n][0] for n in c)
        khe = (cao - sum(sz[n][1] for n in c)) / max(len(c) - 1, 1)
        y = cao
        for n in c:
            pos[n] = (x + w / 2, y - sz[n][1] / 2)
            y -= sz[n][1] + khe
        x += w + GX
    L = ['digraph G {', '  splines=ortho; pad=0.1;', '  ' + nut,
         '  edge [color="#3A5F8F", dir=both, arrowtail=crow, arrowhead=tee, arrowsize=0.6];']
    for n in R:
        L.append(f'  "{n}" [label={bang_html(n)}, pos="{pos[n][0] * 72:.1f},{pos[n][1] * 72:.1f}!"];')
    for n in R:
        for cols, parent, pc in R[n]['fks']:
            L.append(f'  "{n}" -> "{parent}" [style={"solid" if set(cols) <= set(R[n]["pk"]) else "dashed"}];')
    L.append('}')
    base = os.path.join(HINH, 'sodo_quanhe_tong')
    open(base + '.dot', 'w', encoding='utf-8').write('\n'.join(L))
    subprocess.run(['neato', '-n2', '-Tpng', '-Gdpi=220', base + '.dot', '-o', base + '.png'], check=True)


if __name__ == '__main__':
    for k in NHOM:
        ve_bang(k)
    ve_tong()
    print('đã vẽ', len(NHOM) + 1, 'sơ đồ quan hệ dạng bảng')
