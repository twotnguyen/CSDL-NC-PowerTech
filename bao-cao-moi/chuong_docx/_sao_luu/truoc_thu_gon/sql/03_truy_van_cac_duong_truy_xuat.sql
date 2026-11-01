-- 66 truy vấn cho các con đường truy xuất từ 12 nút vào (sinh bằng tools/gen_chuong3.py).
-- Mỗi truy vấn nối các quan hệ theo từng cung của đường; đã chạy thử trên dữ liệu minh họa (sql/02) và đều có kết quả, trừ đường rỗng đúng quy tắc (có ghi chú).

-- Đường 1: ANHMATHANG → MATHANG → LOAIHANG
-- Cho biết ảnh mặt hàng minh họa cho mặt hàng nào; mặt hàng đó thuộc loại hàng nào.
-- Số dòng trên dữ liệu minh họa: 5
SELECT *
FROM ANHMATHANG am
JOIN MATHANG mh ON am.MaSP = mh.MaSP
JOIN LOAIHANG lh ON mh.MaLoai = lh.MaLoai;

-- Đường 2: ANHMATHANG → MATHANG → THUONGHIEU
-- Cho biết ảnh mặt hàng minh họa cho mặt hàng nào; mặt hàng đó mang thương hiệu nào.
-- Số dòng trên dữ liệu minh họa: 5
SELECT *
FROM ANHMATHANG am
JOIN MATHANG mh ON am.MaSP = mh.MaSP
JOIN THUONGHIEU th ON mh.MaTH = th.MaTH;

-- Đường 3: GIATRITHONGSO → MATHANG → LOAIHANG
-- Cho biết giá trị thông số thuộc mặt hàng nào; mặt hàng đó thuộc loại hàng nào.
-- Số dòng trên dữ liệu minh họa: 5
SELECT *
FROM GIATRITHONGSO gt
JOIN MATHANG mh ON gt.MaSP = mh.MaSP
JOIN LOAIHANG lh ON mh.MaLoai = lh.MaLoai;

-- Đường 4: GIATRITHONGSO → MATHANG → THUONGHIEU
-- Cho biết giá trị thông số thuộc mặt hàng nào; mặt hàng đó mang thương hiệu nào.
-- Số dòng trên dữ liệu minh họa: 5
SELECT *
FROM GIATRITHONGSO gt
JOIN MATHANG mh ON gt.MaSP = mh.MaSP
JOIN THUONGHIEU th ON mh.MaTH = th.MaTH;

-- Đường 5: GIATRITHONGSO → DINHNGHIATHONGSO → LOAIHANG
-- Cho biết giá trị thông số ứng với thông số nào; thông số đó do loại hàng nào quy định.
-- Số dòng trên dữ liệu minh họa: 5
SELECT *
FROM GIATRITHONGSO gt
JOIN DINHNGHIATHONGSO dn ON gt.MaTS = dn.MaTS
JOIN LOAIHANG lh ON dn.MaLoai = lh.MaLoai;

-- Đường 6: DIACHIKHACH → KHACHHANG
-- Cho biết địa chỉ giao hàng là địa chỉ của khách hàng nào.
-- Số dòng trên dữ liệu minh họa: 3
SELECT *
FROM DIACHIKHACH dc
JOIN KHACHHANG kh ON dc.MaKH = kh.MaKH;

-- Đường 7: GIUVAITRO → NHANVIEN
-- Cho biết lần giữ vai trò của nhân viên nào.
-- Số dòng trên dữ liệu minh họa: 10
SELECT *
FROM GIUVAITRO gv
JOIN NHANVIEN nv ON gv.MaNV = nv.MaNV;

-- Đường 8: GIUVAITRO → VAITRO
-- Cho biết lần giữ vai trò là vai trò nào.
-- Số dòng trên dữ liệu minh họa: 10
SELECT *
FROM GIUVAITRO gv
JOIN VAITRO vt ON gv.MaVT = vt.MaVT;

-- Đường 9: CHITIETGIOHANG → MATHANG → LOAIHANG
-- Cho biết dòng giỏ hàng chứa mặt hàng nào; mặt hàng đó thuộc loại hàng nào.
-- Số dòng trên dữ liệu minh họa: 4
SELECT *
FROM CHITIETGIOHANG cg
JOIN MATHANG mh ON cg.MaSP = mh.MaSP
JOIN LOAIHANG lh ON mh.MaLoai = lh.MaLoai;

-- Đường 10: CHITIETGIOHANG → MATHANG → THUONGHIEU
-- Cho biết dòng giỏ hàng chứa mặt hàng nào; mặt hàng đó mang thương hiệu nào.
-- Số dòng trên dữ liệu minh họa: 4
SELECT *
FROM CHITIETGIOHANG cg
JOIN MATHANG mh ON cg.MaSP = mh.MaSP
JOIN THUONGHIEU th ON mh.MaTH = th.MaTH;

-- Đường 11: CHITIETGIOHANG → GIOHANG → TAIKHOAN → KHACHHANG
-- Cho biết dòng giỏ hàng thuộc giỏ hàng nào; giỏ hàng đó thuộc tài khoản nào; tài khoản đó thuộc khách hàng nào (nếu là tài khoản khách).
-- Số dòng trên dữ liệu minh họa: 4
SELECT *
FROM CHITIETGIOHANG cg
JOIN GIOHANG gh ON cg.MaGio = gh.MaGio
JOIN TAIKHOAN tk ON gh.MaTK = tk.MaTK
JOIN KHACHHANG kh ON tk.MaKH = kh.MaKH;

-- Đường 12: CHITIETGIOHANG → GIOHANG → TAIKHOAN → NHANVIEN
-- Cho biết dòng giỏ hàng thuộc giỏ hàng nào; giỏ hàng đó thuộc tài khoản nào; tài khoản đó thuộc nhân viên nào (nếu là tài khoản nhân viên).
-- Số dòng trên dữ liệu minh họa: 0 (giỏ hàng chỉ thuộc tài khoản khách, nên không có giỏ của tài khoản nhân viên)
SELECT *
FROM CHITIETGIOHANG cg
JOIN GIOHANG gh ON cg.MaGio = gh.MaGio
JOIN TAIKHOAN tk ON gh.MaTK = tk.MaTK
JOIN NHANVIEN nv ON tk.MaNV = nv.MaNV;

-- Đường 13: NHATKYDONHANG → NHANVIEN
-- Cho biết lần đổi tình trạng đơn do nhân viên nào thực hiện (nếu có).
-- Số dòng trên dữ liệu minh họa: 10
SELECT *
FROM NHATKYDONHANG nk
JOIN NHANVIEN nv ON nk.MaNV = nv.MaNV;

-- Đường 14: NHATKYDONHANG → DONHANG → KHACHHANG
-- Cho biết lần đổi tình trạng đơn ghi tình trạng của đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách).
-- Số dòng trên dữ liệu minh họa: 11
SELECT *
FROM NHATKYDONHANG nk
JOIN DONHANG dh ON nk.MaDH = dh.MaDH
JOIN KHACHHANG kh ON dh.MaKH = kh.MaKH;

-- Đường 15: NHATKYDONHANG → DONHANG → NHANVIEN
-- Cho biết lần đổi tình trạng đơn ghi tình trạng của đơn hàng nào; đơn hàng đó do nhân viên nào lập.
-- Số dòng trên dữ liệu minh họa: 7
SELECT *
FROM NHATKYDONHANG nk
JOIN DONHANG dh ON nk.MaDH = dh.MaDH
JOIN NHANVIEN nv ON dh.MaNV = nv.MaNV;

-- Đường 16: NHATKYDONHANG → DONHANG → MAGIAMGIA → NHANVIEN
-- Cho biết lần đổi tình trạng đơn ghi tình trạng của đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo.
-- Số dòng trên dữ liệu minh họa: 4
SELECT *
FROM NHATKYDONHANG nk
JOIN DONHANG dh ON nk.MaDH = dh.MaDH
JOIN MAGIAMGIA mg ON dh.MaMG = mg.MaMG
JOIN NHANVIEN nv ON mg.MaNV = nv.MaNV;

-- Đường 17: LANGIAO → NHANVIEN
-- Cho biết lần giao hàng do nhân viên nào giao.
-- Số dòng trên dữ liệu minh họa: 4
SELECT *
FROM LANGIAO lg
JOIN NHANVIEN nv ON lg.MaNV = nv.MaNV;

-- Đường 18: LANGIAO → PHIEUGIAO → NHANVIEN
-- Cho biết lần giao hàng thuộc phiếu giao nào; phiếu giao đó do nhân viên nào giao.
-- Số dòng trên dữ liệu minh họa: 4
SELECT *
FROM LANGIAO lg
JOIN PHIEUGIAO pg ON lg.MaGiao = pg.MaGiao
JOIN NHANVIEN nv ON pg.MaNV = nv.MaNV;

-- Đường 19: LANGIAO → PHIEUGIAO → DONHANG → KHACHHANG
-- Cho biết lần giao hàng thuộc phiếu giao nào; phiếu giao đó lập cho đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách).
-- Số dòng trên dữ liệu minh họa: 4
SELECT *
FROM LANGIAO lg
JOIN PHIEUGIAO pg ON lg.MaGiao = pg.MaGiao
JOIN DONHANG dh ON pg.MaDH = dh.MaDH
JOIN KHACHHANG kh ON dh.MaKH = kh.MaKH;

-- Đường 20: LANGIAO → PHIEUGIAO → DONHANG → NHANVIEN
-- Cho biết lần giao hàng thuộc phiếu giao nào; phiếu giao đó lập cho đơn hàng nào; đơn hàng đó do nhân viên nào lập.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM LANGIAO lg
JOIN PHIEUGIAO pg ON lg.MaGiao = pg.MaGiao
JOIN DONHANG dh ON pg.MaDH = dh.MaDH
JOIN NHANVIEN nv ON dh.MaNV = nv.MaNV;

-- Đường 21: LANGIAO → PHIEUGIAO → DONHANG → MAGIAMGIA → NHANVIEN
-- Cho biết lần giao hàng thuộc phiếu giao nào; phiếu giao đó lập cho đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM LANGIAO lg
JOIN PHIEUGIAO pg ON lg.MaGiao = pg.MaGiao
JOIN DONHANG dh ON pg.MaDH = dh.MaDH
JOIN MAGIAMGIA mg ON dh.MaMG = mg.MaMG
JOIN NHANVIEN nv ON mg.MaNV = nv.MaNV;

-- Đường 22: GIAODICHKHO → MATHANG → LOAIHANG
-- Cho biết giao dịch kho liên quan đến mặt hàng nào; mặt hàng đó thuộc loại hàng nào.
-- Số dòng trên dữ liệu minh họa: 4
SELECT *
FROM GIAODICHKHO gd
JOIN MATHANG mh ON gd.MaSP = mh.MaSP
JOIN LOAIHANG lh ON mh.MaLoai = lh.MaLoai;

-- Đường 23: GIAODICHKHO → MATHANG → THUONGHIEU
-- Cho biết giao dịch kho liên quan đến mặt hàng nào; mặt hàng đó mang thương hiệu nào.
-- Số dòng trên dữ liệu minh họa: 4
SELECT *
FROM GIAODICHKHO gd
JOIN MATHANG mh ON gd.MaSP = mh.MaSP
JOIN THUONGHIEU th ON mh.MaTH = th.MaTH;

-- Đường 24: GIAODICHKHO → NHANVIEN
-- Cho biết giao dịch kho do nhân viên nào thực hiện.
-- Số dòng trên dữ liệu minh họa: 4
SELECT *
FROM GIAODICHKHO gd
JOIN NHANVIEN nv ON gd.MaNV = nv.MaNV;

-- Đường 25: CHITIETTRA → HANGCOSERI → CHITIETDONHANG → MATHANG → LOAIHANG
-- Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó đã bán ở dòng đơn nào; dòng đơn đó bán mặt hàng nào; mặt hàng đó thuộc loại hàng nào.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM CHITIETTRA cr
JOIN HANGCOSERI hs ON cr.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETDONHANG ct ON hs.MaDH = ct.MaDH AND hs.SoDongDH = ct.SoDongDH
JOIN MATHANG mh ON ct.MaSP = mh.MaSP
JOIN LOAIHANG lh ON mh.MaLoai = lh.MaLoai;

-- Đường 26: CHITIETTRA → HANGCOSERI → CHITIETDONHANG → MATHANG → THUONGHIEU
-- Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó đã bán ở dòng đơn nào; dòng đơn đó bán mặt hàng nào; mặt hàng đó mang thương hiệu nào.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM CHITIETTRA cr
JOIN HANGCOSERI hs ON cr.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETDONHANG ct ON hs.MaDH = ct.MaDH AND hs.SoDongDH = ct.SoDongDH
JOIN MATHANG mh ON ct.MaSP = mh.MaSP
JOIN THUONGHIEU th ON mh.MaTH = th.MaTH;

-- Đường 27: CHITIETTRA → HANGCOSERI → CHITIETDONHANG → DONHANG → KHACHHANG
-- Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó đã bán ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách).
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM CHITIETTRA cr
JOIN HANGCOSERI hs ON cr.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETDONHANG ct ON hs.MaDH = ct.MaDH AND hs.SoDongDH = ct.SoDongDH
JOIN DONHANG dh ON ct.MaDH = dh.MaDH
JOIN KHACHHANG kh ON dh.MaKH = kh.MaKH;

-- Đường 28: CHITIETTRA → HANGCOSERI → CHITIETDONHANG → DONHANG → NHANVIEN
-- Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó đã bán ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó do nhân viên nào lập.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM CHITIETTRA cr
JOIN HANGCOSERI hs ON cr.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETDONHANG ct ON hs.MaDH = ct.MaDH AND hs.SoDongDH = ct.SoDongDH
JOIN DONHANG dh ON ct.MaDH = dh.MaDH
JOIN NHANVIEN nv ON dh.MaNV = nv.MaNV;

-- Đường 29: CHITIETTRA → HANGCOSERI → CHITIETDONHANG → DONHANG → MAGIAMGIA → NHANVIEN
-- Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó đã bán ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM CHITIETTRA cr
JOIN HANGCOSERI hs ON cr.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETDONHANG ct ON hs.MaDH = ct.MaDH AND hs.SoDongDH = ct.SoDongDH
JOIN DONHANG dh ON ct.MaDH = dh.MaDH
JOIN MAGIAMGIA mg ON dh.MaMG = mg.MaMG
JOIN NHANVIEN nv ON mg.MaNV = nv.MaNV;

-- Đường 30: CHITIETTRA → HANGCOSERI → CHITIETPHIEUNHAP → MATHANG → LOAIHANG
-- Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó nhập mặt hàng nào; mặt hàng đó thuộc loại hàng nào.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM CHITIETTRA cr
JOIN HANGCOSERI hs ON cr.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETPHIEUNHAP cp ON hs.MaPN = cp.MaPN AND hs.SoDongPN = cp.SoDongPN
JOIN MATHANG mh ON cp.MaSP = mh.MaSP
JOIN LOAIHANG lh ON mh.MaLoai = lh.MaLoai;

-- Đường 31: CHITIETTRA → HANGCOSERI → CHITIETPHIEUNHAP → MATHANG → THUONGHIEU
-- Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó nhập mặt hàng nào; mặt hàng đó mang thương hiệu nào.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM CHITIETTRA cr
JOIN HANGCOSERI hs ON cr.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETPHIEUNHAP cp ON hs.MaPN = cp.MaPN AND hs.SoDongPN = cp.SoDongPN
JOIN MATHANG mh ON cp.MaSP = mh.MaSP
JOIN THUONGHIEU th ON mh.MaTH = th.MaTH;

-- Đường 32: CHITIETTRA → HANGCOSERI → CHITIETPHIEUNHAP → PHIEUNHAP → NHANVIEN
-- Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó thuộc phiếu nhập nào; phiếu nhập đó do nhân viên kho nào lập.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM CHITIETTRA cr
JOIN HANGCOSERI hs ON cr.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETPHIEUNHAP cp ON hs.MaPN = cp.MaPN AND hs.SoDongPN = cp.SoDongPN
JOIN PHIEUNHAP pn ON cp.MaPN = pn.MaPN
JOIN NHANVIEN nv ON pn.MaNV = nv.MaNV;

-- Đường 33: CHITIETTRA → HANGCOSERI → CHITIETPHIEUNHAP → PHIEUNHAP → NHACUNGCAP
-- Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó thuộc phiếu nhập nào; phiếu nhập đó nhận từ nhà cung cấp nào.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM CHITIETTRA cr
JOIN HANGCOSERI hs ON cr.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETPHIEUNHAP cp ON hs.MaPN = cp.MaPN AND hs.SoDongPN = cp.SoDongPN
JOIN PHIEUNHAP pn ON cp.MaPN = pn.MaPN
JOIN NHACUNGCAP nc ON pn.MaNCC = nc.MaNCC;

-- Đường 34: CHITIETTRA → HOSODOITRA → NHANVIEN
-- Cho biết dòng trả hàng thuộc hồ sơ đổi trả nào; hồ sơ đổi trả đó do nhân viên nào tiếp nhận.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM CHITIETTRA cr
JOIN HOSODOITRA hd ON cr.MaHS = hd.MaHS
JOIN NHANVIEN nv ON hd.MaNV = nv.MaNV;

-- Đường 35: CHITIETTRA → HOSODOITRA → DONHANG → KHACHHANG
-- Cho biết dòng trả hàng thuộc hồ sơ đổi trả nào; hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách).
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM CHITIETTRA cr
JOIN HOSODOITRA hd ON cr.MaHS = hd.MaHS
JOIN DONHANG dh ON hd.MaDH = dh.MaDH
JOIN KHACHHANG kh ON dh.MaKH = kh.MaKH;

-- Đường 36: CHITIETTRA → HOSODOITRA → DONHANG → NHANVIEN
-- Cho biết dòng trả hàng thuộc hồ sơ đổi trả nào; hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó do nhân viên nào lập.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM CHITIETTRA cr
JOIN HOSODOITRA hd ON cr.MaHS = hd.MaHS
JOIN DONHANG dh ON hd.MaDH = dh.MaDH
JOIN NHANVIEN nv ON dh.MaNV = nv.MaNV;

-- Đường 37: CHITIETTRA → HOSODOITRA → DONHANG → MAGIAMGIA → NHANVIEN
-- Cho biết dòng trả hàng thuộc hồ sơ đổi trả nào; hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM CHITIETTRA cr
JOIN HOSODOITRA hd ON cr.MaHS = hd.MaHS
JOIN DONHANG dh ON hd.MaDH = dh.MaDH
JOIN MAGIAMGIA mg ON dh.MaMG = mg.MaMG
JOIN NHANVIEN nv ON mg.MaNV = nv.MaNV;

-- Đường 38: LANNHANLAI → NHANVIEN
-- Cho biết lần nhận lại hàng do nhân viên nào kiểm tra.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM LANNHANLAI nl
JOIN NHANVIEN nv ON nl.MaNV = nv.MaNV;

-- Đường 39: LANNHANLAI → HOSODOITRA → NHANVIEN
-- Cho biết lần nhận lại hàng thuộc hồ sơ đổi trả nào; hồ sơ đổi trả đó do nhân viên nào tiếp nhận.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM LANNHANLAI nl
JOIN HOSODOITRA hd ON nl.MaHS = hd.MaHS
JOIN NHANVIEN nv ON hd.MaNV = nv.MaNV;

-- Đường 40: LANNHANLAI → HOSODOITRA → DONHANG → KHACHHANG
-- Cho biết lần nhận lại hàng thuộc hồ sơ đổi trả nào; hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách).
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM LANNHANLAI nl
JOIN HOSODOITRA hd ON nl.MaHS = hd.MaHS
JOIN DONHANG dh ON hd.MaDH = dh.MaDH
JOIN KHACHHANG kh ON dh.MaKH = kh.MaKH;

-- Đường 41: LANNHANLAI → HOSODOITRA → DONHANG → NHANVIEN
-- Cho biết lần nhận lại hàng thuộc hồ sơ đổi trả nào; hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó do nhân viên nào lập.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM LANNHANLAI nl
JOIN HOSODOITRA hd ON nl.MaHS = hd.MaHS
JOIN DONHANG dh ON hd.MaDH = dh.MaDH
JOIN NHANVIEN nv ON dh.MaNV = nv.MaNV;

-- Đường 42: LANNHANLAI → HOSODOITRA → DONHANG → MAGIAMGIA → NHANVIEN
-- Cho biết lần nhận lại hàng thuộc hồ sơ đổi trả nào; hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM LANNHANLAI nl
JOIN HOSODOITRA hd ON nl.MaHS = hd.MaHS
JOIN DONHANG dh ON hd.MaDH = dh.MaDH
JOIN MAGIAMGIA mg ON dh.MaMG = mg.MaMG
JOIN NHANVIEN nv ON mg.MaNV = nv.MaNV;

-- Đường 43: KHOANHOAN → NHANVIEN
-- Cho biết khoản hoàn tiền do người quản lý nào duyệt.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM KHOANHOAN kc
JOIN NHANVIEN nv ON kc.MaNV = nv.MaNV;

-- Đường 44: KHOANHOAN → THANHTOAN → NHANVIEN
-- Cho biết khoản hoàn tiền tính trên khoản thanh toán nào; khoản thanh toán đó do nhân viên nào xác nhận thu.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM KHOANHOAN kc
JOIN THANHTOAN tt ON kc.MaTT = tt.MaTT
JOIN NHANVIEN nv ON tt.MaNV = nv.MaNV;

-- Đường 45: KHOANHOAN → THANHTOAN → DONHANG → KHACHHANG
-- Cho biết khoản hoàn tiền tính trên khoản thanh toán nào; khoản thanh toán đó trả cho đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách).
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM KHOANHOAN kc
JOIN THANHTOAN tt ON kc.MaTT = tt.MaTT
JOIN DONHANG dh ON tt.MaDH = dh.MaDH
JOIN KHACHHANG kh ON dh.MaKH = kh.MaKH;

-- Đường 46: KHOANHOAN → THANHTOAN → DONHANG → NHANVIEN
-- Cho biết khoản hoàn tiền tính trên khoản thanh toán nào; khoản thanh toán đó trả cho đơn hàng nào; đơn hàng đó do nhân viên nào lập.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM KHOANHOAN kc
JOIN THANHTOAN tt ON kc.MaTT = tt.MaTT
JOIN DONHANG dh ON tt.MaDH = dh.MaDH
JOIN NHANVIEN nv ON dh.MaNV = nv.MaNV;

-- Đường 47: KHOANHOAN → THANHTOAN → DONHANG → MAGIAMGIA → NHANVIEN
-- Cho biết khoản hoàn tiền tính trên khoản thanh toán nào; khoản thanh toán đó trả cho đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM KHOANHOAN kc
JOIN THANHTOAN tt ON kc.MaTT = tt.MaTT
JOIN DONHANG dh ON tt.MaDH = dh.MaDH
JOIN MAGIAMGIA mg ON dh.MaMG = mg.MaMG
JOIN NHANVIEN nv ON mg.MaNV = nv.MaNV;

-- Đường 48: KHOANHOAN → HOSODOITRA → NHANVIEN
-- Cho biết khoản hoàn tiền theo hồ sơ đổi trả nào (nếu do đổi trả); hồ sơ đổi trả đó do nhân viên nào tiếp nhận.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM KHOANHOAN kc
JOIN HOSODOITRA hd ON kc.MaHS = hd.MaHS
JOIN NHANVIEN nv ON hd.MaNV = nv.MaNV;

-- Đường 49: KHOANHOAN → HOSODOITRA → DONHANG → KHACHHANG
-- Cho biết khoản hoàn tiền theo hồ sơ đổi trả nào (nếu do đổi trả); hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách).
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM KHOANHOAN kc
JOIN HOSODOITRA hd ON kc.MaHS = hd.MaHS
JOIN DONHANG dh ON hd.MaDH = dh.MaDH
JOIN KHACHHANG kh ON dh.MaKH = kh.MaKH;

-- Đường 50: KHOANHOAN → HOSODOITRA → DONHANG → NHANVIEN
-- Cho biết khoản hoàn tiền theo hồ sơ đổi trả nào (nếu do đổi trả); hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó do nhân viên nào lập.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM KHOANHOAN kc
JOIN HOSODOITRA hd ON kc.MaHS = hd.MaHS
JOIN DONHANG dh ON hd.MaDH = dh.MaDH
JOIN NHANVIEN nv ON dh.MaNV = nv.MaNV;

-- Đường 51: KHOANHOAN → HOSODOITRA → DONHANG → MAGIAMGIA → NHANVIEN
-- Cho biết khoản hoàn tiền theo hồ sơ đổi trả nào (nếu do đổi trả); hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM KHOANHOAN kc
JOIN HOSODOITRA hd ON kc.MaHS = hd.MaHS
JOIN DONHANG dh ON hd.MaDH = dh.MaDH
JOIN MAGIAMGIA mg ON dh.MaMG = mg.MaMG
JOIN NHANVIEN nv ON mg.MaNV = nv.MaNV;

-- Đường 52: PHIEUBAOHANH → NHANVIEN
-- Cho biết phiếu bảo hành do nhân viên nào tiếp nhận.
-- Số dòng trên dữ liệu minh họa: 2
SELECT *
FROM PHIEUBAOHANH bh
JOIN NHANVIEN nv ON bh.MaNV = nv.MaNV;

-- Đường 53: PHIEUBAOHANH → CHITIETDONHANG → MATHANG → LOAIHANG
-- Cho biết phiếu bảo hành mua ở dòng đơn nào; dòng đơn đó bán mặt hàng nào; mặt hàng đó thuộc loại hàng nào.
-- Số dòng trên dữ liệu minh họa: 2
SELECT *
FROM PHIEUBAOHANH bh
JOIN CHITIETDONHANG ct ON bh.MaDH = ct.MaDH AND bh.SoDongDH = ct.SoDongDH
JOIN MATHANG mh ON ct.MaSP = mh.MaSP
JOIN LOAIHANG lh ON mh.MaLoai = lh.MaLoai;

-- Đường 54: PHIEUBAOHANH → CHITIETDONHANG → MATHANG → THUONGHIEU
-- Cho biết phiếu bảo hành mua ở dòng đơn nào; dòng đơn đó bán mặt hàng nào; mặt hàng đó mang thương hiệu nào.
-- Số dòng trên dữ liệu minh họa: 2
SELECT *
FROM PHIEUBAOHANH bh
JOIN CHITIETDONHANG ct ON bh.MaDH = ct.MaDH AND bh.SoDongDH = ct.SoDongDH
JOIN MATHANG mh ON ct.MaSP = mh.MaSP
JOIN THUONGHIEU th ON mh.MaTH = th.MaTH;

-- Đường 55: PHIEUBAOHANH → CHITIETDONHANG → DONHANG → KHACHHANG
-- Cho biết phiếu bảo hành mua ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách).
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM PHIEUBAOHANH bh
JOIN CHITIETDONHANG ct ON bh.MaDH = ct.MaDH AND bh.SoDongDH = ct.SoDongDH
JOIN DONHANG dh ON ct.MaDH = dh.MaDH
JOIN KHACHHANG kh ON dh.MaKH = kh.MaKH;

-- Đường 56: PHIEUBAOHANH → CHITIETDONHANG → DONHANG → NHANVIEN
-- Cho biết phiếu bảo hành mua ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó do nhân viên nào lập.
-- Số dòng trên dữ liệu minh họa: 2
SELECT *
FROM PHIEUBAOHANH bh
JOIN CHITIETDONHANG ct ON bh.MaDH = ct.MaDH AND bh.SoDongDH = ct.SoDongDH
JOIN DONHANG dh ON ct.MaDH = dh.MaDH
JOIN NHANVIEN nv ON dh.MaNV = nv.MaNV;

-- Đường 57: PHIEUBAOHANH → CHITIETDONHANG → DONHANG → MAGIAMGIA → NHANVIEN
-- Cho biết phiếu bảo hành mua ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM PHIEUBAOHANH bh
JOIN CHITIETDONHANG ct ON bh.MaDH = ct.MaDH AND bh.SoDongDH = ct.SoDongDH
JOIN DONHANG dh ON ct.MaDH = dh.MaDH
JOIN MAGIAMGIA mg ON dh.MaMG = mg.MaMG
JOIN NHANVIEN nv ON mg.MaNV = nv.MaNV;

-- Đường 58: PHIEUBAOHANH → HANGCOSERI → CHITIETDONHANG → MATHANG → LOAIHANG
-- Cho biết phiếu bảo hành ứng với chiếc hàng có seri nào; chiếc hàng có seri đó đã bán ở dòng đơn nào; dòng đơn đó bán mặt hàng nào; mặt hàng đó thuộc loại hàng nào.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM PHIEUBAOHANH bh
JOIN HANGCOSERI hs ON bh.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETDONHANG ct ON hs.MaDH = ct.MaDH AND hs.SoDongDH = ct.SoDongDH
JOIN MATHANG mh ON ct.MaSP = mh.MaSP
JOIN LOAIHANG lh ON mh.MaLoai = lh.MaLoai;

-- Đường 59: PHIEUBAOHANH → HANGCOSERI → CHITIETDONHANG → MATHANG → THUONGHIEU
-- Cho biết phiếu bảo hành ứng với chiếc hàng có seri nào; chiếc hàng có seri đó đã bán ở dòng đơn nào; dòng đơn đó bán mặt hàng nào; mặt hàng đó mang thương hiệu nào.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM PHIEUBAOHANH bh
JOIN HANGCOSERI hs ON bh.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETDONHANG ct ON hs.MaDH = ct.MaDH AND hs.SoDongDH = ct.SoDongDH
JOIN MATHANG mh ON ct.MaSP = mh.MaSP
JOIN THUONGHIEU th ON mh.MaTH = th.MaTH;

-- Đường 60: PHIEUBAOHANH → HANGCOSERI → CHITIETDONHANG → DONHANG → KHACHHANG
-- Cho biết phiếu bảo hành ứng với chiếc hàng có seri nào; chiếc hàng có seri đó đã bán ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách).
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM PHIEUBAOHANH bh
JOIN HANGCOSERI hs ON bh.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETDONHANG ct ON hs.MaDH = ct.MaDH AND hs.SoDongDH = ct.SoDongDH
JOIN DONHANG dh ON ct.MaDH = dh.MaDH
JOIN KHACHHANG kh ON dh.MaKH = kh.MaKH;

-- Đường 61: PHIEUBAOHANH → HANGCOSERI → CHITIETDONHANG → DONHANG → NHANVIEN
-- Cho biết phiếu bảo hành ứng với chiếc hàng có seri nào; chiếc hàng có seri đó đã bán ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó do nhân viên nào lập.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM PHIEUBAOHANH bh
JOIN HANGCOSERI hs ON bh.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETDONHANG ct ON hs.MaDH = ct.MaDH AND hs.SoDongDH = ct.SoDongDH
JOIN DONHANG dh ON ct.MaDH = dh.MaDH
JOIN NHANVIEN nv ON dh.MaNV = nv.MaNV;

-- Đường 62: PHIEUBAOHANH → HANGCOSERI → CHITIETDONHANG → DONHANG → MAGIAMGIA → NHANVIEN
-- Cho biết phiếu bảo hành ứng với chiếc hàng có seri nào; chiếc hàng có seri đó đã bán ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM PHIEUBAOHANH bh
JOIN HANGCOSERI hs ON bh.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETDONHANG ct ON hs.MaDH = ct.MaDH AND hs.SoDongDH = ct.SoDongDH
JOIN DONHANG dh ON ct.MaDH = dh.MaDH
JOIN MAGIAMGIA mg ON dh.MaMG = mg.MaMG
JOIN NHANVIEN nv ON mg.MaNV = nv.MaNV;

-- Đường 63: PHIEUBAOHANH → HANGCOSERI → CHITIETPHIEUNHAP → MATHANG → LOAIHANG
-- Cho biết phiếu bảo hành ứng với chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó nhập mặt hàng nào; mặt hàng đó thuộc loại hàng nào.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM PHIEUBAOHANH bh
JOIN HANGCOSERI hs ON bh.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETPHIEUNHAP cp ON hs.MaPN = cp.MaPN AND hs.SoDongPN = cp.SoDongPN
JOIN MATHANG mh ON cp.MaSP = mh.MaSP
JOIN LOAIHANG lh ON mh.MaLoai = lh.MaLoai;

-- Đường 64: PHIEUBAOHANH → HANGCOSERI → CHITIETPHIEUNHAP → MATHANG → THUONGHIEU
-- Cho biết phiếu bảo hành ứng với chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó nhập mặt hàng nào; mặt hàng đó mang thương hiệu nào.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM PHIEUBAOHANH bh
JOIN HANGCOSERI hs ON bh.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETPHIEUNHAP cp ON hs.MaPN = cp.MaPN AND hs.SoDongPN = cp.SoDongPN
JOIN MATHANG mh ON cp.MaSP = mh.MaSP
JOIN THUONGHIEU th ON mh.MaTH = th.MaTH;

-- Đường 65: PHIEUBAOHANH → HANGCOSERI → CHITIETPHIEUNHAP → PHIEUNHAP → NHANVIEN
-- Cho biết phiếu bảo hành ứng với chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó thuộc phiếu nhập nào; phiếu nhập đó do nhân viên kho nào lập.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM PHIEUBAOHANH bh
JOIN HANGCOSERI hs ON bh.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETPHIEUNHAP cp ON hs.MaPN = cp.MaPN AND hs.SoDongPN = cp.SoDongPN
JOIN PHIEUNHAP pn ON cp.MaPN = pn.MaPN
JOIN NHANVIEN nv ON pn.MaNV = nv.MaNV;

-- Đường 66: PHIEUBAOHANH → HANGCOSERI → CHITIETPHIEUNHAP → PHIEUNHAP → NHACUNGCAP
-- Cho biết phiếu bảo hành ứng với chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó thuộc phiếu nhập nào; phiếu nhập đó nhận từ nhà cung cấp nào.
-- Số dòng trên dữ liệu minh họa: 1
SELECT *
FROM PHIEUBAOHANH bh
JOIN HANGCOSERI hs ON bh.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETPHIEUNHAP cp ON hs.MaPN = cp.MaPN AND hs.SoDongPN = cp.SoDongPN
JOIN PHIEUNHAP pn ON cp.MaPN = pn.MaPN
JOIN NHACUNGCAP nc ON pn.MaNCC = nc.MaNCC;

