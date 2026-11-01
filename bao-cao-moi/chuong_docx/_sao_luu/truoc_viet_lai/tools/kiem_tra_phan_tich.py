"""In tóm tắt phân tích của 24 quan hệ ban đầu và 25 quan hệ sau cải tiến để soát bằng mắt.  Chạy: python3 tools/kiem_tra_phan_tich.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fd import NF_NAME, fmt_fd, keys_ntd, min_cover, normal_form, parse
import luoc_do

COMPOUND = {'KHACHHANG': ['HoTenKH'], 'NHANVIEN': ['HoTenNV']}


def analyse(R, order, compound):
    out = {}
    for name in order:
        r = R[name]
        attrs = [a[0] for a in r['attrs']]
        F = parse(r['F'])
        G, trace = min_cover(F, attrs)
        k = keys_ntd(attrs, G)
        nf = normal_form(attrs, G, k['keys'], compound.get(name))
        out[name] = dict(attrs=attrs, F=F, G=G, trace=trace, keys=k, nf=nf)
    return out


if __name__ == '__main__':
    for title, R, order, comp in (('BAN ĐẦU', luoc_do.REL, luoc_do.ORDER, COMPOUND),
                                  ('SAU CẢI TIẾN', luoc_do.improved(), luoc_do.ORDER_IMPROVED, {})):
        res = analyse(R, order, comp)
        print('=====', title, len(res), 'quan hệ')
        cnt = {}
        for n, x in res.items():
            nm = NF_NAME[x['nf']['nf']]
            cnt[nm] = cnt.get(nm, 0) + 1
            ks = ['{' + ','.join(k) + '}' for k in x['keys']['keys']]
            print(f"{n:18s} {nm:12s} |G|={len(x['G']):2d} khóa={ks} N={x['keys']['N']} TG={x['keys']['TG']} "
                  f"b2={len(x['trace']['b2'])} b3={[t[0] for t in x['trace']['b3']][:3]}")
            if x['nf']['partial']:
                print('   bộ phận:', x['nf']['partial'])
            if x['nf']['viol3']:
                print('   vi phạm 3NF:', x['nf']['viol3'])
            if x['nf']['violbc']:
                print('   vi phạm BCNF:', x['nf']['violbc'])
        print(cnt)
