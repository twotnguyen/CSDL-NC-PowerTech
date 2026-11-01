"""Nội dung viết tay dùng chung cho các bộ sinh chương: giả thiết, căn cứ nghiệp vụ của các PTH không phải khóa."""

# Giả thiết nghiệp vụ nhóm tự đặt (ghi rõ chữ "giả thiết" khi dùng trong báo cáo)
GIA_THIET = [
    ('G1', 'Số seri chỉ duy nhất trong cùng một mặt hàng; hai mặt hàng khác nhau (hai hãng) có thể in cùng một số seri. '
           'Lý do: số seri do từng hãng tự đánh, cửa hàng không kiểm soát được việc trùng giữa các hãng.'),
    ('G2', 'Mỗi dòng của đơn hàng và mỗi dòng của phiếu nhập chỉ chứa đúng một mặt hàng; cùng một mặt hàng có thể ở nhiều dòng '
           'nếu khác giá hoặc khác lô.'),
    ('G3', 'Cửa hàng tìm khách hàng và nhân viên theo tên gọi (một phần của họ tên), nên họ tên là thuộc tính kép theo tiêu '
           'chí của bài giảng (phép thử: phải dùng `LIKE` trên một phần của giá trị).'),
    ('G4', 'Với các PTH có vế trái chứa cột cho phép rỗng (MaSeri, MaDH, SoDongDH ở HANGCOSERI và PHIEUBAOHANH; MaKH, MaNV ở '
           'TAIKHOAN), PTH chỉ xét trên những bộ mà các cột đó khác rỗng; khóa chứa các cột này chỉ là khóa trên những bộ đó.'),
    ('G5', 'Mã hàng thương mại (SKU), số đơn hàng (SoDH), số phiếu nhập (SoPhieu), mã khách nhập của mã giảm giá '
           '(CodeMG) và tên đăng nhập (TenDangNhap) không trùng nhau giữa các bản ghi cùng loại; mỗi đơn '
           'hàng có tối đa một phiếu giao.'),
    ('G6', 'Mỗi tài khoản thuộc đúng một khách hàng hoặc đúng một nhân viên; mỗi khách và mỗi nhân viên có tối đa một tài '
           'khoản. Mỗi nhân viên có một chức vụ chính (ChucVu); quyền hạn của tài khoản nhân viên theo chức vụ đó.'),
]

# (quan hệ, vế trái của PTH) -> căn cứ nghiệp vụ. PTH có vế trái là khóa chính hoặc UNIQUE đã khai báo được ghi tự động.
CAN_CU = {
    ('ANHMATHANG', 'MaSP,ViTriAnh'): 'Vị trí ảnh trong cùng một mặt hàng không được trùng nhau (mục 1.4.1).',
    ('HANGCOSERI', 'MaSP,SoSeri'): 'Số seri là duy nhất trong cùng mặt hàng (giả thiết G1).',
    ('HANGCOSERI', 'MaPN,SoDongPN'): 'Mỗi dòng phiếu nhập chỉ chứa một mặt hàng (giả thiết G2).',
    ('HANGCOSERI', 'MaDH,SoDongDH'): 'Mỗi dòng đơn chỉ chứa một mặt hàng (giả thiết G2); chỉ xét khi chiếc hàng đã bán (G4).',
    ('CHITIETTRA', 'MaHS'): 'Mỗi hồ sơ đổi trả lập cho đúng một đơn gốc.',
    ('PHIEUBAOHANH', 'MaDH,SoDongDH'): 'Mỗi dòng đơn chỉ chứa một mặt hàng (giả thiết G2).',
    ('PHIEUBAOHANH', 'MaSeri'): 'Mỗi chiếc hàng chỉ thuộc một mặt hàng; chỉ xét khi phiếu có số seri (giả thiết G4).',
    ('SERIMATHANG', 'MaSP,SoSeri'): 'Số seri là duy nhất trong cùng mặt hàng (giả thiết G1).',
    ('PHIEUGIAO', 'MaDH'): 'Mỗi đơn hàng có tối đa một phiếu giao (giả thiết G5).',
    ('TAIKHOAN', 'TenDangNhap'): 'Tên đăng nhập không trùng (giả thiết G5).',
    ('TAIKHOAN', 'MaKH'): 'Mỗi khách có tối đa một tài khoản; chỉ xét trên tài khoản của khách (giả thiết G4, G6).',
    ('TAIKHOAN', 'MaNV'): 'Mỗi nhân viên có tối đa một tài khoản; chỉ xét trên tài khoản của nhân viên (giả thiết G4, G6).',
}

# Ghi chú thiết kế khi chuyển ERD sang quan hệ: các cột lưu thêm cho tiện tra cứu (nguồn của dạng chuẩn thấp)
GHI_CHU_THIET_KE = {
    'KHACHHANG': 'HoTenKH ghi nguyên họ tên trong một cột.',
    'NHANVIEN': 'HoTenNV ghi nguyên họ tên trong một cột.',
    'HANGCOSERI': 'MaSP được ghi thêm vào từng chiếc hàng để tra cứu nhanh theo mặt hàng, dù đã suy ra được từ dòng nhập.',
    'CHITIETTRA': 'MaDH được ghi thêm vào từng dòng trả để khai báo khóa ngoại ghép tới dòng đơn, dù đã có ở hồ sơ.',
    'PHIEUBAOHANH': 'MaSP được ghi thêm vào phiếu để in tên hàng nhanh, dù đã suy ra được từ dòng mua gốc và chiếc hàng.',
}

# Quan hệ chỉ có khóa: khóa chính vừa là khóa ngoại tới nhiều quan hệ
SO_DO_NHOM = {
    'Hàng hóa, ảnh và thông số': ['LOAIHANG', 'THUONGHIEU', 'MATHANG', 'ANHMATHANG', 'DINHNGHIATHONGSO', 'GIATRITHONGSO'],
    'Khách hàng, nhân viên và nhà cung cấp': ['KHACHHANG', 'NHANVIEN', 'NHACUNGCAP'],
    'Bán hàng, thanh toán và giao hàng': ['MAGIAMGIA', 'DONHANG', 'CHITIETDONHANG', 'THANHTOAN', 'PHIEUGIAO', 'LANGIAO'],
    'Nhập hàng, số seri và kho': ['PHIEUNHAP', 'CHITIETPHIEUNHAP', 'HANGCOSERI', 'SERIMATHANG', 'GIAODICHKHO'],
    'Đổi trả, hoàn tiền và bảo hành': ['HOSODOITRA', 'CHITIETTRA', 'LANNHANLAI', 'KHOANHOAN', 'PHIEUBAOHANH'],
}
