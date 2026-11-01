#!/usr/bin/env python3
"""Tách bản nộp .docx thành 4 file, mỗi file một chương (CHƯƠNG 1–4), giữ nguyên định dạng, bảng, hình.

Chạy:  python3 tools/tach_chuong_docx.py [file .docx nguồn] [thư mục đầu ra]
Mặc định: PowerTech_CSDLNC_Bao_cao_moi.docx -> chuong_docx/ (cạnh file nguồn).

Mỗi file chỉ chứa tiêu đề và nội dung của một chương. Bìa, mục lục, lời mở đầu và tài liệu tham khảo
không thuộc chương nào nên không nằm trong 4 file này (vẫn ở file đầy đủ).
Chú thích bảng/hình đã đánh số theo chương (trường SEQ, chương nào bắt đầu lại từ 1) nên số không đổi khi tách.
Không ghi đè file nguồn.
"""
import os
import re
import sys

from docx import Document
from docx.oxml.ns import qn

HERE = os.path.dirname(os.path.abspath(__file__))
BC = os.path.dirname(HERE)
NAMES = {1: 'Chuong1_Tong_quan', 2: 'Chuong2_Thiet_ke_va_chuan_hoa', 3: 'Chuong3_Ket_qua_thuc_nghiem', 4: 'Chuong4_Ket_luan_va_kien_nghi'}


def heading1(el):
    ppr = el.find(qn('w:pPr')) if el.tag == qn('w:p') else None
    st = ppr.find(qn('w:pStyle')) if ppr is not None else None
    if st is None or st.get(qn('w:val')) != 'Heading1':
        return None
    return ''.join(t.text or '' for t in el.iter(qn('w:t')))


def ranges(body):
    """Chương n -> (chỉ số tiêu đề, chỉ số tiêu đề Heading 1 kế tiếp)."""
    kids = list(body)
    heads = [(i, heading1(el)) for i, el in enumerate(kids) if heading1(el) is not None]
    out = {}
    for k, (i, text) in enumerate(heads):
        m = re.match(r'CHƯƠNG\s+(\d+)', text)
        if m:
            out[int(m.group(1))] = (i, heads[k + 1][0] if k + 1 < len(heads) else len(kids) - 1)
    return out


def split(src, outdir):
    os.makedirs(outdir, exist_ok=True)
    rng = ranges(Document(src).element.body)
    assert sorted(rng) == [1, 2, 3, 4], f'không thấy đủ 4 chương: {sorted(rng)}'
    for n, (a, b) in sorted(rng.items()):
        doc = Document(src)                                   # nạp lại để mỗi chương cắt từ bản nguyên
        body = doc.element.body
        for k, el in enumerate(list(body)):
            if el.tag != qn('w:sectPr') and not (a <= k < b):  # giữ sectPr cuối: khổ giấy, lề, chân trang
                body.remove(el)
        used = set(body.xpath('.//@r:embed | .//@r:id | .//@r:link'))   # drop_rel không đếm r:embed nên tự kiểm
        for rid in list(doc.part.rels):                       # bỏ hình của chương khác để file không phình
            if doc.part.rels[rid].reltype.endswith('/image') and rid not in used:
                del doc.part.rels[rid]
        doc.core_properties.title = f'PowerTech – Chương {n}'
        path = os.path.join(outdir, NAMES[n] + '.docx')
        doc.save(path)
        print(f'Chương {n}: phần tử {a}–{b - 1} -> {path} ({os.path.getsize(path) / 1e6:.1f} MB)')


if __name__ == '__main__':
    src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(BC, 'PowerTech_CSDLNC_Bao_cao_moi.docx')
    split(src, sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.abspath(src)), 'chuong_docx'))
