# MỤC 2. XÁC ĐỊNH BA LOẠI THỰC THỂ VÀ THUỘC TÍNH

Căn cứ: [01_Mo_ta_de_tai_v3.md](01_Mo_ta_de_tai_v3.md) (mục 1 chính thức). Các số hiệu "1.2.x" dưới đây là mục tương ứng trong bản mô tả đó.

## 2.1. Cách phân loại và quy ước trình bày

**Ba loại thực thể theo bài giảng:**

| Loại | Định nghĩa | Dấu hiệu nhận biết |
|---|---|---|
| **Cơ bản** | Tài nguyên của hệ thống, có trước khi tin học hóa, ổn định | Không có thuộc tính thời gian (trừ ngày đưa vào dùng) |
| **Đối tượng ngoài** | Con người hoặc tổ chức tương tác với cửa hàng | Có họ tên hoặc tên tổ chức, thông tin liên hệ |
| **Nghiệp vụ** | Hồ sơ, chứng từ, sự kiện phát sinh khi vận hành | Luôn có thuộc tính thời gian; số lượng tăng dần |

**Các quy tắc đã rút ra từ nhận xét của giảng viên và áp dụng ở mục này:**

1. Dòng chi tiết (dòng đơn, dòng phiếu nhập, dòng giỏ...) là **mối kết hợp**, không liệt kê như thực thể (xem 2.4).
2. Giá trị chỉ để phân loại (kênh bán, phương thức thanh toán, tình trạng, nhóm tình trạng kho) là **thuộc tính** có miền giá trị, không thành thực thể.
3. Tồn kho, tổng tiền, hạn bảo hành còn lại, số dư là **dữ liệu tính toán**, không phải thực thể (xem 2.5).
4. Nhật ký trạng thái ("lịch sử...") không xếp thành thực thể; mỗi sự kiện quan trọng đã có thực thể riêng có thời điểm (xem 2.5).

**Quy ước:**

- Tên thực thể viết hoa không dấu (ví dụ `MATHANG`); tên thuộc tính dạng `MaSP`, `ThoiDiem`. Bảng đối chiếu với tên bảng trong `database/data.sql` ở mục 2.6.
- **Kiểu dữ liệu** ghi theo kiểu SQL Server, ở mức khái niệm. Kiểu và độ dài của thuộc tính đã có trong DDL lấy theo DDL; thuộc tính do v3 đề xuất mà DDL chưa có đánh dấu **†**.
- **↗** là liên kết tới thực thể khác, dự kiến thành khóa ngoại ở mục 7. Khóa chính, khóa ứng viên sẽ xác định ở mục 5; cột "Ràng buộc" ở đây chỉ ghi quy tắc đã nêu trong v3.
- **NULL** ghi "có" nếu được để trống.
- **★** là thực thể thuộc ba nhóm đề xuất phân tích sâu: (1) sản phẩm–thông số–ảnh, (2) đơn hàng–thanh toán, (3) phiếu nhập–sổ kho.

## 2.2. Tổng hợp ba loại thực thể

Có **30 thực thể**: 6 cơ bản, 4 đối tượng ngoài, 20 nghiệp vụ; cùng **8 mối kết hợp**.

### 2.2.1. Thực thể CƠ BẢN

| STT | Thực thể | Thuộc tính chính | Lý do xếp vào Cơ bản |
|---|---|---|---|
| 1 | LOAIHANG ★ | MaLoai, TenLoai, MoTa, MaLoaiCha | Danh mục phân loại, có từ trước, ít thay đổi; có thể phân cấp |
| 2 | THUONGHIEU ★ | MaTH, TenTH, MoTa | Danh mục thương hiệu, ổn định |
| 3 | MATHANG ★ | MaSP, SKU, TenSP, GiaNiemYet, GiaKhuyenMai, ThoiHanBaoHanh, CoSeri | Hàng hóa kinh doanh có trước và độc lập với từng giao dịch; chỉ có giá hiện tại, không có thời điểm |
| 4 | ANHMATHANG ★ | MaAnh, MaSP, ViTri, DuongDan, LaAnhChinh | Thành phần của mặt hàng, không phát sinh theo giao dịch |
| 5 | DINHNGHIATHONGSO ★ | MaTS, MaLoai, TenTS, KieuGiaTri, DonVi | Quy định thông số kỹ thuật theo loại hàng, có trước khi nhập hàng |
| 6 | VAITRO | MaVT, TenVT | Danh mục công việc trong cửa hàng; một nhân viên kiêm nhiều việc nên cần thực thể riêng |

### 2.2.2. Thực thể ĐỐI TƯỢNG NGOÀI

| STT | Thực thể | Thuộc tính chính | Loại | Lý do |
|---|---|---|---|---|
| 1 | KHACHHANG | MaKH, HoTen, SDT, Email, MaSoThue | Con người, tổ chức | Người mua, người đề nghị bảo hành hoặc đổi trả; khách doanh nghiệp có mã số thuế |
| 2 | DIACHINHANHANG | MaDC, MaKH, TenNguoiNhan, SDT, TinhThanh, PhuongXa, DiaChiCuThe, LaMacDinh | Thành phần của khách | Một khách có nhiều địa chỉ, tối đa một mặc định |
| 3 | NHANVIEN | MaNV, HoTen, SDT, TinhTrangLamViec | Con người | Người bán, thu ngân, kỹ thuật, kho, giao hàng, chăm sóc khách hàng, quản lý |
| 4 | NHACUNGCAP | MaNCC, TenNCC, NguoiLienHe, SDT, DiaChi, MaSoThue, TinhTrangHopTac | Tổ chức | Nhà phân phối, đại lý chính hãng; cũng là nơi nhận hàng lỗi và hàng gửi bảo hành |

### 2.2.3. Thực thể NGHIỆP VỤ

| STT | Thực thể | Thuộc tính chính | Thuộc tính thời gian | Lý do |
|---|---|---|---|---|
| 1 | TAIKHOAN | MaTK, DinhDanhDangNhap, MaKH, TinhTrang | NgayDangKy, ThoiDiemNoiHoSo | Lập khi khách đăng ký trên trang web |
| 2 | PHIEUNHAP ★ | MaPN, SoPhieu, MaNCC, MaNV, TinhTrang | ThoiDiemNhan | Phát sinh mỗi lần nhận hàng thực tế |
| 3 | HANGCOSERI | MaSeri, SoSeri, MaSP, TinhTrang | ThoiDiemNhap | Mỗi chiếc hàng có seri phát sinh khi nhập |
| 4 | GIAODICHKHO ★ | MaGDK, MaSP, NhomKho, LoaiBienDong, SoLuong | ThoiDiem | Mỗi lần hàng vào, ra hoặc đổi nhóm trong kho |
| 5 | DOTKIEMKE | MaDot, LoaiKiemKe, MaNVLap, MaNVDuyet, TinhTrang | ThoiDiem, ThoiDiemDuyet | Phát sinh mỗi đợt kiểm kê |
| 6 | GIOHANG | MaGio, MaTK, TinhTrang | ThoiDiemTao | Khách chọn hàng qua trang web |
| 7 | DONHANG ★ | MaDH, SoDH, KenhBan, LoaiDon, MaKH, MaNVBan, TinhTrang | ThoiDiemLap | Gồm phiếu bán tại quầy và đơn từ xa |
| 8 | DIEUCHINHDON | MaDieuChinh, MaDH, NoiDungTruoc, NoiDungSau, KhachDongY | ThoiDiem | Mỗi lần sửa đơn trước khi giao |
| 9 | MAGIAMGIA | MaMG, Code, LoaiGiam, MucGiam, GioiHanLuot | NgayBatDau, NgayKetThuc | Chương trình ưu đãi có thời hạn |
| 10 | GIUHANG ★ | MaGiu, MaDH, SoDong, SoLuong | ThoiDiemGiu, ThoiDiemKetThuc | Giữ hàng cho dòng đơn đã xác nhận |
| 11 | THANHTOAN ★ | MaTT, MaDH, LoaiKhoan, PhuongThuc, SoTien, KetQua | ThoiDiem | Mỗi lần trả tiền, kể cả cọc |
| 12 | KHOANHOAN | MaHoan, MaTT, SoTien, PhuongThucHoan, MaNVDuyet | ThoiDiemDuyet, ThoiDiemChi | Mỗi lần hoàn tiền |
| 13 | PHIEUGIAO | MaGiao, MaDH, MaNVGiao, TinhTrang | ThoiDiemXuat | Lập khi xuất hàng giao đi |
| 14 | LANGIAO | MaGiao, SoLan, KetQua, LyDoThatBai | ThoiDiem | Mỗi lần thử giao, tối đa 3 lần |
| 15 | BANGIAOCOD | MaBG, MaGiao, MaTT, MaNVGiao, MaNVNhan, SoTien | ThoiDiem | Người giao nộp tiền thu hộ về thủ quỹ |
| 16 | HOSODOITRA | MaHS, MaDH, LoaiTruongHop, TinhTrang | NgayDeNghi | Mỗi đề nghị đổi hoặc trả |
| 17 | LANNHANLAI | MaNhanLai, MaHS, KetLuan, NhomSauKiemTra | ThoiDiemNhan, ThoiDiemDuyet | Hàng nhận về và kết quả kiểm tra |
| 18 | PHIEUBAOHANH | MaPhieuBH, MaSP, MaSeri, MaDH, SoDong, TinhTrang, KetQua | NgayNhan, NgayHenTra, NgayTraThucTe | Mỗi lần tiếp nhận bảo hành |
| 19 | PHIEUGUIHANG | MaGui, MaNCC, LyDo, KetQua | NgayGui, NgayNhanKetQua | Mỗi lần gửi nhà cung cấp hoặc hãng |
| 20 | BIENDONGSODU (tùy chọn) | MaBD, MaTK, SoTien, LoaiBienDong | ThoiDiem | Chỉ có nếu giữ cách hoàn tiền vào số dư tài khoản |

## 2.3. Thuộc tính chi tiết từng thực thể

### 2.3.1. Thực thể cơ bản

**LOAIHANG** ★ (bảng `Categories`): phân loại hàng, có thể phân cấp cha – con.

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Ràng buộc, miền giá trị |
|---|---|---|---|---|
| MaLoai | Mã loại hàng | INT | không | Định danh |
| TenLoai | Tên loại | NVARCHAR(150) | không | Không giả định duy nhất (1.2.1) |
| MoTa | Mô tả | NVARCHAR(500) | có | |
| MaLoaiCha ↗ LOAIHANG | Loại cha | INT | có | Tối đa một loại cha, không tạo vòng |

**THUONGHIEU** ★ (bảng `Brands`)

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Ràng buộc, miền giá trị |
|---|---|---|---|---|
| MaTH | Mã thương hiệu | INT | không | Định danh |
| TenTH | Tên thương hiệu | NVARCHAR(150) | không | Không giả định duy nhất |
| MoTa | Mô tả | NVARCHAR(500) | có | |

**MATHANG** ★ (bảng `Products`)

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Ràng buộc, miền giá trị |
|---|---|---|---|---|
| MaSP | Mã nội bộ | INT | không | Định danh |
| SKU | Mã hàng thương mại | NVARCHAR(100) | không | Không trùng giữa các mặt hàng |
| TenSP | Tên hàng | NVARCHAR(250) | không | |
| MoTa | Mô tả | NVARCHAR(MAX) | có | |
| GiaNiemYet | Giá niêm yết hiện tại | DECIMAL(18,2) | không | ≥ 0 |
| GiaKhuyenMai | Giá khuyến mãi đang áp dụng | DECIMAL(18,2) | có | ≤ GiaNiemYet |
| ThoiHanBaoHanh | Thời hạn bảo hành, tính theo tháng | INT | không | ≥ 0 (0: không bảo hành phần cứng, ví dụ phần mềm) |
| TinhTrangKinhDoanh | Đang kinh doanh hay đã ngừng | BIT | không | |
| CoSeri † | Có ghi số seri từng chiếc không | BIT | không | |
| MaLoai ↗ LOAIHANG | Loại hàng | INT | không | Mỗi mặt hàng đúng một loại |
| MaTH ↗ THUONGHIEU | Thương hiệu | INT | không | Mỗi mặt hàng đúng một thương hiệu |

**ANHMATHANG** ★ (bảng `ProductImages`): thuộc tính đa trị của mặt hàng, tách thành thực thể vì mỗi ảnh có vị trí và đánh dấu ảnh chính.

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Ràng buộc, miền giá trị |
|---|---|---|---|---|
| MaAnh | Mã ảnh | INT | không | Định danh |
| MaSP ↗ MATHANG | Mặt hàng có ảnh | INT | không | |
| ViTri | Thứ tự sắp xếp ảnh | INT | không | Không trùng trong cùng mặt hàng |
| DuongDan | Đường dẫn ảnh | NVARCHAR(1000) | không | |
| LaAnhChinh | Ảnh đại diện chính | BIT | không | Mặt hàng đang bán có một ảnh chính |
| MoTaAnh | Chú thích ảnh | NVARCHAR(250) | có | |

**DINHNGHIATHONGSO** ★ (bảng `SpecificationDefinitions`)

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Ràng buộc, miền giá trị |
|---|---|---|---|---|
| MaTS | Mã thông số | INT | không | Định danh |
| MaLoai ↗ LOAIHANG | Loại hàng áp dụng | INT | không | |
| TenTS | Tên thông số | NVARCHAR(150) | không | Phân biệt trong cùng loại hàng |
| KieuGiaTri | Kiểu giá trị | NVARCHAR(20) | không | Chữ, số hoặc có/không |
| DonVi | Đơn vị | NVARCHAR(50) | có | |
| BatBuoc | Mặt hàng bán ra phải có thông số này | BIT | không | |

**VAITRO** (bảng `AspNetRoles`)

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Ràng buộc, miền giá trị |
|---|---|---|---|---|
| MaVT | Mã vai trò | INT | không | Định danh |
| TenVT | Tên công việc | NVARCHAR(100) | không | Tư vấn bán hàng, thu ngân kiêm thủ quỹ, kỹ thuật, kho, giao hàng, chăm sóc khách hàng, quản lý |

### 2.3.2. Thực thể đối tượng ngoài

**KHACHHANG** (từ `AspNetUsers`; khách mua tại quầy có hồ sơ riêng, không bắt buộc có tài khoản)

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Ràng buộc, miền giá trị |
|---|---|---|---|---|
| MaKH | Mã khách hàng | INT | không | Định danh |
| HoTen | Họ tên | NVARCHAR(150) | không | Không đủ để phân biệt hai khách |
| SDT | Số điện thoại | NVARCHAR(20) | không | Không đủ để phân biệt; khách không để lại số thì không có hồ sơ |
| Email | Thư điện tử | NVARCHAR(256) | có | |
| MaSoThue † | Mã số thuế của khách doanh nghiệp | NVARCHAR(50) | có | Chỉ có khi khách cần hóa đơn giá trị gia tăng |

**DIACHINHANHANG** (bảng `UserAddresses`): thành phần của khách. Địa chỉ gồm tỉnh hoặc thành phố, phường hoặc xã, địa chỉ cụ thể; không có cấp quận hoặc huyện theo nhận xét của giảng viên (D6/g10).

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Ràng buộc, miền giá trị |
|---|---|---|---|---|
| MaDC | Mã địa chỉ | INT | không | Định danh |
| MaKH ↗ KHACHHANG | Khách sở hữu | INT | không | |
| TenNguoiNhan | Người nhận | NVARCHAR(150) | không | |
| SDT | Số điện thoại người nhận | NVARCHAR(20) | không | |
| TinhThanh | Tỉnh hoặc thành phố | NVARCHAR(100) | không | |
| PhuongXa | Phường hoặc xã | NVARCHAR(100) | không | |
| DiaChiCuThe | Số nhà, đường | NVARCHAR(255) | không | |
| LaMacDinh | Địa chỉ mặc định | BIT | không | Tối đa một địa chỉ mặc định cho mỗi khách |

**NHANVIEN**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Ràng buộc, miền giá trị |
|---|---|---|---|---|
| MaNV | Mã nhân viên | INT | không | Định danh |
| HoTen | Họ tên | NVARCHAR(150) | không | |
| SDT | Số điện thoại | NVARCHAR(20) | không | |
| TinhTrangLamViec | Còn làm hay đã nghỉ | BIT | không | |

**NHACUNGCAP** (bảng `Suppliers`)

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Ràng buộc, miền giá trị |
|---|---|---|---|---|
| MaNCC | Mã nhà cung cấp | INT | không | Định danh |
| TenNCC | Tên công ty | NVARCHAR(150) | không | Không giả định duy nhất |
| NguoiLienHe | Người liên hệ | NVARCHAR(150) | có | |
| SDT | Số điện thoại | NVARCHAR(20) | có | |
| DiaChi | Địa chỉ | NVARCHAR(500) | có | |
| MaSoThue | Mã số thuế | NVARCHAR(50) | có | Chưa coi là khóa khi chưa có quy tắc bắt buộc và duy nhất |
| TinhTrangHopTac | Còn hợp tác không | BIT | không | |

### 2.3.3. Thực thể nghiệp vụ

**TAIKHOAN** (từ `AspNetUsers`): tài khoản khách trên trang web.

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Ràng buộc, miền giá trị |
|---|---|---|---|---|
| MaTK | Mã tài khoản | INT | không | Định danh |
| DinhDanhDangNhap | Số điện thoại hoặc email dùng đăng ký | NVARCHAR(256) | không | Không trùng |
| MaKH ↗ KHACHHANG | Khách gắn với tài khoản | INT | có | Mỗi tài khoản gắn tối đa một khách |
| TinhTrang | Hoạt động hoặc bị khóa | NVARCHAR(20) | không | |
| NgayDangKy | Thời điểm đăng ký | DATETIME2 | không | |
| ThoiDiemNoiHoSo † | Thời điểm hồ sơ quầy được nối vào tài khoản | DATETIME2 | có | Chỉ sau khi khách xác nhận bằng mã gửi về số điện thoại |

**PHIEUNHAP** ★ (bảng `PurchaseReceipts`)

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Ràng buộc, miền giá trị |
|---|---|---|---|---|
| MaPN | Mã phiếu | INT | không | Định danh |
| SoPhieu | Số phiếu | NVARCHAR(50) | không | Không trùng |
| MaNCC ↗ NHACUNGCAP | Nhà cung cấp | INT | không | |
| MaNV ↗ NHANVIEN | Người lập | INT | không | |
| ThoiDiemNhan | Thời điểm nhận hàng | DATETIME2 | không | |
| TinhTrang | Chờ xác nhận hoặc đã xác nhận | NVARCHAR(30) | không | Phải có ít nhất một dòng khi xác nhận; chỉ ghi tăng kho một lần |
| SoHoaDonNCC † | Số hóa đơn của nhà cung cấp | NVARCHAR(50) | có | |
| GhiChu | Ghi chú | NVARCHAR(1000) | có | |

**HANGCOSERI** † (chưa có trong DDL): mỗi chiếc hàng có số seri riêng.

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Ràng buộc, miền giá trị |
|---|---|---|---|---|
| MaSeri | Mã nội bộ của chiếc hàng | INT | không | Định danh |
| SoSeri | Số seri của hãng | NVARCHAR(100) | không | Giả thiết: không trùng trong cùng mặt hàng (chưa kiểm chứng) |
| MaSP ↗ MATHANG | Mặt hàng | INT | không | Mặt hàng có CoSeri = đúng |
| MaPN ↗ CHITIETPHIEUNHAP | Phiếu nhập mà chiếc này đến từ | INT | không | |
| SoDongNhap ↗ CHITIETPHIEUNHAP | Dòng của phiếu nhập | INT | không | |
| MaDH, SoDongDon ↗ CHITIETDONHANG | Dòng đơn đã bán chiếc này | INT | có | Rỗng nếu chưa bán |
| TinhTrang | Trong kho, đã bán, đang bảo hành, đã gửi hãng, đã trả nhà cung cấp | NVARCHAR(30) | không | |
| ThoiDiemNhap | Thời điểm nhập | DATETIME2 | không | |

**GIAODICHKHO** ★ (bảng `StockTransactions`): mỗi lần hàng vào, ra hoặc đổi nhóm. Tồn theo nhóm là dữ liệu tính từ thực thể này.

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Ràng buộc, miền giá trị |
|---|---|---|---|---|
| MaGDK | Mã giao dịch | INT | không | Định danh |
| MaSP ↗ MATHANG | Mặt hàng | INT | không | |
| NhomKho † | Nhóm tình trạng của hàng | NVARCHAR(30) | không | Đủ điều kiện bán, chờ kiểm tra, không bán được chờ xử lý |
| LoaiBienDong | Loại | NVARCHAR(20) | không | Kiểm kê đầu kỳ, nhập, bán, giao, trả, chuyển nhóm, điều chỉnh |
| SoLuong | Số lượng thay đổi | INT | không | > 0; chiều tăng hoặc giảm do loại biến động quyết định (DDL cũng lưu số dương); chuyển nhóm tạo hai dòng đối ứng |
| ThoiDiem | Thời điểm | DATETIME2 | không | |
| MaNV ↗ NHANVIEN | Người thực hiện | INT | có | |
| LoaiChungTu, MaChungTu | Chứng từ gốc (phiếu nhập, đơn, hồ sơ đổi trả...) | NVARCHAR(50), INT | có | Liên kết đa hình, không có khóa ngoại trong DDL hiện tại |
| GhiChu | Ghi chú | NVARCHAR(500) | có | |

**DOTKIEMKE** †

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Ràng buộc, miền giá trị |
|---|---|---|---|---|
| MaDot | Mã đợt | INT | không | Định danh |
| LoaiKiemKe | Đầu kỳ, định kỳ hoặc đột xuất | NVARCHAR(20) | không | |
| ThoiDiem | Thời điểm kiểm kê | DATETIME2 | không | |
| MaNVLap ↗ NHANVIEN | Người lập biên bản | INT | không | |
| MaNVDuyet ↗ NHANVIEN | Người quản lý duyệt | INT | có | Số lượng chỉ được điều chỉnh sau khi duyệt |
| ThoiDiemDuyet | Thời điểm duyệt | DATETIME2 | có | |
| TinhTrang | Chờ duyệt, đã duyệt, từ chối | NVARCHAR(20) | không | |

**GIOHANG** (bảng `Carts`)

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Ràng buộc, miền giá trị |
|---|---|---|---|---|
| MaGio | Mã giỏ | INT | không | Định danh |
| MaTK ↗ TAIKHOAN | Tài khoản | INT | không | Mỗi tài khoản tối đa một giỏ đang dùng |
| TinhTrang † | Đang dùng hoặc đã gửi đơn | NVARCHAR(20) | không | |
| ThoiDiemTao | Thời điểm tạo | DATETIME2 | không | |

**DONHANG** ★ (bảng `Orders`): gồm phiếu bán tại quầy và đơn từ xa, kể cả đơn đặt trước có cọc.

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Ràng buộc, miền giá trị |
|---|---|---|---|---|
| MaDH | Mã đơn | INT | không | Định danh |
| SoDH | Số đơn | NVARCHAR(50) | không | Không trùng |
| ThoiDiemLap | Thời điểm lập | DATETIME2 | không | |
| KenhBan † | Kênh bán | NVARCHAR(20) | không | Quầy, trang web, điện thoại hoặc tin nhắn |
| LoaiDon † | Loại đơn | NVARCHAR(20) | không | Có sẵn, đặt trước, lắp theo yêu cầu |
| MaKH ↗ KHACHHANG | Khách | INT | có | Rỗng nếu khách quầy không để lại thông tin |
| MaNVBan ↗ NHANVIEN | Nhân viên bán hoặc lập đơn | INT | không | |
| TenNguoiNhan | Người nhận | NVARCHAR(150) | không | Chốt khi xác nhận đơn |
| SDTNhan | Số điện thoại nhận | NVARCHAR(20) | không | Chốt khi xác nhận đơn |
| DiaChiGiao | Địa chỉ giao | NVARCHAR(500) | có | Rỗng nếu giao trực tiếp tại quầy; chốt khi xác nhận đơn |
| PhiGiao | Phí giao hàng | DECIMAL(18,2) | không | ≥ 0 |
| GiamGia | Số tiền giảm đã chốt | DECIMAL(18,2) | không | ≥ 0; chỉ giảm tiền hàng |
| MaMG ↗ MAGIAMGIA | Mã giảm giá đã dùng | INT | có | Tối đa một mã mỗi đơn |
| TinhTrang | Tình trạng đơn | NVARCHAR(30) | không | Chờ xác nhận, đã xác nhận, đang chuẩn bị, đang giao, hoàn tất, đã hủy |
| DieuKienCoc † | Điều kiện đặt cọc ghi trên phiếu đặt hàng | NVARCHAR(500) | có | Chỉ có với đơn đặt trước hoặc lắp theo yêu cầu |
| GhiChu | Ghi chú | NVARCHAR(1000) | có | |

**DIEUCHINHDON** †

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Ràng buộc, miền giá trị |
|---|---|---|---|---|
| MaDieuChinh | Mã lần sửa | INT | không | Định danh |
| MaDH ↗ DONHANG | Đơn bị sửa | INT | không | Chỉ sửa trước khi giao |
| ThoiDiem | Thời điểm | DATETIME2 | không | |
| MaNV ↗ NHANVIEN | Người ghi nhận | INT | không | |
| NoiDungTruoc | Nội dung trước khi sửa | NVARCHAR(MAX) | không | |
| NoiDungSau | Nội dung sau khi sửa | NVARCHAR(MAX) | không | |
| KhachDongY | Khách đã đồng ý | BIT | không | Phải đúng |

**MAGIAMGIA** (bảng `Coupons`)

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Ràng buộc, miền giá trị |
|---|---|---|---|---|
| MaMG | Mã nội bộ | INT | không | Định danh |
| Code | Mã khách nhập | NVARCHAR(50) | không | Không trùng |
| TenChuongTrinh † | Tên chương trình | NVARCHAR(150) | không | |
| LoaiGiam | Theo phần trăm hoặc theo số tiền | INT | không | |
| MucGiam | Mức giảm | DECIMAL(18,2) | không | > 0 |
| DonToiThieu | Giá trị đơn tối thiểu | DECIMAL(18,2) | có | |
| GiamToiDa | Mức giảm tối đa | DECIMAL(18,2) | có | |
| NgayBatDau | Bắt đầu áp dụng | DATETIME2 | có | |
| NgayKetThuc | Hết hạn | DATETIME2 | có | ≥ NgayBatDau |
| GioiHanLuot | Số lượt dùng tối đa | INT | có | Số lượt đã dùng là dữ liệu tính từ các đơn |

**GIUHANG** † ★

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Ràng buộc, miền giá trị |
|---|---|---|---|---|
| MaGiu | Mã lần giữ | INT | không | Định danh |
| MaDH, SoDong ↗ CHITIETDONHANG | Dòng đơn được giữ hàng | INT | không | |
| SoLuong | Số lượng giữ | INT | không | > 0 |
| ThoiDiemGiu | Thời điểm giữ | DATETIME2 | không | Sau khi nhân viên xác nhận đơn |
| ThoiDiemKetThuc | Thời điểm kết thúc giữ | DATETIME2 | có | |
| LyDoKetThuc | Lý do | NVARCHAR(30) | có | Xuất hàng, hủy đơn, giao thất bại, hết hạn trả trước |

**THANHTOAN** ★ (bảng `Payments`)

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Ràng buộc, miền giá trị |
|---|---|---|---|---|
| MaTT | Mã lần thanh toán | INT | không | Định danh |
| MaDH ↗ DONHANG | Đơn | INT | không | Một đơn có nhiều lần thanh toán |
| LoaiKhoan † | Cọc, thanh toán, thu khi giao | NVARCHAR(20) | không | |
| PhuongThuc | Phương thức | NVARCHAR(30) | không | Tiền mặt, chuyển khoản hoặc QR, thẻ, ví điện tử hoặc cổng thanh toán, COD (COD không áp dụng tại quầy) |
| SoTien | Số tiền | DECIMAL(18,2) | không | > 0 |
| ThoiDiem | Thời điểm | DATETIME2 | không | |
| KetQua † | Thành công, thất bại, chờ xác nhận | NVARCHAR(20) | không | Lần thất bại không được tính là đã thu |
| MaGiaoDichNgoai | Mã giao dịch bên ngoài | NVARCHAR(100) | có | Phân biệt trong phạm vi đơn vị thanh toán |
| DonViThanhToan | Ngân hàng, ví hoặc cổng thanh toán | NVARCHAR(100) | có | |
| MaNVXacNhan ↗ NHANVIEN | Người xác nhận | INT | có | |

**KHOANHOAN** †

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Ràng buộc, miền giá trị |
|---|---|---|---|---|
| MaHoan | Mã khoản hoàn | INT | không | Định danh |
| MaTT ↗ THANHTOAN | Khoản thu gốc | INT | không | Tổng các khoản hoàn không vượt số tiền đã thu |
| MaHS ↗ HOSODOITRA | Hồ sơ đổi trả hoặc hủy phát sinh khoản hoàn | INT | có | |
| SoTien | Số tiền hoàn | DECIMAL(18,2) | không | > 0 |
| PhuongThucHoan | Theo phương thức đã trả, chuyển khoản, tiền mặt, số dư tài khoản | NVARCHAR(30) | không | |
| MaNVDuyet ↗ NHANVIEN | Người quản lý duyệt | INT | không | |
| ThoiDiemDuyet | Thời điểm duyệt | DATETIME2 | không | |
| ThoiDiemChi | Thời điểm chi | DATETIME2 | có | |

**PHIEUGIAO** †

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Ràng buộc, miền giá trị |
|---|---|---|---|---|
| MaGiao | Mã phiếu giao | INT | không | Định danh |
| MaDH ↗ DONHANG | Đơn giao | INT | không | Mỗi đơn giao trọn trong một đợt |
| MaNVGiao ↗ NHANVIEN | Người giao | INT | không | |
| ThoiDiemXuat | Thời điểm xuất hàng | DATETIME2 | không | Việc giữ hàng kết thúc, số lượng trừ khỏi kho |
| TinhTrang | Đang giao, hoàn tất, thất bại | NVARCHAR(20) | không | |

**LANGIAO** † (thực thể yếu của PHIEUGIAO)

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Ràng buộc, miền giá trị |
|---|---|---|---|---|
| MaGiao ↗ PHIEUGIAO | Phiếu giao | INT | không | |
| SoLan | Lần giao thứ mấy | INT | không | 1 đến 3 |
| ThoiDiem | Thời điểm | DATETIME2 | không | |
| KetQua | Thành công hoặc thất bại | NVARCHAR(20) | không | |
| LyDoThatBai | Lý do | NVARCHAR(250) | có | Có khi thất bại |

**BANGIAOCOD** †

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Ràng buộc, miền giá trị |
|---|---|---|---|---|
| MaBG | Mã bàn giao | INT | không | Định danh |
| MaGiao ↗ PHIEUGIAO | Phiếu giao | INT | không | |
| MaTT ↗ THANHTOAN | Khoản thu COD | INT | không | |
| MaNVGiao ↗ NHANVIEN | Người nộp | INT | không | |
| MaNVNhan ↗ NHANVIEN | Thủ quỹ nhận | INT | không | |
| SoTien | Số tiền nộp | DECIMAL(18,2) | không | > 0 |
| ThoiDiem | Thời điểm nộp | DATETIME2 | không | |

**HOSODOITRA** †

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Ràng buộc, miền giá trị |
|---|---|---|---|---|
| MaHS | Mã hồ sơ | INT | không | Định danh |
| MaDH ↗ DONHANG | Đơn gốc | INT | không | Một đơn có thể được trả nhiều lần |
| MaKH ↗ KHACHHANG | Người đề nghị | INT | có | Rỗng nếu khách quầy không có hồ sơ; khi đó xử lý bằng chứng từ mua |
| NgayDeNghi | Ngày đề nghị | DATETIME2 | không | |
| LoaiTruongHop | Giao sai thiếu hư ngoài, lỗi nhà sản xuất, khách đổi ý | NVARCHAR(30) | không | Quyết định thời hạn (48 giờ, 30 hoặc 7 ngày, 7 ngày) |
| LyDo | Lý do | NVARCHAR(500) | không | |
| TinhTrang | Chờ kiểm tra, chấp nhận, từ chối, hoàn tất | NVARCHAR(20) | không | |
| HinhThucXuLy | Đổi cùng loại, đổi sản phẩm khác, hoàn tiền | NVARCHAR(20) | có | |
| MaNVTiepNhan ↗ NHANVIEN | Người tiếp nhận | INT | không | |

**LANNHANLAI** †

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Ràng buộc, miền giá trị |
|---|---|---|---|---|
| MaNhanLai | Mã lần nhận | INT | không | Định danh |
| MaHS ↗ HOSODOITRA | Hồ sơ | INT | không | Tổng số lượng nhận lại không vượt số đã giao |
| ThoiDiemNhan | Thời điểm nhận hàng | DATETIME2 | không | Hàng luôn vào nhóm chờ kiểm tra |
| MaNVKiemTra ↗ NHANVIEN | Kỹ thuật viên | INT | có | |
| KetLuan | Nguyên niêm phong không lỗi, đã mở hộp không lỗi, lỗi thật | NVARCHAR(30) | có | |
| NhomSauKiemTra | Nhóm kho sau kiểm tra | NVARCHAR(30) | có | Chuyển nhóm tạo giao dịch kho đối ứng |
| MaNVDuyet ↗ NHANVIEN | Người quản lý duyệt | INT | có | |
| ThoiDiemDuyet | Thời điểm duyệt | DATETIME2 | có | |

**PHIEUBAOHANH** †

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Ràng buộc, miền giá trị |
|---|---|---|---|---|
| MaPhieuBH | Mã phiếu | INT | không | Định danh |
| MaKH ↗ KHACHHANG | Khách | INT | có | Rỗng nếu đối chiếu bằng chứng từ mua |
| MaSP ↗ MATHANG | Mặt hàng bảo hành | INT | không | |
| MaSeri ↗ HANGCOSERI | Chiếc hàng có seri | INT | có | Rỗng với hàng không có seri |
| MaDH, SoDong ↗ CHITIETDONHANG | Dòng mua gốc | INT | không | Căn cứ thời hạn bảo hành đã chốt |
| MoTaLoi | Mô tả lỗi | NVARCHAR(500) | không | |
| PhuKienDiKem | Phụ kiện đi kèm | NVARCHAR(250) | có | |
| NgayNhan | Ngày tiếp nhận | DATETIME2 | không | |
| NgayHenTra | Ngày hẹn trả ghi trên phiếu | DATE | không | Thường 7 đến 30 ngày tùy hãng |
| NgayTraThucTe | Ngày trả khách | DATETIME2 | có | |
| TinhTrang | Đã tiếp nhận, đang xử lý, đã gửi hãng, đã xong, từ chối | NVARCHAR(20) | không | |
| KetQua | Sửa xong, đổi mới, hoàn tiền, không thấy lỗi, từ chối | NVARCHAR(20) | có | |
| LyDoTuChoi | Lý do từ chối | NVARCHAR(250) | có | Có khi từ chối |
| MaNVTiepNhan ↗ NHANVIEN | Người tiếp nhận | INT | không | |

**PHIEUGUIHANG** †

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Ràng buộc, miền giá trị |
|---|---|---|---|---|
| MaGui | Mã phiếu gửi | INT | không | Định danh |
| MaNCC ↗ NHACUNGCAP | Nhà cung cấp hoặc hãng nhận | INT | không | |
| LyDo | Bảo hành hoặc trả hàng lỗi | NVARCHAR(20) | không | |
| NgayGui | Ngày gửi | DATETIME2 | không | |
| NgayNhanKetQua | Ngày nhận kết quả | DATETIME2 | có | |
| KetQua | Đổi hàng mới, đã sửa, ghi giảm tiền | NVARCHAR(20) | có | Hàng đổi về nhập theo phiếu nhập |
| MaNVGui ↗ NHANVIEN | Người gửi | INT | không | |

**BIENDONGSODU** † (tùy chọn)

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Ràng buộc, miền giá trị |
|---|---|---|---|---|
| MaBD | Mã biến động | INT | không | Định danh |
| MaTK ↗ TAIKHOAN | Tài khoản | INT | không | |
| SoTien | Số tiền tăng (dương) hoặc giảm (âm) | DECIMAL(18,2) | không | Số dư tính ra không âm |
| LoaiBienDong | Hoàn tiền hoặc dùng để thanh toán | NVARCHAR(20) | không | |
| MaHoan ↗ KHOANHOAN | Nguồn tăng | INT | có | Một nguồn không tạo biến động hai lần |
| ThoiDiem | Thời điểm | DATETIME2 | không | |

## 2.4. Mối kết hợp (không phải thực thể)

Tám mối kết hợp dưới đây mang thuộc tính riêng nên được tách thành quan hệ ở mục 7, nhưng trong ERD vẽ là mối kết hợp giữa các thực thể.

| Mối kết hợp | Giữa | Thuộc tính | Bản số sơ bộ |
|---|---|---|---|
| CHITIETDONHANG ★ (bảng `OrderItems`) | DONHANG – MATHANG | SoDong, SoLuong, DonGiaChot, TenHangChot, SKUChot | n–n; cùng mặt hàng có thể ở nhiều dòng của một đơn |
| CHITIETPHIEUNHAP ★ (bảng `PurchaseReceiptItems`) | PHIEUNHAP – MATHANG | SoDong, SoLuong, GiaNhap | n–n; cùng mặt hàng có thể ở nhiều dòng của một phiếu |
| CHITIETGIOHANG (bảng `CartItems`) | GIOHANG – MATHANG | SoLuong | n–n; mỗi mặt hàng một dòng trong giỏ |
| GIATRITHONGSO ★ (bảng `ProductSpecifications`) | MATHANG – DINHNGHIATHONGSO | GiaTri (chữ, số hoặc có/không) | n–n; mỗi cặp tối đa một giá trị |
| NHANVIEN_VAITRO (bảng `AspNetUserRoles`) | NHANVIEN – VAITRO | không | n–n |
| CHITIETKIEMKE † | DOTKIEMKE – MATHANG | SoLuongSo, SoLuongDem, LyDoChenhLech | n–n; chênh lệch là dữ liệu tính |
| CHITIETTRA † | HOSODOITRA – CHITIETDONHANG | SoLuongTra, MaSeri | n–n; tổng số lượng trả không vượt số đã giao |
| CHITIETGUIHANG † | PHIEUGUIHANG – MATHANG | SoDong, SoLuong, MaSeri, nguồn (phiếu bảo hành hoặc hồ sơ đổi trả) | n–n |

Các mối kết hợp không có thuộc tính thời gian riêng; thời điểm lấy từ thực thể cha.

## 2.5. Những thứ không xếp thành thực thể

| Đối tượng | Vì sao | Cách biểu diễn |
|---|---|---|
| Tồn kho theo nhóm, số lượng có thể nhận bán | Thống kê tính từ GIAODICHKHO và GIUHANG | Dữ liệu tính toán |
| Thành tiền từng dòng, tổng phải trả, tổng tiền phiếu nhập | Tính từ các dòng, giảm giá, phí giao | Dữ liệu tính toán; nếu lưu sẵn (như `LineTotal`, `TotalAmount` trong DDL) thì phải ghi là cột suy diễn |
| Số lượt đã dùng của mã giảm giá | Đếm từ các đơn | Dữ liệu tính toán (DDL hiện có `UsedCount`) |
| Hạn bảo hành còn lại | Ngày mua, thời hạn, thời gian ở bảo hành, lần đổi mới | Dữ liệu tính toán |
| Số dư tài khoản mua hàng | Tổng các biến động | Dữ liệu tính toán |
| Kênh bán, loại đơn, phương thức thanh toán, tình trạng, nhóm tình trạng kho | Giá trị chỉ để phân loại, ít giá trị, không có thuộc tính riêng | Thuộc tính có miền giá trị |
| Lịch sử tình trạng đơn (`OrderHistory` trong DDL) | Nhận xét của giảng viên: "LichSu... là thống kê" | Không xếp thực thể; các sự kiện quan trọng đã có thực thể riêng có thời điểm (thanh toán, giao, đổi trả...). Cần hỏi giảng viên nếu muốn giữ |
| Chính sách đổi trả, biểu phí giao | Quy tắc cửa hàng công bố, thay đổi ít | Ràng buộc nghiệp vụ ở các mục sau; chưa là thực thể |
| Hóa đơn bán lẻ | Chứng từ xuất theo quy định, nội dung lấy từ đơn | Chưa mô hình hóa |
| Đánh giá, hỗ trợ, thu mua thiết bị cũ, hạng thành viên, thông báo | Ngoài phạm vi (v3, mục 1.3) | Không có |

## 2.6. Đối chiếu với `database/data.sql`

| Thực thể hoặc mối kết hợp | Bảng trong DDL | Ghi chú |
|---|---|---|
| LOAIHANG, THUONGHIEU, MATHANG, ANHMATHANG, DINHNGHIATHONGSO, GIATRITHONGSO | `Categories`, `Brands`, `Products`, `ProductImages`, `SpecificationDefinitions`, `ProductSpecifications` | Khớp. DDL còn nhiều cột phục vụ trang web (`Slug`, `ImageUrl`, `IsFeatured`...) không đưa vào mô hình |
| VAITRO, NHANVIEN_VAITRO | `AspNetRoles`, `AspNetUserRoles` | DDL gắn vai trò với tài khoản; v3 gắn với nhân viên |
| KHACHHANG, NHANVIEN, TAIKHOAN | `AspNetUsers` (một bảng chung) | DDL gộp khách, nhân viên và tài khoản. v3 tách vì khách quầy không có tài khoản |
| DIACHINHANHANG | `UserAddresses` | DDL có `District` (quận hoặc huyện); v3 bỏ theo nhận xét của giảng viên |
| NHACUNGCAP | `Suppliers` | DDL có `Email`; v3 không dùng |
| PHIEUNHAP, CHITIETPHIEUNHAP | `PurchaseReceipts`, `PurchaseReceiptItems` | Khớp |
| GIAODICHKHO | `StockTransactions` | v3 thêm `NhomKho`; chứng từ nguồn trong DDL là `ReferenceType`, `ReferenceId` không có khóa ngoại |
| GIOHANG, CHITIETGIOHANG | `Carts`, `CartItems` | DDL cho giỏ không cần tài khoản (`CookieId`) |
| DONHANG, CHITIETDONHANG | `Orders`, `OrderItems` | DDL có cột tổng tiền lưu sẵn; v3 xếp vào dữ liệu tính |
| MAGIAMGIA | `Coupons` | Khớp |
| THANHTOAN | `Payments` | Bảng này rỗng trong dữ liệu mẫu |
| **Chưa có trong DDL** | | HANGCOSERI, DOTKIEMKE, CHITIETKIEMKE, DIEUCHINHDON, GIUHANG, KHOANHOAN, PHIEUGIAO, LANGIAO, BANGIAOCOD, HOSODOITRA, CHITIETTRA, LANNHANLAI, PHIEUBAOHANH, PHIEUGUIHANG, CHITIETGUIHANG, BIENDONGSODU |
| **Có trong DDL, không có trong v3** | | `Reviews`, `ReviewImages`, `SupportTickets`, `TicketResponses`, `TradeInRequests`, `TradeInRequestImages`, `FaqArticles`, `FaqCategories`, `CannedResponses`, `Notifications`, `OrderHistory`, các bảng Identity phụ, `__EFMigrationsHistory` |

Mô hình ở mục này là **thiết kế đề xuất theo v3**, không phải mô tả cơ sở dữ liệu hiện có.

## 2.7. Điểm tranh luận và câu hỏi giảng viên có thể hỏi

1. **Vì sao MATHANG là cơ bản dù có giá?** Mặt hàng có trước giao dịch và không mang thời điểm; giá hiện tại chỉ là thuộc tính. Giá đã bán nằm ở CHITIETDONHANG (giá chốt), nên không lẫn với giá hiện tại.
2. **Vì sao TAIKHOAN là nghiệp vụ còn KHACHHANG là đối tượng ngoài?** Khách là con người, tồn tại kể cả khi chưa có tài khoản. Tài khoản chỉ phát sinh khi khách đăng ký (có `NgayDangKy`).
3. **Vì sao nhóm tình trạng kho không phải thực thể?** Chỉ có ba giá trị cố định, không có thuộc tính riêng; theo nhận xét "Giới tính, Điểm đánh giá là thuộc tính, ko là Table" nên là thuộc tính của GIAODICHKHO. Tồn theo nhóm tính từ giao dịch kho.
4. **Vì sao các dòng `CHITIET...` không nằm trong danh sách thực thể?** Giảng viên nhắc nhiều nhóm rằng `ChiTiet...` là mối kết hợp, không phải thực thể. Ba nhóm ở 2.2 không chứa dòng chi tiết nào; tám mối kết hợp được liệt kê riêng ở 2.4.
5. **GIUHANG và LANGIAO có phải mối kết hợp không?** Hai thực thể này có thời điểm riêng và có thể có nhiều lần cho cùng đối tượng cha nên giữ là thực thể nghiệp vụ; nếu giảng viên coi là chi tiết, có thể gộp vào DONHANG và PHIEUGIAO.
6. **Tại sao có tới 30 thực thể?** v3 mô tả toàn bộ hoạt động; mục 3 trở đi chỉ phân tích sâu ba nhóm ★, các nhóm còn lại nêu ở mức mô tả.

**Thực thể có thể gộp hoặc bỏ nếu cần gọn:** BIENDONGSODU (nếu hoàn tiền chỉ trả trực tiếp); DIEUCHINHDON (nếu ghi lịch sử sửa đơn ở ghi chú); BANGIAOCOD (nếu gộp vào THANHTOAN loại thu khi giao); LANNHANLAI (nếu gộp vào HOSODOITRA).

**Giả thiết cần xác nhận:** (a) `SoSeri` không trùng trong cùng mặt hàng; (b) quản lý lịch sử tình trạng đơn bằng thực thể sự kiện hay không; (c) khách không để lại thông tin thì không có hồ sơ KHACHHANG; (d) các chính sách thời hạn (48 giờ, 30 ngày, 7 ngày) là chính sách giả định của cửa hàng.
