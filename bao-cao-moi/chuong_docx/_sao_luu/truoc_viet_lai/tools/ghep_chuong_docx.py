#!/usr/bin/env python3
"""Ghép 4 file chương (chuong_docx/ChuongN_*.docx) về một bản nộp đầy đủ; ngược lại với tach_chuong_docx.py.

Chạy:  python3 tools/ghep_chuong_docx.py [thư mục 4 chương] [file nền] [file ra]
Mặc định: chuong_docx/ + PowerTech_CSDLNC_Bao_cao_moi.docx -> PowerTech_CSDLNC_Bao_cao_ghep.docx

- File nền cho bìa, mục lục, danh mục hình/bảng, lời mở đầu/cảm ơn/cam đoan, tài liệu tham khảo, khổ giấy, chân trang và
  định nghĩa kiểu chữ. Phần từ "CHƯƠNG 1" đến hết chương 4 của file nền được thay bằng nội dung 4 file chương.
- Hình được chép sang (trùng hình thì dùng chung); kiểu chữ mà file chương có và file nền chưa có được thêm vào.
  Kiểu chữ trùng tên nhưng sửa khác thì lấy theo file nền.
- Chưa hỗ trợ: danh sách đánh số mới, chú thích cuối trang, bình luận, ngắt section trong chương (sẽ cảnh báo hoặc dừng).
- Mục lục và danh mục là trường Word: mở file ghép, chọn "Yes" khi Word hỏi cập nhật trường.
Không ghi đè file nền.
"""
import copy
import io
import os
import sys

from docx import Document
from docx.oxml.ns import qn

HERE = os.path.dirname(os.path.abspath(__file__))
BC = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from tach_chuong_docx import NAMES, heading1, ranges  # noqa: E402

RID = [qn('r:embed'), qn('r:id'), qn('r:link')]
STYLE_XPATH = './/w:pStyle/@w:val | .//w:rStyle/@w:val | .//w:tblStyle/@w:val'


def ensure_style(base, src, sid, seen):
    if sid in seen:
        return
    seen.add(sid)
    if base.styles.element.xpath(f'w:style[@w:styleId="{sid}"]'):
        return
    found = src.styles.element.xpath(f'w:style[@w:styleId="{sid}"]')
    if not found:
        print(f'  cảnh báo: không thấy kiểu "{sid}" ở file chương')
        return
    base.styles.element.append(copy.deepcopy(found[0]))
    print(f'  thêm kiểu chữ "{sid}" từ file chương')
    for parent in found[0].xpath('w:basedOn/@w:val'):
        ensure_style(base, src, parent, seen)


def remap_rels(el, src, base, cache):
    for node in el.iter():
        if not isinstance(node.tag, str):
            continue
        for attr in RID:
            old = node.get(attr)
            if old is None:
                continue
            if old not in cache:
                rel = src.part.rels[old]
                if rel.reltype.endswith('/image'):
                    cache[old] = base.part.get_or_add_image(io.BytesIO(rel.target_part.blob))[0]
                elif rel.is_external and rel.reltype.endswith('/hyperlink'):
                    cache[old] = base.part.relate_to(rel.target_ref, rel.reltype, is_external=True)
                else:
                    sys.exit(f'Dừng: file chương có liên kết loại "{rel.reltype.rsplit("/", 1)[-1]}" (ngắt section, chú thích, bình luận?) '
                             'mà công cụ chưa hỗ trợ.')
            node.set(attr, cache[old])


def ghep(chapter_dir, base_path, out_path):
    if os.path.abspath(out_path) == os.path.abspath(base_path):
        sys.exit('File ra trùng file nền; chọn tên khác.')
    base = Document(base_path)
    body = base.element.body
    kids = list(body)
    rng = ranges(body)
    assert sorted(rng) == [1, 2, 3, 4] and all(rng[k][1] == rng[k + 1][0] for k in (1, 2, 3)), 'file nền không có 4 chương liền nhau'
    anchor = kids[rng[4][1]]                                  # tiêu đề kế tiếp sau chương 4 (tài liệu tham khảo)
    for el in kids[rng[1][0]:rng[4][1]]:
        body.remove(el)

    for n in (1, 2, 3, 4):
        path = os.path.join(chapter_dir, NAMES[n] + '.docx')
        src = Document(path)
        els = [e for e in src.element.body if e.tag != qn('w:sectPr')]
        first = next((heading1(e) for e in els if heading1(e) is not None), None)
        if not first or not first.startswith(f'CHƯƠNG {n}'):
            sys.exit(f'{path}: tiêu đề Heading 1 đầu tiên phải bắt đầu bằng "CHƯƠNG {n}", đang là {first!r}')
        cache, seen = {}, set()
        for e in els:
            e = copy.deepcopy(e)
            for sid in set(e.xpath(STYLE_XPATH)):
                ensure_style(base, src, sid, seen)
            if e.xpath('.//w:numPr'):
                print(f'  cảnh báo (chương {n}): có danh sách đánh số, định dạng danh sách chưa được chép; kiểm tra lại sau khi ghép')
            if e.xpath('.//w:footnoteReference | .//w:commentReference'):
                print(f'  cảnh báo (chương {n}): có chú thích cuối trang hoặc bình luận, sẽ không được chép')
            remap_rels(e, src, base, cache)
            anchor.addprevious(e)
        print(f'Chương {n}: {len(els)} phần tử từ {os.path.basename(path)}')

    # id hình (wp:docPr) phải duy nhất trong cả tài liệu
    for i, d in enumerate(body.iter(qn('wp:docPr')), 1):
        d.set('id', str(i))
    # bỏ hình của bản chương cũ trong file nền mà không còn chỗ nào dùng
    used = set(body.xpath('.//@r:embed | .//@r:id | .//@r:link'))
    for rid in list(base.part.rels):
        if base.part.rels[rid].reltype.endswith('/image') and rid not in used:
            del base.part.rels[rid]
    base.save(out_path)
    print(f'-> {out_path} ({os.path.getsize(out_path) / 1e6:.1f} MB)')


if __name__ == '__main__':
    a = sys.argv
    ghep(a[1] if len(a) > 1 else os.path.join(BC, 'chuong_docx'),
         a[2] if len(a) > 2 else os.path.join(BC, 'PowerTech_CSDLNC_Bao_cao_moi.docx'),
         a[3] if len(a) > 3 else os.path.join(BC, 'PowerTech_CSDLNC_Bao_cao_ghep.docx'))
