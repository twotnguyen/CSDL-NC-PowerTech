# CHƯƠNG 2: THIẾT KẾ VÀ CHUẨN HÓA CƠ SỞ DỮ LIỆU QUAN HỆ

Chương này chuyển mô hình ERD ở chương 1 sang mô hình quan hệ, xác định tập phụ thuộc hàm (PTH), phủ tối thiểu, khóa và dạng chuẩn của **từng** lược đồ quan hệ (LĐQH), rồi cải tiến những lược đồ chưa đạt dạng chuẩn cao bằng thuật toán phân rã và tổng hợp, kiểm tra bảo toàn thông tin, bảo toàn PTH và tìm tình huống dạng chuẩn 4 (4NF). Ký hiệu theo bài giảng: Q(A₁,…,Aₙ), Q⁺, ‖Q‖ (tân từ), X⁺_F, F⁺. Khóa chính gạch chân liền, khóa ngoại gạch chân nét đứt; thuộc tính vừa là khóa chính vừa là khóa ngoại gạch liền và ghi chú FK.

## 2.1 MÔ HÌNH QUAN HỆ

### 2.1.1 Chuyển ERD sang mô hình quan hệ

Quy tắc chuyển đổi áp dụng: (1) mỗi loại thực thể thành một quan hệ có khóa chính là mã của thực thể; (2) mối kết hợp 1–n thêm khóa ngoại vào quan hệ phía n (cột cho phép rỗng khi bản số nhỏ nhất là 0); (3) mối kết hợp 1–1 thêm khóa ngoại và ràng buộc UNIQUE ở một phía (PHIEUGIAO.MaDH); (4) mối kết hợp n–n thành quan hệ riêng có khóa gồm khóa của các thực thể tham gia, cộng số thứ tự dòng khi cùng một cặp có thể lặp (CHITIETDONHANG, CHITIETPHIEUNHAP); (5) mối kết hợp có thuộc tính mang theo thuộc tính đó.

Kết quả là **25 quan hệ**: 20 từ các loại thực thể và 5 từ các mối kết hợp có thuộc tính (GIATRITHONGSO, CHITIETDONHANG, LANGIAO, CHITIETPHIEUNHAP, CHITIETTRA). Khi chuyển, nhóm giữ lại một số cột lưu thêm cho tiện tra cứu (ví dụ MaSP trên phiếu bảo hành). Đây là **lược đồ ban đầu**, chưa tối ưu; các cột này và việc chưa tách họ tên là nguyên nhân của những quan hệ chưa đạt BCNF ở mục 2.2 và được xử lý ở mục 2.3.

| STT | Quan hệ | Nguồn từ ERD | Loại | Ghi chú thiết kế |
|---|---|---|---|---|
| 1 | LOAIHANG | Thực thể | Cơ bản |  |
| 2 | THUONGHIEU | Thực thể | Cơ bản |  |
| 3 | MATHANG | Thực thể | Cơ bản |  |
| 4 | ANHMATHANG | Thực thể | Cơ bản |  |
| 5 | DINHNGHIATHONGSO | Thực thể | Cơ bản |  |
| 6 | GIATRITHONGSO | Mối kết hợp có thuộc tính | Mối kết hợp |  |
| 7 | KHACHHANG | Thực thể | Đối tượng ngoài | HoTenKH ghi nguyên họ tên trong một cột. |
| 8 | NHANVIEN | Thực thể | Đối tượng ngoài | HoTenNV ghi nguyên họ tên trong một cột. |
| 9 | TAIKHOAN | Thực thể | Nghiệp vụ |  |
| 10 | NHACUNGCAP | Thực thể | Đối tượng ngoài |  |
| 11 | MAGIAMGIA | Thực thể | Nghiệp vụ |  |
| 12 | DONHANG | Thực thể | Nghiệp vụ |  |
| 13 | CHITIETDONHANG | Mối kết hợp có thuộc tính | Mối kết hợp |  |
| 14 | THANHTOAN | Thực thể | Nghiệp vụ |  |
| 15 | PHIEUGIAO | Thực thể | Nghiệp vụ |  |
| 16 | LANGIAO | Mối kết hợp có thuộc tính | Mối kết hợp |  |
| 17 | PHIEUNHAP | Thực thể | Nghiệp vụ |  |
| 18 | CHITIETPHIEUNHAP | Mối kết hợp có thuộc tính | Mối kết hợp |  |
| 19 | HANGCOSERI | Thực thể | Nghiệp vụ | MaSP được ghi thêm vào từng chiếc hàng để tra cứu nhanh theo mặt hàng, dù đã suy ra được từ dòng nhập. |
| 20 | GIAODICHKHO | Thực thể | Nghiệp vụ |  |
| 21 | HOSODOITRA | Thực thể | Nghiệp vụ |  |
| 22 | CHITIETTRA | Mối kết hợp có thuộc tính | Mối kết hợp | MaDH được ghi thêm vào từng dòng trả để khai báo khóa ngoại ghép tới dòng đơn, dù đã có ở hồ sơ. |
| 23 | LANNHANLAI | Thực thể | Nghiệp vụ |  |
| 24 | KHOANHOAN | Thực thể | Nghiệp vụ |  |
| 25 | PHIEUBAOHANH | Thực thể | Nghiệp vụ | MaSP được ghi thêm vào phiếu để in tên hàng nhanh, dù đã suy ra được từ dòng mua gốc và chiếc hàng. |

*Bảng 2.1: Đối chiếu ERD và 25 quan hệ ban đầu*

### 2.1.2 Lược đồ quan hệ cơ sở dữ liệu

1. LOAIHANG(<u>MaLoai</u>, TenLoai, MoTaLoai, <span style="text-decoration: underline dashed">MaLoaiCha</span>)
2. THUONGHIEU(<u>MaTH</u>, TenTH, MoTaTH)
3. MATHANG(<u>MaSP</u>, SKU, TenSP, MoTaSP, GiaNiemYet, GiaKhuyenMai, ThoiHanBH, TinhTrangKD, CoSeri, <span style="text-decoration: underline dashed">MaLoai</span>, <span style="text-decoration: underline dashed">MaTH</span>)
4. ANHMATHANG(<u>MaAnh</u>, <span style="text-decoration: underline dashed">MaSP</span>, ViTriAnh, DuongDanAnh, LaAnhChinh)
5. DINHNGHIATHONGSO(<u>MaTS</u>, <span style="text-decoration: underline dashed">MaLoai</span>, TenTS, KieuGiaTri, DonViTS, BatBuoc)
6. GIATRITHONGSO(<u>MaSP</u><sup>FK</sup>, <u>MaTS</u><sup>FK</sup>, GiaTriTS)
7. KHACHHANG(<u>MaKH</u>, HoTenKH, SDTKH, EmailKH, MaSoThueKH)
8. NHANVIEN(<u>MaNV</u>, HoTenNV, SDTNV, EmailNV, NgayVaoLam, NgayNghiViec, TinhTrangNV, ChucVu)
9. TAIKHOAN(<u>MaTK</u>, TenDangNhap, MatKhauBam, TinhTrangTK, ThoiDiemTaoTK, <span style="text-decoration: underline dashed">MaKH</span>, <span style="text-decoration: underline dashed">MaNV</span>)
10. NHACUNGCAP(<u>MaNCC</u>, TenNCC, NguoiLienHeNCC, SDTNCC, DiaChiNCC, MaSoThueNCC, TinhTrangHT)
11. MAGIAMGIA(<u>MaMG</u>, CodeMG, TenChuongTrinh, LoaiGiam, MucGiam, DonToiThieu, GiamToiDa, NgayBatDau, NgayKetThuc, GioiHanLuot, <span style="text-decoration: underline dashed">MaNV</span>)
12. DONHANG(<u>MaDH</u>, SoDH, ThoiDiemLap, KenhBan, <span style="text-decoration: underline dashed">MaKH</span>, <span style="text-decoration: underline dashed">MaNV</span>, TenNguoiNhan, SDTNhan, DiaChiGiao, PhiGiao, GiamGia, <span style="text-decoration: underline dashed">MaMG</span>, TinhTrangDH, DieuKienCoc, GhiChuDH)
13. CHITIETDONHANG(<u>MaDH</u><sup>FK</sup>, <u>SoDongDH</u>, <span style="text-decoration: underline dashed">MaSP</span>, SoLuongBan, DonGiaChot, TenHangChot, SKUChot, ThoiHanBHChot)
14. THANHTOAN(<u>MaTT</u>, <span style="text-decoration: underline dashed">MaDH</span>, LoaiKhoan, PhuongThuc, SoTien, ThoiDiemTT, KetQuaTT, MaGiaoDichNgoai, DonViThanhToan, <span style="text-decoration: underline dashed">MaNV</span>, <span style="text-decoration: underline dashed">MaNVThu</span>)
15. PHIEUGIAO(<u>MaGiao</u>, <span style="text-decoration: underline dashed">MaDH</span>, <span style="text-decoration: underline dashed">MaNV</span>, ThoiDiemXuat, TinhTrangGiao)
16. LANGIAO(<u>MaGiao</u><sup>FK</sup>, <u>SoLan</u>, ThoiDiemGiao, KetQuaGiao, LyDoThatBai, <span style="text-decoration: underline dashed">MaNV</span>)
17. PHIEUNHAP(<u>MaPN</u>, SoPhieu, <span style="text-decoration: underline dashed">MaNCC</span>, <span style="text-decoration: underline dashed">MaNV</span>, ThoiDiemNhan, TinhTrangPN, <span style="text-decoration: underline dashed">MaNVXacNhan</span>, ThoiDiemXacNhan, SoHoaDonNCC, GhiChuPN)
18. CHITIETPHIEUNHAP(<u>MaPN</u><sup>FK</sup>, <u>SoDongPN</u>, <span style="text-decoration: underline dashed">MaSP</span>, SoLuongNhap, GiaNhap)
19. HANGCOSERI(<u>MaSeri</u>, SoSeri, <span style="text-decoration: underline dashed">MaSP</span>, <span style="text-decoration: underline dashed">MaPN</span>, <span style="text-decoration: underline dashed">SoDongPN</span>, <span style="text-decoration: underline dashed">MaDH</span>, <span style="text-decoration: underline dashed">SoDongDH</span>, TinhTrangSeri, ThoiDiemNhap)
20. GIAODICHKHO(<u>MaGDK</u>, <span style="text-decoration: underline dashed">MaSP</span>, NhomKho, LoaiBienDong, SoLuongGD, ThoiDiemGD, <span style="text-decoration: underline dashed">MaNV</span>, LoaiChungTu, MaChungTu, GhiChuGD)
21. HOSODOITRA(<u>MaHS</u>, <span style="text-decoration: underline dashed">MaDH</span>, <span style="text-decoration: underline dashed">MaNV</span>, NgayDeNghi, LoaiTruongHop, LyDoDoiTra, TinhTrangHS, HinhThucXuLy)
22. CHITIETTRA(<u>MaHS</u><sup>FK</sup>, <u>SoDongTra</u>, <span style="text-decoration: underline dashed">SoDongDH</span>, <span style="text-decoration: underline dashed">MaDH</span>, SoLuongTra, <span style="text-decoration: underline dashed">MaSeri</span>)
23. LANNHANLAI(<u>MaNhanLai</u>, <span style="text-decoration: underline dashed">MaHS</span>, ThoiDiemNhanLai, <span style="text-decoration: underline dashed">MaNV</span>, KetLuan, NhomSauKiemTra, ThoiDiemDuyet, <span style="text-decoration: underline dashed">MaNVDuyet</span>)
24. KHOANHOAN(<u>MaHoan</u>, <span style="text-decoration: underline dashed">MaTT</span>, <span style="text-decoration: underline dashed">MaHS</span>, <span style="text-decoration: underline dashed">MaPhieuBH</span>, <span style="text-decoration: underline dashed">MaNV</span>, SoTienHoan, PhuongThucHoan, ThoiDiemDuyetHoan, ThoiDiemChi, <span style="text-decoration: underline dashed">MaNVChi</span>)
25. PHIEUBAOHANH(<u>MaPhieuBH</u>, <span style="text-decoration: underline dashed">MaSeri</span>, <span style="text-decoration: underline dashed">MaSP</span>, <span style="text-decoration: underline dashed">MaDH</span>, <span style="text-decoration: underline dashed">SoDongDH</span>, MoTaLoi, PhuKienDiKem, NgayNhan, NgayHenTra, NgayTraThucTe, TinhTrangBH, KetQuaBH, LyDoTuChoi, <span style="text-decoration: underline dashed">MaNV</span>)

### 2.1.3 Mô tả các quan hệ (tân từ và ràng buộc)

**1/ LOAIHANG(<u>MaLoai</u>, TenLoai, MoTaLoai, <span style="text-decoration: underline dashed">MaLoaiCha</span>)**

Tân từ: Mỗi loại hàng được phân biệt bằng mã loại hàng (MaLoai), có tên (TenLoai) và mô tả (MoTaLoai). Các loại hàng phân cấp: một loại có tối đa một loại cha (MaLoaiCha), ví dụ nhóm "Linh kiện máy tính" gồm "Bộ nhớ RAM". Tên không dùng để phân biệt vì hai loại hàng có thể trùng tên.

Ràng buộc: MaLoai là số tự nhiên tăng dần. TenLoai không rỗng, tối đa 100 ký tự. MaLoaiCha rỗng với loại hàng ở cấp cao nhất và khác MaLoai của chính nó.

**2/ THUONGHIEU(<u>MaTH</u>, TenTH, MoTaTH)**

Tân từ: Mỗi thương hiệu được phân biệt bằng mã thương hiệu (MaTH), có tên (TenTH) không trùng với thương hiệu khác và mô tả (MoTaTH).

Ràng buộc: MaTH là số tự nhiên tăng dần. TenTH không rỗng, không trùng, tối đa 100 ký tự.

**3/ MATHANG(<u>MaSP</u>, SKU, TenSP, MoTaSP, GiaNiemYet, GiaKhuyenMai, ThoiHanBH, TinhTrangKD, CoSeri, <span style="text-decoration: underline dashed">MaLoai</span>, <span style="text-decoration: underline dashed">MaTH</span>)**

Tân từ: Mỗi mặt hàng có mã nội bộ (MaSP) và mã hàng thương mại (SKU) đều không trùng với mặt hàng nào khác. Thông tin gồm tên, mô tả, giá niêm yết, giá khuyến mãi (nếu có), thời hạn bảo hành theo tháng, tình trạng kinh doanh và cờ CoSeri cho biết mặt hàng có ghi số seri từng chiếc hay không. Mỗi mặt hàng thuộc đúng một loại (MaLoai) và một thương hiệu (MaTH).

Ràng buộc: MaSP là số tự nhiên tăng dần. SKU không rỗng, không trùng. GiaNiemYet lớn hơn 0; GiaKhuyenMai nếu có phải nhỏ hơn hoặc bằng GiaNiemYet. ThoiHanBH từ 0 đến 120. TinhTrangKD chỉ nhận "Đang kinh doanh" hoặc "Ngừng kinh doanh".

**4/ ANHMATHANG(<u>MaAnh</u>, <span style="text-decoration: underline dashed">MaSP</span>, ViTriAnh, DuongDanAnh, LaAnhChinh)**

Tân từ: Mỗi mặt hàng có nhiều ảnh minh họa. Mỗi ảnh có mã (MaAnh), thuộc một mặt hàng (MaSP), có vị trí (ViTriAnh) trong mặt hàng đó, đường dẫn tệp (DuongDanAnh) và cờ ảnh đại diện (LaAnhChinh). Vị trí ảnh trong cùng một mặt hàng không trùng nhau.

Ràng buộc: MaAnh là số tự nhiên tăng dần. ViTriAnh bắt đầu từ 1. (MaSP, ViTriAnh) không trùng. Mỗi mặt hàng có tối đa một ảnh có LaAnhChinh = 1.

**5/ DINHNGHIATHONGSO(<u>MaTS</u>, <span style="text-decoration: underline dashed">MaLoai</span>, TenTS, KieuGiaTri, DonViTS, BatBuoc)**

Tân từ: Mỗi loại hàng quy định các thông số riêng của mình. Mỗi thông số có mã (MaTS), thuộc một loại hàng (MaLoai), có tên (TenTS), kiểu giá trị (KieuGiaTri), đơn vị (DonViTS) nếu có và cho biết có bắt buộc nhập hay không.

Ràng buộc: MaTS là số tự nhiên tăng dần. KieuGiaTri chỉ nhận "Chữ", "Số" hoặc "Có/Không". TenTS không rỗng.

**6/ GIATRITHONGSO(<u>MaSP</u><sup>FK</sup>, <u>MaTS</u><sup>FK</sup>, GiaTriTS)**

Tân từ: Giá trị thông số cho biết mặt hàng (MaSP) có giá trị (GiaTriTS) nào ở thông số (MaTS). Mỗi mặt hàng có tối đa một giá trị cho một thông số.

Ràng buộc: GiaTriTS không rỗng. Thông số (MaTS) phải thuộc loại hàng của mặt hàng (MaSP); đây là ràng buộc liên quan hệ không biểu diễn được bằng PTH.

**7/ KHACHHANG(<u>MaKH</u>, HoTenKH, SDTKH, EmailKH, MaSoThueKH)**

Tân từ: Mỗi khách hàng được phân biệt bằng mã khách hàng (MaKH), có họ tên (HoTenKH), số điện thoại (SDTKH), email (EmailKH) nếu có và mã số thuế (MaSoThueKH) nếu là doanh nghiệp cần hóa đơn. Họ tên, số điện thoại hay email có thể trùng hoặc thay đổi nên không dùng để phân biệt hai khách.

Ràng buộc: MaKH là số tự nhiên tăng dần. HoTenKH không rỗng, tối đa 100 ký tự. SDTKH gồm 10 chữ số. EmailKH nếu có phải có ký tự "@". Khách mua tại quầy không để lại thông tin thì không có hồ sơ khách hàng.

**8/ NHANVIEN(<u>MaNV</u>, HoTenNV, SDTNV, EmailNV, NgayVaoLam, NgayNghiViec, TinhTrangNV, ChucVu)**

Tân từ: Mỗi nhân viên được phân biệt bằng mã nhân viên (MaNV), có họ tên (HoTenNV), số điện thoại (SDTNV), email (EmailNV) nếu có, ngày vào làm (NgayVaoLam), ngày nghỉ việc (NgayNghiViec) nếu đã nghỉ và tình trạng làm việc (TinhTrangNV). Nhân viên nghỉ việc vẫn giữ hồ sơ để tra cứu các chứng từ người đó đã lập hoặc duyệt. Mỗi nhân viên có một chức vụ chính (ChucVu) cho biết khâu nào người đó được làm: Quản lý, Bán hàng, Thu ngân, Kỹ thuật, Kho hoặc Giao hàng (giả thiết G6).

Ràng buộc: MaNV là số tự nhiên tăng dần. HoTenNV không rỗng. TinhTrangNV chỉ nhận "Đang làm" hoặc "Đã nghỉ". ChucVu chỉ nhận "Quản lý", "Bán hàng", "Thu ngân", "Kỹ thuật", "Kho" hoặc "Giao hàng". NgayNghiViec không trước NgayVaoLam và chỉ có giá trị khi TinhTrangNV là "Đã nghỉ". Không xóa hồ sơ nhân viên đã có chứng từ.

**9/ TAIKHOAN(<u>MaTK</u>, TenDangNhap, MatKhauBam, TinhTrangTK, ThoiDiemTaoTK, <span style="text-decoration: underline dashed">MaKH</span>, <span style="text-decoration: underline dashed">MaNV</span>)**

Tân từ: Khách đặt hàng trên trang web và nhân viên thao tác trên hệ thống đều có tài khoản. Mỗi tài khoản có mã (MaTK) và tên đăng nhập (TenDangNhap) không trùng, lưu mật khẩu đã băm, tình trạng (khóa khi vi phạm hoặc nghi lộ mật khẩu) và thời điểm tạo. Tài khoản thuộc đúng một khách hàng (MaKH) hoặc đúng một nhân viên (MaNV); mỗi khách và mỗi nhân viên có tối đa một tài khoản. Quyền hạn của tài khoản nhân viên theo chức vụ (ChucVu) của nhân viên đó.

Ràng buộc: MaTK là số tự nhiên tăng dần. TenDangNhap không rỗng, không trùng. TinhTrangTK chỉ nhận "Hoạt động" hoặc "Bị khóa". Đúng một trong hai cột MaKH, MaNV có giá trị. Các PTH có vế trái MaKH hoặc MaNV chỉ xét trên những tài khoản có giá trị đó (giả thiết G4).

**10/ NHACUNGCAP(<u>MaNCC</u>, TenNCC, NguoiLienHeNCC, SDTNCC, DiaChiNCC, MaSoThueNCC, TinhTrangHT)**

Tân từ: Mỗi nhà cung cấp (nhà phân phối, đại lý chính hãng) được phân biệt bằng mã nhà cung cấp (MaNCC), có tên công ty không trùng với nhà cung cấp khác, người liên hệ, số điện thoại, địa chỉ, mã số thuế và tình trạng hợp tác. Thông tin liên hệ có thể trùng hoặc thay đổi nên không dùng để phân biệt.

Ràng buộc: MaNCC là số tự nhiên tăng dần. TenNCC không rỗng, không trùng. TinhTrangHT chỉ nhận "Đang hợp tác" hoặc "Ngừng hợp tác".

**11/ MAGIAMGIA(<u>MaMG</u>, CodeMG, TenChuongTrinh, LoaiGiam, MucGiam, DonToiThieu, GiamToiDa, NgayBatDau, NgayKetThuc, GioiHanLuot, <span style="text-decoration: underline dashed">MaNV</span>)**

Tân từ: Mỗi mã giảm giá có mã nội bộ (MaMG) và mã khách nhập (CodeMG), cả hai không trùng. Mã thuộc một chương trình (TenChuongTrinh), giảm theo phần trăm hoặc theo số tiền (LoaiGiam, MucGiam), áp dụng cho đơn từ giá trị tối thiểu (DonToiThieu), giảm tối đa (GiamToiDa), trong thời gian từ NgayBatDau đến NgayKetThuc và dùng tối đa GioiHanLuot lượt. Mỗi mã ghi nhân viên tạo (MaNV) để biết ai chịu trách nhiệm về chương trình.

Ràng buộc: CodeMG không rỗng, không trùng. LoaiGiam chỉ nhận "Phần trăm" hoặc "Số tiền". MucGiam lớn hơn 0; nếu theo phần trăm thì không quá 100. NgayKetThuc nếu có phải sau hoặc bằng NgayBatDau.

**12/ DONHANG(<u>MaDH</u>, SoDH, ThoiDiemLap, KenhBan, <span style="text-decoration: underline dashed">MaKH</span>, <span style="text-decoration: underline dashed">MaNV</span>, TenNguoiNhan, SDTNhan, DiaChiGiao, PhiGiao, GiamGia, <span style="text-decoration: underline dashed">MaMG</span>, TinhTrangDH, DieuKienCoc, GhiChuDH)**

Tân từ: Mỗi đơn hàng có mã (MaDH) và số đơn (SoDH) không trùng, ghi ngày giờ lập (ThoiDiemLap), kênh bán (KenhBan), nhân viên lập (MaNV, rỗng khi khách tự đặt trên trang web) và khách hàng (MaKH) nếu có. Đơn ghi khoản giảm giá và mã giảm giá đã dùng (MaMG); với đơn cần giao còn ghi tên, số điện thoại, địa chỉ người nhận và phí giao. Các giá trị này được chốt khi cửa hàng xác nhận đơn. Đơn có tình trạng (TinhTrangDH) và, với đơn đặt cọc, ghi điều kiện cọc đã thỏa thuận (DieuKienCoc).

Ràng buộc: SoDH không trùng. KenhBan chỉ nhận "Quầy", "Trang web", "Điện thoại" hoặc "Tin nhắn". TinhTrangDH chỉ nhận "Chờ xác nhận", "Đã xác nhận", "Đang chuẩn bị", "Đang giao", "Hoàn tất" hoặc "Đã hủy". PhiGiao và GiamGia không âm. Mỗi đơn dùng tối đa một mã giảm giá. Đơn bán tại quầy không có người nhận hàng nên TenNguoiNhan, SDTNhan, DiaChiGiao rỗng. Đơn có KenhBan khác "Trang web" phải có MaNV. Khách tự hủy được đơn khi đơn còn "Chờ xác nhận"; sau khi cửa hàng xác nhận thì do cửa hàng xử lý.

**13/ CHITIETDONHANG(<u>MaDH</u><sup>FK</sup>, <u>SoDongDH</u>, <span style="text-decoration: underline dashed">MaSP</span>, SoLuongBan, DonGiaChot, TenHangChot, SKUChot, ThoiHanBHChot)**

Tân từ: Mỗi dòng của đơn hàng được phân biệt bằng đơn (MaDH) và số thứ tự dòng (SoDongDH), cho biết mặt hàng (MaSP), số lượng (SoLuongBan) và đơn giá, tên hàng, SKU, thời hạn bảo hành đã chốt tại thời điểm bán (DonGiaChot, TenHangChot, SKUChot, ThoiHanBHChot). Một mặt hàng có thể ở nhiều dòng của cùng đơn nếu giá hoặc điều kiện bán khác nhau, vì vậy (MaDH, MaSP) không là khóa. Các giá trị chốt không đổi khi mặt hàng đổi giá, đổi tên hoặc đổi thời hạn bảo hành về sau.

Ràng buộc: SoLuongBan lớn hơn 0. DonGiaChot không âm. ThoiHanBHChot từ 0 đến 120. Mỗi đơn có ít nhất một dòng. Tổng tiền hàng của đơn bằng tổng SoLuongBan x DonGiaChot của các dòng; đây là dữ liệu tính toán, không lưu.

**14/ THANHTOAN(<u>MaTT</u>, <span style="text-decoration: underline dashed">MaDH</span>, LoaiKhoan, PhuongThuc, SoTien, ThoiDiemTT, KetQuaTT, MaGiaoDichNgoai, DonViThanhToan, <span style="text-decoration: underline dashed">MaNV</span>, <span style="text-decoration: underline dashed">MaNVThu</span>)**

Tân từ: Mỗi lần thanh toán có mã (MaTT), thuộc một đơn hàng (MaDH), ghi loại khoản (LoaiKhoan: thanh toán hoặc đặt cọc), phương thức (PhuongThuc), số tiền, thời điểm, kết quả và, với giao dịch qua ngân hàng hoặc cổng thanh toán, mã giao dịch ngoài cùng đơn vị thanh toán. Một đơn có thể có nhiều lần thanh toán, kể cả cọc và phần còn lại. Nhân viên (MaNV) xác nhận đã nhận tiền sau khi đối chiếu; với khoản thu khi giao hàng, người giao (MaNVThu) là người đã thu tiền của khách.

Ràng buộc: PhuongThuc chỉ nhận "Tiền mặt", "Chuyển khoản", "Mã QR", "Thẻ ngân hàng", "Ví điện tử", "Cổng thanh toán" hoặc "Thu khi giao". SoTien lớn hơn 0. Chỉ lần thanh toán có KetQuaTT là "Thành công" mới được tính là đã thu. Cặp (DonViThanhToan, MaGiaoDichNgoai) không trùng khi cả hai có giá trị. MaNVThu chỉ có khi PhuongThuc là "Thu khi giao".

**15/ PHIEUGIAO(<u>MaGiao</u>, <span style="text-decoration: underline dashed">MaDH</span>, <span style="text-decoration: underline dashed">MaNV</span>, ThoiDiemXuat, TinhTrangGiao)**

Tân từ: Mỗi phiếu giao có mã (MaGiao), lập cho đúng một đơn cần giao (MaDH) và mỗi đơn chỉ có tối đa một phiếu giao. Phiếu ghi nhân viên giao hàng (MaNV), thời điểm xuất kho (ThoiDiemXuat) và tình trạng giao (TinhTrangGiao).

Ràng buộc: MaDH không trùng. TinhTrangGiao chỉ nhận "Đang giao", "Đã giao" hoặc "Không thành công". Chỉ đơn có người nhận và địa chỉ giao mới có phiếu giao.

**16/ LANGIAO(<u>MaGiao</u><sup>FK</sup>, <u>SoLan</u>, ThoiDiemGiao, KetQuaGiao, LyDoThatBai, <span style="text-decoration: underline dashed">MaNV</span>)**

Tân từ: Mỗi lần thử giao của một phiếu giao được phân biệt bằng phiếu (MaGiao) và số lần (SoLan), ghi thời điểm, kết quả (KetQuaGiao), lý do nếu không thành công (LyDoThatBai) và nhân viên giao hàng thực hiện lần đó (MaNV). Mỗi đơn được thử giao tối đa 3 lần. Đây là mối kết hợp giữa phiếu giao và nhân viên; nhân viên phụ trách phiếu (PHIEUGIAO.MaNV) có thể khác người đi giao một lần cụ thể.

Ràng buộc: SoLan từ 1 đến 3. LyDoThatBai không rỗng khi KetQuaGiao là "Thất bại". MaNV là nhân viên có chức vụ Giao hàng.

**17/ PHIEUNHAP(<u>MaPN</u>, SoPhieu, <span style="text-decoration: underline dashed">MaNCC</span>, <span style="text-decoration: underline dashed">MaNV</span>, ThoiDiemNhan, TinhTrangPN, <span style="text-decoration: underline dashed">MaNVXacNhan</span>, ThoiDiemXacNhan, SoHoaDonNCC, GhiChuPN)**

Tân từ: Mỗi phiếu nhập là một lần nhận hàng thực tế, có mã (MaPN) và số phiếu (SoPhieu) không trùng, ghi nhà cung cấp (MaNCC), nhân viên lập (MaNV), thời điểm nhận, tình trạng phiếu, nhân viên và thời điểm xác nhận phiếu, số hóa đơn của nhà cung cấp và ghi chú.

Ràng buộc: SoPhieu không trùng. TinhTrangPN chỉ nhận "Nháp", "Đã xác nhận" hoặc "Đã hủy". Phiếu có ít nhất một dòng; hàng chỉ được ghi tăng vào kho một lần khi phiếu chuyển sang "Đã xác nhận". Phiếu "Đã xác nhận" phải có MaNVXacNhan và ThoiDiemXacNhan; hai cột này cùng rỗng hoặc cùng có giá trị.

**18/ CHITIETPHIEUNHAP(<u>MaPN</u><sup>FK</sup>, <u>SoDongPN</u>, <span style="text-decoration: underline dashed">MaSP</span>, SoLuongNhap, GiaNhap)**

Tân từ: Mỗi dòng của phiếu nhập được phân biệt bằng phiếu (MaPN) và số thứ tự dòng (SoDongPN), cho biết mặt hàng (MaSP), số lượng thực nhận (SoLuongNhap) và giá nhập (GiaNhap). Cùng một mặt hàng có thể ở nhiều dòng nếu khác giá hoặc khác lô.

Ràng buộc: SoLuongNhap lớn hơn 0. GiaNhap không âm.

**19/ HANGCOSERI(<u>MaSeri</u>, SoSeri, <span style="text-decoration: underline dashed">MaSP</span>, <span style="text-decoration: underline dashed">MaPN</span>, <span style="text-decoration: underline dashed">SoDongPN</span>, <span style="text-decoration: underline dashed">MaDH</span>, <span style="text-decoration: underline dashed">SoDongDH</span>, TinhTrangSeri, ThoiDiemNhap)**

Tân từ: Mỗi chiếc hàng có số seri được phân biệt bằng mã nội bộ (MaSeri). Chiếc hàng ghi số seri (SoSeri), thuộc một mặt hàng (MaSP), nhập về theo một dòng của phiếu nhập (MaPN, SoDongPN) và, khi đã bán, ghi dòng đơn của lần bán gần nhất (MaDH, SoDongDH). Số seri là duy nhất trong cùng mặt hàng; hai mặt hàng khác nhau có thể có cùng số seri. Mỗi dòng nhập hay dòng đơn chỉ chứa một mặt hàng.

Ràng buộc: MaSeri là số tự nhiên tăng dần. Cặp (MaSP, SoSeri) không trùng. MaSP của chiếc phải bằng MaSP của dòng nhập và của dòng đơn nếu có. Mặt hàng phải có CoSeri = 1. MaDH và SoDongDH cùng rỗng hoặc cùng có giá trị. Các PTH có vế trái chứa cột cho phép rỗng (MaDH, SoDongDH) chỉ xét trên những chiếc đã bán. Chiếc trả về rồi bán lại thì MaDH, SoDongDH chuyển sang lần bán mới; lần bán trước vẫn tra được ở dòng trả (CHITIETTRA) và phiếu bảo hành.

**20/ GIAODICHKHO(<u>MaGDK</u>, <span style="text-decoration: underline dashed">MaSP</span>, NhomKho, LoaiBienDong, SoLuongGD, ThoiDiemGD, <span style="text-decoration: underline dashed">MaNV</span>, LoaiChungTu, MaChungTu, GhiChuGD)**

Tân từ: Mỗi lần hàng vào hoặc ra kho (nhập, bán, nhận lại) là một giao dịch kho có mã (MaGDK); mỗi lần chuyển nhóm là hai giao dịch đối ứng (chuyển ra khỏi nhóm cũ, chuyển vào nhóm mới). Mỗi giao dịch ghi mặt hàng, nhóm kho bị ảnh hưởng, loại biến động, số lượng, thời điểm, nhân viên thực hiện và chứng từ gốc. Số lượng hàng trong kho được tính từ các giao dịch này, không lưu thành một cột riêng.

Ràng buộc: SoLuongGD lớn hơn 0; Nhập, Nhận lại, Chuyển vào làm tăng, Xuất bán, Chuyển ra làm giảm. NhomKho chỉ nhận "Đủ điều kiện bán", "Chờ kiểm tra" hoặc "Chờ xử lý". Chuyển ra và Chuyển vào ghi thành cặp cùng mặt hàng, số lượng và chứng từ; số lượng tính được của một nhóm không âm (kiểm khi ghi). (LoaiChungTu, MaChungTu) trỏ tới nhiều loại chứng từ nên không khai báo được khóa ngoại.

**21/ HOSODOITRA(<u>MaHS</u>, <span style="text-decoration: underline dashed">MaDH</span>, <span style="text-decoration: underline dashed">MaNV</span>, NgayDeNghi, LoaiTruongHop, LyDoDoiTra, TinhTrangHS, HinhThucXuLy)**

Tân từ: Mỗi hồ sơ đổi trả có mã (MaHS), lập cho một đơn gốc (MaDH), nhân viên tiếp nhận (MaNV), ngày đề nghị, trường hợp (LoaiTruongHop), lý do, tình trạng và hình thức xử lý (đổi hàng hoặc hoàn tiền). Một đơn có thể có nhiều hồ sơ, miễn tổng số lượng trả không vượt số đã giao.

Ràng buộc: LoaiTruongHop chỉ nhận "Giao sai, thiếu hoặc hư hỏng", "Lỗi nhà sản xuất" hoặc "Khách đổi ý". HinhThucXuLy chỉ nhận "Đổi hàng" hoặc "Hoàn tiền". Hồ sơ chỉ được lập trong thời hạn quy định theo từng trường hợp (48 giờ kể từ khi nhận hàng; 7 hoặc 30 ngày kể từ ngày mua).

**22/ CHITIETTRA(<u>MaHS</u><sup>FK</sup>, <u>SoDongTra</u>, <span style="text-decoration: underline dashed">SoDongDH</span>, <span style="text-decoration: underline dashed">MaDH</span>, SoLuongTra, <span style="text-decoration: underline dashed">MaSeri</span>)**

Tân từ: Mỗi dòng của hồ sơ đổi trả được phân biệt bằng hồ sơ (MaHS) và số thứ tự dòng trả (SoDongTra), ghi dòng của đơn gốc được trả (SoDongDH), số lượng trả (SoLuongTra) và, với hàng có seri, chiếc hàng trả (MaSeri). Hàng có seri mỗi chiếc một dòng trả, nên một dòng đơn có thể ứng với nhiều dòng trả. Để khai báo khóa ngoại tới dòng đơn (MaDH, SoDongDH), dòng trả ghi thêm mã đơn gốc (MaDH), chính là đơn của hồ sơ.

Ràng buộc: SoLuongTra lớn hơn 0, bằng 1 khi có MaSeri, và tổng số lượng trả của một dòng đơn không vượt số đã giao. Trong một hồ sơ, mỗi chiếc hàng chỉ ghi một lần. MaDH phải bằng MaDH của hồ sơ (ràng buộc liên quan hệ).

**23/ LANNHANLAI(<u>MaNhanLai</u>, <span style="text-decoration: underline dashed">MaHS</span>, ThoiDiemNhanLai, <span style="text-decoration: underline dashed">MaNV</span>, KetLuan, NhomSauKiemTra, ThoiDiemDuyet, <span style="text-decoration: underline dashed">MaNVDuyet</span>)**

Tân từ: Mỗi lần cửa hàng nhận hàng trả về có mã (MaNhanLai), thuộc một hồ sơ đổi trả (MaHS), ghi thời điểm nhận. Mọi hàng nhận về vào nhóm chờ kiểm tra; nhân viên kỹ thuật (MaNV) kiểm tra, ghi kết luận và nhóm kho sau kiểm tra, người quản lý (MaNVDuyet) duyệt ở ThoiDiemDuyet.

Ràng buộc: NhomSauKiemTra chỉ nhận "Đủ điều kiện bán" hoặc "Chờ xử lý"; hàng không bán được thuộc nhóm chờ xử lý và lý do ghi ở KetLuan. Hàng chỉ chuyển nhóm sau khi có ThoiDiemDuyet. ThoiDiemDuyet và MaNVDuyet cùng rỗng hoặc cùng có giá trị. Việc chuyển nhóm không làm tăng tổng số hàng thực tế trong kho.

**24/ KHOANHOAN(<u>MaHoan</u>, <span style="text-decoration: underline dashed">MaTT</span>, <span style="text-decoration: underline dashed">MaHS</span>, <span style="text-decoration: underline dashed">MaPhieuBH</span>, <span style="text-decoration: underline dashed">MaNV</span>, SoTienHoan, PhuongThucHoan, ThoiDiemDuyetHoan, ThoiDiemChi, <span style="text-decoration: underline dashed">MaNVChi</span>)**

Tân từ: Mỗi khoản hoàn tiền có mã (MaHoan), gắn với một khoản thu gốc (MaTT); nếu do đổi trả thì gắn với hồ sơ (MaHS), nếu do bảo hành thu hồi sản phẩm thì gắn với phiếu bảo hành (MaPhieuBH), còn hoàn do hủy đơn thì không gắn với hai loại này. Người quản lý (MaNV) duyệt; khoản hoàn ghi số tiền, phương thức hoàn, thời điểm duyệt, thời điểm chi và nhân viên chi tiền (MaNVChi). Có thể hoàn nhiều lần nhưng tổng không vượt số tiền đã thu của khoản gốc.

Ràng buộc: SoTienHoan lớn hơn 0. Tổng SoTienHoan của một MaTT không vượt SoTien của khoản thu đó. MaHS và MaPhieuBH không cùng có giá trị. PhuongThucHoan là phương thức khách đã trả. ThoiDiemChi và MaNVChi cùng rỗng hoặc cùng có giá trị. Chỉ nhân viên có chức vụ Quản lý được duyệt (MaNV).

**25/ PHIEUBAOHANH(<u>MaPhieuBH</u>, <span style="text-decoration: underline dashed">MaSeri</span>, <span style="text-decoration: underline dashed">MaSP</span>, <span style="text-decoration: underline dashed">MaDH</span>, <span style="text-decoration: underline dashed">SoDongDH</span>, MoTaLoi, PhuKienDiKem, NgayNhan, NgayHenTra, NgayTraThucTe, TinhTrangBH, KetQuaBH, LyDoTuChoi, <span style="text-decoration: underline dashed">MaNV</span>)**

Tân từ: Mỗi phiếu tiếp nhận bảo hành có mã (MaPhieuBH), ghi chiếc hàng (MaSeri) nếu có seri, mặt hàng (MaSP), dòng mua gốc (MaDH, SoDongDH), mô tả lỗi, ghi chú phụ kiện đi kèm, ngày nhận, ngày hẹn trả, ngày trả thực tế, tình trạng, kết quả, lý do từ chối nếu có và nhân viên tiếp nhận (MaNV). Mặt hàng được ghi sẵn trên phiếu để tra cứu nhanh. Mỗi dòng mua và mỗi chiếc hàng chỉ thuộc một mặt hàng.

Ràng buộc: NgayHenTra nếu có không trước NgayNhan; phiếu từ chối không có ngày hẹn. TinhTrangBH chỉ nhận "Đã tiếp nhận", "Đang kiểm tra", "Đang gửi hãng", "Đã có kết quả", "Đã trả khách" hoặc "Từ chối". LyDoTuChoi không rỗng khi TinhTrangBH là "Từ chối". MaSP phải trùng MaSP của dòng mua gốc và của chiếc hàng. Các PTH có vế trái là MaSeri chỉ xét trên phiếu có MaSeri.

### 2.1.4 Danh sách thông tin các bảng

Kiểu dữ liệu theo SQL chuẩn (tiền là đồng Việt Nam, kiểu DECIMAL(15,0)). PFK: vừa là khóa chính vừa là khóa ngoại.

**1/ Bảng LOAIHANG** (Loại hàng)

| Tên thuộc tính | Ý nghĩa | Kiểu dữ liệu | Độ dài | Ràng buộc |
|---|---|---|---|---|
| MaLoai | Mã loại hàng | Integer |  | PK |
| TenLoai | Tên loại hàng | Nvarchar | 100 | Not Null |
| MoTaLoai | Mô tả loại hàng | Nvarchar | 500 | Null |
| MaLoaiCha | Mã loại hàng cha | Integer |  | FK, Null |

**2/ Bảng THUONGHIEU** (Thương hiệu)

| Tên thuộc tính | Ý nghĩa | Kiểu dữ liệu | Độ dài | Ràng buộc |
|---|---|---|---|---|
| MaTH | Mã thương hiệu | Integer |  | PK |
| TenTH | Tên thương hiệu | Nvarchar | 100 | Not Null, Unique |
| MoTaTH | Mô tả thương hiệu | Nvarchar | 500 | Null |

**3/ Bảng MATHANG** (Mặt hàng)

| Tên thuộc tính | Ý nghĩa | Kiểu dữ liệu | Độ dài | Ràng buộc |
|---|---|---|---|---|
| MaSP | Mã mặt hàng (nội bộ) | Integer |  | PK |
| SKU | Mã hàng thương mại | Varchar | 50 | Not Null, Unique |
| TenSP | Tên mặt hàng | Nvarchar | 200 | Not Null |
| MoTaSP | Mô tả | Nvarchar | 2000 | Null |
| GiaNiemYet | Giá niêm yết (đồng) | Decimal | 15,0 | Not Null |
| GiaKhuyenMai | Giá khuyến mãi đang áp dụng | Decimal | 15,0 | Null |
| ThoiHanBH | Thời hạn bảo hành (tháng, 0 nếu không bảo hành) | Integer |  | Not Null |
| TinhTrangKD | Đang kinh doanh hoặc đã ngừng | Nvarchar | 20 | Not Null |
| CoSeri | Có theo dõi số seri từng chiếc | Bit |  | Not Null |
| MaLoai | Loại hàng | Integer |  | FK, Not Null |
| MaTH | Thương hiệu | Integer |  | FK, Not Null |

**4/ Bảng ANHMATHANG** (Ảnh mặt hàng)

| Tên thuộc tính | Ý nghĩa | Kiểu dữ liệu | Độ dài | Ràng buộc |
|---|---|---|---|---|
| MaAnh | Mã ảnh | Integer |  | PK |
| MaSP | Mặt hàng | Integer |  | FK, Not Null |
| ViTriAnh | Vị trí ảnh trong mặt hàng | Integer |  | Not Null |
| DuongDanAnh | Đường dẫn tệp ảnh | Varchar | 500 | Not Null |
| LaAnhChinh | Là ảnh đại diện | Bit |  | Not Null |

**5/ Bảng DINHNGHIATHONGSO** (Định nghĩa thông số)

| Tên thuộc tính | Ý nghĩa | Kiểu dữ liệu | Độ dài | Ràng buộc |
|---|---|---|---|---|
| MaTS | Mã thông số | Integer |  | PK |
| MaLoai | Loại hàng quy định thông số này | Integer |  | FK, Not Null |
| TenTS | Tên thông số | Nvarchar | 100 | Not Null |
| KieuGiaTri | Chữ, số hoặc có/không | Nvarchar | 10 | Not Null |
| DonViTS | Đơn vị (GB, MHz, W...) | Nvarchar | 20 | Null |
| BatBuoc | Thông số bắt buộc nhập | Bit |  | Not Null |

**6/ Bảng GIATRITHONGSO** (Giá trị thông số của mặt hàng)

| Tên thuộc tính | Ý nghĩa | Kiểu dữ liệu | Độ dài | Ràng buộc |
|---|---|---|---|---|
| MaSP | Mặt hàng | Integer |  | PFK |
| MaTS | Thông số | Integer |  | PFK |
| GiaTriTS | Giá trị của thông số | Nvarchar | 200 | Not Null |

**7/ Bảng KHACHHANG** (Khách hàng)

| Tên thuộc tính | Ý nghĩa | Kiểu dữ liệu | Độ dài | Ràng buộc |
|---|---|---|---|---|
| MaKH | Mã khách hàng | Integer |  | PK |
| HoTenKH | Họ và tên khách hàng | Nvarchar | 100 | Not Null |
| SDTKH | Số điện thoại | Varchar | 15 | Not Null |
| EmailKH | Địa chỉ email | Varchar | 100 | Null |
| MaSoThueKH | Mã số thuế (khách là doanh nghiệp) | Varchar | 14 | Null |

**8/ Bảng NHANVIEN** (Nhân viên)

| Tên thuộc tính | Ý nghĩa | Kiểu dữ liệu | Độ dài | Ràng buộc |
|---|---|---|---|---|
| MaNV | Mã nhân viên | Integer |  | PK |
| HoTenNV | Họ và tên nhân viên | Nvarchar | 100 | Not Null |
| SDTNV | Số điện thoại | Varchar | 15 | Not Null |
| EmailNV | Địa chỉ email | Varchar | 100 | Null |
| NgayVaoLam | Ngày vào làm | Date |  | Not Null |
| NgayNghiViec | Ngày nghỉ việc (rỗng nếu còn làm) | Date |  | Null |
| TinhTrangNV | Đang làm hoặc đã nghỉ | Nvarchar | 20 | Not Null |
| ChucVu | Chức vụ chính của nhân viên | Nvarchar | 20 | Not Null |

**9/ Bảng TAIKHOAN** (Tài khoản đăng nhập)

| Tên thuộc tính | Ý nghĩa | Kiểu dữ liệu | Độ dài | Ràng buộc |
|---|---|---|---|---|
| MaTK | Mã tài khoản | Integer |  | PK |
| TenDangNhap | Tên đăng nhập | Varchar | 50 | Not Null, Unique |
| MatKhauBam | Mật khẩu đã băm (không lưu mật khẩu gốc) | Varchar | 255 | Not Null |
| TinhTrangTK | Hoạt động hoặc bị khóa | Nvarchar | 20 | Not Null |
| ThoiDiemTaoTK | Thời điểm tạo tài khoản | Datetime |  | Not Null |
| MaKH | Khách hàng sở hữu tài khoản (rỗng nếu là tài khoản nhân viên) | Integer |  | FK, Null, Unique |
| MaNV | Nhân viên sở hữu tài khoản (rỗng nếu là tài khoản khách) | Integer |  | FK, Null, Unique |

**10/ Bảng NHACUNGCAP** (Nhà cung cấp)

| Tên thuộc tính | Ý nghĩa | Kiểu dữ liệu | Độ dài | Ràng buộc |
|---|---|---|---|---|
| MaNCC | Mã nhà cung cấp | Integer |  | PK |
| TenNCC | Tên công ty | Nvarchar | 200 | Not Null, Unique |
| NguoiLienHeNCC | Người liên hệ | Nvarchar | 100 | Null |
| SDTNCC | Số điện thoại | Varchar | 15 | Null |
| DiaChiNCC | Địa chỉ | Nvarchar | 300 | Null |
| MaSoThueNCC | Mã số thuế | Varchar | 14 | Null |
| TinhTrangHT | Tình trạng hợp tác | Nvarchar | 20 | Not Null |

**11/ Bảng MAGIAMGIA** (Mã giảm giá)

| Tên thuộc tính | Ý nghĩa | Kiểu dữ liệu | Độ dài | Ràng buộc |
|---|---|---|---|---|
| MaMG | Mã nội bộ | Integer |  | PK |
| CodeMG | Mã khách nhập | Varchar | 30 | Not Null, Unique |
| TenChuongTrinh | Tên chương trình | Nvarchar | 200 | Not Null |
| LoaiGiam | Theo phần trăm hoặc theo số tiền | Nvarchar | 10 | Not Null |
| MucGiam | Mức giảm | Decimal | 15,2 | Not Null |
| DonToiThieu | Giá trị đơn tối thiểu | Decimal | 15,0 | Null |
| GiamToiDa | Mức giảm tối đa | Decimal | 15,0 | Null |
| NgayBatDau | Ngày bắt đầu áp dụng | Date |  | Null |
| NgayKetThuc | Ngày hết hạn | Date |  | Null |
| GioiHanLuot | Số lượt dùng tối đa | Integer |  | Null |
| MaNV | Nhân viên tạo mã | Integer |  | FK, Not Null |

**12/ Bảng DONHANG** (Đơn hàng)

| Tên thuộc tính | Ý nghĩa | Kiểu dữ liệu | Độ dài | Ràng buộc |
|---|---|---|---|---|
| MaDH | Mã đơn hàng | Integer |  | PK |
| SoDH | Số đơn hàng in trên phiếu | Varchar | 20 | Not Null, Unique |
| ThoiDiemLap | Ngày giờ lập đơn | Datetime |  | Not Null |
| KenhBan | Quầy, trang web, điện thoại hoặc tin nhắn | Nvarchar | 20 | Not Null |
| MaKH | Khách hàng (rỗng nếu khách vãng lai) | Integer |  | FK, Null |
| MaNV | Nhân viên lập đơn (rỗng nếu khách tự đặt trên trang web) | Integer |  | FK, Null |
| TenNguoiNhan | Tên người nhận hàng | Nvarchar | 100 | Null |
| SDTNhan | Số điện thoại người nhận | Varchar | 15 | Null |
| DiaChiGiao | Địa chỉ giao hàng | Nvarchar | 300 | Null |
| PhiGiao | Phí giao hàng | Decimal | 15,0 | Not Null |
| GiamGia | Số tiền giảm trên tiền hàng | Decimal | 15,0 | Not Null |
| MaMG | Mã giảm giá đã dùng | Integer |  | FK, Null |
| TinhTrangDH | Tình trạng đơn | Nvarchar | 20 | Not Null |
| DieuKienCoc | Điều kiện đặt cọc đã thỏa thuận | Nvarchar | 300 | Null |
| GhiChuDH | Ghi chú | Nvarchar | 500 | Null |

**13/ Bảng CHITIETDONHANG** (Chi tiết đơn hàng)

| Tên thuộc tính | Ý nghĩa | Kiểu dữ liệu | Độ dài | Ràng buộc |
|---|---|---|---|---|
| MaDH | Đơn hàng | Integer |  | PFK |
| SoDongDH | Số thứ tự dòng trong đơn | Integer |  | PK |
| MaSP | Mặt hàng bán | Integer |  | FK, Not Null |
| SoLuongBan | Số lượng | Integer |  | Not Null |
| DonGiaChot | Đơn giá bán đã chốt | Decimal | 15,0 | Not Null |
| TenHangChot | Tên hàng đã chốt | Nvarchar | 200 | Not Null |
| SKUChot | SKU đã chốt | Varchar | 50 | Not Null |
| ThoiHanBHChot | Thời hạn bảo hành đã chốt (tháng) | Integer |  | Not Null |

**14/ Bảng THANHTOAN** (Thanh toán)

| Tên thuộc tính | Ý nghĩa | Kiểu dữ liệu | Độ dài | Ràng buộc |
|---|---|---|---|---|
| MaTT | Mã lần thanh toán | Integer |  | PK |
| MaDH | Đơn hàng | Integer |  | FK, Not Null |
| LoaiKhoan | Thanh toán hoặc đặt cọc | Nvarchar | 15 | Not Null |
| PhuongThuc | Phương thức | Nvarchar | 20 | Not Null |
| SoTien | Số tiền | Decimal | 15,0 | Not Null |
| ThoiDiemTT | Thời điểm | Datetime |  | Not Null |
| KetQuaTT | Thành công, thất bại hoặc chờ | Nvarchar | 15 | Not Null |
| MaGiaoDichNgoai | Mã giao dịch của ngân hàng hoặc cổng thanh toán | Varchar | 50 | Null |
| DonViThanhToan | Ngân hàng, ví hoặc cổng thanh toán | Nvarchar | 50 | Null |
| MaNV | Nhân viên xác nhận đã nhận tiền | Integer |  | FK, Null |
| MaNVThu | Nhân viên giao hàng thu tiền (khoản thu khi giao) | Integer |  | FK, Null |

**15/ Bảng PHIEUGIAO** (Phiếu giao hàng)

| Tên thuộc tính | Ý nghĩa | Kiểu dữ liệu | Độ dài | Ràng buộc |
|---|---|---|---|---|
| MaGiao | Mã phiếu giao | Integer |  | PK |
| MaDH | Đơn hàng được giao | Integer |  | FK, Not Null, Unique |
| MaNV | Nhân viên giao hàng | Integer |  | FK, Not Null |
| ThoiDiemXuat | Thời điểm xuất kho giao đi | Datetime |  | Not Null |
| TinhTrangGiao | Tình trạng giao | Nvarchar | 20 | Not Null |

**16/ Bảng LANGIAO** (Lần giao hàng)

| Tên thuộc tính | Ý nghĩa | Kiểu dữ liệu | Độ dài | Ràng buộc |
|---|---|---|---|---|
| MaGiao | Phiếu giao | Integer |  | PFK |
| SoLan | Lần giao thứ mấy (1 đến 3) | Integer |  | PK |
| ThoiDiemGiao | Thời điểm thử giao | Datetime |  | Not Null |
| KetQuaGiao | Thành công hoặc thất bại | Nvarchar | 20 | Not Null |
| LyDoThatBai | Lý do khách vắng hoặc từ chối nhận | Nvarchar | 300 | Null |
| MaNV | Nhân viên giao hàng thực hiện lần này | Integer |  | FK, Not Null |

**17/ Bảng PHIEUNHAP** (Phiếu nhập)

| Tên thuộc tính | Ý nghĩa | Kiểu dữ liệu | Độ dài | Ràng buộc |
|---|---|---|---|---|
| MaPN | Mã phiếu nhập | Integer |  | PK |
| SoPhieu | Số phiếu nhập | Varchar | 20 | Not Null, Unique |
| MaNCC | Nhà cung cấp | Integer |  | FK, Not Null |
| MaNV | Nhân viên kho lập phiếu | Integer |  | FK, Not Null |
| ThoiDiemNhan | Thời điểm nhận hàng | Datetime |  | Not Null |
| TinhTrangPN | Tình trạng phiếu | Nvarchar | 20 | Not Null |
| MaNVXacNhan | Nhân viên xác nhận phiếu | Integer |  | FK, Null |
| ThoiDiemXacNhan | Thời điểm xác nhận | Datetime |  | Null |
| SoHoaDonNCC | Số hóa đơn của nhà cung cấp | Varchar | 30 | Null |
| GhiChuPN | Ghi chú | Nvarchar | 500 | Null |

**18/ Bảng CHITIETPHIEUNHAP** (Chi tiết phiếu nhập)

| Tên thuộc tính | Ý nghĩa | Kiểu dữ liệu | Độ dài | Ràng buộc |
|---|---|---|---|---|
| MaPN | Phiếu nhập | Integer |  | PFK |
| SoDongPN | Số thứ tự dòng trong phiếu | Integer |  | PK |
| MaSP | Mặt hàng nhập | Integer |  | FK, Not Null |
| SoLuongNhap | Số lượng thực nhận | Integer |  | Not Null |
| GiaNhap | Giá nhập một đơn vị | Decimal | 15,0 | Not Null |

**19/ Bảng HANGCOSERI** (Chiếc hàng có số seri)

| Tên thuộc tính | Ý nghĩa | Kiểu dữ liệu | Độ dài | Ràng buộc |
|---|---|---|---|---|
| MaSeri | Mã nội bộ của chiếc hàng | Integer |  | PK |
| SoSeri | Số seri in trên sản phẩm | Varchar | 60 | Not Null |
| MaSP | Mặt hàng của chiếc này | Integer |  | FK, Not Null |
| MaPN | Phiếu nhập chiếc này về | Integer |  | FK, Not Null |
| SoDongPN | Dòng của phiếu nhập | Integer |  | FK, Not Null |
| MaDH | Đơn của lần bán gần nhất | Integer |  | FK, Null |
| SoDongDH | Dòng đơn của lần bán gần nhất | Integer |  | FK, Null |
| TinhTrangSeri | Trong kho, đã bán, chờ kiểm tra... | Nvarchar | 20 | Not Null |
| ThoiDiemNhap | Thời điểm nhập kho | Datetime |  | Not Null |

**20/ Bảng GIAODICHKHO** (Giao dịch kho)

| Tên thuộc tính | Ý nghĩa | Kiểu dữ liệu | Độ dài | Ràng buộc |
|---|---|---|---|---|
| MaGDK | Mã giao dịch kho | Integer |  | PK |
| MaSP | Mặt hàng | Integer |  | FK, Not Null |
| NhomKho | Đủ điều kiện bán, chờ kiểm tra hoặc chờ xử lý | Nvarchar | 20 | Not Null |
| LoaiBienDong | Nhập, xuất bán, nhận lại, chuyển ra hoặc chuyển vào | Nvarchar | 20 | Not Null |
| SoLuongGD | Số lượng thay đổi (luôn dương) | Integer |  | Not Null |
| ThoiDiemGD | Thời điểm | Datetime |  | Not Null |
| MaNV | Nhân viên thực hiện | Integer |  | FK, Null |
| LoaiChungTu | Loại chứng từ gốc | Nvarchar | 20 | Null |
| MaChungTu | Mã chứng từ gốc | Integer |  | Null |
| GhiChuGD | Ghi chú | Nvarchar | 500 | Null |

**21/ Bảng HOSODOITRA** (Hồ sơ đổi trả)

| Tên thuộc tính | Ý nghĩa | Kiểu dữ liệu | Độ dài | Ràng buộc |
|---|---|---|---|---|
| MaHS | Mã hồ sơ đổi trả | Integer |  | PK |
| MaDH | Đơn gốc | Integer |  | FK, Not Null |
| MaNV | Nhân viên tiếp nhận | Integer |  | FK, Not Null |
| NgayDeNghi | Ngày đề nghị | Date |  | Not Null |
| LoaiTruongHop | Giao sai/hư hỏng, lỗi nhà sản xuất, khách đổi ý | Nvarchar | 30 | Not Null |
| LyDoDoiTra | Lý do | Nvarchar | 500 | Not Null |
| TinhTrangHS | Tình trạng hồ sơ | Nvarchar | 20 | Not Null |
| HinhThucXuLy | Đổi hàng hoặc hoàn tiền | Nvarchar | 20 | Null |

**22/ Bảng CHITIETTRA** (Chi tiết trả hàng)

| Tên thuộc tính | Ý nghĩa | Kiểu dữ liệu | Độ dài | Ràng buộc |
|---|---|---|---|---|
| MaHS | Hồ sơ đổi trả | Integer |  | PFK |
| SoDongTra | Số thứ tự dòng trong hồ sơ | Integer |  | PK |
| SoDongDH | Dòng của đơn gốc được trả | Integer |  | FK, Not Null |
| MaDH | Đơn gốc (lưu thêm để khai báo khóa ngoại tới dòng đơn) | Integer |  | FK, Not Null |
| SoLuongTra | Số lượng trả | Integer |  | Not Null |
| MaSeri | Chiếc hàng trả (hàng có seri) | Integer |  | FK, Null |

**23/ Bảng LANNHANLAI** (Lần nhận lại hàng)

| Tên thuộc tính | Ý nghĩa | Kiểu dữ liệu | Độ dài | Ràng buộc |
|---|---|---|---|---|
| MaNhanLai | Mã lần nhận lại | Integer |  | PK |
| MaHS | Hồ sơ đổi trả | Integer |  | FK, Not Null |
| ThoiDiemNhanLai | Thời điểm nhận hàng về | Datetime |  | Not Null |
| MaNV | Nhân viên kiểm tra | Integer |  | FK, Null |
| KetLuan | Kết luận kiểm tra | Nvarchar | 200 | Null |
| NhomSauKiemTra | Nhóm kho sau kiểm tra | Nvarchar | 20 | Null |
| ThoiDiemDuyet | Thời điểm người quản lý duyệt | Datetime |  | Null |
| MaNVDuyet | Người quản lý duyệt chuyển nhóm | Integer |  | FK, Null |

**24/ Bảng KHOANHOAN** (Khoản hoàn tiền)

| Tên thuộc tính | Ý nghĩa | Kiểu dữ liệu | Độ dài | Ràng buộc |
|---|---|---|---|---|
| MaHoan | Mã khoản hoàn | Integer |  | PK |
| MaTT | Khoản thu gốc được hoàn | Integer |  | FK, Not Null |
| MaHS | Hồ sơ đổi trả liên quan | Integer |  | FK, Null |
| MaPhieuBH | Phiếu bảo hành liên quan | Integer |  | FK, Null |
| MaNV | Người quản lý duyệt hoàn | Integer |  | FK, Not Null |
| SoTienHoan | Số tiền hoàn | Decimal | 15,0 | Not Null |
| PhuongThucHoan | Phương thức hoàn | Nvarchar | 30 | Not Null |
| ThoiDiemDuyetHoan | Thời điểm duyệt | Datetime |  | Not Null |
| ThoiDiemChi | Thời điểm chi tiền | Datetime |  | Null |
| MaNVChi | Nhân viên chi tiền hoàn | Integer |  | FK, Null |

**25/ Bảng PHIEUBAOHANH** (Phiếu tiếp nhận bảo hành)

| Tên thuộc tính | Ý nghĩa | Kiểu dữ liệu | Độ dài | Ràng buộc |
|---|---|---|---|---|
| MaPhieuBH | Mã phiếu bảo hành | Integer |  | PK |
| MaSeri | Chiếc hàng bảo hành (hàng có seri) | Integer |  | FK, Null |
| MaSP | Mặt hàng bảo hành | Integer |  | FK, Not Null |
| MaDH | Đơn mua gốc | Integer |  | FK, Not Null |
| SoDongDH | Dòng mua gốc | Integer |  | FK, Not Null |
| MoTaLoi | Mô tả lỗi | Nvarchar | 500 | Not Null |
| PhuKienDiKem | Ghi chú phụ kiện đi kèm (văn bản tự do) | Nvarchar | 300 | Null |
| NgayNhan | Ngày nhận | Date |  | Not Null |
| NgayHenTra | Ngày hẹn trả (rỗng nếu từ chối) | Date |  | Null |
| NgayTraThucTe | Ngày trả thực tế | Date |  | Null |
| TinhTrangBH | Tình trạng phiếu | Nvarchar | 20 | Not Null |
| KetQuaBH | Kết quả (sửa xong, đổi mới, hoàn tiền...) | Nvarchar | 30 | Null |
| LyDoTuChoi | Lý do từ chối bảo hành | Nvarchar | 300 | Null |
| MaNV | Nhân viên tiếp nhận | Integer |  | FK, Not Null |

### 2.1.5 Sơ đồ quan hệ cơ sở dữ liệu (sau cải tiến)

Các hình dưới đây vẽ lược đồ sau cải tiến theo từng nhóm: mỗi bảng ghi tên cột, kiểu, NOT NULL (NN) và khóa; chữ đỏ là khóa chính (PK), xanh lam là khóa vừa chính vừa ngoại (PFK), xanh lục là khóa ngoại (FK), xám là cột cho phép rỗng. Đường nét đứt nối khóa ngoại tới khóa chính của bảng cha, ghi tên mối kết hợp; bảng cha thuộc nhóm khác chỉ vẽ phần khóa.

![Hình 2.5: Sơ đồ quan hệ nhóm “Hàng hóa, ảnh và thông số”](hinh/sodo_quanhe_b1.png)

*Hình 2.5: Sơ đồ quan hệ nhóm “Hàng hóa, ảnh và thông số”*

![Hình 2.6: Sơ đồ quan hệ nhóm “Khách hàng, nhân viên và tài khoản”](hinh/sodo_quanhe_b2.png)

*Hình 2.6: Sơ đồ quan hệ nhóm “Khách hàng, nhân viên và tài khoản”*

![Hình 2.7: Sơ đồ quan hệ nhóm “Đơn hàng, thanh toán và giao hàng”](hinh/sodo_quanhe_b3.png)

*Hình 2.7: Sơ đồ quan hệ nhóm “Đơn hàng, thanh toán và giao hàng”*

![Hình 2.8: Sơ đồ quan hệ nhóm “Nhập hàng, số seri và kho”](hinh/sodo_quanhe_b4.png)

*Hình 2.8: Sơ đồ quan hệ nhóm “Nhập hàng, số seri và kho”*

![Hình 2.9: Sơ đồ quan hệ nhóm “Đổi trả, hoàn tiền và bảo hành”](hinh/sodo_quanhe_b5.png)

*Hình 2.9: Sơ đồ quan hệ nhóm “Đổi trả, hoàn tiền và bảo hành”*

## 2.2 TẬP PHỤ THUỘC HÀM, PHỦ TỐI THIỂU, KHÓA VÀ DẠNG CHUẨN CỦA TỪNG QUAN HỆ

### 2.2.1 Quy ước và giả thiết

Với mỗi quan hệ, báo cáo trình bày theo khuôn: (1) tập PTH F kèm căn cứ; (2) phủ tối thiểu theo 3 bước của bài giảng (B1 tách vế phải, B2 bỏ thuộc tính thừa ở vế trái bằng bao đóng, B3 bỏ PTH dư thừa); (3) khóa theo thuật toán nguồn N, trung gian TG, đích D; (4) dạng chuẩn từng mức. Phép tính đều đã được đối chiếu bằng chương trình `tools/fd.py` (tính lại bao đóng, khóa và dạng chuẩn); lời giải trong báo cáo vẫn trình bày từng bước.

Phụ thuộc hàm rút từ tân từ và quy tắc nghiệp vụ, **không** rút từ dữ liệu mẫu (dữ liệu mẫu không chứng minh được một PTH). Tập F chỉ ghi các PTH không hiển nhiên. Các giả thiết nghiệp vụ nhóm tự đặt:

- **G1**: Số seri chỉ duy nhất trong cùng một mặt hàng; hai mặt hàng khác nhau (hai hãng) có thể in cùng một số seri. Lý do: số seri do từng hãng tự đánh, cửa hàng không kiểm soát được việc trùng giữa các hãng.
- **G2**: Mỗi dòng của đơn hàng và mỗi dòng của phiếu nhập chỉ chứa đúng một mặt hàng; cùng một mặt hàng có thể ở nhiều dòng nếu khác giá hoặc khác lô.
- **G3**: Cửa hàng tìm khách hàng và nhân viên theo tên gọi (một phần của họ tên), nên họ tên là thuộc tính kép theo tiêu chí của bài giảng (phép thử: phải dùng `LIKE` trên một phần của giá trị).
- **G4**: Với các PTH có vế trái chứa cột cho phép rỗng (MaDH, SoDongDH ở HANGCOSERI; MaSeri ở PHIEUBAOHANH và CHITIETTRA; MaKH, MaNV ở TAIKHOAN), PTH chỉ xét trên những bộ mà các cột đó khác rỗng. Đây là PTH có điều kiện; tập thuộc tính suy ra từ các PTH này chỉ là ràng buộc duy nhất có điều kiện, không phải khóa của toàn quan hệ.
- **G5**: Mã hàng thương mại (SKU), số đơn hàng (SoDH), số phiếu nhập (SoPhieu), tên thương hiệu (TenTH), tên nhà cung cấp (TenNCC), mã khách nhập của mã giảm giá (CodeMG) và tên đăng nhập (TenDangNhap) không trùng nhau giữa các bản ghi cùng loại; mỗi đơn hàng có tối đa một phiếu giao.
- **G6**: Mỗi tài khoản thuộc đúng một khách hàng hoặc đúng một nhân viên; mỗi khách và mỗi nhân viên có tối đa một tài khoản. Mỗi nhân viên có một chức vụ chính (ChucVu); quyền hạn của tài khoản nhân viên theo chức vụ đó.

Dạng chuẩn dùng định nghĩa của giáo trình: DC1 mọi thuộc tính đơn; DC2 không phụ thuộc một phần vào khóa; DC3 không phụ thuộc bắc cầu vào khóa (hay với mọi PTH không hiển nhiên X → A, X là siêu khóa hoặc A là thuộc tính khóa); BCNF (BCK) mọi PTH không hiển nhiên có vế trái chứa khóa. Mọi khóa ứng viên đều được xét, không chỉ khóa chính.

**Phạm vi của G4.** Khóa ứng viên phải xác định duy nhất bộ trên mọi thể hiện hợp lệ của toàn quan hệ. Vì vậy một tập thuộc tính chỉ duy nhất trên những bộ khác rỗng (như MaKH của TAIKHOAN) là **ràng buộc duy nhất có điều kiện**, không phải khóa ứng viên; khi cài đặt, nó là UNIQUE có điều kiện `WHERE ... IS NOT NULL`. Báo cáo kiểm TAIKHOAN, HANGCOSERI, CHITIETTRA, PHIEUBAOHANH ở hai phạm vi: (a) **toàn quan hệ**, chỉ dùng PTH có vế trái không rỗng, cho khóa của toàn quan hệ; (b) **trên các bộ khác rỗng**, dùng thêm PTH có điều kiện để phát hiện dư thừa. Phép tính từng bước ở các mục sau trình bày phạm vi (b) vì đủ PTH hơn, và ghi rõ dòng nào là khóa có điều kiện. Cả 4 quan hệ này có dạng chuẩn như nhau ở hai phạm vi, nên kết luận dạng chuẩn không dựa vào khóa có điều kiện.

### 2.2.2 Lược đồ quan hệ LOAIHANG

Xét LĐQH LOAIHANG(<u>MaLoai</u>, TenLoai, MoTaLoai, <span style="text-decoration: underline dashed">MaLoaiCha</span>).

**Các phụ thuộc hàm:**

- f1: MaLoai → TenLoai,MoTaLoai,MaLoaiCha — khóa chính xác định mọi thuộc tính còn lại.

**Phủ tối thiểu của F_LOAIHANG:**

Bước 1: Tách vế phải, thu được 3 PTH, mỗi PTH một thuộc tính ở vế phải: MaLoai → TenLoai; MaLoai → MoTaLoai; MaLoai → MaLoaiCha.

Bước 2: Không thực hiện vì mọi PTH đều có vế trái là một thuộc tính (đã đầy đủ).

Bước 3: Không có PTH dư thừa vì không PTH nào suy ra được từ các PTH còn lại.

Vậy phủ tối thiểu của F_LOAIHANG là G_LOAIHANG = {MaLoai → TenLoai; MaLoai → MoTaLoai; MaLoai → MaLoaiCha}. (G ≡ F: đã kiểm tra bằng bao đóng.)

**Xác định khóa:**

N = {MaLoai}; TG = ∅; D = {TenLoai, MoTaLoai, MaLoaiCha}.

{MaLoai}⁺ = {MaLoai, TenLoai, MoTaLoai, MaLoaiCha} = Q⁺. Vậy khóa duy nhất là {MaLoai}.

**Xác định dạng chuẩn:**

- Đạt dạng chuẩn 1 vì mọi thuộc tính của LOAIHANG đều là thuộc tính đơn.
- Đạt dạng chuẩn 2 vì mọi khóa chỉ có một thuộc tính ({MaLoai}).
- Đạt dạng chuẩn 3 vì không có thuộc tính không khóa nào phụ thuộc bắc cầu vào khóa.
- Đạt BCNF vì mọi PTH không hiển nhiên đều có vế trái chứa khóa: {MaLoai}.
- Kết luận: **LOAIHANG đạt dạng chuẩn BCNF**.

### 2.2.3 Lược đồ quan hệ THUONGHIEU

Xét LĐQH THUONGHIEU(<u>MaTH</u>, TenTH, MoTaTH).

**Các phụ thuộc hàm:**

- f1: MaTH → TenTH,MoTaTH — khóa chính xác định mọi thuộc tính còn lại.
- f2: TenTH → MaTH,MoTaTH — ràng buộc UNIQUE: giá trị không trùng nên cũng xác định mọi thuộc tính.

**Phủ tối thiểu của F_THUONGHIEU:**

Bước 1: Tách vế phải, thu được 4 PTH, mỗi PTH một thuộc tính ở vế phải: MaTH → TenTH; MaTH → MoTaTH; TenTH → MaTH; TenTH → MoTaTH.

Bước 2: Không thực hiện vì mọi PTH đều có vế trái là một thuộc tính (đã đầy đủ).

Bước 3: Loại các PTH dư thừa (xét từ PTH cuối lên đầu để giữ các PTH của khóa chính):

- TenTH → MoTaTH: bỏ nó vẫn có TenTH⁺ ∋ MoTaTH.

Vậy phủ tối thiểu của F_THUONGHIEU là G_THUONGHIEU = {MaTH → TenTH; MaTH → MoTaTH; TenTH → MaTH}. (G ≡ F: đã kiểm tra bằng bao đóng.)

**Xác định khóa:**

N = ∅; TG = {MaTH, TenTH}; D = {MoTaTH}.

Bảng tổ hợp (Kᵢ = N ∪ Mᵢ với Mᵢ là tập con của TG):

| Mᵢ | Kᵢ | Kᵢ⁺ | Kết luận |
|---|---|---|---|
| ∅ | ∅ | ∅ | không |
| {MaTH} | {MaTH} | Q⁺ | khóa |
| {TenTH} | {TenTH} | Q⁺ | khóa |
| {MaTH, TenTH} | {MaTH, TenTH} | Q⁺ | siêu khóa |

Các khóa: {MaTH}; {TenTH}.

**Xác định dạng chuẩn:**

- Đạt dạng chuẩn 1 vì mọi thuộc tính của THUONGHIEU đều là thuộc tính đơn.
- Đạt dạng chuẩn 2 vì mọi khóa chỉ có một thuộc tính ({MaTH}; {TenTH}).
- Đạt dạng chuẩn 3 vì không có thuộc tính không khóa nào phụ thuộc bắc cầu vào khóa.
- Đạt BCNF vì mọi PTH không hiển nhiên đều có vế trái chứa khóa: {MaTH}; {TenTH}.
- Kết luận: **THUONGHIEU đạt dạng chuẩn BCNF**.

### 2.2.4 Lược đồ quan hệ MATHANG

Xét LĐQH MATHANG(<u>MaSP</u>, SKU, TenSP, MoTaSP, GiaNiemYet, GiaKhuyenMai, ThoiHanBH, TinhTrangKD, CoSeri, <span style="text-decoration: underline dashed">MaLoai</span>, <span style="text-decoration: underline dashed">MaTH</span>).

**Các phụ thuộc hàm:**

- f1: MaSP → SKU,TenSP,MoTaSP,GiaNiemYet,GiaKhuyenMai,ThoiHanBH,TinhTrangKD,CoSeri,MaLoai,MaTH — khóa chính xác định mọi thuộc tính còn lại.
- f2: SKU → MaSP,TenSP,MoTaSP,GiaNiemYet,GiaKhuyenMai,ThoiHanBH,TinhTrangKD,CoSeri,MaLoai,MaTH — ràng buộc UNIQUE: giá trị không trùng nên cũng xác định mọi thuộc tính.

**Phủ tối thiểu của F_MATHANG:**

Bước 1: Tách vế phải, thu được 20 PTH, mỗi PTH một thuộc tính ở vế phải: MaSP → {SKU, TenSP, MoTaSP, GiaNiemYet, GiaKhuyenMai, ThoiHanBH, TinhTrangKD, CoSeri, MaLoai, MaTH} (10 PTH); SKU → {MaSP, TenSP, MoTaSP, GiaNiemYet, GiaKhuyenMai, ThoiHanBH, TinhTrangKD, CoSeri, MaLoai, MaTH} (10 PTH).

Bước 2: Không thực hiện vì mọi PTH đều có vế trái là một thuộc tính (đã đầy đủ).

Bước 3: Loại các PTH dư thừa (xét từ PTH cuối lên đầu để giữ các PTH của khóa chính):

- SKU → {TenSP, MoTaSP, GiaNiemYet, GiaKhuyenMai, ThoiHanBH, TinhTrangKD, CoSeri, MaLoai, MaTH} (9 PTH): mỗi PTH suy ra được từ các PTH còn lại theo luật bắc cầu (ví dụ bỏ nó vẫn có SKU⁺ ∋ TenSP).

Vậy phủ tối thiểu của F_MATHANG là G_MATHANG = {MaSP → {SKU, TenSP, MoTaSP, GiaNiemYet, GiaKhuyenMai, ThoiHanBH, TinhTrangKD, CoSeri, MaLoai, MaTH} (10 PTH); SKU → {MaSP} (1 PTH)}. (G ≡ F: đã kiểm tra bằng bao đóng.)

**Xác định khóa:**

N = ∅; TG = {MaSP, SKU}; D = {TenSP, MoTaSP, GiaNiemYet, GiaKhuyenMai, ThoiHanBH, TinhTrangKD, CoSeri, MaLoai, MaTH}.

Bảng tổ hợp (Kᵢ = N ∪ Mᵢ với Mᵢ là tập con của TG):

| Mᵢ | Kᵢ | Kᵢ⁺ | Kết luận |
|---|---|---|---|
| ∅ | ∅ | ∅ | không |
| {MaSP} | {MaSP} | Q⁺ | khóa |
| {SKU} | {SKU} | Q⁺ | khóa |
| {MaSP, SKU} | {MaSP, SKU} | Q⁺ | siêu khóa |

Các khóa: {MaSP}; {SKU}.

**Xác định dạng chuẩn:**

- Đạt dạng chuẩn 1 vì mọi thuộc tính của MATHANG đều là thuộc tính đơn.
- Đạt dạng chuẩn 2 vì mọi khóa chỉ có một thuộc tính ({MaSP}; {SKU}).
- Đạt dạng chuẩn 3 vì không có thuộc tính không khóa nào phụ thuộc bắc cầu vào khóa.
- Đạt BCNF vì mọi PTH không hiển nhiên đều có vế trái chứa khóa: {MaSP}; {SKU}.
- Kết luận: **MATHANG đạt dạng chuẩn BCNF**.

### 2.2.5 Lược đồ quan hệ ANHMATHANG

Xét LĐQH ANHMATHANG(<u>MaAnh</u>, <span style="text-decoration: underline dashed">MaSP</span>, ViTriAnh, DuongDanAnh, LaAnhChinh).

**Các phụ thuộc hàm:**

- f1: MaAnh → MaSP,ViTriAnh,DuongDanAnh,LaAnhChinh — khóa chính xác định mọi thuộc tính còn lại.
- f2: MaSP,ViTriAnh → MaAnh,DuongDanAnh,LaAnhChinh — Vị trí ảnh trong cùng một mặt hàng không được trùng nhau (mục 1.4).

**Phủ tối thiểu của F_ANHMATHANG:**

Bước 1: Tách vế phải, thu được 7 PTH, mỗi PTH một thuộc tính ở vế phải: MaAnh → MaSP; MaAnh → ViTriAnh; MaAnh → DuongDanAnh; MaAnh → LaAnhChinh; MaSP,ViTriAnh → MaAnh; MaSP,ViTriAnh → DuongDanAnh; MaSP,ViTriAnh → LaAnhChinh.

Bước 2: Xét vế trái {MaSP, ViTriAnh}: (ViTriAnh)⁺ = {ViTriAnh}; (MaSP)⁺ = {MaSP}. Không chứa vế phải nên không thuộc tính nào thừa. Giữ nguyên.

Bước 3: Loại các PTH dư thừa (xét từ PTH cuối lên đầu để giữ các PTH của khóa chính):

- MaSP,ViTriAnh → DuongDanAnh: bỏ nó vẫn có (MaSP,ViTriAnh)⁺ ∋ DuongDanAnh.
- MaSP,ViTriAnh → LaAnhChinh: bỏ nó vẫn có (MaSP,ViTriAnh)⁺ ∋ LaAnhChinh.

Vậy phủ tối thiểu của F_ANHMATHANG là G_ANHMATHANG = {MaAnh → MaSP; MaAnh → ViTriAnh; MaAnh → DuongDanAnh; MaAnh → LaAnhChinh; MaSP,ViTriAnh → MaAnh}. (G ≡ F: đã kiểm tra bằng bao đóng.)

**Xác định khóa:**

N = ∅; TG = {MaAnh, MaSP, ViTriAnh}; D = {DuongDanAnh, LaAnhChinh}.

Bảng tổ hợp (Kᵢ = N ∪ Mᵢ với Mᵢ là tập con của TG):

| Mᵢ | Kᵢ | Kᵢ⁺ | Kết luận |
|---|---|---|---|
| ∅ | ∅ | ∅ | không |
| {MaAnh} | {MaAnh} | Q⁺ | khóa |
| {MaSP} | {MaSP} | {MaSP} | không |
| {ViTriAnh} | {ViTriAnh} | {ViTriAnh} | không |
| {MaAnh, MaSP} | {MaAnh, MaSP} | Q⁺ | siêu khóa |
| {MaAnh, ViTriAnh} | {MaAnh, ViTriAnh} | Q⁺ | siêu khóa |
| {MaSP, ViTriAnh} | {MaSP, ViTriAnh} | Q⁺ | khóa |
| {MaAnh, MaSP, ViTriAnh} | {MaAnh, MaSP, ViTriAnh} | Q⁺ | siêu khóa |

Các khóa: {MaAnh}; {MaSP, ViTriAnh}.

**Xác định dạng chuẩn:**

- Đạt dạng chuẩn 1 vì mọi thuộc tính của ANHMATHANG đều là thuộc tính đơn.
- Đạt dạng chuẩn 2 vì mọi thuộc tính không khóa (DuongDanAnh, LaAnhChinh) phụ thuộc đầy đủ vào khóa: không có tập con thật sự của khóa nào xác định chúng.
- Đạt dạng chuẩn 3 vì không có thuộc tính không khóa nào phụ thuộc bắc cầu vào khóa.
- Đạt BCNF vì mọi PTH không hiển nhiên đều có vế trái chứa khóa: {MaAnh}; {MaSP, ViTriAnh}.
- Kết luận: **ANHMATHANG đạt dạng chuẩn BCNF**.

### 2.2.6 Lược đồ quan hệ DINHNGHIATHONGSO

Xét LĐQH DINHNGHIATHONGSO(<u>MaTS</u>, <span style="text-decoration: underline dashed">MaLoai</span>, TenTS, KieuGiaTri, DonViTS, BatBuoc).

**Các phụ thuộc hàm:**

- f1: MaTS → MaLoai,TenTS,KieuGiaTri,DonViTS,BatBuoc — khóa chính xác định mọi thuộc tính còn lại.

**Phủ tối thiểu của F_DINHNGHIATHONGSO:**

Bước 1: Tách vế phải, thu được 5 PTH, mỗi PTH một thuộc tính ở vế phải: MaTS → MaLoai; MaTS → TenTS; MaTS → KieuGiaTri; MaTS → DonViTS; MaTS → BatBuoc.

Bước 2: Không thực hiện vì mọi PTH đều có vế trái là một thuộc tính (đã đầy đủ).

Bước 3: Không có PTH dư thừa vì không PTH nào suy ra được từ các PTH còn lại.

Vậy phủ tối thiểu của F_DINHNGHIATHONGSO là G_DINHNGHIATHONGSO = {MaTS → MaLoai; MaTS → TenTS; MaTS → KieuGiaTri; MaTS → DonViTS; MaTS → BatBuoc}. (G ≡ F: đã kiểm tra bằng bao đóng.)

**Xác định khóa:**

N = {MaTS}; TG = ∅; D = {MaLoai, TenTS, KieuGiaTri, DonViTS, BatBuoc}.

{MaTS}⁺ = {MaTS, MaLoai, TenTS, KieuGiaTri, DonViTS, BatBuoc} = Q⁺. Vậy khóa duy nhất là {MaTS}.

**Xác định dạng chuẩn:**

- Đạt dạng chuẩn 1 vì mọi thuộc tính của DINHNGHIATHONGSO đều là thuộc tính đơn.
- Đạt dạng chuẩn 2 vì mọi khóa chỉ có một thuộc tính ({MaTS}).
- Đạt dạng chuẩn 3 vì không có thuộc tính không khóa nào phụ thuộc bắc cầu vào khóa.
- Đạt BCNF vì mọi PTH không hiển nhiên đều có vế trái chứa khóa: {MaTS}.
- Kết luận: **DINHNGHIATHONGSO đạt dạng chuẩn BCNF**.

### 2.2.7 Lược đồ quan hệ GIATRITHONGSO

Xét LĐQH GIATRITHONGSO(<u>MaSP</u><sup>FK</sup>, <u>MaTS</u><sup>FK</sup>, GiaTriTS).

**Các phụ thuộc hàm:**

- f1: MaSP,MaTS → GiaTriTS — khóa chính xác định mọi thuộc tính còn lại.

**Phủ tối thiểu của F_GIATRITHONGSO:**

Bước 1: Tách vế phải. Không thực hiện vì mọi PTH đã có vế phải là một thuộc tính.

Bước 2: Xét vế trái {MaSP, MaTS}: (MaTS)⁺ = {MaTS}; (MaSP)⁺ = {MaSP}. Không chứa vế phải nên không thuộc tính nào thừa. Giữ nguyên.

Bước 3: Không có PTH dư thừa vì không PTH nào suy ra được từ các PTH còn lại.

Vậy phủ tối thiểu của F_GIATRITHONGSO là G_GIATRITHONGSO = {MaSP,MaTS → GiaTriTS}. (G ≡ F: đã kiểm tra bằng bao đóng.)

**Xác định khóa:**

N = {MaSP, MaTS}; TG = ∅; D = {GiaTriTS}.

{MaSP, MaTS}⁺ = {MaSP, MaTS, GiaTriTS} = Q⁺. Vậy khóa duy nhất là {MaSP, MaTS}.

**Xác định dạng chuẩn:**

- Đạt dạng chuẩn 1 vì mọi thuộc tính của GIATRITHONGSO đều là thuộc tính đơn.
- Đạt dạng chuẩn 2 vì mọi thuộc tính không khóa (GiaTriTS) phụ thuộc đầy đủ vào khóa: không có tập con thật sự của khóa nào xác định chúng.
- Đạt dạng chuẩn 3 vì không có thuộc tính không khóa nào phụ thuộc bắc cầu vào khóa.
- Đạt BCNF vì mọi PTH không hiển nhiên đều có vế trái chứa khóa: {MaSP, MaTS}.
- Kết luận: **GIATRITHONGSO đạt dạng chuẩn BCNF**.

### 2.2.8 Lược đồ quan hệ KHACHHANG

Xét LĐQH KHACHHANG(<u>MaKH</u>, HoTenKH, SDTKH, EmailKH, MaSoThueKH).

**Các phụ thuộc hàm:**

- f1: MaKH → HoTenKH,SDTKH,EmailKH,MaSoThueKH — khóa chính xác định mọi thuộc tính còn lại.

**Phủ tối thiểu của F_KHACHHANG:**

Bước 1: Tách vế phải, thu được 4 PTH, mỗi PTH một thuộc tính ở vế phải: MaKH → HoTenKH; MaKH → SDTKH; MaKH → EmailKH; MaKH → MaSoThueKH.

Bước 2: Không thực hiện vì mọi PTH đều có vế trái là một thuộc tính (đã đầy đủ).

Bước 3: Không có PTH dư thừa vì không PTH nào suy ra được từ các PTH còn lại.

Vậy phủ tối thiểu của F_KHACHHANG là G_KHACHHANG = {MaKH → HoTenKH; MaKH → SDTKH; MaKH → EmailKH; MaKH → MaSoThueKH}. (G ≡ F: đã kiểm tra bằng bao đóng.)

**Xác định khóa:**

N = {MaKH}; TG = ∅; D = {HoTenKH, SDTKH, EmailKH, MaSoThueKH}.

{MaKH}⁺ = {MaKH, HoTenKH, SDTKH, EmailKH, MaSoThueKH} = Q⁺. Vậy khóa duy nhất là {MaKH}.

**Xác định dạng chuẩn:**

- Không đạt dạng chuẩn 1 vì HoTenKH là thuộc tính kép (họ lót và tên, giả thiết G3); cửa hàng phải lọc theo từng phần của giá trị. Các mức sau xét trên các PTH đã cho, coi như họ tên đã được tách (mục 2.3.2).
- Đạt dạng chuẩn 2 vì mọi khóa chỉ có một thuộc tính ({MaKH}).
- Đạt dạng chuẩn 3 vì không có thuộc tính không khóa nào phụ thuộc bắc cầu vào khóa.
- Đạt BCNF vì mọi PTH không hiển nhiên đều có vế trái chứa khóa: {MaKH}.
- Kết luận: **KHACHHANG đạt dạng chuẩn BCNF (khi họ tên đã tách)** nhưng chưa đạt dạng chuẩn 1.

### 2.2.9 Lược đồ quan hệ NHANVIEN

Xét LĐQH NHANVIEN(<u>MaNV</u>, HoTenNV, SDTNV, EmailNV, NgayVaoLam, NgayNghiViec, TinhTrangNV, ChucVu).

**Các phụ thuộc hàm:**

- f1: MaNV → HoTenNV,SDTNV,EmailNV,NgayVaoLam,NgayNghiViec,TinhTrangNV,ChucVu — khóa chính xác định mọi thuộc tính còn lại.

**Phủ tối thiểu của F_NHANVIEN:**

Bước 1: Tách vế phải, thu được 7 PTH, mỗi PTH một thuộc tính ở vế phải: MaNV → HoTenNV; MaNV → SDTNV; MaNV → EmailNV; MaNV → NgayVaoLam; MaNV → NgayNghiViec; MaNV → TinhTrangNV; MaNV → ChucVu.

Bước 2: Không thực hiện vì mọi PTH đều có vế trái là một thuộc tính (đã đầy đủ).

Bước 3: Không có PTH dư thừa vì không PTH nào suy ra được từ các PTH còn lại.

Vậy phủ tối thiểu của F_NHANVIEN là G_NHANVIEN = {MaNV → HoTenNV; MaNV → SDTNV; MaNV → EmailNV; MaNV → NgayVaoLam; MaNV → NgayNghiViec; MaNV → TinhTrangNV; MaNV → ChucVu}. (G ≡ F: đã kiểm tra bằng bao đóng.)

**Xác định khóa:**

N = {MaNV}; TG = ∅; D = {HoTenNV, SDTNV, EmailNV, NgayVaoLam, NgayNghiViec, TinhTrangNV, ChucVu}.

{MaNV}⁺ = {MaNV, HoTenNV, SDTNV, EmailNV, NgayVaoLam, NgayNghiViec, TinhTrangNV, ChucVu} = Q⁺. Vậy khóa duy nhất là {MaNV}.

**Xác định dạng chuẩn:**

- Không đạt dạng chuẩn 1 vì HoTenNV là thuộc tính kép (họ lót và tên, giả thiết G3); cửa hàng phải lọc theo từng phần của giá trị. Các mức sau xét trên các PTH đã cho, coi như họ tên đã được tách (mục 2.3.2).
- Đạt dạng chuẩn 2 vì mọi khóa chỉ có một thuộc tính ({MaNV}).
- Đạt dạng chuẩn 3 vì không có thuộc tính không khóa nào phụ thuộc bắc cầu vào khóa.
- Đạt BCNF vì mọi PTH không hiển nhiên đều có vế trái chứa khóa: {MaNV}.
- Kết luận: **NHANVIEN đạt dạng chuẩn BCNF (khi họ tên đã tách)** nhưng chưa đạt dạng chuẩn 1.

### 2.2.10 Lược đồ quan hệ TAIKHOAN

Xét LĐQH TAIKHOAN(<u>MaTK</u>, TenDangNhap, MatKhauBam, TinhTrangTK, ThoiDiemTaoTK, <span style="text-decoration: underline dashed">MaKH</span>, <span style="text-decoration: underline dashed">MaNV</span>).

**Các phụ thuộc hàm:**

- f1: MaTK → TenDangNhap,MatKhauBam,TinhTrangTK,ThoiDiemTaoTK,MaKH,MaNV — khóa chính xác định mọi thuộc tính còn lại.
- f2: TenDangNhap → MaTK,MatKhauBam,TinhTrangTK,ThoiDiemTaoTK,MaKH,MaNV — Tên đăng nhập không trùng (giả thiết G5).
- f3: MaKH → MaTK,TenDangNhap,MatKhauBam,TinhTrangTK,ThoiDiemTaoTK,MaNV — Mỗi khách có tối đa một tài khoản; chỉ xét trên tài khoản của khách (giả thiết G4, G6).
- f4: MaNV → MaTK,TenDangNhap,MatKhauBam,TinhTrangTK,ThoiDiemTaoTK,MaKH — Mỗi nhân viên có tối đa một tài khoản; chỉ xét trên tài khoản của nhân viên (giả thiết G4, G6).

**Phủ tối thiểu của F_TAIKHOAN:**

Bước 1: Tách vế phải, thu được 24 PTH, mỗi PTH một thuộc tính ở vế phải: MaTK → {TenDangNhap, MatKhauBam, TinhTrangTK, ThoiDiemTaoTK, MaKH, MaNV} (6 PTH); TenDangNhap → {MaTK, MatKhauBam, TinhTrangTK, ThoiDiemTaoTK, MaKH, MaNV} (6 PTH); MaKH → {MaTK, TenDangNhap, MatKhauBam, TinhTrangTK, ThoiDiemTaoTK, MaNV} (6 PTH); MaNV → {MaTK, TenDangNhap, MatKhauBam, TinhTrangTK, ThoiDiemTaoTK, MaKH} (6 PTH).

Bước 2: Không thực hiện vì mọi PTH đều có vế trái là một thuộc tính (đã đầy đủ).

Bước 3: Loại các PTH dư thừa (xét từ PTH cuối lên đầu để giữ các PTH của khóa chính):

- TenDangNhap → {MatKhauBam, TinhTrangTK, ThoiDiemTaoTK, MaKH, MaNV} (5 PTH): mỗi PTH suy ra được từ các PTH còn lại theo luật bắc cầu (ví dụ bỏ nó vẫn có TenDangNhap⁺ ∋ MatKhauBam).
- MaKH → {TenDangNhap, MatKhauBam, TinhTrangTK, ThoiDiemTaoTK, MaNV} (5 PTH): mỗi PTH suy ra được từ các PTH còn lại theo luật bắc cầu (ví dụ bỏ nó vẫn có MaKH⁺ ∋ TenDangNhap).
- MaNV → {TenDangNhap, MatKhauBam, TinhTrangTK, ThoiDiemTaoTK, MaKH} (5 PTH): mỗi PTH suy ra được từ các PTH còn lại theo luật bắc cầu (ví dụ bỏ nó vẫn có MaNV⁺ ∋ TenDangNhap).

Vậy phủ tối thiểu của F_TAIKHOAN là G_TAIKHOAN = {MaTK → {TenDangNhap, MatKhauBam, TinhTrangTK, ThoiDiemTaoTK, MaKH, MaNV} (6 PTH); TenDangNhap → {MaTK} (1 PTH); MaKH → {MaTK} (1 PTH); MaNV → {MaTK} (1 PTH)}. (G ≡ F: đã kiểm tra bằng bao đóng.)

**Xác định khóa:**

N = ∅; TG = {MaTK, TenDangNhap, MaKH, MaNV}; D = {MatKhauBam, TinhTrangTK, ThoiDiemTaoTK}.

Bảng tổ hợp (Kᵢ = N ∪ Mᵢ với Mᵢ là tập con của TG):

| Mᵢ | Kᵢ | Kᵢ⁺ | Kết luận |
|---|---|---|---|
| ∅ | ∅ | ∅ | không |
| {MaTK} | {MaTK} | Q⁺ | khóa |
| {TenDangNhap} | {TenDangNhap} | Q⁺ | khóa |
| {MaKH} | {MaKH} | Q⁺ | khóa có điều kiện (G4) |
| {MaNV} | {MaNV} | Q⁺ | khóa có điều kiện (G4) |
| {MaTK, TenDangNhap} | {MaTK, TenDangNhap} | Q⁺ | siêu khóa |
| {MaTK, MaKH} | {MaTK, MaKH} | Q⁺ | siêu khóa |
| {MaTK, MaNV} | {MaTK, MaNV} | Q⁺ | siêu khóa |
| {TenDangNhap, MaKH} | {TenDangNhap, MaKH} | Q⁺ | siêu khóa |
| {TenDangNhap, MaNV} | {TenDangNhap, MaNV} | Q⁺ | siêu khóa |
| {MaKH, MaNV} | {MaKH, MaNV} | Q⁺ | siêu khóa |
| {MaTK, TenDangNhap, MaKH} | {MaTK, TenDangNhap, MaKH} | Q⁺ | siêu khóa |
| {MaTK, TenDangNhap, MaNV} | {MaTK, TenDangNhap, MaNV} | Q⁺ | siêu khóa |
| {MaTK, MaKH, MaNV} | {MaTK, MaKH, MaNV} | Q⁺ | siêu khóa |
| {TenDangNhap, MaKH, MaNV} | {TenDangNhap, MaKH, MaNV} | Q⁺ | siêu khóa |
| {MaTK, TenDangNhap, MaKH, MaNV} | {MaTK, TenDangNhap, MaKH, MaNV} | Q⁺ | siêu khóa |

Các khóa: {MaTK}; {TenDangNhap}.
Khóa có điều kiện: {MaKH}; {MaNV}; chỉ có hiệu lực trên các bộ khác rỗng ở cột cho phép rỗng (G4), không phải khóa của toàn quan hệ.

**Xác định dạng chuẩn:**

- Đạt dạng chuẩn 1 vì mọi thuộc tính của TAIKHOAN đều là thuộc tính đơn.
- Đạt dạng chuẩn 2 vì mọi khóa chỉ có một thuộc tính ({MaTK}; {TenDangNhap}).
- Đạt dạng chuẩn 3 vì không có thuộc tính không khóa nào phụ thuộc bắc cầu vào khóa.
- Đạt BCNF vì mọi PTH không hiển nhiên đều có vế trái chứa khóa: {MaTK}; {TenDangNhap}; {MaKH} (khóa có điều kiện, trên các bộ khác rỗng); {MaNV} (khóa có điều kiện, trên các bộ khác rỗng).
- Kết luận: **TAIKHOAN đạt dạng chuẩn BCNF**.

Kiểm tra ở phạm vi toàn quan hệ (không dùng PTH có điều kiện, khóa {MaTK}; {TenDangNhap}): dạng chuẩn không đổi, vẫn là BCNF.

### 2.2.11 Lược đồ quan hệ NHACUNGCAP

Xét LĐQH NHACUNGCAP(<u>MaNCC</u>, TenNCC, NguoiLienHeNCC, SDTNCC, DiaChiNCC, MaSoThueNCC, TinhTrangHT).

**Các phụ thuộc hàm:**

- f1: MaNCC → TenNCC,NguoiLienHeNCC,SDTNCC,DiaChiNCC,MaSoThueNCC,TinhTrangHT — khóa chính xác định mọi thuộc tính còn lại.
- f2: TenNCC → MaNCC,NguoiLienHeNCC,SDTNCC,DiaChiNCC,MaSoThueNCC,TinhTrangHT — ràng buộc UNIQUE: giá trị không trùng nên cũng xác định mọi thuộc tính.

**Phủ tối thiểu của F_NHACUNGCAP:**

Bước 1: Tách vế phải, thu được 12 PTH, mỗi PTH một thuộc tính ở vế phải: MaNCC → {TenNCC, NguoiLienHeNCC, SDTNCC, DiaChiNCC, MaSoThueNCC, TinhTrangHT} (6 PTH); TenNCC → {MaNCC, NguoiLienHeNCC, SDTNCC, DiaChiNCC, MaSoThueNCC, TinhTrangHT} (6 PTH).

Bước 2: Không thực hiện vì mọi PTH đều có vế trái là một thuộc tính (đã đầy đủ).

Bước 3: Loại các PTH dư thừa (xét từ PTH cuối lên đầu để giữ các PTH của khóa chính):

- TenNCC → {NguoiLienHeNCC, SDTNCC, DiaChiNCC, MaSoThueNCC, TinhTrangHT} (5 PTH): mỗi PTH suy ra được từ các PTH còn lại theo luật bắc cầu (ví dụ bỏ nó vẫn có TenNCC⁺ ∋ NguoiLienHeNCC).

Vậy phủ tối thiểu của F_NHACUNGCAP là G_NHACUNGCAP = {MaNCC → TenNCC; MaNCC → NguoiLienHeNCC; MaNCC → SDTNCC; MaNCC → DiaChiNCC; MaNCC → MaSoThueNCC; MaNCC → TinhTrangHT; TenNCC → MaNCC}. (G ≡ F: đã kiểm tra bằng bao đóng.)

**Xác định khóa:**

N = ∅; TG = {MaNCC, TenNCC}; D = {NguoiLienHeNCC, SDTNCC, DiaChiNCC, MaSoThueNCC, TinhTrangHT}.

Bảng tổ hợp (Kᵢ = N ∪ Mᵢ với Mᵢ là tập con của TG):

| Mᵢ | Kᵢ | Kᵢ⁺ | Kết luận |
|---|---|---|---|
| ∅ | ∅ | ∅ | không |
| {MaNCC} | {MaNCC} | Q⁺ | khóa |
| {TenNCC} | {TenNCC} | Q⁺ | khóa |
| {MaNCC, TenNCC} | {MaNCC, TenNCC} | Q⁺ | siêu khóa |

Các khóa: {MaNCC}; {TenNCC}.

**Xác định dạng chuẩn:**

- Đạt dạng chuẩn 1 vì mọi thuộc tính của NHACUNGCAP đều là thuộc tính đơn.
- Đạt dạng chuẩn 2 vì mọi khóa chỉ có một thuộc tính ({MaNCC}; {TenNCC}).
- Đạt dạng chuẩn 3 vì không có thuộc tính không khóa nào phụ thuộc bắc cầu vào khóa.
- Đạt BCNF vì mọi PTH không hiển nhiên đều có vế trái chứa khóa: {MaNCC}; {TenNCC}.
- Kết luận: **NHACUNGCAP đạt dạng chuẩn BCNF**.

### 2.2.12 Lược đồ quan hệ MAGIAMGIA

Xét LĐQH MAGIAMGIA(<u>MaMG</u>, CodeMG, TenChuongTrinh, LoaiGiam, MucGiam, DonToiThieu, GiamToiDa, NgayBatDau, NgayKetThuc, GioiHanLuot, <span style="text-decoration: underline dashed">MaNV</span>).

**Các phụ thuộc hàm:**

- f1: MaMG → CodeMG,TenChuongTrinh,LoaiGiam,MucGiam,DonToiThieu,GiamToiDa,NgayBatDau,NgayKetThuc,GioiHanLuot,MaNV — khóa chính xác định mọi thuộc tính còn lại.
- f2: CodeMG → MaMG,TenChuongTrinh,LoaiGiam,MucGiam,DonToiThieu,GiamToiDa,NgayBatDau,NgayKetThuc,GioiHanLuot,MaNV — ràng buộc UNIQUE: giá trị không trùng nên cũng xác định mọi thuộc tính.

**Phủ tối thiểu của F_MAGIAMGIA:**

Bước 1: Tách vế phải, thu được 20 PTH, mỗi PTH một thuộc tính ở vế phải: MaMG → {CodeMG, TenChuongTrinh, LoaiGiam, MucGiam, DonToiThieu, GiamToiDa, NgayBatDau, NgayKetThuc, GioiHanLuot, MaNV} (10 PTH); CodeMG → {MaMG, TenChuongTrinh, LoaiGiam, MucGiam, DonToiThieu, GiamToiDa, NgayBatDau, NgayKetThuc, GioiHanLuot, MaNV} (10 PTH).

Bước 2: Không thực hiện vì mọi PTH đều có vế trái là một thuộc tính (đã đầy đủ).

Bước 3: Loại các PTH dư thừa (xét từ PTH cuối lên đầu để giữ các PTH của khóa chính):

- CodeMG → {TenChuongTrinh, LoaiGiam, MucGiam, DonToiThieu, GiamToiDa, NgayBatDau, NgayKetThuc, GioiHanLuot, MaNV} (9 PTH): mỗi PTH suy ra được từ các PTH còn lại theo luật bắc cầu (ví dụ bỏ nó vẫn có CodeMG⁺ ∋ TenChuongTrinh).

Vậy phủ tối thiểu của F_MAGIAMGIA là G_MAGIAMGIA = {MaMG → {CodeMG, TenChuongTrinh, LoaiGiam, MucGiam, DonToiThieu, GiamToiDa, NgayBatDau, NgayKetThuc, GioiHanLuot, MaNV} (10 PTH); CodeMG → {MaMG} (1 PTH)}. (G ≡ F: đã kiểm tra bằng bao đóng.)

**Xác định khóa:**

N = ∅; TG = {MaMG, CodeMG}; D = {TenChuongTrinh, LoaiGiam, MucGiam, DonToiThieu, GiamToiDa, NgayBatDau, NgayKetThuc, GioiHanLuot, MaNV}.

Bảng tổ hợp (Kᵢ = N ∪ Mᵢ với Mᵢ là tập con của TG):

| Mᵢ | Kᵢ | Kᵢ⁺ | Kết luận |
|---|---|---|---|
| ∅ | ∅ | ∅ | không |
| {MaMG} | {MaMG} | Q⁺ | khóa |
| {CodeMG} | {CodeMG} | Q⁺ | khóa |
| {MaMG, CodeMG} | {MaMG, CodeMG} | Q⁺ | siêu khóa |

Các khóa: {MaMG}; {CodeMG}.

**Xác định dạng chuẩn:**

- Đạt dạng chuẩn 1 vì mọi thuộc tính của MAGIAMGIA đều là thuộc tính đơn.
- Đạt dạng chuẩn 2 vì mọi khóa chỉ có một thuộc tính ({MaMG}; {CodeMG}).
- Đạt dạng chuẩn 3 vì không có thuộc tính không khóa nào phụ thuộc bắc cầu vào khóa.
- Đạt BCNF vì mọi PTH không hiển nhiên đều có vế trái chứa khóa: {MaMG}; {CodeMG}.
- Kết luận: **MAGIAMGIA đạt dạng chuẩn BCNF**.

### 2.2.13 Lược đồ quan hệ DONHANG

Xét LĐQH DONHANG(<u>MaDH</u>, SoDH, ThoiDiemLap, KenhBan, <span style="text-decoration: underline dashed">MaKH</span>, <span style="text-decoration: underline dashed">MaNV</span>, TenNguoiNhan, SDTNhan, DiaChiGiao, PhiGiao, GiamGia, <span style="text-decoration: underline dashed">MaMG</span>, TinhTrangDH, DieuKienCoc, GhiChuDH).

**Các phụ thuộc hàm:**

- f1: MaDH → SoDH,ThoiDiemLap,KenhBan,MaKH,MaNV,TenNguoiNhan,SDTNhan,DiaChiGiao,PhiGiao,GiamGia,MaMG,TinhTrangDH,DieuKienCoc,GhiChuDH — khóa chính xác định mọi thuộc tính còn lại.
- f2: SoDH → MaDH,ThoiDiemLap,KenhBan,MaKH,MaNV,TenNguoiNhan,SDTNhan,DiaChiGiao,PhiGiao,GiamGia,MaMG,TinhTrangDH,DieuKienCoc,GhiChuDH — ràng buộc UNIQUE: giá trị không trùng nên cũng xác định mọi thuộc tính.

**Phủ tối thiểu của F_DONHANG:**

Bước 1: Tách vế phải, thu được 28 PTH, mỗi PTH một thuộc tính ở vế phải: MaDH → {SoDH, ThoiDiemLap, KenhBan, MaKH, MaNV, TenNguoiNhan, SDTNhan, DiaChiGiao, PhiGiao, GiamGia, MaMG, TinhTrangDH, DieuKienCoc, GhiChuDH} (14 PTH); SoDH → {MaDH, ThoiDiemLap, KenhBan, MaKH, MaNV, TenNguoiNhan, SDTNhan, DiaChiGiao, PhiGiao, GiamGia, MaMG, TinhTrangDH, DieuKienCoc, GhiChuDH} (14 PTH).

Bước 2: Không thực hiện vì mọi PTH đều có vế trái là một thuộc tính (đã đầy đủ).

Bước 3: Loại các PTH dư thừa (xét từ PTH cuối lên đầu để giữ các PTH của khóa chính):

- SoDH → {ThoiDiemLap, KenhBan, MaKH, MaNV, TenNguoiNhan, SDTNhan, DiaChiGiao, PhiGiao, GiamGia, MaMG, TinhTrangDH, DieuKienCoc, GhiChuDH} (13 PTH): mỗi PTH suy ra được từ các PTH còn lại theo luật bắc cầu (ví dụ bỏ nó vẫn có SoDH⁺ ∋ ThoiDiemLap).

Vậy phủ tối thiểu của F_DONHANG là G_DONHANG = {MaDH → {SoDH, ThoiDiemLap, KenhBan, MaKH, MaNV, TenNguoiNhan, SDTNhan, DiaChiGiao, PhiGiao, GiamGia, MaMG, TinhTrangDH, DieuKienCoc, GhiChuDH} (14 PTH); SoDH → {MaDH} (1 PTH)}. (G ≡ F: đã kiểm tra bằng bao đóng.)

**Xác định khóa:**

N = ∅; TG = {MaDH, SoDH}; D = {ThoiDiemLap, KenhBan, MaKH, MaNV, TenNguoiNhan, SDTNhan, DiaChiGiao, PhiGiao, GiamGia, MaMG, TinhTrangDH, DieuKienCoc, GhiChuDH}.

Bảng tổ hợp (Kᵢ = N ∪ Mᵢ với Mᵢ là tập con của TG):

| Mᵢ | Kᵢ | Kᵢ⁺ | Kết luận |
|---|---|---|---|
| ∅ | ∅ | ∅ | không |
| {MaDH} | {MaDH} | Q⁺ | khóa |
| {SoDH} | {SoDH} | Q⁺ | khóa |
| {MaDH, SoDH} | {MaDH, SoDH} | Q⁺ | siêu khóa |

Các khóa: {MaDH}; {SoDH}.

**Xác định dạng chuẩn:**

- Đạt dạng chuẩn 1 vì mọi thuộc tính của DONHANG đều là thuộc tính đơn.
- Đạt dạng chuẩn 2 vì mọi khóa chỉ có một thuộc tính ({MaDH}; {SoDH}).
- Đạt dạng chuẩn 3 vì không có thuộc tính không khóa nào phụ thuộc bắc cầu vào khóa.
- Đạt BCNF vì mọi PTH không hiển nhiên đều có vế trái chứa khóa: {MaDH}; {SoDH}.
- Kết luận: **DONHANG đạt dạng chuẩn BCNF**.

### 2.2.14 Lược đồ quan hệ CHITIETDONHANG

Xét LĐQH CHITIETDONHANG(<u>MaDH</u><sup>FK</sup>, <u>SoDongDH</u>, <span style="text-decoration: underline dashed">MaSP</span>, SoLuongBan, DonGiaChot, TenHangChot, SKUChot, ThoiHanBHChot).

**Các phụ thuộc hàm:**

- f1: MaDH,SoDongDH → MaSP,SoLuongBan,DonGiaChot,TenHangChot,SKUChot,ThoiHanBHChot — khóa chính xác định mọi thuộc tính còn lại.

**Phủ tối thiểu của F_CHITIETDONHANG:**

Bước 1: Tách vế phải, thu được 6 PTH, mỗi PTH một thuộc tính ở vế phải: MaDH,SoDongDH → MaSP; MaDH,SoDongDH → SoLuongBan; MaDH,SoDongDH → DonGiaChot; MaDH,SoDongDH → TenHangChot; MaDH,SoDongDH → SKUChot; MaDH,SoDongDH → ThoiHanBHChot.

Bước 2: Xét vế trái {MaDH, SoDongDH}: (SoDongDH)⁺ = {SoDongDH}; (MaDH)⁺ = {MaDH}. Không chứa vế phải nên không thuộc tính nào thừa. Giữ nguyên.

Bước 3: Không có PTH dư thừa vì không PTH nào suy ra được từ các PTH còn lại.

Vậy phủ tối thiểu của F_CHITIETDONHANG là G_CHITIETDONHANG = {MaDH,SoDongDH → MaSP; MaDH,SoDongDH → SoLuongBan; MaDH,SoDongDH → DonGiaChot; MaDH,SoDongDH → TenHangChot; MaDH,SoDongDH → SKUChot; MaDH,SoDongDH → ThoiHanBHChot}. (G ≡ F: đã kiểm tra bằng bao đóng.)

**Xác định khóa:**

N = {MaDH, SoDongDH}; TG = ∅; D = {MaSP, SoLuongBan, DonGiaChot, TenHangChot, SKUChot, ThoiHanBHChot}.

{MaDH, SoDongDH}⁺ = {MaDH, SoDongDH, MaSP, SoLuongBan, DonGiaChot, TenHangChot, SKUChot, ThoiHanBHChot} = Q⁺. Vậy khóa duy nhất là {MaDH, SoDongDH}.

**Xác định dạng chuẩn:**

- Đạt dạng chuẩn 1 vì mọi thuộc tính của CHITIETDONHANG đều là thuộc tính đơn.
- Đạt dạng chuẩn 2 vì mọi thuộc tính không khóa (MaSP, SoLuongBan, DonGiaChot, TenHangChot, SKUChot, ThoiHanBHChot) phụ thuộc đầy đủ vào khóa: không có tập con thật sự của khóa nào xác định chúng.
- Đạt dạng chuẩn 3 vì không có thuộc tính không khóa nào phụ thuộc bắc cầu vào khóa.
- Đạt BCNF vì mọi PTH không hiển nhiên đều có vế trái chứa khóa: {MaDH, SoDongDH}.
- Kết luận: **CHITIETDONHANG đạt dạng chuẩn BCNF**.

### 2.2.15 Lược đồ quan hệ THANHTOAN

Xét LĐQH THANHTOAN(<u>MaTT</u>, <span style="text-decoration: underline dashed">MaDH</span>, LoaiKhoan, PhuongThuc, SoTien, ThoiDiemTT, KetQuaTT, MaGiaoDichNgoai, DonViThanhToan, <span style="text-decoration: underline dashed">MaNV</span>, <span style="text-decoration: underline dashed">MaNVThu</span>).

**Các phụ thuộc hàm:**

- f1: MaTT → MaDH,LoaiKhoan,PhuongThuc,SoTien,ThoiDiemTT,KetQuaTT,MaGiaoDichNgoai,DonViThanhToan,MaNV,MaNVThu — khóa chính xác định mọi thuộc tính còn lại.

**Phủ tối thiểu của F_THANHTOAN:**

Bước 1: Tách vế phải, thu được 10 PTH, mỗi PTH một thuộc tính ở vế phải: MaTT → {MaDH, LoaiKhoan, PhuongThuc, SoTien, ThoiDiemTT, KetQuaTT, MaGiaoDichNgoai, DonViThanhToan, MaNV, MaNVThu} (10 PTH).

Bước 2: Không thực hiện vì mọi PTH đều có vế trái là một thuộc tính (đã đầy đủ).

Bước 3: Không có PTH dư thừa vì không PTH nào suy ra được từ các PTH còn lại.

Vậy phủ tối thiểu của F_THANHTOAN là G_THANHTOAN = {MaTT → {MaDH, LoaiKhoan, PhuongThuc, SoTien, ThoiDiemTT, KetQuaTT, MaGiaoDichNgoai, DonViThanhToan, MaNV, MaNVThu} (10 PTH)}. (G ≡ F: đã kiểm tra bằng bao đóng.)

**Xác định khóa:**

N = {MaTT}; TG = ∅; D = {MaDH, LoaiKhoan, PhuongThuc, SoTien, ThoiDiemTT, KetQuaTT, MaGiaoDichNgoai, DonViThanhToan, MaNV, MaNVThu}.

{MaTT}⁺ = {MaTT, MaDH, LoaiKhoan, PhuongThuc, SoTien, ThoiDiemTT, KetQuaTT, MaGiaoDichNgoai, DonViThanhToan, MaNV, MaNVThu} = Q⁺. Vậy khóa duy nhất là {MaTT}.

**Xác định dạng chuẩn:**

- Đạt dạng chuẩn 1 vì mọi thuộc tính của THANHTOAN đều là thuộc tính đơn.
- Đạt dạng chuẩn 2 vì mọi khóa chỉ có một thuộc tính ({MaTT}).
- Đạt dạng chuẩn 3 vì không có thuộc tính không khóa nào phụ thuộc bắc cầu vào khóa.
- Đạt BCNF vì mọi PTH không hiển nhiên đều có vế trái chứa khóa: {MaTT}.
- Kết luận: **THANHTOAN đạt dạng chuẩn BCNF**.

### 2.2.16 Lược đồ quan hệ PHIEUGIAO

Xét LĐQH PHIEUGIAO(<u>MaGiao</u>, <span style="text-decoration: underline dashed">MaDH</span>, <span style="text-decoration: underline dashed">MaNV</span>, ThoiDiemXuat, TinhTrangGiao).

**Các phụ thuộc hàm:**

- f1: MaGiao → MaDH,MaNV,ThoiDiemXuat,TinhTrangGiao — khóa chính xác định mọi thuộc tính còn lại.
- f2: MaDH → MaGiao,MaNV,ThoiDiemXuat,TinhTrangGiao — Mỗi đơn hàng có tối đa một phiếu giao (giả thiết G5).

**Phủ tối thiểu của F_PHIEUGIAO:**

Bước 1: Tách vế phải, thu được 8 PTH, mỗi PTH một thuộc tính ở vế phải: MaGiao → {MaDH, MaNV, ThoiDiemXuat, TinhTrangGiao} (4 PTH); MaDH → {MaGiao, MaNV, ThoiDiemXuat, TinhTrangGiao} (4 PTH).

Bước 2: Không thực hiện vì mọi PTH đều có vế trái là một thuộc tính (đã đầy đủ).

Bước 3: Loại các PTH dư thừa (xét từ PTH cuối lên đầu để giữ các PTH của khóa chính):

- MaDH → MaNV: bỏ nó vẫn có MaDH⁺ ∋ MaNV.
- MaDH → ThoiDiemXuat: bỏ nó vẫn có MaDH⁺ ∋ ThoiDiemXuat.
- MaDH → TinhTrangGiao: bỏ nó vẫn có MaDH⁺ ∋ TinhTrangGiao.

Vậy phủ tối thiểu của F_PHIEUGIAO là G_PHIEUGIAO = {MaGiao → MaDH; MaGiao → MaNV; MaGiao → ThoiDiemXuat; MaGiao → TinhTrangGiao; MaDH → MaGiao}. (G ≡ F: đã kiểm tra bằng bao đóng.)

**Xác định khóa:**

N = ∅; TG = {MaGiao, MaDH}; D = {MaNV, ThoiDiemXuat, TinhTrangGiao}.

Bảng tổ hợp (Kᵢ = N ∪ Mᵢ với Mᵢ là tập con của TG):

| Mᵢ | Kᵢ | Kᵢ⁺ | Kết luận |
|---|---|---|---|
| ∅ | ∅ | ∅ | không |
| {MaGiao} | {MaGiao} | Q⁺ | khóa |
| {MaDH} | {MaDH} | Q⁺ | khóa |
| {MaGiao, MaDH} | {MaGiao, MaDH} | Q⁺ | siêu khóa |

Các khóa: {MaGiao}; {MaDH}.

**Xác định dạng chuẩn:**

- Đạt dạng chuẩn 1 vì mọi thuộc tính của PHIEUGIAO đều là thuộc tính đơn.
- Đạt dạng chuẩn 2 vì mọi khóa chỉ có một thuộc tính ({MaGiao}; {MaDH}).
- Đạt dạng chuẩn 3 vì không có thuộc tính không khóa nào phụ thuộc bắc cầu vào khóa.
- Đạt BCNF vì mọi PTH không hiển nhiên đều có vế trái chứa khóa: {MaGiao}; {MaDH}.
- Kết luận: **PHIEUGIAO đạt dạng chuẩn BCNF**.

### 2.2.17 Lược đồ quan hệ LANGIAO

Xét LĐQH LANGIAO(<u>MaGiao</u><sup>FK</sup>, <u>SoLan</u>, ThoiDiemGiao, KetQuaGiao, LyDoThatBai, <span style="text-decoration: underline dashed">MaNV</span>).

**Các phụ thuộc hàm:**

- f1: MaGiao,SoLan → ThoiDiemGiao,KetQuaGiao,LyDoThatBai,MaNV — khóa chính xác định mọi thuộc tính còn lại.

**Phủ tối thiểu của F_LANGIAO:**

Bước 1: Tách vế phải, thu được 4 PTH, mỗi PTH một thuộc tính ở vế phải: MaGiao,SoLan → ThoiDiemGiao; MaGiao,SoLan → KetQuaGiao; MaGiao,SoLan → LyDoThatBai; MaGiao,SoLan → MaNV.

Bước 2: Xét vế trái {MaGiao, SoLan}: (SoLan)⁺ = {SoLan}; (MaGiao)⁺ = {MaGiao}. Không chứa vế phải nên không thuộc tính nào thừa. Giữ nguyên.

Bước 3: Không có PTH dư thừa vì không PTH nào suy ra được từ các PTH còn lại.

Vậy phủ tối thiểu của F_LANGIAO là G_LANGIAO = {MaGiao,SoLan → ThoiDiemGiao; MaGiao,SoLan → KetQuaGiao; MaGiao,SoLan → LyDoThatBai; MaGiao,SoLan → MaNV}. (G ≡ F: đã kiểm tra bằng bao đóng.)

**Xác định khóa:**

N = {MaGiao, SoLan}; TG = ∅; D = {ThoiDiemGiao, KetQuaGiao, LyDoThatBai, MaNV}.

{MaGiao, SoLan}⁺ = {MaGiao, SoLan, ThoiDiemGiao, KetQuaGiao, LyDoThatBai, MaNV} = Q⁺. Vậy khóa duy nhất là {MaGiao, SoLan}.

**Xác định dạng chuẩn:**

- Đạt dạng chuẩn 1 vì mọi thuộc tính của LANGIAO đều là thuộc tính đơn.
- Đạt dạng chuẩn 2 vì mọi thuộc tính không khóa (ThoiDiemGiao, KetQuaGiao, LyDoThatBai, MaNV) phụ thuộc đầy đủ vào khóa: không có tập con thật sự của khóa nào xác định chúng.
- Đạt dạng chuẩn 3 vì không có thuộc tính không khóa nào phụ thuộc bắc cầu vào khóa.
- Đạt BCNF vì mọi PTH không hiển nhiên đều có vế trái chứa khóa: {MaGiao, SoLan}.
- Kết luận: **LANGIAO đạt dạng chuẩn BCNF**.

### 2.2.18 Lược đồ quan hệ PHIEUNHAP

Xét LĐQH PHIEUNHAP(<u>MaPN</u>, SoPhieu, <span style="text-decoration: underline dashed">MaNCC</span>, <span style="text-decoration: underline dashed">MaNV</span>, ThoiDiemNhan, TinhTrangPN, <span style="text-decoration: underline dashed">MaNVXacNhan</span>, ThoiDiemXacNhan, SoHoaDonNCC, GhiChuPN).

**Các phụ thuộc hàm:**

- f1: MaPN → SoPhieu,MaNCC,MaNV,ThoiDiemNhan,TinhTrangPN,MaNVXacNhan,ThoiDiemXacNhan,SoHoaDonNCC,GhiChuPN — khóa chính xác định mọi thuộc tính còn lại.
- f2: SoPhieu → MaPN,MaNCC,MaNV,ThoiDiemNhan,TinhTrangPN,MaNVXacNhan,ThoiDiemXacNhan,SoHoaDonNCC,GhiChuPN — ràng buộc UNIQUE: giá trị không trùng nên cũng xác định mọi thuộc tính.

**Phủ tối thiểu của F_PHIEUNHAP:**

Bước 1: Tách vế phải, thu được 18 PTH, mỗi PTH một thuộc tính ở vế phải: MaPN → {SoPhieu, MaNCC, MaNV, ThoiDiemNhan, TinhTrangPN, MaNVXacNhan, ThoiDiemXacNhan, SoHoaDonNCC, GhiChuPN} (9 PTH); SoPhieu → {MaPN, MaNCC, MaNV, ThoiDiemNhan, TinhTrangPN, MaNVXacNhan, ThoiDiemXacNhan, SoHoaDonNCC, GhiChuPN} (9 PTH).

Bước 2: Không thực hiện vì mọi PTH đều có vế trái là một thuộc tính (đã đầy đủ).

Bước 3: Loại các PTH dư thừa (xét từ PTH cuối lên đầu để giữ các PTH của khóa chính):

- SoPhieu → {MaNCC, MaNV, ThoiDiemNhan, TinhTrangPN, MaNVXacNhan, ThoiDiemXacNhan, SoHoaDonNCC, GhiChuPN} (8 PTH): mỗi PTH suy ra được từ các PTH còn lại theo luật bắc cầu (ví dụ bỏ nó vẫn có SoPhieu⁺ ∋ MaNCC).

Vậy phủ tối thiểu của F_PHIEUNHAP là G_PHIEUNHAP = {MaPN → {SoPhieu, MaNCC, MaNV, ThoiDiemNhan, TinhTrangPN, MaNVXacNhan, ThoiDiemXacNhan, SoHoaDonNCC, GhiChuPN} (9 PTH); SoPhieu → {MaPN} (1 PTH)}. (G ≡ F: đã kiểm tra bằng bao đóng.)

**Xác định khóa:**

N = ∅; TG = {MaPN, SoPhieu}; D = {MaNCC, MaNV, ThoiDiemNhan, TinhTrangPN, MaNVXacNhan, ThoiDiemXacNhan, SoHoaDonNCC, GhiChuPN}.

Bảng tổ hợp (Kᵢ = N ∪ Mᵢ với Mᵢ là tập con của TG):

| Mᵢ | Kᵢ | Kᵢ⁺ | Kết luận |
|---|---|---|---|
| ∅ | ∅ | ∅ | không |
| {MaPN} | {MaPN} | Q⁺ | khóa |
| {SoPhieu} | {SoPhieu} | Q⁺ | khóa |
| {MaPN, SoPhieu} | {MaPN, SoPhieu} | Q⁺ | siêu khóa |

Các khóa: {MaPN}; {SoPhieu}.

**Xác định dạng chuẩn:**

- Đạt dạng chuẩn 1 vì mọi thuộc tính của PHIEUNHAP đều là thuộc tính đơn.
- Đạt dạng chuẩn 2 vì mọi khóa chỉ có một thuộc tính ({MaPN}; {SoPhieu}).
- Đạt dạng chuẩn 3 vì không có thuộc tính không khóa nào phụ thuộc bắc cầu vào khóa.
- Đạt BCNF vì mọi PTH không hiển nhiên đều có vế trái chứa khóa: {MaPN}; {SoPhieu}.
- Kết luận: **PHIEUNHAP đạt dạng chuẩn BCNF**.

### 2.2.19 Lược đồ quan hệ CHITIETPHIEUNHAP

Xét LĐQH CHITIETPHIEUNHAP(<u>MaPN</u><sup>FK</sup>, <u>SoDongPN</u>, <span style="text-decoration: underline dashed">MaSP</span>, SoLuongNhap, GiaNhap).

**Các phụ thuộc hàm:**

- f1: MaPN,SoDongPN → MaSP,SoLuongNhap,GiaNhap — khóa chính xác định mọi thuộc tính còn lại.

**Phủ tối thiểu của F_CHITIETPHIEUNHAP:**

Bước 1: Tách vế phải, thu được 3 PTH, mỗi PTH một thuộc tính ở vế phải: MaPN,SoDongPN → MaSP; MaPN,SoDongPN → SoLuongNhap; MaPN,SoDongPN → GiaNhap.

Bước 2: Xét vế trái {MaPN, SoDongPN}: (SoDongPN)⁺ = {SoDongPN}; (MaPN)⁺ = {MaPN}. Không chứa vế phải nên không thuộc tính nào thừa. Giữ nguyên.

Bước 3: Không có PTH dư thừa vì không PTH nào suy ra được từ các PTH còn lại.

Vậy phủ tối thiểu của F_CHITIETPHIEUNHAP là G_CHITIETPHIEUNHAP = {MaPN,SoDongPN → MaSP; MaPN,SoDongPN → SoLuongNhap; MaPN,SoDongPN → GiaNhap}. (G ≡ F: đã kiểm tra bằng bao đóng.)

**Xác định khóa:**

N = {MaPN, SoDongPN}; TG = ∅; D = {MaSP, SoLuongNhap, GiaNhap}.

{MaPN, SoDongPN}⁺ = {MaPN, SoDongPN, MaSP, SoLuongNhap, GiaNhap} = Q⁺. Vậy khóa duy nhất là {MaPN, SoDongPN}.

**Xác định dạng chuẩn:**

- Đạt dạng chuẩn 1 vì mọi thuộc tính của CHITIETPHIEUNHAP đều là thuộc tính đơn.
- Đạt dạng chuẩn 2 vì mọi thuộc tính không khóa (MaSP, SoLuongNhap, GiaNhap) phụ thuộc đầy đủ vào khóa: không có tập con thật sự của khóa nào xác định chúng.
- Đạt dạng chuẩn 3 vì không có thuộc tính không khóa nào phụ thuộc bắc cầu vào khóa.
- Đạt BCNF vì mọi PTH không hiển nhiên đều có vế trái chứa khóa: {MaPN, SoDongPN}.
- Kết luận: **CHITIETPHIEUNHAP đạt dạng chuẩn BCNF**.

### 2.2.20 Lược đồ quan hệ HANGCOSERI

Xét LĐQH HANGCOSERI(<u>MaSeri</u>, SoSeri, <span style="text-decoration: underline dashed">MaSP</span>, <span style="text-decoration: underline dashed">MaPN</span>, <span style="text-decoration: underline dashed">SoDongPN</span>, <span style="text-decoration: underline dashed">MaDH</span>, <span style="text-decoration: underline dashed">SoDongDH</span>, TinhTrangSeri, ThoiDiemNhap).

**Các phụ thuộc hàm:**

- f1: MaSeri → SoSeri,MaSP,MaPN,SoDongPN,MaDH,SoDongDH,TinhTrangSeri,ThoiDiemNhap — khóa chính xác định mọi thuộc tính còn lại.
- f2: SoSeri,MaSP → MaSeri — ràng buộc UNIQUE: giá trị không trùng nên cũng xác định mọi thuộc tính.
- f3: MaPN,SoDongPN → MaSP — Mỗi dòng phiếu nhập chỉ chứa một mặt hàng (giả thiết G2).
- f4: MaDH,SoDongDH → MaSP — Mỗi dòng đơn chỉ chứa một mặt hàng (giả thiết G2); chỉ xét khi chiếc hàng đã bán (G4).

**Phủ tối thiểu của F_HANGCOSERI:**

Bước 1: Tách vế phải, thu được 11 PTH, mỗi PTH một thuộc tính ở vế phải: MaSeri → {SoSeri, MaSP, MaPN, SoDongPN, MaDH, SoDongDH, TinhTrangSeri, ThoiDiemNhap} (8 PTH); SoSeri,MaSP → {MaSeri} (1 PTH); MaPN,SoDongPN → {MaSP} (1 PTH); MaDH,SoDongDH → {MaSP} (1 PTH).

Bước 2: Xét vế trái {MaDH, SoDongDH}: (SoDongDH)⁺ = {SoDongDH}; (MaDH)⁺ = {MaDH}. Không chứa vế phải nên không thuộc tính nào thừa. Giữ nguyên.
Bước 2: Xét vế trái {MaPN, SoDongPN}: (SoDongPN)⁺ = {SoDongPN}; (MaPN)⁺ = {MaPN}. Không chứa vế phải nên không thuộc tính nào thừa. Giữ nguyên.
Bước 2: Xét vế trái {SoSeri, MaSP}: (MaSP)⁺ = {MaSP}; (SoSeri)⁺ = {SoSeri}. Không chứa vế phải nên không thuộc tính nào thừa. Giữ nguyên.

Bước 3: Loại các PTH dư thừa (xét từ PTH cuối lên đầu để giữ các PTH của khóa chính):

- MaSeri → MaSP: bỏ nó vẫn có MaSeri⁺ ∋ MaSP.

Vậy phủ tối thiểu của F_HANGCOSERI là G_HANGCOSERI = {MaSeri → {SoSeri, MaPN, SoDongPN, MaDH, SoDongDH, TinhTrangSeri, ThoiDiemNhap} (7 PTH); SoSeri,MaSP → {MaSeri} (1 PTH); MaPN,SoDongPN → {MaSP} (1 PTH); MaDH,SoDongDH → {MaSP} (1 PTH)}. (G ≡ F: đã kiểm tra bằng bao đóng.)

**Xác định khóa:**

N = ∅; TG = {MaSeri, SoSeri, MaSP, MaPN, SoDongPN, MaDH, SoDongDH}; D = {TinhTrangSeri, ThoiDiemNhap}.

Bảng tổ hợp (Kᵢ = N ∪ Mᵢ với Mᵢ là tập con của TG). TG có 7 thuộc tính nên có 128 tổ hợp; đã tính đủ bao đóng, trong đó 41 tổ hợp có Kᵢ⁺ ≠ Q⁺ và 83 tổ hợp là siêu khóa vì chứa một khóa. Bảng chỉ ghi các tổ hợp là khóa:

| Mᵢ | Kᵢ | Kᵢ⁺ | Kết luận |
|---|---|---|---|
| {MaSeri} | {MaSeri} | Q⁺ | khóa |
| {SoSeri, MaSP} | {SoSeri, MaSP} | Q⁺ | khóa |
| {SoSeri, MaPN, SoDongPN} | {SoSeri, MaPN, SoDongPN} | Q⁺ | khóa |
| {SoSeri, MaDH, SoDongDH} | {SoSeri, MaDH, SoDongDH} | Q⁺ | khóa có điều kiện (G4) |

Các khóa: {MaSeri}; {SoSeri, MaSP}; {SoSeri, MaPN, SoDongPN}.
Khóa có điều kiện: {SoSeri, MaDH, SoDongDH}; chỉ có hiệu lực trên các bộ khác rỗng ở cột cho phép rỗng (G4), không phải khóa của toàn quan hệ.

**Xác định dạng chuẩn:**

- Đạt dạng chuẩn 1 vì mọi thuộc tính của HANGCOSERI đều là thuộc tính đơn.
- Đạt dạng chuẩn 2 vì mọi thuộc tính không khóa (MaDH, SoDongDH, TinhTrangSeri, ThoiDiemNhap) phụ thuộc đầy đủ vào khóa: không có tập con thật sự của khóa nào xác định chúng.
- Đạt dạng chuẩn 3 vì mọi PTH không hiển nhiên hoặc có vế trái là siêu khóa hoặc có vế phải là thuộc tính khóa (MaSP là thuộc tính khóa vì thuộc khóa {SoSeri, MaSP}).
- Không đạt BCNF vì có PTH {MaPN, SoDongPN} → MaSP; {MaDH, SoDongDH} → MaSP có vế trái không chứa khóa.
- Kết luận: **HANGCOSERI đạt dạng chuẩn 3NF**.

Kiểm tra ở phạm vi toàn quan hệ (không dùng PTH có điều kiện, khóa {MaSeri}; {SoSeri, MaSP}; {SoSeri, MaPN, SoDongPN}): dạng chuẩn không đổi, vẫn là 3NF.

### 2.2.21 Lược đồ quan hệ GIAODICHKHO

Xét LĐQH GIAODICHKHO(<u>MaGDK</u>, <span style="text-decoration: underline dashed">MaSP</span>, NhomKho, LoaiBienDong, SoLuongGD, ThoiDiemGD, <span style="text-decoration: underline dashed">MaNV</span>, LoaiChungTu, MaChungTu, GhiChuGD).

**Các phụ thuộc hàm:**

- f1: MaGDK → MaSP,NhomKho,LoaiBienDong,SoLuongGD,ThoiDiemGD,MaNV,LoaiChungTu,MaChungTu,GhiChuGD — khóa chính xác định mọi thuộc tính còn lại.

**Phủ tối thiểu của F_GIAODICHKHO:**

Bước 1: Tách vế phải, thu được 9 PTH, mỗi PTH một thuộc tính ở vế phải: MaGDK → {MaSP, NhomKho, LoaiBienDong, SoLuongGD, ThoiDiemGD, MaNV, LoaiChungTu, MaChungTu, GhiChuGD} (9 PTH).

Bước 2: Không thực hiện vì mọi PTH đều có vế trái là một thuộc tính (đã đầy đủ).

Bước 3: Không có PTH dư thừa vì không PTH nào suy ra được từ các PTH còn lại.

Vậy phủ tối thiểu của F_GIAODICHKHO là G_GIAODICHKHO = {MaGDK → {MaSP, NhomKho, LoaiBienDong, SoLuongGD, ThoiDiemGD, MaNV, LoaiChungTu, MaChungTu, GhiChuGD} (9 PTH)}. (G ≡ F: đã kiểm tra bằng bao đóng.)

**Xác định khóa:**

N = {MaGDK}; TG = ∅; D = {MaSP, NhomKho, LoaiBienDong, SoLuongGD, ThoiDiemGD, MaNV, LoaiChungTu, MaChungTu, GhiChuGD}.

{MaGDK}⁺ = {MaGDK, MaSP, NhomKho, LoaiBienDong, SoLuongGD, ThoiDiemGD, MaNV, LoaiChungTu, MaChungTu, GhiChuGD} = Q⁺. Vậy khóa duy nhất là {MaGDK}.

**Xác định dạng chuẩn:**

- Đạt dạng chuẩn 1 vì mọi thuộc tính của GIAODICHKHO đều là thuộc tính đơn.
- Đạt dạng chuẩn 2 vì mọi khóa chỉ có một thuộc tính ({MaGDK}).
- Đạt dạng chuẩn 3 vì không có thuộc tính không khóa nào phụ thuộc bắc cầu vào khóa.
- Đạt BCNF vì mọi PTH không hiển nhiên đều có vế trái chứa khóa: {MaGDK}.
- Kết luận: **GIAODICHKHO đạt dạng chuẩn BCNF**.

### 2.2.22 Lược đồ quan hệ HOSODOITRA

Xét LĐQH HOSODOITRA(<u>MaHS</u>, <span style="text-decoration: underline dashed">MaDH</span>, <span style="text-decoration: underline dashed">MaNV</span>, NgayDeNghi, LoaiTruongHop, LyDoDoiTra, TinhTrangHS, HinhThucXuLy).

**Các phụ thuộc hàm:**

- f1: MaHS → MaDH,MaNV,NgayDeNghi,LoaiTruongHop,LyDoDoiTra,TinhTrangHS,HinhThucXuLy — khóa chính xác định mọi thuộc tính còn lại.

**Phủ tối thiểu của F_HOSODOITRA:**

Bước 1: Tách vế phải, thu được 7 PTH, mỗi PTH một thuộc tính ở vế phải: MaHS → MaDH; MaHS → MaNV; MaHS → NgayDeNghi; MaHS → LoaiTruongHop; MaHS → LyDoDoiTra; MaHS → TinhTrangHS; MaHS → HinhThucXuLy.

Bước 2: Không thực hiện vì mọi PTH đều có vế trái là một thuộc tính (đã đầy đủ).

Bước 3: Không có PTH dư thừa vì không PTH nào suy ra được từ các PTH còn lại.

Vậy phủ tối thiểu của F_HOSODOITRA là G_HOSODOITRA = {MaHS → MaDH; MaHS → MaNV; MaHS → NgayDeNghi; MaHS → LoaiTruongHop; MaHS → LyDoDoiTra; MaHS → TinhTrangHS; MaHS → HinhThucXuLy}. (G ≡ F: đã kiểm tra bằng bao đóng.)

**Xác định khóa:**

N = {MaHS}; TG = ∅; D = {MaDH, MaNV, NgayDeNghi, LoaiTruongHop, LyDoDoiTra, TinhTrangHS, HinhThucXuLy}.

{MaHS}⁺ = {MaHS, MaDH, MaNV, NgayDeNghi, LoaiTruongHop, LyDoDoiTra, TinhTrangHS, HinhThucXuLy} = Q⁺. Vậy khóa duy nhất là {MaHS}.

**Xác định dạng chuẩn:**

- Đạt dạng chuẩn 1 vì mọi thuộc tính của HOSODOITRA đều là thuộc tính đơn.
- Đạt dạng chuẩn 2 vì mọi khóa chỉ có một thuộc tính ({MaHS}).
- Đạt dạng chuẩn 3 vì không có thuộc tính không khóa nào phụ thuộc bắc cầu vào khóa.
- Đạt BCNF vì mọi PTH không hiển nhiên đều có vế trái chứa khóa: {MaHS}.
- Kết luận: **HOSODOITRA đạt dạng chuẩn BCNF**.

### 2.2.23 Lược đồ quan hệ CHITIETTRA

Xét LĐQH CHITIETTRA(<u>MaHS</u><sup>FK</sup>, <u>SoDongTra</u>, <span style="text-decoration: underline dashed">SoDongDH</span>, <span style="text-decoration: underline dashed">MaDH</span>, SoLuongTra, <span style="text-decoration: underline dashed">MaSeri</span>).

**Các phụ thuộc hàm:**

- f1: MaHS,SoDongTra → SoDongDH,MaDH,SoLuongTra,MaSeri — khóa chính xác định mọi thuộc tính còn lại.
- f2: MaHS,MaSeri → SoDongTra — Trong một hồ sơ, mỗi chiếc hàng chỉ ghi một lần; chỉ xét trên dòng trả có số seri (giả thiết G4).
- f3: MaHS → MaDH — Mỗi hồ sơ đổi trả lập cho đúng một đơn gốc.

**Phủ tối thiểu của F_CHITIETTRA:**

Bước 1: Tách vế phải, thu được 6 PTH, mỗi PTH một thuộc tính ở vế phải: MaHS,SoDongTra → SoDongDH; MaHS,SoDongTra → MaDH; MaHS,SoDongTra → SoLuongTra; MaHS,SoDongTra → MaSeri; MaHS,MaSeri → SoDongTra; MaHS → MaDH.

Bước 2: Xét MaHS,SoDongTra → MaDH: thuộc tính SoDongTra ở vế trái là thừa vì vế phải suy ra được khi bỏ SoDongTra. Thay bằng MaHS → MaDH.

Bước 3: Loại các PTH dư thừa (xét từ PTH cuối lên đầu để giữ các PTH của khóa chính):

- MaHS → MaDH: trùng với một PTH đã có.

Vậy phủ tối thiểu của F_CHITIETTRA là G_CHITIETTRA = {MaHS,SoDongTra → SoDongDH; MaHS → MaDH; MaHS,SoDongTra → SoLuongTra; MaHS,SoDongTra → MaSeri; MaHS,MaSeri → SoDongTra}. (G ≡ F: đã kiểm tra bằng bao đóng.)

**Xác định khóa:**

N = {MaHS}; TG = {SoDongTra, MaSeri}; D = {SoDongDH, MaDH, SoLuongTra}.

Bảng tổ hợp (Kᵢ = N ∪ Mᵢ với Mᵢ là tập con của TG):

| Mᵢ | Kᵢ | Kᵢ⁺ | Kết luận |
|---|---|---|---|
| ∅ | {MaHS} | {MaHS, MaDH} | không |
| {SoDongTra} | {MaHS, SoDongTra} | Q⁺ | khóa |
| {MaSeri} | {MaHS, MaSeri} | Q⁺ | khóa có điều kiện (G4) |
| {SoDongTra, MaSeri} | {MaHS, SoDongTra, MaSeri} | Q⁺ | siêu khóa |

Các khóa: {MaHS, SoDongTra}.
Khóa có điều kiện: {MaHS, MaSeri}; chỉ có hiệu lực trên các bộ khác rỗng ở cột cho phép rỗng (G4), không phải khóa của toàn quan hệ.

**Xác định dạng chuẩn:**

- Đạt dạng chuẩn 1 vì mọi thuộc tính của CHITIETTRA đều là thuộc tính đơn.
- Không đạt dạng chuẩn 2 vì thuộc tính không khóa MaDH phụ thuộc vào {MaHS}, là một phần của khóa {MaHS, SoDongTra}.
- Không đạt dạng chuẩn 3 vì chưa đạt dạng chuẩn 2.
- Không đạt BCNF vì chưa đạt dạng chuẩn 3.
- Kết luận: **CHITIETTRA đạt dạng chuẩn 1NF**.

Kiểm tra ở phạm vi toàn quan hệ (không dùng PTH có điều kiện, khóa {MaHS, SoDongTra}): dạng chuẩn không đổi, vẫn là 1NF.

### 2.2.24 Lược đồ quan hệ LANNHANLAI

Xét LĐQH LANNHANLAI(<u>MaNhanLai</u>, <span style="text-decoration: underline dashed">MaHS</span>, ThoiDiemNhanLai, <span style="text-decoration: underline dashed">MaNV</span>, KetLuan, NhomSauKiemTra, ThoiDiemDuyet, <span style="text-decoration: underline dashed">MaNVDuyet</span>).

**Các phụ thuộc hàm:**

- f1: MaNhanLai → MaHS,ThoiDiemNhanLai,MaNV,KetLuan,NhomSauKiemTra,ThoiDiemDuyet,MaNVDuyet — khóa chính xác định mọi thuộc tính còn lại.

**Phủ tối thiểu của F_LANNHANLAI:**

Bước 1: Tách vế phải, thu được 7 PTH, mỗi PTH một thuộc tính ở vế phải: MaNhanLai → MaHS; MaNhanLai → ThoiDiemNhanLai; MaNhanLai → MaNV; MaNhanLai → KetLuan; MaNhanLai → NhomSauKiemTra; MaNhanLai → ThoiDiemDuyet; MaNhanLai → MaNVDuyet.

Bước 2: Không thực hiện vì mọi PTH đều có vế trái là một thuộc tính (đã đầy đủ).

Bước 3: Không có PTH dư thừa vì không PTH nào suy ra được từ các PTH còn lại.

Vậy phủ tối thiểu của F_LANNHANLAI là G_LANNHANLAI = {MaNhanLai → MaHS; MaNhanLai → ThoiDiemNhanLai; MaNhanLai → MaNV; MaNhanLai → KetLuan; MaNhanLai → NhomSauKiemTra; MaNhanLai → ThoiDiemDuyet; MaNhanLai → MaNVDuyet}. (G ≡ F: đã kiểm tra bằng bao đóng.)

**Xác định khóa:**

N = {MaNhanLai}; TG = ∅; D = {MaHS, ThoiDiemNhanLai, MaNV, KetLuan, NhomSauKiemTra, ThoiDiemDuyet, MaNVDuyet}.

{MaNhanLai}⁺ = {MaNhanLai, MaHS, ThoiDiemNhanLai, MaNV, KetLuan, NhomSauKiemTra, ThoiDiemDuyet, MaNVDuyet} = Q⁺. Vậy khóa duy nhất là {MaNhanLai}.

**Xác định dạng chuẩn:**

- Đạt dạng chuẩn 1 vì mọi thuộc tính của LANNHANLAI đều là thuộc tính đơn.
- Đạt dạng chuẩn 2 vì mọi khóa chỉ có một thuộc tính ({MaNhanLai}).
- Đạt dạng chuẩn 3 vì không có thuộc tính không khóa nào phụ thuộc bắc cầu vào khóa.
- Đạt BCNF vì mọi PTH không hiển nhiên đều có vế trái chứa khóa: {MaNhanLai}.
- Kết luận: **LANNHANLAI đạt dạng chuẩn BCNF**.

### 2.2.25 Lược đồ quan hệ KHOANHOAN

Xét LĐQH KHOANHOAN(<u>MaHoan</u>, <span style="text-decoration: underline dashed">MaTT</span>, <span style="text-decoration: underline dashed">MaHS</span>, <span style="text-decoration: underline dashed">MaPhieuBH</span>, <span style="text-decoration: underline dashed">MaNV</span>, SoTienHoan, PhuongThucHoan, ThoiDiemDuyetHoan, ThoiDiemChi, <span style="text-decoration: underline dashed">MaNVChi</span>).

**Các phụ thuộc hàm:**

- f1: MaHoan → MaTT,MaHS,MaPhieuBH,MaNV,SoTienHoan,PhuongThucHoan,ThoiDiemDuyetHoan,ThoiDiemChi,MaNVChi — khóa chính xác định mọi thuộc tính còn lại.

**Phủ tối thiểu của F_KHOANHOAN:**

Bước 1: Tách vế phải, thu được 9 PTH, mỗi PTH một thuộc tính ở vế phải: MaHoan → {MaTT, MaHS, MaPhieuBH, MaNV, SoTienHoan, PhuongThucHoan, ThoiDiemDuyetHoan, ThoiDiemChi, MaNVChi} (9 PTH).

Bước 2: Không thực hiện vì mọi PTH đều có vế trái là một thuộc tính (đã đầy đủ).

Bước 3: Không có PTH dư thừa vì không PTH nào suy ra được từ các PTH còn lại.

Vậy phủ tối thiểu của F_KHOANHOAN là G_KHOANHOAN = {MaHoan → {MaTT, MaHS, MaPhieuBH, MaNV, SoTienHoan, PhuongThucHoan, ThoiDiemDuyetHoan, ThoiDiemChi, MaNVChi} (9 PTH)}. (G ≡ F: đã kiểm tra bằng bao đóng.)

**Xác định khóa:**

N = {MaHoan}; TG = ∅; D = {MaTT, MaHS, MaPhieuBH, MaNV, SoTienHoan, PhuongThucHoan, ThoiDiemDuyetHoan, ThoiDiemChi, MaNVChi}.

{MaHoan}⁺ = {MaHoan, MaTT, MaHS, MaPhieuBH, MaNV, SoTienHoan, PhuongThucHoan, ThoiDiemDuyetHoan, ThoiDiemChi, MaNVChi} = Q⁺. Vậy khóa duy nhất là {MaHoan}.

**Xác định dạng chuẩn:**

- Đạt dạng chuẩn 1 vì mọi thuộc tính của KHOANHOAN đều là thuộc tính đơn.
- Đạt dạng chuẩn 2 vì mọi khóa chỉ có một thuộc tính ({MaHoan}).
- Đạt dạng chuẩn 3 vì không có thuộc tính không khóa nào phụ thuộc bắc cầu vào khóa.
- Đạt BCNF vì mọi PTH không hiển nhiên đều có vế trái chứa khóa: {MaHoan}.
- Kết luận: **KHOANHOAN đạt dạng chuẩn BCNF**.

### 2.2.26 Lược đồ quan hệ PHIEUBAOHANH

Xét LĐQH PHIEUBAOHANH(<u>MaPhieuBH</u>, <span style="text-decoration: underline dashed">MaSeri</span>, <span style="text-decoration: underline dashed">MaSP</span>, <span style="text-decoration: underline dashed">MaDH</span>, <span style="text-decoration: underline dashed">SoDongDH</span>, MoTaLoi, PhuKienDiKem, NgayNhan, NgayHenTra, NgayTraThucTe, TinhTrangBH, KetQuaBH, LyDoTuChoi, <span style="text-decoration: underline dashed">MaNV</span>).

**Các phụ thuộc hàm:**

- f1: MaPhieuBH → MaSeri,MaSP,MaDH,SoDongDH,MoTaLoi,PhuKienDiKem,NgayNhan,NgayHenTra,NgayTraThucTe,TinhTrangBH,KetQuaBH,LyDoTuChoi,MaNV — khóa chính xác định mọi thuộc tính còn lại.
- f2: MaDH,SoDongDH → MaSP — Mỗi dòng đơn chỉ chứa một mặt hàng (giả thiết G2).
- f3: MaSeri → MaSP — Mỗi chiếc hàng chỉ thuộc một mặt hàng; chỉ xét khi phiếu có số seri (giả thiết G4).

**Phủ tối thiểu của F_PHIEUBAOHANH:**

Bước 1: Tách vế phải, thu được 15 PTH, mỗi PTH một thuộc tính ở vế phải: MaPhieuBH → {MaSeri, MaSP, MaDH, SoDongDH, MoTaLoi, PhuKienDiKem, NgayNhan, NgayHenTra, NgayTraThucTe, TinhTrangBH, KetQuaBH, LyDoTuChoi, MaNV} (13 PTH); MaDH,SoDongDH → {MaSP} (1 PTH); MaSeri → {MaSP} (1 PTH).

Bước 2: Xét vế trái {MaDH, SoDongDH}: (SoDongDH)⁺ = {SoDongDH}; (MaDH)⁺ = {MaDH}. Không chứa vế phải nên không thuộc tính nào thừa. Giữ nguyên.

Bước 3: Loại các PTH dư thừa (xét từ PTH cuối lên đầu để giữ các PTH của khóa chính):

- MaPhieuBH → MaSP: bỏ nó vẫn có MaPhieuBH⁺ ∋ MaSP.

Vậy phủ tối thiểu của F_PHIEUBAOHANH là G_PHIEUBAOHANH = {MaPhieuBH → {MaSeri, MaDH, SoDongDH, MoTaLoi, PhuKienDiKem, NgayNhan, NgayHenTra, NgayTraThucTe, TinhTrangBH, KetQuaBH, LyDoTuChoi, MaNV} (12 PTH); MaDH,SoDongDH → {MaSP} (1 PTH); MaSeri → {MaSP} (1 PTH)}. (G ≡ F: đã kiểm tra bằng bao đóng.)

**Xác định khóa:**

N = {MaPhieuBH}; TG = {MaSeri, MaDH, SoDongDH}; D = {MaSP, MoTaLoi, PhuKienDiKem, NgayNhan, NgayHenTra, NgayTraThucTe, TinhTrangBH, KetQuaBH, LyDoTuChoi, MaNV}.

{MaPhieuBH}⁺ = {MaPhieuBH, MaSeri, MaSP, MaDH, SoDongDH, MoTaLoi, PhuKienDiKem, NgayNhan, NgayHenTra, NgayTraThucTe, TinhTrangBH, KetQuaBH, LyDoTuChoi, MaNV} = Q⁺. Vậy khóa duy nhất là {MaPhieuBH}.

**Xác định dạng chuẩn:**

- Đạt dạng chuẩn 1 vì mọi thuộc tính của PHIEUBAOHANH đều là thuộc tính đơn.
- Đạt dạng chuẩn 2 vì mọi khóa chỉ có một thuộc tính ({MaPhieuBH}).
- Không đạt dạng chuẩn 3 vì MaSP là thuộc tính không khóa phụ thuộc bắc cầu vào khóa: {MaDH, SoDongDH} → MaSP mà {MaDH, SoDongDH} không là siêu khóa.
- Không đạt BCNF vì chưa đạt dạng chuẩn 3.
- Kết luận: **PHIEUBAOHANH đạt dạng chuẩn 2NF**.

Kiểm tra ở phạm vi toàn quan hệ (không dùng PTH có điều kiện, khóa {MaPhieuBH}): dạng chuẩn không đổi, vẫn là 2NF.

### 2.2.27 Đánh giá lược đồ ban đầu

| STT | Quan hệ | Khóa của toàn quan hệ | Dạng chuẩn |
|---|---|---|---|
| 1 | LOAIHANG | {MaLoai} | BCNF |
| 2 | THUONGHIEU | {MaTH}; {TenTH} | BCNF |
| 3 | MATHANG | {MaSP}; {SKU} | BCNF |
| 4 | ANHMATHANG | {MaAnh}; {MaSP, ViTriAnh} | BCNF |
| 5 | DINHNGHIATHONGSO | {MaTS} | BCNF |
| 6 | GIATRITHONGSO | {MaSP, MaTS} | BCNF |
| 7 | KHACHHANG | {MaKH} | chưa đạt 1NF |
| 8 | NHANVIEN | {MaNV} | chưa đạt 1NF |
| 9 | TAIKHOAN | {MaTK}; {TenDangNhap} (có điều kiện: {MaKH}; {MaNV}) | BCNF |
| 10 | NHACUNGCAP | {MaNCC}; {TenNCC} | BCNF |
| 11 | MAGIAMGIA | {MaMG}; {CodeMG} | BCNF |
| 12 | DONHANG | {MaDH}; {SoDH} | BCNF |
| 13 | CHITIETDONHANG | {MaDH, SoDongDH} | BCNF |
| 14 | THANHTOAN | {MaTT} | BCNF |
| 15 | PHIEUGIAO | {MaGiao}; {MaDH} | BCNF |
| 16 | LANGIAO | {MaGiao, SoLan} | BCNF |
| 17 | PHIEUNHAP | {MaPN}; {SoPhieu} | BCNF |
| 18 | CHITIETPHIEUNHAP | {MaPN, SoDongPN} | BCNF |
| 19 | HANGCOSERI | {MaSeri}; {SoSeri, MaSP}; {SoSeri, MaPN, SoDongPN} (có điều kiện: {SoSeri, MaDH, SoDongDH}) | 3NF |
| 20 | GIAODICHKHO | {MaGDK} | BCNF |
| 21 | HOSODOITRA | {MaHS} | BCNF |
| 22 | CHITIETTRA | {MaHS, SoDongTra} (có điều kiện: {MaHS, MaSeri}) | 1NF |
| 23 | LANNHANLAI | {MaNhanLai} | BCNF |
| 24 | KHOANHOAN | {MaHoan} | BCNF |
| 25 | PHIEUBAOHANH | {MaPhieuBH} | 2NF |

*Bảng 2.2: Đánh giá dạng chuẩn của 25 quan hệ ban đầu*

Phần “có điều kiện” là ràng buộc duy nhất trên các bộ khác rỗng (G4), không phải khóa của toàn quan hệ.

Thống kê: 1NF: 1 quan hệ, 2NF: 1 quan hệ, 3NF: 1 quan hệ, BCNF: 20 quan hệ, chưa đạt 1NF: 2 quan hệ. Dạng chuẩn của cả lược đồ là dạng chuẩn thấp nhất của các quan hệ, tức **chưa đạt 1NF** (do KHACHHANG và NHANVIEN có họ tên là thuộc tính kép). Ngay cả khi tách họ tên, lược đồ vẫn chỉ đạt 1NF vì CHITIETTRA còn phụ thuộc bộ phận (1NF), PHIEUBAOHANH còn phụ thuộc bắc cầu (2NF) và HANGCOSERI còn vi phạm BCNF (3NF). Các quan hệ này được cải tiến ở mục 2.3.

## 2.3 CẢI TIẾN LƯỢC ĐỒ

### 2.3.1 Phương pháp

**Thuật toán phân rã (định lý Delobel):** nếu f: X → A ∈ F⁺ và XA là tập con thật sự của Q⁺ thì tách Q thành Q₁(X, A) và Q₂(Q⁺ \ A) là phép tách bảo toàn thông tin. B1 bỏ khỏi F các PTH có VT ∪ VP = Q⁺; B2 nếu F* = ∅ thì dừng, ngược lại chọn PTH “gây xấu” (vế trái không chứa khóa), tách rồi phân rã đệ quy. Kết quả đạt BCNF, bảo toàn thông tin nhưng có thể mất PTH.

**Thuật toán tổng hợp cải tiến:** B1 tìm phủ tối thiểu; B2 nhóm các PTH cùng vế trái; B3 gộp các nhóm có vế trái phụ thuộc lẫn nhau; B4 mỗi nhóm thành một quan hệ con; B5 tìm khóa của Q; B6 nếu chưa quan hệ con nào chứa khóa của Q thì thêm quan hệ chứa một khóa. Kết quả đạt 3NF, bảo toàn PTH, và bảo toàn thông tin sau B5–B6, nhưng có thể còn trùng lắp.

**Chứng minh:** (a) bảo toàn PTH: đặt F' = ∪Fᵢ, cần mọi f' ∈ F' \ F thuộc F⁺ và mọi f ∈ F \ F' thuộc F'⁺; (b) bảo toàn thông tin: lập bảng a/b (cột là thuộc tính của Q, dòng là các Qᵢ; ô là aⱼ nếu thuộc tính ∈ Qᵢ, ngược lại bₖ), áp các PTH để đồng nhất ký hiệu; có một dòng toàn a thì bảo toàn. Chữ cái A, B, C… ứng với thứ tự cột của quan hệ trong lược đồ ban đầu (bảng ánh xạ nhắc lại ở từng quan hệ).

### 2.3.2 Đạt dạng chuẩn 1: tách họ tên

KHACHHANG và NHANVIEN chưa đạt dạng chuẩn 1 vì họ tên là thuộc tính kép. Phép thử theo bài giảng: để đếm hoặc lọc khách tên “Mỹ” cửa hàng phải viết `WHERE HoTenKH LIKE N'%Mỹ'`, tức dùng một phần của giá trị. Cách sửa không cần phân rã quan hệ: **thay cột HoTenKH bằng HoLotKH và TenKH** (tương tự HoLotNV, TenNV). Sau khi tách, truy vấn trở thành `WHERE TenKH = N'Mỹ'`. Phép tách không làm mất thông tin vì họ tên ghép lại từ HoLot và Ten; PTH đổi thành MaKH → HoLotKH, TenKH,… nên khóa và dạng chuẩn BCNF của quan hệ không đổi. Giới hạn: tên người Việt có thể có nhiều chữ nên quy ước “Ten là từ cuối cùng”; đây là quy ước nhập liệu, không kiểm tra được bằng PTH.

Tiêu chí này áp dụng thống nhất cho mọi cột văn bản: một cột chỉ phải tách khi cửa hàng cần dùng một phần giá trị của nó. Theo **giả thiết** của nhóm, các cột sau không có nhu cầu đó nên được xem là thuộc tính đơn. TenNguoiNhan và NguoiLienHeNCC ghi tên để liên hệ; cửa hàng tra đơn theo số đơn, số điện thoại và tra nhà cung cấp theo tên công ty, không tìm theo tên gọi ở hai cột này. DiaChiGiao và DiaChiNCC ghi nguyên một địa chỉ để giao hàng và liên hệ, không lọc hay thống kê theo tỉnh, quận; phí giao được ghi trực tiếp trên đơn nên không phải suy từ địa chỉ. PhuKienDiKem là ghi chú tự do để đối chiếu khi trả khách, không tra cứu hay đếm theo từng phụ kiện; nếu sau này cần theo dõi từng phụ kiện thì tách thành quan hệ riêng.

### 2.3.3 CHITIETTRA: từ 1NF lên BCNF

Ánh xạ chữ cái: A = MaHS, B = SoDongTra, C = SoDongDH, D = MaDH, E = SoLuongTra, F = MaSeri.
F (phủ tối thiểu G): MaHS,SoDongTra → SoDongDH; MaHS → MaDH; MaHS,SoDongTra → SoLuongTra; MaHS,SoDongTra → MaSeri; MaHS,MaSeri → SoDongTra. Khóa: {MaHS, SoDongTra}; khóa có điều kiện trên dòng trả có số seri: {MaHS, MaSeri} (G4). Vi phạm: MaHS → MaDH có vế trái là một phần của khóa nên MaDH phụ thuộc bộ phận (chưa đạt 2NF).

**Phân rã theo thuật toán.** B1: loại khỏi F PTH có VT ∪ VP = Q⁺ (PTH của khóa chính MaHS,SoDongTra → SoDongDH,MaDH,SoLuongTra,MaSeri); còn F* = {MaHS,MaSeri → SoDongTra; MaHS → MaDH} ≠ ∅. B2: chọn PTH gây xấu **MaHS → MaDH** (vế trái là một phần của khóa). Tách Q₁ = {MaHS, MaDH} và Q₂ = Q⁺ \ {MaDH}.

**Phép tách CHITIETTRA thành Q₁ và Q₂**

Các quan hệ con và PTH chiếu (Fᵢ):

- **Q1**(MaHS, MaDH): F = {MaHS → MaDH}
- **Q2**(MaHS, SoDongTra, SoDongDH, SoLuongTra, MaSeri): F = {MaHS,SoDongTra → SoDongDH; MaHS,SoDongTra → SoLuongTra; MaHS,SoDongTra → MaSeri; MaHS,MaSeri → SoDongTra}

Ký hiệu cột gộp: Z = {SoDongDH, SoLuongTra} (các thuộc tính này chỉ phụ thuộc vào cùng một khóa và có cùng cách xuất hiện ở các quan hệ con).

Kiểm tra **bảo toàn thông tin** bằng bảng a/b của giáo trình. Bảng khởi tạo:

| T | A | B | Z | D | F |
|---|---|---|---|---|---|
| Q1 | a1 | b1 | b2 | a4 | b3 |
| Q2 | a1 | a2 | a3 | b4 | a5 |

Biến đổi theo PTH của F:

- Hai dòng Q1 và Q2 cùng giá trị ở A; theo PTH A → D, ô cột D: b4 thành a4.

Bảng sau biến đổi:

| T | A | B | Z | D | F |
|---|---|---|---|---|---|
| Q1 | a1 | b1 | b2 | a4 | b3 |
| Q2 | a1 | a2 | a3 | b4 ⇒ a4 | a5 |

Có một dòng chứa toàn ký hiệu a → **bảo toàn thông tin**.

Kiểm tra **bảo toàn PTH** (cách của bài giảng): F' = ∪Fᵢ = {MaHS → MaDH; MaHS,SoDongTra → SoDongDH; MaHS,SoDongTra → SoLuongTra; MaHS,SoDongTra → MaSeri; MaHS,MaSeri → SoDongTra}.

- (1) Mọi f' ∈ F' \ F đều thuộc F⁺ vì mỗi Fᵢ là PTH chiếu từ F⁺.
- (2) Mọi f ∈ F \ F' phải thuộc F'⁺. Kiểm tra từng PTH của F bằng bao đóng theo F':
  - MaHS,SoDongTra → {SoDongDH, SoLuongTra, MaSeri}: (MaHS,SoDongTra)⁺_F' = Q⁺ chứa các thuộc tính vế phải → thỏa.
  - MaHS → {MaDH}: (MaHS)⁺_F' = {MaHS, MaDH} chứa các thuộc tính vế phải → thỏa.
  - MaHS,MaSeri → {SoDongTra}: (MaHS,MaSeri)⁺_F' = Q⁺ chứa các thuộc tính vế phải → thỏa.

**Kết luận: bảo toàn PTH** (thỏa (1) và (2)).

Dạng chuẩn các quan hệ con: Q1: BCNF (khóa {MaHS}); Q2: BCNF (khóa {MaHS, SoDongTra}; khóa có điều kiện {MaHS, MaSeri}).

Q₁ **trùng với phép chiếu (MaHS, MaDH) của HOSODOITRA**, nên không tạo quan hệ mới: chỉ **bỏ cột MaDH khỏi CHITIETTRA**; dòng đơn được trả là (HOSODOITRA.MaDH, SoDongDH). **CHITIETTRA nâng từ 1NF lên BCNF.**

![Hình 2.1: Phân rã CHITIETTRA theo phụ thuộc hàm MaHS → MaDH](hinh/phan_ra_chitiettra.png)

*Hình 2.1: Phân rã CHITIETTRA theo phụ thuộc hàm MaHS → MaDH*

### 2.3.4 PHIEUBAOHANH: từ 2NF lên BCNF

Ánh xạ chữ cái: A = MaPhieuBH, B = MaSeri, C = MaSP, D = MaDH, E = SoDongDH, F = MoTaLoi, G = PhuKienDiKem, H = NgayNhan, I = NgayHenTra, J = NgayTraThucTe, K = TinhTrangBH, L = KetQuaBH, M = LyDoTuChoi, N = MaNV.
F (phủ tối thiểu G): MaPhieuBH → {MaSeri, MaDH, SoDongDH, MoTaLoi, PhuKienDiKem, NgayNhan, NgayHenTra, NgayTraThucTe, TinhTrangBH, KetQuaBH, LyDoTuChoi, MaNV} (12 PTH); MaDH,SoDongDH → {MaSP} (1 PTH); MaSeri → {MaSP} (1 PTH). Khóa duy nhất {MaPhieuBH}. Vi phạm: (MaDH, SoDongDH) → MaSP và MaSeri → MaSP có vế trái không phải siêu khóa và MaSP không là thuộc tính khóa (bắc cầu).

**Cách 1: thuật toán phân rã.** B1: loại PTH của khóa chính (VT ∪ VP = Q⁺); còn F* = {MaDH,SoDongDH → MaSP; MaSeri → MaSP} ≠ ∅. B2: chọn **MaSeri → MaSP** (vế trái không chứa khóa). Tách Q₁{MaSeri, MaSP} và Q₂ = Q⁺ \ {MaSP}.

**Phép tách PHIEUBAOHANH bằng phân rã**

Các quan hệ con và PTH chiếu (Fᵢ):

- **Q1**(MaSeri, MaSP): F = {MaSeri → MaSP}
- **Q2**(MaPhieuBH, MaSeri, MaDH, SoDongDH, MoTaLoi, PhuKienDiKem, NgayNhan, NgayHenTra, NgayTraThucTe, TinhTrangBH, KetQuaBH, LyDoTuChoi, MaNV): F = {MaPhieuBH → {MaSeri, MaDH, SoDongDH, MoTaLoi, PhuKienDiKem, NgayNhan, NgayHenTra, NgayTraThucTe, TinhTrangBH, KetQuaBH, LyDoTuChoi, MaNV} (12 PTH)}

Ký hiệu cột gộp: Z = {MoTaLoi, PhuKienDiKem, NgayNhan, NgayHenTra, NgayTraThucTe, TinhTrangBH, KetQuaBH, LyDoTuChoi, MaNV} (các thuộc tính này chỉ phụ thuộc vào cùng một khóa và có cùng cách xuất hiện ở các quan hệ con).

Kiểm tra **bảo toàn thông tin** bằng bảng a/b của giáo trình. Bảng khởi tạo:

| T | A | B | C | D | E | Z |
|---|---|---|---|---|---|---|
| Q1 | b1 | a2 | a3 | b2 | b3 | b4 |
| Q2 | a1 | a2 | b5 | a4 | a5 | a6 |

Biến đổi theo PTH của F:

- Hai dòng Q1 và Q2 cùng giá trị ở B; theo PTH B → C, ô cột C: b5 thành a3.

Bảng sau biến đổi:

| T | A | B | C | D | E | Z |
|---|---|---|---|---|---|---|
| Q1 | b1 | a2 | a3 | b2 | b3 | b4 |
| Q2 | a1 | a2 | b5 ⇒ a3 | a4 | a5 | a6 |

Có một dòng chứa toàn ký hiệu a → **bảo toàn thông tin**.

Kiểm tra **bảo toàn PTH** (cách của bài giảng): F' = ∪Fᵢ = {MaSeri → {MaSP} (1 PTH); MaPhieuBH → {MaSeri, MaDH, SoDongDH, MoTaLoi, PhuKienDiKem, NgayNhan, NgayHenTra, NgayTraThucTe, TinhTrangBH, KetQuaBH, LyDoTuChoi, MaNV} (12 PTH)}.

- (1) Mọi f' ∈ F' \ F đều thuộc F⁺ vì mỗi Fᵢ là PTH chiếu từ F⁺.
- (2) Mọi f ∈ F \ F' phải thuộc F'⁺. Kiểm tra từng PTH của F bằng bao đóng theo F':
  - MaPhieuBH → {MaSeri, MaDH, SoDongDH, MoTaLoi, PhuKienDiKem, NgayNhan, NgayHenTra, NgayTraThucTe, TinhTrangBH, KetQuaBH, LyDoTuChoi, MaNV}: (MaPhieuBH)⁺_F' = Q⁺ chứa các thuộc tính vế phải → thỏa.
  - MaDH,SoDongDH → MaSP: (MaDH,SoDongDH)⁺_F' = {MaDH, SoDongDH} ∌ MaSP → **không thỏa**.
  - MaSeri → {MaSP}: (MaSeri)⁺_F' = {MaSeri, MaSP} chứa các thuộc tính vế phải → thỏa.

**Kết luận: không bảo toàn PTH** (thỏa (1) nhưng không thỏa (2)); PTH bị mất: {MaDH, SoDongDH} → MaSP.

Dạng chuẩn các quan hệ con: Q1: BCNF (khóa {MaSeri}); Q2: BCNF (khóa {MaPhieuBH}).

**Giới hạn của Cách 1.** MaSeri → MaSP là PTH có điều kiện (G4), nên chứng minh trên chỉ đúng với các phiếu có số seri. Phiếu của hàng không theo dõi seri có MaSeri rỗng: Q₁ không giữ được MaSP của các phiếu này và phép nối trong làm mất chúng. Vì vậy Cách 1 không dùng làm lược đồ cuối.

**Cách 2: thuật toán tổng hợp cải tiến.** B1: phủ tối thiểu G như trên. B2: nhóm theo vế trái: F₁ (MaPhieuBH), F₂ (MaDH, SoDongDH), F₃ (MaSeri). B3: không có hai vế trái phụ thuộc lẫn nhau. B4: R₁ gồm MaPhieuBH và các thuộc tính phụ thuộc vào nó (trừ MaSP); R₂{MaDH, SoDongDH, MaSP}; R₃{MaSeri, MaSP}. B5–B6: khóa MaPhieuBH nằm trong R₁ nên không thêm quan hệ.

**Phép tách PHIEUBAOHANH bằng tổng hợp**

Các quan hệ con và PTH chiếu (Fᵢ):

- **R1**(MaPhieuBH, MaSeri, MaDH, SoDongDH, MoTaLoi, PhuKienDiKem, NgayNhan, NgayHenTra, NgayTraThucTe, TinhTrangBH, KetQuaBH, LyDoTuChoi, MaNV): F = {MaPhieuBH → {MaSeri, MaDH, SoDongDH, MoTaLoi, PhuKienDiKem, NgayNhan, NgayHenTra, NgayTraThucTe, TinhTrangBH, KetQuaBH, LyDoTuChoi, MaNV} (12 PTH)}
- **R2**(MaSP, MaDH, SoDongDH): F = {MaDH,SoDongDH → MaSP}
- **R3**(MaSeri, MaSP): F = {MaSeri → MaSP}

Ký hiệu cột gộp: Z = {MoTaLoi, PhuKienDiKem, NgayNhan, NgayHenTra, NgayTraThucTe, TinhTrangBH, KetQuaBH, LyDoTuChoi, MaNV} (các thuộc tính này chỉ phụ thuộc vào cùng một khóa và có cùng cách xuất hiện ở các quan hệ con).

Kiểm tra **bảo toàn thông tin** bằng bảng a/b của giáo trình. Bảng khởi tạo:

| T | A | B | C | D | E | Z |
|---|---|---|---|---|---|---|
| R1 | a1 | a2 | b1 | a4 | a5 | a6 |
| R2 | b2 | b3 | a3 | a4 | a5 | b4 |
| R3 | b5 | a2 | a3 | b6 | b7 | b8 |

Biến đổi theo PTH của F:

- Hai dòng R1 và R2 cùng giá trị ở D,E; theo PTH D,E → C, ô cột C: b1 thành a3.

Bảng sau biến đổi:

| T | A | B | C | D | E | Z |
|---|---|---|---|---|---|---|
| R1 | a1 | a2 | b1 ⇒ a3 | a4 | a5 | a6 |
| R2 | b2 | b3 | a3 | a4 | a5 | b4 |
| R3 | b5 | a2 | a3 | b6 | b7 | b8 |

Có một dòng chứa toàn ký hiệu a → **bảo toàn thông tin**.

Kiểm tra **bảo toàn PTH** (cách của bài giảng): F' = ∪Fᵢ = {MaPhieuBH → {MaSeri, MaDH, SoDongDH, MoTaLoi, PhuKienDiKem, NgayNhan, NgayHenTra, NgayTraThucTe, TinhTrangBH, KetQuaBH, LyDoTuChoi, MaNV} (12 PTH); MaDH,SoDongDH → {MaSP} (1 PTH); MaSeri → {MaSP} (1 PTH)}.

- (1) Mọi f' ∈ F' \ F đều thuộc F⁺ vì mỗi Fᵢ là PTH chiếu từ F⁺.
- (2) Mọi f ∈ F \ F' phải thuộc F'⁺. Kiểm tra từng PTH của F bằng bao đóng theo F':
  - MaPhieuBH → {MaSeri, MaDH, SoDongDH, MoTaLoi, PhuKienDiKem, NgayNhan, NgayHenTra, NgayTraThucTe, TinhTrangBH, KetQuaBH, LyDoTuChoi, MaNV}: (MaPhieuBH)⁺_F' = Q⁺ chứa các thuộc tính vế phải → thỏa.
  - MaDH,SoDongDH → {MaSP}: (MaDH,SoDongDH)⁺_F' = {MaSP, MaDH, SoDongDH} chứa các thuộc tính vế phải → thỏa.
  - MaSeri → {MaSP}: (MaSeri)⁺_F' = {MaSeri, MaSP} chứa các thuộc tính vế phải → thỏa.

**Kết luận: bảo toàn PTH** (thỏa (1) và (2)).

Dạng chuẩn các quan hệ con: R1: BCNF (khóa {MaPhieuBH}); R2: BCNF (khóa {MaDH, SoDongDH}); R3: BCNF (khóa {MaSeri}).

**Lựa chọn.** Tổng hợp bảo toàn cả thông tin và PTH. Trong cơ sở dữ liệu, R₂ là một phép chiếu của CHITIETDONHANG và R₃ nằm trong SERIMATHANG (mục 2.3.5), nên không tạo quan hệ mới: chỉ có R₁ thay PHIEUBAOHANH, tức **bỏ cột MaSP**. Tên hàng lấy bằng phép nối với CHITIETDONHANG theo (MaDH, SoDongDH); hai cột này không rỗng nên phiếu nào cũng lấy được mặt hàng, và PTH (MaDH, SoDongDH) → MaSP dùng được trên toàn quan hệ. Chỉ R₃ có điều kiện: khi ghép thông tin chiếc hàng phải dùng phép nối ngoài (`LEFT JOIN`) để giữ phiếu có MaSeri rỗng. **PHIEUBAOHANH nâng từ 2NF lên BCNF.**

![Hình 2.2: Phân rã PHIEUBAOHANH: bỏ cột MaSP suy ra được](hinh/phan_ra_phieubaohanh.png)

*Hình 2.2: Phân rã PHIEUBAOHANH: bỏ cột MaSP suy ra được*

### 2.3.5 HANGCOSERI: từ 3NF lên BCNF

Ánh xạ chữ cái: A = MaSeri, B = SoSeri, C = MaSP, D = MaPN, E = SoDongPN, F = MaDH, G = SoDongDH, H = TinhTrangSeri, I = ThoiDiemNhap.
F (phủ tối thiểu G): MaSeri → {SoSeri, MaPN, SoDongPN, MaDH, SoDongDH, TinhTrangSeri, ThoiDiemNhap} (7 PTH); SoSeri,MaSP → {MaSeri} (1 PTH); MaPN,SoDongPN → {MaSP} (1 PTH); MaDH,SoDongDH → {MaSP} (1 PTH). Các khóa: {MaSeri}; {SoSeri, MaSP}; {SoSeri, MaPN, SoDongPN} (có điều kiện: {SoSeri, MaDH, SoDongDH}). Đang ở 3NF vì MaSP là thuộc tính khóa (thuộc khóa {SoSeri, MaSP}); vi phạm BCNF: (MaPN, SoDongPN) → MaSP và (MaDH, SoDongDH) → MaSP có vế trái không chứa khóa.

**Cách 1: thuật toán phân rã.** B1: loại PTH của khóa chính (VT ∪ VP = Q⁺); còn F* = {MaSP,SoSeri → MaSeri; MaPN,SoDongPN → MaSP; MaDH,SoDongDH → MaSP} ≠ ∅. B2: chọn **MaPN,SoDongPN → MaSP** (vế trái không chứa khóa). Tách Q₁{MaPN, SoDongPN, MaSP} và Q₂ = Q⁺ \ {MaSP}; Q₂ có mọi vế trái PTH là khóa nên dừng.

**Phép tách HANGCOSERI bằng phân rã (Delobel)**

Các quan hệ con và PTH chiếu (Fᵢ):

- **Q1**(MaSP, MaPN, SoDongPN): F = {MaPN,SoDongPN → MaSP}
- **Q2**(MaSeri, SoSeri, MaPN, SoDongPN, MaDH, SoDongDH, TinhTrangSeri, ThoiDiemNhap): F = {MaSeri → {SoSeri, MaPN, SoDongPN, MaDH, SoDongDH, TinhTrangSeri, ThoiDiemNhap} (7 PTH); SoSeri,MaPN,SoDongPN → {MaSeri} (1 PTH); SoSeri,MaDH,SoDongDH → {MaSeri} (1 PTH)}

Ký hiệu cột gộp: Z = {TinhTrangSeri, ThoiDiemNhap} (các thuộc tính này chỉ phụ thuộc vào cùng một khóa và có cùng cách xuất hiện ở các quan hệ con).

Kiểm tra **bảo toàn thông tin** bằng bảng a/b của giáo trình. Bảng khởi tạo:

| T | A | B | C | D | E | F | G | Z |
|---|---|---|---|---|---|---|---|---|
| Q1 | b1 | b2 | a3 | a4 | a5 | b3 | b4 | b5 |
| Q2 | a1 | a2 | b6 | a4 | a5 | a6 | a7 | a8 |

Biến đổi theo PTH của F:

- Hai dòng Q1 và Q2 cùng giá trị ở D,E; theo PTH D,E → C, ô cột C: b6 thành a3.

Bảng sau biến đổi:

| T | A | B | C | D | E | F | G | Z |
|---|---|---|---|---|---|---|---|---|
| Q1 | b1 | b2 | a3 | a4 | a5 | b3 | b4 | b5 |
| Q2 | a1 | a2 | b6 ⇒ a3 | a4 | a5 | a6 | a7 | a8 |

Có một dòng chứa toàn ký hiệu a → **bảo toàn thông tin**.

Kiểm tra **bảo toàn PTH** (cách của bài giảng): F' = ∪Fᵢ = {MaPN,SoDongPN → {MaSP} (1 PTH); MaSeri → {SoSeri, MaPN, SoDongPN, MaDH, SoDongDH, TinhTrangSeri, ThoiDiemNhap} (7 PTH); SoSeri,MaPN,SoDongPN → {MaSeri} (1 PTH); SoSeri,MaDH,SoDongDH → {MaSeri} (1 PTH)}.

- (1) Mọi f' ∈ F' \ F đều thuộc F⁺ vì mỗi Fᵢ là PTH chiếu từ F⁺.
- (2) Mọi f ∈ F \ F' phải thuộc F'⁺. Kiểm tra từng PTH của F bằng bao đóng theo F':
  - MaSeri → {SoSeri, MaPN, SoDongPN, MaDH, SoDongDH, TinhTrangSeri, ThoiDiemNhap}: (MaSeri)⁺_F' = Q⁺ chứa các thuộc tính vế phải → thỏa.
  - SoSeri,MaSP → MaSeri: (SoSeri,MaSP)⁺_F' = {SoSeri, MaSP} ∌ MaSeri → **không thỏa**.
  - MaPN,SoDongPN → {MaSP}: (MaPN,SoDongPN)⁺_F' = {MaSP, MaPN, SoDongPN} chứa các thuộc tính vế phải → thỏa.
  - MaDH,SoDongDH → MaSP: (MaDH,SoDongDH)⁺_F' = {MaDH, SoDongDH} ∌ MaSP → **không thỏa**.

**Kết luận: không bảo toàn PTH** (thỏa (1) nhưng không thỏa (2)); PTH bị mất: {SoSeri, MaSP} → MaSeri; {MaDH, SoDongDH} → MaSP.

Dạng chuẩn các quan hệ con: Q1: BCNF (khóa {MaPN, SoDongPN}); Q2: BCNF (khóa {MaSeri}, {SoSeri, MaPN, SoDongPN}; khóa có điều kiện {SoSeri, MaDH, SoDongDH}).

Phép tách bảo toàn thông tin nhưng **mất PTH** (MaSP, SoSeri) → MaSeri, tức quy tắc “số seri duy nhất trong cùng mặt hàng” (G1), vì MaSP và SoSeri không còn nằm chung một quan hệ, và mất (MaDH, SoDongDH) → MaSP.

**Cách 2: thuật toán tổng hợp.** B1: phủ tối thiểu G. B2: nhóm theo vế trái: F₁ (MaSeri), F₂ (MaSP, SoSeri), F₃ (MaPN, SoDongPN), F₄ (MaDH, SoDongDH). B3: MaSeri → {MaSP, SoSeri} và {MaSP, SoSeri} → MaSeri nên F₁ và F₂ phụ thuộc lẫn nhau, gộp. B4: quan hệ gộp chứa mọi thuộc tính của Q, tức **chính Q**; hai quan hệ còn lại là tập con của Q nên bị loại. Kết quả của tổng hợp là Q nguyên vẹn, chỉ đạt 3NF.

**Phương án C: bốn thành phần (BCNF, bảo toàn đủ).** Tách Q₁{MaPN, SoDongPN, MaSP}; Q₂{MaDH, SoDongDH, MaSP}; Q₃ gồm MaSeri và các thuộc tính còn lại trừ MaSP, SoSeri; Q₄{MaSeri, SoSeri, MaSP} (hai khóa MaSeri và {MaSP, SoSeri}).

**Phép tách HANGCOSERI theo phương án C**

Các quan hệ con và PTH chiếu (Fᵢ):

- **Q1**(MaSP, MaPN, SoDongPN): F = {MaPN,SoDongPN → MaSP}
- **Q2**(MaSP, MaDH, SoDongDH): F = {MaDH,SoDongDH → MaSP}
- **Q3**(MaSeri, MaPN, SoDongPN, MaDH, SoDongDH, TinhTrangSeri, ThoiDiemNhap): F = {MaSeri → MaPN; MaSeri → SoDongPN; MaSeri → MaDH; MaSeri → SoDongDH; MaSeri → TinhTrangSeri; MaSeri → ThoiDiemNhap}
- **Q4**(MaSeri, SoSeri, MaSP): F = {MaSeri → SoSeri; MaSeri → MaSP; SoSeri,MaSP → MaSeri}

Ký hiệu cột gộp: Z = {TinhTrangSeri, ThoiDiemNhap} (các thuộc tính này chỉ phụ thuộc vào cùng một khóa và có cùng cách xuất hiện ở các quan hệ con).

Kiểm tra **bảo toàn thông tin** bằng bảng a/b của giáo trình. Bảng khởi tạo:

| T | A | B | C | D | E | F | G | Z |
|---|---|---|---|---|---|---|---|---|
| Q1 | b1 | b2 | a3 | a4 | a5 | b3 | b4 | b5 |
| Q2 | b6 | b7 | a3 | b8 | b9 | a6 | a7 | b10 |
| Q3 | a1 | b11 | b12 | a4 | a5 | a6 | a7 | a8 |
| Q4 | a1 | a2 | a3 | b13 | b14 | b15 | b16 | b17 |

Biến đổi theo PTH của F:

- Hai dòng Q3 và Q4 cùng giá trị ở A; theo PTH A → B, ô cột B: b11 thành a2.
- Hai dòng Q3 và Q4 cùng giá trị ở A; theo PTH A → D, ô cột D: b13 thành a4.
- Hai dòng Q3 và Q4 cùng giá trị ở A; theo PTH A → E, ô cột E: b14 thành a5.
- Hai dòng Q3 và Q4 cùng giá trị ở A; theo PTH A → F, ô cột F: b15 thành a6.
- Hai dòng Q3 và Q4 cùng giá trị ở A; theo PTH A → G, ô cột G: b16 thành a7.
- Hai dòng Q3 và Q4 cùng giá trị ở A; theo PTH A → Z, ô cột Z: b17 thành a8.
- Hai dòng Q1 và Q3 cùng giá trị ở D,E; theo PTH D,E → C, ô cột C: b12 thành a3.

Bảng sau biến đổi:

| T | A | B | C | D | E | F | G | Z |
|---|---|---|---|---|---|---|---|---|
| Q1 | b1 | b2 | a3 | a4 | a5 | b3 | b4 | b5 |
| Q2 | b6 | b7 | a3 | b8 | b9 | a6 | a7 | b10 |
| Q3 | a1 | b11 ⇒ a2 | b12 ⇒ a3 | a4 | a5 | a6 | a7 | a8 |
| Q4 | a1 | a2 | a3 | b13 ⇒ a4 | b14 ⇒ a5 | b15 ⇒ a6 | b16 ⇒ a7 | b17 ⇒ a8 |

Có một dòng chứa toàn ký hiệu a → **bảo toàn thông tin**.

Kiểm tra **bảo toàn PTH** (cách của bài giảng): F' = ∪Fᵢ = {MaPN,SoDongPN → {MaSP} (1 PTH); MaDH,SoDongDH → {MaSP} (1 PTH); MaSeri → {SoSeri, MaSP, MaPN, SoDongPN, MaDH, SoDongDH, TinhTrangSeri, ThoiDiemNhap} (8 PTH); SoSeri,MaSP → {MaSeri} (1 PTH)}.

- (1) Mọi f' ∈ F' \ F đều thuộc F⁺ vì mỗi Fᵢ là PTH chiếu từ F⁺.
- (2) Mọi f ∈ F \ F' phải thuộc F'⁺. Kiểm tra từng PTH của F bằng bao đóng theo F':
  - MaSeri → {SoSeri, MaPN, SoDongPN, MaDH, SoDongDH, TinhTrangSeri, ThoiDiemNhap}: (MaSeri)⁺_F' = Q⁺ chứa các thuộc tính vế phải → thỏa.
  - SoSeri,MaSP → {MaSeri}: (SoSeri,MaSP)⁺_F' = Q⁺ chứa các thuộc tính vế phải → thỏa.
  - MaPN,SoDongPN → {MaSP}: (MaPN,SoDongPN)⁺_F' = {MaSP, MaPN, SoDongPN} chứa các thuộc tính vế phải → thỏa.
  - MaDH,SoDongDH → {MaSP}: (MaDH,SoDongDH)⁺_F' = {MaSP, MaDH, SoDongDH} chứa các thuộc tính vế phải → thỏa.

**Kết luận: bảo toàn PTH** (thỏa (1) và (2)).

Dạng chuẩn các quan hệ con: Q1: BCNF (khóa {MaPN, SoDongPN}); Q2: BCNF (khóa {MaDH, SoDongDH}); Q3: BCNF (khóa {MaSeri}); Q4: BCNF (khóa {MaSeri}, {SoSeri, MaSP}).

Q₁ và Q₂ **trùng với phép chiếu của CHITIETPHIEUNHAP và CHITIETDONHANG** (đã có) nên không tạo quan hệ mới. Hai quan hệ cần: **HANGCOSERI** rút gọn (Q₃, bỏ SoSeri và MaSP) và **SERIMATHANG** mới (Q₄).

| Phương án | Dạng chuẩn | Bảo toàn thông tin | Bảo toàn PTH | Quan hệ mới | Ghi chú |
|---|---|---|---|---|---|
| Giữ nguyên | 3NF | không cần tách | có | không | MaSP lưu thừa ở mỗi chiếc |
| Phân rã (Delobel) | BCNF | có | **không** | không | Mất bảo đảm seri duy nhất theo mặt hàng |
| Tổng hợp | 3NF | có | có | không | Trả lại đúng Q |
| **C: bốn thành phần** | **BCNF** | **có** | **có** | **SERIMATHANG** | Cần ràng buộc nhất quán MaSP (mục 2.3.6) |

*Bảng 2.91: So sánh các phương án tách HANGCOSERI*

**Chọn phương án C**, vì giữ quy tắc “seri duy nhất theo mặt hàng” (G1), đạt BCNF và không mất PTH. **HANGCOSERI nâng từ 3NF lên BCNF.**

**Lưu ý về NULL.** Q₃ và Q₄ nối theo MaSeri, Q₁ theo (MaPN, SoDongPN); các cột này không rỗng nên đúng với mọi chiếc hàng. Riêng (MaDH, SoDongDH) → MaSP là PTH có điều kiện: chiếc chưa bán có hai cột này rỗng, nên khi nối HANGCOSERI với dòng đơn phải dùng `LEFT JOIN` (như K4 ở chương 3); nối trong sẽ làm mất chiếc chưa bán.

![Hình 2.3: Phân rã HANGCOSERI thành bốn thành phần (phương án C)](hinh/phan_ra_hangcoseri.png)

*Hình 2.3: Phân rã HANGCOSERI thành bốn thành phần (phương án C)*

### 2.3.6 Lược đồ sau cải tiến

Lược đồ sau cải tiến có **26 quan hệ** (25 quan hệ ban đầu, thêm SERIMATHANG). Các thay đổi: tách HoTen ở KHACHHANG, NHANVIEN; bỏ MaDH khỏi CHITIETTRA; bỏ MaSP khỏi PHIEUBAOHANH; HANGCOSERI bỏ SoSeri và MaSP, thêm SERIMATHANG.

1. LOAIHANG(<u>MaLoai</u>, TenLoai, MoTaLoai, <span style="text-decoration: underline dashed">MaLoaiCha</span>)
2. THUONGHIEU(<u>MaTH</u>, TenTH, MoTaTH)
3. MATHANG(<u>MaSP</u>, SKU, TenSP, MoTaSP, GiaNiemYet, GiaKhuyenMai, ThoiHanBH, TinhTrangKD, CoSeri, <span style="text-decoration: underline dashed">MaLoai</span>, <span style="text-decoration: underline dashed">MaTH</span>)
4. ANHMATHANG(<u>MaAnh</u>, <span style="text-decoration: underline dashed">MaSP</span>, ViTriAnh, DuongDanAnh, LaAnhChinh)
5. DINHNGHIATHONGSO(<u>MaTS</u>, <span style="text-decoration: underline dashed">MaLoai</span>, TenTS, KieuGiaTri, DonViTS, BatBuoc)
6. GIATRITHONGSO(<u>MaSP</u><sup>FK</sup>, <u>MaTS</u><sup>FK</sup>, GiaTriTS)
7. KHACHHANG(<u>MaKH</u>, HoLotKH, TenKH, SDTKH, EmailKH, MaSoThueKH) *(đã thay đổi)*
8. NHANVIEN(<u>MaNV</u>, HoLotNV, TenNV, SDTNV, EmailNV, NgayVaoLam, NgayNghiViec, TinhTrangNV, ChucVu) *(đã thay đổi)*
9. TAIKHOAN(<u>MaTK</u>, TenDangNhap, MatKhauBam, TinhTrangTK, ThoiDiemTaoTK, <span style="text-decoration: underline dashed">MaKH</span>, <span style="text-decoration: underline dashed">MaNV</span>)
10. NHACUNGCAP(<u>MaNCC</u>, TenNCC, NguoiLienHeNCC, SDTNCC, DiaChiNCC, MaSoThueNCC, TinhTrangHT)
11. MAGIAMGIA(<u>MaMG</u>, CodeMG, TenChuongTrinh, LoaiGiam, MucGiam, DonToiThieu, GiamToiDa, NgayBatDau, NgayKetThuc, GioiHanLuot, <span style="text-decoration: underline dashed">MaNV</span>)
12. DONHANG(<u>MaDH</u>, SoDH, ThoiDiemLap, KenhBan, <span style="text-decoration: underline dashed">MaKH</span>, <span style="text-decoration: underline dashed">MaNV</span>, TenNguoiNhan, SDTNhan, DiaChiGiao, PhiGiao, GiamGia, <span style="text-decoration: underline dashed">MaMG</span>, TinhTrangDH, DieuKienCoc, GhiChuDH)
13. CHITIETDONHANG(<u>MaDH</u><sup>FK</sup>, <u>SoDongDH</u>, <span style="text-decoration: underline dashed">MaSP</span>, SoLuongBan, DonGiaChot, TenHangChot, SKUChot, ThoiHanBHChot)
14. THANHTOAN(<u>MaTT</u>, <span style="text-decoration: underline dashed">MaDH</span>, LoaiKhoan, PhuongThuc, SoTien, ThoiDiemTT, KetQuaTT, MaGiaoDichNgoai, DonViThanhToan, <span style="text-decoration: underline dashed">MaNV</span>, <span style="text-decoration: underline dashed">MaNVThu</span>)
15. PHIEUGIAO(<u>MaGiao</u>, <span style="text-decoration: underline dashed">MaDH</span>, <span style="text-decoration: underline dashed">MaNV</span>, ThoiDiemXuat, TinhTrangGiao)
16. LANGIAO(<u>MaGiao</u><sup>FK</sup>, <u>SoLan</u>, ThoiDiemGiao, KetQuaGiao, LyDoThatBai, <span style="text-decoration: underline dashed">MaNV</span>)
17. PHIEUNHAP(<u>MaPN</u>, SoPhieu, <span style="text-decoration: underline dashed">MaNCC</span>, <span style="text-decoration: underline dashed">MaNV</span>, ThoiDiemNhan, TinhTrangPN, <span style="text-decoration: underline dashed">MaNVXacNhan</span>, ThoiDiemXacNhan, SoHoaDonNCC, GhiChuPN)
18. CHITIETPHIEUNHAP(<u>MaPN</u><sup>FK</sup>, <u>SoDongPN</u>, <span style="text-decoration: underline dashed">MaSP</span>, SoLuongNhap, GiaNhap)
19. HANGCOSERI(<u>MaSeri</u><sup>FK</sup>, <span style="text-decoration: underline dashed">MaPN</span>, <span style="text-decoration: underline dashed">SoDongPN</span>, <span style="text-decoration: underline dashed">MaDH</span>, <span style="text-decoration: underline dashed">SoDongDH</span>, TinhTrangSeri, ThoiDiemNhap) *(đã thay đổi)*
20. SERIMATHANG(<u>MaSeri</u>, SoSeri, <span style="text-decoration: underline dashed">MaSP</span>) *(mới)*
21. GIAODICHKHO(<u>MaGDK</u>, <span style="text-decoration: underline dashed">MaSP</span>, NhomKho, LoaiBienDong, SoLuongGD, ThoiDiemGD, <span style="text-decoration: underline dashed">MaNV</span>, LoaiChungTu, MaChungTu, GhiChuGD)
22. HOSODOITRA(<u>MaHS</u>, <span style="text-decoration: underline dashed">MaDH</span>, <span style="text-decoration: underline dashed">MaNV</span>, NgayDeNghi, LoaiTruongHop, LyDoDoiTra, TinhTrangHS, HinhThucXuLy)
23. CHITIETTRA(<u>MaHS</u><sup>FK</sup>, <u>SoDongTra</u>, SoDongDH, SoLuongTra, <span style="text-decoration: underline dashed">MaSeri</span>) *(đã thay đổi)*
24. LANNHANLAI(<u>MaNhanLai</u>, <span style="text-decoration: underline dashed">MaHS</span>, ThoiDiemNhanLai, <span style="text-decoration: underline dashed">MaNV</span>, KetLuan, NhomSauKiemTra, ThoiDiemDuyet, <span style="text-decoration: underline dashed">MaNVDuyet</span>)
25. KHOANHOAN(<u>MaHoan</u>, <span style="text-decoration: underline dashed">MaTT</span>, <span style="text-decoration: underline dashed">MaHS</span>, <span style="text-decoration: underline dashed">MaPhieuBH</span>, <span style="text-decoration: underline dashed">MaNV</span>, SoTienHoan, PhuongThucHoan, ThoiDiemDuyetHoan, ThoiDiemChi, <span style="text-decoration: underline dashed">MaNVChi</span>)
26. PHIEUBAOHANH(<u>MaPhieuBH</u>, <span style="text-decoration: underline dashed">MaSeri</span>, <span style="text-decoration: underline dashed">MaDH</span>, <span style="text-decoration: underline dashed">SoDongDH</span>, MoTaLoi, PhuKienDiKem, NgayNhan, NgayHenTra, NgayTraThucTe, TinhTrangBH, KetQuaBH, LyDoTuChoi, <span style="text-decoration: underline dashed">MaNV</span>) *(đã thay đổi)*

**Ràng buộc nhất quán** không biểu diễn được bằng PTH trong một quan hệ (cưỡng chế bằng khóa ngoại ghép hoặc kiểm tra khi ghi):

1. MaSP của SERIMATHANG phải bằng MaSP của dòng nhập (MaPN, SoDongPN) và của dòng đơn (MaDH, SoDongDH) nếu có.
2. Phiếu bảo hành có MaSeri thì mặt hàng của chiếc hàng (SERIMATHANG.MaSP) phải bằng MaSP của dòng mua gốc (MaDH, SoDongDH). Phiếu ghi đúng dòng mua của lần bán đó, còn HANGCOSERI chỉ ghi lần bán gần nhất, nên khi chiếc được trả về rồi bán lại, hai dòng đơn này có thể khác nhau; đơn gốc của phiếu vẫn đúng.
3. Dòng đơn trong CHITIETTRA là (MaDH của hồ sơ, SoDongDH) và phải có trong CHITIETDONHANG. Nếu muốn khai báo khóa ngoại ở mức cơ sở dữ liệu thì khi cài đặt giữ thêm cột MaDH với khóa ngoại ghép (MaHS, MaDH) tới HOSODOITRA; về lý thuyết đó là cột nhân bản có kiểm soát, không thuộc lược đồ logic.
4. Khoản hoàn tiền có MaHS thì đơn của khoản thu gốc (THANHTOAN.MaDH) phải bằng đơn của hồ sơ đổi trả (HOSODOITRA.MaDH); đồ thị ở chương 3 cho thấy KHOANHOAN có các mạch đi tới DONHANG qua THANHTOAN, qua HOSODOITRA và qua PHIEUBAOHANH nên các mạch phải cùng dẫn tới một đơn. Một khoản hoàn không cùng lúc có MaHS và MaPhieuBH.

Các ràng buộc **tài khoản, chức vụ và trách nhiệm** (không biểu diễn được bằng PTH; các quy tắc về chức vụ là **giả thiết** nghiệp vụ của nhóm):

5. TAIKHOAN: đúng một trong hai cột MaKH, MaNV có giá trị.
6. Người thực hiện một khâu phải có chức vụ phù hợp (NHANVIEN.ChucVu): duyệt hoàn tiền (KHOANHOAN.MaNV) và duyệt chuyển nhóm hàng nhận lại (LANNHANLAI.MaNVDuyet) là Quản lý; chi tiền hoàn (MaNVChi) là Thu ngân; xác nhận thu (THANHTOAN.MaNV) là Thu ngân, Bán hàng hoặc Quản lý; thu tiền khi giao (THANHTOAN.MaNVThu) là Giao hàng; xác nhận phiếu nhập (PHIEUNHAP.MaNVXacNhan) là Kho; tạo mã giảm giá (MAGIAMGIA.MaNV) là Bán hàng hoặc Quản lý.
7. Đơn có KenhBan khác "Trang web" phải có MaNV; khách chỉ tự hủy được đơn còn "Chờ xác nhận".

**Mã SQL đề xuất** (đã chạy trên SQLite và SQL Server LocalDB 17.0, CSDL dùng collation UTF-8 tiếng Việt; toàn bộ 26 bảng ở `sql/01_tao_bang.sql`):

```sql
CREATE TABLE SERIMATHANG (
    MaSeri INT NOT NULL PRIMARY KEY,
    SoSeri VARCHAR(60) NOT NULL,
    MaSP   INT NOT NULL REFERENCES MATHANG(MaSP),
    CONSTRAINT UQ_SERIMATHANG UNIQUE (MaSP, SoSeri)
);
-- Khung nhìn trả lại hình dạng cũ của HANGCOSERI khi cần
CREATE VIEW vw_HangCoSeri AS
SELECT h.*, s.SoSeri, s.MaSP FROM HANGCOSERI h JOIN SERIMATHANG s ON s.MaSeri = h.MaSeri;
```

### 2.3.7 So sánh trước và sau cải tiến

| Quan hệ | Dư thừa trước | Dị thường trước | Sau cải tiến | Chi phí |
|---|---|---|---|---|
| KHACHHANG, NHANVIEN | Họ tên ghi một cột | Lọc theo tên phải dùng LIKE trên một phần giá trị; sắp xếp theo tên khó | HoLot và Ten riêng | Nhập hai ô thay vì một |
| CHITIETTRA | MaDH lặp lại ở mỗi dòng trả của cùng hồ sơ | **Cập nhật:** sửa đơn gốc của hồ sơ nhưng sót một dòng thì hồ sơ có hai đơn. **Thêm:** dòng trả có MaDH khác đơn của hồ sơ | MaDH chỉ ở HOSODOITRA | Muốn biết đơn của dòng trả phải nối với HOSODOITRA |
| PHIEUBAOHANH | MaSP lặp ở mỗi phiếu của cùng dòng đơn hoặc cùng chiếc | **Cập nhật:** đổi mặt hàng của dòng đơn mà không sửa phiếu. **Thêm:** phiếu ghi MaSP không khớp dòng mua gốc | MaSP chỉ ở CHITIETDONHANG và SERIMATHANG | Một phép nối với CHITIETDONHANG |
| HANGCOSERI | MaSP lặp ở mỗi chiếc của cùng dòng nhập; SoSeri gắn MaSP | **Cập nhật:** sửa mặt hàng của dòng nhập mà sót chiếc. **Thêm:** nhập chiếc có MaSP khác MaSP của dòng nhập | MaSP của chiếc chỉ ở SERIMATHANG; khóa {MaSP, SoSeri} được cưỡng chế bằng UNIQUE | Thêm một quan hệ và một phép nối; phải kiểm soát ràng buộc nhất quán 1 |

**Nhận xét.** Với CHITIETTRA và PHIEUBAOHANH, cải tiến loại hẳn dữ liệu thừa. Với HANGCOSERI, cải tiến đưa lược đồ về BCNF nhưng lượng MaSP lưu không giảm (mỗi chiếc vẫn có một MaSP ở SERIMATHANG); lợi ích là mỗi quan hệ không còn PTH vi phạm và khóa {MaSP, SoSeri} được cưỡng chế, còn tính nhất quán liên quan hệ do ràng buộc ở 2.3.6 bảo đảm. Chưa đo hiệu năng: thêm một phép nối có thể làm truy vấn chậm hơn hoặc không, cần đo trên dữ liệu thật.

### 2.3.8 Phụ thuộc đa trị và dạng chuẩn 4

Theo giáo trình, X ↠ Y (với X ∩ Y = ∅, Z = Q⁺ \ XY) là phụ thuộc đa trị nếu mỗi giá trị x của X xác định một tập giá trị Y không phụ thuộc vào Z. Quan hệ đạt 4NF nếu đạt BCNF và mọi phụ thuộc đa trị không hiển nhiên (XY ≠ Q⁺) có X là siêu khóa. Cách kiểm tra: tách X ↠ Y thành Q[X,Y] và Q[X,Z]; phép tách theo phụ thuộc đa trị luôn bảo toàn thông tin.

**Tình huống: ảnh và thông số của mặt hàng.** Theo mô tả (mục 1.4), mỗi mặt hàng có nhiều ảnh minh họa và nhiều giá trị thông số, và việc thêm hoặc đổi ảnh không làm đổi thông số: hai tập này **độc lập** nhau.

*Bước 1. Nếu lưu chung* một quan hệ M(MaSP, DuongDanAnh, MaTS, GiaTriTS), mỗi dòng là một cặp (ảnh, thông số) của mặt hàng:

- PTH: (MaSP, MaTS) → GiaTriTS. Khóa của M là {MaSP, DuongDanAnh, MaTS}. PTH này có vế trái là một phần của khóa nên M **không đạt 2NF**.
- Tách theo PTH: **R₁(MaSP, MaTS, GiaTriTS)** (chính là GIATRITHONGSO) và **R₂(MaSP, DuongDanAnh, MaTS)**.

*Bước 2. R₂ đạt BCNF nhưng không đạt 4NF.* R₂ toàn khóa nên **đạt BCNF** (không có PTH không hiển nhiên). Nhưng vì tập ảnh và tập thông số độc lập nên với mỗi mặt hàng, R₂ phải chứa **mọi cặp** (ảnh, thông số):

- **MaSP ↠ DuongDanAnh** (và MaSP ↠ MaTS) là phụ thuộc đa trị không hiển nhiên (MaSP ∪ DuongDanAnh ≠ R₂⁺) mà MaSP không là siêu khóa → R₂ **vi phạm 4NF**.
- Tách R₂ thành **R₂₁(MaSP, DuongDanAnh)** (ANHMATHANG, với MaAnh làm khóa thay thế) và **R₂₂(MaSP, MaTS)** (đã có trong R₁). Phép tách bảo toàn thông tin: R₂₁ ∩ R₂₂ = {MaSP} và MaSP ↠ DuongDanAnh.

**Kết quả: ANHMATHANG và GIATRITHONGSO đạt 4NF; lược đồ không chứa R₂.**

![Hình 2.4: Từ quan hệ lưu chung ảnh và thông số đến dạng chuẩn 4](hinh/phan_ra_4nf.png)

*Hình 2.4: Từ quan hệ lưu chung ảnh và thông số đến dạng chuẩn 4*

**Số liệu minh họa** (tính từ `database/data.seed.sql` của PowerTech: 120 mặt hàng có cả ảnh và thông số; trung bình 2,58 ảnh và 10,23 thông số mỗi mặt hàng):

| Cách lưu | Số dòng |
|---|---|
| M (lưu chung, mỗi dòng một cặp ảnh – thông số) | **3.256** (tổng ảnh × thông số theo từng mặt hàng) |
| ANHMATHANG và GIATRITHONGSO (tách) | **1.538** = 310 ảnh + 1.228 thông số |

*Bảng 2.92: Số dòng khi lưu chung và khi tách ảnh, thông số*

Lưu chung nhiều dòng hơn khoảng 2,1 lần chỉ để lặp lại cùng thông tin. Dị thường thêm: thêm một ảnh thứ tư cho một mặt hàng đang có 3 thông số buộc thêm 3 dòng ở dạng chung nhưng chỉ 1 dòng ở dạng tách.

**Toàn bộ lược đồ.** Tách đúng một tình huống không nói gì về các quan hệ khác, nên phần này chứng minh riêng cho cả 26 quan hệ, chỉ dùng khóa của toàn quan hệ (không dùng khóa có điều kiện).

*Mệnh đề.* Cho Q đạt BCNF, X ↠ Y không hiển nhiên (Y ≠ ∅, Z = Q⁺ \ XY ≠ ∅) và X không là siêu khóa. Khi đó mọi khóa của Q đều có thuộc tính nằm trong Y và có thuộc tính nằm trong Z.

*Chứng minh.* Giả sử khóa K không có thuộc tính trong Z, tức XY ⊃ K. Lấy hai bộ t₁, t₂ cùng giá trị trên X. Theo X ↠ Y có bộ t₃ cùng X, lấy Y của t₁ và Z của t₂. Bộ t₃ trùng t₁ trên XY nên trùng trên K, do đó t₃ = t₁, suy ra t₁[Z] = t₂[Z]. Vậy X → Z. Đây là PTH không hiển nhiên nên theo BCNF, X là siêu khóa: mâu thuẫn. Trường hợp K không có thuộc tính trong Y làm tương tự, vì X ↠ Y kéo theo X ↠ Z. ∎

Phép chứng minh chỉ dùng định nghĩa nên không phụ thuộc dữ liệu. Nhóm thử thêm mệnh đề bằng chương trình trên các quan hệ ngẫu nhiên, không gặp phản ví dụ. Kết quả cùng hướng với điều kiện khóa đơn của Date và Fagin (1992).

*Trường hợp 1: 21 quan hệ có khóa một thuộc tính* (LOAIHANG, THUONGHIEU, MATHANG, ANHMATHANG, DINHNGHIATHONGSO, KHACHHANG, NHANVIEN, TAIKHOAN, NHACUNGCAP, MAGIAMGIA, DONHANG, THANHTOAN, PHIEUGIAO, PHIEUNHAP, HANGCOSERI, SERIMATHANG, GIAODICHKHO, HOSODOITRA, LANNHANLAI, KHOANHOAN, PHIEUBAOHANH). Một thuộc tính không thể nằm ở cả Y và Z, nên theo mệnh đề không tồn tại phụ thuộc đa trị không hiển nhiên có X không là siêu khóa. Vậy các quan hệ này đạt 4NF.

Điều kiện của trường hợp này: mã phải định danh một đối tượng thật. Nếu gắn mã số dòng vào quan hệ M ở trên thì mệnh đề vẫn đúng về hình thức nhưng dư thừa vẫn còn, vì mã mới chỉ che phụ thuộc đa trị. Trong lược đồ, mỗi bộ của các quan hệ này là một đối tượng hoặc một chứng từ, không phải một cặp ghép chéo: ảnh và thông số đã tách, dòng chi tiết, lần giao, lần nhận lại đều ở quan hệ riêng, các thuộc tính còn lại đơn trị theo mã.

*Trường hợp 2: 5 quan hệ có khóa hai thuộc tính {A, B}.* Theo mệnh đề, nếu có phụ thuộc đa trị vi phạm thì A nằm trong Y, B nằm trong Z, nên X chỉ gồm thuộc tính không khóa (có thể rỗng). Khi đó mọi cặp bộ trùng nhau trên tất cả cột không khóa đều bắt buộc kéo theo bộ ghép chéo (a₁, b₂, v). Phụ thuộc đa trị phải đúng trên mọi thể hiện hợp lệ, nên một thể hiện hợp lệ thiếu bộ ghép chéo là đủ bác bỏ:

| Quan hệ | Thể hiện hợp lệ: t₁ = (a₁, b₁, v), t₂ = (a₂, b₂, v) | Bộ bắt buộc nhưng không có |
|---|---|---|
| GIATRITHONGSO | Mặt hàng 1 có thông số 1, mặt hàng 2 có thông số 2, cùng giá trị “Có” | (mặt hàng 1, thông số 2): mặt hàng 1 không có thông số này |
| CHITIETDONHANG | Đơn 1 chỉ có dòng 1; đơn 2 có hai dòng, dòng 2 cùng hàng, số lượng, giá, thời hạn với dòng 1 của đơn 1 | (đơn 1, dòng 2): đơn 1 không có dòng 2 |
| LANGIAO | Phiếu 1 giao lần 1 thành công; phiếu 2 giao hai lần, lần 2 cùng thời điểm, người giao, kết quả với lần giao của phiếu 1 | (phiếu 1, lần 2): phiếu 1 chỉ giao một lần |
| CHITIETPHIEUNHAP | Phiếu 1 chỉ có dòng 1; phiếu 2 có hai dòng, dòng 2 cùng hàng, số lượng, giá với dòng 1 của phiếu 1 | (phiếu 1, dòng 2): phiếu 1 không có dòng 2 |
| CHITIETTRA | Hồ sơ 1 chỉ có dòng 1 trả chiếc S; chiếc S được bán lại và trả tiếp ở dòng 2 của hồ sơ 2, cùng số dòng đơn, số lượng | (hồ sơ 1, dòng 2): hồ sơ 1 không có dòng 2 |

*Bảng 2.3: Thể hiện hợp lệ bác bỏ phụ thuộc đa trị ở năm quan hệ khóa hai thuộc tính*

**Kết luận: cả 26 quan hệ đạt 4NF.** Kết luận đúng trong phạm vi tập PTH và giả thiết nghiệp vụ đã nêu; nếu cửa hàng có thêm quy tắc làm đổi khóa hoặc lưu thêm thuộc tính đa trị thì phải kiểm lại.

### 2.3.9 Đánh giá lược đồ sau cải tiến

| STT | Quan hệ | Khóa của toàn quan hệ | Trước | Sau |
|---|---|---|---|---|
| 1 | LOAIHANG | {MaLoai} | BCNF | BCNF |
| 2 | THUONGHIEU | {MaTH}; {TenTH} | BCNF | BCNF |
| 3 | MATHANG | {MaSP}; {SKU} | BCNF | BCNF |
| 4 | ANHMATHANG | {MaAnh}; {MaSP, ViTriAnh} | BCNF | BCNF |
| 5 | DINHNGHIATHONGSO | {MaTS} | BCNF | BCNF |
| 6 | GIATRITHONGSO | {MaSP, MaTS} | BCNF | BCNF |
| 7 | KHACHHANG | {MaKH} | chưa đạt 1NF | BCNF |
| 8 | NHANVIEN | {MaNV} | chưa đạt 1NF | BCNF |
| 9 | TAIKHOAN | {MaTK}; {TenDangNhap} (có điều kiện: {MaKH}; {MaNV}) | BCNF | BCNF |
| 10 | NHACUNGCAP | {MaNCC}; {TenNCC} | BCNF | BCNF |
| 11 | MAGIAMGIA | {MaMG}; {CodeMG} | BCNF | BCNF |
| 12 | DONHANG | {MaDH}; {SoDH} | BCNF | BCNF |
| 13 | CHITIETDONHANG | {MaDH, SoDongDH} | BCNF | BCNF |
| 14 | THANHTOAN | {MaTT} | BCNF | BCNF |
| 15 | PHIEUGIAO | {MaGiao}; {MaDH} | BCNF | BCNF |
| 16 | LANGIAO | {MaGiao, SoLan} | BCNF | BCNF |
| 17 | PHIEUNHAP | {MaPN}; {SoPhieu} | BCNF | BCNF |
| 18 | CHITIETPHIEUNHAP | {MaPN, SoDongPN} | BCNF | BCNF |
| 19 | HANGCOSERI | {MaSeri} | 3NF | BCNF |
| 20 | SERIMATHANG | {MaSeri}; {SoSeri, MaSP} | — | BCNF |
| 21 | GIAODICHKHO | {MaGDK} | BCNF | BCNF |
| 22 | HOSODOITRA | {MaHS} | BCNF | BCNF |
| 23 | CHITIETTRA | {MaHS, SoDongTra} (có điều kiện: {MaHS, MaSeri}) | 1NF | BCNF |
| 24 | LANNHANLAI | {MaNhanLai} | BCNF | BCNF |
| 25 | KHOANHOAN | {MaHoan} | BCNF | BCNF |
| 26 | PHIEUBAOHANH | {MaPhieuBH} | 2NF | BCNF |

*Bảng 2.4: Dạng chuẩn trước và sau cải tiến*

**Dạng chuẩn của lược đồ sau cải tiến: BCNF** (cả 26 quan hệ, kiểm ở cả hai phạm vi của G4) **và 4NF** theo chứng minh ở 2.3.8. So với mục 2.2: từ **chưa đạt 1NF** lên **4NF**, trong phạm vi tập PTH đã nêu. Điều kiện đi kèm: (a) các ràng buộc nhất quán và ràng buộc trách nhiệm ở 2.3.6; (b) chọn phương án C với quy tắc “seri duy nhất theo mặt hàng” (G1) thay cho “seri duy nhất toàn cửa hàng”; (c) họ tên tách theo quy ước G3; (d) mỗi bộ của quan hệ có khóa một thuộc tính là một đối tượng thật (2.3.8).

**Đánh giá theo ba tiêu chuẩn của giáo trình.** *Nhất quán:* mỗi sự kiện chỉ ghi ở một quan hệ; các ràng buộc liên quan hệ ở 2.3.6 còn phải kiểm khi ghi. *Không trùng lắp:* đã bỏ MaDH, MaSP lưu thừa; giá, tên, SKU và thời hạn chốt trên dòng đơn là dữ liệu lịch sử có chủ ý, không phải trùng lắp. *Dễ khai thác:* đồ thị ở chương 3 cho thấy mọi yêu cầu tra cứu đều có đường nối, đổi lại một số câu phải nối thêm quan hệ (2.3.7); chưa đo hiệu năng.

## 2.4 PHÂN TÍCH CHỨC NĂNG VÀ QUY TRÌNH NGHIỆP VỤ

Mục này đặt cạnh lược đồ để đối chiếu: Use Case cho biết ai làm chức năng nào trên các quan hệ ở mục 2.1, còn lưu đồ vẽ lại bốn quy trình có quy tắc dễ nhầm nhất, làm căn cứ cho các ràng buộc ở 2.3.6 và cho các truy vấn ở chương 3. Nội dung nghiệp vụ lấy từ mục 1.4.

### 2.4.1 Sơ đồ Use Case

Theo báo cáo mẫu, các chức năng được nhóm theo ba loại thực thể (đối tượng ngoài, danh mục cơ bản, nghiệp vụ) cùng hai nhóm chung là tìm kiếm và thống kê. Sáu chức vụ (quản lý, bán hàng, thu ngân, kỹ thuật, kho, giao hàng; giả thiết G6) được vẽ thành sáu tác nhân riêng, mỗi tác nhân chỉ nối với các chức năng thuộc quyền của mình theo phân công ở mục 1.4 và ràng buộc 6 ở mục 2.3.6; tác nhân Khách hàng dùng trang web để đăng ký tài khoản, đặt hàng, hủy đơn khi còn chờ xác nhận và tra cứu đơn của mình. Các chức năng nằm trong phạm vi ở mục 1.3; những phần đã loại khỏi phạm vi (giỏ hàng, sổ địa chỉ, nhật ký đơn, lịch sử giữ vai trò) không có ca sử dụng.

![Hình 2.20: Sơ đồ Use Case tổng quát](hinh/usecase_tong_quat.png)

*Hình 2.20: Sơ đồ Use Case tổng quát*

![Hình 2.21: Sơ đồ Use Case quản lý đối tượng ngoài](hinh/usecase_doi_tuong_ngoai.png)

*Hình 2.21: Sơ đồ Use Case quản lý đối tượng ngoài*

![Hình 2.22: Sơ đồ Use Case quản lý danh mục cơ bản](hinh/usecase_danh_muc.png)

*Hình 2.22: Sơ đồ Use Case quản lý danh mục cơ bản*

![Hình 2.23: Sơ đồ Use Case quản lý nghiệp vụ](hinh/usecase_nghiep_vu.png)

*Hình 2.23: Sơ đồ Use Case quản lý nghiệp vụ*

![Hình 2.24: Sơ đồ Use Case tìm kiếm](hinh/usecase_tim_kiem.png)

*Hình 2.24: Sơ đồ Use Case tìm kiếm*

![Hình 2.25: Sơ đồ Use Case thống kê](hinh/usecase_thong_ke.png)

*Hình 2.25: Sơ đồ Use Case thống kê*

### 2.4.2 Lưu đồ các quy trình nghiệp vụ

Bốn lưu đồ dưới đây tóm tắt vòng đời tình trạng đơn hàng, đổi trả và hoàn tiền, tiếp nhận bảo hành và ba nhóm hàng trong kho. Các quan hệ liên quan:

- Tình trạng đơn hàng: DONHANG, THANHTOAN, PHIEUGIAO, LANGIAO (tối đa 3 lần giao).
- Đổi trả và hoàn tiền: HOSODOITRA, CHITIETTRA, LANNHANLAI, KHOANHOAN, GIAODICHKHO.
- Bảo hành: PHIEUBAOHANH, CHITIETDONHANG, HANGCOSERI, SERIMATHANG.
- Ba nhóm hàng trong kho: GIAODICHKHO, HANGCOSERI, LANNHANLAI.

![Hình 2.26: Lưu đồ tình trạng đơn hàng](hinh/luudo_don_hang.png)

*Hình 2.26: Lưu đồ tình trạng đơn hàng*

![Hình 2.27: Lưu đồ đổi trả hàng, hoàn tiền](hinh/luudo_doi_tra.png)

*Hình 2.27: Lưu đồ đổi trả hàng, hoàn tiền*

![Hình 2.28: Lưu đồ tiếp nhận và xử lý bảo hành](hinh/luudo_bao_hanh.png)

*Hình 2.28: Lưu đồ tiếp nhận và xử lý bảo hành*

![Hình 2.29: Lưu đồ ba nhóm hàng trong kho](hinh/luudo_kho.png)

*Hình 2.29: Lưu đồ ba nhóm hàng trong kho*

