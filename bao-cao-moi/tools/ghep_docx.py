#!/usr/bin/env python3
"""Ghép các chương (chuong/*.md) thành bản nộp .docx theo bố cục báo cáo mẫu.

Chạy:  python3 tools/ghep_docx.py [file .docx đầu ra]
- Bìa, lời mở đầu, lời cảm ơn, lời cam đoan, mục lục, danh mục hình, danh mục bảng (trường Word, cập nhật khi mở bằng F9).
- Khóa chính gạch chân liền, khóa ngoại gạch chân nét đứt (từ <u> và <span ... underline dashed>).
- Chú thích bảng (phía trên) và hình (phía dưới) đánh số theo chương bằng trường SEQ; các tham chiếu "bảng x.y" trong văn bản được đổi theo số mới.
- Mọi hình nằm gọn trong một trang A4 dọc (tối đa 16 × 21 cm, kèm chú thích); không dùng trang ngang.
"""
import glob
import os
import re
import sys

from docx import Document
from docx.enum.section import WD_ORIENT
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_UNDERLINE
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
BC = os.path.dirname(HERE)
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(BC, 'PowerTech_CSDLNC_Bao_cao_moi.docx')
FONT = 'Times New Roman'
FILES = sorted(os.path.basename(f) for f in glob.glob(os.path.join(BC, 'chuong', '0[0-6]_*.md')))
CHAP = {f: int(f[:2]) for f in FILES}


# ======================= 1. ĐỌC MARKDOWN =======================
def parse(path):
    lines = open(path, encoding='utf-8').read().split('\n')
    out, i = [], 0
    while i < len(lines):
        l = lines[i]
        if l.startswith('```'):
            lang = l[3:].strip(); j = i + 1; body = []
            while j < len(lines) and not lines[j].startswith('```'):
                body.append(lines[j]); j += 1
            out.append(dict(t='code', lang=lang, lines=body)); i = j + 1; continue
        if l.startswith('|'):
            j = i; rows = []
            while j < len(lines) and lines[j].startswith('|'):
                cells = re.split(r'(?<!\\)\|', lines[j].strip())[1:-1]
                cells = [c.strip().replace('\\|', '|') for c in cells]
                if not all(re.fullmatch(r':?-{2,}:?', c) for c in cells):
                    rows.append(cells)
                j += 1
            out.append(dict(t='table', rows=rows)); i = j; continue
        m = re.match(r'^(#{1,4})\s+(.*)', l)
        if m:
            out.append(dict(t='h', lvl=len(m.group(1)), text=m.group(2).strip())); i += 1; continue
        if not l.strip() or l.strip() == '---':
            i += 1; continue
        m = re.match(r'^!\[([^\]]*)\]\(([^)]+)\)\s*$', l.strip())
        if m:
            out.append(dict(t='img', alt=m.group(1), path=m.group(2))); i += 1; continue
        m = re.match(r'^\*(Bảng|Hình) (\d+\.\d+): (.*)\*\s*$', l.strip())
        if m:
            out.append(dict(t='cap', kind=m.group(1), old=m.group(2), title=m.group(3))); i += 1; continue
        m = re.match(r'^(\s*)[-*]\s+(.*)', l)
        if m:
            out.append(dict(t='li', lvl=len(m.group(1)) // 2 + 1, text=m.group(2), ord=None)); i += 1; continue
        m = re.match(r'^(\s*)(\d+)\.\s+(.*)', l)
        if m:
            out.append(dict(t='li', lvl=len(m.group(1)) // 2 + 1, text=m.group(3), ord=m.group(2))); i += 1; continue
        out.append(dict(t='p', text=l.strip())); i += 1
    return out


def plain(t):
    t = re.sub(r'<[^>]+>', '', t)
    return re.sub(r'[*`]', '', t)


def assign_captions(bl, chap, state):
    """Gắn chú thích cho bảng và hình; trả (khối mới, ánh xạ nhãn cũ -> nhãn mới)."""
    out, last_h, refmap, k = [], '', {}, 0
    while k < len(bl):
        b = bl[k]
        nxt = bl[k + 1] if k + 1 < len(bl) else None
        if b['t'] == 'h':
            last_h = re.sub(r'^[\d.]+\s*', '', b['text'])
            out.append(b); k += 1; continue
        if b['t'] == 'cap':
            k += 1; continue
        if b['t'] in ('table', 'img'):
            kind = 'Bảng' if b['t'] == 'table' else 'Hình'
            title = old = None
            if nxt and nxt['t'] == 'cap' and nxt['kind'] == kind:
                title, old = nxt['title'], nxt['old']
                k += 1
            elif kind == 'Bảng':
                if out and out[-1]['t'] == 'p':
                    prev = out[-1]['text']
                    m = re.match(r'^\*\*\d+/ Bảng (\w+)\*\*', prev)
                    if m:
                        title = f'Thuộc tính của bảng {m.group(1)}'; out.pop()
                    elif prev.startswith('Bảng tổ hợp'):
                        title = f'Bảng tổ hợp tìm khóa, {last_h}'
                    elif 'Bảng khởi tạo' in prev:
                        title = f'Bảng a/b khởi tạo, {last_h}'
                    elif prev.startswith('Bảng sau biến đổi'):
                        title = f'Bảng a/b sau biến đổi, {last_h}'
                if title is None:
                    title = last_h
            else:
                title = b.get('alt') or last_h
            state[kind] += 1
            b['cap'] = dict(kind=kind, chap=chap, n=state[kind], title=title.rstrip('.'))
            if old is not None:
                refmap[f'{kind} {old}'] = f'{kind} {chap}.{state[kind]}'
                refmap[f'{kind.lower()} {old}'] = f'{kind.lower()} {chap}.{state[kind]}'
            out.append(b); k += 1; continue
        out.append(b); k += 1
    return out, refmap


# ======================= 2. DOCX =======================
doc = Document()
sec0 = doc.sections[0]


def page_setup(sec):
    sec.orientation = WD_ORIENT.PORTRAIT; sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
    sec.left_margin, sec.right_margin, sec.top_margin, sec.bottom_margin = Cm(3.0), Cm(2.0), Cm(2.0), Cm(2.0)


page_setup(sec0)


def set_font(style, size, bold=None, italic=None, color=True):
    style.font.name = FONT; style.font.size = Pt(size)
    if bold is not None: style.font.bold = bold
    if italic is not None: style.font.italic = italic
    if color: style.font.color.rgb = RGBColor(0, 0, 0)
    rpr = style.element.get_or_add_rPr(); rf = rpr.find(qn('w:rFonts'))
    if rf is None:
        rf = OxmlElement('w:rFonts'); rpr.append(rf)
    for a in ('w:ascii', 'w:hAnsi', 'w:eastAsia', 'w:cs'): rf.set(qn(a), FONT)
    for a in ('w:asciiTheme', 'w:hAnsiTheme', 'w:eastAsiaTheme', 'w:cstheme'):
        if rf.get(qn(a)) is not None: del rf.attrib[qn(a)]


ST = doc.styles
set_font(ST['Normal'], 13)
for name, size, bold, ital in (('Heading 1', 16, True, False), ('Heading 2', 14, True, False), ('Heading 3', 13, True, False), ('Heading 4', 13, True, True)):
    st = ST[name]; set_font(st, size, bold, ital)
    st.paragraph_format.space_before = Pt(14 if name == 'Heading 1' else 10); st.paragraph_format.space_after = Pt(6)
    st.paragraph_format.keep_with_next = True
ST['Heading 1'].paragraph_format.page_break_before = True
set_font(ST['List Bullet'], 13); set_font(ST['List Bullet 2'], 13)
set_font(ST['Caption'], 11, True, False)
ST['Caption'].paragraph_format.space_before = Pt(6); ST['Caption'].paragraph_format.space_after = Pt(4)
code_style = ST.add_style('MaNguon', WD_STYLE_TYPE.PARAGRAPH)
code_style.base_style = ST['Normal']; code_style.font.name = 'Courier New'; code_style.font.size = Pt(9)
code_style.paragraph_format.space_after = Pt(0); code_style.paragraph_format.line_spacing = 1.0
cr = code_style.element.get_or_add_rPr(); rf = cr.find(qn('w:rFonts'))
if rf is None:
    rf = OxmlElement('w:rFonts'); cr.append(rf)
for a in ('w:ascii', 'w:hAnsi', 'w:eastAsia', 'w:cs'): rf.set(qn(a), 'Courier New')
tit_style = ST.add_style('TieuDeMucLuc', WD_STYLE_TYPE.PARAGRAPH); tit_style.base_style = ST['Normal']
set_font(tit_style, 16, True); tit_style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
tit_style.paragraph_format.space_before = Pt(12); tit_style.paragraph_format.space_after = Pt(12)
tit_style.paragraph_format.page_break_before = True

PPR_AFTER_SHD = ['tabs', 'suppressAutoHyphens', 'kinsoku', 'wordWrap', 'overflowPunct', 'topLinePunct', 'autoSpaceDE', 'autoSpaceDN', 'bidi',
                 'adjustRightInd', 'snapToGrid', 'spacing', 'ind', 'contextualSpacing', 'mirrorIndents', 'suppressOverlap', 'jc',
                 'textDirection', 'textAlignment', 'textboxTightWrap', 'outlineLvl', 'divId', 'cnfStyle', 'rPr', 'sectPr', 'pPrChange']


def insert_before(parent, el, successors):
    for ch in parent:
        if ch.tag in {qn('w:' + x) for x in successors}:
            ch.addprevious(el); return
    parent.append(el)


def shade(el_pr, fill):
    sh = OxmlElement('w:shd'); sh.set(qn('w:val'), 'clear'); sh.set(qn('w:color'), 'auto'); sh.set(qn('w:fill'), fill)
    if el_pr.tag == qn('w:pPr'): insert_before(el_pr, sh, PPR_AFTER_SHD)
    else: el_pr.append(sh)


def fld(par, instr, cached, bold=None):
    for typ in ('begin', None, 'separate', 'text', 'end'):
        r = par.add_run()
        if bold is not None: r.bold = bold
        if typ in ('begin', 'separate', 'end'):
            e = OxmlElement('w:fldChar'); e.set(qn('w:fldCharType'), typ); r._r.append(e)
        elif typ is None:
            e = OxmlElement('w:instrText'); e.set(qn('xml:space'), 'preserve'); e.text = instr; r._r.append(e)
        else:
            r.text = cached


TOKEN = re.compile(r'(\*\*|`|<u>|</u>|<span[^>]*>|</span>|<sup>|</sup>|\[[^\]]+\]\([^)]+\)|\\[*_`\[\]|]|\*)')


def add_inline(par, text, size=None, bold=False, italic=False):
    st = dict(b=bold, i=italic, u=None, sup=False)
    stack_span = []

    def emit(s):
        if not s: return
        r = par.add_run(s); r.bold = st['b'] or None; r.italic = st['i'] or None
        if st['u']: r.underline = st['u']
        if st['sup']: r.font.superscript = True
        if size: r.font.size = Pt(size)
    parts = TOKEN.split(text)
    k = 0
    while k < len(parts):
        tok = parts[k]; k += 1
        if not TOKEN.fullmatch(tok):
            emit(tok); continue
        if tok == '**': st['b'] = not st['b']
        elif tok == '*':
            prev = ''.join(parts[:k - 1])[-1:] if k > 1 else ''
            nxt = parts[k][:1] if k < len(parts) else ''
            if not st['i'] and (prev == '' or prev in ' (—–-/') and nxt not in ('', ' '): st['i'] = True
            elif st['i'] and prev not in ('', ' '): st['i'] = False
            else: emit('*')
        elif tok == '`':
            j = k; lit = []
            while j < len(parts) and parts[j] != '`': lit.append(parts[j]); j += 1
            k = j + 1
            r = par.add_run(''.join(lit)); r.font.name = 'Courier New'; r.font.size = Pt((size or 13) - 1.5)
            r._r.get_or_add_rPr().find(qn('w:rFonts')).set(qn('w:eastAsia'), 'Courier New')
            if st['b']: r.bold = True
        elif tok == '<u>': st['u'] = WD_UNDERLINE.SINGLE
        elif tok == '</u>': st['u'] = None
        elif tok.startswith('<span'):
            stack_span.append(st['u'])
            if 'dashed' in tok: st['u'] = WD_UNDERLINE.DASH
            elif 'underline' in tok: st['u'] = WD_UNDERLINE.SINGLE
        elif tok == '</span>': st['u'] = stack_span.pop() if stack_span else None
        elif tok == '<sup>': st['sup'] = True
        elif tok == '</sup>': st['sup'] = False
        elif tok.startswith('['):
            m = re.match(r'\[([^\]]+)\]\(([^)]+)\)', tok); emit(m.group(1))
        elif tok.startswith('\\'): emit(tok[1:])


def conv_text(t, refmap):
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: m.group(1), t)
    if refmap:
        t = re.sub('|'.join(re.escape(k) + r'(?![0-9A-Za-z.])' for k in sorted(refmap, key=len, reverse=True)), lambda m: refmap[m.group(0)], t)
    return t


# ---- trang bìa ----
def center(text, size, bold=False, before=0, after=6, italic=False):
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(before); p.paragraph_format.space_after = Pt(after)
    r = p.add_run(text); r.bold = bold; r.italic = italic; r.font.size = Pt(size)
    return p


def left(text, size=13, bold=False, indent=3.0, after=4):
    p = doc.add_paragraph(); p.paragraph_format.left_indent = Cm(indent); p.paragraph_format.space_after = Pt(after)
    r = p.add_run(text); r.bold = bold; r.font.size = Pt(size)
    return p


sec0.different_first_page_header_footer = True
center('TRƯỜNG ĐẠI HỌC CÔNG NGHỆ TP.HCM', 14, True, 0, 2)
center('KHOA CÔNG NGHỆ THÔNG TIN', 14, True, 0, 40)
center('BÁO CÁO ĐỒ ÁN HỌC PHẦN', 18, True, 20, 6)
center('CƠ SỞ DỮ LIỆU NÂNG CAO', 20, True, 0, 30)
center('POWERTECH', 24, True, 10, 6)
center('PHÂN TÍCH, THIẾT KẾ VÀ CHUẨN HÓA CƠ SỞ DỮ LIỆU', 16, True, 0, 4)
center('CỬA HÀNG BÁN LẺ LINH KIỆN MÁY TÍNH', 16, True, 0, 40)
left('Ngành:\tCông nghệ thông tin', 13, False, 3.0)
left('Lớp:\t23DTHD6 – Nhóm 6', 13, False, 3.0)
left('Giảng viên hướng dẫn:\tThS. Võ Hoàng Khang', 13, False, 3.0, 10)
left('Sinh viên thực hiện:', 13, True, 3.0, 2)
for n, m in (('Nguyễn Ngọc Tình (trưởng nhóm)', '2380614851'), ('Đỗ Thanh Hoàng Đức Nhả', '2380601510'), ('Võ Thành Đông', '2380600518')):
    left(f'{n} – MSSV: {m}', 13, False, 3.5, 2)
center('TP. Hồ Chí Minh, năm 2026', 13, False, 60)

# ---- chuẩn bị nội dung ----
state = dict(Bảng=0, Hình=0)
CH = {}
for f in FILES:
    bl = parse(os.path.join(BC, 'chuong', f))
    state['Bảng'] = state['Hình'] = 0
    CH[f] = assign_captions(bl, CHAP[f], state)
allmap = {}
for f in FILES:
    allmap.update(CH[f][1])
heads = [(b['lvl'], conv_text(b['text'], allmap)) for f in FILES for b in CH[f][0] if b['t'] == 'h' and b['lvl'] <= 3]
caps = {'Bảng': [], 'Hình': []}
for f in FILES:
    for b in CH[f][0]:
        if 'cap' in b:
            c = b['cap']; caps[c['kind']].append(f"{c['kind']} {c['chap']}.{c['n']}. {conv_text(c['title'], allmap)}")


def toc_block(title, instr, entries):
    p = doc.add_paragraph(style='TieuDeMucLuc'); p.add_run(title)
    first = True
    for k, (lvl, text) in enumerate(entries):
        p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.left_indent = Cm(0.7 * (lvl - 1))
        if first:
            for typ in ('begin', 'instr', 'separate'):
                r = p.add_run()
                if typ == 'instr':
                    e = OxmlElement('w:instrText'); e.set(qn('xml:space'), 'preserve'); e.text = instr
                else:
                    e = OxmlElement('w:fldChar'); e.set(qn('w:fldCharType'), typ)
                r._r.append(e)
            first = False
        r = p.add_run(text); r.font.size = Pt(12 if lvl > 1 else 12.5); r.bold = (lvl == 1) or None
        if k == len(entries) - 1:
            r = p.add_run(); e = OxmlElement('w:fldChar'); e.set(qn('w:fldCharType'), 'end'); r._r.append(e)


clean = lambda t: re.sub(r'[*`]', '', plain(t))
toc_block('MỤC LỤC', ' TOC \\o "1-3" \\h \\z \\u ', [(l, clean(t)) for l, t in heads])
toc_block('DANH MỤC HÌNH', ' TOC \\h \\z \\c "Hinh" ', [(1, clean(c)) for c in caps['Hình']])
toc_block('DANH MỤC BẢNG', ' TOC \\h \\z \\c "Bang" ', [(1, clean(c)) for c in caps['Bảng']])


seq_first = {}


def caption(kind, chap, n, title, above=True):
    p = doc.add_paragraph(style='Caption')
    p.paragraph_format.keep_with_next = above
    if not above: p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    ident = 'Bang' if kind == 'Bảng' else 'Hinh'
    p.add_run(f'{kind} {chap}.')
    key = (ident, chap)
    instr = f' SEQ {ident} \\* ARABIC' + ('' if key in seq_first else ' \\r 1') + ' '
    seq_first[key] = True
    fld(p, instr, str(n), bold=True)
    p.add_run('. ')
    add_inline(p, title, size=11, bold=True)


def set_cell_margins(table, top=40, bottom=40, left=70, right=70):
    tblPr = table._tbl.tblPr; m = OxmlElement('w:tblCellMar')
    for k, v in (('top', top), ('left', left), ('bottom', bottom), ('right', right)):
        e = OxmlElement(f'w:{k}'); e.set(qn('w:w'), str(v)); e.set(qn('w:type'), 'dxa'); m.append(e)
    insert_before(tblPr, m, ['tblLook', 'tblCaption', 'tblDescription'])


def build_table(rows, width_cm, refmap):
    ncol = max(len(r) for r in rows)
    rows = [r + [''] * (ncol - len(r)) for r in rows]
    size = 10 if ncol <= 4 else (9.5 if ncol <= 6 else 9)
    t = doc.add_table(rows=len(rows), cols=ncol); t.style = 'Table Grid'; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    bd = OxmlElement('w:tblBorders')
    for k in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        e = OxmlElement(f'w:{k}'); e.set(qn('w:val'), 'single'); e.set(qn('w:sz'), '4'); e.set(qn('w:space'), '0'); e.set(qn('w:color'), '7F7F7F'); bd.append(e)
    insert_before(t._tbl.tblPr, bd, ['shd', 'tblLayout', 'tblCellMar', 'tblLook', 'tblCaption', 'tblDescription'])
    set_cell_margins(t)
    wts = []
    for c in range(ncol):
        L = [len(plain(r[c])) for r in rows]
        # ô ngắn (≤ 12 ký tự) không được ngắt dòng nên cột phải đủ rộng cho cả ô
        words = max((len(plain(r[c])) if len(plain(r[c])) <= 12 else max((len(w) for w in plain(r[c]).split()), default=0) for r in rows), default=3)
        wts.append(max(3.0, min(max(max(L) ** 0.75 * 1.6, words * (1.55 if words <= 12 else 1.6)), 38)))   # tên quan hệ dài không bị bẻ giữa từ
    tot = sum(wts); widths = [max(1.1, width_cm * w / tot) for w in wts]
    s = sum(widths); widths = [w * width_cm / s for w in widths]
    # cột không hẹp hơn từ dài nhất, tránh ngắt giữa tên quan hệ
    mins = [min(4.6, max((len(w) for r in rows for w in plain(r[c]).split()), default=0) * 0.235 * size / 9.5 + 0.4) for c in range(ncol)]
    if sum(mins) < width_cm:
        du = [max(0, w - m) for w, m in zip(widths, mins)]
        widths = [m + d * (width_cm - sum(mins)) / (sum(du) or 1) for m, d in zip(mins, du)]
    for ri, r in enumerate(rows):
        row = t.rows[ri]
        trPr = row._tr.get_or_add_trPr(); trPr.append(OxmlElement('w:cantSplit'))
        if ri == 0: trPr.append(OxmlElement('w:tblHeader'))
        for ci in range(ncol):
            cell = row.cells[ci]; cell.width = Cm(widths[ci])
            p = cell.paragraphs[0]; p.paragraph_format.space_after = Pt(0); p.paragraph_format.line_spacing = 1.0
            txt = conv_text(r[ci], refmap)
            if len(plain(txt)) <= 12: txt = txt.replace(' ', '\u00a0')   # ô ngắn không xuống dòng ("11 → 10", "siêu khóa")
            add_inline(p, txt, size=size, bold=(ri == 0))
            if ri == 0: shade(cell._tc.get_or_add_tcPr(), 'D9E2F3')
    tw = t._tbl.tblPr.find(qn('w:tblW'))
    if tw is None:
        tw = OxmlElement('w:tblW'); insert_before(t._tbl.tblPr, tw, ['jc', 'tblCellSpacing', 'tblInd', 'tblBorders', 'shd', 'tblLayout', 'tblCellMar', 'tblLook'])
    tw.set(qn('w:type'), 'dxa'); tw.set(qn('w:w'), str(int(width_cm * 567)))
    for gc, w in zip(t._tbl.tblGrid.findall(qn('w:gridCol')), widths): gc.set(qn('w:w'), str(int(w * 567)))


def add_list_item(b, refmap):
    text = conv_text(b['text'], refmap)
    if b['ord'] is None:
        p = doc.add_paragraph(style='List Bullet' if b['lvl'] == 1 else 'List Bullet 2')
        add_inline(p, text)
    else:
        p = doc.add_paragraph(); p.paragraph_format.left_indent = Cm(1.0 + 0.8 * (b['lvl'] - 1))
        p.paragraph_format.first_line_indent = Cm(-0.75)
        add_inline(p, f"{b['ord']}. " + text)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY; p.paragraph_format.space_after = Pt(4); p.paragraph_format.line_spacing = 1.15


def add_code(lines):
    p = doc.add_paragraph(style='MaNguon')
    p.paragraph_format.left_indent = Cm(0.3); p.paragraph_format.space_before = Pt(4); p.paragraph_format.space_after = Pt(8)
    shade(p._p.get_or_add_pPr(), 'F2F2F2')
    for k, ln in enumerate(lines):
        r = p.add_run(ln.replace('\t', '    '))
        if k < len(lines) - 1: r.add_break(WD_BREAK.LINE)


def add_image(path):
    full = os.path.join(BC, path)
    w, h = Image.open(full).size
    maxw, maxh = 16.0, 21.0
    wc = maxw; hc = wc * h / w
    if hc > maxh: hc = maxh; wc = hc * w / h
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.keep_with_next = True
    p.add_run().add_picture(full, width=Cm(wc))


for f in FILES:
    bl, refmap = CH[f]; chap = CHAP[f]
    for b in bl:
        t = b['t']
        if t == 'h':
            p = doc.add_paragraph(style=f"Heading {b['lvl']}")
            if b['lvl'] == 1: p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            add_inline(p, conv_text(b['text'], refmap))
        elif t == 'p':
            p = doc.add_paragraph(); add_inline(p, conv_text(b['text'], refmap))
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY; p.paragraph_format.space_after = Pt(6); p.paragraph_format.line_spacing = 1.15
        elif t == 'li':
            add_list_item(b, refmap)
        elif t == 'table':
            cap = b['cap']
            caption('Bảng', cap['chap'], cap['n'], conv_text(cap['title'], refmap), above=True)
            build_table(b['rows'], 16.0, refmap)
            doc.add_paragraph().paragraph_format.space_after = Pt(4)
        elif t == 'img':
            cap = b['cap']
            add_image(b['path'])
            caption('Hình', cap['chap'], cap['n'], conv_text(cap['title'], refmap), above=False)
        elif t == 'code':
            add_code(b['lines'])

fp = sec0.footer.paragraphs[0]; fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
fld(fp, ' PAGE ', '1')
settings = doc.settings.element
uf = OxmlElement('w:updateFields'); uf.set(qn('w:val'), 'true')
insert_before(settings, uf, ['hdrShapeDefaults', 'footnotePr', 'endnotePr', 'compat', 'docVars', 'rsids', 'mathPr', 'attachedSchema', 'themeFontLang',
                             'clrSchemeMapping', 'doNotIncludeSubdocsInStats', 'doNotAutoCompressPictures', 'forceUpgrade', 'captions',
                             'readModeInkLockDown', 'smartTagType', 'schemaLibrary', 'shapeDefaults', 'doNotEmbedSmartTags', 'decimalSymbol', 'listSeparator'])
doc.core_properties.title = 'Báo cáo CSDL nâng cao - PowerTech'
doc.core_properties.author = 'Nhóm 6 - 23DTHD6'
doc.save(OUT)
print('đã lưu', OUT, '| bảng', len(caps['Bảng']), '| hình', len(caps['Hình']))
