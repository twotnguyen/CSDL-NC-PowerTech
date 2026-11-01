-- Các truy vấn khai thác theo con đường truy xuất (chương 3, mục 3.3.3). Đã chạy thử trên dữ liệu minh họa.

-- K1: Lịch sử mua hàng của một khách theo số điện thoại
-- Con đường: KHACHHANG ⇒ DONHANG ⇒ CHITIETDONHANG
-- Số dòng trên dữ liệu minh họa: 3
SELECT dh.SoDH, dh.ThoiDiemLap, ct.SoDongDH, ct.TenHangChot, ct.SoLuongBan, ct.DonGiaChot,
       ct.SoLuongBan * ct.DonGiaChot AS ThanhTien
FROM KHACHHANG kh
JOIN DONHANG dh ON dh.MaKH = kh.MaKH
JOIN CHITIETDONHANG ct ON ct.MaDH = dh.MaDH
WHERE kh.SDTKH = '0900000001'
ORDER BY dh.ThoiDiemLap, ct.SoDongDH;

-- K2: Doanh thu tiền hàng theo loại hàng trong tháng 10/2026 (không tính đơn đã hủy, chưa trừ giảm giá và hoàn tiền)
-- Con đường: CHITIETDONHANG → DONHANG; CHITIETDONHANG → MATHANG → LOAIHANG
-- Số dòng trên dữ liệu minh họa: 3
SELECT lh.MaLoai, lh.TenLoai, SUM(ct.SoLuongBan * ct.DonGiaChot) AS DoanhThuTienHang
FROM CHITIETDONHANG ct
JOIN DONHANG dh ON dh.MaDH = ct.MaDH
JOIN MATHANG mh ON mh.MaSP = ct.MaSP
JOIN LOAIHANG lh ON lh.MaLoai = mh.MaLoai
WHERE dh.TinhTrangDH <> 'Đã hủy'
  AND dh.ThoiDiemLap >= '2026-10-01' AND dh.ThoiDiemLap < '2026-11-01'
GROUP BY lh.MaLoai, lh.TenLoai
ORDER BY DoanhThuTienHang DESC;

-- K3: Số lượng hàng trong kho theo mặt hàng và nhóm kho, tính từ giao dịch kho
-- Con đường: GIAODICHKHO → MATHANG
-- Số dòng trên dữ liệu minh họa: 4
SELECT mh.MaSP, mh.TenSP, gd.NhomKho,
       SUM(CASE WHEN gd.LoaiBienDong IN ('Nhập', 'Nhận lại', 'Chuyển vào') THEN gd.SoLuongGD
                ELSE -gd.SoLuongGD END) AS SoLuong
FROM GIAODICHKHO gd
JOIN MATHANG mh ON mh.MaSP = gd.MaSP
GROUP BY mh.MaSP, mh.TenSP, gd.NhomKho
ORDER BY mh.MaSP, gd.NhomKho;

-- K4: Truy vết một chiếc hàng theo số seri: nhập từ đâu, lần bán gần nhất cho ai
-- Con đường: SERIMATHANG ⇒ HANGCOSERI → CHITIETPHIEUNHAP → PHIEUNHAP → NHACUNGCAP; HANGCOSERI → CHITIETDONHANG → DONHANG → KHACHHANG
-- Số dòng trên dữ liệu minh họa: 1
SELECT sm.SoSeri, mh.TenSP, pn.SoPhieu, nc.TenNCC, dh.SoDH, kh.HoLotKH, kh.TenKH
FROM SERIMATHANG sm
JOIN MATHANG mh ON mh.MaSP = sm.MaSP
JOIN HANGCOSERI hs ON hs.MaSeri = sm.MaSeri
JOIN CHITIETPHIEUNHAP cp ON cp.MaPN = hs.MaPN AND cp.SoDongPN = hs.SoDongPN
JOIN PHIEUNHAP pn ON pn.MaPN = cp.MaPN
JOIN NHACUNGCAP nc ON nc.MaNCC = pn.MaNCC
LEFT JOIN CHITIETDONHANG ct ON ct.MaDH = hs.MaDH AND ct.SoDongDH = hs.SoDongDH
LEFT JOIN DONHANG dh ON dh.MaDH = ct.MaDH
LEFT JOIN KHACHHANG kh ON kh.MaKH = dh.MaKH
WHERE sm.MaSP = 2 AND sm.SoSeri = 'S1T-0001';

-- K5: Các dòng trả của từng hồ sơ đổi trả trong một đơn, kèm tổng tiền đã chi hoàn của hồ sơ
-- Con đường: HOSODOITRA ⇒ CHITIETTRA; HOSODOITRA ⇒ KHOANHOAN
-- Số dòng trên dữ liệu minh họa: 1
SELECT hd.MaHS, hd.LoaiTruongHop, ct.SoDongTra, ct.SoDongDH, ct.SoLuongTra, h.TongHoan
FROM HOSODOITRA hd
JOIN CHITIETTRA ct ON ct.MaHS = hd.MaHS
LEFT JOIN (SELECT MaHS, SUM(SoTienHoan) AS TongHoan
           FROM KHOANHOAN
           WHERE MaHS IS NOT NULL AND ThoiDiemChi IS NOT NULL
           GROUP BY MaHS) h ON h.MaHS = hd.MaHS
WHERE hd.MaDH = 2
ORDER BY hd.MaHS, ct.SoDongTra;

-- K6: Ai đã lập đơn, xác nhận tiền, thu tiền khi giao và giao một đơn hàng, và người đó có chức vụ gì (truy trách nhiệm)
-- Con đường: DONHANG → NHANVIEN (lập); DONHANG ⇐ THANHTOAN → NHANVIEN (xác nhận tiền, cột MaNV; thu khi giao, cột MaNVThu); DONHANG ⇐ PHIEUGIAO → NHANVIEN (giao)
-- Số dòng trên dữ liệu minh họa: 1
SELECT dh.SoDH, nl.HoLotNV AS HoLotNguoiLap, nl.TenNV AS TenNguoiLap, nl.ChucVu AS ChucVuNguoiLap,
       tt.MaTT, tt.PhuongThuc, nx.HoLotNV AS HoLotNguoiXacNhan, nx.TenNV AS TenNguoiXacNhan, nx.ChucVu AS ChucVuNguoiXacNhan,
       nt.HoLotNV AS HoLotNguoiThu, nt.TenNV AS TenNguoiThu, nt.ChucVu AS ChucVuNguoiThu,
       pg.MaGiao, ng.HoLotNV AS HoLotNguoiGiao, ng.TenNV AS TenNguoiGiao, ng.ChucVu AS ChucVuNguoiGiao
FROM DONHANG dh
LEFT JOIN NHANVIEN nl ON nl.MaNV = dh.MaNV
LEFT JOIN THANHTOAN tt ON tt.MaDH = dh.MaDH
LEFT JOIN NHANVIEN nx ON nx.MaNV = tt.MaNV
LEFT JOIN NHANVIEN nt ON nt.MaNV = tt.MaNVThu
LEFT JOIN PHIEUGIAO pg ON pg.MaDH = dh.MaDH
LEFT JOIN NHANVIEN ng ON ng.MaNV = pg.MaNV
WHERE dh.SoDH = 'DH-0002';

-- K7: Các khoản hoàn tiền trong tháng 10/2026: ai duyệt, ai chi tiền
-- Con đường: KHOANHOAN → NHANVIEN (người duyệt, cột MaNV); KHOANHOAN → NHANVIEN (người chi, cột MaNVChi)
-- Số dòng trên dữ liệu minh họa: 2
SELECT kc.MaHoan, kc.SoTienHoan, kc.ThoiDiemDuyetHoan, nd.HoLotNV AS HoLotNguoiDuyet, nd.TenNV AS TenNguoiDuyet,
       kc.ThoiDiemChi, nc.HoLotNV AS HoLotNguoiChi, nc.TenNV AS TenNguoiChi
FROM KHOANHOAN kc
JOIN NHANVIEN nd ON nd.MaNV = kc.MaNV
LEFT JOIN NHANVIEN nc ON nc.MaNV = kc.MaNVChi
WHERE kc.ThoiDiemDuyetHoan >= '2026-10-01' AND kc.ThoiDiemDuyetHoan < '2026-11-01'
ORDER BY kc.ThoiDiemDuyetHoan;

-- K8: Danh sách nhân viên còn làm việc theo chức vụ
-- Con đường: NHANVIEN (tra theo thuộc tính ChucVu, không nối quan hệ khác)
-- Số dòng trên dữ liệu minh họa: 7
SELECT nv.ChucVu, nv.MaNV, nv.HoLotNV, nv.TenNV, nv.NgayVaoLam
FROM NHANVIEN nv
WHERE nv.TinhTrangNV = 'Đang làm'
ORDER BY nv.ChucVu, nv.MaNV;

-- K9: Phiếu bảo hành đã quá ngày hẹn trả mà chưa trả khách, kèm khách cần liên hệ
-- Con đường: PHIEUBAOHANH → CHITIETDONHANG → DONHANG → KHACHHANG
-- Số dòng trên dữ liệu minh họa: 1
WITH ThamSo AS (SELECT '2026-11-01' AS NgayTraCuu)
SELECT bh.MaPhieuBH, bh.NgayNhan, bh.NgayHenTra, bh.TinhTrangBH, ct.TenHangChot, dh.SoDH, kh.HoLotKH, kh.TenKH, kh.SDTKH
FROM PHIEUBAOHANH bh
CROSS JOIN ThamSo ts
JOIN CHITIETDONHANG ct ON ct.MaDH = bh.MaDH AND ct.SoDongDH = bh.SoDongDH
JOIN DONHANG dh ON dh.MaDH = ct.MaDH
LEFT JOIN KHACHHANG kh ON kh.MaKH = dh.MaKH
WHERE bh.NgayTraThucTe IS NULL AND bh.NgayHenTra < ts.NgayTraCuu
ORDER BY bh.NgayHenTra;

