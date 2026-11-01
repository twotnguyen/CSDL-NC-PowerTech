#!/usr/bin/env python3
"""Ghép các mục 1-10 (Markdown) thành bản nộp .docx.

Chạy:  python3 bao-cao/tools/ghep_docx.py [thư mục ảnh sơ đồ] [file .docx đầu ra]
- Khóa chính gạch chân liền, khóa ngoại gạch đứt (từ <u> và <span ... underline dashed>).
- Mục lục, danh mục hình, danh mục bảng là trường Word (TOC); Word cập nhật khi mở (số trang).
- Chú thích bảng/hình đánh số "Bảng <mục>.<n>", "Hình <mục>.<n>" bằng trường SEQ.
- Bỏ các phần dành cho ôn tập ("Câu hỏi giảng viên có thể hỏi"); sơ đồ Mermaid lấy từ ảnh PNG đã xuất.
"""
import os, re, sys, glob
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_UNDERLINE, WD_BREAK
from docx.enum.section import WD_ORIENT, WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = os.path.dirname(os.path.abspath(__file__))
BC = os.path.dirname(HERE)
IMG_DIR = sys.argv[1] if len(sys.argv) > 1 else os.path.join(BC, 'hinh')
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(BC, 'PowerTech_CSDLNC_Bao_cao.docx')
FONT = 'Times New Roman'
FILES = ['01_Mo_ta_de_tai_v3.md'] + sorted(os.path.basename(f) for f in glob.glob(os.path.join(BC, '0[2-9]_*.md'))) + \
        sorted(os.path.basename(f) for f in glob.glob(os.path.join(BC, '10_*.md')))
if os.environ.get('GHEP_THU'):
    FILES = os.environ['GHEP_THU'].split(',')   # chạy thử một vài mục, bỏ bìa và mục lục
THU = bool(os.environ.get('GHEP_THU'))
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
                if not all(re.fullmatch(r':?-{2,}:?', c) for c in cells): rows.append(cells)
                j += 1
            out.append(dict(t='table', rows=rows)); i = j; continue
        m = re.match(r'^(#{1,4})\s+(.*)', l)
        if m:
            out.append(dict(t='h', lvl=len(m.group(1)), text=m.group(2).strip())); i += 1; continue
        if not l.strip() or l.strip() == '---':
            i += 1; continue
        m = re.match(r'^(\s*)[-*]\s+(.*)', l)
        if m:
            out.append(dict(t='li', lvl=len(m.group(1)) // 2 + 1, text=m.group(2), ord=None)); i += 1; continue
        m = re.match(r'^(\s*)(\d+)\.\s+(.*)', l)
        if m:
            out.append(dict(t='li', lvl=len(m.group(1)) // 2 + 1, text=m.group(3), ord=m.group(2))); i += 1; continue
        out.append(dict(t='p', text=l.strip())); i += 1
    return out

def filter_blocks(bl):
    """Bỏ phần ôn tập, bỏ bullet 'Cần hỏi giảng viên', sửa tiêu đề hỗn hợp."""
    out, skip_lvl, skip_q = [], None, False
    for b in bl:
        if b['t'] == 'h':
            skip_q = False
            if skip_lvl is not None and b['lvl'] > skip_lvl:
                continue
            skip_lvl = None
            if re.search(r'^[\d.]+\s*Câu hỏi giảng viên có thể hỏi$', b['text']):
                skip_lvl = b['lvl']; continue
            b['text'] = re.sub(r'\s+và câu hỏi giảng viên có thể hỏi$', '', b['text'])
            ma = re.match(r'^Phụ lục\.\s*Bảng (\d+\.[A-Z]):\s*(.*)$', b['text'])
            if ma: b['old_tab'] = ma.group(1); b['text'] = 'Phụ lục. ' + ma.group(2)
        if skip_lvl is not None: continue
        if b['t'] == 'p' and re.match(r'^\*\*Câu hỏi có thể gặp', b['text']):
            skip_q = True; continue
        if skip_q: continue
        if b['t'] == 'li' and b['text'].startswith('**Cần hỏi giảng viên'): continue
        out.append(b)
    return out

def plain(t):
    t = re.sub(r'<[^>]+>', '', t)
    return re.sub(r'[*`]', '', t)

def assign_captions(bl, chap, state):
    """Gắn chú thích cho bảng/hình; bỏ các dòng chú thích tường minh. Trả (blocks mới, ánh xạ nhãn cũ -> mới)."""
    expl_t, expl_f, out, last_h, refmap = None, None, [], '', {}
    pend = []  # (index trong out, kind, nhãn cũ, tiêu đề)
    # lượt 1: tìm chú thích tường minh và bỏ khỏi danh sách
    tmp = []
    for k, b in enumerate(bl):
        if b['t'] == 'p':
            m = re.match(r'^\*\*Bảng (\d+\.[0-9A-Z]+)\.\s+(.*?)\*\*$', b['text'])
            if m: tmp.append(dict(t='cap_t', old=m.group(1), title=m.group(2))); continue
            m = re.match(r'^\*\*Hình (\d+\.\d+)\.\*\*\s*(.*)$', b['text'])
            if m: tmp.append(dict(t='cap_f', old=m.group(1), title=m.group(2))); continue
            m = re.match(r'^\*\*Sơ đồ (\d+)\.\s*(.*?)\*\*$', b['text'])
            if m: tmp.append(dict(t='cap_f', old='S' + m.group(1), title=m.group(2))); continue
        tmp.append(b)
    pending_t = pending_f = None; hold = None
    for k, b in enumerate(tmp):
        if b['t'] == 'h':
            last_h = re.sub(r'^[\d.]+\s*', '', b['text']); pending_t = pending_f = None; hold = b.get('old_tab')
            out.append(b); continue
        if b['t'] == 'cap_t': pending_t = b; continue
        if b['t'] == 'cap_f': pending_f = b; continue
        if b['t'] == 'table' or (b['t'] == 'code' and b['lang'] == 'mermaid'):
            kind = 'Bảng' if b['t'] == 'table' else 'Hình'
            cap = pending_t if kind == 'Bảng' else pending_f
            title = None; old = None
            if cap:
                title, old = cap['title'], cap['old']
                if kind == 'Bảng': pending_t = None
                else: pending_f = None
            else:
                # dòng in đậm đứng ngay trước bảng
                if kind == 'Bảng' and out and out[-1]['t'] == 'p':
                    mi = re.match(r'^\*\*([A-Z][A-Z_0-9]+)\*\*', out[-1]['text']) if chap in (2, 7) else None
                    if mi:
                        title = f'Thuộc tính của {mi.group(1)}'; out.pop()
                    m = None if mi else re.match(r'^\*\*([^*]+?)\*\*[:.]?$', out[-1]['text'])
                    if m:
                        title = m.group(1).strip().rstrip(':.')
                        out.pop()
                        if title in ('Bảng khởi tạo', 'Bảng sau biến đổi'):
                            title = f'{title} (tableau), {last_h}'
                if title is None:
                    title = last_h if kind == 'Bảng' else ('Sơ đồ ' + last_h[0].lower() + last_h[1:])
                    if kind == 'Bảng' and hold: old, hold = hold, None
            state[kind] += 1
            n = state[kind] if state['chap'] == chap else None
            b['cap'] = dict(kind=kind, chap=chap, n=state[kind], title=title.rstrip('.'))
            if old is not None: refmap[f'{kind} {old}' if not old.startswith('S') else f'Sơ đồ {old[1:]}'] = f'{kind} {chap}.{state[kind]}'
            out.append(b); continue
        out.append(b)
    return out, refmap

# ======================= 2. DOCX =======================
doc = Document()
sec0 = doc.sections[0]
def page_setup(sec, landscape=False):
    if landscape:
        sec.orientation = WD_ORIENT.LANDSCAPE; sec.page_width, sec.page_height = Cm(29.7), Cm(21.0)
        sec.left_margin = sec.right_margin = Cm(2.0); sec.top_margin = sec.bottom_margin = Cm(2.0)
    else:
        sec.orientation = WD_ORIENT.PORTRAIT; sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
        sec.left_margin, sec.right_margin, sec.top_margin, sec.bottom_margin = Cm(2.5), Cm(2.0), Cm(2.0), Cm(2.0)
page_setup(sec0)

def set_font(style, size, bold=None, italic=None, color=True):
    style.font.name = FONT; style.font.size = Pt(size)
    if bold is not None: style.font.bold = bold
    if italic is not None: style.font.italic = italic
    if color: style.font.color.rgb = RGBColor(0, 0, 0)
    rpr = style.element.get_or_add_rPr(); rf = rpr.find(qn('w:rFonts'))
    if rf is None: rf = OxmlElement('w:rFonts'); rpr.append(rf)
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
from docx.enum.style import WD_STYLE_TYPE
code_style = ST.add_style('MaNguon', WD_STYLE_TYPE.PARAGRAPH)
code_style.base_style = ST['Normal']; code_style.font.name = 'Courier New'; code_style.font.size = Pt(9.5)
code_style.paragraph_format.space_after = Pt(0); code_style.paragraph_format.line_spacing = 1.0
cr = code_style.element.get_or_add_rPr(); rf = cr.find(qn('w:rFonts'))
if rf is None: rf = OxmlElement('w:rFonts'); cr.append(rf)
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
        return r
    pos = 0
    parts = TOKEN.split(text)
    k = 0
    while k < len(parts):
        tok = parts[k]; k += 1
        if k % 2 == 1 and False: pass
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
    def link(m):
        txt, tgt = m.group(1), m.group(2)
        mm = re.match(r'^(\d\d)_.*\.md$', tgt)
        if mm: return f'mục {int(mm.group(1))}'
        if tgt.endswith(('.py', '.sql')) or tgt.startswith(('tools/', 'sql/')): return f'`{txt}`'
        return txt
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link, t)
    if refmap:
        t = re.sub('|'.join(re.escape(k) + r'(?![0-9A-Za-z])' for k in sorted(refmap, key=len, reverse=True)), lambda m: refmap[m.group(0)], t)
    return t

# ---- trang bìa ----
def center(text, size, bold=False, before=0, after=6, italic=False):
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(before); p.paragraph_format.space_after = Pt(after)
    r = p.add_run(text); r.bold = bold; r.italic = italic; r.font.size = Pt(size)
    return p
sec0.different_first_page_header_footer = True
if THU: pass
if not THU:
    center('BÁO CÁO HỌC PHẦN', 16, True, 60)
    center('CƠ SỞ DỮ LIỆU NÂNG CAO', 20, True, 6, 24)
    center('PHÂN TÍCH, THIẾT KẾ VÀ CHUẨN HÓA', 18, True, 30, 6)
    center('CƠ SỞ DỮ LIỆU CỬA HÀNG POWERTECH', 18, True, 0, 40)
    center('Nhóm 6 – Lớp 23DTHD6', 14, True, 20)
    center('Thành viên:', 13, False, 10, 2)
    for n in ('Nguyễn Ngọc Tình (trưởng nhóm)', 'Đỗ Thanh Hoàng Đức Nhả', 'Võ Thành Đông'):
        center(n, 13, False, 0, 2)
    center('Giảng viên hướng dẫn: ……………………………………', 13, False, 40)
    center('Tháng 10 năm 2026', 13, False, 60)

# ---- chuẩn bị nội dung ----
state = dict(Bảng=0, Hình=0, chap=None)
CH = {}
allrefs = {}
for f in FILES:
    bl = filter_blocks(parse(os.path.join(BC, f)))
    chap = CHAP[f]
    state['Bảng'] = state['Hình'] = 0
    bl, refmap = assign_captions(bl, chap, state)
    CH[f] = (bl, refmap)
heads = [(b['lvl'], b['text']) for f in FILES for b in CH[f][0] if b['t'] == 'h' and b['lvl'] <= 3]
caps = {'Bảng': [], 'Hình': []}
for f in FILES:
    for b in CH[f][0]:
        if 'cap' in b: caps[b['cap']['kind']].append(f"{b['cap']['kind']} {b['cap']['chap']}.{b['cap']['n']}. {b['cap']['title']}")

def toc_block(title, instr, entries, indent=None):
    p = doc.add_paragraph(style='TieuDeMucLuc'); p.add_run(title)
    # trường nhiều đoạn với kết quả lưu sẵn
    first = True
    for k, (lvl, text) in enumerate(entries):
        p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.left_indent = Cm(0.7 * (lvl - 1)); r0 = p
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

allmap = {}
for f in FILES: allmap.update(CH[f][1])
cl = lambda t: re.sub(r'[*`]', '', conv_text(t, allmap))
if not THU: toc_block('MỤC LỤC', ' TOC \\o "1-3" \\h \\z \\u ', [(l, cl(t)) for l, t in heads])
if not THU: toc_block('DANH MỤC HÌNH', ' TOC \\h \\z \\c "Hinh" ', [(1, re.sub(r'[*`]', '', c)) for c in caps['Hình']])
if not THU: toc_block('DANH MỤC BẢNG', ' TOC \\h \\z \\c "Bang" ', [(1, re.sub(r'[*`]', '', c)) for c in caps['Bảng']])

# ---- hàm dựng nội dung ----
def add_landscape():
    s = doc.add_section(WD_SECTION.NEW_PAGE); page_setup(s, True); s.different_first_page_header_footer = False
def add_portrait():
    s = doc.add_section(WD_SECTION.NEW_PAGE); page_setup(s, False); s.different_first_page_header_footer = False

seq_first = {}
def caption(kind, chap, n, title, above=True):
    p = doc.add_paragraph(style='Caption')
    p.paragraph_format.keep_with_next = above
    if not above: p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    ident = 'Bang' if kind == 'Bảng' else 'Hinh'
    r = p.add_run(f'{kind} {chap}.')
    key = (ident, chap)
    instr = f' SEQ {ident} \\* ARABIC' + ('' if key in seq_first else ' \\r 1') + ' '
    seq_first[key] = True
    fld(p, instr, str(n), bold=True)
    p.add_run('. ')
    add_inline(p, title, size=11, bold=True)
    return p

def set_cell_margins(table, top=40, bottom=40, left=70, right=70):
    tblPr = table._tbl.tblPr; m = OxmlElement('w:tblCellMar')
    for k, v in (('top', top), ('left', left), ('bottom', bottom), ('right', right)):
        e = OxmlElement(f'w:{k}'); e.set(qn('w:w'), str(v)); e.set(qn('w:type'), 'dxa'); m.append(e)
    insert_before(tblPr, m, ['tblLook', 'tblCaption', 'tblDescription'])

def build_table(rows, width_cm, refmap):
    ncol = max(len(r) for r in rows)
    rows = [r + [''] * (ncol - len(r)) for r in rows]
    size = 10 if ncol <= 4 else (9.5 if ncol <= 6 else 9 if ncol <= 8 else 8.5)
    t = doc.add_table(rows=len(rows), cols=ncol); t.style = 'Table Grid'; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    bd = OxmlElement('w:tblBorders')
    for k in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        e = OxmlElement(f'w:{k}'); e.set(qn('w:val'), 'single'); e.set(qn('w:sz'), '4'); e.set(qn('w:space'), '0'); e.set(qn('w:color'), '7F7F7F'); bd.append(e)
    insert_before(t._tbl.tblPr, bd, ['shd', 'tblLayout', 'tblCellMar', 'tblLook', 'tblCaption', 'tblDescription'])
    set_cell_margins(t)
    wts = []
    for c in range(ncol):
        L = [len(plain(re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', r[c]))) for r in rows]
        words = max((len(w) for r in rows for w in plain(r[c]).split()), default=3)
        wts.append(max(3.0, min(max(max(L) ** 0.75 * 1.6, words * 1.0), 38)))
    tot = sum(wts); widths = [max(1.1, width_cm * w / tot) for w in wts]
    s = sum(widths); widths = [w * width_cm / s for w in widths]
    for ri, r in enumerate(rows):
        row = t.rows[ri]
        trPr = row._tr.get_or_add_trPr(); cs = OxmlElement('w:cantSplit'); trPr.append(cs)
        if ri == 0:
            th = OxmlElement('w:tblHeader'); trPr.append(th)
        for ci in range(ncol):
            cell = row.cells[ci]; cell.width = Cm(widths[ci])
            p = cell.paragraphs[0]; p.paragraph_format.space_after = Pt(0); p.paragraph_format.line_spacing = 1.0
            add_inline(p, conv_text(r[ci], refmap), size=size, bold=(ri == 0))
            if ri == 0: shade(cell._tc.get_or_add_tcPr(), 'D9E2F3')
    tw = t._tbl.tblPr.find(qn('w:tblW'))
    if tw is None:
        tw = OxmlElement('w:tblW'); insert_before(t._tbl.tblPr, tw, ['jc', 'tblCellSpacing', 'tblInd', 'tblBorders', 'shd', 'tblLayout', 'tblCellMar', 'tblLook'])
    tw.set(qn('w:type'), 'dxa'); tw.set(qn('w:w'), str(int(width_cm * 567)))
    # lưới cột
    grid = t._tbl.tblGrid
    for gc, w in zip(grid.findall(qn('w:gridCol')), widths): gc.set(qn('w:w'), str(int(w * 567)))
    return t

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
    pPr = p._p.get_or_add_pPr(); shade(pPr, 'F2F2F2')
    for k, ln in enumerate(lines):
        r = p.add_run(ln.replace('\t', '    '))
        if k < len(lines) - 1: r.add_break(WD_BREAK.LINE)

NIMG = {}
def add_image(chap, idx_in_file, fn, landscape=False):
    path = os.path.join(IMG_DIR, fn)
    from PIL import Image
    w, h = Image.open(path).size
    maxw, maxh = (24.5, 15.0) if landscape else (16.3, 20.0)
    wc = maxw; hc = wc * h / w
    if hc > maxh: hc = maxh; wc = hc * w / h
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.keep_with_next = True
    p.add_run().add_picture(path, width=Cm(wc))

fig_counter = {}
for f in FILES:
    bl, refmap = CH[f]; chap = CHAP[f]; fig_counter[f] = 0
    for b in bl:
        t = b['t']
        if t == 'h':
            text = conv_text(b['text'], refmap)
            p = doc.add_paragraph(style=f"Heading {b['lvl']}")
            if b['lvl'] == 1: p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            add_inline(p, text)
        elif t == 'p':
            p = doc.add_paragraph(); add_inline(p, conv_text(b['text'], refmap))
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY; p.paragraph_format.space_after = Pt(6); p.paragraph_format.line_spacing = 1.15
        elif t == 'li':
            add_list_item(b, refmap)
        elif t == 'table':
            cap = b['cap']; rows = b['rows']
            ncol = max(len(r) for r in rows)
            wide = ncol >= 8 and max(len(plain(c)) for r in rows for c in r) > 40
            if wide: add_landscape()
            caption('Bảng', cap['chap'], cap['n'], conv_text(cap['title'], refmap), above=True)
            build_table(rows, 24.7 if wide else 16.5, refmap)
            doc.add_paragraph().paragraph_format.space_after = Pt(4)
            if wide: add_portrait()
        elif t == 'code':
            if b['lang'] == 'mermaid':
                fig_counter[f] += 1
                cap = b['cap']; fn = f"{f[:2]}_{fig_counter[f]}.png"
                land = (f[:2] == '06' and fig_counter[f] == 1)
                if land: add_landscape()
                add_image(chap, fig_counter[f], fn, land)
                caption('Hình', cap['chap'], cap['n'], conv_text(cap['title'], refmap), above=False)
                if land: add_portrait()
            else:
                add_code(b['lines'])

# số trang ở chân trang
fp = sec0.footer.paragraphs[0]; fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
fld(fp, ' PAGE ', '1')

# cập nhật trường khi mở
settings = doc.settings.element
uf = OxmlElement('w:updateFields'); uf.set(qn('w:val'), 'true')
insert_before(settings, uf, ['hdrShapeDefaults', 'footnotePr', 'endnotePr', 'compat', 'docVars', 'rsids', 'mathPr', 'attachedSchema', 'themeFontLang', 'clrSchemeMapping', 'doNotIncludeSubdocsInStats', 'doNotAutoCompressPictures', 'forceUpgrade', 'captions', 'readModeInkLockDown', 'smartTagType', 'schemaLibrary', 'shapeDefaults', 'doNotEmbedSmartTags', 'decimalSymbol', 'listSeparator'])
z = settings.find(qn('w:zoom'))
if z is not None and z.get(qn('w:percent')) is None: z.set(qn('w:percent'), '100')
doc.core_properties.title = 'Báo cáo CSDL nâng cao - PowerTech'
doc.core_properties.author = 'Nhóm 6 - 23DTHD6'
doc.save(OUT)
print('đã lưu', OUT, '| bảng', len(caps['Bảng']), '| hình', len(caps['Hình']))
