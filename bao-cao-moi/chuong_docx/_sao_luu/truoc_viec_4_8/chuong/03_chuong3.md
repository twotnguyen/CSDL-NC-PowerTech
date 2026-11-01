# CHƯƠNG 3: KẾT QUẢ THỰC NGHIỆM

Chương này biểu diễn lược đồ sau cải tiến (26 quan hệ, mục 2.3.6) thành đồ thị quan hệ theo thuật toán B1–B7 của giáo trình, nêu các con đường truy xuất và ngữ nghĩa của từng con đường, rồi viết truy vấn SQL cho các con đường đó. Phép tính do `tools/dothi.py` đối chiếu; các truy vấn đều đã chạy thử trên dữ liệu minh họa nhỏ (`sql/02_du_lieu_minh_hoa.sql`, 26 bảng, không vi phạm khóa ngoại) và đều trả về ít nhất một dòng.

## 3.1 ĐỒ THỊ QUAN HỆ

**Quy ước áp dụng** (giáo trình cho phép nhiều đồ thị cho cùng một lược đồ; mục 10.4):

- **Q1.** Mỗi quan hệ dùng khóa chính làm khóa ưu tiên (giáo trình 10.4.2: khi cài đặt chọn một khóa ưu tiên).
- **Q2.** Hai cột là cùng một thuộc tính khi nối nhau bằng khóa ngoại, **trừ** khóa ngoại tới NHANVIEN không thuộc khóa chính: nhân viên lập đơn, xác nhận thu, giao hàng, nhập hàng… là các vai trò khác nhau của cùng một người nên mỗi cung vai trò được giữ riêng, không bị coi là thừa. Khóa ngoại **phụ** tới NHANVIEN có tên khác MaNV (MaNVThu, MaNVXacNhan, MaNVDuyet, MaNVChi) ghi thêm một vai trò nữa của nhân viên trên cùng quan hệ; chúng cùng đích với cung của MaNV (hoặc đã có cung tới NHANVIEN) nên không vẽ thành cung song song, và được truy xuất bằng cách nối thêm cột đó (ví dụ truy vấn K7).
- **Q3.** Cung A → B bị coi là thừa (PTH_Thừa) khi B đạt được qua cung A → H mà đường đó bắt buộc (không rỗng), hoặc khóa của B nằm trong khóa của H.
- **Q4.** Khuyên (cung từ một nút về chính nó) là liên kết loại hàng cha – con (MaLoaiCha); nằm ngoài thuật toán.

**Bước 1: Biến C thành phân rã đồng nhất C_d.** Hai quan hệ có khóa tương hỗ thì gộp thành một nút. HANGCOSERI và SERIMATHANG đều có khóa {MaSeri} nên gộp; quan hệ gộp là HANGCOSERI(MaSeri, SoSeri, MaSP, MaPN, SoDongPN, MaDH, SoDongDH, TinhTrangSeri, ThoiDiemNhap), tức hình dạng ban đầu của quan hệ này. Các quan hệ còn lại giữ nguyên: **25 nút**.

**Bước 2: Tạo nút và quan hệ nút.** Mỗi quan hệ là một nút Nᵢ với Q_Nᵢ = Qᵢ:

(Q1) LOAIHANG(MaLoai, TenLoai, MoTaLoai, MaLoaiCha).
(Q2) THUONGHIEU(MaTH, TenTH, MoTaTH).
(Q3) MATHANG(MaSP, SKU, TenSP, MoTaSP, GiaNiemYet, GiaKhuyenMai, ThoiHanBH, TinhTrangKD, CoSeri, MaLoai, MaTH).
(Q4) ANHMATHANG(MaAnh, MaSP, ViTriAnh, DuongDanAnh, LaAnhChinh).
(Q5) DINHNGHIATHONGSO(MaTS, MaLoai, TenTS, KieuGiaTri, DonViTS, BatBuoc).
(Q6) GIATRITHONGSO(MaSP, MaTS, GiaTriTS).
(Q7) KHACHHANG(MaKH, HoLotKH, TenKH, SDTKH, EmailKH, MaSoThueKH).
(Q8) NHANVIEN(MaNV, HoLotNV, TenNV, SDTNV, EmailNV, NgayVaoLam, NgayNghiViec, TinhTrangNV, ChucVu).
(Q9) TAIKHOAN(MaTK, TenDangNhap, MatKhauBam, TinhTrangTK, ThoiDiemTaoTK, MaKH, MaNV).
(Q10) NHACUNGCAP(MaNCC, TenNCC, NguoiLienHeNCC, SDTNCC, DiaChiNCC, MaSoThueNCC, TinhTrangHT).
(Q11) MAGIAMGIA(MaMG, CodeMG, TenChuongTrinh, LoaiGiam, MucGiam, DonToiThieu, GiamToiDa, NgayBatDau, NgayKetThuc, GioiHanLuot, MaNV).
(Q12) DONHANG(MaDH, SoDH, ThoiDiemLap, KenhBan, MaKH, MaNV, TenNguoiNhan, SDTNhan, DiaChiGiao, PhiGiao, GiamGia, MaMG, TinhTrangDH, DieuKienCoc, GhiChuDH).
(Q13) CHITIETDONHANG(MaDH, SoDongDH, MaSP, SoLuongBan, DonGiaChot, TenHangChot, SKUChot, ThoiHanBHChot).
(Q14) THANHTOAN(MaTT, MaDH, LoaiKhoan, PhuongThuc, SoTien, ThoiDiemTT, KetQuaTT, MaGiaoDichNgoai, DonViThanhToan, MaNV, MaNVThu).
(Q15) PHIEUGIAO(MaGiao, MaDH, MaNV, ThoiDiemXuat, TinhTrangGiao).
(Q16) LANGIAO(MaGiao, SoLan, ThoiDiemGiao, KetQuaGiao, LyDoThatBai, MaNV).
(Q17) PHIEUNHAP(MaPN, SoPhieu, MaNCC, MaNV, ThoiDiemNhan, TinhTrangPN, MaNVXacNhan, ThoiDiemXacNhan, SoHoaDonNCC, GhiChuPN).
(Q18) CHITIETPHIEUNHAP(MaPN, SoDongPN, MaSP, SoLuongNhap, GiaNhap).
(Q19) HANGCOSERI(MaSeri, MaPN, SoDongPN, MaDH, SoDongDH, TinhTrangSeri, ThoiDiemNhap, SoSeri, MaSP).
(Q20) GIAODICHKHO(MaGDK, MaSP, NhomKho, LoaiBienDong, SoLuongGD, ThoiDiemGD, MaNV, LoaiChungTu, MaChungTu, GhiChuGD).
(Q21) HOSODOITRA(MaHS, MaDH, MaNV, NgayDeNghi, LoaiTruongHop, LyDoDoiTra, TinhTrangHS, HinhThucXuLy).
(Q22) CHITIETTRA(MaHS, SoDongTra, SoDongDH, SoLuongTra, MaSeri).
(Q23) LANNHANLAI(MaNhanLai, MaHS, ThoiDiemNhanLai, MaNV, KetLuan, NhomSauKiemTra, ThoiDiemDuyet, MaNVDuyet).
(Q24) KHOANHOAN(MaHoan, MaTT, MaHS, MaPhieuBH, MaNV, SoTienHoan, PhuongThucHoan, ThoiDiemDuyetHoan, ThoiDiemChi, MaNVChi).
(Q25) PHIEUBAOHANH(MaPhieuBH, MaSeri, MaDH, SoDongDH, MoTaLoi, PhuKienDiKem, NgayNhan, NgayHenTra, NgayTraThucTe, TinhTrangBH, KetQuaBH, LyDoTuChoi, MaNV).

**Bước 3: Tạo nút bản lề và quan hệ nút bản lề.** Xét giao Q_ij = Qᵢ ∩ Qⱼ của mọi cặp nút; có 64 cặp có giao khác rỗng. Nếu khóa của Q_ij là khóa của một quan hệ nào đó thì không tạo nút bản lề (bảng 3.1).

| Qᵢ ∩ Qⱼ | Giao | Khóa của giao | Trùng khóa của | Kết luận |
|---|---|---|---|---|
| Q1 ∩ Q3 | {MaLoai} | {MaLoai} | Q1 | không tạo |
| Q1 ∩ Q5 | {MaLoai} | {MaLoai} | Q1 | không tạo |
| Q2 ∩ Q3 | {MaTH} | {MaTH} | Q2 | không tạo |
| Q3 ∩ Q4 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q3 ∩ Q5 | {MaLoai} | {MaLoai} | Q1 | không tạo |
| Q3 ∩ Q6 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q3 ∩ Q13 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q3 ∩ Q18 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q3 ∩ Q19 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q3 ∩ Q20 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q4 ∩ Q6 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q4 ∩ Q13 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q4 ∩ Q18 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q4 ∩ Q19 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q4 ∩ Q20 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q5 ∩ Q6 | {MaTS} | {MaTS} | Q5 | không tạo |
| Q6 ∩ Q13 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q6 ∩ Q18 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q6 ∩ Q19 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q6 ∩ Q20 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q7 ∩ Q9 | {MaKH} | {MaKH} | Q7 | không tạo |
| Q7 ∩ Q12 | {MaKH} | {MaKH} | Q7 | không tạo |
| Q9 ∩ Q12 | {MaKH} | {MaKH} | Q7 | không tạo |
| Q10 ∩ Q17 | {MaNCC} | {MaNCC} | Q10 | không tạo |
| Q11 ∩ Q12 | {MaMG} | {MaMG} | Q11 | không tạo |
| Q12 ∩ Q13 | {MaDH} | {MaDH} | Q12 | không tạo |
| Q12 ∩ Q14 | {MaDH} | {MaDH} | Q12 | không tạo |
| Q12 ∩ Q15 | {MaDH} | {MaDH} | Q12 | không tạo |
| Q12 ∩ Q19 | {MaDH} | {MaDH} | Q12 | không tạo |
| Q12 ∩ Q21 | {MaDH} | {MaDH} | Q12 | không tạo |
| Q12 ∩ Q25 | {MaDH} | {MaDH} | Q12 | không tạo |
| Q13 ∩ Q14 | {MaDH} | {MaDH} | Q12 | không tạo |
| Q13 ∩ Q15 | {MaDH} | {MaDH} | Q12 | không tạo |
| Q13 ∩ Q18 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q13 ∩ Q19 | {MaDH, MaSP, SoDongDH} | {MaDH, SoDongDH} | Q13 | không tạo |
| Q13 ∩ Q19 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q13 ∩ Q20 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q13 ∩ Q21 | {MaDH} | {MaDH} | Q12 | không tạo |
| Q13 ∩ Q25 | {MaDH, SoDongDH} | {MaDH, SoDongDH} | Q13 | không tạo |
| Q14 ∩ Q15 | {MaDH} | {MaDH} | Q12 | không tạo |
| Q14 ∩ Q19 | {MaDH} | {MaDH} | Q12 | không tạo |
| Q14 ∩ Q21 | {MaDH} | {MaDH} | Q12 | không tạo |
| Q14 ∩ Q24 | {MaTT} | {MaTT} | Q14 | không tạo |
| Q14 ∩ Q25 | {MaDH} | {MaDH} | Q12 | không tạo |
| Q15 ∩ Q16 | {MaGiao} | {MaGiao} | Q15 | không tạo |
| Q15 ∩ Q19 | {MaDH} | {MaDH} | Q12 | không tạo |
| Q15 ∩ Q21 | {MaDH} | {MaDH} | Q12 | không tạo |
| Q15 ∩ Q25 | {MaDH} | {MaDH} | Q12 | không tạo |
| Q17 ∩ Q18 | {MaPN} | {MaPN} | Q17 | không tạo |
| Q17 ∩ Q19 | {MaPN} | {MaPN} | Q17 | không tạo |
| Q18 ∩ Q19 | {MaPN, MaSP, SoDongPN} | {MaPN, SoDongPN} | Q18 | không tạo |
| Q18 ∩ Q19 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q18 ∩ Q20 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q19 ∩ Q20 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q19 ∩ Q21 | {MaDH} | {MaDH} | Q12 | không tạo |
| Q19 ∩ Q22 | {MaSeri} | {MaSeri} | Q19 | không tạo |
| Q19 ∩ Q25 | {MaDH, MaSeri, SoDongDH} | {MaSeri} | Q19 | không tạo |
| Q19 ∩ Q25 | {MaDH, SoDongDH} | {MaDH, SoDongDH} | Q13 | không tạo |
| Q21 ∩ Q22 | {MaHS} | {MaHS} | Q21 | không tạo |
| Q21 ∩ Q23 | {MaHS} | {MaHS} | Q21 | không tạo |
| Q21 ∩ Q24 | {MaHS} | {MaHS} | Q21 | không tạo |
| Q21 ∩ Q25 | {MaDH} | {MaDH} | Q12 | không tạo |
| Q22 ∩ Q23 | {MaHS} | {MaHS} | Q21 | không tạo |
| Q22 ∩ Q24 | {MaHS} | {MaHS} | Q21 | không tạo |
| Q22 ∩ Q25 | {MaSeri} | {MaSeri} | Q19 | không tạo |
| Q23 ∩ Q24 | {MaHS} | {MaHS} | Q21 | không tạo |
| Q24 ∩ Q25 | {MaPhieuBH} | {MaPhieuBH} | Q25 | không tạo |

*Bảng 3.1: Giao các cặp quan hệ nút*

**Kết luận:** không tạo nút bản lề nào.

**Bước 4: Tạo cung và quan hệ cung.** Với mỗi nút Nᵢ: PTH(Nᵢ) là tập các nút Nⱼ có khóa nằm trong Qᵢ; PTH_Thừa(Nᵢ) là các nút đạt được qua nút khác; LK(Nᵢ) là các nút có khóa nằm trong khóa của Nᵢ (lồng khóa); LK_Thừa(Nᵢ) là các lồng khóa đạt được qua lồng khóa khác; Cung(Nᵢ) = (PTH − PTH_Thừa) ∪ (LK − LK_Thừa).

| Nút | PTH(Nᵢ) | PTH_Thừa(Nᵢ) | LK(Nᵢ) | LK_Thừa(Nᵢ) | Cung(Nᵢ) |
|---|---|---|---|---|---|
| 1. LOAIHANG | – | – | – | – | – |
| 2. THUONGHIEU | – | – | – | – | – |
| 3. MATHANG | 1, 2 | – | – | – | 1, 2 |
| 4. ANHMATHANG | 3 | – | – | – | 3 |
| 5. DINHNGHIATHONGSO | 1 | – | – | – | 1 |
| 6. GIATRITHONGSO | 3, 5 | – | 3, 5 | – | 3, 5 |
| 7. KHACHHANG | – | – | – | – | – |
| 8. NHANVIEN | – | – | – | – | – |
| 9. TAIKHOAN | 7, 8 | – | – | – | 7, 8 |
| 10. NHACUNGCAP | – | – | – | – | – |
| 11. MAGIAMGIA | 8 | – | – | – | 8 |
| 12. DONHANG | 7, 8, 11 | – | – | – | 7, 8, 11 |
| 13. CHITIETDONHANG | 3, 12 | – | 12 | – | 3, 12 |
| 14. THANHTOAN | 8, 12 | – | – | – | 8, 12 |
| 15. PHIEUGIAO | 8, 12 | – | – | – | 8, 12 |
| 16. LANGIAO | 8, 15 | – | 15 | – | 8, 15 |
| 17. PHIEUNHAP | 8, 10 | – | – | – | 8, 10 |
| 18. CHITIETPHIEUNHAP | 3, 17 | – | 17 | – | 3, 17 |
| 19. HANGCOSERI | 3, 12, 13, 17, 18 | 3, 12, 17 | – | – | 13, 18 |
| 20. GIAODICHKHO | 3, 8 | – | – | – | 3, 8 |
| 21. HOSODOITRA | 8, 12 | – | – | – | 8, 12 |
| 22. CHITIETTRA | 19, 21 | – | 21 | – | 19, 21 |
| 23. LANNHANLAI | 8, 21 | – | – | – | 8, 21 |
| 24. KHOANHOAN | 8, 14, 21, 25 | – | – | – | 8, 14, 21, 25 |
| 25. PHIEUBAOHANH | 8, 12, 13, 19 | 12 | – | – | 8, 13, 19 |

*Bảng 3.2: Tập cung của từng nút*

Từ bảng trên, mỗi nút Nⱼ ∈ Cung(Nᵢ) cho một cung có hướng cᵢⱼ từ Nᵢ đến Nⱼ với quan hệ cung Qᵢⱼ = Qᵢ[KQᵢ ∪ KQⱼ]. Có tất cả **42 quan hệ cung** (kể cả khuyên của LOAIHANG và các cung vai trò tới NHANVIEN):

| Cung | Quan hệ cung Qᵢⱼ | Bản số xuôi (m, A, M) | Bản số ngược (m, A, M) |
|---|---|---|---|
| Q3.1: MATHANG → LOAIHANG | MATHANG(MaSP, MaLoai) | (1, 1, 1) | (0, -, n) |
| Q3.2: MATHANG → THUONGHIEU | MATHANG(MaSP, MaTH) | (1, 1, 1) | (0, -, n) |
| Q4.3: ANHMATHANG → MATHANG | ANHMATHANG(MaAnh, MaSP) | (1, 1, 1) | (0, -, n) |
| Q5.1: DINHNGHIATHONGSO → LOAIHANG | DINHNGHIATHONGSO(MaTS, MaLoai) | (1, 1, 1) | (0, -, n) |
| Q6.3: GIATRITHONGSO → MATHANG | GIATRITHONGSO(MaSP, MaTS) | (1, 1, 1) | (0, -, n) |
| Q6.5: GIATRITHONGSO → DINHNGHIATHONGSO | GIATRITHONGSO(MaSP, MaTS) | (1, 1, 1) | (0, -, n) |
| Q9.7: TAIKHOAN → KHACHHANG | TAIKHOAN(MaTK, MaKH) | (0, -, 1) | (0, -, 1) |
| Q9.8: TAIKHOAN → NHANVIEN | TAIKHOAN(MaTK, MaNV) | (0, -, 1) | (0, -, 1) |
| Q11.8: MAGIAMGIA → NHANVIEN | MAGIAMGIA(MaMG, MaNV) | (1, 1, 1) | (0, -, n) |
| Q12.7: DONHANG → KHACHHANG | DONHANG(MaDH, MaKH) | (0, -, 1) | (0, -, n) |
| Q12.8: DONHANG → NHANVIEN | DONHANG(MaDH, MaNV) | (0, -, 1) | (0, -, n) |
| Q12.11: DONHANG → MAGIAMGIA | DONHANG(MaDH, MaMG) | (0, -, 1) | (0, -, n) |
| Q13.3: CHITIETDONHANG → MATHANG | CHITIETDONHANG(MaDH, SoDongDH, MaSP) | (1, 1, 1) | (0, -, n) |
| Q13.12: CHITIETDONHANG → DONHANG | CHITIETDONHANG(MaDH, SoDongDH) | (1, 1, 1) | (1, -, n) |
| Q14.8: THANHTOAN → NHANVIEN | THANHTOAN(MaTT, MaNV) | (0, -, 1) | (0, -, n) |
| Q14.12: THANHTOAN → DONHANG | THANHTOAN(MaTT, MaDH) | (1, 1, 1) | (0, -, n) |
| Q15.8: PHIEUGIAO → NHANVIEN | PHIEUGIAO(MaGiao, MaNV) | (1, 1, 1) | (0, -, n) |
| Q15.12: PHIEUGIAO → DONHANG | PHIEUGIAO(MaGiao, MaDH) | (1, 1, 1) | (0, -, 1) |
| Q16.8: LANGIAO → NHANVIEN | LANGIAO(MaGiao, SoLan, MaNV) | (1, 1, 1) | (0, -, n) |
| Q16.15: LANGIAO → PHIEUGIAO | LANGIAO(MaGiao, SoLan) | (1, 1, 1) | (0, -, 3) |
| Q17.8: PHIEUNHAP → NHANVIEN | PHIEUNHAP(MaPN, MaNV) | (1, 1, 1) | (0, -, n) |
| Q17.10: PHIEUNHAP → NHACUNGCAP | PHIEUNHAP(MaPN, MaNCC) | (1, 1, 1) | (0, -, n) |
| Q18.3: CHITIETPHIEUNHAP → MATHANG | CHITIETPHIEUNHAP(MaPN, SoDongPN, MaSP) | (1, 1, 1) | (0, -, n) |
| Q18.17: CHITIETPHIEUNHAP → PHIEUNHAP | CHITIETPHIEUNHAP(MaPN, SoDongPN) | (1, 1, 1) | (1, -, n) |
| Q19.13: HANGCOSERI → CHITIETDONHANG | HANGCOSERI(MaSeri, MaDH, SoDongDH) | (0, -, 1) | (0, -, n) |
| Q19.18: HANGCOSERI → CHITIETPHIEUNHAP | HANGCOSERI(MaSeri, MaPN, SoDongPN) | (1, 1, 1) | (0, -, n) |
| Q20.3: GIAODICHKHO → MATHANG | GIAODICHKHO(MaGDK, MaSP) | (1, 1, 1) | (0, -, n) |
| Q20.8: GIAODICHKHO → NHANVIEN | GIAODICHKHO(MaGDK, MaNV) | (0, -, 1) | (0, -, n) |
| Q21.8: HOSODOITRA → NHANVIEN | HOSODOITRA(MaHS, MaNV) | (1, 1, 1) | (0, -, n) |
| Q21.12: HOSODOITRA → DONHANG | HOSODOITRA(MaHS, MaDH) | (1, 1, 1) | (0, -, n) |
| Q22.19: CHITIETTRA → HANGCOSERI | CHITIETTRA(MaHS, SoDongTra, MaSeri) | (0, -, 1) | (0, -, n) |
| Q22.21: CHITIETTRA → HOSODOITRA | CHITIETTRA(MaHS, SoDongTra) | (1, 1, 1) | (1, -, n) |
| Q23.8: LANNHANLAI → NHANVIEN | LANNHANLAI(MaNhanLai, MaNV) | (0, -, 1) | (0, -, n) |
| Q23.21: LANNHANLAI → HOSODOITRA | LANNHANLAI(MaNhanLai, MaHS) | (1, 1, 1) | (0, -, n) |
| Q24.8: KHOANHOAN → NHANVIEN | KHOANHOAN(MaHoan, MaNV) | (1, 1, 1) | (0, -, n) |
| Q24.14: KHOANHOAN → THANHTOAN | KHOANHOAN(MaHoan, MaTT) | (1, 1, 1) | (0, -, n) |
| Q24.21: KHOANHOAN → HOSODOITRA | KHOANHOAN(MaHoan, MaHS) | (0, -, 1) | (0, -, n) |
| Q24.25: KHOANHOAN → PHIEUBAOHANH | KHOANHOAN(MaHoan, MaPhieuBH) | (0, -, 1) | (0, -, n) |
| Q25.8: PHIEUBAOHANH → NHANVIEN | PHIEUBAOHANH(MaPhieuBH, MaNV) | (1, 1, 1) | (0, -, n) |
| Q25.13: PHIEUBAOHANH → CHITIETDONHANG | PHIEUBAOHANH(MaPhieuBH, MaDH, SoDongDH) | (1, 1, 1) | (0, -, n) |
| Q25.19: PHIEUBAOHANH → HANGCOSERI | PHIEUBAOHANH(MaPhieuBH, MaSeri) | (0, -, 1) | (0, -, n) |
| Q1.1: LOAIHANG → LOAIHANG | LOAIHANG(MaLoai, MaLoaiCha) | (0, -, 1) | (0, -, n) |

*Bảng 3.3: Quan hệ cung và bản số*

**Bước 5: Hủy nút bản lề thừa.** Không thực hiện vì không có nút bản lề.

**Bước 6: Mịn hóa các quan hệ nút.** Với mỗi cung Nᵢ → Nⱼ, hủy khỏi Qᵢ⁺ các thuộc tính khóa của Qⱼ không phải thuộc tính khóa của Qᵢ (chúng đã nằm ở quan hệ cung). Các nút bị thay đổi:

| Nút | Quan hệ nút sau mịn hóa | Thuộc tính chuyển sang quan hệ cung |
|---|---|---|
| LOAIHANG | LOAIHANG(MaLoai, TenLoai, MoTaLoai) | MaLoaiCha |
| MATHANG | MATHANG(MaSP, SKU, TenSP, MoTaSP, GiaNiemYet, GiaKhuyenMai, ThoiHanBH, TinhTrangKD, CoSeri) | MaLoai, MaTH |
| ANHMATHANG | ANHMATHANG(MaAnh, ViTriAnh, DuongDanAnh, LaAnhChinh) | MaSP |
| DINHNGHIATHONGSO | DINHNGHIATHONGSO(MaTS, TenTS, KieuGiaTri, DonViTS, BatBuoc) | MaLoai |
| TAIKHOAN | TAIKHOAN(MaTK, TenDangNhap, MatKhauBam, TinhTrangTK, ThoiDiemTaoTK) | MaKH, MaNV |
| MAGIAMGIA | MAGIAMGIA(MaMG, CodeMG, TenChuongTrinh, LoaiGiam, MucGiam, DonToiThieu, GiamToiDa, NgayBatDau, NgayKetThuc, GioiHanLuot) | MaNV |
| DONHANG | DONHANG(MaDH, SoDH, ThoiDiemLap, KenhBan, TenNguoiNhan, SDTNhan, DiaChiGiao, PhiGiao, GiamGia, TinhTrangDH, DieuKienCoc, GhiChuDH) | MaKH, MaNV, MaMG |
| CHITIETDONHANG | CHITIETDONHANG(MaDH, SoDongDH, SoLuongBan, DonGiaChot, TenHangChot, SKUChot, ThoiHanBHChot) | MaSP |
| THANHTOAN | THANHTOAN(MaTT, LoaiKhoan, PhuongThuc, SoTien, ThoiDiemTT, KetQuaTT, MaGiaoDichNgoai, DonViThanhToan, MaNVThu) | MaNV, MaDH |
| PHIEUGIAO | PHIEUGIAO(MaGiao, ThoiDiemXuat, TinhTrangGiao) | MaNV, MaDH |
| LANGIAO | LANGIAO(MaGiao, SoLan, ThoiDiemGiao, KetQuaGiao, LyDoThatBai) | MaNV |
| PHIEUNHAP | PHIEUNHAP(MaPN, SoPhieu, ThoiDiemNhan, TinhTrangPN, MaNVXacNhan, ThoiDiemXacNhan, SoHoaDonNCC, GhiChuPN) | MaNV, MaNCC |
| CHITIETPHIEUNHAP | CHITIETPHIEUNHAP(MaPN, SoDongPN, SoLuongNhap, GiaNhap) | MaSP |
| HANGCOSERI | HANGCOSERI(MaSeri, TinhTrangSeri, ThoiDiemNhap, SoSeri, MaSP) | MaDH, SoDongDH, MaPN, SoDongPN |
| GIAODICHKHO | GIAODICHKHO(MaGDK, NhomKho, LoaiBienDong, SoLuongGD, ThoiDiemGD, LoaiChungTu, MaChungTu, GhiChuGD) | MaSP, MaNV |
| HOSODOITRA | HOSODOITRA(MaHS, NgayDeNghi, LoaiTruongHop, LyDoDoiTra, TinhTrangHS, HinhThucXuLy) | MaNV, MaDH |
| CHITIETTRA | CHITIETTRA(MaHS, SoDongTra, SoDongDH, SoLuongTra) | MaSeri |
| LANNHANLAI | LANNHANLAI(MaNhanLai, ThoiDiemNhanLai, KetLuan, NhomSauKiemTra, ThoiDiemDuyet, MaNVDuyet) | MaNV, MaHS |
| KHOANHOAN | KHOANHOAN(MaHoan, SoTienHoan, PhuongThucHoan, ThoiDiemDuyetHoan, ThoiDiemChi, MaNVChi) | MaNV, MaTT, MaHS, MaPhieuBH |
| PHIEUBAOHANH | PHIEUBAOHANH(MaPhieuBH, MoTaLoi, PhuKienDiKem, NgayNhan, NgayHenTra, NgayTraThucTe, TinhTrangBH, KetQuaBH, LyDoTuChoi) | MaNV, MaDH, SoDongDH, MaSeri |

**Bước 7: Tạo cung vô hướng.** Không có nút Nₖ nào thỏa điều kiện (quan hệ chỉ gồm thuộc tính khóa, có đúng hai cung ra và không có cung vào): quan hệ nối n–n của lược đồ đều có thuộc tính riêng (GIATRITHONGSO có GiaTriTS; CHITIET* có số lượng, giá). Vì vậy không có cung vô hướng và đồ thị quan hệ chỉ có cung có hướng (hình 3.1).

![Hình 3.1: Đồ thị quan hệ của PowerTech (nút viền đậm là nút vào)](hinh/do_thi_quan_he.png)

*Hình 3.1: Đồ thị quan hệ (25 nút, 42 cung; cung xám là cung vai trò tới NHANVIEN; nút viền đậm là nút vào)*

Hình 3.1 chỉ ghi số thứ tự nút (tên nút ở bảng 3.2). Hình 3.2 vẽ cùng đồ thị nhưng ghi tên quan hệ để dễ đối chiếu. Đồ thị này không vẽ phẳng được (đã kiểm bằng thuật toán kiểm tra tính phẳng), nên khi mọi cung là đường thẳng vẫn còn chỗ hai cung cắt nhau. Các nút được xếp để chỉ còn 14 chỗ cắt, không cung nào đi xuyên qua một nút khác; chỗ hai cung cắt nhau không phải là nút. Con số này do chương trình tìm được, chưa chứng minh là nhỏ nhất.

![Hình 3.2: Đồ thị quan hệ có tên nút](hinh/do_thi_quan_he_ten.png)

*Hình 3.2: Đồ thị quan hệ có tên nút (cùng đồ thị với hình 3.1)*

**Nhận xét về đồ thị.** (1) Có nút đạt được bằng hai mạch đi khác nhau, làm lộ ràng buộc nhất quán: từ PHIEUBAOHANH tới CHITIETDONHANG có mạch trực tiếp và mạch qua HANGCOSERI (hai mạch phải cùng mặt hàng; mạch trực tiếp là lần mua ứng với phiếu, mạch qua HANGCOSERI là lần bán gần nhất, nên khi chiếc được bán lại, người mua của phiếu phải tra theo mạch trực tiếp); từ KHOANHOAN tới DONHANG có mạch qua THANHTOAN, mạch qua HOSODOITRA và mạch qua PHIEUBAOHANH (các mạch phải cùng một đơn). Đó là ràng buộc 2 và 4 ở mục 2.3.6. (2) CHITIETTRA chỉ nối với HOSODOITRA và HANGCOSERI; dòng đơn được trả là (HOSODOITRA.MaDH, SoDongDH) nên đường từ dòng trả tới dòng đơn đi qua HOSODOITRA và cần cả MaDH lẫn SoDongDH, không phải một cung đơn. (3) NHANVIEN là nút đích của nhiều cung vai trò (lập đơn, xác nhận thu, giao, nhập, tạo mã, tài khoản…): đó là các con đường **truy trách nhiệm** từ chứng từ về người thực hiện; chức vụ ChucVu của người đó cho biết khâu họ được làm (truy vấn K6–K8). (4) Đồ thị không duy nhất: chọn khóa ưu tiên khác (ví dụ SoDH cho DONHANG) cho đồ thị khác nhưng tương đương về bảo toàn thông tin và PTH.

## 3.2 Ý NGHĨA CÁC CON ĐƯỜNG TRUY XUẤT

### 3.2.1 Nút vào

Theo giáo trình, nút vào là nút mà người dùng cung cấp giá trị khóa để truy xuất trực tiếp một bộ. Để liệt kê các con đường nhiều ngữ nghĩa nhất, chương này chọn **nút vào là các nút không có cung đi tới** (không quan hệ nào trỏ về nó bằng cung có hướng), vì từ nút khác chỉ đến được các nút này bằng cách đi ngược cung (cho nhiều bộ). Có **8 nút vào**: 4. ANHMATHANG, 6. GIATRITHONGSO, 9. TAIKHOAN, 16. LANGIAO, 20. GIAODICHKHO, 22. CHITIETTRA, 23. LANNHANLAI, 24. KHOANHOAN. Từ mỗi nút vào, mọi mạch đi theo chiều cung đến nút cuối (không lặp nút) là một con đường truy xuất; tổng cộng **57 con đường**. Các nút còn lại (KHACHHANG, DONHANG, MATHANG…) nằm trên các đường này và cũng là ngõ vào tra cứu theo khóa riêng (mục 3.4).

### 3.2.2 Con đường truy xuất cơ bản (theo từng cung)

Mỗi cung có hai con đường: xuôi theo cung (cho một bộ, (1,1,1) hoặc (0,-,1)) và ngược lại (cho n bộ). Ngữ nghĩa:

| Cung | Xuôi (từ một bộ của nút đi) | Ngược (từ một bộ của nút đến) |
|---|---|---|
| 3 → 1 | Cho biết mặt hàng thuộc loại hàng nào (1, 1, 1) | Từ một loại hàng cho biết các mặt hàng của loại hàng đó (0, -, n) |
| 3 → 2 | Cho biết mặt hàng mang thương hiệu nào (1, 1, 1) | Từ một thương hiệu cho biết các mặt hàng của thương hiệu đó (0, -, n) |
| 4 → 3 | Cho biết ảnh mặt hàng minh họa cho mặt hàng nào (1, 1, 1) | Từ một mặt hàng cho biết các ảnh của mặt hàng đó (0, -, n) |
| 5 → 1 | Cho biết thông số do loại hàng nào quy định (1, 1, 1) | Từ một loại hàng cho biết các thông số mà loại hàng đó quy định (0, -, n) |
| 6 → 3 | Cho biết giá trị thông số thuộc mặt hàng nào (1, 1, 1) | Từ một mặt hàng cho biết các giá trị thông số của mặt hàng đó (0, -, n) |
| 6 → 5 | Cho biết giá trị thông số ứng với thông số nào (1, 1, 1) | Từ một thông số cho biết các mặt hàng có giá trị cho thông số đó (0, -, n) |
| 9 → 7 | Cho biết tài khoản thuộc khách hàng nào (nếu là tài khoản khách) (0, -, 1) | Từ một khách hàng cho biết tài khoản của khách đó (tối đa một) (0, -, 1) |
| 9 → 8 | Cho biết tài khoản thuộc nhân viên nào (nếu là tài khoản nhân viên) (0, -, 1) | Từ một nhân viên cho biết tài khoản của nhân viên đó (tối đa một) (0, -, 1) |
| 11 → 8 | Cho biết mã giảm giá do nhân viên nào tạo (1, 1, 1) | Từ một nhân viên cho biết các mã giảm giá do nhân viên đó tạo (0, -, n) |
| 12 → 7 | Cho biết đơn hàng do khách hàng nào đặt (nếu có hồ sơ khách) (0, -, 1) | Từ một khách hàng cho biết các đơn hàng của khách đó (0, -, n) |
| 12 → 8 | Cho biết đơn hàng do nhân viên nào lập (0, -, 1) | Từ một nhân viên cho biết các đơn hàng do nhân viên đó lập (0, -, n) |
| 12 → 11 | Cho biết đơn hàng áp dụng mã giảm giá nào (nếu có) (0, -, 1) | Từ một mã giảm giá cho biết các đơn đã dùng mã giảm giá đó (0, -, n) |
| 13 → 3 | Cho biết dòng đơn bán mặt hàng nào (1, 1, 1) | Từ một mặt hàng cho biết các dòng đơn đã bán mặt hàng đó (0, -, n) |
| 13 → 12 | Cho biết dòng đơn thuộc đơn hàng nào (1, 1, 1) | Từ một đơn hàng cho biết các dòng của đơn đó (1, -, n) |
| 14 → 8 | Cho biết khoản thanh toán do nhân viên nào xác nhận thu (0, -, 1) | Từ một nhân viên cho biết các khoản thu do nhân viên đó xác nhận (0, -, n) |
| 14 → 12 | Cho biết khoản thanh toán trả cho đơn hàng nào (1, 1, 1) | Từ một đơn hàng cho biết các lần thanh toán và đặt cọc của đơn đó (0, -, n) |
| 15 → 8 | Cho biết phiếu giao do nhân viên nào giao (1, 1, 1) | Từ một nhân viên cho biết các phiếu giao do nhân viên đó phụ trách (0, -, n) |
| 15 → 12 | Cho biết phiếu giao lập cho đơn hàng nào (1, 1, 1) | Từ một đơn hàng cho biết phiếu giao của đơn đó (tối đa một) (0, -, 1) |
| 16 → 8 | Cho biết lần giao hàng do nhân viên nào giao (1, 1, 1) | Từ một nhân viên cho biết các lần giao do nhân viên đó thực hiện (0, -, n) |
| 16 → 15 | Cho biết lần giao hàng thuộc phiếu giao nào (1, 1, 1) | Từ một phiếu giao cho biết các lần thử giao của phiếu đó (tối đa 3) (0, -, 3) |
| 17 → 8 | Cho biết phiếu nhập do nhân viên kho nào lập (1, 1, 1) | Từ một nhân viên cho biết các phiếu nhập do nhân viên đó lập (0, -, n) |
| 17 → 10 | Cho biết phiếu nhập nhận từ nhà cung cấp nào (1, 1, 1) | Từ một nhà cung cấp cho biết các phiếu nhập từ nhà cung cấp đó (0, -, n) |
| 18 → 3 | Cho biết dòng phiếu nhập nhập mặt hàng nào (1, 1, 1) | Từ một mặt hàng cho biết các dòng nhập của mặt hàng đó (0, -, n) |
| 18 → 17 | Cho biết dòng phiếu nhập thuộc phiếu nhập nào (1, 1, 1) | Từ một phiếu nhập cho biết các dòng của phiếu nhập đó (1, -, n) |
| 19 → 13 | Cho biết chiếc hàng có seri bán gần nhất ở dòng đơn nào (0, -, 1) | Từ một dòng đơn cho biết các chiếc hàng có seri có lần bán gần nhất ở dòng đơn đó (0, -, n) |
| 19 → 18 | Cho biết chiếc hàng có seri nhập về ở dòng phiếu nhập nào (1, 1, 1) | Từ một dòng phiếu nhập cho biết các chiếc hàng có seri nhập ở dòng đó (0, -, n) |
| 20 → 3 | Cho biết giao dịch kho liên quan đến mặt hàng nào (1, 1, 1) | Từ một mặt hàng cho biết các giao dịch kho của mặt hàng đó (0, -, n) |
| 20 → 8 | Cho biết giao dịch kho do nhân viên nào thực hiện (0, -, 1) | Từ một nhân viên cho biết các giao dịch kho do nhân viên đó thực hiện (0, -, n) |
| 21 → 8 | Cho biết hồ sơ đổi trả do nhân viên nào tiếp nhận (1, 1, 1) | Từ một nhân viên cho biết các hồ sơ đổi trả do nhân viên đó tiếp nhận (0, -, n) |
| 21 → 12 | Cho biết hồ sơ đổi trả lập cho đơn hàng nào (1, 1, 1) | Từ một đơn hàng cho biết các hồ sơ đổi trả của đơn đó (0, -, n) |
| 22 → 19 | Cho biết dòng trả hàng ghi chiếc hàng có seri nào (0, -, 1) | Từ một chiếc hàng có seri cho biết các dòng trả có chiếc hàng đó (0, -, n) |
| 22 → 21 | Cho biết dòng trả hàng thuộc hồ sơ đổi trả nào (1, 1, 1) | Từ một hồ sơ đổi trả cho biết các dòng trả của hồ sơ đó (1, -, n) |
| 23 → 8 | Cho biết lần nhận lại hàng do nhân viên nào kiểm tra (0, -, 1) | Từ một nhân viên cho biết các lần nhận lại do nhân viên đó kiểm tra (0, -, n) |
| 23 → 21 | Cho biết lần nhận lại hàng thuộc hồ sơ đổi trả nào (1, 1, 1) | Từ một hồ sơ đổi trả cho biết các lần nhận lại của hồ sơ đó (0, -, n) |
| 24 → 8 | Cho biết khoản hoàn tiền do người quản lý nào duyệt (1, 1, 1) | Từ một nhân viên cho biết các khoản hoàn do người quản lý đó duyệt (0, -, n) |
| 24 → 14 | Cho biết khoản hoàn tiền tính trên khoản thanh toán nào (1, 1, 1) | Từ một khoản thanh toán cho biết các khoản hoàn của khoản thanh toán đó (0, -, n) |
| 24 → 21 | Cho biết khoản hoàn tiền theo hồ sơ đổi trả nào (nếu do đổi trả) (0, -, 1) | Từ một hồ sơ đổi trả cho biết các khoản hoàn của hồ sơ đó (0, -, n) |
| 24 → 25 | Cho biết khoản hoàn tiền theo phiếu bảo hành nào (nếu do bảo hành thu hồi) (0, -, 1) | Từ một phiếu bảo hành cho biết các khoản hoàn của phiếu đó (0, -, n) |
| 25 → 8 | Cho biết phiếu bảo hành do nhân viên nào tiếp nhận (1, 1, 1) | Từ một nhân viên cho biết các phiếu bảo hành do nhân viên đó tiếp nhận (0, -, n) |
| 25 → 13 | Cho biết phiếu bảo hành mua ở dòng đơn nào (1, 1, 1) | Từ một dòng đơn cho biết các phiếu bảo hành của dòng đơn đó (0, -, n) |
| 25 → 19 | Cho biết phiếu bảo hành ứng với chiếc hàng có seri nào (0, -, 1) | Từ một chiếc hàng có seri cho biết các phiếu bảo hành của chiếc hàng đó (0, -, n) |
| 1 → 1 | Cho biết loại hàng thuộc loại hàng cha nào (0, -, 1) | Từ một loại hàng cho biết các loại hàng con của loại hàng đó (0, -, n) |

*Bảng 3.4: Ngữ nghĩa các con đường truy xuất cơ bản*

### 3.2.3 Các con đường truy xuất dài từ nút vào

| Đường | Mạch đi | Ý nghĩa dữ liệu | Số dòng trên dữ liệu minh họa |
|---|---|---|---|
| 1 | 4 → 3 → 1 | Cho biết ảnh mặt hàng minh họa cho mặt hàng nào; mặt hàng đó thuộc loại hàng nào. | 5 |
| 2 | 4 → 3 → 2 | Cho biết ảnh mặt hàng minh họa cho mặt hàng nào; mặt hàng đó mang thương hiệu nào. | 5 |
| 3 | 6 → 3 → 1 | Cho biết giá trị thông số thuộc mặt hàng nào; mặt hàng đó thuộc loại hàng nào. | 5 |
| 4 | 6 → 3 → 2 | Cho biết giá trị thông số thuộc mặt hàng nào; mặt hàng đó mang thương hiệu nào. | 5 |
| 5 | 6 → 5 → 1 | Cho biết giá trị thông số ứng với thông số nào; thông số đó do loại hàng nào quy định. | 5 |
| 6 | 9 → 7 | Cho biết tài khoản thuộc khách hàng nào (nếu là tài khoản khách). | 3 |
| 7 | 9 → 8 | Cho biết tài khoản thuộc nhân viên nào (nếu là tài khoản nhân viên). | 3 |
| 8 | 16 → 8 | Cho biết lần giao hàng do nhân viên nào giao. | 4 |
| 9 | 16 → 15 → 8 | Cho biết lần giao hàng thuộc phiếu giao nào; phiếu giao đó do nhân viên nào giao. | 4 |
| 10 | 16 → 15 → 12 → 7 | Cho biết lần giao hàng thuộc phiếu giao nào; phiếu giao đó lập cho đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách). | 4 |
| 11 | 16 → 15 → 12 → 8 | Cho biết lần giao hàng thuộc phiếu giao nào; phiếu giao đó lập cho đơn hàng nào; đơn hàng đó do nhân viên nào lập. | 1 |
| 12 | 16 → 15 → 12 → 11 → 8 | Cho biết lần giao hàng thuộc phiếu giao nào; phiếu giao đó lập cho đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo. | 1 |
| 13 | 20 → 3 → 1 | Cho biết giao dịch kho liên quan đến mặt hàng nào; mặt hàng đó thuộc loại hàng nào. | 4 |
| 14 | 20 → 3 → 2 | Cho biết giao dịch kho liên quan đến mặt hàng nào; mặt hàng đó mang thương hiệu nào. | 4 |
| 15 | 20 → 8 | Cho biết giao dịch kho do nhân viên nào thực hiện. | 4 |
| 16 | 22 → 19 → 13 → 3 → 1 | Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó bán gần nhất ở dòng đơn nào; dòng đơn đó bán mặt hàng nào; mặt hàng đó thuộc loại hàng nào. | 1 |
| 17 | 22 → 19 → 13 → 3 → 2 | Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó bán gần nhất ở dòng đơn nào; dòng đơn đó bán mặt hàng nào; mặt hàng đó mang thương hiệu nào. | 1 |
| 18 | 22 → 19 → 13 → 12 → 7 | Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó bán gần nhất ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách). | 1 |
| 19 | 22 → 19 → 13 → 12 → 8 | Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó bán gần nhất ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó do nhân viên nào lập. | 1 |
| 20 | 22 → 19 → 13 → 12 → 11 → 8 | Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó bán gần nhất ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo. | 1 |
| 21 | 22 → 19 → 18 → 3 → 1 | Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó nhập mặt hàng nào; mặt hàng đó thuộc loại hàng nào. | 1 |
| 22 | 22 → 19 → 18 → 3 → 2 | Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó nhập mặt hàng nào; mặt hàng đó mang thương hiệu nào. | 1 |
| 23 | 22 → 19 → 18 → 17 → 8 | Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó thuộc phiếu nhập nào; phiếu nhập đó do nhân viên kho nào lập. | 1 |
| 24 | 22 → 19 → 18 → 17 → 10 | Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó thuộc phiếu nhập nào; phiếu nhập đó nhận từ nhà cung cấp nào. | 1 |
| 25 | 22 → 21 → 8 | Cho biết dòng trả hàng thuộc hồ sơ đổi trả nào; hồ sơ đổi trả đó do nhân viên nào tiếp nhận. | 1 |
| 26 | 22 → 21 → 12 → 7 | Cho biết dòng trả hàng thuộc hồ sơ đổi trả nào; hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách). | 1 |
| 27 | 22 → 21 → 12 → 8 | Cho biết dòng trả hàng thuộc hồ sơ đổi trả nào; hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó do nhân viên nào lập. | 1 |
| 28 | 22 → 21 → 12 → 11 → 8 | Cho biết dòng trả hàng thuộc hồ sơ đổi trả nào; hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo. | 1 |
| 29 | 23 → 8 | Cho biết lần nhận lại hàng do nhân viên nào kiểm tra. | 1 |
| 30 | 23 → 21 → 8 | Cho biết lần nhận lại hàng thuộc hồ sơ đổi trả nào; hồ sơ đổi trả đó do nhân viên nào tiếp nhận. | 1 |
| 31 | 23 → 21 → 12 → 7 | Cho biết lần nhận lại hàng thuộc hồ sơ đổi trả nào; hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách). | 1 |
| 32 | 23 → 21 → 12 → 8 | Cho biết lần nhận lại hàng thuộc hồ sơ đổi trả nào; hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó do nhân viên nào lập. | 1 |
| 33 | 23 → 21 → 12 → 11 → 8 | Cho biết lần nhận lại hàng thuộc hồ sơ đổi trả nào; hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo. | 1 |
| 34 | 24 → 8 | Cho biết khoản hoàn tiền do người quản lý nào duyệt. | 2 |
| 35 | 24 → 14 → 8 | Cho biết khoản hoàn tiền tính trên khoản thanh toán nào; khoản thanh toán đó do nhân viên nào xác nhận thu. | 2 |
| 36 | 24 → 14 → 12 → 7 | Cho biết khoản hoàn tiền tính trên khoản thanh toán nào; khoản thanh toán đó trả cho đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách). | 2 |
| 37 | 24 → 14 → 12 → 8 | Cho biết khoản hoàn tiền tính trên khoản thanh toán nào; khoản thanh toán đó trả cho đơn hàng nào; đơn hàng đó do nhân viên nào lập. | 2 |
| 38 | 24 → 14 → 12 → 11 → 8 | Cho biết khoản hoàn tiền tính trên khoản thanh toán nào; khoản thanh toán đó trả cho đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo. | 2 |
| 39 | 24 → 21 → 8 | Cho biết khoản hoàn tiền theo hồ sơ đổi trả nào (nếu do đổi trả); hồ sơ đổi trả đó do nhân viên nào tiếp nhận. | 1 |
| 40 | 24 → 21 → 12 → 7 | Cho biết khoản hoàn tiền theo hồ sơ đổi trả nào (nếu do đổi trả); hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách). | 1 |
| 41 | 24 → 21 → 12 → 8 | Cho biết khoản hoàn tiền theo hồ sơ đổi trả nào (nếu do đổi trả); hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó do nhân viên nào lập. | 1 |
| 42 | 24 → 21 → 12 → 11 → 8 | Cho biết khoản hoàn tiền theo hồ sơ đổi trả nào (nếu do đổi trả); hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo. | 1 |
| 43 | 24 → 25 → 8 | Cho biết khoản hoàn tiền theo phiếu bảo hành nào (nếu do bảo hành thu hồi); phiếu bảo hành đó do nhân viên nào tiếp nhận. | 1 |
| 44 | 24 → 25 → 13 → 3 → 1 | Cho biết khoản hoàn tiền theo phiếu bảo hành nào (nếu do bảo hành thu hồi); phiếu bảo hành đó mua ở dòng đơn nào; dòng đơn đó bán mặt hàng nào; mặt hàng đó thuộc loại hàng nào. | 1 |
| 45 | 24 → 25 → 13 → 3 → 2 | Cho biết khoản hoàn tiền theo phiếu bảo hành nào (nếu do bảo hành thu hồi); phiếu bảo hành đó mua ở dòng đơn nào; dòng đơn đó bán mặt hàng nào; mặt hàng đó mang thương hiệu nào. | 1 |
| 46 | 24 → 25 → 13 → 12 → 7 | Cho biết khoản hoàn tiền theo phiếu bảo hành nào (nếu do bảo hành thu hồi); phiếu bảo hành đó mua ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách). | 1 |
| 47 | 24 → 25 → 13 → 12 → 8 | Cho biết khoản hoàn tiền theo phiếu bảo hành nào (nếu do bảo hành thu hồi); phiếu bảo hành đó mua ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó do nhân viên nào lập. | 1 |
| 48 | 24 → 25 → 13 → 12 → 11 → 8 | Cho biết khoản hoàn tiền theo phiếu bảo hành nào (nếu do bảo hành thu hồi); phiếu bảo hành đó mua ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo. | 1 |
| 49 | 24 → 25 → 19 → 13 → 3 → 1 | Cho biết khoản hoàn tiền theo phiếu bảo hành nào (nếu do bảo hành thu hồi); phiếu bảo hành đó ứng với chiếc hàng có seri nào; chiếc hàng có seri đó bán gần nhất ở dòng đơn nào; dòng đơn đó bán mặt hàng nào; mặt hàng đó thuộc loại hàng nào. | 1 |
| 50 | 24 → 25 → 19 → 13 → 3 → 2 | Cho biết khoản hoàn tiền theo phiếu bảo hành nào (nếu do bảo hành thu hồi); phiếu bảo hành đó ứng với chiếc hàng có seri nào; chiếc hàng có seri đó bán gần nhất ở dòng đơn nào; dòng đơn đó bán mặt hàng nào; mặt hàng đó mang thương hiệu nào. | 1 |
| 51 | 24 → 25 → 19 → 13 → 12 → 7 | Cho biết khoản hoàn tiền theo phiếu bảo hành nào (nếu do bảo hành thu hồi); phiếu bảo hành đó ứng với chiếc hàng có seri nào; chiếc hàng có seri đó bán gần nhất ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách). | 1 |
| 52 | 24 → 25 → 19 → 13 → 12 → 8 | Cho biết khoản hoàn tiền theo phiếu bảo hành nào (nếu do bảo hành thu hồi); phiếu bảo hành đó ứng với chiếc hàng có seri nào; chiếc hàng có seri đó bán gần nhất ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó do nhân viên nào lập. | 1 |
| 53 | 24 → 25 → 19 → 13 → 12 → 11 → 8 | Cho biết khoản hoàn tiền theo phiếu bảo hành nào (nếu do bảo hành thu hồi); phiếu bảo hành đó ứng với chiếc hàng có seri nào; chiếc hàng có seri đó bán gần nhất ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo. | 1 |
| 54 | 24 → 25 → 19 → 18 → 3 → 1 | Cho biết khoản hoàn tiền theo phiếu bảo hành nào (nếu do bảo hành thu hồi); phiếu bảo hành đó ứng với chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó nhập mặt hàng nào; mặt hàng đó thuộc loại hàng nào. | 1 |
| 55 | 24 → 25 → 19 → 18 → 3 → 2 | Cho biết khoản hoàn tiền theo phiếu bảo hành nào (nếu do bảo hành thu hồi); phiếu bảo hành đó ứng với chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó nhập mặt hàng nào; mặt hàng đó mang thương hiệu nào. | 1 |
| 56 | 24 → 25 → 19 → 18 → 17 → 8 | Cho biết khoản hoàn tiền theo phiếu bảo hành nào (nếu do bảo hành thu hồi); phiếu bảo hành đó ứng với chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó thuộc phiếu nhập nào; phiếu nhập đó do nhân viên kho nào lập. | 1 |
| 57 | 24 → 25 → 19 → 18 → 17 → 10 | Cho biết khoản hoàn tiền theo phiếu bảo hành nào (nếu do bảo hành thu hồi); phiếu bảo hành đó ứng với chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó thuộc phiếu nhập nào; phiếu nhập đó nhận từ nhà cung cấp nào. | 1 |

*Bảng 3.5: 57 con đường truy xuất từ các nút vào (số là số thứ tự nút ở bảng 3.2)*

## 3.3 CÁC TRUY VẤN BẰNG NGÔN NGỮ SQL

### 3.3.1 Quy tắc chung

Mỗi con đường truy xuất tương ứng một câu SELECT nối (JOIN) các quan hệ theo thứ tự các nút trên đường; điều kiện nối là khóa ngoại của cung (cột của nút đi bằng cột khóa của nút đến). Danh sách cột chỉ gồm khóa chính của các quan hệ trên đường (cột trùng giá trị do nối thì lấy một lần), đủ để nhận ra mỗi dòng kết quả là một bộ chứng từ nào; muốn xem thêm thông tin thì thêm cột cần thiết:

```sql
SELECT a0.<khóa chính>, a1.<khóa chính>, a2.<khóa chính>, ...
FROM   <nút vào> a0
JOIN   <nút 1>   a1 ON a0.<khóa ngoại> = a1.<khóa>
JOIN   <nút 2>   a2 ON a1.<khóa ngoại> = a2.<khóa>
...
```

Với nút HANGCOSERI (gộp từ HANGCOSERI và SERIMATHANG) câu lệnh nối thêm SERIMATHANG theo MaSeri để lấy lại đủ số seri và mặt hàng. Đã sinh **57 câu lệnh**, lưu ở `sql/03_truy_van_cac_duong_truy_xuat.sql`; mỗi câu đã chạy thử và đều trả về ít nhất một dòng (cột cuối bảng 3.5).

### 3.3.2 Một số câu truy vấn của các con đường

**Đường 46: KHOANHOAN → PHIEUBAOHANH → CHITIETDONHANG → DONHANG → KHACHHANG**

Ý nghĩa: Cho biết khoản hoàn tiền theo phiếu bảo hành nào (nếu do bảo hành thu hồi); phiếu bảo hành đó mua ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách).

```sql
SELECT kc.MaHoan, bh.MaPhieuBH, ct.MaDH, ct.SoDongDH, kh.MaKH
FROM KHOANHOAN kc
JOIN PHIEUBAOHANH bh ON kc.MaPhieuBH = bh.MaPhieuBH
JOIN CHITIETDONHANG ct ON bh.MaDH = ct.MaDH AND bh.SoDongDH = ct.SoDongDH
JOIN DONHANG dh ON ct.MaDH = dh.MaDH
JOIN KHACHHANG kh ON dh.MaKH = kh.MaKH;
```

**Đường 36: KHOANHOAN → THANHTOAN → DONHANG → KHACHHANG**

Ý nghĩa: Cho biết khoản hoàn tiền tính trên khoản thanh toán nào; khoản thanh toán đó trả cho đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách).

```sql
SELECT kc.MaHoan, tt.MaTT, dh.MaDH, kh.MaKH
FROM KHOANHOAN kc
JOIN THANHTOAN tt ON kc.MaTT = tt.MaTT
JOIN DONHANG dh ON tt.MaDH = dh.MaDH
JOIN KHACHHANG kh ON dh.MaKH = kh.MaKH;
```

**Đường 24: CHITIETTRA → HANGCOSERI → CHITIETPHIEUNHAP → PHIEUNHAP → NHACUNGCAP**

Ý nghĩa: Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó thuộc phiếu nhập nào; phiếu nhập đó nhận từ nhà cung cấp nào.

```sql
SELECT cr.MaHS, cr.SoDongTra, hs.MaSeri, cp.MaPN, cp.SoDongPN, nc.MaNCC
FROM CHITIETTRA cr
JOIN HANGCOSERI hs ON cr.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETPHIEUNHAP cp ON hs.MaPN = cp.MaPN AND hs.SoDongPN = cp.SoDongPN
JOIN PHIEUNHAP pn ON cp.MaPN = pn.MaPN
JOIN NHACUNGCAP nc ON pn.MaNCC = nc.MaNCC;
```

**Đường 5: GIATRITHONGSO → DINHNGHIATHONGSO → LOAIHANG**

Ý nghĩa: Cho biết giá trị thông số ứng với thông số nào; thông số đó do loại hàng nào quy định.

```sql
SELECT gt.MaSP, gt.MaTS, lh.MaLoai
FROM GIATRITHONGSO gt
JOIN DINHNGHIATHONGSO dn ON gt.MaTS = dn.MaTS
JOIN LOAIHANG lh ON dn.MaLoai = lh.MaLoai;
```

**Đường 10: LANGIAO → PHIEUGIAO → DONHANG → KHACHHANG**

Ý nghĩa: Cho biết lần giao hàng thuộc phiếu giao nào; phiếu giao đó lập cho đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách).

```sql
SELECT lg.MaGiao, lg.SoLan, dh.MaDH, kh.MaKH
FROM LANGIAO lg
JOIN PHIEUGIAO pg ON lg.MaGiao = pg.MaGiao
JOIN DONHANG dh ON pg.MaDH = dh.MaDH
JOIN KHACHHANG kh ON dh.MaKH = kh.MaKH;
```

### 3.3.3 Truy vấn khai thác theo con đường truy xuất

Các yêu cầu khai thác thực tế dùng các con đường (cả xuôi và ngược) của đồ thị. Mỗi truy vấn dưới đây ở `sql/04_truy_van_khai_thac.sql` và đã chạy thử:

**K1. Lịch sử mua hàng của một khách theo số điện thoại** (đường: KHACHHANG ⇒ DONHANG ⇒ CHITIETDONHANG; 3 dòng trên dữ liệu minh họa)

```sql
SELECT dh.SoDH, dh.ThoiDiemLap, ct.SoDongDH, ct.TenHangChot, ct.SoLuongBan, ct.DonGiaChot,
       ct.SoLuongBan * ct.DonGiaChot AS ThanhTien
FROM KHACHHANG kh
JOIN DONHANG dh ON dh.MaKH = kh.MaKH
JOIN CHITIETDONHANG ct ON ct.MaDH = dh.MaDH
WHERE kh.SDTKH = '0900000001'
ORDER BY dh.ThoiDiemLap, ct.SoDongDH;
```

**K2. Doanh thu tiền hàng theo loại hàng trong tháng 10/2026 (không tính đơn đã hủy, chưa trừ giảm giá và hoàn tiền)** (đường: CHITIETDONHANG → DONHANG; CHITIETDONHANG → MATHANG → LOAIHANG; 3 dòng trên dữ liệu minh họa)

```sql
SELECT lh.TenLoai, SUM(ct.SoLuongBan * ct.DonGiaChot) AS DoanhThuTienHang
FROM CHITIETDONHANG ct
JOIN DONHANG dh ON dh.MaDH = ct.MaDH
JOIN MATHANG mh ON mh.MaSP = ct.MaSP
JOIN LOAIHANG lh ON lh.MaLoai = mh.MaLoai
WHERE dh.TinhTrangDH <> 'Đã hủy'
  AND dh.ThoiDiemLap >= '2026-10-01' AND dh.ThoiDiemLap < '2026-11-01'
GROUP BY lh.TenLoai
ORDER BY DoanhThuTienHang DESC;
```

**K3. Số lượng hàng trong kho theo mặt hàng và nhóm kho, tính từ giao dịch kho** (đường: GIAODICHKHO → MATHANG; 3 dòng trên dữ liệu minh họa)

```sql
SELECT mh.TenSP, gd.NhomKho,
       SUM(CASE WHEN gd.LoaiBienDong IN ('Nhập', 'Nhận lại') THEN gd.SoLuongGD
                WHEN gd.LoaiBienDong = 'Xuất bán' THEN -gd.SoLuongGD
                ELSE 0 END) AS SoLuong
FROM GIAODICHKHO gd
JOIN MATHANG mh ON mh.MaSP = gd.MaSP
GROUP BY mh.TenSP, gd.NhomKho
ORDER BY mh.TenSP, gd.NhomKho;
```

**K4. Truy vết một chiếc hàng theo số seri: nhập từ đâu, lần bán gần nhất cho ai** (đường: SERIMATHANG ⇒ HANGCOSERI → CHITIETPHIEUNHAP → PHIEUNHAP → NHACUNGCAP; HANGCOSERI → CHITIETDONHANG → DONHANG → KHACHHANG; 1 dòng trên dữ liệu minh họa)

```sql
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
```

**K5. Hồ sơ đổi trả của một đơn kèm số tiền đã hoàn** (đường: HOSODOITRA ⇒ CHITIETTRA; HOSODOITRA ⇒ KHOANHOAN → THANHTOAN; 1 dòng trên dữ liệu minh họa)

```sql
SELECT hd.MaHS, hd.LoaiTruongHop, ct.SoDongDH, ct.SoLuongTra, kc.SoTienHoan, tt.SoTien AS SoTienDaThu
FROM HOSODOITRA hd
JOIN CHITIETTRA ct ON ct.MaHS = hd.MaHS
LEFT JOIN KHOANHOAN kc ON kc.MaHS = hd.MaHS
LEFT JOIN THANHTOAN tt ON tt.MaTT = kc.MaTT
WHERE hd.MaDH = 2;
```

**K6. Ai đã lập đơn, thu tiền và giao một đơn hàng, và người đó có chức vụ gì (truy trách nhiệm)** (đường: DONHANG → NHANVIEN (lập); DONHANG ⇐ THANHTOAN → NHANVIEN (xác nhận thu); DONHANG ⇐ PHIEUGIAO → NHANVIEN (giao); 1 dòng trên dữ liệu minh họa)

```sql
SELECT dh.SoDH, nl.HoLotNV AS HoLotNguoiLap, nl.TenNV AS TenNguoiLap, nl.ChucVu AS ChucVuNguoiLap,
       tt.MaTT, tt.PhuongThuc, nt.HoLotNV AS HoLotNguoiThu, nt.TenNV AS TenNguoiThu,
       pg.MaGiao, ng.HoLotNV AS HoLotNguoiGiao, ng.TenNV AS TenNguoiGiao, ng.ChucVu AS ChucVuNguoiGiao
FROM DONHANG dh
LEFT JOIN NHANVIEN nl ON nl.MaNV = dh.MaNV
LEFT JOIN THANHTOAN tt ON tt.MaDH = dh.MaDH
LEFT JOIN NHANVIEN nt ON nt.MaNV = tt.MaNV
LEFT JOIN PHIEUGIAO pg ON pg.MaDH = dh.MaDH
LEFT JOIN NHANVIEN ng ON ng.MaNV = pg.MaNV
WHERE dh.SoDH = 'DH-0002';
```

**K7. Các khoản hoàn tiền trong tháng 10/2026: ai duyệt, ai chi tiền** (đường: KHOANHOAN → NHANVIEN (người duyệt, cột MaNV); KHOANHOAN → NHANVIEN (người chi, cột MaNVChi); 2 dòng trên dữ liệu minh họa)

```sql
SELECT kc.MaHoan, kc.SoTienHoan, kc.ThoiDiemDuyetHoan, nd.HoLotNV AS HoLotNguoiDuyet, nd.TenNV AS TenNguoiDuyet,
       kc.ThoiDiemChi, nc.HoLotNV AS HoLotNguoiChi, nc.TenNV AS TenNguoiChi
FROM KHOANHOAN kc
JOIN NHANVIEN nd ON nd.MaNV = kc.MaNV
LEFT JOIN NHANVIEN nc ON nc.MaNV = kc.MaNVChi
WHERE kc.ThoiDiemDuyetHoan >= '2026-10-01' AND kc.ThoiDiemDuyetHoan < '2026-11-01'
ORDER BY kc.ThoiDiemDuyetHoan;
```

**K8. Danh sách nhân viên còn làm việc theo chức vụ** (đường: NHANVIEN (tra theo thuộc tính ChucVu, không nối quan hệ khác); 7 dòng trên dữ liệu minh họa)

```sql
SELECT nv.ChucVu, nv.MaNV, nv.HoLotNV, nv.TenNV, nv.NgayVaoLam
FROM NHANVIEN nv
WHERE nv.TinhTrangNV = 'Đang làm'
ORDER BY nv.ChucVu, nv.MaNV;
```

**K9. Phiếu bảo hành đã quá ngày hẹn trả mà chưa trả khách, kèm khách cần liên hệ** (đường: PHIEUBAOHANH → CHITIETDONHANG → DONHANG → KHACHHANG; 1 dòng trên dữ liệu minh họa)

```sql
SELECT bh.MaPhieuBH, bh.NgayNhan, bh.NgayHenTra, bh.TinhTrangBH, ct.TenHangChot, dh.SoDH, kh.HoLotKH, kh.TenKH, kh.SDTKH
FROM PHIEUBAOHANH bh
JOIN CHITIETDONHANG ct ON ct.MaDH = bh.MaDH AND ct.SoDongDH = bh.SoDongDH
JOIN DONHANG dh ON dh.MaDH = ct.MaDH
LEFT JOIN KHACHHANG kh ON kh.MaKH = dh.MaKH
WHERE bh.NgayTraThucTe IS NULL AND bh.NgayHenTra < '2026-11-01'
ORDER BY bh.NgayHenTra;
```

Ghi chú: K3 quy ước chiều biến động theo LoaiBienDong (Nhập và Nhận lại làm tăng; Xuất bán làm giảm; Chuyển nhóm cần thêm nhóm đích nên chưa tính); quy ước dấu của sổ kho chưa chốt với cửa hàng và là điểm cần xác nhận.

## 3.4 NGÕ VÀO TRA CỨU VÀ CHỈ MỤC ĐỀ XUẤT

Giáo trình Bài 9 nhấn mạnh phép kết là thao tác chính và cần chỉ mục cho cột nối. Hai nhóm chỉ mục đề xuất, suy từ đồ thị:

1. **Ngõ vào tra cứu theo khóa riêng** (người dùng cung cấp giá trị): đã có chỉ mục tự động từ UNIQUE: SKU (MATHANG), SoDH (DONHANG), SoPhieu (PHIEUNHAP), CodeMG (MAGIAMGIA), (MaSP, SoSeri) (SERIMATHANG), (MaSP, ViTriAnh) (ANHMATHANG), MaDH (PHIEUGIAO), TenDangNhap, MaKH, MaNV (TAIKHOAN). Cần thêm chỉ mục tìm khách theo SDTKH và nhân viên theo tên (TenKH, TenNV).
2. **Cột khóa ngoại của cung** nên có chỉ mục để phép nối theo chiều ngược (từ cha xuống n con) nhanh: DONHANG(MaKH), DONHANG(MaNV), CHITIETDONHANG(MaSP), THANHTOAN(MaDH), HOSODOITRA(MaDH), KHOANHOAN(MaTT), KHOANHOAN(MaHS), LANNHANLAI(MaHS), GIAODICHKHO(MaSP, ThoiDiemGD), PHIEUBAOHANH(MaDH, SoDongDH), HANGCOSERI(MaDH, SoDongDH), HANGCOSERI(MaPN, SoDongPN), và các khóa ngoại phụ tới NHANVIEN (MaNVDuyet, MaNVChi, MaNVThu, MaNVXacNhan) để tra “một nhân viên đã duyệt, chi, thu những gì”.

Khẳng định tốc độ cần đo trên dữ liệu thật; báo cáo chưa đo hiệu năng.

