-- Dữ liệu minh họa nhỏ do nhóm tạo để kiểm tra các câu truy vấn của chương 3 (không phải dữ liệu thật của cửa hàng).
-- Mọi khóa ngoại đều thỏa; có đủ trường hợp rỗng và không rỗng để mỗi con đường truy xuất trả về ít nhất một dòng.

INSERT INTO LOAIHANG VALUES (1, 'Linh kiện máy tính', 'Nhóm lớn các linh kiện', NULL);
INSERT INTO LOAIHANG VALUES (2, 'Bộ nhớ RAM', NULL, 1);
INSERT INTO LOAIHANG VALUES (3, 'Ổ cứng SSD', NULL, 1);
INSERT INTO LOAIHANG VALUES (4, 'Chuột', 'Chuột có dây và không dây', NULL);

INSERT INTO THUONGHIEU VALUES (1, 'Kingston', NULL);
INSERT INTO THUONGHIEU VALUES (2, 'Samsung', NULL);
INSERT INTO THUONGHIEU VALUES (3, 'Logitech', NULL);

INSERT INTO MATHANG VALUES (1, 'RAM-KS-16G-3200', 'RAM Kingston Fury 16GB DDR4 3200', NULL, 1050000, 990000, 36, 'Đang kinh doanh', 0, 2, 1);
INSERT INTO MATHANG VALUES (2, 'SSD-SS-1T-980', 'SSD Samsung 980 1TB NVMe', NULL, 2490000, NULL, 60, 'Đang kinh doanh', 1, 3, 2);
INSERT INTO MATHANG VALUES (3, 'SSD-SS-500-980', 'SSD Samsung 980 500GB NVMe', NULL, 1390000, NULL, 60, 'Đang kinh doanh', 1, 3, 2);
INSERT INTO MATHANG VALUES (4, 'MOU-LG-G102', 'Chuột Logitech G102', NULL, 450000, 390000, 24, 'Đang kinh doanh', 0, 4, 3);

INSERT INTO ANHMATHANG VALUES (1, 1, 1, '/anh/ram-1.jpg', 1);
INSERT INTO ANHMATHANG VALUES (2, 1, 2, '/anh/ram-2.jpg', 0);
INSERT INTO ANHMATHANG VALUES (3, 2, 1, '/anh/ssd1t-1.jpg', 1);
INSERT INTO ANHMATHANG VALUES (4, 2, 2, '/anh/ssd1t-2.jpg', 0);
INSERT INTO ANHMATHANG VALUES (5, 4, 1, '/anh/chuot-1.jpg', 1);

INSERT INTO DINHNGHIATHONGSO VALUES (1, 2, 'Dung lượng', 'Số', 'GB', 1);
INSERT INTO DINHNGHIATHONGSO VALUES (2, 2, 'Tốc độ', 'Số', 'MHz', 1);
INSERT INTO DINHNGHIATHONGSO VALUES (3, 3, 'Dung lượng', 'Số', 'GB', 1);
INSERT INTO DINHNGHIATHONGSO VALUES (4, 3, 'Chuẩn kết nối', 'Chữ', NULL, 1);
INSERT INTO DINHNGHIATHONGSO VALUES (5, 4, 'Kiểu kết nối', 'Chữ', NULL, 0);

INSERT INTO GIATRITHONGSO VALUES (1, 1, '16');
INSERT INTO GIATRITHONGSO VALUES (1, 2, '3200');
INSERT INTO GIATRITHONGSO VALUES (2, 3, '1000');
INSERT INTO GIATRITHONGSO VALUES (2, 4, 'NVMe');
INSERT INTO GIATRITHONGSO VALUES (4, 5, 'Có dây');

INSERT INTO KHACHHANG VALUES (1, 'Nguyễn Văn', 'An', '0900000001', 'an@example.com', NULL);
INSERT INTO KHACHHANG VALUES (2, 'Trần Thị', 'Bình', '0900000002', NULL, NULL);
INSERT INTO KHACHHANG VALUES (3, 'Lê Hoàng', 'Cường', '0900000003', 'cuong@example.com', '0312345678');

INSERT INTO NHANVIEN VALUES (1, 'Phạm Minh', 'Tuấn', '0910000001', 'tuan@powertech.example', '2025-01-02', NULL, 'Đang làm', 'Bán hàng');
INSERT INTO NHANVIEN VALUES (2, 'Võ Thị', 'Lan', '0910000002', NULL, '2025-03-01', NULL, 'Đang làm', 'Kho');
INSERT INTO NHANVIEN VALUES (3, 'Đỗ Quốc', 'Huy', '0910000003', NULL, '2025-05-10', NULL, 'Đang làm', 'Giao hàng');
INSERT INTO NHANVIEN VALUES (4, 'Nguyễn Thanh', 'Quản', '0910000004', 'quan@powertech.example', '2024-06-01', NULL, 'Đang làm', 'Quản lý');
INSERT INTO NHANVIEN VALUES (5, 'Lê Thị', 'Quyên', '0910000005', 'quyen@powertech.example', '2024-01-01', NULL, 'Đang làm', 'Quản lý');
INSERT INTO NHANVIEN VALUES (6, 'Trần Văn', 'Kỹ', '0910000006', NULL, '2025-02-01', NULL, 'Đang làm', 'Kỹ thuật');
INSERT INTO NHANVIEN VALUES (7, 'Phan Thị', 'Chăm', '0910000007', NULL, '2025-04-01', NULL, 'Đang làm', 'Thu ngân');
INSERT INTO NHANVIEN VALUES (8, 'Hoàng Văn', 'Cũ', '0910000008', NULL, '2025-02-15', '2026-03-31', 'Đã nghỉ', 'Giao hàng');

INSERT INTO TAIKHOAN VALUES (1, 'khach.an', 'BAM-MAU-0001', 'Hoạt động', '2026-09-01 08:00:00', 1, NULL);
INSERT INTO TAIKHOAN VALUES (2, 'khach.binh', 'BAM-MAU-0002', 'Hoạt động', '2026-09-10 08:00:00', 2, NULL);
INSERT INTO TAIKHOAN VALUES (3, 'khach.cuong', 'BAM-MAU-0003', 'Bị khóa', '2026-09-12 08:00:00', 3, NULL);
INSERT INTO TAIKHOAN VALUES (4, 'nv.tuan', 'BAM-MAU-0004', 'Hoạt động', '2025-01-02 08:00:00', NULL, 1);
INSERT INTO TAIKHOAN VALUES (5, 'nv.quan', 'BAM-MAU-0005', 'Hoạt động', '2024-06-01 08:00:00', NULL, 4);
INSERT INTO TAIKHOAN VALUES (6, 'nv.quyen', 'BAM-MAU-0006', 'Hoạt động', '2024-01-01 08:00:00', NULL, 5);

INSERT INTO NHACUNGCAP VALUES (1, 'Công ty phân phối Alpha', 'Anh Hải', '0280000001', 'Quận 1', '0300000001', 'Đang hợp tác');
INSERT INTO NHACUNGCAP VALUES (2, 'Đại lý Beta', NULL, NULL, NULL, NULL, 'Đang hợp tác');

INSERT INTO MAGIAMGIA VALUES (1, 'KM10', 'Khuyến mãi tháng 10', 'Phần trăm', 10, 1000000, 200000, '2026-10-01', '2026-10-31', 100, 4);

INSERT INTO DONHANG VALUES (1, 'DH-0001', '2026-10-01 10:15:00', 'Quầy', NULL, 1, NULL, NULL, NULL, 0, 0, NULL, 'Hoàn tất', NULL, NULL);
INSERT INTO DONHANG VALUES (2, 'DH-0002', '2026-10-03 09:30:00', 'Điện thoại', 1, 1, 'Nguyễn Văn An', '0900000001', '12 Lê Lợi, Quận 1', 30000, 100000, 1, 'Hoàn tất', NULL, NULL);
INSERT INTO DONHANG VALUES (3, 'DH-0003', '2026-10-05 14:00:00', 'Điện thoại', 2, 1, 'Trần Thị Bình', '0900000002', '45 Nguyễn Huệ, Quận 1', 0, 0, NULL, 'Đã xác nhận', 'Đặt cọc 30% giá trị đơn', NULL);
INSERT INTO DONHANG VALUES (4, 'DH-0004', '2026-10-06 16:20:00', 'Trang web', 3, NULL, 'Lê Hoàng Cường', '0900000003', '8 Hai Bà Trưng, Quận 3', 20000, 0, NULL, 'Đã hủy', NULL, 'Giao thất bại 3 lần');
INSERT INTO DONHANG VALUES (5, 'DH-0005', '2026-10-22 08:00:00', 'Trang web', 1, NULL, 'Nguyễn Văn An', '0900000001', '12 Lê Lợi, Quận 1', 0, 0, NULL, 'Chờ xác nhận', NULL, NULL);

INSERT INTO CHITIETDONHANG VALUES (1, 1, 1, 2, 990000, 'RAM Kingston Fury 16GB DDR4 3200', 'RAM-KS-16G-3200', 36);
INSERT INTO CHITIETDONHANG VALUES (1, 2, 4, 1, 390000, 'Chuột Logitech G102', 'MOU-LG-G102', 24);
INSERT INTO CHITIETDONHANG VALUES (2, 1, 2, 2, 2490000, 'SSD Samsung 980 1TB NVMe', 'SSD-SS-1T-980', 60);
INSERT INTO CHITIETDONHANG VALUES (2, 2, 1, 1, 990000, 'RAM Kingston Fury 16GB DDR4 3200', 'RAM-KS-16G-3200', 36);
INSERT INTO CHITIETDONHANG VALUES (3, 1, 3, 1, 1390000, 'SSD Samsung 980 500GB NVMe', 'SSD-SS-500-980', 60);
INSERT INTO CHITIETDONHANG VALUES (4, 1, 4, 2, 450000, 'Chuột Logitech G102', 'MOU-LG-G102', 24);
INSERT INTO CHITIETDONHANG VALUES (5, 1, 4, 1, 390000, 'Chuột Logitech G102', 'MOU-LG-G102', 24);

INSERT INTO THANHTOAN VALUES (1, 1, 'Thanh toán', 'Tiền mặt', 2370000, '2026-10-01 10:20:00', 'Thành công', NULL, NULL, 1, NULL);
INSERT INTO THANHTOAN VALUES (2, 2, 'Thanh toán', 'Chuyển khoản', 5900000, '2026-10-03 09:45:00', 'Thành công', 'FT0001', 'Vietcombank', 4, NULL);
INSERT INTO THANHTOAN VALUES (3, 3, 'Đặt cọc', 'Chuyển khoản', 417000, '2026-10-05 14:30:00', 'Thành công', 'FT0002', 'Techcombank', 1, NULL);
INSERT INTO THANHTOAN VALUES (4, 4, 'Thanh toán', 'Thu khi giao', 900000, '2026-10-07 10:00:00', 'Thất bại', NULL, NULL, NULL, 3);

INSERT INTO PHIEUGIAO VALUES (1, 2, 3, '2026-10-03 13:00:00', 'Đã giao');
INSERT INTO PHIEUGIAO VALUES (2, 4, 3, '2026-10-07 09:00:00', 'Không thành công');

INSERT INTO LANGIAO VALUES (1, 1, '2026-10-03 15:00:00', 'Thành công', NULL, 3);
INSERT INTO LANGIAO VALUES (2, 1, '2026-10-07 10:00:00', 'Thất bại', 'Khách vắng nhà', 3);
INSERT INTO LANGIAO VALUES (2, 2, '2026-10-08 10:00:00', 'Thất bại', 'Khách từ chối nhận', 3);
INSERT INTO LANGIAO VALUES (2, 3, '2026-10-09 10:00:00', 'Thất bại', 'Không liên lạc được', 3);

INSERT INTO PHIEUNHAP VALUES (1, 'PN-0001', 1, 2, '2026-09-25 09:00:00', 'Đã xác nhận', 2, '2026-09-25 09:30:00', 'HD-A-100', NULL);
INSERT INTO PHIEUNHAP VALUES (2, 'PN-0002', 2, 2, '2026-09-28 09:00:00', 'Đã xác nhận', 2, '2026-09-28 09:20:00', NULL, NULL);

INSERT INTO CHITIETPHIEUNHAP VALUES (1, 1, 2, 3, 2000000);
INSERT INTO CHITIETPHIEUNHAP VALUES (1, 2, 3, 1, 1100000);
INSERT INTO CHITIETPHIEUNHAP VALUES (2, 1, 1, 10, 800000);
INSERT INTO CHITIETPHIEUNHAP VALUES (2, 2, 4, 5, 300000);

INSERT INTO SERIMATHANG VALUES (1, 'S1T-0001', 2);
INSERT INTO SERIMATHANG VALUES (2, 'S1T-0002', 2);
INSERT INTO SERIMATHANG VALUES (3, 'S1T-0003', 2);
INSERT INTO SERIMATHANG VALUES (4, 'S05-0001', 3);

INSERT INTO HANGCOSERI VALUES (1, 1, 1, 2, 1, 'Đã bán', '2026-09-25 09:30:00');
INSERT INTO HANGCOSERI VALUES (2, 1, 1, 2, 1, 'Đã bán', '2026-09-25 09:30:00');
INSERT INTO HANGCOSERI VALUES (3, 1, 1, NULL, NULL, 'Trong kho', '2026-09-25 09:30:00');
INSERT INTO HANGCOSERI VALUES (4, 1, 2, NULL, NULL, 'Trong kho', '2026-09-25 09:30:00');

INSERT INTO GIAODICHKHO VALUES (1, 2, 'Đủ điều kiện bán', 'Nhập', 3, '2026-09-25 09:30:00', 2, 'Phiếu nhập', 1, NULL);
INSERT INTO GIAODICHKHO VALUES (2, 3, 'Đủ điều kiện bán', 'Nhập', 1, '2026-09-25 09:30:00', 2, 'Phiếu nhập', 1, NULL);
INSERT INTO GIAODICHKHO VALUES (3, 2, 'Đủ điều kiện bán', 'Xuất bán', 2, '2026-10-03 09:50:00', 1, 'Đơn hàng', 2, NULL);
INSERT INTO GIAODICHKHO VALUES (4, 2, 'Chờ kiểm tra', 'Nhận lại', 1, '2026-10-09 10:00:00', 2, 'Hồ sơ đổi trả', 1, NULL);
INSERT INTO GIAODICHKHO VALUES (5, 2, 'Chờ kiểm tra', 'Chuyển ra', 1, '2026-10-09 15:00:00', 2, 'Hồ sơ đổi trả', 1, NULL);
INSERT INTO GIAODICHKHO VALUES (6, 2, 'Chờ xử lý', 'Chuyển vào', 1, '2026-10-09 15:00:00', 2, 'Hồ sơ đổi trả', 1, NULL);

INSERT INTO HOSODOITRA VALUES (1, 2, 7, '2026-10-08', 'Lỗi nhà sản xuất', 'SSD không nhận trong máy', 'Đã duyệt', 'Hoàn tiền');

INSERT INTO CHITIETTRA VALUES (1, 1, 1, 1, 1);

INSERT INTO LANNHANLAI VALUES (1, 1, '2026-10-09 10:00:00', 6, 'Hàng lỗi thật', 'Chờ xử lý', '2026-10-09 15:00:00', 4);

INSERT INTO PHIEUBAOHANH VALUES (1, 2, 2, 1, 'SSD nóng bất thường', 'Hộp và cáp', '2026-10-20', '2026-10-30', '2026-10-30', 'Đã trả khách', 'Thu hồi, trả lại tiền', NULL, 6);
INSERT INTO PHIEUBAOHANH VALUES (2, NULL, 1, 1, 'RAM báo lỗi khi khởi động', NULL, '2026-10-21', '2026-10-28', NULL, 'Đang kiểm tra', NULL, NULL, 6);

INSERT INTO KHOANHOAN VALUES (1, 2, 1, NULL, 4, 2490000, 'Chuyển khoản', '2026-10-09 16:00:00', '2026-10-10 09:00:00', 1);
INSERT INTO KHOANHOAN VALUES (2, 2, NULL, 1, 4, 2240000, 'Chuyển khoản', '2026-10-30 16:00:00', '2026-10-31 09:00:00', 1);
