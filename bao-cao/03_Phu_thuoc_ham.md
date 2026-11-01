# MỤC 3. XÁC ĐỊNH TẬP PHỤ THUỘC HÀM CỦA TỪNG LOẠI THỰC THỂ

Căn cứ: [01_Mo_ta_de_tai_v3.md](01_Mo_ta_de_tai_v3.md) (mục 1) và [02_Xac_dinh_thuc_the.md](02_Xac_dinh_thuc_the.md) (mục 2). Phân tích sâu ba nhóm: (1) sản phẩm–thông số–ảnh, (2) đơn hàng–thanh toán, (3) phiếu nhập–sổ kho. Các thực thể còn lại nêu tập F ngắn gọn ở mục 3.5.

## 3.1. Phương pháp và quy ước

**Cách xác định.** Với mỗi quan hệ Q: viết tân từ ‖Q‖ (câu mô tả ngữ nghĩa một bộ), rút các phụ thuộc hàm (PTH) từ tân từ và quy tắc nghiệp vụ, rồi ghi căn cứ cho từng PTH. Không rút PTH từ dữ liệu mẫu: dữ liệu mẫu chỉ bác bỏ được một PTH (một phản ví dụ), không chứng minh được.

**Căn cứ của mỗi PTH:**

| Nhãn | Nghĩa |
|---|---|
| **[DDL]** | Khóa chính hoặc ràng buộc UNIQUE đã khai báo trong `database/data.sql` |
| **[v3]** | Quy tắc nêu trong bản mô tả v3 (ghi số mục), chưa chắc đã được DDL cưỡng chế |
| **[GT]** | Giả thiết đề xuất, cần xác nhận |

**Ký hiệu.** Mỗi PTH đánh số theo quan hệ, ví dụ `MH.f2` là PTH thứ hai của MATHANG. Vế phải có nhiều thuộc tính được viết gộp, sẽ tách ở mục 4. Giữ nguyên tên thuộc tính ở mục 2 nên không cần bảng đặt tên viết tắt. Thuộc tính in nghiêng ở tân từ là thuộc tính của quan hệ.

**Về khóa `Id` thay thế.** Phần lớn quan hệ có mã định danh nội bộ (`MaSP`, `MaDH`...) nên `Mã → mọi thuộc tính` luôn đúng. Phần quan trọng là các PTH **khác** của khóa thay thế (SKU, SoDH, cặp UNIQUE) và các PTH **không** được phép xác lập (xem mục 3.6).

## 3.2. Thực thể CƠ BẢN

### 3.2.1. LOAIHANG(MaLoai, TenLoai, MoTa, MaLoaiCha)

**‖LOAIHANG‖:** Mỗi loại hàng có một *MaLoai* riêng, có *TenLoai* và *MoTa*, và thuộc tối đa một loại cha *MaLoaiCha*. Hai loại hàng có thể trùng tên.

| PTH | Nội dung | Ý nghĩa nghiệp vụ | Căn cứ |
|---|---|---|---|
| LH.f1 | MaLoai → TenLoai, MoTa, MaLoaiCha | Biết mã loại thì biết tên, mô tả và loại cha | [DDL] PK; [v3] 1.2.1 |

Không xác lập: TenLoai → MaLoai (v3 nói tên có thể trùng; DDL không có UNIQUE trên tên, chỉ trên `Slug` mà `Slug` không thuộc mô hình).

### 3.2.2. THUONGHIEU(MaTH, TenTH, MoTa)

**‖THUONGHIEU‖:** Mỗi thương hiệu có một *MaTH* riêng, có *TenTH* và *MoTa*.

| PTH | Nội dung | Ý nghĩa nghiệp vụ | Căn cứ |
|---|---|---|---|
| TH.f1 | MaTH → TenTH, MoTa | Biết mã thương hiệu thì biết tên và mô tả | [DDL] PK; [v3] 1.2.1 |

**Điểm lệch cần quyết định.** DDL có UNIQUE trên `Brands.Name`, còn v3 nói tên thương hiệu "có thể trùng". Nếu chốt tên thương hiệu duy nhất thì thêm **TH.f2: TenTH → MaTH** và TenTH thành khóa ứng viên (ảnh hưởng mục 5). Bản này theo v3, không đưa TH.f2 vào F.

### 3.2.3. MATHANG(MaSP, SKU, TenSP, MoTa, GiaNiemYet, GiaKhuyenMai, ThoiHanBaoHanh, TinhTrangKinhDoanh, CoSeri, MaLoai, MaTH)

**‖MATHANG‖:** Mỗi mặt hàng có một *MaSP* nội bộ và một *SKU* không trùng mặt hàng nào khác; có *TenSP*, *MoTa*, *GiaNiemYet* hiện tại, *GiaKhuyenMai* nếu đang áp dụng, *ThoiHanBaoHanh* theo tháng, *TinhTrangKinhDoanh*, *CoSeri*; thuộc đúng một loại *MaLoai* và một thương hiệu *MaTH*.

| PTH | Nội dung | Ý nghĩa nghiệp vụ | Căn cứ |
|---|---|---|---|
| MH.f1 | MaSP → SKU, TenSP, MoTa, GiaNiemYet, GiaKhuyenMai, ThoiHanBaoHanh, TinhTrangKinhDoanh, CoSeri, MaLoai, MaTH | Biết mã nội bộ thì biết mọi thông tin hiện tại của mặt hàng | [DDL] PK; [v3] 1.2.1 |
| MH.f2 | SKU → MaSP | Mã hàng thương mại không trùng nhau nên xác định đúng một mặt hàng | [DDL] `UX_Products_SKU`; [v3] 1.2.1 |

Không xác lập (vì sao: xem 3.6): TenSP → MaSP; MaLoai → ThoiHanBaoHanh; MaLoai → CoSeri; MaTH → ThoiHanBaoHanh.

### 3.2.4. ANHMATHANG(MaAnh, MaSP, ViTri, DuongDan, LaAnhChinh, MoTaAnh)

**‖ANHMATHANG‖:** Mỗi ảnh có một *MaAnh* riêng, thuộc một mặt hàng *MaSP*, có *ViTri* sắp xếp, *DuongDan*, đánh dấu *LaAnhChinh* và *MoTaAnh*. Trong một mặt hàng, vị trí ảnh không trùng nhau và không dùng một đường dẫn hai lần.

| PTH | Nội dung | Ý nghĩa nghiệp vụ | Căn cứ |
|---|---|---|---|
| AMH.f1 | MaAnh → MaSP, ViTri, DuongDan, LaAnhChinh, MoTaAnh | Biết mã ảnh thì biết ảnh thuộc mặt hàng nào và các thông tin của ảnh | [DDL] PK |
| AMH.f2 | MaSP, ViTri → MaAnh | Trong một mặt hàng, mỗi vị trí chỉ có một ảnh | [v3] 1.2.1; **DDL chưa cưỡng chế** (`SortOrder` không có UNIQUE) |
| AMH.f3 | MaSP, DuongDan → MaAnh | Một mặt hàng không dùng cùng một ảnh hai lần | [DDL] `UX_ProductImages_ProductId_ImageUrl` |

Không phải PTH: "mỗi mặt hàng đang bán có đúng một ảnh chính". DDL chỉ bảo đảm **tối đa** một ảnh chính qua chỉ mục UNIQUE có điều kiện (`IsPrimary = 1`), không bảo đảm phải có một ảnh chính; đây là ràng buộc, không phải khóa của toàn quan hệ.

### 3.2.5. DINHNGHIATHONGSO(MaTS, MaLoai, TenTS, KieuGiaTri, DonVi, BatBuoc)

**‖DINHNGHIATHONGSO‖:** Mỗi thông số kỹ thuật có một *MaTS* riêng, áp dụng cho một loại hàng *MaLoai*, có *TenTS*, *KieuGiaTri* (chữ, số hoặc có/không), *DonVi* nếu có và *BatBuoc*. Trong cùng một loại hàng, tên thông số không trùng nhau.

| PTH | Nội dung | Ý nghĩa nghiệp vụ | Căn cứ |
|---|---|---|---|
| DNTS.f1 | MaTS → MaLoai, TenTS, KieuGiaTri, DonVi, BatBuoc | Biết mã thông số thì biết loại áp dụng và cách ghi giá trị | [DDL] PK |
| DNTS.f2 | MaLoai, TenTS → MaTS | Trong một loại hàng, mỗi tên thông số chỉ định nghĩa một lần | [DDL] `UX_SpecificationDefinitions_CategoryId_SpecName`; [v3] 1.2.1 |

Không xác lập: TenTS → KieuGiaTri hay TenTS → DonVi (cùng tên thông số ở loại khác có thể khác kiểu hoặc đơn vị; mẫu cho thấy 6 tên thông số như vậy).

### 3.2.6. GIATRITHONGSO(MaSP, MaTS, GiaTri): mối kết hợp MATHANG – DINHNGHIATHONGSO

**‖GIATRITHONGSO‖:** Mỗi mặt hàng *MaSP* có tối đa một giá trị *GiaTri* cho mỗi thông số *MaTS* của loại hàng mình thuộc về. *GiaTri* là chữ, số hoặc có/không tùy *KieuGiaTri* của thông số.

| PTH | Nội dung | Ý nghĩa nghiệp vụ | Căn cứ |
|---|---|---|---|
| GTTS.f1 | MaSP, MaTS → GiaTri | Cho một mặt hàng và một thông số thì có đúng một giá trị | [DDL] `UX_ProductSpecifications_ProductId_SpecDefinitionId`; [v3] 1.2.1 |

Không phải PTH nội bộ của quan hệ mà là ràng buộc giữa các quan hệ: thông số `MaTS` phải thuộc đúng loại hàng của `MaSP`, và `GiaTri` phải đúng kiểu `KieuGiaTri` (xem 3.9). DDL cũng chỉ bắt "có ít nhất một giá trị" trong ba cột giá trị, chưa bảo đảm "đúng một".

### 3.2.7. VAITRO(MaVT, TenVT)

**‖VAITRO‖:** Mỗi công việc có một *MaVT* riêng và *TenVT*. F: MaVT → TenVT [DDL] PK; [v3] 1.2.2.

## 3.3. Thực thể ĐỐI TƯỢNG NGOÀI

### 3.3.1. KHACHHANG(MaKH, HoTen, SDT, Email, MaSoThue)

**‖KHACHHANG‖:** Mỗi khách có một *MaKH* riêng, *HoTen*, *SDT*, *Email* nếu có và *MaSoThue* nếu là doanh nghiệp cần hóa đơn. Họ tên, số điện thoại, email không đủ để phân biệt hai khách.

| PTH | Nội dung | Ý nghĩa nghiệp vụ | Căn cứ |
|---|---|---|---|
| KH.f1 | MaKH → HoTen, SDT, Email, MaSoThue | Biết mã khách thì biết toàn bộ hồ sơ | [v3] 1.2.2 |

Không xác lập: SDT → MaKH, Email → MaKH (v3 nói không dùng để phân biệt; khi nối hồ sơ quầy vào tài khoản phải có bước xác nhận mã chính vì số điện thoại không đủ định danh).

### 3.3.2. DIACHINHANHANG(MaDC, MaKH, TenNguoiNhan, SDT, TinhThanh, PhuongXa, DiaChiCuThe, LaMacDinh)

**‖DIACHINHANHANG‖:** Mỗi địa chỉ nhận hàng có một *MaDC* riêng, thuộc một khách *MaKH*, ghi người nhận, số điện thoại và địa chỉ gồm tỉnh hoặc thành phố, phường hoặc xã, địa chỉ cụ thể. Mỗi khách có tối đa một địa chỉ mặc định.

| PTH | Nội dung | Ý nghĩa nghiệp vụ | Căn cứ |
|---|---|---|---|
| DC.f1 | MaDC → MaKH, TenNguoiNhan, SDT, TinhThanh, PhuongXa, DiaChiCuThe, LaMacDinh | Biết mã địa chỉ thì biết đầy đủ nội dung | [DDL] PK |

Không phải PTH: "tối đa một địa chỉ mặc định mỗi khách". DDL bảo đảm bằng chỉ mục UNIQUE có điều kiện (`IsDefault = 1`), chỉ bảo đảm **không quá một**, không bảo đảm phải có một.

### 3.3.3. NHANVIEN(MaNV, HoTen, SDT, TinhTrangLamViec)

**‖NHANVIEN‖:** Mỗi nhân viên có một *MaNV* riêng, *HoTen*, *SDT* và *TinhTrangLamViec*. F: NV.f1: MaNV → HoTen, SDT, TinhTrangLamViec [v3] 1.2.2.

### 3.3.4. NHACUNGCAP(MaNCC, TenNCC, NguoiLienHe, SDT, DiaChi, MaSoThue, TinhTrangHopTac)

**‖NHACUNGCAP‖:** Mỗi nhà cung cấp có một *MaNCC* riêng, có tên công ty, người liên hệ, số điện thoại, địa chỉ, mã số thuế và tình trạng hợp tác.

| PTH | Nội dung | Ý nghĩa nghiệp vụ | Căn cứ |
|---|---|---|---|
| NCC.f1 | MaNCC → TenNCC, NguoiLienHe, SDT, DiaChi, MaSoThue, TinhTrangHopTac | Biết mã thì biết toàn bộ hồ sơ | [DDL] PK; [v3] 1.2.9 |

Cùng điểm lệch với THUONGHIEU: DDL có UNIQUE trên `Suppliers.Name`, v3 nói tên có thể trùng. Nếu chốt tên duy nhất thì thêm NCC.f2: TenNCC → MaNCC. Mã số thuế chưa coi là khóa vì chưa có quy tắc bắt buộc và duy nhất (có thể để trống).

## 3.4. Thực thể NGHIỆP VỤ (ba nhóm phân tích sâu)

### Nhóm 3: phiếu nhập – sổ kho

#### 3.4.1. PHIEUNHAP(MaPN, SoPhieu, MaNCC, MaNV, ThoiDiemNhan, TinhTrang, SoHoaDonNCC, GhiChu)

**‖PHIEUNHAP‖:** Mỗi phiếu nhập ghi một lần nhận hàng thực tế, có *MaPN* và *SoPhieu* không trùng, do nhân viên *MaNV* lập từ nhà cung cấp *MaNCC*, tại *ThoiDiemNhan*, có *TinhTrang* (chờ xác nhận hoặc đã xác nhận), *SoHoaDonNCC* và *GhiChu*.

| PTH | Nội dung | Ý nghĩa nghiệp vụ | Căn cứ |
|---|---|---|---|
| PN.f1 | MaPN → SoPhieu, MaNCC, MaNV, ThoiDiemNhan, TinhTrang, SoHoaDonNCC, GhiChu | Biết mã phiếu thì biết nhà cung cấp, người lập, thời điểm và tình trạng | [DDL] PK |
| PN.f2 | SoPhieu → MaPN | Số phiếu không trùng nên xác định đúng một phiếu | [DDL] `UX_PurchaseReceipts_ReceiptCode`; [v3] 1.2.9 |

Không xác lập: (MaNCC, SoHoaDonNCC) → MaPN (một hóa đơn của nhà cung cấp có thể được giao làm nhiều lần, v3 chưa quy định). Tổng tiền phiếu không phải thuộc tính (dữ liệu tính, xem 3.7).

#### 3.4.2. CHITIETPHIEUNHAP(MaPN, SoDong, MaSP, SoLuong, GiaNhap): mối kết hợp PHIEUNHAP – MATHANG

**‖CHITIETPHIEUNHAP‖:** Mỗi dòng của phiếu nhập *MaPN* có số dòng *SoDong* riêng trong phiếu, ghi mặt hàng *MaSP*, *SoLuong* thực nhận và *GiaNhap* của dòng. Cùng một mặt hàng có thể ở nhiều dòng của một phiếu (khác giá hoặc khác lô).

| PTH | Nội dung | Ý nghĩa nghiệp vụ | Căn cứ |
|---|---|---|---|
| CTPN.f1 | MaPN, SoDong → MaSP, SoLuong, GiaNhap | Biết phiếu và số dòng thì biết mặt hàng, số lượng, giá nhập | [v3] 1.2.9 bước 3; DDL dùng `Id` riêng |

Không xác lập: (MaPN, MaSP) → SoLuong, GiaNhap hay (MaPN, MaSP) → SoDong. DDL không có UNIQUE cặp (phiếu, mặt hàng); v3 cho phép một mặt hàng nằm ở nhiều dòng. Không xác lập MaSP → GiaNhap (giá nhập thay đổi theo từng đợt, mục 1.1 khó khăn 2).

#### 3.4.3. GIAODICHKHO(MaGDK, MaSP, NhomKho, LoaiBienDong, SoLuong, ThoiDiem, MaNV, LoaiChungTu, MaChungTu, GhiChu)

**‖GIAODICHKHO‖:** Mỗi lần hàng vào, ra hoặc đổi nhóm trong kho có một *MaGDK*, ghi mặt hàng *MaSP*, nhóm tình trạng *NhomKho*, loại biến động *LoaiBienDong*, *SoLuong*, *ThoiDiem*, nhân viên thực hiện *MaNV* và chứng từ gốc (*LoaiChungTu*, *MaChungTu*). Chuyển nhóm tạo hai giao dịch đối ứng cùng thời điểm, cùng mặt hàng, khác nhóm.

| PTH | Nội dung | Ý nghĩa nghiệp vụ | Căn cứ |
|---|---|---|---|
| GDK.f1 | MaGDK → MaSP, NhomKho, LoaiBienDong, SoLuong, ThoiDiem, MaNV, LoaiChungTu, MaChungTu, GhiChu | Biết mã giao dịch thì biết mọi nội dung của lần biến động | [DDL] PK; [v3] 1.2.9 mục 7 |

Không xác lập: (MaSP, ThoiDiem) → MaGDK (chuyển nhóm tạo hai dòng cùng mặt hàng, cùng thời điểm); (LoaiChungTu, MaChungTu, MaSP) → MaGDK (mẫu có một cặp phiếu–mặt hàng xuất hiện ở hai giao dịch kho). `LoaiChungTu`, `MaChungTu` là liên kết đa hình, DDL không có khóa ngoại.

### Nhóm 2: đơn hàng – thanh toán

#### 3.4.4. DONHANG(MaDH, SoDH, ThoiDiemLap, KenhBan, LoaiDon, MaKH, MaNVBan, TenNguoiNhan, SDTNhan, DiaChiGiao, PhiGiao, GiamGia, MaMG, TinhTrang, DieuKienCoc, GhiChu)

**‖DONHANG‖:** Mỗi đơn hàng (phiếu bán tại quầy hoặc đơn từ xa) có *MaDH* và *SoDH* không trùng, lập tại *ThoiDiemLap* qua *KenhBan*, loại *LoaiDon*, của khách *MaKH* (nếu có), do nhân viên *MaNVBan* lập. Đơn ghi người nhận, số điện thoại và địa chỉ giao đã chốt khi xác nhận, *PhiGiao*, *GiamGia* đã chốt, tối đa một mã giảm giá *MaMG*, *TinhTrang* và *DieuKienCoc* nếu đặt cọc.

| PTH | Nội dung | Ý nghĩa nghiệp vụ | Căn cứ |
|---|---|---|---|
| DH.f1 | MaDH → SoDH, ThoiDiemLap, KenhBan, LoaiDon, MaKH, MaNVBan, TenNguoiNhan, SDTNhan, DiaChiGiao, PhiGiao, GiamGia, MaMG, TinhTrang, DieuKienCoc, GhiChu | Biết mã đơn thì biết toàn bộ nội dung đơn | [DDL] PK; [v3] 1.2.4 |
| DH.f2 | SoDH → MaDH | Số đơn không trùng nên xác định đúng một đơn | [DDL] `UX_Orders_OrderCode`; [v3] 1.2.4 mục 4 |

Không xác lập:

- MaKH → TenNguoiNhan, SDTNhan, DiaChiGiao: thông tin nhận hàng được **chốt** tại đơn (v3 1.2.4 mục 4), người nhận có thể khác khách và khác nhau giữa các đơn.
- MaMG → GiamGia: khoản giảm của đơn phụ thuộc giá trị đơn, mức tối đa và loại mã (phần trăm hoặc số tiền), nên cùng mã cho các đơn khác nhau có khoản giảm khác nhau.
- KenhBan → LoaiDon, LoaiDon → DieuKienCoc: điều kiện cọc ghi riêng cho từng đơn.

#### 3.4.5. CHITIETDONHANG(MaDH, SoDong, MaSP, SoLuong, DonGiaChot, TenHangChot, SKUChot): mối kết hợp DONHANG – MATHANG

**‖CHITIETDONHANG‖:** Mỗi dòng của đơn *MaDH* có số dòng *SoDong* riêng trong đơn, ghi mặt hàng *MaSP*, *SoLuong* và các giá trị **đã chốt** tại thời điểm xác nhận đơn: *DonGiaChot*, *TenHangChot*, *SKUChot*. Cùng một mặt hàng có thể ở nhiều dòng của một đơn nếu giá hoặc điều kiện bán khác nhau.

| PTH | Nội dung | Ý nghĩa nghiệp vụ | Căn cứ |
|---|---|---|---|
| CTDH.f1 | MaDH, SoDong → MaSP, SoLuong, DonGiaChot, TenHangChot, SKUChot | Biết đơn và số dòng thì biết mặt hàng, số lượng và giá đã bán | [v3] 1.2.3 bước 1, 1.2.4 mục 4; DDL dùng `Id` riêng |

Không xác lập (đây là bẫy chính của nhóm):

- **MaSP → DonGiaChot**: đơn giá là giá đã bán tại từng thời điểm. Mẫu bác bỏ: có 1 mặt hàng bán với nhiều đơn giá, và 9 trong 51 dòng đơn có đơn giá khác giá hiện tại của mặt hàng.
- **MaSP → TenHangChot, SKUChot**: là giá trị đã chốt (snapshot), không phải tên và mã hiện tại.
- **(MaDH, MaSP) → SoDong hoặc → SoLuong**: DDL không có UNIQUE cặp (đơn, mặt hàng); v3 cho phép nhiều dòng cùng mặt hàng. Mẫu hiện không có cặp trùng, nhưng mẫu không chứng minh quy tắc.

#### 3.4.6. GIUHANG(MaGiu, MaDH, SoDong, SoLuong, ThoiDiemGiu, ThoiDiemKetThuc, LyDoKetThuc)

**‖GIUHANG‖:** Mỗi lần giữ hàng có một *MaGiu*, gắn với dòng *SoDong* của đơn *MaDH* sau khi nhân viên xác nhận đơn, giữ *SoLuong* từ *ThoiDiemGiu* đến *ThoiDiemKetThuc* với *LyDoKetThuc* (xuất hàng, hủy đơn, giao thất bại, hết hạn trả trước).

| PTH | Nội dung | Ý nghĩa nghiệp vụ | Căn cứ |
|---|---|---|---|
| GH.f1 | MaGiu → MaDH, SoDong, SoLuong, ThoiDiemGiu, ThoiDiemKetThuc, LyDoKetThuc | Biết mã lần giữ thì biết dòng đơn, số lượng và thời gian giữ | [v3] 1.2.4 mục 3; chưa có trong DDL |

Không xác lập: (MaDH, SoDong) → MaGiu. Khi sửa đơn (số lượng đổi), một dòng đơn có thể được giữ lại nhiều lần theo thời gian; v3 chưa quy định chỉ một lần.

#### 3.4.7. THANHTOAN(MaTT, MaDH, LoaiKhoan, PhuongThuc, SoTien, ThoiDiem, KetQua, MaGiaoDichNgoai, DonViThanhToan, MaNVXacNhan)

**‖THANHTOAN‖:** Mỗi lần thanh toán có một *MaTT* riêng, thuộc đơn *MaDH*, loại khoản *LoaiKhoan* (cọc, thanh toán, thu khi giao), phương thức *PhuongThuc*, *SoTien*, *ThoiDiem*, *KetQua*; nếu qua ngân hàng, ví hoặc cổng thanh toán thì có *DonViThanhToan* và *MaGiaoDichNgoai* của bên đó; do *MaNVXacNhan* xác nhận.

| PTH | Nội dung | Ý nghĩa nghiệp vụ | Căn cứ |
|---|---|---|---|
| TT.f1 | MaTT → MaDH, LoaiKhoan, PhuongThuc, SoTien, ThoiDiem, KetQua, MaGiaoDichNgoai, DonViThanhToan, MaNVXacNhan | Biết mã lần thanh toán thì biết đơn, số tiền, phương thức và kết quả | [DDL] PK; [v3] 1.2.5 mục 1 |
| TT.f2 | DonViThanhToan, MaGiaoDichNgoai → MaTT | Mã giao dịch của bên thanh toán chỉ có ý nghĩa trong phạm vi bên đó, dùng để chống ghi nhận lặp | [GT] từ [v3] 1.2.5; DDL chưa cưỡng chế (`TransactionCode` không UNIQUE) |

Không xác lập: MaDH → PhuongThuc hay MaDH → SoTien (một đơn có nhiều lần thanh toán, kể cả cọc và phần còn lại). TT.f2 chỉ áp dụng khi hai thuộc tính đều có giá trị (thanh toán tiền mặt tại quầy không có mã giao dịch ngoài).

#### 3.4.8. MAGIAMGIA(MaMG, Code, TenChuongTrinh, LoaiGiam, MucGiam, DonToiThieu, GiamToiDa, NgayBatDau, NgayKetThuc, GioiHanLuot)

**‖MAGIAMGIA‖:** Mỗi mã giảm giá có *MaMG* riêng và *Code* không trùng, thuộc một chương trình *TenChuongTrinh*, giảm theo *LoaiGiam* với *MucGiam*, áp dụng từ *NgayBatDau* đến *NgayKetThuc* cho đơn từ *DonToiThieu*, giảm tối đa *GiamToiDa*, dùng tối đa *GioiHanLuot* lượt.

| PTH | Nội dung | Ý nghĩa nghiệp vụ | Căn cứ |
|---|---|---|---|
| MG.f1 | MaMG → Code, TenChuongTrinh, LoaiGiam, MucGiam, DonToiThieu, GiamToiDa, NgayBatDau, NgayKetThuc, GioiHanLuot | Biết mã nội bộ thì biết mọi điều kiện của mã | [DDL] PK |
| MG.f2 | Code → MaMG | Mã khách nhập không trùng nên xác định đúng một chương trình | [DDL] `IX_Coupons_Code`; [v3] 1.2.4 mục 6 |

## 3.5. Các thực thể nghiệp vụ còn lại (nêu tập F ngắn gọn)

Chưa phân tích sâu; mỗi quan hệ chỉ có PTH của mã định danh và các khóa thay thế nêu trong v3. Căn cứ chung: [v3] mục tương ứng; các quan hệ này **chưa có trong DDL**, trừ TAIKHOAN, GIOHANG và CHITIETGIOHANG.

| Quan hệ | Tập F | Ghi chú |
|---|---|---|
| TAIKHOAN | MaTK → DinhDanhDangNhap, MaKH, TinhTrang, NgayDangKy, ThoiDiemNoiHoSo; DinhDanhDangNhap → MaTK | Định danh đăng nhập không trùng; MaKH → MaTK không xác lập (v3 chỉ nói mỗi tài khoản gắn tối đa một khách) |
| GIOHANG | MaGio → MaTK, TinhTrang, ThoiDiemTao | "Mỗi tài khoản tối đa một giỏ đang dùng" là ràng buộc có điều kiện, không phải PTH |
| CHITIETGIOHANG | MaGio, MaSP → SoLuong | v3: mỗi mặt hàng một dòng trong giỏ; DDL UNIQUE `(CartId, ProductId)` |
| HANGCOSERI | HS.f1: MaSeri → SoSeri, MaSP, MaPN, SoDongNhap, MaDH, SoDongDon, TinhTrang, ThoiDiemNhap; HS.f2: MaSP, SoSeri → MaSeri; HS.f3: MaPN, SoDongNhap → MaSP; HS.f4: MaDH, SoDongDon → MaSP | HS.f2 là **[GT]** (seri duy nhất trong cùng mặt hàng, chưa kiểm chứng). HS.f3, HS.f4 theo [v3] 1.2.9 mục 2 và 1.2.3 bước 1 (dòng nhập, dòng đơn đã xác định mặt hàng). Vế trái của f3, f4 không phải khóa (một dòng có nhiều chiếc có seri) nên MaSP là thuộc tính dư thừa, ứng viên cho bước cải tiến ở mục 8, 9 |
| DOTKIEMKE | MaDot → LoaiKiemKe, ThoiDiem, MaNVLap, MaNVDuyet, ThoiDiemDuyet, TinhTrang | |
| CHITIETKIEMKE | MaDot, MaSP → SoLuongSo, SoLuongDem, LyDoChenhLech | Chênh lệch là dữ liệu tính |
| DIEUCHINHDON | MaDieuChinh → MaDH, ThoiDiem, MaNV, NoiDungTruoc, NoiDungSau, KhachDongY | |
| KHOANHOAN | MaHoan → MaTT, MaHS, SoTien, PhuongThucHoan, MaNVDuyet, ThoiDiemDuyet, ThoiDiemChi | Tổng hoàn không vượt tiền đã thu: ràng buộc giữa các quan hệ |
| PHIEUGIAO | MaGiao → MaDH, MaNVGiao, ThoiDiemXuat, TinhTrang | v3: mỗi đơn giao trọn trong một đợt nên có thể thêm MaDH → MaGiao **[GT]** |
| LANGIAO | MaGiao, SoLan → ThoiDiem, KetQua, LyDoThatBai | SoLan chỉ nhận 1 đến 3 |
| BANGIAOCOD | MaBG → MaGiao, MaTT, MaNVGiao, MaNVNhan, SoTien, ThoiDiem | |
| HOSODOITRA | MaHS → MaDH, MaKH, NgayDeNghi, LoaiTruongHop, LyDo, TinhTrang, HinhThucXuLy, MaNVTiepNhan | LoaiTruongHop quyết định thời hạn (48 giờ, 30 ngày, 7 ngày) |
| CHITIETTRA | MaHS, MaDH, SoDong → SoLuongTra, MaSeri; **MaHS → MaDH** | PTH thứ hai theo [v3] 1.2.8: mỗi hồ sơ có đúng một đơn gốc nên MaHS xác định MaDH (bổ sung khi chuyển sang mô hình quan hệ, mục 7); khóa là (MaHS, SoDong). Tổng số lượng trả không vượt số đã giao: ràng buộc giữa các quan hệ |
| LANNHANLAI | MaNhanLai → MaHS, ThoiDiemNhan, MaNVKiemTra, KetLuan, NhomSauKiemTra, MaNVDuyet, ThoiDiemDuyet | |
| PHIEUBAOHANH | PB.f1: MaPhieuBH → MaKH, MaSP, MaSeri, MaDH, SoDong, MoTaLoi, PhuKienDiKem, NgayNhan, NgayHenTra, NgayTraThucTe, TinhTrang, KetQua, LyDoTuChoi, MaNVTiepNhan; PB.f2: MaDH, SoDong → MaSP; PB.f3: MaSeri → MaSP | PB.f2, PB.f3 theo [v3] 1.2.7 (dòng mua gốc và số seri đã xác định mặt hàng). Vế trái không phải khóa (một dòng hoặc một chiếc có thể có nhiều phiếu bảo hành theo thời gian) nên MaSP dư thừa |
| PHIEUGUIHANG | MaGui → MaNCC, LyDo, NgayGui, NgayNhanKetQua, KetQua, MaNVGui | |
| CHITIETGUIHANG | MaGui, SoDong → MaSP, MaSeri, SoLuong, MaPhieuBH, MaHS | |
| BIENDONGSODU | MaBD → MaTK, SoTien, LoaiBienDong, MaHoan, ThoiDiem | Tùy chọn |
| NHANVIEN_VAITRO | (không có PTH không tầm thường; khóa là cả hai thuộc tính MaNV, MaVT) | Quan hệ toàn khóa |
| CHITIETKIEMKE, CHITIETTRA, CHITIETGUIHANG | xem các dòng trên | |

Hai quan hệ HANGCOSERI, PHIEUBAOHANH (và trường hợp GIAODICHKHO ở 3.6) cho thấy dạng PTH bắc cầu qua khóa ngoại: một thuộc tính (`MaSP`) lưu thêm dù đã suy được từ dòng đơn, dòng nhập hoặc số seri. Những PTH này có vế trái không phải siêu khóa nên quan hệ không đạt BCNF; ở PHIEUBAOHANH, MaSP không thuộc khóa nào nên còn vi phạm cả 3NF (HANGCOSERI xem mục 5.8). Đây là tình huống tốt cho phần cải tiến ở mục 8 và 9.

## 3.6. Các PTH tưởng đúng nhưng không xác lập, vì sao

| PTH bị loại | Quan hệ | Lý do | Bằng chứng |
|---|---|---|---|
| MaSP → DonGiaChot | CHITIETDONHANG | Giá đã bán thay đổi theo thời điểm | **Mẫu bác bỏ**: 1 mặt hàng có nhiều đơn giá; 9/51 dòng khác giá hiện tại |
| MaSP → TenHangChot, SKUChot | CHITIETDONHANG | Giá trị đã chốt, không phải thông tin hiện tại | Quy tắc v3 1.2.4 mục 4 |
| MaSP → GiaNhap | CHITIETPHIEUNHAP | Giá nhập thay đổi theo đợt | Quy tắc v3 1.1 khó khăn 2 (mẫu chưa bác bỏ: không mặt hàng nào có hai giá nhập; nhưng mẫu không chứng minh) |
| MaLoai → ThoiHanBaoHanh | MATHANG | Thời hạn phụ thuộc hãng và dòng hàng, không chỉ loại | **Mẫu bác bỏ**: 9/17 loại hàng có nhiều giá trị (ví dụ nguồn máy tính: 36 và 120 tháng) |
| MaTH → ThoiHanBaoHanh | MATHANG | Một hãng bảo hành khác nhau theo dòng | **Mẫu bác bỏ**: 12 thương hiệu có nhiều giá trị |
| MaLoai → CoSeri | MATHANG | Chưa có quy tắc "mọi mặt hàng cùng loại cùng có hoặc không có seri" | **Cần quyết định.** Nếu v3 chốt quy tắc này thì MATHANG có PTH bắc cầu MaSP → MaLoai → CoSeri và không đạt 3NF; phải tách (mục 9) |
| LoaiBienDong → LoaiChungTu | GIAODICHKHO | Đúng cho nhập (phiếu nhập), bán, giao (đơn); sai cho chuyển nhóm, điều chỉnh (nhiều nguồn chứng từ) | **Cần quyết định.** Nếu chốt mỗi loại biến động chỉ có một loại chứng từ thì có thêm PTH không khóa, GIAODICHKHO không đạt 3NF |
| TenTS → KieuGiaTri, DonVi | DINHNGHIATHONGSO | Cùng tên ở loại khác có thể khác kiểu hoặc đơn vị | **Mẫu bác bỏ**: 6 tên thông số như vậy |
| TenLoai → MaLoai | LOAIHANG | v3: tên có thể trùng | DDL không UNIQUE trên tên |
| (MaDH, MaSP) → SoDong | CHITIETDONHANG | v3 cho phép nhiều dòng cùng mặt hàng | DDL không UNIQUE; mẫu không có cặp trùng nhưng không chứng minh |
| (MaPN, MaSP) → SoDong | CHITIETPHIEUNHAP | Như trên | DDL không UNIQUE |
| MaMG → GiamGia | DONHANG | Khoản giảm tùy đơn | Quy tắc v3 1.2.4 mục 6 |
| MaKH → TenNguoiNhan, SDTNhan, DiaChiGiao | DONHANG | Thông tin nhận hàng được chốt tại đơn | Quy tắc v3 1.2.4 mục 4 |
| (LoaiChungTu, MaChungTu, MaSP) → MaGDK | GIAODICHKHO | Một chứng từ có thể sinh nhiều giao dịch cùng mặt hàng | **Mẫu bác bỏ**: 1 cặp phiếu–mặt hàng xuất hiện ở 2 giao dịch |
| MaDH → PhuongThuc | THANHTOAN | Một đơn có nhiều lần thanh toán | Quy tắc v3 1.2.5 mục 1 |

## 3.7. PTH phát sinh nếu lưu sẵn cột dẫn xuất

v3 xếp các giá trị dưới đây vào dữ liệu tính toán nên **chưa đưa vào F**. DDL hiện tại lại lưu sẵn chúng; nếu giữ thì mỗi cột tạo thêm một PTH và phải phân tích ở mục 8, 9.

| Cột lưu sẵn (DDL) | PTH nếu lưu | Hệ quả dạng chuẩn | Ghi chú dữ liệu mẫu |
|---|---|---|---|
| `OrderItems.LineTotal` | SoLuong, DonGiaChot → ThanhTien | Vế trái không phải siêu khóa → không đạt 3NF | DDL có CHECK `LineTotal = UnitPrice × Quantity` |
| `Orders.Subtotal`, `Orders.TotalAmount` | Subtotal, PhiGiao, GiamGia → TongPhaiTra; Subtotal phụ thuộc vào tập dòng đơn (phụ thuộc giữa quan hệ) | Không đạt 3NF | CHECK `TotalAmount = Subtotal + ShippingFee − DiscountAmount`; mẫu: 0 đơn lệch |
| `PurchaseReceiptItems.LineTotal` | SoLuong, GiaNhap → ThanhTien | Không đạt 3NF | CHECK có |
| `PurchaseReceipts.Subtotal`, `TotalAmount` | Tổng các dòng của phiếu | Phụ thuộc giữa quan hệ | **Mẫu: 1 trong 7 phiếu lệch tổng 3.518.000 đồng** |
| `Products.StockQuantity`, `SoldQuantity` | Tính từ GIAODICHKHO và các đơn | Phụ thuộc giữa quan hệ | **Mẫu: 134/134 mặt hàng lệch tồn so với sổ kho**; chi tiết ở `database/data-integrity-report.md` |
| `StockTransactions.BeforeQuantity`, `AfterQuantity` | AfterQuantity = BeforeQuantity ± Quantity (theo loại) | Cột suy diễn | Mẫu: 4 chỗ đứt chuỗi |
| `Coupons.UsedCount` | Đếm các đơn dùng mã | Phụ thuộc giữa quan hệ | Mẫu khớp |

## 3.8. Phụ thuộc đa trị (chỉ ghi nhận cho mục 9)

Tách riêng ảnh và thông số của mặt hàng là tình huống thử 4NF. Nếu gộp hai tập này vào một quan hệ giả định MATHANG_ANH_TS(MaSP, ViTri, DuongDan, MaTS, GiaTri) thì theo v3 ("thêm ảnh không làm đổi thông số") có hai phụ thuộc đa trị độc lập:

- MaSP ↠ ViTri, DuongDan
- MaSP ↠ MaTS, GiaTri

Mỗi mặt hàng có tập ảnh và tập thông số **độc lập** nên gộp sẽ phải nhân tích hai tập. Đây là căn cứ để giữ ANHMATHANG và GIATRITHONGSO là hai quan hệ riêng (4NF); chứng minh đầy đủ nằm ở mục 9. Hai quan hệ sau tách đều chỉ có PTH nêu ở 3.2.4 và 3.2.6.

## 3.9. Ràng buộc nghiệp vụ không phải PTH

Các quy tắc sau nằm trong v3 nhưng không biểu diễn được bằng PTH trong một quan hệ; sẽ xử lý ở phần ràng buộc toàn vẹn.

| Quy tắc | Loại |
|---|---|
| Thông số `MaTS` của GIATRITHONGSO phải thuộc đúng loại hàng của `MaSP` | Liên quan hệ |
| `GiaTri` đúng kiểu `KieuGiaTri` của thông số | Miền giá trị theo dữ liệu |
| Mỗi mặt hàng đang bán có đúng một ảnh chính | Tồn tại có điều kiện |
| Loại hàng không tạo vòng cha–con | Ràng buộc đệ quy |
| Mỗi mã giảm giá không dùng vượt `GioiHanLuot`, không dùng ngoài khoảng ngày | Tổng hợp |
| Một đơn tối đa 3 lần giao thất bại | Tổng hợp |
| Tổng các khoản hoàn của một khoản thu không vượt số tiền đã thu | Tổng hợp |
| Tổng số lượng trả của một dòng đơn không vượt số lượng đã giao | Tổng hợp |
| Phiếu nhập xác nhận phải có ít nhất một dòng và chỉ ghi tăng kho một lần | Tồn tại, trạng thái |
| Đơn trả trước chỉ giao khi đã thu đủ; không thu đủ sau 24 giờ thì hủy | Quy tắc trạng thái |
| Chuyển nhóm kho tạo hai giao dịch đối ứng, không làm đổi tổng số hàng | Tổng hợp |

## 3.10. Điểm cần xác nhận và câu hỏi giảng viên có thể hỏi

**Cần xác nhận:**

1. Có chốt tên thương hiệu và tên nhà cung cấp là duy nhất (DDL đã có, v3 nói ngược lại).
2. Có cưỡng chế (MaSP, ViTri) duy nhất trong ANHMATHANG (v3 có, DDL chưa).
3. Quy tắc "mọi mặt hàng cùng loại cùng có hoặc không có seri" có đúng không (quyết định MATHANG có đạt 3NF hay không).
4. Seri chỉ duy nhất trong cùng mặt hàng hay toàn cửa hàng.
5. Mỗi loại biến động kho có đúng một loại chứng từ nguồn hay nhiều (xem 3.6).
6. Có giữ cột dẫn xuất (3.7) trong thiết kế đề xuất hay chỉ tính khi truy vấn.

**Câu hỏi có thể gặp:**

- *Vì sao MaSP → DonGiaChot không phải PTH?* Vì giá đã chốt thay đổi theo thời điểm; mẫu cho thấy một mặt hàng có nhiều đơn giá. Nếu coi là PTH thì sẽ đòi hỏi tách giá ra một quan hệ riêng và mất ý nghĩa lịch sử.
- *Vì sao (MaDH, MaSP) không phải khóa của CHITIETDONHANG?* Vì v3 cho phép một mặt hàng xuất hiện ở nhiều dòng của một đơn (giá hoặc điều kiện khác nhau), và DDL không có UNIQUE cặp này.
- *Vì sao SKU → MaSP là PTH còn TenSP → MaSP thì không?* SKU được khai báo duy nhất (UNIQUE) còn tên sản phẩm chưa có quy tắc duy nhất; mẫu không có tên trùng nhưng mẫu không chứng minh quy tắc.
- *Dữ liệu mẫu dùng để làm gì ở mục này?* Chỉ để bác bỏ PTH (tìm phản ví dụ), không dùng để chứng minh.
