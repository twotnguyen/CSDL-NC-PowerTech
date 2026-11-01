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
SELECT lh.TenLoai, SUM(ct.SoLuongBan * ct.DonGiaChot) AS DoanhThuTienHang
FROM CHITIETDONHANG ct
JOIN DONHANG dh ON dh.MaDH = ct.MaDH
JOIN MATHANG mh ON mh.MaSP = ct.MaSP
JOIN LOAIHANG lh ON lh.MaLoai = mh.MaLoai
WHERE dh.TinhTrangDH <> 'Đã hủy'
  AND dh.ThoiDiemLap >= '2026-10-01' AND dh.ThoiDiemLap < '2026-11-01'
GROUP BY lh.TenLoai
ORDER BY DoanhThuTienHang DESC;

-- K3: Số lượng hàng trong kho theo mặt hàng và nhóm kho, tính từ giao dịch kho
-- Con đường: GIAODICHKHO → MATHANG
-- Số dòng trên dữ liệu minh họa: 3
SELECT mh.TenSP, gd.NhomKho,
       SUM(CASE WHEN gd.LoaiBienDong IN ('Nhập', 'Nhận lại') THEN gd.SoLuongGD
                WHEN gd.LoaiBienDong = 'Xuất bán' THEN -gd.SoLuongGD
                ELSE 0 END) AS SoLuong
FROM GIAODICHKHO gd
JOIN MATHANG mh ON mh.MaSP = gd.MaSP
GROUP BY mh.TenSP, gd.NhomKho
ORDER BY mh.TenSP, gd.NhomKho;

-- K4: Truy vết một chiếc hàng theo số seri: nhập từ đâu, bán cho ai
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

-- K5: Hồ sơ đổi trả của một đơn kèm số tiền đã hoàn
-- Con đường: HOSODOITRA ⇒ CHITIETTRA; HOSODOITRA ⇒ KHOANHOAN → THANHTOAN
-- Số dòng trên dữ liệu minh họa: 1
SELECT hd.MaHS, hd.LoaiTruongHop, ct.SoDongDH, ct.SoLuongTra, kc.SoTienHoan, tt.SoTien AS SoTienDaThu
FROM HOSODOITRA hd
JOIN CHITIETTRA ct ON ct.MaHS = hd.MaHS
LEFT JOIN KHOANHOAN kc ON kc.MaHS = hd.MaHS
LEFT JOIN THANHTOAN tt ON tt.MaTT = kc.MaTT
WHERE hd.MaDH = 2;

-- K6: Ai đã xử lý từng bước của một đơn hàng, và lúc đó giữ vai trò gì (truy trách nhiệm)
-- Con đường: DONHANG ⇒ NHATKYDONHANG → NHANVIEN; NHANVIEN ⇒ GIUVAITRO → VAITRO
-- Số dòng trên dữ liệu minh họa: 6
SELECT dh.SoDH, nk.SoLanDoi, nk.TinhTrangMoi, nk.ThoiDiemDoi, nv.HoLotNV, nv.TenNV, vt.TenVT, nk.LyDoDoi
FROM DONHANG dh
JOIN NHATKYDONHANG nk ON nk.MaDH = dh.MaDH
LEFT JOIN NHANVIEN nv ON nv.MaNV = nk.MaNV
LEFT JOIN GIUVAITRO gv ON gv.MaNV = nv.MaNV AND nk.ThoiDiemDoi >= gv.NgayBatDauVT
                      AND (gv.NgayKetThucVT IS NULL OR nk.ThoiDiemDoi < gv.NgayKetThucVT)
LEFT JOIN VAITRO vt ON vt.MaVT = gv.MaVT
WHERE dh.SoDH = 'DH-0002'
ORDER BY nk.SoLanDoi, vt.TenVT;

-- K7: Các khoản hoàn tiền trong tháng 10/2026: ai duyệt, ai chi tiền
-- Con đường: KHOANHOAN → NHANVIEN (người duyệt, cột MaNV); KHOANHOAN → NHANVIEN (người chi, cột MaNVChi)
-- Số dòng trên dữ liệu minh họa: 1
SELECT kc.MaHoan, kc.SoTienHoan, kc.ThoiDiemDuyetHoan, nd.HoLotNV AS HoLotNguoiDuyet, nd.TenNV AS TenNguoiDuyet,
       kc.ThoiDiemChi, nc.HoLotNV AS HoLotNguoiChi, nc.TenNV AS TenNguoiChi
FROM KHOANHOAN kc
JOIN NHANVIEN nd ON nd.MaNV = kc.MaNV
LEFT JOIN NHANVIEN nc ON nc.MaNV = kc.MaNVChi
WHERE kc.ThoiDiemDuyetHoan >= '2026-10-01' AND kc.ThoiDiemDuyetHoan < '2026-11-01'
ORDER BY kc.ThoiDiemDuyetHoan;

-- K8: Vai trò đang giữ của các nhân viên còn làm việc
-- Con đường: NHANVIEN ⇐ GIUVAITRO → VAITRO
-- Số dòng trên dữ liệu minh họa: 8
SELECT nv.MaNV, nv.HoLotNV, nv.TenNV, vt.TenVT, gv.NgayBatDauVT
FROM NHANVIEN nv
JOIN GIUVAITRO gv ON gv.MaNV = nv.MaNV
JOIN VAITRO vt ON vt.MaVT = gv.MaVT
WHERE nv.TinhTrangNV = 'Đang làm' AND gv.NgayKetThucVT IS NULL
ORDER BY nv.MaNV, vt.TenVT;

-- K9: Giỏ hàng đang dùng của một khách kèm tiền tạm tính theo giá hiện hành
-- Con đường: KHACHHANG ⇒ TAIKHOAN ⇒ GIOHANG ⇒ CHITIETGIOHANG → MATHANG
-- Số dòng trên dữ liệu minh họa: 2
SELECT kh.HoLotKH, kh.TenKH, mh.TenSP, cg.SoLuongGio,
       COALESCE(mh.GiaKhuyenMai, mh.GiaNiemYet) AS DonGiaHienHanh,
       cg.SoLuongGio * COALESCE(mh.GiaKhuyenMai, mh.GiaNiemYet) AS TamTinh
FROM KHACHHANG kh
JOIN TAIKHOAN tk ON tk.MaKH = kh.MaKH
JOIN GIOHANG gh ON gh.MaTK = tk.MaTK
JOIN CHITIETGIOHANG cg ON cg.MaGio = gh.MaGio
JOIN MATHANG mh ON mh.MaSP = cg.MaSP
WHERE kh.SDTKH = '0900000001' AND gh.TinhTrangGio = 'Đang dùng';

