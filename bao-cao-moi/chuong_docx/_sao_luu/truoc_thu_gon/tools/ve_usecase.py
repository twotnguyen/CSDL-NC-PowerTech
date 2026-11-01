#!/usr/bin/env python3
"""Sơ đồ Use Case theo báo cáo mẫu (tổng quát và theo ba loại thực thể, tìm kiếm, thống kê), vẽ bằng PIL.  Chạy: python3 tools/ve_usecase.py"""
import math
import os
import sys

from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from ve_erd import Hinh, S, YEL, YEL_B, BLU, BLU_B, INK, clip_ell, font

HINH = os.path.join(HERE, '..', 'hinh')
GREEN, PINK = (213, 232, 212), (248, 206, 204)


def ve_actor(g, x, y, label, general):
    d, k = g.d, S
    ink = (70, 70, 70)
    d.ellipse(((x - 14) * k, (y - 52) * k, (x + 14) * k, (y - 24) * k), fill=PINK if general else GREEN, outline=ink, width=2 * k)
    d.line([(x * k, (y - 24) * k), (x * k, (y + 12) * k)], fill=ink, width=2 * k)
    d.line([((x - 26) * k, (y - 10) * k), ((x + 26) * k, (y - 10) * k)], fill=ink, width=2 * k)
    d.line([(x * k, (y + 12) * k), ((x - 20) * k, (y + 44) * k)], fill=ink, width=2 * k)
    d.line([(x * k, (y + 12) * k), ((x + 20) * k, (y + 44) * k)], fill=ink, width=2 * k)
    for i, t in enumerate(label.split('\n')):
        g.text(x, y + 62 + i * 22, t, 17, False)


def uc(name, title, left, right, ucs, edges, gen=(), general=(), ncols=1, mid=None):
    """left/right: [(id, nhãn)]; ucs: [(id, nhãn có \\n)]; edges: [(tác nhân, ca)]; gen: [(con, cha)]; mid: [(id, nhãn)] tác nhân khái quát đặt giữa."""
    rows = math.ceil(len(ucs) / ncols)
    n_act = max(len(left), len(right))
    H_act = n_act * 165 + 330
    rowh, ucw, uch = max(120, (H_act - 260) / rows), 330, 84
    box_w = ncols * (ucw + 50) + 50
    xl = 120 if not mid else 120
    box_x0 = 330 if not mid else 560
    box_x1 = box_x0 + box_w
    W = box_x1 + 330
    H = max(230 + rows * rowh + 60, H_act)
    g = Hinh(int(W), int(H))
    # vị trí ca sử dụng
    pos = {}
    for i, (u, lab) in enumerate(ucs):
        c, r = i % ncols, i // ncols
        pos[u] = (box_x0 + 50 + ucw / 2 + c * (ucw + 50), 190 + r * rowh + rowh / 2)
    # vị trí tác nhân
    apos = {}

    def want(a):
        ys = [pos[u][1] for x, u in edges if x == a and u in pos]
        if not ys:
            ys = [apos[c][1] for c, p in gen if p == a and c in apos]
        return sum(ys) / len(ys) if ys else 0
    for col, lst, x in ((0, left, xl), (1, right, W - 120)):
        for a, lab in lst:
            apos[a] = (x, want(a))
    if mid:
        for a, lab in mid:
            apos[a] = (box_x0 - 130, 0)
    for col, lst in ((0, left), (1, right)):
        order = sorted(lst, key=lambda t: apos[t[0]][1])
        last = 140
        for a, lab in order:
            y = max(apos[a][1], last)
            apos[a] = (apos[a][0], y)
            last = y + 160
    if mid:
        for a, lab in mid:
            ys = [apos[c][1] for c, p in gen if p == a]
            apos[a] = (apos[a][0], sum(ys) / len(ys))
    # hộp hệ thống
    g.d.rectangle((box_x0 * S, 80 * S, box_x1 * S, (H - 30) * S), fill=(244, 248, 253), outline=BLU_B, width=3 * S)
    g.d.rectangle((box_x0 * S, 80 * S, (box_x0 + 36 + 11 * len(title)) * S, 118 * S), fill=(244, 248, 253), outline=BLU_B, width=3 * S)
    g.text(box_x0 + 18 + 11 * len(title) / 2, 99, title, 18, True)
    # đường nối
    for a, u in edges:
        if a in apos and u in pos:
            ax, ay = apos[a]
            ux, uy = pos[u]
            p = clip_ell(ux, uy, ucw, uch, ax, ay)
            g.line([(ax + (30 if ax < ux else -30), ay - 10), p], (60, 60, 60), 1.6)
    for c, p in gen:
        (cx, cy), (px, py) = apos[c], apos[p]
        a = (cx + 30, cy - 10)
        b = (px - 34, py - 10)
        g.line([a, b], (60, 60, 60), 1.6)
        ang = math.atan2(b[1] - a[1], b[0] - a[0])
        tri = [(b[0], b[1]), (b[0] - 20 * math.cos(ang) + 10 * math.sin(ang), b[1] - 20 * math.sin(ang) - 10 * math.cos(ang)),
               (b[0] - 20 * math.cos(ang) - 10 * math.sin(ang), b[1] - 20 * math.sin(ang) + 10 * math.cos(ang))]
        g.d.polygon([(x * S, y * S) for x, y in tri], fill='white', outline=(60, 60, 60))
    for u, lab in ucs:
        x, y = pos[u]
        g.ell(x, y, ucw, uch, lab, YEL, YEL_B, False, 17)
    for a, lab in list(left) + list(right) + list(mid or []):
        ve_actor(g, apos[a][0], apos[a][1], lab, a in general)
    g.save(os.path.join(HINH, f'usecase_{name}.png'))


ROLES = [('qt', 'Quản trị'), ('ql', 'Quản lý'), ('bh', 'Bán hàng'), ('tn', 'Thu ngân'), ('kt', 'Kỹ thuật'), ('kho', 'Kho'), ('gh', 'Giao hàng'), ('cs', 'Chăm sóc\nkhách hàng')]


def ve_all():
    uc('tong_quat', 'Tổng quát', ROLES, [('kh', 'Khách hàng')],
       [('u1', 'Quản lý\nđối tượng ngoài'), ('u2', 'Quản lý\ndanh mục cơ bản'), ('u3', 'Quản lý nghiệp vụ'), ('u4', 'Tìm kiếm'), ('u5', 'Thống kê')],
       [('nv', 'u1'), ('nv', 'u2'), ('nv', 'u3'), ('nv', 'u4'), ('nv', 'u5'), ('kh', 'u1'), ('kh', 'u3'), ('kh', 'u4')],
       gen=[(r, 'nv') for r, _ in ROLES], general={'nv', 'kh'}, mid=[('nv', 'Nhân viên')])
    uc('doi_tuong_ngoai', 'Quản lý đối tượng ngoài', [('qt', 'Quản trị'), ('bh', 'Bán hàng'), ('cs', 'Chăm sóc\nkhách hàng'), ('kho', 'Kho')], [('kh', 'Khách hàng')],
       [('a1', 'Quản lý khách hàng'), ('a2', 'Quản lý nhân viên'), ('a3', 'Quản lý nhà cung cấp'), ('a4', 'Quản lý tài khoản\n(khóa, mở khóa)'), ('a5', 'Quản lý địa chỉ\ngiao hàng'), ('a6', 'Đăng ký tài khoản')],
       [('bh', 'a1'), ('cs', 'a1'), ('qt', 'a2'), ('kho', 'a3'), ('qt', 'a4'), ('kh', 'a5'), ('kh', 'a6')], general={'kh'})
    uc('danh_muc', 'Quản lý danh mục cơ bản', [('ql', 'Quản lý'), ('bh', 'Bán hàng'), ('qt', 'Quản trị')], [],
       [('b1', 'Quản lý loại hàng'), ('b2', 'Quản lý thương hiệu'), ('b3', 'Quản lý mặt hàng'), ('b4', 'Quản lý ảnh mặt hàng'), ('b5', 'Quản lý thông số\nvà giá trị thông số'), ('b6', 'Quản lý vai trò')],
       [('ql', 'b1'), ('ql', 'b2'), ('bh', 'b3'), ('bh', 'b4'), ('bh', 'b5'), ('qt', 'b6')])
    uc('nghiep_vu', 'Quản lý nghiệp vụ', [('bh', 'Bán hàng'), ('tn', 'Thu ngân'), ('kho', 'Kho'), ('gh', 'Giao hàng'), ('kt', 'Kỹ thuật'), ('cs', 'Chăm sóc\nkhách hàng'), ('ql', 'Quản lý')], [('kh', 'Khách hàng')],
       [('c1', 'Chọn hàng vào giỏ và đặt hàng'), ('c2', 'Lập, xác nhận và hủy đơn'), ('c11', 'Tạo mã giảm giá'), ('c3', 'Thanh toán, đặt cọc'), ('c9', 'Duyệt và chi hoàn tiền'),
        ('c5', 'Nhập hàng, ghi số seri'), ('c6', 'Ghi giao dịch kho'), ('c4', 'Giao hàng'), ('c8', 'Kiểm tra hàng nhận lại'), ('c10', 'Tiếp nhận bảo hành'), ('c7', 'Tiếp nhận đổi trả')],
       [('kh', 'c1'), ('bh', 'c2'), ('bh', 'c11'), ('ql', 'c11'), ('tn', 'c3'), ('ql', 'c9'), ('tn', 'c9'), ('kho', 'c5'), ('kho', 'c6'), ('gh', 'c4'), ('kt', 'c8'), ('kt', 'c10'), ('cs', 'c7')],
       general={'kh'})
    uc('tim_kiem', 'Tìm kiếm', [('bh', 'Bán hàng'), ('cs', 'Chăm sóc\nkhách hàng'), ('ql', 'Quản lý')], [('kh', 'Khách hàng')],
       [('d1', 'Tìm mặt hàng theo loại,\nthương hiệu, thông số'), ('d2', 'Tra cứu lịch sử\nmua hàng của khách'), ('d3', 'Truy vết chiếc hàng\ntheo số seri'), ('d4', 'Tra cứu bảo hành,\nđổi trả của đơn'),
        ('d5', 'Xem tình trạng đơn\ncủa tôi'), ('d6', 'Truy trách nhiệm:\nai xử lý từng bước đơn')],
       [('kh', 'd1'), ('kh', 'd5'), ('bh', 'd1'), ('bh', 'd2'), ('cs', 'd2'), ('cs', 'd3'), ('cs', 'd4'), ('ql', 'd3'), ('ql', 'd6')], general={'kh'})
    uc('thong_ke', 'Thống kê', [('ql', 'Quản lý'), ('kho', 'Kho'), ('qt', 'Quản trị')], [],
       [('e1', 'Doanh thu tiền hàng\ntheo loại hàng'), ('e2', 'Tồn kho theo\nmặt hàng và nhóm kho'), ('e3', 'Hoàn tiền: ai duyệt,\nai chi'), ('e4', 'Vai trò đang giữ\ncủa nhân viên'), ('e5', 'Giỏ hàng đang dùng\nvà tiền tạm tính')],
       [('ql', 'e1'), ('ql', 'e3'), ('kho', 'e2'), ('qt', 'e4'), ('ql', 'e4'), ('ql', 'e5')])


if __name__ == '__main__':
    ve_all()
    print('đã vẽ use case')
