#!/usr/bin/env python3
"""Lưu đồ nghiệp vụ (tình trạng đơn, đổi trả, bảo hành, ba nhóm kho) và sơ đồ phân rã trước/sau, vẽ bằng Graphviz.  Chạy: python3 tools/ve_luudo.py"""
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
HINH = os.path.join(HERE, '..', 'hinh')
YEL, YEL_B = '#FFF2CC', '#D6B656'
ORG, ORG_B = '#FFE6CC', '#D79B00'
BLU, BLU_B = '#DAE8FC', '#6C8EBF'
GRN, GRN_B = '#D5E8D4', '#82B366'
RED, RED_B = '#F8CECC', '#B85450'
HEAD = ('digraph G {', '  rankdir=@RD@; splines=polyline; nodesep=0.5; ranksep=0.75; pad=0.25;',
        '  node [fontname="Helvetica", fontsize=12, margin="0.18,0.1"]; edge [fontname="Helvetica", fontsize=10.5, color="#444444"];')


def run(name, body, rd='TB', dpi=170):
    text = '\n'.join(HEAD).replace('@RD@', rd) + '\n' + '\n'.join(body) + '\n}'
    base = os.path.join(HINH, name)
    open(base + '.dot', 'w', encoding='utf-8').write(text)
    subprocess.run(['dot', '-Tpng', f'-Gdpi={dpi}', base + '.dot', '-o', base + '.png'], check=True)


def box(i, t, kind='p'):
    st = {'p': f'shape=box, style="rounded,filled", fillcolor="{YEL}", color="{YEL_B}"',
          'd': f'shape=diamond, style=filled, fillcolor="{ORG}", color="{ORG_B}", margin="0.05,0.05"',
          's': f'shape=ellipse, style=filled, fillcolor="{BLU}", color="{BLU_B}"',
          'ok': f'shape=box, style="rounded,filled", fillcolor="{GRN}", color="{GRN_B}"',
          'no': f'shape=box, style="rounded,filled", fillcolor="{RED}", color="{RED_B}"'}[kind]
    return f'  {i} [label=<{t}>, {st}];'


def e(a, b, lab='', extra=''):
    return f'  {a} -> {b} [{f"label=<{lab}>," if lab else ""}{extra}];'


def luudo_don():
    B = [box('a', '<B>Chờ xác nhận</B>', 's'), box('b', '<B>Đã xác nhận</B>', 's'), box('c', '<B>Đang chuẩn bị</B>', 's'), box('d', '<B>Đang giao</B>', 's'),
         box('f', '<B>Hoàn tất</B>', 'ok'), box('x', '<B>Đã hủy</B>', 'no')]
    E = [e('a', 'b', 'Bán hàng gọi khách,<BR/>xác nhận đơn'), e('b', 'c', 'Kho lấy hàng,<BR/>ghi số seri, niêm phong'), e('c', 'd', 'Giao hàng nhận giao<BR/>cùng phiếu giao'),
         e('d', 'f', 'Khách nhận hàng,<BR/>tiền thu đủ'),
         e('a', 'x', 'Khách tự hủy<BR/>(chưa xác nhận)'), e('d', 'x', '3 lần giao<BR/>không thành công')]
    note = ['  n [shape=note, style=filled, fillcolor="#FFFFFF", color="#999999", label=<Đơn trả trước phải thanh toán<BR/>trước khi được xác nhận;<BR/>người lập, thu tiền, giao hàng<BR/>ghi trên đơn, thanh toán, phiếu giao>];', '  { rank=same; f; n }']
    run('luudo_don_hang', B + E + [note[0], '  { rank=same; f; n }'][:-1], rd='TB')


def luudo_doitra():
    B = [box('s', '<B>Khách đề nghị<BR/>đổi trả</B>', 's'), box('k', 'Kỹ thuật kiểm tra<BR/>sản phẩm'), box('q', 'Đủ điều kiện<BR/>đổi trả?', 'd'), box('t', 'Từ chối,<BR/>giải thích cho khách', 'no'),
         box('h', 'Bán hàng tiếp nhận,<BR/>lập <B>hồ sơ đổi trả</B><BR/>(đơn gốc, dòng, số lượng)'), box('n', 'Nhận hàng về:<BR/>nhóm <B>chờ kiểm tra</B>'), box('k2', 'Kỹ thuật kiểm tra,<BR/>ghi kết luận'),
         box('m', 'Quản lý duyệt<BR/>chuyển nhóm'), box('r', 'Kết quả?', 'd'), box('ok', 'Nhóm <B>đủ điều kiện bán</B>', 'ok'), box('cx', 'Nhóm <B>chờ xử lý</B><BR/>(đã mở hộp hoặc lỗi thật)', 'no'),
         box('y', 'Khách muốn?', 'd'), box('dn', 'Lập đơn mới,<BR/>tính chênh lệch'), box('hd', 'Quản lý duyệt hoàn;<BR/>Thu ngân chi tiền hoàn')]
    E = [e('s', 'k'), e('k', 'q'), e('q', 't', 'Không'), e('q', 'h', 'Có'), e('h', 'n'), e('n', 'k2'), e('k2', 'm'), e('m', 'r'), e('r', 'ok', 'Còn nguyên,<BR/>không lỗi'), e('r', 'cx', 'Khác'),
         e('h', 'y', '', 'style=dashed'), e('y', 'dn', 'Đổi sản phẩm'), e('y', 'hd', 'Hoàn tiền')]
    run('luudo_doi_tra', B + E)


def luudo_baohanh():
    B = [box('s', '<B>Khách mang sản phẩm lỗi</B><BR/>đến cửa hàng', 's'), box('k', 'Kỹ thuật kiểm tra:<BR/>còn hạn, có thông tin mua,<BR/>số seri khớp, tem còn nguyên,<BR/>không rơi vỡ, vào nước, tháo sửa'),
         box('q', 'Đủ điều kiện?', 'd'), box('t', 'Ghi lý do từ chối,<BR/>trả sản phẩm cho khách', 'no'), box('p', 'Lập <B>phiếu tiếp nhận bảo hành</B><BR/>(seri, dòng mua gốc, lỗi, ngày hẹn trả)'),
         box('g', 'Kiểm tra lỗi; sửa tại cửa hàng<BR/>hoặc gửi hãng, ghi từng bước'), box('r', 'Hãng không sửa được?', 'd'),
         box('d', 'Đổi sản phẩm tương đương<BR/>hoặc thu hồi theo giá trị còn lại<BR/>sau khấu hao'), box('v', 'Báo khách đến nhận,<BR/>cùng kiểm tra, ký biên bản trả', 'ok')]
    E = [e('s', 'k'), e('k', 'q'), e('q', 't', 'Không'), e('q', 'p', 'Có'), e('p', 'g'), e('g', 'r'), e('r', 'd', 'Có'), e('r', 'v', 'Không')]
    run('luudo_bao_hanh', B + E)


def luudo_kho():
    B = [box('n', '<B>Nhập hàng</B><BR/>phiếu nhập được xác nhận', 's'), box('b', '<B>Bán hàng</B><BR/>(xuất bán)', 's'), box('l', '<B>Hàng khách trả về</B><BR/>(nhận lại)', 's'),
         box('a', '<B>Đủ điều kiện bán</B>', 'ok'), box('c', '<B>Chờ kiểm tra</B>', 'p'), box('x', '<B>Chờ xử lý</B><BR/>(không bán được)', 'no'), box('o', 'Khách nhận hàng', 's')]
    E = [e('n', 'a', 'ghi tăng,<BR/>một lần'), e('a', 'b', 'chỉ nhóm này<BR/>được bán', 'dir=forward'), e('b', 'o'), e('l', 'c', 'mọi hàng nhận lại'), e('c', 'a', 'Kỹ thuật kiểm tra,<BR/>Quản lý duyệt'), e('c', 'x', 'đã mở hộp<BR/>hoặc lỗi thật')]
    note = '  n2 [shape=note, style=filled, fillcolor="#FFFFFF", color="#999999", label=<Mỗi lần vào, ra, chuyển nhóm ghi một dòng <B>GIAO DỊCH KHO</B>.<BR/>Chuyển nhóm không làm tăng tổng số hàng thực tế.>];'
    run('luudo_kho', B + E + [note], rd='TB')


def ds(name, title, attrs, keys=(), fks=(), color=BLU):
    rows = []
    for a in attrs:
        t = f'<U>{a}</U>' if a in keys else (f'<FONT COLOR="#2E7D32">{a}</FONT>' if a in fks else a)
        rows.append(f'<TR><TD ALIGN="LEFT">{t}</TD></TR>')
    return (f'<<TABLE BORDER="1" COLOR="{BLU_B}" CELLBORDER="0" CELLSPACING="0" CELLPADDING="3"><TR><TD BGCOLOR="{color}"><B>{title}</B></TD></TR>' + ''.join(rows) + '</TABLE>>')


def tbl(i, label):
    return f'  {i} [shape=plaintext, label={label}];'


def phan_ra():
    # CHITIETTRA
    B = [tbl('q', ds('q', 'Q: CHITIETTRA (ban đầu)', ['MaHS', 'SoDongDH', 'MaDH', 'SoLuongTra', 'MaSeri'], ['MaHS', 'SoDongDH'], (), '#F8CECC')),
         '  pth [shape=note, style=filled, fillcolor="#FFFFFF", color="#999999", label=<PTH gây vi phạm:<BR/><B>MaHS → MaDH</B><BR/>(phụ thuộc một phần vào khóa)>];',
         tbl('q1', ds('q1', 'Q₁ = HOSODOITRA (đã có)', ['MaHS', 'MaDH', '…'], ['MaHS'])), tbl('q2', ds('q2', 'Q₂: CHITIETTRA (sau cải tiến)', ['MaHS', 'SoDongDH', 'SoLuongTra', 'MaSeri'], ['MaHS', 'SoDongDH'], (), '#D5E8D4')),
         '  q -> q1 [label="tách theo MaHS → MaDH"]; q -> q2 [label="Q ∖ {MaDH}"]; pth -> q [style=dashed, arrowhead=none];',
         '  { rank=same; q; pth }']
    run('phan_ra_chitiettra', B, rd='TB')
    B = [tbl('q', ds('q', 'Q: PHIEUBAOHANH (ban đầu)', ['MaPhieuBH', 'MaSeri', 'MaSP', 'MaDH', 'SoDongDH', '…'], ['MaPhieuBH'], ['MaSeri', 'MaDH', 'SoDongDH'], '#F8CECC')),
         '  pth [shape=note, style=filled, fillcolor="#FFFFFF", color="#999999", label=<PTH bắc cầu:<BR/><B>MaDH,SoDongDH → MaSP</B><BR/><B>MaSeri → MaSP</B>>];',
         tbl('q1', ds('q1', 'Q₁ = CHITIETDONHANG (đã có)', ['MaDH', 'SoDongDH', 'MaSP', '…'], ['MaDH', 'SoDongDH'])),
         tbl('q2', ds('q2', 'Q₂: PHIEUBAOHANH (sau cải tiến)', ['MaPhieuBH', 'MaSeri', 'MaDH', 'SoDongDH', '…'], ['MaPhieuBH'], ['MaSeri', 'MaDH', 'SoDongDH'], '#D5E8D4')),
         '  q -> q1 [label="tách theo\\nMaDH,SoDongDH → MaSP"]; q -> q2 [label="bỏ MaSP"]; pth -> q [style=dashed, arrowhead=none];', '  { rank=same; q; pth }']
    run('phan_ra_phieubaohanh', B, rd='TB')
    B = [tbl('q', ds('q', 'Q: HANGCOSERI (ban đầu, 3NF)', ['MaSeri', 'SoSeri', 'MaSP', 'MaPN', 'SoDongPN', 'MaDH', 'SoDongDH', '…'], ['MaSeri'], ['MaSP', 'MaPN', 'SoDongPN', 'MaDH', 'SoDongDH'], '#F8CECC')),
         '  pth [shape=note, style=filled, fillcolor="#FFFFFF", color="#999999", label=<PTH vi phạm BCNF:<BR/><B>MaPN,SoDongPN → MaSP</B><BR/><B>MaDH,SoDongDH → MaSP</B><BR/>Giữ: SoSeri, MaSP → MaSeri>];',
         tbl('q1', ds('q1', 'Q₁ = CHITIETPHIEUNHAP (đã có)', ['MaPN', 'SoDongPN', 'MaSP', '…'], ['MaPN', 'SoDongPN'])),
         tbl('q2', ds('q2', 'Q₂ = CHITIETDONHANG (đã có)', ['MaDH', 'SoDongDH', 'MaSP', '…'], ['MaDH', 'SoDongDH'])),
         tbl('q3', ds('q3', 'Q₃: HANGCOSERI (rút gọn)', ['MaSeri', 'MaPN', 'SoDongPN', 'MaDH', 'SoDongDH', '…'], ['MaSeri'], ['MaPN', 'SoDongPN', 'MaDH', 'SoDongDH'], '#D5E8D4')),
         tbl('q4', ds('q4', 'Q₄: SERIMATHANG (mới)', ['MaSeri', 'SoSeri', 'MaSP'], ['MaSeri'], ['MaSP'], '#D5E8D4')),
         '  q -> q1; q -> q2; q -> q3; q -> q4; pth -> q [style=dashed, arrowhead=none];', '  { rank=same; q; pth }', '  { rank=same; q1; q2; q3; q4 }']
    run('phan_ra_hangcoseri', B, rd='TB')
    B = [tbl('m', ds('m', 'M: lưu chung ảnh và thông số', ['MaSP', 'DuongDanAnh', 'MaTS', 'GiaTriTS'], ['MaSP', 'DuongDanAnh', 'MaTS'], (), '#F8CECC')),
         tbl('r1', ds('r1', 'R₁ = GIATRITHONGSO', ['MaSP', 'MaTS', 'GiaTriTS'], ['MaSP', 'MaTS'])),
         tbl('r2', ds('r2', 'R₂ (BCNF, chưa 4NF)', ['MaSP', 'DuongDanAnh', 'MaTS'], ['MaSP', 'DuongDanAnh', 'MaTS'], (), '#FFE6CC')),
         tbl('r21', ds('r21', 'R₂₁ = ANHMATHANG', ['MaSP', 'DuongDanAnh', '…'], ['MaSP'], (), '#D5E8D4')),
         tbl('r22', ds('r22', 'R₂₂(MaSP, MaTS) (đã có trong R₁)', ['MaSP', 'MaTS'], ['MaSP', 'MaTS'], (), '#D5E8D4')),
         '  m -> r1 [label="MaSP,MaTS → GiaTriTS"]; m -> r2; r2 -> r21 [label="MaSP ↠ DuongDanAnh"]; r2 -> r22 [label="MaSP ↠ MaTS"];',
         '  { rank=same; r1; r2 }', '  { rank=same; r21; r22 }']
    run('phan_ra_4nf', B, rd='TB')


if __name__ == '__main__':
    luudo_don(); luudo_doitra(); luudo_baohanh(); luudo_kho(); phan_ra()
    print('đã vẽ lưu đồ và sơ đồ phân rã')
