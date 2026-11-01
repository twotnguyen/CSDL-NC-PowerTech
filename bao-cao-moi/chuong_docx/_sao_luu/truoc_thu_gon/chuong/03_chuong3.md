# CHƯƠNG 3: KẾT QUẢ THỰC NGHIỆM

Chương này biểu diễn lược đồ sau cải tiến (32 quan hệ, mục 2.3.6) thành đồ thị quan hệ theo thuật toán B1–B7 của giáo trình, nêu các con đường truy xuất và ngữ nghĩa của từng con đường, rồi viết truy vấn SQL cho các con đường đó. Phép tính do `tools/dothi.py` đối chiếu; các truy vấn đều đã chạy thử trên dữ liệu minh họa nhỏ (`sql/02_du_lieu_minh_hoa.sql`, 32 bảng, không vi phạm khóa ngoại) và đều trả về ít nhất một dòng, trừ đường rỗng đúng quy tắc nêu ở mục 3.2.3.

## 3.1 ĐỒ THỊ QUAN HỆ

**Quy ước áp dụng** (giáo trình cho phép nhiều đồ thị cho cùng một lược đồ; mục 10.4):

- **Q1.** Mỗi quan hệ dùng khóa chính làm khóa ưu tiên (giáo trình 10.4.2: khi cài đặt chọn một khóa ưu tiên).
- **Q2.** Hai cột là cùng một thuộc tính khi nối nhau bằng khóa ngoại, **trừ** khóa ngoại tới NHANVIEN không thuộc khóa chính: nhân viên lập đơn, xác nhận thu, giao hàng, nhập hàng… là các vai trò khác nhau của cùng một người nên mỗi cung vai trò được giữ riêng, không bị coi là thừa. Khóa ngoại **phụ** tới NHANVIEN có tên khác MaNV (MaNVThu, MaNVXacNhan, MaNVDuyet, MaNVChi, MaNVPhanCong) ghi thêm một vai trò nữa của nhân viên trên cùng quan hệ; chúng cùng đích với cung của MaNV (hoặc đã có cung tới NHANVIEN) nên không vẽ thành cung song song, và được truy xuất bằng cách nối thêm cột đó (ví dụ truy vấn K7).
- **Q3.** Cung A → B bị coi là thừa (PTH_Thừa) khi B đạt được qua cung A → H mà đường đó bắt buộc (không rỗng), hoặc khóa của B nằm trong khóa của H.
- **Q4.** Khuyên (cung từ một nút về chính nó) là liên kết loại hàng cha – con (MaLoaiCha); nằm ngoài thuật toán.

**Bước 1: Biến C thành phân rã đồng nhất C_d.** Hai quan hệ có khóa tương hỗ thì gộp thành một nút. HANGCOSERI và SERIMATHANG đều có khóa {MaSeri} nên gộp; quan hệ gộp là HANGCOSERI(MaSeri, SoSeri, MaSP, MaPN, SoDongPN, MaDH, SoDongDH, TinhTrangSeri, ThoiDiemNhap), tức hình dạng ban đầu của quan hệ này. Các quan hệ còn lại giữ nguyên: **31 nút**.

**Bước 2: Tạo nút và quan hệ nút.** Mỗi quan hệ là một nút Nᵢ với Q_Nᵢ = Qᵢ:

(Q1) LOAIHANG(MaLoai, TenLoai, MoTaLoai, MaLoaiCha).
(Q2) THUONGHIEU(MaTH, TenTH, MoTaTH).
(Q3) MATHANG(MaSP, SKU, TenSP, MoTaSP, GiaNiemYet, GiaKhuyenMai, ThoiHanBH, TinhTrangKD, CoSeri, MaLoai, MaTH).
(Q4) ANHMATHANG(MaAnh, MaSP, ViTriAnh, DuongDanAnh, LaAnhChinh).
(Q5) DINHNGHIATHONGSO(MaTS, MaLoai, TenTS, KieuGiaTri, DonViTS, BatBuoc).
(Q6) GIATRITHONGSO(MaSP, MaTS, GiaTriTS).
(Q7) KHACHHANG(MaKH, HoLotKH, TenKH, SDTKH, EmailKH, MaSoThueKH).
(Q8) DIACHIKHACH(MaDC, MaKH, TenNguoiNhanDC, SDTNhanDC, DiaChiChiTiet, LaMacDinh).
(Q9) NHANVIEN(MaNV, HoLotNV, TenNV, SDTNV, EmailNV, NgayVaoLam, NgayNghiViec, TinhTrangNV).
(Q10) VAITRO(MaVT, TenVT, MoTaVT).
(Q11) GIUVAITRO(MaNV, MaVT, NgayBatDauVT, NgayKetThucVT, MaNVPhanCong).
(Q12) TAIKHOAN(MaTK, TenDangNhap, MatKhauBam, TinhTrangTK, ThoiDiemTaoTK, MaKH, MaNV).
(Q13) NHACUNGCAP(MaNCC, TenNCC, NguoiLienHeNCC, SDTNCC, DiaChiNCC, MaSoThueNCC, TinhTrangHT).
(Q14) GIOHANG(MaGio, MaTK, ThoiDiemTaoGio, ThoiDiemCapNhatGio, TinhTrangGio).
(Q15) CHITIETGIOHANG(MaGio, MaSP, SoLuongGio, ThoiDiemThemGio).
(Q16) MAGIAMGIA(MaMG, CodeMG, TenChuongTrinh, LoaiGiam, MucGiam, DonToiThieu, GiamToiDa, NgayBatDau, NgayKetThuc, GioiHanLuot, MaNV).
(Q17) DONHANG(MaDH, SoDH, ThoiDiemLap, KenhBan, MaKH, MaNV, TenNguoiNhan, SDTNhan, DiaChiGiao, PhiGiao, GiamGia, MaMG, TinhTrangDH, DieuKienCoc, GhiChuDH).
(Q18) CHITIETDONHANG(MaDH, SoDongDH, MaSP, SoLuongBan, DonGiaChot, TenHangChot, SKUChot).
(Q19) NHATKYDONHANG(MaDH, SoLanDoi, TinhTrangMoi, ThoiDiemDoi, MaNV, LyDoDoi).
(Q20) THANHTOAN(MaTT, MaDH, LoaiKhoan, PhuongThuc, SoTien, ThoiDiemTT, KetQuaTT, MaGiaoDichNgoai, DonViThanhToan, MaNV, MaNVThu).
(Q21) PHIEUGIAO(MaGiao, MaDH, MaNV, ThoiDiemXuat, TinhTrangGiao).
(Q22) LANGIAO(MaGiao, SoLan, ThoiDiemGiao, KetQuaGiao, LyDoThatBai, MaNV).
(Q23) PHIEUNHAP(MaPN, SoPhieu, MaNCC, MaNV, ThoiDiemNhan, TinhTrangPN, MaNVXacNhan, ThoiDiemXacNhan, SoHoaDonNCC, GhiChuPN).
(Q24) CHITIETPHIEUNHAP(MaPN, SoDongPN, MaSP, SoLuongNhap, GiaNhap).
(Q25) HANGCOSERI(MaSeri, MaPN, SoDongPN, MaDH, SoDongDH, TinhTrangSeri, ThoiDiemNhap, SoSeri, MaSP).
(Q26) GIAODICHKHO(MaGDK, MaSP, NhomKho, LoaiBienDong, SoLuongGD, ThoiDiemGD, MaNV, LoaiChungTu, MaChungTu, GhiChuGD).
(Q27) HOSODOITRA(MaHS, MaDH, MaNV, NgayDeNghi, LoaiTruongHop, LyDoDoiTra, TinhTrangHS, HinhThucXuLy).
(Q28) CHITIETTRA(MaHS, SoDongDH, SoLuongTra, MaSeri).
(Q29) LANNHANLAI(MaNhanLai, MaHS, ThoiDiemNhanLai, MaNV, KetLuan, NhomSauKiemTra, ThoiDiemDuyet, MaNVDuyet).
(Q30) KHOANHOAN(MaHoan, MaTT, MaHS, MaNV, SoTienHoan, PhuongThucHoan, ThoiDiemDuyetHoan, ThoiDiemChi, MaNVChi).
(Q31) PHIEUBAOHANH(MaPhieuBH, MaSeri, MaDH, SoDongDH, MoTaLoi, PhuKienDiKem, NgayNhan, NgayHenTra, NgayTraThucTe, TinhTrangBH, KetQuaBH, LyDoTuChoi, MaNV).

**Bước 3: Tạo nút bản lề và quan hệ nút bản lề.** Xét giao Q_ij = Qᵢ ∩ Qⱼ của mọi cặp nút; có 84 cặp có giao khác rỗng. Nếu khóa của Q_ij là khóa của một quan hệ nào đó thì không tạo nút bản lề (bảng 3.1).

| Qᵢ ∩ Qⱼ | Giao | Khóa của giao | Trùng khóa của | Kết luận |
|---|---|---|---|---|
| Q1 ∩ Q3 | {MaLoai} | {MaLoai} | Q1 | không tạo |
| Q1 ∩ Q5 | {MaLoai} | {MaLoai} | Q1 | không tạo |
| Q2 ∩ Q3 | {MaTH} | {MaTH} | Q2 | không tạo |
| Q3 ∩ Q4 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q3 ∩ Q5 | {MaLoai} | {MaLoai} | Q1 | không tạo |
| Q3 ∩ Q6 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q3 ∩ Q15 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q3 ∩ Q18 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q3 ∩ Q24 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q3 ∩ Q25 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q3 ∩ Q26 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q4 ∩ Q6 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q4 ∩ Q15 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q4 ∩ Q18 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q4 ∩ Q24 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q4 ∩ Q25 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q4 ∩ Q26 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q5 ∩ Q6 | {MaTS} | {MaTS} | Q5 | không tạo |
| Q6 ∩ Q15 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q6 ∩ Q18 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q6 ∩ Q24 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q6 ∩ Q25 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q6 ∩ Q26 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q7 ∩ Q8 | {MaKH} | {MaKH} | Q7 | không tạo |
| Q7 ∩ Q12 | {MaKH} | {MaKH} | Q7 | không tạo |
| Q7 ∩ Q17 | {MaKH} | {MaKH} | Q7 | không tạo |
| Q8 ∩ Q12 | {MaKH} | {MaKH} | Q7 | không tạo |
| Q8 ∩ Q17 | {MaKH} | {MaKH} | Q7 | không tạo |
| Q9 ∩ Q11 | {MaNV} | {MaNV} | Q9 | không tạo |
| Q10 ∩ Q11 | {MaVT} | {MaVT} | Q10 | không tạo |
| Q12 ∩ Q14 | {MaTK} | {MaTK} | Q12 | không tạo |
| Q12 ∩ Q17 | {MaKH} | {MaKH} | Q7 | không tạo |
| Q13 ∩ Q23 | {MaNCC} | {MaNCC} | Q13 | không tạo |
| Q14 ∩ Q15 | {MaGio} | {MaGio} | Q14 | không tạo |
| Q15 ∩ Q18 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q15 ∩ Q24 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q15 ∩ Q25 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q15 ∩ Q26 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q16 ∩ Q17 | {MaMG} | {MaMG} | Q16 | không tạo |
| Q17 ∩ Q18 | {MaDH} | {MaDH} | Q17 | không tạo |
| Q17 ∩ Q19 | {MaDH} | {MaDH} | Q17 | không tạo |
| Q17 ∩ Q20 | {MaDH} | {MaDH} | Q17 | không tạo |
| Q17 ∩ Q21 | {MaDH} | {MaDH} | Q17 | không tạo |
| Q17 ∩ Q25 | {MaDH} | {MaDH} | Q17 | không tạo |
| Q17 ∩ Q27 | {MaDH} | {MaDH} | Q17 | không tạo |
| Q17 ∩ Q31 | {MaDH} | {MaDH} | Q17 | không tạo |
| Q18 ∩ Q19 | {MaDH} | {MaDH} | Q17 | không tạo |
| Q18 ∩ Q20 | {MaDH} | {MaDH} | Q17 | không tạo |
| Q18 ∩ Q21 | {MaDH} | {MaDH} | Q17 | không tạo |
| Q18 ∩ Q24 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q18 ∩ Q25 | {MaDH, MaSP, SoDongDH} | {MaDH, SoDongDH} | Q18 | không tạo |
| Q18 ∩ Q25 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q18 ∩ Q26 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q18 ∩ Q27 | {MaDH} | {MaDH} | Q17 | không tạo |
| Q18 ∩ Q31 | {MaDH, SoDongDH} | {MaDH, SoDongDH} | Q18 | không tạo |
| Q19 ∩ Q20 | {MaDH} | {MaDH} | Q17 | không tạo |
| Q19 ∩ Q21 | {MaDH} | {MaDH} | Q17 | không tạo |
| Q19 ∩ Q25 | {MaDH} | {MaDH} | Q17 | không tạo |
| Q19 ∩ Q27 | {MaDH} | {MaDH} | Q17 | không tạo |
| Q19 ∩ Q31 | {MaDH} | {MaDH} | Q17 | không tạo |
| Q20 ∩ Q21 | {MaDH} | {MaDH} | Q17 | không tạo |
| Q20 ∩ Q25 | {MaDH} | {MaDH} | Q17 | không tạo |
| Q20 ∩ Q27 | {MaDH} | {MaDH} | Q17 | không tạo |
| Q20 ∩ Q30 | {MaTT} | {MaTT} | Q20 | không tạo |
| Q20 ∩ Q31 | {MaDH} | {MaDH} | Q17 | không tạo |
| Q21 ∩ Q22 | {MaGiao} | {MaGiao} | Q21 | không tạo |
| Q21 ∩ Q25 | {MaDH} | {MaDH} | Q17 | không tạo |
| Q21 ∩ Q27 | {MaDH} | {MaDH} | Q17 | không tạo |
| Q21 ∩ Q31 | {MaDH} | {MaDH} | Q17 | không tạo |
| Q23 ∩ Q24 | {MaPN} | {MaPN} | Q23 | không tạo |
| Q23 ∩ Q25 | {MaPN} | {MaPN} | Q23 | không tạo |
| Q24 ∩ Q25 | {MaPN, MaSP, SoDongPN} | {MaPN, SoDongPN} | Q24 | không tạo |
| Q24 ∩ Q25 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q24 ∩ Q26 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q25 ∩ Q26 | {MaSP} | {MaSP} | Q3 | không tạo |
| Q25 ∩ Q27 | {MaDH} | {MaDH} | Q17 | không tạo |
| Q25 ∩ Q28 | {MaSeri} | {MaSeri} | Q25 | không tạo |
| Q25 ∩ Q31 | {MaDH, MaSeri, SoDongDH} | {MaSeri} | Q25 | không tạo |
| Q25 ∩ Q31 | {MaDH, SoDongDH} | {MaDH, SoDongDH} | Q18 | không tạo |
| Q27 ∩ Q28 | {MaHS} | {MaHS} | Q27 | không tạo |
| Q27 ∩ Q29 | {MaHS} | {MaHS} | Q27 | không tạo |
| Q27 ∩ Q30 | {MaHS} | {MaHS} | Q27 | không tạo |
| Q27 ∩ Q31 | {MaDH} | {MaDH} | Q17 | không tạo |
| Q28 ∩ Q29 | {MaHS} | {MaHS} | Q27 | không tạo |
| Q28 ∩ Q30 | {MaHS} | {MaHS} | Q27 | không tạo |
| Q28 ∩ Q31 | {MaSeri} | {MaSeri} | Q25 | không tạo |
| Q29 ∩ Q30 | {MaHS} | {MaHS} | Q27 | không tạo |

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
| 8. DIACHIKHACH | 7 | – | – | – | 7 |
| 9. NHANVIEN | – | – | – | – | – |
| 10. VAITRO | – | – | – | – | – |
| 11. GIUVAITRO | 9, 10 | – | 9, 10 | – | 9, 10 |
| 12. TAIKHOAN | 7, 9 | – | – | – | 7, 9 |
| 13. NHACUNGCAP | – | – | – | – | – |
| 14. GIOHANG | 12 | – | – | – | 12 |
| 15. CHITIETGIOHANG | 3, 14 | – | 3, 14 | – | 3, 14 |
| 16. MAGIAMGIA | 9 | – | – | – | 9 |
| 17. DONHANG | 7, 9, 16 | – | – | – | 7, 9, 16 |
| 18. CHITIETDONHANG | 3, 17 | – | 17 | – | 3, 17 |
| 19. NHATKYDONHANG | 9, 17 | – | 17 | – | 9, 17 |
| 20. THANHTOAN | 9, 17 | – | – | – | 9, 17 |
| 21. PHIEUGIAO | 9, 17 | – | – | – | 9, 17 |
| 22. LANGIAO | 9, 21 | – | 21 | – | 9, 21 |
| 23. PHIEUNHAP | 9, 13 | – | – | – | 9, 13 |
| 24. CHITIETPHIEUNHAP | 3, 23 | – | 23 | – | 3, 23 |
| 25. HANGCOSERI | 3, 17, 18, 23, 24 | 3, 17, 23 | – | – | 18, 24 |
| 26. GIAODICHKHO | 3, 9 | – | – | – | 3, 9 |
| 27. HOSODOITRA | 9, 17 | – | – | – | 9, 17 |
| 28. CHITIETTRA | 25, 27 | – | 27 | – | 25, 27 |
| 29. LANNHANLAI | 9, 27 | – | – | – | 9, 27 |
| 30. KHOANHOAN | 9, 20, 27 | – | – | – | 9, 20, 27 |
| 31. PHIEUBAOHANH | 9, 17, 18, 25 | 17 | – | – | 9, 18, 25 |

*Bảng 3.2: Tập cung của từng nút*

Từ bảng trên, mỗi nút Nⱼ ∈ Cung(Nᵢ) cho một cung có hướng cᵢⱼ từ Nᵢ đến Nⱼ với quan hệ cung Qᵢⱼ = Qᵢ[KQᵢ ∪ KQⱼ]. Có tất cả **49 quan hệ cung** (kể cả khuyên của LOAIHANG và các cung vai trò tới NHANVIEN):

| Cung | Quan hệ cung Qᵢⱼ | Bản số xuôi (m, A, M) | Bản số ngược (m, A, M) |
|---|---|---|---|
| Q3.1: MATHANG → LOAIHANG | MATHANG(MaSP, MaLoai) | (1, 1, 1) | (0, -, n) |
| Q3.2: MATHANG → THUONGHIEU | MATHANG(MaSP, MaTH) | (1, 1, 1) | (0, -, n) |
| Q4.3: ANHMATHANG → MATHANG | ANHMATHANG(MaAnh, MaSP) | (1, 1, 1) | (0, -, n) |
| Q5.1: DINHNGHIATHONGSO → LOAIHANG | DINHNGHIATHONGSO(MaTS, MaLoai) | (1, 1, 1) | (0, -, n) |
| Q6.3: GIATRITHONGSO → MATHANG | GIATRITHONGSO(MaSP, MaTS) | (1, 1, 1) | (0, -, n) |
| Q6.5: GIATRITHONGSO → DINHNGHIATHONGSO | GIATRITHONGSO(MaSP, MaTS) | (1, 1, 1) | (0, -, n) |
| Q8.7: DIACHIKHACH → KHACHHANG | DIACHIKHACH(MaDC, MaKH) | (1, 1, 1) | (0, -, n) |
| Q11.9: GIUVAITRO → NHANVIEN | GIUVAITRO(MaNV, MaVT, NgayBatDauVT) | (1, 1, 1) | (0, -, n) |
| Q11.10: GIUVAITRO → VAITRO | GIUVAITRO(MaNV, MaVT, NgayBatDauVT) | (1, 1, 1) | (0, -, n) |
| Q12.7: TAIKHOAN → KHACHHANG | TAIKHOAN(MaTK, MaKH) | (0, -, 1) | (0, -, 1) |
| Q12.9: TAIKHOAN → NHANVIEN | TAIKHOAN(MaTK, MaNV) | (0, -, 1) | (0, -, 1) |
| Q14.12: GIOHANG → TAIKHOAN | GIOHANG(MaGio, MaTK) | (1, 1, 1) | (0, -, n) |
| Q15.3: CHITIETGIOHANG → MATHANG | CHITIETGIOHANG(MaGio, MaSP) | (1, 1, 1) | (0, -, n) |
| Q15.14: CHITIETGIOHANG → GIOHANG | CHITIETGIOHANG(MaGio, MaSP) | (1, 1, 1) | (0, -, n) |
| Q16.9: MAGIAMGIA → NHANVIEN | MAGIAMGIA(MaMG, MaNV) | (1, 1, 1) | (0, -, n) |
| Q17.7: DONHANG → KHACHHANG | DONHANG(MaDH, MaKH) | (0, -, 1) | (0, -, n) |
| Q17.9: DONHANG → NHANVIEN | DONHANG(MaDH, MaNV) | (0, -, 1) | (0, -, n) |
| Q17.16: DONHANG → MAGIAMGIA | DONHANG(MaDH, MaMG) | (0, -, 1) | (0, -, n) |
| Q18.3: CHITIETDONHANG → MATHANG | CHITIETDONHANG(MaDH, SoDongDH, MaSP) | (1, 1, 1) | (0, -, n) |
| Q18.17: CHITIETDONHANG → DONHANG | CHITIETDONHANG(MaDH, SoDongDH) | (1, 1, 1) | (1, -, n) |
| Q19.9: NHATKYDONHANG → NHANVIEN | NHATKYDONHANG(MaDH, SoLanDoi, MaNV) | (0, -, 1) | (0, -, n) |
| Q19.17: NHATKYDONHANG → DONHANG | NHATKYDONHANG(MaDH, SoLanDoi) | (1, 1, 1) | (0, -, n) |
| Q20.9: THANHTOAN → NHANVIEN | THANHTOAN(MaTT, MaNV) | (0, -, 1) | (0, -, n) |
| Q20.17: THANHTOAN → DONHANG | THANHTOAN(MaTT, MaDH) | (1, 1, 1) | (0, -, n) |
| Q21.9: PHIEUGIAO → NHANVIEN | PHIEUGIAO(MaGiao, MaNV) | (1, 1, 1) | (0, -, n) |
| Q21.17: PHIEUGIAO → DONHANG | PHIEUGIAO(MaGiao, MaDH) | (1, 1, 1) | (0, -, 1) |
| Q22.9: LANGIAO → NHANVIEN | LANGIAO(MaGiao, SoLan, MaNV) | (1, 1, 1) | (0, -, n) |
| Q22.21: LANGIAO → PHIEUGIAO | LANGIAO(MaGiao, SoLan) | (1, 1, 1) | (0, -, 3) |
| Q23.9: PHIEUNHAP → NHANVIEN | PHIEUNHAP(MaPN, MaNV) | (1, 1, 1) | (0, -, n) |
| Q23.13: PHIEUNHAP → NHACUNGCAP | PHIEUNHAP(MaPN, MaNCC) | (1, 1, 1) | (0, -, n) |
| Q24.3: CHITIETPHIEUNHAP → MATHANG | CHITIETPHIEUNHAP(MaPN, SoDongPN, MaSP) | (1, 1, 1) | (0, -, n) |
| Q24.23: CHITIETPHIEUNHAP → PHIEUNHAP | CHITIETPHIEUNHAP(MaPN, SoDongPN) | (1, 1, 1) | (1, -, n) |
| Q25.18: HANGCOSERI → CHITIETDONHANG | HANGCOSERI(MaSeri, MaDH, SoDongDH) | (0, -, 1) | (0, -, n) |
| Q25.24: HANGCOSERI → CHITIETPHIEUNHAP | HANGCOSERI(MaSeri, MaPN, SoDongPN) | (1, 1, 1) | (0, -, n) |
| Q26.3: GIAODICHKHO → MATHANG | GIAODICHKHO(MaGDK, MaSP) | (1, 1, 1) | (0, -, n) |
| Q26.9: GIAODICHKHO → NHANVIEN | GIAODICHKHO(MaGDK, MaNV) | (0, -, 1) | (0, -, n) |
| Q27.9: HOSODOITRA → NHANVIEN | HOSODOITRA(MaHS, MaNV) | (1, 1, 1) | (0, -, n) |
| Q27.17: HOSODOITRA → DONHANG | HOSODOITRA(MaHS, MaDH) | (1, 1, 1) | (0, -, n) |
| Q28.25: CHITIETTRA → HANGCOSERI | CHITIETTRA(MaHS, SoDongDH, MaSeri) | (0, -, 1) | (0, -, n) |
| Q28.27: CHITIETTRA → HOSODOITRA | CHITIETTRA(MaHS, SoDongDH) | (1, 1, 1) | (1, -, n) |
| Q29.9: LANNHANLAI → NHANVIEN | LANNHANLAI(MaNhanLai, MaNV) | (0, -, 1) | (0, -, n) |
| Q29.27: LANNHANLAI → HOSODOITRA | LANNHANLAI(MaNhanLai, MaHS) | (1, 1, 1) | (0, -, n) |
| Q30.9: KHOANHOAN → NHANVIEN | KHOANHOAN(MaHoan, MaNV) | (1, 1, 1) | (0, -, n) |
| Q30.20: KHOANHOAN → THANHTOAN | KHOANHOAN(MaHoan, MaTT) | (1, 1, 1) | (0, -, n) |
| Q30.27: KHOANHOAN → HOSODOITRA | KHOANHOAN(MaHoan, MaHS) | (0, -, 1) | (0, -, n) |
| Q31.9: PHIEUBAOHANH → NHANVIEN | PHIEUBAOHANH(MaPhieuBH, MaNV) | (1, 1, 1) | (0, -, n) |
| Q31.18: PHIEUBAOHANH → CHITIETDONHANG | PHIEUBAOHANH(MaPhieuBH, MaDH, SoDongDH) | (1, 1, 1) | (0, -, n) |
| Q31.25: PHIEUBAOHANH → HANGCOSERI | PHIEUBAOHANH(MaPhieuBH, MaSeri) | (0, -, 1) | (0, -, n) |
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
| DIACHIKHACH | DIACHIKHACH(MaDC, TenNguoiNhanDC, SDTNhanDC, DiaChiChiTiet, LaMacDinh) | MaKH |
| TAIKHOAN | TAIKHOAN(MaTK, TenDangNhap, MatKhauBam, TinhTrangTK, ThoiDiemTaoTK) | MaKH, MaNV |
| GIOHANG | GIOHANG(MaGio, ThoiDiemTaoGio, ThoiDiemCapNhatGio, TinhTrangGio) | MaTK |
| MAGIAMGIA | MAGIAMGIA(MaMG, CodeMG, TenChuongTrinh, LoaiGiam, MucGiam, DonToiThieu, GiamToiDa, NgayBatDau, NgayKetThuc, GioiHanLuot) | MaNV |
| DONHANG | DONHANG(MaDH, SoDH, ThoiDiemLap, KenhBan, TenNguoiNhan, SDTNhan, DiaChiGiao, PhiGiao, GiamGia, TinhTrangDH, DieuKienCoc, GhiChuDH) | MaKH, MaNV, MaMG |
| CHITIETDONHANG | CHITIETDONHANG(MaDH, SoDongDH, SoLuongBan, DonGiaChot, TenHangChot, SKUChot) | MaSP |
| NHATKYDONHANG | NHATKYDONHANG(MaDH, SoLanDoi, TinhTrangMoi, ThoiDiemDoi, LyDoDoi) | MaNV |
| THANHTOAN | THANHTOAN(MaTT, LoaiKhoan, PhuongThuc, SoTien, ThoiDiemTT, KetQuaTT, MaGiaoDichNgoai, DonViThanhToan, MaNVThu) | MaNV, MaDH |
| PHIEUGIAO | PHIEUGIAO(MaGiao, ThoiDiemXuat, TinhTrangGiao) | MaNV, MaDH |
| LANGIAO | LANGIAO(MaGiao, SoLan, ThoiDiemGiao, KetQuaGiao, LyDoThatBai) | MaNV |
| PHIEUNHAP | PHIEUNHAP(MaPN, SoPhieu, ThoiDiemNhan, TinhTrangPN, MaNVXacNhan, ThoiDiemXacNhan, SoHoaDonNCC, GhiChuPN) | MaNV, MaNCC |
| CHITIETPHIEUNHAP | CHITIETPHIEUNHAP(MaPN, SoDongPN, SoLuongNhap, GiaNhap) | MaSP |
| HANGCOSERI | HANGCOSERI(MaSeri, TinhTrangSeri, ThoiDiemNhap, SoSeri, MaSP) | MaDH, SoDongDH, MaPN, SoDongPN |
| GIAODICHKHO | GIAODICHKHO(MaGDK, NhomKho, LoaiBienDong, SoLuongGD, ThoiDiemGD, LoaiChungTu, MaChungTu, GhiChuGD) | MaSP, MaNV |
| HOSODOITRA | HOSODOITRA(MaHS, NgayDeNghi, LoaiTruongHop, LyDoDoiTra, TinhTrangHS, HinhThucXuLy) | MaNV, MaDH |
| CHITIETTRA | CHITIETTRA(MaHS, SoDongDH, SoLuongTra) | MaSeri |
| LANNHANLAI | LANNHANLAI(MaNhanLai, ThoiDiemNhanLai, KetLuan, NhomSauKiemTra, ThoiDiemDuyet, MaNVDuyet) | MaNV, MaHS |
| KHOANHOAN | KHOANHOAN(MaHoan, SoTienHoan, PhuongThucHoan, ThoiDiemDuyetHoan, ThoiDiemChi, MaNVChi) | MaNV, MaTT, MaHS |
| PHIEUBAOHANH | PHIEUBAOHANH(MaPhieuBH, MoTaLoi, PhuKienDiKem, NgayNhan, NgayHenTra, NgayTraThucTe, TinhTrangBH, KetQuaBH, LyDoTuChoi) | MaNV, MaDH, SoDongDH, MaSeri |

**Bước 7: Tạo cung vô hướng.** Không có nút Nₖ nào thỏa điều kiện (quan hệ chỉ gồm thuộc tính khóa, có đúng hai cung ra và không có cung vào): quan hệ nối n–n của lược đồ đều có thuộc tính riêng (GIATRITHONGSO có GiaTriTS; CHITIET* có số lượng, giá). Vì vậy không có cung vô hướng và đồ thị quan hệ chỉ có cung có hướng (hình 3.1).

![Hình 3.1: Đồ thị quan hệ của PowerTech (nút viền đậm là nút vào)](hinh/do_thi_quan_he.png)

*Hình 3.1: Đồ thị quan hệ (31 nút, 49 cung; cung xám là cung vai trò tới NHANVIEN; nút viền đậm là nút vào)*

Hình 3.1 chỉ ghi số thứ tự nút (tên nút ở bảng 3.2). Hình 3.2 vẽ cùng đồ thị nhưng ghi tên quan hệ để dễ đối chiếu.

![Hình 3.2: Đồ thị quan hệ có tên nút](hinh/do_thi_quan_he_ten.png)

*Hình 3.2: Đồ thị quan hệ có tên nút (cùng đồ thị với hình 3.1)*

**Nhận xét về đồ thị.** (1) Có nút đạt được bằng hai mạch đi khác nhau, làm lộ ràng buộc nhất quán: từ PHIEUBAOHANH tới CHITIETDONHANG có mạch trực tiếp và mạch qua HANGCOSERI (chiếc hàng bảo hành phải thuộc đúng dòng đơn đã mua); từ KHOANHOAN tới DONHANG có mạch qua THANHTOAN và mạch qua HOSODOITRA (hai mạch phải cùng một đơn). Đó là ràng buộc 2 và 4 ở mục 2.3.6. (2) CHITIETTRA chỉ nối với HOSODOITRA và HANGCOSERI; dòng đơn được trả là (HOSODOITRA.MaDH, SoDongDH) nên đường từ dòng trả tới dòng đơn đi qua HOSODOITRA và cần cả MaDH lẫn SoDongDH, không phải một cung đơn. (3) NHANVIEN là nút đích của nhiều cung vai trò (lập đơn, xác nhận thu, giao, nhập, tạo mã, tài khoản, đổi tình trạng đơn…): đó là các con đường **truy trách nhiệm** từ chứng từ về người thực hiện; kết hợp với GIUVAITRO cho biết người đó giữ vai trò gì vào lúc làm (truy vấn K6–K8). (4) Đồ thị không duy nhất: chọn khóa ưu tiên khác (ví dụ SoDH cho DONHANG) cho đồ thị khác nhưng tương đương về bảo toàn thông tin và PTH.

## 3.2 Ý NGHĨA CÁC CON ĐƯỜNG TRUY XUẤT

### 3.2.1 Nút vào

Theo giáo trình, nút vào là nút mà người dùng cung cấp giá trị khóa để truy xuất trực tiếp một bộ. Để liệt kê các con đường nhiều ngữ nghĩa nhất, chương này chọn **nút vào là các nút không có cung đi tới** (không quan hệ nào trỏ về nó bằng cung có hướng), vì từ nút khác chỉ đến được các nút này bằng cách đi ngược cung (cho nhiều bộ). Có **12 nút vào**: 4. ANHMATHANG, 6. GIATRITHONGSO, 8. DIACHIKHACH, 11. GIUVAITRO, 15. CHITIETGIOHANG, 19. NHATKYDONHANG, 22. LANGIAO, 26. GIAODICHKHO, 28. CHITIETTRA, 29. LANNHANLAI, 30. KHOANHOAN, 31. PHIEUBAOHANH. Từ mỗi nút vào, mọi mạch đi theo chiều cung đến nút cuối (không lặp nút) là một con đường truy xuất; tổng cộng **66 con đường**. Các nút còn lại (KHACHHANG, DONHANG, MATHANG…) nằm trên các đường này và cũng là ngõ vào tra cứu theo khóa riêng (mục 3.4).

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
| 8 → 7 | Cho biết địa chỉ giao hàng là địa chỉ của khách hàng nào (1, 1, 1) | Từ một khách hàng cho biết các địa chỉ giao hàng của khách đó (0, -, n) |
| 11 → 9 | Cho biết lần giữ vai trò của nhân viên nào (1, 1, 1) | Từ một nhân viên cho biết các lần giữ vai trò của nhân viên đó (0, -, n) |
| 11 → 10 | Cho biết lần giữ vai trò là vai trò nào (1, 1, 1) | Từ một vai trò cho biết các lần giữ vai trò đó (0, -, n) |
| 12 → 7 | Cho biết tài khoản thuộc khách hàng nào (nếu là tài khoản khách) (0, -, 1) | Từ một khách hàng cho biết tài khoản của khách đó (tối đa một) (0, -, 1) |
| 12 → 9 | Cho biết tài khoản thuộc nhân viên nào (nếu là tài khoản nhân viên) (0, -, 1) | Từ một nhân viên cho biết tài khoản của nhân viên đó (tối đa một) (0, -, 1) |
| 14 → 12 | Cho biết giỏ hàng thuộc tài khoản nào (1, 1, 1) | Từ một tài khoản cho biết các giỏ hàng của tài khoản đó (0, -, n) |
| 15 → 3 | Cho biết dòng giỏ hàng chứa mặt hàng nào (1, 1, 1) | Từ một mặt hàng cho biết các dòng giỏ đang chứa mặt hàng đó (0, -, n) |
| 15 → 14 | Cho biết dòng giỏ hàng thuộc giỏ hàng nào (1, 1, 1) | Từ một giỏ hàng cho biết các dòng của giỏ đó (0, -, n) |
| 16 → 9 | Cho biết mã giảm giá do nhân viên nào tạo (1, 1, 1) | Từ một nhân viên cho biết các mã giảm giá do nhân viên đó tạo (0, -, n) |
| 17 → 7 | Cho biết đơn hàng do khách hàng nào đặt (nếu có hồ sơ khách) (0, -, 1) | Từ một khách hàng cho biết các đơn hàng của khách đó (0, -, n) |
| 17 → 9 | Cho biết đơn hàng do nhân viên nào lập (0, -, 1) | Từ một nhân viên cho biết các đơn hàng do nhân viên đó lập (0, -, n) |
| 17 → 16 | Cho biết đơn hàng áp dụng mã giảm giá nào (nếu có) (0, -, 1) | Từ một mã giảm giá cho biết các đơn đã dùng mã giảm giá đó (0, -, n) |
| 18 → 3 | Cho biết dòng đơn bán mặt hàng nào (1, 1, 1) | Từ một mặt hàng cho biết các dòng đơn đã bán mặt hàng đó (0, -, n) |
| 18 → 17 | Cho biết dòng đơn thuộc đơn hàng nào (1, 1, 1) | Từ một đơn hàng cho biết các dòng của đơn đó (1, -, n) |
| 19 → 9 | Cho biết lần đổi tình trạng đơn do nhân viên nào thực hiện (nếu có) (0, -, 1) | Từ một nhân viên cho biết các lần đổi tình trạng đơn do nhân viên đó thực hiện (0, -, n) |
| 19 → 17 | Cho biết lần đổi tình trạng đơn ghi tình trạng của đơn hàng nào (1, 1, 1) | Từ một đơn hàng cho biết các lần đổi tình trạng của đơn đó (0, -, n) |
| 20 → 9 | Cho biết khoản thanh toán do nhân viên nào xác nhận thu (0, -, 1) | Từ một nhân viên cho biết các khoản thu do nhân viên đó xác nhận (0, -, n) |
| 20 → 17 | Cho biết khoản thanh toán trả cho đơn hàng nào (1, 1, 1) | Từ một đơn hàng cho biết các lần thanh toán và đặt cọc của đơn đó (0, -, n) |
| 21 → 9 | Cho biết phiếu giao do nhân viên nào giao (1, 1, 1) | Từ một nhân viên cho biết các phiếu giao do nhân viên đó phụ trách (0, -, n) |
| 21 → 17 | Cho biết phiếu giao lập cho đơn hàng nào (1, 1, 1) | Từ một đơn hàng cho biết phiếu giao của đơn đó (tối đa một) (0, -, 1) |
| 22 → 9 | Cho biết lần giao hàng do nhân viên nào giao (1, 1, 1) | Từ một nhân viên cho biết các lần giao do nhân viên đó thực hiện (0, -, n) |
| 22 → 21 | Cho biết lần giao hàng thuộc phiếu giao nào (1, 1, 1) | Từ một phiếu giao cho biết các lần thử giao của phiếu đó (tối đa 3) (0, -, 3) |
| 23 → 9 | Cho biết phiếu nhập do nhân viên kho nào lập (1, 1, 1) | Từ một nhân viên cho biết các phiếu nhập do nhân viên đó lập (0, -, n) |
| 23 → 13 | Cho biết phiếu nhập nhận từ nhà cung cấp nào (1, 1, 1) | Từ một nhà cung cấp cho biết các phiếu nhập từ nhà cung cấp đó (0, -, n) |
| 24 → 3 | Cho biết dòng phiếu nhập nhập mặt hàng nào (1, 1, 1) | Từ một mặt hàng cho biết các dòng nhập của mặt hàng đó (0, -, n) |
| 24 → 23 | Cho biết dòng phiếu nhập thuộc phiếu nhập nào (1, 1, 1) | Từ một phiếu nhập cho biết các dòng của phiếu nhập đó (1, -, n) |
| 25 → 18 | Cho biết chiếc hàng có seri đã bán ở dòng đơn nào (0, -, 1) | Từ một dòng đơn cho biết các chiếc hàng có seri đã bán ở dòng đơn đó (0, -, n) |
| 25 → 24 | Cho biết chiếc hàng có seri nhập về ở dòng phiếu nhập nào (1, 1, 1) | Từ một dòng phiếu nhập cho biết các chiếc hàng có seri nhập ở dòng đó (0, -, n) |
| 26 → 3 | Cho biết giao dịch kho liên quan đến mặt hàng nào (1, 1, 1) | Từ một mặt hàng cho biết các giao dịch kho của mặt hàng đó (0, -, n) |
| 26 → 9 | Cho biết giao dịch kho do nhân viên nào thực hiện (0, -, 1) | Từ một nhân viên cho biết các giao dịch kho do nhân viên đó thực hiện (0, -, n) |
| 27 → 9 | Cho biết hồ sơ đổi trả do nhân viên nào tiếp nhận (1, 1, 1) | Từ một nhân viên cho biết các hồ sơ đổi trả do nhân viên đó tiếp nhận (0, -, n) |
| 27 → 17 | Cho biết hồ sơ đổi trả lập cho đơn hàng nào (1, 1, 1) | Từ một đơn hàng cho biết các hồ sơ đổi trả của đơn đó (0, -, n) |
| 28 → 25 | Cho biết dòng trả hàng ghi chiếc hàng có seri nào (0, -, 1) | Từ một chiếc hàng có seri cho biết các dòng trả có chiếc hàng đó (0, -, n) |
| 28 → 27 | Cho biết dòng trả hàng thuộc hồ sơ đổi trả nào (1, 1, 1) | Từ một hồ sơ đổi trả cho biết các dòng trả của hồ sơ đó (1, -, n) |
| 29 → 9 | Cho biết lần nhận lại hàng do nhân viên nào kiểm tra (0, -, 1) | Từ một nhân viên cho biết các lần nhận lại do nhân viên đó kiểm tra (0, -, n) |
| 29 → 27 | Cho biết lần nhận lại hàng thuộc hồ sơ đổi trả nào (1, 1, 1) | Từ một hồ sơ đổi trả cho biết các lần nhận lại của hồ sơ đó (0, -, n) |
| 30 → 9 | Cho biết khoản hoàn tiền do người quản lý nào duyệt (1, 1, 1) | Từ một nhân viên cho biết các khoản hoàn do người quản lý đó duyệt (0, -, n) |
| 30 → 20 | Cho biết khoản hoàn tiền tính trên khoản thanh toán nào (1, 1, 1) | Từ một khoản thanh toán cho biết các khoản hoàn của khoản thanh toán đó (0, -, n) |
| 30 → 27 | Cho biết khoản hoàn tiền theo hồ sơ đổi trả nào (nếu do đổi trả) (0, -, 1) | Từ một hồ sơ đổi trả cho biết các khoản hoàn của hồ sơ đó (0, -, n) |
| 31 → 9 | Cho biết phiếu bảo hành do nhân viên nào tiếp nhận (1, 1, 1) | Từ một nhân viên cho biết các phiếu bảo hành do nhân viên đó tiếp nhận (0, -, n) |
| 31 → 18 | Cho biết phiếu bảo hành mua ở dòng đơn nào (1, 1, 1) | Từ một dòng đơn cho biết các phiếu bảo hành của dòng đơn đó (0, -, n) |
| 31 → 25 | Cho biết phiếu bảo hành ứng với chiếc hàng có seri nào (0, -, 1) | Từ một chiếc hàng có seri cho biết các phiếu bảo hành của chiếc hàng đó (0, -, n) |
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
| 6 | 8 → 7 | Cho biết địa chỉ giao hàng là địa chỉ của khách hàng nào. | 3 |
| 7 | 11 → 9 | Cho biết lần giữ vai trò của nhân viên nào. | 10 |
| 8 | 11 → 10 | Cho biết lần giữ vai trò là vai trò nào. | 10 |
| 9 | 15 → 3 → 1 | Cho biết dòng giỏ hàng chứa mặt hàng nào; mặt hàng đó thuộc loại hàng nào. | 4 |
| 10 | 15 → 3 → 2 | Cho biết dòng giỏ hàng chứa mặt hàng nào; mặt hàng đó mang thương hiệu nào. | 4 |
| 11 | 15 → 14 → 12 → 7 | Cho biết dòng giỏ hàng thuộc giỏ hàng nào; giỏ hàng đó thuộc tài khoản nào; tài khoản đó thuộc khách hàng nào (nếu là tài khoản khách). | 4 |
| 12 | 15 → 14 → 12 → 9 | Cho biết dòng giỏ hàng thuộc giỏ hàng nào; giỏ hàng đó thuộc tài khoản nào; tài khoản đó thuộc nhân viên nào (nếu là tài khoản nhân viên). | 0 |
| 13 | 19 → 9 | Cho biết lần đổi tình trạng đơn do nhân viên nào thực hiện (nếu có). | 10 |
| 14 | 19 → 17 → 7 | Cho biết lần đổi tình trạng đơn ghi tình trạng của đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách). | 11 |
| 15 | 19 → 17 → 9 | Cho biết lần đổi tình trạng đơn ghi tình trạng của đơn hàng nào; đơn hàng đó do nhân viên nào lập. | 7 |
| 16 | 19 → 17 → 16 → 9 | Cho biết lần đổi tình trạng đơn ghi tình trạng của đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo. | 4 |
| 17 | 22 → 9 | Cho biết lần giao hàng do nhân viên nào giao. | 4 |
| 18 | 22 → 21 → 9 | Cho biết lần giao hàng thuộc phiếu giao nào; phiếu giao đó do nhân viên nào giao. | 4 |
| 19 | 22 → 21 → 17 → 7 | Cho biết lần giao hàng thuộc phiếu giao nào; phiếu giao đó lập cho đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách). | 4 |
| 20 | 22 → 21 → 17 → 9 | Cho biết lần giao hàng thuộc phiếu giao nào; phiếu giao đó lập cho đơn hàng nào; đơn hàng đó do nhân viên nào lập. | 1 |
| 21 | 22 → 21 → 17 → 16 → 9 | Cho biết lần giao hàng thuộc phiếu giao nào; phiếu giao đó lập cho đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo. | 1 |
| 22 | 26 → 3 → 1 | Cho biết giao dịch kho liên quan đến mặt hàng nào; mặt hàng đó thuộc loại hàng nào. | 4 |
| 23 | 26 → 3 → 2 | Cho biết giao dịch kho liên quan đến mặt hàng nào; mặt hàng đó mang thương hiệu nào. | 4 |
| 24 | 26 → 9 | Cho biết giao dịch kho do nhân viên nào thực hiện. | 4 |
| 25 | 28 → 25 → 18 → 3 → 1 | Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó đã bán ở dòng đơn nào; dòng đơn đó bán mặt hàng nào; mặt hàng đó thuộc loại hàng nào. | 1 |
| 26 | 28 → 25 → 18 → 3 → 2 | Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó đã bán ở dòng đơn nào; dòng đơn đó bán mặt hàng nào; mặt hàng đó mang thương hiệu nào. | 1 |
| 27 | 28 → 25 → 18 → 17 → 7 | Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó đã bán ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách). | 1 |
| 28 | 28 → 25 → 18 → 17 → 9 | Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó đã bán ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó do nhân viên nào lập. | 1 |
| 29 | 28 → 25 → 18 → 17 → 16 → 9 | Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó đã bán ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo. | 1 |
| 30 | 28 → 25 → 24 → 3 → 1 | Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó nhập mặt hàng nào; mặt hàng đó thuộc loại hàng nào. | 1 |
| 31 | 28 → 25 → 24 → 3 → 2 | Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó nhập mặt hàng nào; mặt hàng đó mang thương hiệu nào. | 1 |
| 32 | 28 → 25 → 24 → 23 → 9 | Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó thuộc phiếu nhập nào; phiếu nhập đó do nhân viên kho nào lập. | 1 |
| 33 | 28 → 25 → 24 → 23 → 13 | Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó thuộc phiếu nhập nào; phiếu nhập đó nhận từ nhà cung cấp nào. | 1 |
| 34 | 28 → 27 → 9 | Cho biết dòng trả hàng thuộc hồ sơ đổi trả nào; hồ sơ đổi trả đó do nhân viên nào tiếp nhận. | 1 |
| 35 | 28 → 27 → 17 → 7 | Cho biết dòng trả hàng thuộc hồ sơ đổi trả nào; hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách). | 1 |
| 36 | 28 → 27 → 17 → 9 | Cho biết dòng trả hàng thuộc hồ sơ đổi trả nào; hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó do nhân viên nào lập. | 1 |
| 37 | 28 → 27 → 17 → 16 → 9 | Cho biết dòng trả hàng thuộc hồ sơ đổi trả nào; hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo. | 1 |
| 38 | 29 → 9 | Cho biết lần nhận lại hàng do nhân viên nào kiểm tra. | 1 |
| 39 | 29 → 27 → 9 | Cho biết lần nhận lại hàng thuộc hồ sơ đổi trả nào; hồ sơ đổi trả đó do nhân viên nào tiếp nhận. | 1 |
| 40 | 29 → 27 → 17 → 7 | Cho biết lần nhận lại hàng thuộc hồ sơ đổi trả nào; hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách). | 1 |
| 41 | 29 → 27 → 17 → 9 | Cho biết lần nhận lại hàng thuộc hồ sơ đổi trả nào; hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó do nhân viên nào lập. | 1 |
| 42 | 29 → 27 → 17 → 16 → 9 | Cho biết lần nhận lại hàng thuộc hồ sơ đổi trả nào; hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo. | 1 |
| 43 | 30 → 9 | Cho biết khoản hoàn tiền do người quản lý nào duyệt. | 1 |
| 44 | 30 → 20 → 9 | Cho biết khoản hoàn tiền tính trên khoản thanh toán nào; khoản thanh toán đó do nhân viên nào xác nhận thu. | 1 |
| 45 | 30 → 20 → 17 → 7 | Cho biết khoản hoàn tiền tính trên khoản thanh toán nào; khoản thanh toán đó trả cho đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách). | 1 |
| 46 | 30 → 20 → 17 → 9 | Cho biết khoản hoàn tiền tính trên khoản thanh toán nào; khoản thanh toán đó trả cho đơn hàng nào; đơn hàng đó do nhân viên nào lập. | 1 |
| 47 | 30 → 20 → 17 → 16 → 9 | Cho biết khoản hoàn tiền tính trên khoản thanh toán nào; khoản thanh toán đó trả cho đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo. | 1 |
| 48 | 30 → 27 → 9 | Cho biết khoản hoàn tiền theo hồ sơ đổi trả nào (nếu do đổi trả); hồ sơ đổi trả đó do nhân viên nào tiếp nhận. | 1 |
| 49 | 30 → 27 → 17 → 7 | Cho biết khoản hoàn tiền theo hồ sơ đổi trả nào (nếu do đổi trả); hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách). | 1 |
| 50 | 30 → 27 → 17 → 9 | Cho biết khoản hoàn tiền theo hồ sơ đổi trả nào (nếu do đổi trả); hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó do nhân viên nào lập. | 1 |
| 51 | 30 → 27 → 17 → 16 → 9 | Cho biết khoản hoàn tiền theo hồ sơ đổi trả nào (nếu do đổi trả); hồ sơ đổi trả đó lập cho đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo. | 1 |
| 52 | 31 → 9 | Cho biết phiếu bảo hành do nhân viên nào tiếp nhận. | 2 |
| 53 | 31 → 18 → 3 → 1 | Cho biết phiếu bảo hành mua ở dòng đơn nào; dòng đơn đó bán mặt hàng nào; mặt hàng đó thuộc loại hàng nào. | 2 |
| 54 | 31 → 18 → 3 → 2 | Cho biết phiếu bảo hành mua ở dòng đơn nào; dòng đơn đó bán mặt hàng nào; mặt hàng đó mang thương hiệu nào. | 2 |
| 55 | 31 → 18 → 17 → 7 | Cho biết phiếu bảo hành mua ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách). | 1 |
| 56 | 31 → 18 → 17 → 9 | Cho biết phiếu bảo hành mua ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó do nhân viên nào lập. | 2 |
| 57 | 31 → 18 → 17 → 16 → 9 | Cho biết phiếu bảo hành mua ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo. | 1 |
| 58 | 31 → 25 → 18 → 3 → 1 | Cho biết phiếu bảo hành ứng với chiếc hàng có seri nào; chiếc hàng có seri đó đã bán ở dòng đơn nào; dòng đơn đó bán mặt hàng nào; mặt hàng đó thuộc loại hàng nào. | 1 |
| 59 | 31 → 25 → 18 → 3 → 2 | Cho biết phiếu bảo hành ứng với chiếc hàng có seri nào; chiếc hàng có seri đó đã bán ở dòng đơn nào; dòng đơn đó bán mặt hàng nào; mặt hàng đó mang thương hiệu nào. | 1 |
| 60 | 31 → 25 → 18 → 17 → 7 | Cho biết phiếu bảo hành ứng với chiếc hàng có seri nào; chiếc hàng có seri đó đã bán ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách). | 1 |
| 61 | 31 → 25 → 18 → 17 → 9 | Cho biết phiếu bảo hành ứng với chiếc hàng có seri nào; chiếc hàng có seri đó đã bán ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó do nhân viên nào lập. | 1 |
| 62 | 31 → 25 → 18 → 17 → 16 → 9 | Cho biết phiếu bảo hành ứng với chiếc hàng có seri nào; chiếc hàng có seri đó đã bán ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó áp dụng mã giảm giá nào (nếu có); mã giảm giá đó do nhân viên nào tạo. | 1 |
| 63 | 31 → 25 → 24 → 3 → 1 | Cho biết phiếu bảo hành ứng với chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó nhập mặt hàng nào; mặt hàng đó thuộc loại hàng nào. | 1 |
| 64 | 31 → 25 → 24 → 3 → 2 | Cho biết phiếu bảo hành ứng với chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó nhập mặt hàng nào; mặt hàng đó mang thương hiệu nào. | 1 |
| 65 | 31 → 25 → 24 → 23 → 9 | Cho biết phiếu bảo hành ứng với chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó thuộc phiếu nhập nào; phiếu nhập đó do nhân viên kho nào lập. | 1 |
| 66 | 31 → 25 → 24 → 23 → 13 | Cho biết phiếu bảo hành ứng với chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó thuộc phiếu nhập nào; phiếu nhập đó nhận từ nhà cung cấp nào. | 1 |

*Bảng 3.5: 66 con đường truy xuất từ các nút vào (số là số thứ tự nút ở bảng 3.2)*

Đường 12 cho 0 dòng là **đúng quy tắc**: giỏ hàng chỉ thuộc tài khoản khách, nên không có giỏ của tài khoản nhân viên.

## 3.3 CÁC TRUY VẤN BẰNG NGÔN NGỮ SQL

### 3.3.1 Quy tắc chung

Mỗi con đường truy xuất tương ứng một câu SELECT nối (JOIN) các quan hệ theo thứ tự các nút trên đường; điều kiện nối là khóa ngoại của cung (cột của nút đi bằng cột khóa của nút đến):

```sql
SELECT *
FROM   <nút vào> a0
JOIN   <nút 1>   a1 ON a0.<khóa ngoại> = a1.<khóa>
JOIN   <nút 2>   a2 ON a1.<khóa ngoại> = a2.<khóa>
...
```

Với nút HANGCOSERI (gộp từ HANGCOSERI và SERIMATHANG) câu lệnh nối thêm SERIMATHANG theo MaSeri để lấy lại đủ số seri và mặt hàng. Đã sinh **66 câu lệnh**, lưu ở `sql/03_truy_van_cac_duong_truy_xuat.sql`; mỗi câu đã chạy thử và đều trả về ít nhất một dòng, trừ 1 đường rỗng đúng quy tắc nêu dưới bảng 3.5 (cột cuối bảng 3.5).

### 3.3.2 Một số câu truy vấn của các con đường

**Đường 55: PHIEUBAOHANH → CHITIETDONHANG → DONHANG → KHACHHANG**

Ý nghĩa: Cho biết phiếu bảo hành mua ở dòng đơn nào; dòng đơn đó thuộc đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách).

```sql
SELECT *
FROM PHIEUBAOHANH bh
JOIN CHITIETDONHANG ct ON bh.MaDH = ct.MaDH AND bh.SoDongDH = ct.SoDongDH
JOIN DONHANG dh ON ct.MaDH = dh.MaDH
JOIN KHACHHANG kh ON dh.MaKH = kh.MaKH;
```

**Đường 45: KHOANHOAN → THANHTOAN → DONHANG → KHACHHANG**

Ý nghĩa: Cho biết khoản hoàn tiền tính trên khoản thanh toán nào; khoản thanh toán đó trả cho đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách).

```sql
SELECT *
FROM KHOANHOAN kc
JOIN THANHTOAN tt ON kc.MaTT = tt.MaTT
JOIN DONHANG dh ON tt.MaDH = dh.MaDH
JOIN KHACHHANG kh ON dh.MaKH = kh.MaKH;
```

**Đường 33: CHITIETTRA → HANGCOSERI → CHITIETPHIEUNHAP → PHIEUNHAP → NHACUNGCAP**

Ý nghĩa: Cho biết dòng trả hàng ghi chiếc hàng có seri nào; chiếc hàng có seri đó nhập về ở dòng phiếu nhập nào; dòng phiếu nhập đó thuộc phiếu nhập nào; phiếu nhập đó nhận từ nhà cung cấp nào.

```sql
SELECT *
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
SELECT *
FROM GIATRITHONGSO gt
JOIN DINHNGHIATHONGSO dn ON gt.MaTS = dn.MaTS
JOIN LOAIHANG lh ON dn.MaLoai = lh.MaLoai;
```

**Đường 19: LANGIAO → PHIEUGIAO → DONHANG → KHACHHANG**

Ý nghĩa: Cho biết lần giao hàng thuộc phiếu giao nào; phiếu giao đó lập cho đơn hàng nào; đơn hàng đó do khách hàng nào đặt (nếu có hồ sơ khách).

```sql
SELECT *
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

**K4. Truy vết một chiếc hàng theo số seri: nhập từ đâu, bán cho ai** (đường: SERIMATHANG ⇒ HANGCOSERI → CHITIETPHIEUNHAP → PHIEUNHAP → NHACUNGCAP; HANGCOSERI → CHITIETDONHANG → DONHANG → KHACHHANG; 1 dòng trên dữ liệu minh họa)

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

**K6. Ai đã xử lý từng bước của một đơn hàng, và lúc đó giữ vai trò gì (truy trách nhiệm)** (đường: DONHANG ⇒ NHATKYDONHANG → NHANVIEN; NHANVIEN ⇒ GIUVAITRO → VAITRO; 6 dòng trên dữ liệu minh họa)

```sql
SELECT dh.SoDH, nk.SoLanDoi, nk.TinhTrangMoi, nk.ThoiDiemDoi, nv.HoLotNV, nv.TenNV, vt.TenVT, nk.LyDoDoi
FROM DONHANG dh
JOIN NHATKYDONHANG nk ON nk.MaDH = dh.MaDH
LEFT JOIN NHANVIEN nv ON nv.MaNV = nk.MaNV
LEFT JOIN GIUVAITRO gv ON gv.MaNV = nv.MaNV AND nk.ThoiDiemDoi >= gv.NgayBatDauVT
                      AND (gv.NgayKetThucVT IS NULL OR nk.ThoiDiemDoi < gv.NgayKetThucVT)
LEFT JOIN VAITRO vt ON vt.MaVT = gv.MaVT
WHERE dh.SoDH = 'DH-0002'
ORDER BY nk.SoLanDoi, vt.TenVT;
```

**K7. Các khoản hoàn tiền trong tháng 10/2026: ai duyệt, ai chi tiền** (đường: KHOANHOAN → NHANVIEN (người duyệt, cột MaNV); KHOANHOAN → NHANVIEN (người chi, cột MaNVChi); 1 dòng trên dữ liệu minh họa)

```sql
SELECT kc.MaHoan, kc.SoTienHoan, kc.ThoiDiemDuyetHoan, nd.HoLotNV AS HoLotNguoiDuyet, nd.TenNV AS TenNguoiDuyet,
       kc.ThoiDiemChi, nc.HoLotNV AS HoLotNguoiChi, nc.TenNV AS TenNguoiChi
FROM KHOANHOAN kc
JOIN NHANVIEN nd ON nd.MaNV = kc.MaNV
LEFT JOIN NHANVIEN nc ON nc.MaNV = kc.MaNVChi
WHERE kc.ThoiDiemDuyetHoan >= '2026-10-01' AND kc.ThoiDiemDuyetHoan < '2026-11-01'
ORDER BY kc.ThoiDiemDuyetHoan;
```

**K8. Vai trò đang giữ của các nhân viên còn làm việc** (đường: NHANVIEN ⇐ GIUVAITRO → VAITRO; 8 dòng trên dữ liệu minh họa)

```sql
SELECT nv.MaNV, nv.HoLotNV, nv.TenNV, vt.TenVT, gv.NgayBatDauVT
FROM NHANVIEN nv
JOIN GIUVAITRO gv ON gv.MaNV = nv.MaNV
JOIN VAITRO vt ON vt.MaVT = gv.MaVT
WHERE nv.TinhTrangNV = 'Đang làm' AND gv.NgayKetThucVT IS NULL
ORDER BY nv.MaNV, vt.TenVT;
```

**K9. Giỏ hàng đang dùng của một khách kèm tiền tạm tính theo giá hiện hành** (đường: KHACHHANG ⇒ TAIKHOAN ⇒ GIOHANG ⇒ CHITIETGIOHANG → MATHANG; 2 dòng trên dữ liệu minh họa)

```sql
SELECT kh.HoLotKH, kh.TenKH, mh.TenSP, cg.SoLuongGio,
       COALESCE(mh.GiaKhuyenMai, mh.GiaNiemYet) AS DonGiaHienHanh,
       cg.SoLuongGio * COALESCE(mh.GiaKhuyenMai, mh.GiaNiemYet) AS TamTinh
FROM KHACHHANG kh
JOIN TAIKHOAN tk ON tk.MaKH = kh.MaKH
JOIN GIOHANG gh ON gh.MaTK = tk.MaTK
JOIN CHITIETGIOHANG cg ON cg.MaGio = gh.MaGio
JOIN MATHANG mh ON mh.MaSP = cg.MaSP
WHERE kh.SDTKH = '0900000001' AND gh.TinhTrangGio = 'Đang dùng';
```

Ghi chú: K3 quy ước chiều biến động theo LoaiBienDong (Nhập và Nhận lại làm tăng; Xuất bán làm giảm; Chuyển nhóm cần thêm nhóm đích nên chưa tính); quy ước dấu của sổ kho chưa chốt với cửa hàng và là điểm cần xác nhận.

## 3.4 NGÕ VÀO TRA CỨU VÀ CHỈ MỤC ĐỀ XUẤT

Giáo trình Bài 9 nhấn mạnh phép kết là thao tác chính và cần chỉ mục cho cột nối. Hai nhóm chỉ mục đề xuất, suy từ đồ thị:

1. **Ngõ vào tra cứu theo khóa riêng** (người dùng cung cấp giá trị): đã có chỉ mục tự động từ UNIQUE: SKU (MATHANG), SoDH (DONHANG), SoPhieu (PHIEUNHAP), CodeMG (MAGIAMGIA), (MaSP, SoSeri) (SERIMATHANG), (MaSP, ViTriAnh) (ANHMATHANG), MaDH (PHIEUGIAO), TenDangNhap, MaKH, MaNV (TAIKHOAN), TenVT (VAITRO). Cần thêm chỉ mục tìm khách theo SDTKH và nhân viên theo tên (TenKH, TenNV).
2. **Cột khóa ngoại của cung** nên có chỉ mục để phép nối theo chiều ngược (từ cha xuống n con) nhanh: DONHANG(MaKH), DONHANG(MaNV), CHITIETDONHANG(MaSP), THANHTOAN(MaDH), HOSODOITRA(MaDH), KHOANHOAN(MaTT), KHOANHOAN(MaHS), LANNHANLAI(MaHS), GIAODICHKHO(MaSP, ThoiDiemGD), PHIEUBAOHANH(MaDH, SoDongDH), HANGCOSERI(MaDH, SoDongDH), HANGCOSERI(MaPN, SoDongPN), GIOHANG(MaTK, TinhTrangGio), CHITIETGIOHANG(MaSP), DIACHIKHACH(MaKH), NHATKYDONHANG(MaNV, ThoiDiemDoi), GIUVAITRO(MaVT), và các khóa ngoại phụ tới NHANVIEN (MaNVDuyet, MaNVChi, MaNVThu, MaNVXacNhan, MaNVPhanCong) để tra “một nhân viên đã duyệt, chi, thu những gì”.

Khẳng định tốc độ cần đo trên dữ liệu thật; báo cáo chưa đo hiệu năng.

