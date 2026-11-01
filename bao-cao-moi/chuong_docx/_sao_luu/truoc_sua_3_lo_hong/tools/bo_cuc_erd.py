"""Bố cục đặt tay của ERD tổng quát (điểm ảnh). ENT_POS: thực thể -> (x, y); MKH_POS: mối kết hợp có thuộc tính -> (x, y);
REL_POS: (con, cha, tên) -> vị trí oval; WAY: ((con, cha, tên), đầu) hoặc (mối kết hợp, thực thể) -> điểm gấp khúc; SIZE: kích thước riêng."""
NV_BAR = 2420
X1, XN = 1220, 1660
ENT_POS = {
    'NHANVIEN': (XN, 1250),
    'TAIKHOAN': (X1, 340), 'MAGIAMGIA': (X1, 560), 'PHIEUGIAO': (X1, 1070),
    'THANHTOAN': (X1, 1300), 'KHOANHOAN': (X1, 1470), 'HOSODOITRA': (X1, 1640), 'LANNHANLAI': (X1, 1810),
    'PHIEUBAOHANH': (X1, 1980), 'PHIEUNHAP': (X1, 2150), 'GIAODICHKHO': (X1, 2320),
    'DONHANG': (850, 900), 'VAITRO': (850, 170), 'GIOHANG': (850, 340), 'KHACHHANG': (560, 640), 'DIACHIKHACH': (200, 640),
    'HANGCOSERI': (500, 1960), 'NHACUNGCAP': (850, 2320),
    'MATHANG': (480, 1200), 'ANHMATHANG': (480, 1000), 'LOAIHANG': (150, 1380), 'THUONGHIEU': (150, 1720),
    'DINHNGHIATHONGSO': (230, 1000),
}
MKH_POS = {
    'GIUVAITRO': (X1, 170), 'CHITIETGIOHANG': (480, 340), 'CHITIETDONHANG': (665, 1050), 'CHITIETPHIEUNHAP': (760, 1560),
    'GIATRITHONGSO': (330, 1110), 'CHITIETTRA': (942, 1400),
    'NHATKYDONHANG': (X1, 730), 'LANGIAO': (850, 1185),
}
SIZE = {'MATHANG': (380, 52), 'HANGCOSERI': (280, 52)}
REL_POS = {
    ('DINHNGHIATHONGSO', 'LOAIHANG', 'Quy định'): (175, 1262),
    ('THANHTOAN', 'DONHANG', 'Thu tiền cho'): (1075, 1160),
}
WAY = {
    ('CHITIETGIOHANG', 'MATHANG'): [(40, 340), (40, 1200), (80, 1200)],
}
