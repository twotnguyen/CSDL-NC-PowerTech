-- Mục 10. Truy vấn khai thác theo con đường truy xuất và chỉ mục đề xuất (T-SQL).
-- Dựa trên lược đồ 39 quan hệ của mục 9. Chỉ minh họa, chưa áp dụng vào CSDL nào.
-- Tên bảng/cột đã được kiểm tra bằng SQLite rỗng dựng từ lược đồ; chưa chạy trên SQL Server.

-- K1. Lịch sử mua hàng của một khách (theo số điện thoại)
SELECT dh.SoDH, dh.ThoiDiemLap, dh.TinhTrang,
       d.SoDong, d.TenHangChot, d.SoLuong, d.DonGiaChot
FROM KHACHHANG kh
JOIN DONHANG dh        ON dh.MaKH = kh.MaKH
JOIN CHITIETDONHANG d  ON d.MaDH  = dh.MaDH
WHERE kh.SDT = @SDT
ORDER BY dh.ThoiDiemLap DESC, d.SoDong;

-- K2. Doanh thu hàng theo loại hàng trong một kỳ
SELECT l.TenLoai,
       SUM(d.SoLuong * d.DonGiaChot) AS DoanhThuHang,
       COUNT(DISTINCT dh.MaDH)       AS SoDon
FROM CHITIETDONHANG d
JOIN DONHANG dh ON dh.MaDH  = d.MaDH
JOIN MATHANG m  ON m.MaSP   = d.MaSP
JOIN LOAIHANG l ON l.MaLoai = m.MaLoai
WHERE dh.TinhTrang = N'hoàn tất'
  AND dh.ThoiDiemLap >= @TuNgay AND dh.ThoiDiemLap < @DenNgay
GROUP BY l.TenLoai
ORDER BY DoanhThuHang DESC;

-- K3. Sổ kho của một mặt hàng, gộp theo nhóm kho và loại biến động
SELECT g.NhomKho, g.LoaiBienDong,
       COUNT(*)        AS SoGiaoDich,
       SUM(g.SoLuong)  AS TongSoLuong
FROM MATHANG m
JOIN GIAODICHKHO g ON g.MaSP = m.MaSP
WHERE m.SKU = @SKU
GROUP BY g.NhomKho, g.LoaiBienDong
ORDER BY g.NhomKho, g.LoaiBienDong;

-- K4. Công việc của từng người giao hàng
SELECT nv.MaNV, nv.HoTen,
       COUNT(DISTINCT pg.MaGiao) AS SoPhieuGiao,
       SUM(CASE WHEN l.KetQua = N'thất bại' THEN 1 ELSE 0 END) AS SoLanGiaoThatBai
FROM NHANVIEN nv
JOIN PHIEUGIAO pg ON pg.MaNVGiao = nv.MaNV
LEFT JOIN LANGIAO l ON l.MaGiao = pg.MaGiao
WHERE pg.ThoiDiemXuat >= @TuNgay AND pg.ThoiDiemXuat < @DenNgay
GROUP BY nv.MaNV, nv.HoTen
ORDER BY SoPhieuGiao DESC;

-- K5. Truy vết một chiếc hàng theo số seri: nhập từ đâu, bán cho ai
SELECT s.SoSeri, m.SKU, m.TenSP, h.TinhTrang,
       pn.SoPhieu, pn.ThoiDiemNhan, ncc.TenNCC,
       dh.SoDH, dh.ThoiDiemLap, kh.MaKH
FROM SERIMATHANG s
JOIN HANGCOSERI h        ON h.MaSeri  = s.MaSeri
JOIN CHITIETPHIEUNHAP cn ON cn.MaPN   = h.MaPN AND cn.SoDong = h.SoDongNhap
JOIN PHIEUNHAP pn        ON pn.MaPN   = cn.MaPN
JOIN NHACUNGCAP ncc      ON ncc.MaNCC = pn.MaNCC
JOIN MATHANG m           ON m.MaSP    = cn.MaSP
LEFT JOIN CHITIETDONHANG cd ON cd.MaDH = h.MaDH AND cd.SoDong = h.SoDongDon
LEFT JOIN DONHANG dh        ON dh.MaDH = cd.MaDH
LEFT JOIN KHACHHANG kh      ON kh.MaKH = dh.MaKH
WHERE s.SoSeri = @SoSeri;

-- K6. Dòng hàng trả và tiền hoàn của các hồ sơ đổi trả thuộc một đơn
SELECT h.MaHS, h.NgayDeNghi, ct.SoDong, cd.TenHangChot,
       ct.SoLuongTra, cd.DonGiaChot,
       (SELECT SUM(k.SoTien) FROM KHOANHOAN k WHERE k.MaHS = h.MaHS) AS TongHoan
FROM DONHANG dh
JOIN HOSODOITRA h       ON h.MaDH  = dh.MaDH
JOIN CHITIETTRA ct      ON ct.MaHS = h.MaHS
JOIN CHITIETDONHANG cd  ON cd.MaDH = h.MaDH AND cd.SoDong = ct.SoDong
WHERE dh.SoDH = @SoDH
ORDER BY h.MaHS, ct.SoDong;

-- K7. Lọc mặt hàng theo giá trị một thông số của loại hàng
SELECT m.SKU, m.TenSP, gt.GiaTri
FROM LOAIHANG l
JOIN DINHNGHIATHONGSO ts ON ts.MaLoai = l.MaLoai
JOIN GIATRITHONGSO gt    ON gt.MaTS    = ts.MaTS
JOIN MATHANG m           ON m.MaSP     = gt.MaSP
WHERE l.TenLoai = @TenLoai AND ts.TenTS = @TenTS
  AND m.TinhTrangKinhDoanh = 1
ORDER BY m.TenSP;

-- Chỉ mục đề xuất (mỗi chỉ mục ứng với một cung "->>" hoặc một nút vào)
CREATE INDEX IX_KHACHHANG_SDT ON KHACHHANG (SDT);  -- K1: ngõ vào theo số điện thoại (không duy nhất)
CREATE INDEX IX_DONHANG_MaKH ON DONHANG (MaKH);  -- K1: cung ngược KHACHHANG ->> DONHANG
CREATE INDEX IX_DONHANG_ThoiDiemLap ON DONHANG (ThoiDiemLap, TinhTrang);  -- K2: chọn đơn theo kỳ và tình trạng
CREATE INDEX IX_CHITIETDONHANG_MaSP ON CHITIETDONHANG (MaSP);  -- K2: cung ngược MATHANG ->> CHITIETDONHANG
CREATE INDEX IX_GIAODICHKHO_MaSP ON GIAODICHKHO (MaSP, ThoiDiem);  -- K3: cung ngược MATHANG ->> GIAODICHKHO
CREATE UNIQUE INDEX UX_MATHANG_SKU ON MATHANG (SKU);  -- K3: ngõ vào theo SKU (khóa thay thế, duy nhất)
CREATE INDEX IX_PHIEUGIAO_MaNVGiao ON PHIEUGIAO (MaNVGiao, ThoiDiemXuat);  -- K4: cung ngược NHANVIEN ->> PHIEUGIAO
CREATE INDEX IX_SERIMATHANG_SoSeri ON SERIMATHANG (SoSeri);  -- K5: ngõ vào theo số seri (không duy nhất toàn cửa hàng)
CREATE INDEX IX_HANGCOSERI_DonHang ON HANGCOSERI (MaDH, SoDongDon);  -- K5: cung ngược CHITIETDONHANG ->> HANGCOSERI
CREATE INDEX IX_PHIEUBAOHANH_MaSeri ON PHIEUBAOHANH (MaSeri);  -- K5: cung ngược HANGCOSERI ->> PHIEUBAOHANH
CREATE INDEX IX_HOSODOITRA_MaDH ON HOSODOITRA (MaDH);  -- K6: cung ngược DONHANG ->> HOSODOITRA
CREATE INDEX IX_KHOANHOAN_MaHS ON KHOANHOAN (MaHS);  -- K6: cung ngược HOSODOITRA ->> KHOANHOAN
CREATE INDEX IX_GIATRITHONGSO_MaTS ON GIATRITHONGSO (MaTS);  -- K7: cung ngược DINHNGHIATHONGSO ->> GIATRITHONGSO (khóa chính bắt đầu bằng MaSP)
