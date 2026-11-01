#!/usr/bin/env python3
"""Sinh chương 2 (chuong/02_chuong2.md) từ tools/luoc_do.py và tools/fd.py.

Nội dung: 2.1 mô hình quan hệ (lược đồ, tân từ, ràng buộc, từ điển dữ liệu); 2.2 PTH, phủ tối thiểu, khóa, dạng chuẩn của
từng quan hệ ban đầu; 2.3 cải tiến (phân rã, tổng hợp, bảo toàn thông tin và PTH, 4NF); lược đồ sau cải tiến.
Chạy:  python3 tools/gen_chuong2.py
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import luoc_do
import noidung
from fd import NF_NAME, chase, closure, equivalent, fmt_fd, keys_ntd, min_cover, normal_form, parse, preservation, project

REL = luoc_do.REL
IMP = luoc_do.improved()
ORD = luoc_do.ORDER
ORDI = luoc_do.ORDER_IMPROVED
COMPOUND = {'KHACHHANG': ['HoTenKH'], 'NHANVIEN': ['HoTenNV']}
OUT = []
FIG24 = []


def w(s=''):
    OUT.append(s)


def fig(path, title):
    w(f'![{title}](hinh/{path}.png)')
    w()
    w(f'*{title}*')
    w()


def U(x):
    return f'<u>{x}</u>'


def DASH(x):
    return f'<span style="text-decoration: underline dashed">{x}</span>'


def sig(name, R):
    r = R[name]
    fkcols = {c for cols, p, pc in r['fks'] for c in cols}
    parts = []
    for a in r['attrs']:
        n = a[0]
        if n in r['pk']:
            parts.append(U(n) + ('<sup>FK</sup>' if n in fkcols else ''))
        elif n in fkcols:
            parts.append(DASH(n))
        else:
            parts.append(n)
    return f'{name}({", ".join(parts)})'


def plain_sig(name, R):
    return f'{name}({", ".join(a[0] for a in R[name]["attrs"])})'


def set_str(xs):
    xs = list(xs)
    return '{' + ', '.join(xs) + '}' if xs else '∅'


def split_type(t):
    base = t.split('(')[0]
    ln = t[t.find('(') + 1:-1] if '(' in t else ''
    nm = {'INT': 'Integer', 'NVARCHAR': 'Nvarchar', 'VARCHAR': 'Varchar', 'DECIMAL': 'Decimal', 'BIT': 'Bit',
          'DATE': 'Date', 'DATETIME': 'Datetime'}[base]
    return nm, ln


def grouped(G, order, limit=7):
    """Hiển thị tập PTH: liệt kê hết nếu ngắn, ngược lại gộp theo vế trái."""
    if len(G) <= limit:
        return '; '.join(fmt_fd(fd, order) for fd in G)
    byl = {}
    for L, R in G:
        byl.setdefault(tuple(sorted(L, key=order.index)), []).append(next(iter(R)))
    return '; '.join(f'{",".join(l)} → {{{", ".join(sorted(rs, key=order.index))}}} ({len(rs)} PTH)' for l, rs in byl.items())


def cnt_unit(n):
    return f'{n} PTH'


# =============================================================== 2.1
def sec_21():
    w('# CHƯƠNG 2: THIẾT KẾ VÀ CHUẨN HÓA CƠ SỞ DỮ LIỆU QUAN HỆ')
    w()
    w('Chương này chuyển mô hình ERD ở chương 1 sang mô hình quan hệ, xác định tập phụ thuộc hàm (PTH), phủ tối thiểu, khóa và '
      'dạng chuẩn của **từng** lược đồ quan hệ (LĐQH), rồi cải tiến những lược đồ chưa đạt dạng chuẩn cao bằng thuật toán phân rã '
      'và tổng hợp, kiểm tra bảo toàn thông tin, bảo toàn PTH và tìm tình huống dạng chuẩn 4 (4NF). Ký hiệu theo bài giảng: Q(A₁,…,Aₙ), '
      'Q⁺, ‖Q‖ (tân từ), X⁺_F, F⁺. Khóa chính gạch chân liền, khóa ngoại gạch chân nét đứt; thuộc tính vừa là khóa chính '
      'vừa là khóa ngoại gạch liền và ghi chú FK.')
    w()
    w('## 2.1 MÔ HÌNH QUAN HỆ')
    w()
    w('### 2.1.1 Chuyển ERD sang mô hình quan hệ')
    w()
    w('Quy tắc chuyển đổi áp dụng: (1) mỗi loại thực thể thành một quan hệ có khóa chính là mã của thực thể; (2) mối kết hợp 1–n '
      'thêm khóa ngoại vào quan hệ phía n (cột cho phép rỗng khi bản số nhỏ nhất là 0); (3) mối kết hợp 1–1 thêm khóa ngoại và '
      'ràng buộc UNIQUE ở một phía (PHIEUGIAO.MaDH); (4) mối kết hợp n–n thành quan hệ riêng có khóa gồm khóa của các thực thể tham gia, '
      'cộng số thứ tự dòng khi cùng một cặp có thể lặp (CHITIETDONHANG, CHITIETPHIEUNHAP); (5) mối kết hợp có thuộc tính mang theo thuộc tính đó.')
    w()
    mk_names = [n for n in ORD if REL[n]['loai'] == 'mkh']
    w(f'Kết quả là **{len(ORD)} quan hệ**: {len(ORD) - len(mk_names)} từ các loại thực thể và {len(mk_names)} từ các mối kết hợp có thuộc tính '
      f'({", ".join(mk_names)}). Khi chuyển, nhóm giữ lại một số cột lưu thêm cho tiện tra cứu (ví dụ MaSP trên phiếu bảo hành). '
      'Đây là **lược đồ ban đầu**, chưa tối ưu; các cột này và việc chưa tách họ tên là nguyên nhân của những quan hệ chưa đạt BCNF '
      'ở mục 2.2 và được xử lý ở mục 2.3.')
    w()
    w('| STT | Quan hệ | Nguồn từ ERD | Loại | Ghi chú thiết kế |')
    w('|---|---|---|---|---|')
    for i, n in enumerate(ORD, 1):
        r = REL[n]
        src = 'Mối kết hợp có thuộc tính' if r['loai'] == 'mkh' else 'Thực thể'
        w(f'| {i} | {n} | {src} | {luoc_do.LOAI[r["loai"]]} | {noidung.GHI_CHU_THIET_KE.get(n, "")} |')
    w()
    w(f'*Bảng 2.1: Đối chiếu ERD và {len(ORD)} quan hệ ban đầu*')
    w()
    w('### 2.1.2 Lược đồ quan hệ cơ sở dữ liệu')
    w()
    for i, n in enumerate(ORD, 1):
        w(f'{i}. {sig(n, REL)}')
    w()
    w('### 2.1.3 Mô tả các quan hệ (tân từ và ràng buộc)')
    w()
    for i, n in enumerate(ORD, 1):
        r = REL[n]
        w(f'**{i}/ {sig(n, REL)}**')
        w()
        w(f'Tân từ: {r["tantu"]}')
        w()
        w(f'Ràng buộc: {r["rangbuoc"]}')
        w()
    w('### 2.1.4 Danh sách thông tin các bảng')
    w()
    w('Kiểu dữ liệu theo SQL chuẩn (tiền là đồng Việt Nam, kiểu DECIMAL(15,0)). PFK: vừa là khóa chính vừa là khóa ngoại.')
    w()
    for i, n in enumerate(ORD, 1):
        r = REL[n]
        fkcols = {c for cols, p, pc in r['fks'] for c in cols}
        w(f'**{i}/ Bảng {n}** ({r["ten"]})')
        w()
        w('| Tên thuộc tính | Ý nghĩa | Kiểu dữ liệu | Độ dài | Ràng buộc |')
        w('|---|---|---|---|---|')
        for a, t, nl, mean in r['attrs']:
            tn, ln = split_type(t)
            if a in r['pk']:
                cs = 'PFK' if a in fkcols else 'PK'
            else:
                cs = 'FK' if a in fkcols else ''
                cs = (cs + ', ' if cs else '') + ('Not Null' if nl == 'NN' else 'Null')
            if any(u == (a,) for u in r['uniques']):
                cs += ', Unique'
            w(f'| {a} | {mean} | {tn} | {ln} | {cs} |')
        w()


# =============================================================== 2.2
def analyse_all(R, order, compound):
    res = {}
    for n in order:
        r = R[n]
        attrs = [a[0] for a in r['attrs']]
        F = parse(r['F'])
        G, tr = min_cover(F, attrs)
        k = keys_ntd(attrs, G)
        nf = normal_form(attrs, G, k['keys'], compound.get(n))
        res[n] = dict(attrs=attrs, F=F, G=G, trace=tr, keys=k, nf=nf)
    return res


def fd_reason(n, L, R):
    key = ','.join(sorted(L, key=[a[0] for a in REL[n]['attrs']].index))
    r = REL[n]
    if (n, key) in noidung.CAN_CU:
        return noidung.CAN_CU[(n, key)]
    if list(L) and set(L) == set(r['pk']):
        return 'khóa chính xác định mọi thuộc tính còn lại.'
    if any(set(u) == set(L) for u in r['uniques']):
        return 'ràng buộc UNIQUE: giá trị không trùng nên cũng xác định mọi thuộc tính.'
    return 'quy tắc nghiệp vụ.'


def sec_22(res):
    w('### 2.1.5 Sơ đồ quan hệ cơ sở dữ liệu (sau cải tiến)')
    w()
    w('Các hình dưới đây vẽ lược đồ sau cải tiến theo từng nhóm: mỗi bảng ghi tên cột, kiểu, NOT NULL (NN) và khóa; chữ đỏ là khóa chính (PK), xanh lam là khóa vừa chính vừa ngoại (PFK), '
      'xanh lục là khóa ngoại (FK), xám là cột cho phép rỗng. Đường nét đứt nối khóa ngoại tới khóa chính của bảng cha, ghi tên mối kết hợp; bảng cha thuộc nhóm khác chỉ vẽ phần khóa.')
    w()
    import ve_bang
    for k, (ten, tables, rd) in ve_bang.NHOM.items():
        fig(f'sodo_quanhe_{k}', f'Hình 2.{5 + int(k[1:]) - 1 + 0}: Sơ đồ quan hệ nhóm “{ten}”')
    w('## 2.2 TẬP PHỤ THUỘC HÀM, PHỦ TỐI THIỂU, KHÓA VÀ DẠNG CHUẨN CỦA TỪNG QUAN HỆ')
    w()
    w('### 2.2.1 Quy ước và giả thiết')
    w()
    w('Với mỗi quan hệ, báo cáo trình bày theo khuôn: (1) tập PTH F kèm căn cứ; (2) phủ tối thiểu theo 3 bước của bài giảng '
      '(B1 tách vế phải, B2 bỏ thuộc tính thừa ở vế trái bằng bao đóng, B3 bỏ PTH dư thừa); (3) khóa theo thuật toán nguồn N, trung gian '
      'TG, đích D; (4) dạng chuẩn từng mức. Phép tính đều đã được đối chiếu bằng chương trình `tools/fd.py` (tính lại bao đóng, '
      'khóa và dạng chuẩn); lời giải trong báo cáo vẫn trình bày từng bước.')
    w()
    w('Phụ thuộc hàm rút từ tân từ và quy tắc nghiệp vụ, **không** rút từ dữ liệu mẫu (dữ liệu mẫu không chứng minh được một PTH). '
      'Cột F chỉ ghi các PTH không hiển nhiên. Các giả thiết nghiệp vụ nhóm tự đặt:')
    w()
    for k, t in noidung.GIA_THIET:
        w(f'- **{k}**: {t}')
    w()
    w('Dạng chuẩn dùng định nghĩa của giáo trình: DC1 mọi thuộc tính đơn; DC2 không phụ thuộc một phần vào khóa; DC3 không phụ '
      'thuộc bắc cầu vào khóa (hay với mọi PTH không hiển nhiên X → A, X là siêu khóa hoặc A là thuộc tính khóa); BCNF (BCK) mọi PTH '
      'không hiển nhiên có vế trái chứa khóa. Mọi khóa ứng viên đều được xét, không chỉ khóa chính.')
    w()
    for i, n in enumerate(ORD, 1):
        quan_he_block(i, n, res[n])
    # đánh giá
    w(f'### 2.2.{len(ORD) + 2} Đánh giá lược đồ ban đầu')
    w()
    w('| STT | Quan hệ | Khóa (mọi khóa ứng viên) | Dạng chuẩn |')
    w('|---|---|---|---|')
    cnt = {}
    for i, n in enumerate(ORD, 1):
        x = res[n]
        ks = '; '.join('{' + ', '.join(k) + '}' for k in x['keys']['keys'])
        nm = NF_NAME[x['nf']['nf']]
        cnt[nm] = cnt.get(nm, 0) + 1
        w(f'| {i} | {n} | {ks} | {nm} |')
    w()
    w(f'*Bảng 2.2: Đánh giá dạng chuẩn của {len(ORD)} quan hệ ban đầu*')
    w()
    lowest = min(x['nf']['nf'] for x in res.values())
    w(f'Thống kê: {", ".join(f"{k}: {v} quan hệ" for k, v in sorted(cnt.items(), key=lambda kv: kv[0]))}. Dạng chuẩn của cả lược đồ '
      f'là dạng chuẩn thấp nhất của các quan hệ, tức **{NF_NAME[lowest]}** (do KHACHHANG và NHANVIEN có họ tên là thuộc tính kép). '
      'Ngay cả khi tách họ tên, lược đồ vẫn chỉ đạt 1NF vì CHITIETTRA còn phụ thuộc bộ phận (1NF), PHIEUBAOHANH còn phụ thuộc bắc '
      'cầu (2NF) và HANGCOSERI còn vi phạm BCNF (3NF). Các quan hệ này được cải tiến ở mục 2.3.')
    w()


def quan_he_block(i, n, x):
    r = REL[n]
    attrs = x['attrs']
    G, tr, k = x['G'], x['trace'], x['keys']
    w(f'### 2.2.{i + 1} Lược đồ quan hệ {n}')
    w()
    w(f'Xét LĐQH {sig(n, REL)}.')
    w()
    w('**Các phụ thuộc hàm:**')
    w()
    for j, (L, R) in enumerate(x['F'], 1):
        w(f'- f{j}: {fmt_fd((L, R), attrs)} — {fd_reason(n, L, R)}')
    w()
    w(f'**Phủ tối thiểu của F_{n}:**')
    w()
    b1 = tr['b1']
    if len(b1) == len(x['F']):
        w('Bước 1: Tách vế phải. Không thực hiện vì mọi PTH đã có vế phải là một thuộc tính.')
    else:
        w(f'Bước 1: Tách vế phải, thu được {len(b1)} PTH, mỗi PTH một thuộc tính ở vế phải: {grouped(b1, attrs)}.')
    w()
    multi = sorted({tuple(sorted(L, key=attrs.index)) for L, R in b1 if len(L) > 1})
    if tr['b2']:
        for before, b, after in tr['b2']:
            w(f'Bước 2: Xét {before}: thuộc tính {b} ở vế trái là thừa vì vế phải suy ra được khi bỏ {b}. Thay bằng {after}.')
    elif multi:
        for L in multi:
            parts = []
            for b in L:
                rest = set(L) - {b}
                cl = sorted(closure(rest, G), key=attrs.index)
                parts.append(f'({",".join(sorted(rest, key=attrs.index))})⁺ = {set_str(cl)}')
            w(f'Bước 2: Xét vế trái {{{", ".join(L)}}}: ' + '; '.join(parts) +
              '. Không chứa vế phải nên không thuộc tính nào thừa. Giữ nguyên.')
    else:
        w('Bước 2: Không thực hiện vì mọi PTH đều có vế trái là một thuộc tính (đã đầy đủ).')
    w()
    if tr['b3']:
        w('Bước 3: Loại các PTH dư thừa (xét từ PTH cuối lên đầu để giữ các PTH của khóa chính):')
        w()
        byl = {}
        for s_, why in tr['b3']:
            byl.setdefault(s_.split(' → ')[0], []).append((s_, why))
        for L, items in byl.items():
            if len(items) > 3:
                rhs = [s_.split(' → ')[1] for s_, _ in items]
                w(f'- {L} → {{{", ".join(rhs)}}} ({len(items)} PTH): mỗi PTH suy ra được từ các PTH còn lại theo luật bắc cầu '
                  f'(ví dụ {items[0][1]}).')
            else:
                for s_, why in items:
                    w(f'- {s_}: {why}.')
    else:
        w('Bước 3: Không có PTH dư thừa vì không PTH nào suy ra được từ các PTH còn lại.')
    w()
    w(f'Vậy phủ tối thiểu của F_{n} là G_{n} = {{{grouped(G, attrs)}}}. (G ≡ F: {"đã kiểm tra" if equivalent(x["F"], G) else "LỖI"} bằng bao đóng.)')
    w()
    w('**Xác định khóa:**')
    w()
    w(f'N = {set_str(k["N"])}; TG = {set_str(k["TG"])}; D = {set_str(k["D"])}.')
    w()
    U_ = set(attrs)
    if k['unique']:
        cl = sorted(closure(set(k['N']), G), key=attrs.index)
        w(f'{set_str(k["N"])}⁺ = {set_str(cl)} = Q⁺. Vậy khóa duy nhất là {set_str(k["N"])}.')
    else:
        w('Bảng tổ hợp (Kᵢ = N ∪ Mᵢ với Mᵢ là tập con của TG):')
        w()
        w('| Mᵢ | Kᵢ | Kᵢ⁺ | Kết luận |')
        w('|---|---|---|---|')
        for c, K, cl, st in k['rows']:
            shown = 'Q⁺' if set(cl) == U_ else set_str(cl)
            w(f'| {set_str(c) if c else "∅"} | {set_str(K) if K else "∅"} | {shown} | {st} |')
        w()
        w('Các khóa: ' + '; '.join(set_str(kk) for kk in k['keys']) + '.')
    w()
    nf_block(n, x)


def nf_block(n, x):
    attrs, G, k, nfd = x['attrs'], x['G'], x['keys'], x['nf']
    r = REL[n]
    keys = k['keys']
    w('**Xác định dạng chuẩn:**')
    w()
    comp = COMPOUND.get(n)
    if comp:
        w(f'- Không đạt dạng chuẩn 1 vì {", ".join(comp)} là thuộc tính kép (họ lót và tên, giả thiết G3); cửa hàng phải lọc theo '
          'từng phần của giá trị. Các mức sau xét trên các PTH đã cho, coi như họ tên đã được tách (mục 2.3.2).')
    else:
        w('- Đạt dạng chuẩn 1 vì mọi thuộc tính của ' + n + ' đều là thuộc tính đơn.')
    nonp = nfd['nonprime']
    if nfd['partial']:
        sub, kk, got = nfd['partial'][0]
        w(f'- Không đạt dạng chuẩn 2 vì thuộc tính không khóa {", ".join(got)} phụ thuộc vào {set_str(sub)}, là một phần của khóa {set_str(kk)}.')
        ok2 = False
    else:
        ok2 = True
        if all(len(kk) == 1 for kk in keys):
            w(f'- Đạt dạng chuẩn 2 vì mọi khóa chỉ có một thuộc tính ({"; ".join(set_str(kk) for kk in keys)}).')
        elif not nonp:
            w('- Đạt dạng chuẩn 2 vì mọi thuộc tính đều là thuộc tính khóa.')
        else:
            w(f'- Đạt dạng chuẩn 2 vì mọi thuộc tính không khóa ({", ".join(nonp)}) phụ thuộc đầy đủ vào khóa: không có tập con thật sự của khóa nào xác định chúng.')
    if not ok2:
        w('- Không đạt dạng chuẩn 3 vì chưa đạt dạng chuẩn 2.')
        w('- Không đạt BCNF vì chưa đạt dạng chuẩn 3.')
        w(f'- Kết luận: **{n} đạt dạng chuẩn {NF_NAME[nfd["nf"]]}**.')
        w()
        return
    if nfd['viol3']:
        L, a = nfd['viol3'][0]
        w(f'- Không đạt dạng chuẩn 3 vì {a} là thuộc tính không khóa phụ thuộc bắc cầu vào khóa: {set_str(L)} → {a} mà {set_str(L)} không là siêu khóa.')
        w('- Không đạt BCNF vì chưa đạt dạng chuẩn 3.')
        w(f'- Kết luận: **{n} đạt dạng chuẩn {NF_NAME[nfd["nf"]]}**.')
        w()
        return
    prime = nfd['prime']
    if nfd['violbc']:
        ex = '; '.join(f'{set_str(L)} → {a}' for L, a in nfd['violbc'])
        w(f'- Đạt dạng chuẩn 3 vì mọi PTH không hiển nhiên hoặc có vế trái là siêu khóa hoặc có vế phải là thuộc tính khóa (MaSP là thuộc tính khóa vì thuộc khóa {set_str(next(kk for kk in keys if "MaSP" in kk))}).')
        w(f'- Không đạt BCNF vì có PTH {ex} có vế trái không chứa khóa.')
        w(f'- Kết luận: **{n} đạt dạng chuẩn {NF_NAME[nfd["nf"]]}**.')
        w()
        return
    w('- Đạt dạng chuẩn 3 vì không có thuộc tính không khóa nào phụ thuộc bắc cầu vào khóa.')
    lhs = sorted({tuple(sorted(L, key=attrs.index)) for L, _ in G}, key=lambda t: attrs.index(t[0]))
    w(f'- Đạt BCNF vì mọi PTH không hiển nhiên đều có vế trái chứa khóa: ' + '; '.join(set_str(t) for t in lhs) + '.')
    w(f'- Kết luận: **{n} đạt dạng chuẩn {"BCNF" if not comp else "BCNF (khi họ tên đã tách)"}**' +
      (' nhưng chưa đạt dạng chuẩn 1.' if comp else '.'))
    w()


# =============================================================== 2.3
def letters(attrs):
    return {a: chr(ord('A') + i) for i, a in enumerate(attrs)}


def table_tableau(U_, comps, F, steps_text=True, groupable=None):
    """Trả về (các dòng markdown của bảng đầu, các bước, bảng sau, bảng sau có dòng a hay không)."""
    first, steps, final, ok = chase(U_, comps, F)
    L = letters(U_)
    lhs_all = set().union(*[l for l, _ in F])
    rhs_by = {}
    for l, rr in F:
        for a in rr:
            rhs_by.setdefault(a, set()).add(l)
    groupable = {a for a in U_ if a not in lhs_all and len(rhs_by.get(a, [])) <= 1}
    pattern = {a: tuple(a in Q for Q in comps.values()) for a in U_}
    cols, grp = [], {}
    for a in U_:
        if a in groupable:
            key = (pattern[a], tuple(sorted(rhs_by.get(a, []), key=lambda s: sorted(s))))
            if key in grp:
                grp[key].append(a)
                continue
            grp[key] = [a]
            cols.append(('Z', key))
        else:
            cols.append(('A', a))
    # chọn tên cột
    zn = 0
    names, members = [], []
    for kind, v in cols:
        if kind == 'A':
            names.append(L[v])
            members.append([v])
        else:
            mem = grp[v]
            if len(mem) == 1:
                names.append(L[mem[0]])
            else:
                zn += 1
                names.append('Z' if zn == 1 else f'Z{zn}')
            members.append(mem)
    # đánh số hiển thị cho b
    disp = {}
    nb = 0
    for nm in comps:
        for ci, mem in enumerate(members):
            v = first[nm][mem[0]]
            if v.startswith('b') and v not in disp:
                nb += 1
                disp[v] = f'b{nb}'

    def cell(v, ci):
        return f'a{ci + 1}' if v.startswith('a:') else disp.get(v, v)
    hdr = '| T | ' + ' | '.join(names) + ' |'
    sep = '|---|' + '---|' * len(names)
    t1 = [hdr, sep]
    for nm in comps:
        t1.append(f'| {nm} | ' + ' | '.join(cell(first[nm][m[0]], ci) for ci, m in enumerate(members)) + ' |')
    t2 = [hdr, sep]
    for nm in comps:
        cells = []
        for ci, m in enumerate(members):
            v0, v1 = first[nm][m[0]], final[nm][m[0]]
            if v0 != v1:
                cells.append(f'{cell(v0, ci)} ⇒ {cell(v1, ci)}')
            else:
                cells.append(cell(v1, ci))
        t2.append(f'| {nm} | ' + ' | '.join(cells) + ' |')
    # bước
    stext = []
    colname = {}
    for ci, m in enumerate(members):
        for a in m:
            colname[a] = (names[ci], ci)
    seen_pairs = set()
    for i, j, Lh, y, old, new in steps:
        nm, ci = colname[y]
        key = (i, j, Lh, nm, old)
        if key in seen_pairs:
            continue
        seen_pairs.add(key)
        lcols = ','.join(colname[a][0] for a in Lh)
        stext.append(f'Hai dòng {i} và {j} cùng giá trị ở {lcols}; theo PTH {lcols} → {nm}, ô cột {nm}: {disp.get(old, old if not old.startswith("a:") else "a")} thành {cell(new, ci)}.')
    ngroup = [(names[ci], members[ci]) for ci in range(len(members)) if len(members[ci]) > 1]
    return t1, stext, t2, ok, ngroup


def decomp_block(title, rel, G, comps, notes=None, with_tableau=True):
    """Sinh một khối phân tích phép tách: PTH chiếu, bảo toàn thông tin, bảo toàn PTH. Trả về (bảo toàn TT, bảo toàn PTH)."""
    attrs = [a[0] for a in REL[rel]['attrs']]
    L = letters(attrs)
    w(f'**{title}**')
    w()
    Fp, lost = preservation(G, comps, attrs)
    w('Các quan hệ con và PTH chiếu (Fᵢ):')
    w()
    for nm, Q in comps.items():
        Fi = project(G, Q, attrs)
        qs = ', '.join(L[a] for a in sorted(Q, key=attrs.index))
        qn = ', '.join(sorted(Q, key=attrs.index))
        fs = '; '.join(fmt_fd(f, attrs) for f in Fi) if Fi else '∅'
        w(f'- **{nm}**({qn}): F = {{{fs}}}')
    w()
    t1, stext, t2, ok, ngroup = table_tableau(attrs, comps, G)
    if ngroup:
        w('Ký hiệu cột gộp: ' + '; '.join(f'{n} = {{{", ".join(m)}}}' for n, m in ngroup) + ' (các thuộc tính này chỉ phụ thuộc vào cùng một khóa và có cùng cách xuất hiện ở các quan hệ con).')
        w()
    w('Kiểm tra **bảo toàn thông tin** bằng bảng a/b của giáo trình. Bảng khởi tạo:')
    w()
    for ln in t1:
        w(ln)
    w()
    w('Biến đổi theo PTH của F:')
    w()
    for s in stext:
        w(f'- {s}')
    if not stext:
        w('- Không có cặp dòng nào thỏa vế trái của một PTH để thay đổi ký hiệu.')
    w()
    w('Bảng sau biến đổi:')
    w()
    for ln in t2:
        w(ln)
    w()
    w(('Có một dòng chứa toàn ký hiệu a → **bảo toàn thông tin**.' if ok else 'Không có dòng nào chứa toàn ký hiệu a → **không bảo toàn thông tin**.'))
    w()
    w('Kiểm tra **bảo toàn PTH** (cách của bài giảng): F\' = ∪Fᵢ = {' + '; '.join(fmt_fd(f, attrs) for f in Fp) + '}.')
    w()
    w('- (1) Mọi f\' ∈ F\' \\ F đều thuộc F⁺ vì mỗi Fᵢ là PTH chiếu từ F⁺.')
    w('- (2) Mọi f ∈ F \\ F\' phải thuộc F\'⁺. Kiểm tra từng PTH của F bằng bao đóng theo F\':')
    for Lh, Rh in G:
        for a in Rh:
            cl = closure(Lh, Fp)
            okf = a in cl
            lh = ','.join(sorted(Lh, key=attrs.index))
            w(f'  - {lh} → {a}: ({lh})⁺_F\' = {set_str(sorted(cl, key=attrs.index))} {"∋" if okf else "∌"} {a} → {"thỏa" if okf else "**không thỏa**"}.')
    w()
    okp = not lost
    w(('**Kết luận: bảo toàn PTH** (thỏa (1) và (2)).' if okp else
       '**Kết luận: không bảo toàn PTH** (thỏa (1) nhưng không thỏa (2)); PTH bị mất: ' + '; '.join(f'{set_str(sorted(l, key=attrs.index))} → {a}' for l, a in lost) + '.'))
    w()
    # dạng chuẩn các quan hệ con
    nfs = []
    for nm, Q in comps.items():
        Fi = project(G, Q, attrs)
        Qs = sorted(Q, key=attrs.index)
        kk = keys_ntd(Qs, Fi)
        nf = normal_form(Qs, Fi, kk['keys'])
        nfs.append(f'{nm}: {NF_NAME[nf["nf"]]} (khóa ' + ', '.join(set_str(x) for x in kk['keys']) + ')')
    w('Dạng chuẩn các quan hệ con: ' + '; '.join(nfs) + '.')
    w()
    return ok, okp


def sec_23(res):
    w('## 2.3 CẢI TIẾN LƯỢC ĐỒ')
    w()
    w('### 2.3.1 Phương pháp')
    w()
    w('**Thuật toán phân rã (định lý Delobel):** nếu f: X → A ∈ F⁺ và XA là tập con thật sự của Q⁺ thì tách Q thành Q₁(X, A) và '
      'Q₂(Q⁺ \\ A) là phép tách bảo toàn thông tin. B1 bỏ khỏi F các PTH có VT ∪ VP = Q⁺; B2 nếu F* = ∅ thì dừng, ngược lại chọn PTH '
      '“gây xấu” (vế trái không chứa khóa), tách rồi phân rã đệ quy. Kết quả đạt BCNF, bảo toàn thông tin nhưng có thể mất PTH.')
    w()
    w('**Thuật toán tổng hợp cải tiến:** B1 tìm phủ tối thiểu; B2 nhóm các PTH cùng vế trái; B3 gộp các nhóm có vế trái phụ thuộc lẫn '
      'nhau; B4 mỗi nhóm thành một quan hệ con; B5 tìm khóa của Q; B6 nếu chưa quan hệ con nào chứa khóa của Q thì thêm quan hệ chứa một khóa. '
      'Kết quả đạt 3NF, bảo toàn PTH, và bảo toàn thông tin sau B5–B6, nhưng có thể còn trùng lắp.')
    w()
    w('**Chứng minh:** (a) bảo toàn PTH: đặt F\' = ∪Fᵢ, cần mọi f\' ∈ F\' \\ F thuộc F⁺ và mọi f ∈ F \\ F\' thuộc F\'⁺; (b) bảo toàn '
      'thông tin: lập bảng a/b (cột là thuộc tính của Q, dòng là các Qᵢ; ô là aⱼ nếu thuộc tính ∈ Qᵢ, ngược lại bₖ), áp các PTH để đồng '
      'nhất ký hiệu; có một dòng toàn a thì bảo toàn. Chữ cái A, B, C… ứng với thứ tự cột của quan hệ trong lược đồ ban đầu '
      '(bảng ánh xạ nhắc lại ở từng quan hệ).')
    w()
    # --- DC1
    w('### 2.3.2 Đạt dạng chuẩn 1: tách họ tên')
    w()
    w('KHACHHANG và NHANVIEN chưa đạt dạng chuẩn 1 vì họ tên là thuộc tính kép. Phép thử theo bài giảng: để đếm hoặc lọc khách tên “Mỹ” '
      'cửa hàng phải viết `WHERE HoTenKH LIKE N\'%Mỹ\'`, tức dùng một phần của giá trị. Cách sửa không cần phân rã quan hệ: **thay cột '
      'HoTenKH bằng HoLotKH và TenKH** (tương tự HoLotNV, TenNV). Sau khi tách, truy vấn trở thành `WHERE TenKH = N\'Mỹ\'`. '
      'Phép tách không làm mất thông tin vì họ tên ghép lại từ HoLot và Ten; PTH đổi thành MaKH → HoLotKH, TenKH,… nên khóa và '
      'dạng chuẩn BCNF của quan hệ không đổi. Giới hạn: tên người Việt có thể có nhiều chữ nên quy ước “Ten là từ cuối cùng”; '
      'đây là quy ước nhập liệu, không kiểm tra được bằng PTH.')
    w()
    # --- CHITIETTRA
    attrs_ct = [a[0] for a in REL['CHITIETTRA']['attrs']]
    Lc = letters(attrs_ct)
    w('### 2.3.3 CHITIETTRA: từ 1NF lên BCNF')
    w()
    w('Ánh xạ chữ cái: ' + ', '.join(f'{Lc[a]} = {a}' for a in attrs_ct) + '.')
    G = res['CHITIETTRA']['G']
    w(f'F (phủ tối thiểu G): ' + '; '.join(fmt_fd(f, attrs_ct) for f in G) + f'. Khóa duy nhất {set_str(res["CHITIETTRA"]["keys"]["keys"][0])}. '
      'Vi phạm: MaHS → MaDH có vế trái là một phần của khóa nên MaDH phụ thuộc bộ phận (chưa đạt 2NF).')
    w()
    w('**Phân rã theo thuật toán.** B1: loại khỏi F PTH có VT ∪ VP = Q⁺ (PTH của khóa chính MaHS,SoDongDH → MaDH,SoLuongTra,MaSeri); '
      'còn F* = {MaHS → MaDH} ≠ ∅. B2: chọn PTH gây xấu **MaHS → MaDH** (vế trái là một phần của khóa). Tách Q₁ = {MaHS, MaDH} và Q₂ = Q⁺ \\ {MaDH}.')
    w()
    comps = {'Q1': {'MaHS', 'MaDH'}, 'Q2': {'MaHS', 'SoDongDH', 'SoLuongTra', 'MaSeri'}}
    decomp_block('Phép tách CHITIETTRA thành Q₁ và Q₂', 'CHITIETTRA', G, comps)
    w('Q₁ **trùng với phép chiếu (MaHS, MaDH) của HOSODOITRA**, nên không tạo quan hệ mới: chỉ **bỏ cột MaDH khỏi CHITIETTRA**; '
      'dòng đơn được trả là (HOSODOITRA.MaDH, SoDongDH). **CHITIETTRA nâng từ 1NF lên BCNF.**')
    w()
    fig('phan_ra_chitiettra', 'Hình 2.1: Phân rã CHITIETTRA theo phụ thuộc hàm MaHS → MaDH')
    # --- PHIEUBAOHANH
    attrs_bh = [a[0] for a in REL['PHIEUBAOHANH']['attrs']]
    Lb = letters(attrs_bh)
    w('### 2.3.4 PHIEUBAOHANH: từ 2NF lên BCNF')
    w()
    w('Ánh xạ chữ cái: ' + ', '.join(f'{Lb[a]} = {a}' for a in attrs_bh) + '.')
    Gb = res['PHIEUBAOHANH']['G']
    w('F (phủ tối thiểu G): ' + grouped(Gb, attrs_bh, limit=0).replace('(', '(').replace(')', ')') + '. Khóa duy nhất {MaPhieuBH}. '
      'Vi phạm: (MaDH, SoDongDH) → MaSP và MaSeri → MaSP có vế trái không phải siêu khóa và MaSP không là thuộc tính khóa (bắc cầu).')
    w()
    w('**Cách 1: thuật toán phân rã.** B1: loại PTH của khóa chính (VT ∪ VP = Q⁺); còn F* = {MaDH,SoDongDH → MaSP; MaSeri → MaSP} ≠ ∅. B2: chọn **MaSeri → MaSP** (vế trái không chứa khóa). Tách Q₁{MaSeri, MaSP} và Q₂ = Q⁺ \\ {MaSP}.')
    w()
    c1 = {'Q1': {'MaSeri', 'MaSP'}, 'Q2': set(attrs_bh) - {'MaSP'}}
    decomp_block('Phép tách PHIEUBAOHANH bằng phân rã', 'PHIEUBAOHANH', Gb, c1)
    w('**Cách 2: thuật toán tổng hợp cải tiến.** B1: phủ tối thiểu G như trên. B2: nhóm theo vế trái: F₁ (MaPhieuBH), F₂ (MaDH, SoDongDH), '
      'F₃ (MaSeri). B3: không có hai vế trái phụ thuộc lẫn nhau. B4: R₁ gồm MaPhieuBH và các thuộc tính phụ thuộc vào nó (trừ MaSP); '
      'R₂{MaDH, SoDongDH, MaSP}; R₃{MaSeri, MaSP}. B5–B6: khóa MaPhieuBH nằm trong R₁ nên không thêm quan hệ.')
    w()
    c2 = {'R1': set(attrs_bh) - {'MaSP'}, 'R2': {'MaDH', 'SoDongDH', 'MaSP'}, 'R3': {'MaSeri', 'MaSP'}}
    decomp_block('Phép tách PHIEUBAOHANH bằng tổng hợp', 'PHIEUBAOHANH', Gb, c2)
    w('**Lựa chọn.** Tổng hợp bảo toàn cả thông tin và PTH. Trong cơ sở dữ liệu, R₂ là một phép chiếu của CHITIETDONHANG '
      'và R₃ nằm trong SERIMATHANG (mục 2.3.5), nên không tạo quan hệ mới: chỉ có R₁ thay PHIEUBAOHANH, tức **bỏ cột MaSP**. Tên hàng lấy '
      'bằng phép nối với CHITIETDONHANG theo (MaDH, SoDongDH). **PHIEUBAOHANH nâng từ 2NF lên BCNF.**')
    w()
    fig('phan_ra_phieubaohanh', 'Hình 2.2: Phân rã PHIEUBAOHANH: bỏ cột MaSP suy ra được')
    # --- HANGCOSERI
    attrs_hs = [a[0] for a in REL['HANGCOSERI']['attrs']]
    Lh = letters(attrs_hs)
    Gh = res['HANGCOSERI']['G']
    w('### 2.3.5 HANGCOSERI: từ 3NF lên BCNF')
    w()
    w('Ánh xạ chữ cái: ' + ', '.join(f'{Lh[a]} = {a}' for a in attrs_hs) + '.')
    w('F (phủ tối thiểu G): ' + grouped(Gh, attrs_hs, limit=0) + '. Các khóa: ' +
      '; '.join(set_str(kk) for kk in res['HANGCOSERI']['keys']['keys']) + '. Đang ở 3NF vì MaSP là thuộc tính khóa (thuộc khóa {SoSeri, MaSP}); '
      'vi phạm BCNF: (MaPN, SoDongPN) → MaSP và (MaDH, SoDongDH) → MaSP có vế trái không chứa khóa.')
    w()
    w('**Cách 1: thuật toán phân rã.** B1: loại PTH của khóa chính (VT ∪ VP = Q⁺); còn F* = {MaSP,SoSeri → MaSeri; MaPN,SoDongPN → MaSP; MaDH,SoDongDH → MaSP} ≠ ∅. B2: chọn **MaPN,SoDongPN → MaSP** (vế trái không chứa khóa). Tách Q₁{MaPN, SoDongPN, MaSP} và Q₂ = Q⁺ \\ {MaSP}; Q₂ có mọi vế trái PTH là khóa nên dừng.')
    w()
    q1 = {'Q1': {'MaPN', 'SoDongPN', 'MaSP'}, 'Q2': set(attrs_hs) - {'MaSP'}}
    decomp_block('Phép tách HANGCOSERI bằng phân rã (Delobel)', 'HANGCOSERI', Gh, q1)
    w('Phép tách bảo toàn thông tin nhưng **mất PTH** (MaSP, SoSeri) → MaSeri, tức quy tắc “số seri duy nhất trong cùng mặt hàng” (G1), '
      'vì MaSP và SoSeri không còn nằm chung một quan hệ, và mất (MaDH, SoDongDH) → MaSP.')
    w()
    w('**Cách 2: thuật toán tổng hợp.** B1: phủ tối thiểu G. B2: nhóm theo vế trái: F₁ (MaSeri), F₂ (MaSP, SoSeri), F₃ (MaPN, SoDongPN), '
      'F₄ (MaDH, SoDongDH). B3: MaSeri → {MaSP, SoSeri} và {MaSP, SoSeri} → MaSeri nên F₁ và F₂ phụ thuộc lẫn nhau, gộp. B4: quan hệ gộp chứa '
      'mọi thuộc tính của Q, tức **chính Q**; hai quan hệ còn lại là tập con của Q nên bị loại. Kết quả của tổng hợp là Q nguyên vẹn, chỉ '
      'đạt 3NF.')
    w()
    w('**Phương án C: bốn thành phần (BCNF, bảo toàn đủ).** Tách Q₁{MaPN, SoDongPN, MaSP}; Q₂{MaDH, SoDongDH, MaSP}; Q₃ gồm MaSeri và các '
      'thuộc tính còn lại trừ MaSP, SoSeri; Q₄{MaSeri, SoSeri, MaSP} (hai khóa MaSeri và {MaSP, SoSeri}).')
    w()
    q4 = {'Q1': {'MaPN', 'SoDongPN', 'MaSP'}, 'Q2': {'MaDH', 'SoDongDH', 'MaSP'},
          'Q3': set(attrs_hs) - {'SoSeri', 'MaSP'}, 'Q4': {'MaSeri', 'SoSeri', 'MaSP'}}
    decomp_block('Phép tách HANGCOSERI theo phương án C', 'HANGCOSERI', Gh, q4)
    w('Q₁ và Q₂ **trùng với phép chiếu của CHITIETPHIEUNHAP và CHITIETDONHANG** (đã có) nên không tạo quan hệ mới. Hai quan hệ cần: '
      '**HANGCOSERI** rút gọn (Q₃, bỏ SoSeri và MaSP) và **SERIMATHANG** mới (Q₄).')
    w()
    w('| Phương án | Dạng chuẩn | Bảo toàn thông tin | Bảo toàn PTH | Quan hệ mới | Ghi chú |')
    w('|---|---|---|---|---|---|')
    w('| Giữ nguyên | 3NF | không cần tách | có | không | MaSP lưu thừa ở mỗi chiếc |')
    w('| Phân rã (Delobel) | BCNF | có | **không** | không | Mất bảo đảm seri duy nhất theo mặt hàng |')
    w('| Tổng hợp | 3NF | có | có | không | Trả lại đúng Q |')
    w('| **C: bốn thành phần** | **BCNF** | **có** | **có** | **SERIMATHANG** | Cần ràng buộc nhất quán MaSP (mục 2.3.6) |')
    w()
    w('**Chọn phương án C**, vì giữ quy tắc “seri duy nhất theo mặt hàng” (G1), đạt BCNF và không mất PTH. **HANGCOSERI nâng từ 3NF lên BCNF.**')
    w()
    fig('phan_ra_hangcoseri', 'Hình 2.3: Phân rã HANGCOSERI thành bốn thành phần (phương án C)')
    sec_236(res)
    sec_4nf()


def sec_236(res):
    w('### 2.3.6 Lược đồ sau cải tiến')
    w()
    w(f'Lược đồ sau cải tiến có **{len(ORDI)} quan hệ** ({len(ORD)} quan hệ ban đầu, thêm SERIMATHANG). Các thay đổi: tách HoTen ở KHACHHANG, NHANVIEN; bỏ '
      'MaDH khỏi CHITIETTRA; bỏ MaSP khỏi PHIEUBAOHANH; HANGCOSERI bỏ SoSeri và MaSP, thêm SERIMATHANG.')
    w()
    for i, n in enumerate(ORDI, 1):
        mark = ' *(đã thay đổi)*' if n in ('KHACHHANG', 'NHANVIEN', 'CHITIETTRA', 'PHIEUBAOHANH', 'HANGCOSERI') else (' *(mới)*' if n == 'SERIMATHANG' else '')
        w(f'{i}. {sig(n, IMP)}{mark}')
    w()
    w('**Ràng buộc nhất quán** không biểu diễn được bằng PTH trong một quan hệ (cưỡng chế bằng khóa ngoại ghép hoặc kiểm tra khi ghi):')
    w()
    w('1. MaSP của SERIMATHANG phải bằng MaSP của dòng nhập (MaPN, SoDongPN) và của dòng đơn (MaDH, SoDongDH) nếu có.')
    w('2. Phiếu bảo hành có MaSeri thì mặt hàng của chiếc hàng (SERIMATHANG.MaSP) phải bằng MaSP của dòng mua gốc (MaDH, SoDongDH).')
    w('3. Dòng đơn trong CHITIETTRA là (MaDH của hồ sơ, SoDongDH) và phải có trong CHITIETDONHANG. Nếu muốn khai báo khóa ngoại ở mức cơ sở '
      'dữ liệu thì khi cài đặt giữ thêm cột MaDH với khóa ngoại ghép (MaHS, MaDH) tới HOSODOITRA; về lý thuyết đó là cột nhân bản có kiểm soát, '
      'không thuộc lược đồ logic.')
    w('4. Khoản hoàn tiền có MaHS thì đơn của khoản thu gốc (THANHTOAN.MaDH) phải bằng đơn của hồ sơ đổi trả (HOSODOITRA.MaDH); đồ thị ở chương 3 cho thấy KHOANHOAN '
      'có hai mạch đi tới DONHANG (qua THANHTOAN và qua HOSODOITRA) nên hai mạch phải cùng dẫn tới một đơn.')
    w()
    w('Các ràng buộc **tài khoản, chức vụ và trách nhiệm** (không biểu diễn được bằng PTH; các quy tắc về chức vụ là **giả thiết** nghiệp vụ của nhóm):')
    w()
    w('5. TAIKHOAN: đúng một trong hai cột MaKH, MaNV có giá trị.')
    w('6. Người thực hiện một khâu phải có chức vụ phù hợp (NHANVIEN.ChucVu): duyệt hoàn tiền (KHOANHOAN.MaNV) và duyệt chuyển nhóm '
      'hàng nhận lại (LANNHANLAI.MaNVDuyet) là Quản lý; chi tiền hoàn (MaNVChi) là Thu ngân; thu tiền khi giao (THANHTOAN.MaNVThu) là Giao hàng; xác nhận phiếu nhập '
      '(PHIEUNHAP.MaNVXacNhan) là Kho; tạo mã giảm giá (MAGIAMGIA.MaNV) là Bán hàng hoặc Quản lý.')
    w('7. Đơn có KenhBan khác "Trang web" phải có MaNV; khách chỉ tự hủy được đơn còn "Chờ xác nhận".')
    w()
    w(f'**Mã SQL đề xuất** (chạy được trên SQL Server và SQLite; toàn bộ {len(ORDI)} bảng ở `sql/01_tao_bang.sql`):')
    w()
    w('```sql')
    w('CREATE TABLE SERIMATHANG (')
    w('    MaSeri INT NOT NULL PRIMARY KEY,')
    w('    SoSeri VARCHAR(60) NOT NULL,')
    w('    MaSP   INT NOT NULL REFERENCES MATHANG(MaSP),')
    w('    CONSTRAINT UQ_SERIMATHANG UNIQUE (MaSP, SoSeri)')
    w(');')
    w('-- Khung nhìn trả lại hình dạng cũ của HANGCOSERI khi cần')
    w('CREATE VIEW vw_HangCoSeri AS')
    w('SELECT h.*, s.SoSeri, s.MaSP FROM HANGCOSERI h JOIN SERIMATHANG s ON s.MaSeri = h.MaSeri;')
    w('```')
    w()
    w('### 2.3.7 So sánh trước và sau cải tiến')
    w()
    w('| Quan hệ | Dư thừa trước | Dị thường trước | Sau cải tiến | Chi phí |')
    w('|---|---|---|---|---|')
    w('| KHACHHANG, NHANVIEN | Họ tên ghi một cột | Lọc theo tên phải dùng LIKE trên một phần giá trị; sắp xếp theo tên khó | HoLot và Ten riêng | Nhập hai ô thay vì một |')
    w('| CHITIETTRA | MaDH lặp lại ở mỗi dòng trả của cùng hồ sơ | **Cập nhật:** sửa đơn gốc của hồ sơ nhưng sót một dòng thì hồ sơ có hai đơn. **Thêm:** dòng trả có MaDH khác đơn của hồ sơ | MaDH chỉ ở HOSODOITRA | Muốn biết đơn của dòng trả phải nối với HOSODOITRA |')
    w('| PHIEUBAOHANH | MaSP lặp ở mỗi phiếu của cùng dòng đơn hoặc cùng chiếc | **Cập nhật:** đổi mặt hàng của dòng đơn mà không sửa phiếu. **Thêm:** phiếu ghi MaSP không khớp dòng mua gốc | MaSP chỉ ở CHITIETDONHANG và SERIMATHANG | Một phép nối với CHITIETDONHANG |')
    w('| HANGCOSERI | MaSP lặp ở mỗi chiếc của cùng dòng nhập; SoSeri gắn MaSP | **Cập nhật:** sửa mặt hàng của dòng nhập mà sót chiếc. **Thêm:** nhập chiếc có MaSP khác MaSP của dòng nhập | MaSP của chiếc chỉ ở SERIMATHANG; khóa {MaSP, SoSeri} được cưỡng chế bằng UNIQUE | Thêm một quan hệ và một phép nối; phải kiểm soát ràng buộc nhất quán 1 |')
    w()
    w('**Nhận xét trung thực.** Với CHITIETTRA và PHIEUBAOHANH, cải tiến loại hẳn dữ liệu thừa. Với HANGCOSERI, cải tiến đưa lược đồ về '
      'BCNF nhưng lượng MaSP lưu không giảm (mỗi chiếc vẫn có một MaSP ở SERIMATHANG); lợi ích là mỗi quan hệ không còn PTH vi phạm và '
      'khóa {MaSP, SoSeri} được cưỡng chế, còn tính nhất quán liên quan hệ do ràng buộc ở 2.3.6 bảo đảm. Chưa đo hiệu năng: thêm một phép nối '
      'có thể làm truy vấn chậm hơn hoặc không, cần đo trên dữ liệu thật.')
    w()


def sec_4nf():
    w('### 2.3.8 Phụ thuộc đa trị và dạng chuẩn 4')
    w()
    w('Theo giáo trình, X ↠ Y (với X ∩ Y = ∅, Z = Q⁺ \\ XY) là phụ thuộc đa trị nếu mỗi giá trị x của X xác định một tập giá trị Y '
      'không phụ thuộc vào Z. Quan hệ đạt 4NF nếu đạt BCNF và mọi phụ thuộc đa trị không hiển nhiên (XY ≠ Q⁺) có X là siêu khóa. '
      'Cách kiểm tra: tách X ↠ Y thành Q[X,Y] và Q[X,Z]; phép tách theo phụ thuộc đa trị luôn bảo toàn thông tin.')
    w()
    w('**Tình huống: ảnh và thông số của mặt hàng.** Theo mô tả (mục 1.4), mỗi mặt hàng có nhiều ảnh minh họa và nhiều giá trị thông số, '
      'và việc thêm hoặc đổi ảnh không làm đổi thông số: hai tập này **độc lập** nhau.')
    w()
    w('*Bước 1. Nếu lưu chung* một quan hệ M(MaSP, DuongDanAnh, MaTS, GiaTriTS), mỗi dòng là một cặp (ảnh, thông số) của mặt hàng:')
    w()
    w('- PTH: (MaSP, MaTS) → GiaTriTS. Khóa của M là {MaSP, DuongDanAnh, MaTS}. PTH này có vế trái là một phần của khóa nên M **không đạt 2NF**.')
    w('- Tách theo PTH: **R₁(MaSP, MaTS, GiaTriTS)** (chính là GIATRITHONGSO) và **R₂(MaSP, DuongDanAnh, MaTS)**.')
    w()
    w('*Bước 2. R₂ đạt BCNF nhưng không đạt 4NF.* R₂ toàn khóa nên **đạt BCNF** (không có PTH không hiển nhiên). Nhưng vì tập ảnh và tập thông '
      'số độc lập nên với mỗi mặt hàng, R₂ phải chứa **mọi cặp** (ảnh, thông số):')
    w()
    w('- **MaSP ↠ DuongDanAnh** (và MaSP ↠ MaTS) là phụ thuộc đa trị không hiển nhiên (MaSP ∪ DuongDanAnh ≠ R₂⁺) mà MaSP không là siêu khóa → R₂ **vi phạm 4NF**.')
    w('- Tách R₂ thành **R₂₁(MaSP, DuongDanAnh)** (ANHMATHANG, với MaAnh làm khóa thay thế) và **R₂₂(MaSP, MaTS)** (đã có trong R₁). Phép tách '
      'bảo toàn thông tin: R₂₁ ∩ R₂₂ = {MaSP} và MaSP ↠ DuongDanAnh.')
    w()
    w('**Kết quả: ANHMATHANG và GIATRITHONGSO đạt 4NF; lược đồ không chứa R₂.**')
    w()
    fig('phan_ra_4nf', 'Hình 2.4: Từ quan hệ lưu chung ảnh và thông số đến dạng chuẩn 4')
    w('**Số liệu minh họa** (tính từ `database/data.seed.sql` của PowerTech: 120 mặt hàng có cả ảnh và thông số; trung bình 2,58 ảnh '
      'và 10,23 thông số mỗi mặt hàng):')
    w()
    w('| Cách lưu | Số dòng |')
    w('|---|---|')
    w('| M (lưu chung, mỗi dòng một cặp ảnh – thông số) | **3.256** (tổng ảnh × thông số theo từng mặt hàng) |')
    w('| ANHMATHANG và GIATRITHONGSO (tách) | **1.538** = 310 ảnh + 1.228 thông số |')
    w()
    w('Lưu chung nhiều dòng hơn khoảng 2,1 lần chỉ để lặp lại cùng thông tin. Dị thường thêm: thêm một ảnh thứ tư cho một mặt hàng đang có '
      '3 thông số buộc thêm 3 dòng ở dạng chung nhưng chỉ 1 dòng ở dạng tách.')
    w()
    w('**Các quan hệ còn lại.** Theo mô tả nghiệp vụ, mỗi quan hệ còn lại chỉ chứa **một** tập giá trị của đối tượng chính (dòng chi tiết, lần giao, '
      'lần nhận lại… đã tách thành quan hệ riêng), nên không chứa hai tập độc lập và không có phụ thuộc đa trị không hiển nhiên ngoài PTH. '
      'Kết luận này dựa trên mô tả nghiệp vụ, **chưa chứng minh tổng quát** (không thể chứng minh bằng dữ liệu mẫu).')
    w()
    w('### 2.3.9 Đánh giá lược đồ sau cải tiến')
    w()
    resi = analyse_all(IMP, ORDI, {})
    w('| STT | Quan hệ | Khóa (mọi khóa ứng viên) | Trước | Sau |')
    w('|---|---|---|---|---|')
    before = analyse_all(REL, ORD, COMPOUND)
    for i, n in enumerate(ORDI, 1):
        x = resi[n]
        ks = '; '.join('{' + ', '.join(k) + '}' for k in x['keys']['keys'])
        b = NF_NAME[before[n]['nf']['nf']] if n in before else '—'
        w(f'| {i} | {n} | {ks} | {b} | {NF_NAME[x["nf"]["nf"]]} |')
    w()
    w('*Bảng 2.3: Dạng chuẩn trước và sau cải tiến*')
    w()
    assert all(x['nf']['nf'] == 4 for x in resi.values())
    w(f'**Dạng chuẩn của lược đồ sau cải tiến: BCNF** (cả {len(ORDI)} quan hệ), và đạt 4NF theo giả định độc lập ở 2.3.8. So với mục 2.2: từ **chưa đạt 1NF** '
      'lên **BCNF/4NF**. Điều kiện đi kèm: (a) các ràng buộc nhất quán và ràng buộc trách nhiệm ở 2.3.6; (b) chọn phương án C với quy tắc “seri duy nhất theo mặt hàng” '
      '(G1) thay cho “seri duy nhất toàn cửa hàng”; (c) họ tên tách theo quy ước G3.')
    w()


def sec_24():
    w('## 2.4 PHÂN TÍCH CHỨC NĂNG VÀ QUY TRÌNH NGHIỆP VỤ')
    w()
    w('Mục này đặt cạnh lược đồ để đối chiếu: Use Case cho biết ai làm chức năng nào trên các quan hệ ở mục 2.1, còn lưu đồ vẽ lại bốn quy trình có quy tắc dễ nhầm nhất, '
      'làm căn cứ cho các ràng buộc ở 2.3.6 và cho các truy vấn ở chương 3. Nội dung nghiệp vụ lấy từ mục 1.4.')
    w()
    w('### 2.4.1 Sơ đồ Use Case')
    w()
    w('Theo báo cáo mẫu, các chức năng được nhóm theo ba loại thực thể (đối tượng ngoài, danh mục cơ bản, nghiệp vụ) cùng hai nhóm chung là tìm kiếm và thống kê. '
      'Tác nhân Nhân viên là khái quát hóa của sáu chức vụ (quản lý, bán hàng, thu ngân, kỹ thuật, kho, giao hàng; giả thiết G6), mỗi chức vụ chỉ làm những chức năng '
      'thuộc quyền của mình; tác nhân Khách hàng dùng trang web để đăng ký tài khoản, đặt hàng, hủy đơn khi còn chờ xác nhận và tra cứu đơn của mình. '
      'Các chức năng nằm trong phạm vi ở mục 1.3; những phần đã loại khỏi phạm vi (giỏ hàng, sổ địa chỉ, nhật ký đơn, lịch sử giữ vai trò) không có ca sử dụng.')
    w()
    for name, title in (('tong_quat', 'Sơ đồ Use Case tổng quát'), ('doi_tuong_ngoai', 'Sơ đồ Use Case quản lý đối tượng ngoài'),
                        ('danh_muc', 'Sơ đồ Use Case quản lý danh mục cơ bản'), ('nghiep_vu', 'Sơ đồ Use Case quản lý nghiệp vụ'),
                        ('tim_kiem', 'Sơ đồ Use Case tìm kiếm'), ('thong_ke', 'Sơ đồ Use Case thống kê')):
        fig(f'usecase_{name}', f'Hình 2.{20 + len(FIG24)}: {title}')
        FIG24.append(name)
    w('### 2.4.2 Lưu đồ các quy trình nghiệp vụ')
    w()
    w('Bốn lưu đồ dưới đây tóm tắt vòng đời tình trạng đơn hàng, đổi trả và hoàn tiền, tiếp nhận bảo hành và ba nhóm hàng trong kho. Các quan hệ liên quan:')
    w()
    w('- Tình trạng đơn hàng: DONHANG, THANHTOAN, PHIEUGIAO, LANGIAO (tối đa 3 lần giao).')
    w('- Đổi trả và hoàn tiền: HOSODOITRA, CHITIETTRA, LANNHANLAI, KHOANHOAN, GIAODICHKHO.')
    w('- Bảo hành: PHIEUBAOHANH, CHITIETDONHANG, HANGCOSERI, SERIMATHANG.')
    w('- Ba nhóm hàng trong kho: GIAODICHKHO, HANGCOSERI, LANNHANLAI.')
    w()
    for name, title in (('don_hang', 'Lưu đồ tình trạng đơn hàng'), ('doi_tra', 'Lưu đồ đổi trả hàng, hoàn tiền'),
                        ('bao_hanh', 'Lưu đồ tiếp nhận và xử lý bảo hành'), ('kho', 'Lưu đồ ba nhóm hàng trong kho')):
        fig(f'luudo_{name}', f'Hình 2.{20 + len(FIG24)}: {title}')
        FIG24.append(name)


def main():
    res = analyse_all(REL, ORD, COMPOUND)
    sec_21()
    sec_22(res)
    sec_23(res)
    sec_24()
    out = os.path.join(HERE, '..', 'chuong', '02_chuong2.md')
    open(out, 'w', encoding='utf-8').write('\n'.join(OUT) + '\n')
    print('đã ghi', os.path.normpath(out), len(OUT), 'dòng')


if __name__ == '__main__':
    main()
