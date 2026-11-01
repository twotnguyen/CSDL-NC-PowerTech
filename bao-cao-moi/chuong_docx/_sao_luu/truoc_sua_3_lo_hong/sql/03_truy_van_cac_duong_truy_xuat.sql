-- 57 truy vấn cho các con đường truy xuất từ 9 nút vào (sinh bằng tools/gen_chuong3.py).
-- Mỗi truy vấn nối các quan hệ theo từng cung của đường; đã chạy thử trên dữ liệu minh họa (sql/02) và đều có kết quả, trừ đường rỗng đúng quy tắc (có ghi chú).

-- Đường 1: ANHMATHANG → MATHANG → LOAIHANG
-- Cho biết ảnh mặt hàng minh họa cho mặt hàng nào; mặt hàng đó thuộc loại hàng nào.
-- Số dòng trên dữ liệu minh họa: 5
SELECT am.MaAnh, mh.MaSP, lh.MaLoai
FROM ANHMATHANG am
JOIN MATHANG mh ON am.MaSP = mh.MaSP
JOIN LOAIHANG lh ON mh.MaLoai = lh.MaLoai;

-- Đường 2: ANHMATHANG → MATHANG → THUONGHIEU
-- Cho biết ảnh mặt hàng minh họa cho mặt hàng nào; mặt hàng đó mang thương hiệu nào.
-- Số dòng trên dữ liệu minh họa: 5
SELECT am.MaAnh, mh.MaSP, th.MaTH
FROM ANHMATHANG am
JOIN MATHANG mh ON am.MaSP = mh.MaSP
JOIN THUONGHIEU th ON mh.MaTH = th.MaTH;

-- Đường 3: GIATRITHONGSO → MATHANG → LOAIHANG
-- Cho biết giá trị thông số thuộc mặt hàng nào; mặt hàng đó thuộc loại hàng nào.
-- Số dòng trên dữ liệu minh họa: 5
SELECT gt.MaSP, gt.MaTS, lh.MaLoai
FROM GIATRITHONGSO gt
JOIN MATHANG mh ON gt.MaSP = mh.MaSP
JOIN LOAIHANG lh ON mh.MaLoai = lh.MaLoai;

-- Đường 4: GIATRITHONGSO → MATHANG → THUONGHIEU
-- Cho biết giá trị thông số thuộc mặt hàng nào; mặt hàng đó mang thương hiệu nào.
-- Số dòng trên dữ liệu minh họa: 5
SELECT gt.MaSP, gt.MaTS, th.MaTH
FROM GIATRITHONGSO gt
JOIN MATHANG mh ON gt.MaSP = mh.MaSP
JOIN THUONGHIEU th ON mh.MaTH = th.MaTH;

-- Đường 5: GIATRITHONGSO → DINHNGHIATHONGSO → LOAIHANG
-- Cho biết giá trị thông số ứng với thông số nào; thông số đó do loại hàng nào quy định.
-- Số dòng trên dữ liệu minh họa: 5
SELECT gt.MaSP, gt.MaTS, lh.MaLoai
FROM GIATRITHONGSO gt
JOIN DINHNGHIATHONGSO dn ON gt.MaTS = dn.MaTS
JOIN LOAIHANG lh ON dn.MaLoai = lh.MaLoai;

-- Đường 6: TAIKHOAN → KHACHHANG
-- Cho biết tài khoản thuộc khách hàng nào (nếu là tài khoản khách).
-- Số dòng trên dữ liệu minh họa: 3
SELECT tk.MaTK, kh.MaKH
FROM TAIKHOAN tk
JOIN KHACHHANG kh ON tk.MaKH = kh.MaKH;

-- Đường 7: TAIKHOAN → NHANVIEN
-- Cho biết tài khoản thuộc nhân viên nào (nếu là tài khoản nhân viên).
-- Số dòng trên dữ liệu minh họa: 3
SELECT tk.MaTK, nv.MaNV
FROM TAIKHOAN tk
JOIN NHANVIEN nv ON tk.MaNV = nv.MaNV;

-- Đường 8: LANGIAO → NHANVIEN
-- Cho biết lần giao hàng do nhân viên nào giao.
-- Số dòng trên dữ liệu minh họa: 4
SELECT lg.MaGiao, lg.SoLan, nv.MaNV
FROM LANGIAO lg
JOIN NHANVIEN nv ON lg.MaNV = nv.MaNV;

-- Đường 9: LANGIAO → PHIEUGIAO → NHANVIEN
-- Cho biết lần giao hàng thuộc phiếu giao nào; phiếu giao đó do nhân viên nào giao.
-- Số dòng trên dữ liệu minh họa: 4
SELECT lg.MaGiao, lg.SoLan, nv.MaNV
FROM LANGIAO lg
JOIN PHIEUGIAO pg ON lg.MaGiao = pg.MaGiao
JOIN NHANVIEN nv ON pg.MaNV = nv.MaNV;

-- Đường 10: LANGIAO → PHIEUGIAO → DONHANG → KHACHHANG
-- Cho biết lần giao hàng thuộc phiếu giao nào; phiếu giao đó lập cho đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách).
-- Số dòng trên dữ liệu minh họa: 4
SELECT lg.MaGiao, lg.SoLan, dh.MaDH, kh.MaKH
FROM LANGIAO lg
JOIN PHIEUGIAO pg ON lg.MaGiao = pg.MaGiao
JOIN DONHANG dh ON pg.MaDH = dh.MaDH
JOIN KHACHHANG kh ON dh.MaKH = kh.MaKH;

-- Đường 11: LANGIAO → PHIEUGIAO → DONHANG → NHANVIEN
-- Cho biết lần giao hàng thuộc phiếu giao nào; phiếu giao đó lập cho đơn hàng nào; đơn hàng đó do nhân viên nào lập.
-- Số dòng trên dữ liệu minh họa: 1
SELECT lg.MaGiao, lg.SoLan, dh.MaDH, nv.MaNV
FROM LANGIAO lg
JOIN PHIEUGIAO pg ON lg.MaGiao = pg.MaGiao
JOIN DONHANG dh ON pg.MaDH = dh.MaDH
JOIN NHANVIEN nv ON dh.MaNV = nv.MaNV;

-- Đường 12: LANGIAO → PHIEUGIAO → DONHANG → MAGIAMGIA → NHANVIEN
-- Cho biết lần giao hàng thuộc phiếu giao nào; phiếu giao đó lập cho đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo.
-- Số dòng trên dữ liệu minh họa: 1
SELECT lg.MaGiao, lg.SoLan, dh.MaDH, mg.MaMG, nv.MaNV
FROM LANGIAO lg
JOIN PHIEUGIAO pg ON lg.MaGiao = pg.MaGiao
JOIN DONHANG dh ON pg.MaDH = dh.MaDH
JOIN MAGIAMGIA mg ON dh.MaMG = mg.MaMG
JOIN NHANVIEN nv ON mg.MaNV = nv.MaNV;

-- Đường 13: GIAODICHKHO → MATHANG → LOAIHANG
-- Cho biết giao dịch kho liên quan đến mặt hàng nào; mặt hàng đó thuộc loại hàng nào.
-- Số dòng trên dữ liệu minh họa: 4
SELECT gd.MaGDK, mh.MaSP, lh.MaLoai
FROM GIAODICHKHO gd
JOIN MATHANG mh ON gd.MaSP = mh.MaSP
JOIN LOAIHANG lh ON mh.MaLoai = lh.MaLoai;

-- Đường 14: GIAODICHKHO → MATHANG → THUONGHIEU
-- Cho biết giao dịch kho liên quan đến mặt hàng nào; mặt hàng đó mang thương hiệu nào.
-- Số dòng trên dữ liệu minh họa: 4
SELECT gd.MaGDK, mh.MaSP, th.MaTH
FROM GIAODICHKHO gd
JOIN MATHANG mh ON gd.MaSP = mh.MaSP
JOIN THUONGHIEU th ON mh.MaTH = th.MaTH;

-- Đường 15: GIAODICHKHO → NHANVIEN
-- Cho biết giao dịch kho do nhân viên nào thực hiện.
-- Số dòng trên dữ liệu minh họa: 4
SELECT gd.MaGDK, nv.MaNV
FROM GIAODICHKHO gd
JOIN NHANVIEN nv ON gd.MaNV = nv.MaNV;

-- Đường 16: CHITIETTRA → HANGCOSERI → CHITIETDONHANG → MATHANG → LOAIHANG
-- Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó đã bán ở dòng đơn nào; dòng đơn đó bán mặt hàng nào; mặt hàng đó thuộc loại hàng nào.
-- Số dòng trên dữ liệu minh họa: 1
SELECT cr.MaHS, cr.SoDongDH, hs.MaSeri, ct.MaDH, mh.MaSP, lh.MaLoai
FROM CHITIETTRA cr
JOIN HANGCOSERI hs ON cr.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETDONHANG ct ON hs.MaDH = ct.MaDH AND hs.SoDongDH = ct.SoDongDH
JOIN MATHANG mh ON ct.MaSP = mh.MaSP
JOIN LOAIHANG lh ON mh.MaLoai = lh.MaLoai;

-- Đường 17: CHITIETTRA → HANGCOSERI → CHITIETDONHANG → MATHANG → THUONGHIEU
-- Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó đã bán ở dòng đơn nào; dòng đơn đó bán mặt hàng nào; mặt hàng đó mang thương hiệu nào.
-- Số dòng trên dữ liệu minh họa: 1
SELECT cr.MaHS, cr.SoDongDH, hs.MaSeri, ct.MaDH, mh.MaSP, th.MaTH
FROM CHITIETTRA cr
JOIN HANGCOSERI hs ON cr.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETDONHANG ct ON hs.MaDH = ct.MaDH AND hs.SoDongDH = ct.SoDongDH
JOIN MATHANG mh ON ct.MaSP = mh.MaSP
JOIN THUONGHIEU th ON mh.MaTH = th.MaTH;

-- Đường 18: CHITIETTRA → HANGCOSERI → CHITIETDONHANG → DONHANG → KHACHHANG
-- Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó đã bán ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách).
-- Số dòng trên dữ liệu minh họa: 1
SELECT cr.MaHS, cr.SoDongDH, hs.MaSeri, ct.MaDH, kh.MaKH
FROM CHITIETTRA cr
JOIN HANGCOSERI hs ON cr.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETDONHANG ct ON hs.MaDH = ct.MaDH AND hs.SoDongDH = ct.SoDongDH
JOIN DONHANG dh ON ct.MaDH = dh.MaDH
JOIN KHACHHANG kh ON dh.MaKH = kh.MaKH;

-- Đường 19: CHITIETTRA → HANGCOSERI → CHITIETDONHANG → DONHANG → NHANVIEN
-- Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó đã bán ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó do nhân viên nào lập.
-- Số dòng trên dữ liệu minh họa: 1
SELECT cr.MaHS, cr.SoDongDH, hs.MaSeri, ct.MaDH, nv.MaNV
FROM CHITIETTRA cr
JOIN HANGCOSERI hs ON cr.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETDONHANG ct ON hs.MaDH = ct.MaDH AND hs.SoDongDH = ct.SoDongDH
JOIN DONHANG dh ON ct.MaDH = dh.MaDH
JOIN NHANVIEN nv ON dh.MaNV = nv.MaNV;

-- Đường 20: CHITIETTRA → HANGCOSERI → CHITIETDONHANG → DONHANG → MAGIAMGIA → NHANVIEN
-- Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó đã bán ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo.
-- Số dòng trên dữ liệu minh họa: 1
SELECT cr.MaHS, cr.SoDongDH, hs.MaSeri, ct.MaDH, mg.MaMG, nv.MaNV
FROM CHITIETTRA cr
JOIN HANGCOSERI hs ON cr.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETDONHANG ct ON hs.MaDH = ct.MaDH AND hs.SoDongDH = ct.SoDongDH
JOIN DONHANG dh ON ct.MaDH = dh.MaDH
JOIN MAGIAMGIA mg ON dh.MaMG = mg.MaMG
JOIN NHANVIEN nv ON mg.MaNV = nv.MaNV;

-- Đường 21: CHITIETTRA → HANGCOSERI → CHITIETPHIEUNHAP → MATHANG → LOAIHANG
-- Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó nhập mặt hàng nào; mặt hàng đó thuộc loại hàng nào.
-- Số dòng trên dữ liệu minh họa: 1
SELECT cr.MaHS, cr.SoDongDH, hs.MaSeri, cp.MaPN, cp.SoDongPN, mh.MaSP, lh.MaLoai
FROM CHITIETTRA cr
JOIN HANGCOSERI hs ON cr.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETPHIEUNHAP cp ON hs.MaPN = cp.MaPN AND hs.SoDongPN = cp.SoDongPN
JOIN MATHANG mh ON cp.MaSP = mh.MaSP
JOIN LOAIHANG lh ON mh.MaLoai = lh.MaLoai;

-- Đường 22: CHITIETTRA → HANGCOSERI → CHITIETPHIEUNHAP → MATHANG → THUONGHIEU
-- Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó nhập mặt hàng nào; mặt hàng đó mang thương hiệu nào.
-- Số dòng trên dữ liệu minh họa: 1
SELECT cr.MaHS, cr.SoDongDH, hs.MaSeri, cp.MaPN, cp.SoDongPN, mh.MaSP, th.MaTH
FROM CHITIETTRA cr
JOIN HANGCOSERI hs ON cr.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETPHIEUNHAP cp ON hs.MaPN = cp.MaPN AND hs.SoDongPN = cp.SoDongPN
JOIN MATHANG mh ON cp.MaSP = mh.MaSP
JOIN THUONGHIEU th ON mh.MaTH = th.MaTH;

-- Đường 23: CHITIETTRA → HANGCOSERI → CHITIETPHIEUNHAP → PHIEUNHAP → NHANVIEN
-- Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó thuộc phiếu nhập nào; phiếu nhập đó do nhân viên kho nào lập.
-- Số dòng trên dữ liệu minh họa: 1
SELECT cr.MaHS, cr.SoDongDH, hs.MaSeri, cp.MaPN, cp.SoDongPN, nv.MaNV
FROM CHITIETTRA cr
JOIN HANGCOSERI hs ON cr.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETPHIEUNHAP cp ON hs.MaPN = cp.MaPN AND hs.SoDongPN = cp.SoDongPN
JOIN PHIEUNHAP pn ON cp.MaPN = pn.MaPN
JOIN NHANVIEN nv ON pn.MaNV = nv.MaNV;

-- Đường 24: CHITIETTRA → HANGCOSERI → CHITIETPHIEUNHAP → PHIEUNHAP → NHACUNGCAP
-- Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó thuộc phiếu nhập nào; phiếu nhập đó nhận từ nhà cung cấp nào.
-- Số dòng trên dữ liệu minh họa: 1
SELECT cr.MaHS, cr.SoDongDH, hs.MaSeri, cp.MaPN, cp.SoDongPN, nc.MaNCC
FROM CHITIETTRA cr
JOIN HANGCOSERI hs ON cr.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETPHIEUNHAP cp ON hs.MaPN = cp.MaPN AND hs.SoDongPN = cp.SoDongPN
JOIN PHIEUNHAP pn ON cp.MaPN = pn.MaPN
JOIN NHACUNGCAP nc ON pn.MaNCC = nc.MaNCC;

-- Đường 25: CHITIETTRA → HOSODOITRA → NHANVIEN
-- Cho biết dòng trả hàng thuộc hồ sơ đổi trả nào; hồ sơ đổi trả đó do nhân viên nào tiếp nhận.
-- Số dòng trên dữ liệu minh họa: 1
SELECT cr.MaHS, cr.SoDongDH, nv.MaNV
FROM CHITIETTRA cr
JOIN HOSODOITRA hd ON cr.MaHS = hd.MaHS
JOIN NHANVIEN nv ON hd.MaNV = nv.MaNV;

-- Đường 26: CHITIETTRA → HOSODOITRA → DONHANG → KHACHHANG
-- Cho biết dòng trả hàng thuộc hồ sơ đổi trả nào; hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách).
-- Số dòng trên dữ liệu minh họa: 1
SELECT cr.MaHS, cr.SoDongDH, dh.MaDH, kh.MaKH
FROM CHITIETTRA cr
JOIN HOSODOITRA hd ON cr.MaHS = hd.MaHS
JOIN DONHANG dh ON hd.MaDH = dh.MaDH
JOIN KHACHHANG kh ON dh.MaKH = kh.MaKH;

-- Đường 27: CHITIETTRA → HOSODOITRA → DONHANG → NHANVIEN
-- Cho biết dòng trả hàng thuộc hồ sơ đổi trả nào; hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó do nhân viên nào lập.
-- Số dòng trên dữ liệu minh họa: 1
SELECT cr.MaHS, cr.SoDongDH, dh.MaDH, nv.MaNV
FROM CHITIETTRA cr
JOIN HOSODOITRA hd ON cr.MaHS = hd.MaHS
JOIN DONHANG dh ON hd.MaDH = dh.MaDH
JOIN NHANVIEN nv ON dh.MaNV = nv.MaNV;

-- Đường 28: CHITIETTRA → HOSODOITRA → DONHANG → MAGIAMGIA → NHANVIEN
-- Cho biết dòng trả hàng thuộc hồ sơ đổi trả nào; hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo.
-- Số dòng trên dữ liệu minh họa: 1
SELECT cr.MaHS, cr.SoDongDH, dh.MaDH, mg.MaMG, nv.MaNV
FROM CHITIETTRA cr
JOIN HOSODOITRA hd ON cr.MaHS = hd.MaHS
JOIN DONHANG dh ON hd.MaDH = dh.MaDH
JOIN MAGIAMGIA mg ON dh.MaMG = mg.MaMG
JOIN NHANVIEN nv ON mg.MaNV = nv.MaNV;

-- Đường 29: LANNHANLAI → NHANVIEN
-- Cho biết lần nhận lại hàng do nhân viên nào kiểm tra.
-- Số dòng trên dữ liệu minh họa: 1
SELECT nl.MaNhanLai, nv.MaNV
FROM LANNHANLAI nl
JOIN NHANVIEN nv ON nl.MaNV = nv.MaNV;

-- Đường 30: LANNHANLAI → HOSODOITRA → NHANVIEN
-- Cho biết lần nhận lại hàng thuộc hồ sơ đổi trả nào; hồ sơ đổi trả đó do nhân viên nào tiếp nhận.
-- Số dòng trên dữ liệu minh họa: 1
SELECT nl.MaNhanLai, hd.MaHS, nv.MaNV
FROM LANNHANLAI nl
JOIN HOSODOITRA hd ON nl.MaHS = hd.MaHS
JOIN NHANVIEN nv ON hd.MaNV = nv.MaNV;

-- Đường 31: LANNHANLAI → HOSODOITRA → DONHANG → KHACHHANG
-- Cho biết lần nhận lại hàng thuộc hồ sơ đổi trả nào; hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách).
-- Số dòng trên dữ liệu minh họa: 1
SELECT nl.MaNhanLai, hd.MaHS, dh.MaDH, kh.MaKH
FROM LANNHANLAI nl
JOIN HOSODOITRA hd ON nl.MaHS = hd.MaHS
JOIN DONHANG dh ON hd.MaDH = dh.MaDH
JOIN KHACHHANG kh ON dh.MaKH = kh.MaKH;

-- Đường 32: LANNHANLAI → HOSODOITRA → DONHANG → NHANVIEN
-- Cho biết lần nhận lại hàng thuộc hồ sơ đổi trả nào; hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó do nhân viên nào lập.
-- Số dòng trên dữ liệu minh họa: 1
SELECT nl.MaNhanLai, hd.MaHS, dh.MaDH, nv.MaNV
FROM LANNHANLAI nl
JOIN HOSODOITRA hd ON nl.MaHS = hd.MaHS
JOIN DONHANG dh ON hd.MaDH = dh.MaDH
JOIN NHANVIEN nv ON dh.MaNV = nv.MaNV;

-- Đường 33: LANNHANLAI → HOSODOITRA → DONHANG → MAGIAMGIA → NHANVIEN
-- Cho biết lần nhận lại hàng thuộc hồ sơ đổi trả nào; hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo.
-- Số dòng trên dữ liệu minh họa: 1
SELECT nl.MaNhanLai, hd.MaHS, dh.MaDH, mg.MaMG, nv.MaNV
FROM LANNHANLAI nl
JOIN HOSODOITRA hd ON nl.MaHS = hd.MaHS
JOIN DONHANG dh ON hd.MaDH = dh.MaDH
JOIN MAGIAMGIA mg ON dh.MaMG = mg.MaMG
JOIN NHANVIEN nv ON mg.MaNV = nv.MaNV;

-- Đường 34: KHOANHOAN → NHANVIEN
-- Cho biết khoản hoàn tiền do người quản lý nào duyệt.
-- Số dòng trên dữ liệu minh họa: 1
SELECT kc.MaHoan, nv.MaNV
FROM KHOANHOAN kc
JOIN NHANVIEN nv ON kc.MaNV = nv.MaNV;

-- Đường 35: KHOANHOAN → THANHTOAN → NHANVIEN
-- Cho biết khoản hoàn tiền tính trên khoản thanh toán nào; khoản thanh toán đó do nhân viên nào xác nhận thu.
-- Số dòng trên dữ liệu minh họa: 1
SELECT kc.MaHoan, tt.MaTT, nv.MaNV
FROM KHOANHOAN kc
JOIN THANHTOAN tt ON kc.MaTT = tt.MaTT
JOIN NHANVIEN nv ON tt.MaNV = nv.MaNV;

-- Đường 36: KHOANHOAN → THANHTOAN → DONHANG → KHACHHANG
-- Cho biết khoản hoàn tiền tính trên khoản thanh toán nào; khoản thanh toán đó trả cho đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách).
-- Số dòng trên dữ liệu minh họa: 1
SELECT kc.MaHoan, tt.MaTT, dh.MaDH, kh.MaKH
FROM KHOANHOAN kc
JOIN THANHTOAN tt ON kc.MaTT = tt.MaTT
JOIN DONHANG dh ON tt.MaDH = dh.MaDH
JOIN KHACHHANG kh ON dh.MaKH = kh.MaKH;

-- Đường 37: KHOANHOAN → THANHTOAN → DONHANG → NHANVIEN
-- Cho biết khoản hoàn tiền tính trên khoản thanh toán nào; khoản thanh toán đó trả cho đơn hàng nào; đơn hàng đó do nhân viên nào lập.
-- Số dòng trên dữ liệu minh họa: 1
SELECT kc.MaHoan, tt.MaTT, dh.MaDH, nv.MaNV
FROM KHOANHOAN kc
JOIN THANHTOAN tt ON kc.MaTT = tt.MaTT
JOIN DONHANG dh ON tt.MaDH = dh.MaDH
JOIN NHANVIEN nv ON dh.MaNV = nv.MaNV;

-- Đường 38: KHOANHOAN → THANHTOAN → DONHANG → MAGIAMGIA → NHANVIEN
-- Cho biết khoản hoàn tiền tính trên khoản thanh toán nào; khoản thanh toán đó trả cho đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo.
-- Số dòng trên dữ liệu minh họa: 1
SELECT kc.MaHoan, tt.MaTT, dh.MaDH, mg.MaMG, nv.MaNV
FROM KHOANHOAN kc
JOIN THANHTOAN tt ON kc.MaTT = tt.MaTT
JOIN DONHANG dh ON tt.MaDH = dh.MaDH
JOIN MAGIAMGIA mg ON dh.MaMG = mg.MaMG
JOIN NHANVIEN nv ON mg.MaNV = nv.MaNV;

-- Đường 39: KHOANHOAN → HOSODOITRA → NHANVIEN
-- Cho biết khoản hoàn tiền theo hồ sơ đổi trả nào (nếu do đổi trả); hồ sơ đổi trả đó do nhân viên nào tiếp nhận.
-- Số dòng trên dữ liệu minh họa: 1
SELECT kc.MaHoan, hd.MaHS, nv.MaNV
FROM KHOANHOAN kc
JOIN HOSODOITRA hd ON kc.MaHS = hd.MaHS
JOIN NHANVIEN nv ON hd.MaNV = nv.MaNV;

-- Đường 40: KHOANHOAN → HOSODOITRA → DONHANG → KHACHHANG
-- Cho biết khoản hoàn tiền theo hồ sơ đổi trả nào (nếu do đổi trả); hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách).
-- Số dòng trên dữ liệu minh họa: 1
SELECT kc.MaHoan, hd.MaHS, dh.MaDH, kh.MaKH
FROM KHOANHOAN kc
JOIN HOSODOITRA hd ON kc.MaHS = hd.MaHS
JOIN DONHANG dh ON hd.MaDH = dh.MaDH
JOIN KHACHHANG kh ON dh.MaKH = kh.MaKH;

-- Đường 41: KHOANHOAN → HOSODOITRA → DONHANG → NHANVIEN
-- Cho biết khoản hoàn tiền theo hồ sơ đổi trả nào (nếu do đổi trả); hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó do nhân viên nào lập.
-- Số dòng trên dữ liệu minh họa: 1
SELECT kc.MaHoan, hd.MaHS, dh.MaDH, nv.MaNV
FROM KHOANHOAN kc
JOIN HOSODOITRA hd ON kc.MaHS = hd.MaHS
JOIN DONHANG dh ON hd.MaDH = dh.MaDH
JOIN NHANVIEN nv ON dh.MaNV = nv.MaNV;

-- Đường 42: KHOANHOAN → HOSODOITRA → DONHANG → MAGIAMGIA → NHANVIEN
-- Cho biết khoản hoàn tiền theo hồ sơ đổi trả nào (nếu do đổi trả); hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo.
-- Số dòng trên dữ liệu minh họa: 1
SELECT kc.MaHoan, hd.MaHS, dh.MaDH, mg.MaMG, nv.MaNV
FROM KHOANHOAN kc
JOIN HOSODOITRA hd ON kc.MaHS = hd.MaHS
JOIN DONHANG dh ON hd.MaDH = dh.MaDH
JOIN MAGIAMGIA mg ON dh.MaMG = mg.MaMG
JOIN NHANVIEN nv ON mg.MaNV = nv.MaNV;

-- Đường 43: PHIEUBAOHANH → NHANVIEN
-- Cho biết phiếu bảo hành do nhân viên nào tiếp nhận.
-- Số dòng trên dữ liệu minh họa: 2
SELECT bh.MaPhieuBH, nv.MaNV
FROM PHIEUBAOHANH bh
JOIN NHANVIEN nv ON bh.MaNV = nv.MaNV;

-- Đường 44: PHIEUBAOHANH → CHITIETDONHANG → MATHANG → LOAIHANG
-- Cho biết phiếu bảo hành mua ở dòng đơn nào; dòng đơn đó bán mặt hàng nào; mặt hàng đó thuộc loại hàng nào.
-- Số dòng trên dữ liệu minh họa: 2
SELECT bh.MaPhieuBH, ct.MaDH, ct.SoDongDH, mh.MaSP, lh.MaLoai
FROM PHIEUBAOHANH bh
JOIN CHITIETDONHANG ct ON bh.MaDH = ct.MaDH AND bh.SoDongDH = ct.SoDongDH
JOIN MATHANG mh ON ct.MaSP = mh.MaSP
JOIN LOAIHANG lh ON mh.MaLoai = lh.MaLoai;

-- Đường 45: PHIEUBAOHANH → CHITIETDONHANG → MATHANG → THUONGHIEU
-- Cho biết phiếu bảo hành mua ở dòng đơn nào; dòng đơn đó bán mặt hàng nào; mặt hàng đó mang thương hiệu nào.
-- Số dòng trên dữ liệu minh họa: 2
SELECT bh.MaPhieuBH, ct.MaDH, ct.SoDongDH, mh.MaSP, th.MaTH
FROM PHIEUBAOHANH bh
JOIN CHITIETDONHANG ct ON bh.MaDH = ct.MaDH AND bh.SoDongDH = ct.SoDongDH
JOIN MATHANG mh ON ct.MaSP = mh.MaSP
JOIN THUONGHIEU th ON mh.MaTH = th.MaTH;

-- Đường 46: PHIEUBAOHANH → CHITIETDONHANG → DONHANG → KHACHHANG
-- Cho biết phiếu bảo hành mua ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách).
-- Số dòng trên dữ liệu minh họa: 1
SELECT bh.MaPhieuBH, ct.MaDH, ct.SoDongDH, kh.MaKH
FROM PHIEUBAOHANH bh
JOIN CHITIETDONHANG ct ON bh.MaDH = ct.MaDH AND bh.SoDongDH = ct.SoDongDH
JOIN DONHANG dh ON ct.MaDH = dh.MaDH
JOIN KHACHHANG kh ON dh.MaKH = kh.MaKH;

-- Đường 47: PHIEUBAOHANH → CHITIETDONHANG → DONHANG → NHANVIEN
-- Cho biết phiếu bảo hành mua ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó do nhân viên nào lập.
-- Số dòng trên dữ liệu minh họa: 2
SELECT bh.MaPhieuBH, ct.MaDH, ct.SoDongDH, nv.MaNV
FROM PHIEUBAOHANH bh
JOIN CHITIETDONHANG ct ON bh.MaDH = ct.MaDH AND bh.SoDongDH = ct.SoDongDH
JOIN DONHANG dh ON ct.MaDH = dh.MaDH
JOIN NHANVIEN nv ON dh.MaNV = nv.MaNV;

-- Đường 48: PHIEUBAOHANH → CHITIETDONHANG → DONHANG → MAGIAMGIA → NHANVIEN
-- Cho biết phiếu bảo hành mua ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo.
-- Số dòng trên dữ liệu minh họa: 1
SELECT bh.MaPhieuBH, ct.MaDH, ct.SoDongDH, mg.MaMG, nv.MaNV
FROM PHIEUBAOHANH bh
JOIN CHITIETDONHANG ct ON bh.MaDH = ct.MaDH AND bh.SoDongDH = ct.SoDongDH
JOIN DONHANG dh ON ct.MaDH = dh.MaDH
JOIN MAGIAMGIA mg ON dh.MaMG = mg.MaMG
JOIN NHANVIEN nv ON mg.MaNV = nv.MaNV;

-- Đường 49: PHIEUBAOHANH → HANGCOSERI → CHITIETDONHANG → MATHANG → LOAIHANG
-- Cho biết phiếu bảo hành ứng với chiếc hàng có seri nào; chiếc hàng có seri đó đã bán ở dòng đơn nào; dòng đơn đó bán mặt hàng nào; mặt hàng đó thuộc loại hàng nào.
-- Số dòng trên dữ liệu minh họa: 1
SELECT bh.MaPhieuBH, hs.MaSeri, ct.MaDH, ct.SoDongDH, mh.MaSP, lh.MaLoai
FROM PHIEUBAOHANH bh
JOIN HANGCOSERI hs ON bh.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETDONHANG ct ON hs.MaDH = ct.MaDH AND hs.SoDongDH = ct.SoDongDH
JOIN MATHANG mh ON ct.MaSP = mh.MaSP
JOIN LOAIHANG lh ON mh.MaLoai = lh.MaLoai;

-- Đường 50: PHIEUBAOHANH → HANGCOSERI → CHITIETDONHANG → MATHANG → THUONGHIEU
-- Cho biết phiếu bảo hành ứng với chiếc hàng có seri nào; chiếc hàng có seri đó đã bán ở dòng đơn nào; dòng đơn đó bán mặt hàng nào; mặt hàng đó mang thương hiệu nào.
-- Số dòng trên dữ liệu minh họa: 1
SELECT bh.MaPhieuBH, hs.MaSeri, ct.MaDH, ct.SoDongDH, mh.MaSP, th.MaTH
FROM PHIEUBAOHANH bh
JOIN HANGCOSERI hs ON bh.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETDONHANG ct ON hs.MaDH = ct.MaDH AND hs.SoDongDH = ct.SoDongDH
JOIN MATHANG mh ON ct.MaSP = mh.MaSP
JOIN THUONGHIEU th ON mh.MaTH = th.MaTH;

-- Đường 51: PHIEUBAOHANH → HANGCOSERI → CHITIETDONHANG → DONHANG → KHACHHANG
-- Cho biết phiếu bảo hành ứng với chiếc hàng có seri nào; chiếc hàng có seri đó đã bán ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách).
-- Số dòng trên dữ liệu minh họa: 1
SELECT bh.MaPhieuBH, hs.MaSeri, ct.MaDH, ct.SoDongDH, kh.MaKH
FROM PHIEUBAOHANH bh
JOIN HANGCOSERI hs ON bh.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETDONHANG ct ON hs.MaDH = ct.MaDH AND hs.SoDongDH = ct.SoDongDH
JOIN DONHANG dh ON ct.MaDH = dh.MaDH
JOIN KHACHHANG kh ON dh.MaKH = kh.MaKH;

-- Đường 52: PHIEUBAOHANH → HANGCOSERI → CHITIETDONHANG → DONHANG → NHANVIEN
-- Cho biết phiếu bảo hành ứng với chiếc hàng có seri nào; chiếc hàng có seri đó đã bán ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó do nhân viên nào lập.
-- Số dòng trên dữ liệu minh họa: 1
SELECT bh.MaPhieuBH, hs.MaSeri, ct.MaDH, ct.SoDongDH, nv.MaNV
FROM PHIEUBAOHANH bh
JOIN HANGCOSERI hs ON bh.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETDONHANG ct ON hs.MaDH = ct.MaDH AND hs.SoDongDH = ct.SoDongDH
JOIN DONHANG dh ON ct.MaDH = dh.MaDH
JOIN NHANVIEN nv ON dh.MaNV = nv.MaNV;

-- Đường 53: PHIEUBAOHANH → HANGCOSERI → CHITIETDONHANG → DONHANG → MAGIAMGIA → NHANVIEN
-- Cho biết phiếu bảo hành ứng với chiếc hàng có seri nào; chiếc hàng có seri đó đã bán ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo.
-- Số dòng trên dữ liệu minh họa: 1
SELECT bh.MaPhieuBH, hs.MaSeri, ct.MaDH, ct.SoDongDH, mg.MaMG, nv.MaNV
FROM PHIEUBAOHANH bh
JOIN HANGCOSERI hs ON bh.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETDONHANG ct ON hs.MaDH = ct.MaDH AND hs.SoDongDH = ct.SoDongDH
JOIN DONHANG dh ON ct.MaDH = dh.MaDH
JOIN MAGIAMGIA mg ON dh.MaMG = mg.MaMG
JOIN NHANVIEN nv ON mg.MaNV = nv.MaNV;

-- Đường 54: PHIEUBAOHANH → HANGCOSERI → CHITIETPHIEUNHAP → MATHANG → LOAIHANG
-- Cho biết phiếu bảo hành ứng với chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó nhập mặt hàng nào; mặt hàng đó thuộc loại hàng nào.
-- Số dòng trên dữ liệu minh họa: 1
SELECT bh.MaPhieuBH, hs.MaSeri, cp.MaPN, cp.SoDongPN, mh.MaSP, lh.MaLoai
FROM PHIEUBAOHANH bh
JOIN HANGCOSERI hs ON bh.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETPHIEUNHAP cp ON hs.MaPN = cp.MaPN AND hs.SoDongPN = cp.SoDongPN
JOIN MATHANG mh ON cp.MaSP = mh.MaSP
JOIN LOAIHANG lh ON mh.MaLoai = lh.MaLoai;

-- Đường 55: PHIEUBAOHANH → HANGCOSERI → CHITIETPHIEUNHAP → MATHANG → THUONGHIEU
-- Cho biết phiếu bảo hành ứng với chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó nhập mặt hàng nào; mặt hàng đó mang thương hiệu nào.
-- Số dòng trên dữ liệu minh họa: 1
SELECT bh.MaPhieuBH, hs.MaSeri, cp.MaPN, cp.SoDongPN, mh.MaSP, th.MaTH
FROM PHIEUBAOHANH bh
JOIN HANGCOSERI hs ON bh.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETPHIEUNHAP cp ON hs.MaPN = cp.MaPN AND hs.SoDongPN = cp.SoDongPN
JOIN MATHANG mh ON cp.MaSP = mh.MaSP
JOIN THUONGHIEU th ON mh.MaTH = th.MaTH;

-- Đường 56: PHIEUBAOHANH → HANGCOSERI → CHITIETPHIEUNHAP → PHIEUNHAP → NHANVIEN
-- Cho biết phiếu bảo hành ứng với chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó thuộc phiếu nhập nào; phiếu nhập đó do nhân viên kho nào lập.
-- Số dòng trên dữ liệu minh họa: 1
SELECT bh.MaPhieuBH, hs.MaSeri, cp.MaPN, cp.SoDongPN, nv.MaNV
FROM PHIEUBAOHANH bh
JOIN HANGCOSERI hs ON bh.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETPHIEUNHAP cp ON hs.MaPN = cp.MaPN AND hs.SoDongPN = cp.SoDongPN
JOIN PHIEUNHAP pn ON cp.MaPN = pn.MaPN
JOIN NHANVIEN nv ON pn.MaNV = nv.MaNV;

-- Đường 57: PHIEUBAOHANH → HANGCOSERI → CHITIETPHIEUNHAP → PHIEUNHAP → NHACUNGCAP
-- Cho biết phiếu bảo hành ứng với chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó thuộc phiếu nhập nào; phiếu nhập đó nhận từ nhà cung cấp nào.
-- Số dòng trên dữ liệu minh họa: 1
SELECT bh.MaPhieuBH, hs.MaSeri, cp.MaPN, cp.SoDongPN, nc.MaNCC
FROM PHIEUBAOHANH bh
JOIN HANGCOSERI hs ON bh.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETPHIEUNHAP cp ON hs.MaPN = cp.MaPN AND hs.SoDongPN = cp.SoDongPN
JOIN PHIEUNHAP pn ON cp.MaPN = pn.MaPN
JOIN NHACUNGCAP nc ON pn.MaNCC = nc.MaNCC;

