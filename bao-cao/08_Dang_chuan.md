# MỤC 8. XÁC ĐỊNH DẠNG CHUẨN TỪNG BẢNG VÀ DẠNG CHUẨN CỦA LƯỢC ĐỒ

Căn cứ: lược đồ quan hệ ở [07_Mo_hinh_quan_he.md](07_Mo_hinh_quan_he.md), phủ tối thiểu ở [04_Phu_toi_thieu.md](04_Phu_toi_thieu.md), khóa ở [05_Tim_khoa.md](05_Tim_khoa.md). Xét **38 quan hệ** theo **mọi khóa ứng viên**, đến BCNF. Dạng chuẩn 4NF (phụ thuộc đa trị) được xét ở mục 9 cùng phần cải tiến.

## 8.1. Định nghĩa và cách kiểm tra

Theo bài giảng:

| Dạng chuẩn | Điều kiện |
|---|---|
| **DC1 (1NF)** | Mọi thuộc tính là đơn, nguyên tố: không đa trị, không nhóm lặp |
| **DC2 (2NF)** | Đạt DC1 và mọi thuộc tính không khóa phụ thuộc **đầy đủ** vào khóa (không phụ thuộc một phần). Khóa chỉ một thuộc tính thì đạt DC2 |
| **DC3 (3NF)** | Với mọi PTH không tầm thường X → A: X là siêu khóa **hoặc** A là thuộc tính khóa (không có phụ thuộc bắc cầu vào khóa) |
| **BCNF** | Với mọi PTH không tầm thường X → A: X là siêu khóa |

**Thuộc tính khóa** là thuộc tính thuộc ít nhất một khóa ứng viên; ngược lại là thuộc tính không khóa. BCNF ⇒ 3NF ⇒ 2NF ⇒ 1NF. Dạng chuẩn của lược đồ là dạng chuẩn **thấp nhất** trong các quan hệ; bài giảng nêu DC3 là dạng chuẩn tối thiểu mong muốn của lược đồ.

**Cách kiểm tra** (dùng phủ tối thiểu G của mục 4, khóa của mục 5):

1. **2NF:** với từng khóa ứng viên K và từng tập con thực sự X của K, tính X⁺; nếu X⁺ chứa thuộc tính không khóa thì có phụ thuộc bộ phận.
2. **3NF:** xét từng PTH X → A trong G (A ∉ X); vi phạm nếu X không là siêu khóa và A không là thuộc tính khóa.
3. **BCNF:** xét từng PTH X → A trong G; vi phạm nếu X không là siêu khóa. Vì G là phủ của F nên chỉ cần xét các PTH trong G.

Kết quả tay được đối chiếu bằng chương trình ([tools/dangchuan.py](tools/dangchuan.py)): tính khóa bằng duyệt mọi tập con, rồi kiểm tra 2NF, 3NF, BCNF.

## 8.2. Dạng chuẩn 1 (DC1)

**Nhóm lặp và thuộc tính đa trị đã được tách.** Ảnh, thông số, dòng đơn, dòng phiếu nhập, dòng giỏ, vai trò nhân viên, lần giao, lần nhận lại... đều là quan hệ riêng nên không có ô nào chứa danh sách. Mọi cột là một giá trị đơn.

**Các thuộc tính cần xem kỹ:**

| Thuộc tính | Quan hệ | Nhận xét | Kết luận |
|---|---|---|---|
| HoTen | KHACHHANG, NHANVIEN | Gộp họ, tên lót, tên. Bài giảng nêu ví dụ `HoTen` là đa trị (Họ + Lót + Tên) vì có truy vấn theo từng phần, và sửa thành (HoLot, Ten) | Xem phương án dưới |
| TenNguoiNhan | DIACHINHANHANG, DONHANG | Như trên | Xem phương án dưới |
| NguoiLienHe | NHACUNGCAP | Như trên | Xem phương án dưới |
| DiaChiCuThe, DiaChiGiao | DIACHINHANHANG, DONHANG | Số nhà và đường; tỉnh và phường hoặc xã đã tách riêng; cửa hàng không tìm riêng số nhà | Đạt DC1 theo nghiệp vụ |
| TenSP, TenHangChot | MATHANG, CHITIETDONHANG | Tên thương mại; thương hiệu và loại đã tách thành quan hệ riêng | Đạt DC1 |
| GiaTri | GIATRITHONGSO | Một giá trị theo kiểu của thông số (DDL tách thành ba cột chữ, số, có/không) | Đạt DC1 |

**Hai phương án cho họ tên.**

- **Phương án 1 (dùng làm mặc định):** cửa hàng chỉ in, đọc và tìm họ tên nguyên chuỗi, chưa có yêu cầu truy vấn theo họ hoặc theo tên, nên coi `HoTen` là thuộc tính đơn. Mọi quan hệ đạt DC1.
- **Phương án 2 (theo ví dụ bài giảng):** nếu giảng viên yêu cầu tách, thay `HoTen` bằng `HoLot`, `Ten` ở KHACHHANG và NHANVIEN (và tương tự `TenNguoiNhan`, `NguoiLienHe`). Thay đổi này không ảnh hưởng PTH nào khác. Theo phương án này lược đồ **chưa đạt DC1** cho tới khi tách; nên hỏi giảng viên.

## 8.3. Phân tích chi tiết các quan hệ có nhiều khóa hoặc nhiều PTH

### 8.3.1. Nhóm "mã định danh cộng khóa thay thế": BCNF

Sáu quan hệ có G = { A → các thuộc tính còn lại ; B → A } với A, B đều là khóa (mục 5, 5.4.5). Mọi PTH có vế trái là một khóa nên là siêu khóa.

| Quan hệ | Khóa ứng viên | Số thuộc tính khóa | Số thuộc tính không khóa | Dạng chuẩn |
|---|---|---|---|---|
| MATHANG | {MaSP}; {SKU} | 2 | 9 | BCNF |
| DONHANG | {MaDH}; {SoDH} | 2 | 14 | BCNF |
| PHIEUNHAP | {MaPN}; {SoPhieu} | 2 | 6 | BCNF |
| MAGIAMGIA | {MaMG}; {Code} | 2 | 8 | BCNF |
| TAIKHOAN | {MaTK}; {DinhDanhDangNhap} | 2 | 4 | BCNF |
| PHIEUGIAO | {MaGiao}; {MaDH} | 2 | 3 | BCNF |

- **2NF:** hai khóa đều một thuộc tính nên không có tập con thực sự, không có phụ thuộc bộ phận.
- **3NF và BCNF:** mọi PTH trong G có vế trái A hoặc B, đều là siêu khóa → không vi phạm.

**Kết luận:** MATHANG, DONHANG, PHIEUNHAP, MAGIAMGIA, TAIKHOAN, PHIEUGIAO đạt **BCNF**. (PHIEUGIAO dựa trên giả thiết mỗi đơn giao một đợt; nếu bỏ giả thiết, khóa duy nhất là MaGiao và vẫn đạt BCNF.)

### 8.3.2. THANHTOAN: BCNF

Khóa: {MaTT} và {DonViThanhToan, MaGiaoDichNgoai}. Thuộc tính khóa: MaTT, DonViThanhToan, MaGiaoDichNgoai; không khóa: MaDH, LoaiKhoan, PhuongThuc, SoTien, ThoiDiem, KetQua, MaNVXacNhan.

- **2NF:** xét tập con thực sự của khóa ghép: (DonViThanhToan)⁺ = {DonViThanhToan}, (MaGiaoDichNgoai)⁺ = {MaGiaoDichNgoai}; không chứa thuộc tính không khóa → không có phụ thuộc bộ phận.
- **3NF, BCNF:** hai PTH trong G có vế trái MaTT và (DonViThanhToan, MaGiaoDichNgoai), đều là khóa → đạt.

**Kết luận: BCNF.**

### 8.3.3. ANHMATHANG: BCNF

Khóa: {MaAnh}, {MaSP, ViTri}, {MaSP, DuongDan}. Thuộc tính khóa: MaAnh, MaSP, ViTri, DuongDan; không khóa: LaAnhChinh, MoTaAnh.

- **2NF:** các tập con thực sự: MaSP⁺ = {MaSP}, ViTri⁺ = {ViTri}, DuongDan⁺ = {DuongDan} → không có phụ thuộc bộ phận.
- **3NF, BCNF:** vế trái các PTH là MaAnh, (MaSP, ViTri), (MaSP, DuongDan), đều là khóa.

**Kết luận: BCNF.** Quan hệ có ba khóa ứng viên nhưng vẫn đạt BCNF vì kiểm theo từng khóa đều đạt.

### 8.3.4. DINHNGHIATHONGSO: BCNF

Khóa: {MaTS}, {MaLoai, TenTS}. Không khóa: KieuGiaTri, DonVi, BatBuoc. MaLoai⁺ = {MaLoai}, TenTS⁺ = {TenTS} nên không có phụ thuộc bộ phận; mọi PTH có vế trái là khóa. **Kết luận: BCNF.**

### 8.3.5. HANGCOSERI: 3NF, không đạt BCNF

**Khóa:** {MaSeri}, {SoSeri, MaSP}, {SoSeri, MaPN, SoDongNhap}, {SoSeri, MaDH, SoDongDon}.
**Thuộc tính khóa:** MaSeri, SoSeri, MaSP, MaPN, SoDongNhap, MaDH, SoDongDon. **Không khóa:** TinhTrang, ThoiDiemNhap.

**PTH trong G:** MaSeri → SoSeri, MaPN, SoDongNhap, MaDH, SoDongDon, TinhTrang, ThoiDiemNhap; (MaSP, SoSeri) → MaSeri; **(MaPN, SoDongNhap) → MaSP**; **(MaDH, SoDongDon) → MaSP**.

- **2NF:** xét tập con thực sự của từng khóa ghép. Ví dụ (MaPN, SoDongNhap)⁺ = {MaPN, SoDongNhap, MaSP}: chỉ thêm MaSP, là thuộc tính khóa chứ không phải thuộc tính không khóa. Không tập con nào có bao đóng chứa TinhTrang hay ThoiDiemNhap → **đạt 2NF**.
- **3NF:** các PTH có vế trái không phải siêu khóa là (MaPN, SoDongNhap) → MaSP và (MaDH, SoDongDon) → MaSP. Vế phải MaSP là **thuộc tính khóa** (thuộc khóa {SoSeri, MaSP}) nên không vi phạm → **đạt 3NF**.
- **BCNF:** vế trái (MaPN, SoDongNhap) và (MaDH, SoDongDon) không là siêu khóa (bao đóng không chứa SoSeri) → **vi phạm BCNF**.

**Kết luận: 3NF.** Kết luận này phụ thuộc giả thiết "số seri duy nhất trong cùng mặt hàng" (mục 5.7). Nếu số seri duy nhất toàn cửa hàng, khóa còn {MaSeri} và {SoSeri}, MaSP không thuộc khóa nào và HANGCOSERI **chỉ đạt 2NF** (xem kịch bản S1 ở 8.7).

### 8.3.6. PHIEUBAOHANH: 2NF, không đạt 3NF

**Khóa:** {MaPhieuBH} (duy nhất). Mọi thuộc tính còn lại là không khóa.
**PTH trong G:** MaPhieuBH → các thuộc tính còn lại; **(MaDH, SoDong) → MaSP**; **MaSeri → MaSP**.

- **2NF:** khóa chỉ một thuộc tính nên không có phụ thuộc bộ phận → **đạt 2NF**.
- **3NF:** (MaDH, SoDong) → MaSP có vế trái không là siêu khóa (một dòng đơn có thể có nhiều phiếu bảo hành) và MaSP không phải thuộc tính khóa; tương tự MaSeri → MaSP → **vi phạm 3NF**. Đây là phụ thuộc bắc cầu vào khóa: MaPhieuBH → (MaDH, SoDong) → MaSP, đúng dạng "AB → C" trong ví dụ của bài giảng.

**Kết luận: 2NF.**

### 8.3.7. CHITIETTRA: chỉ đạt 1NF

**Khóa:** {MaHS, SoDong} (mục 5, 5.5). **Thuộc tính khóa:** MaHS, SoDong. **Không khóa:** MaDH, SoLuongTra, MaSeri.
**PTH trong G:** (MaHS, SoDong) → SoLuongTra, MaSeri; **MaHS → MaDH**.

- **2NF:** MaHS là một phần của khóa và MaHS → MaDH, trong đó MaDH là thuộc tính không khóa → có **phụ thuộc bộ phận** → **không đạt 2NF**. Hoàn toàn giống ví dụ KetQua(MSSV, MAMH, TenMH, Diem) của bài giảng: TenMH chỉ phụ thuộc MAMH, một phần của khóa.
- Vì không đạt 2NF nên không xét tiếp 3NF, BCNF.

**Kết luận: 1NF.** MaDH được giữ trong quan hệ để tạo khóa ngoại ghép tới dòng đơn, nhưng nó đã có sẵn ở HOSODOITRA (mục 9 xử lý).

## 8.4. Các quan hệ còn lại: BCNF

Với 26 quan hệ mà F chỉ có PTH "khóa → tất cả thuộc tính còn lại" (kể cả NHANVIEN_VAITRO toàn khóa):

- **BCNF:** mọi PTH không tầm thường có vế trái là khóa, nên là siêu khóa.
- **2NF với khóa ghép:** F không có PTH nào có vế trái là tập con thực sự của khóa (mục 4.4), nên không có phụ thuộc bộ phận; ngoài ra BCNF kéo theo 2NF.

| Quan hệ | Khóa duy nhất | Dạng chuẩn |
|---|---|---|
| LOAIHANG | {MaLoai} | BCNF |
| THUONGHIEU | {MaTH} | BCNF |
| VAITRO | {MaVT} | BCNF |
| KHACHHANG | {MaKH} | BCNF |
| DIACHINHANHANG | {MaDC} | BCNF |
| NHANVIEN | {MaNV} | BCNF |
| NHACUNGCAP | {MaNCC} | BCNF |
| GIAODICHKHO | {MaGDK} | BCNF |
| DOTKIEMKE | {MaDot} | BCNF |
| GIOHANG | {MaGio} | BCNF |
| DIEUCHINHDON | {MaDieuChinh} | BCNF |
| GIUHANG | {MaGiu} | BCNF |
| KHOANHOAN | {MaHoan} | BCNF |
| LANGIAO | {MaGiao, SoLan} | BCNF |
| BANGIAOCOD | {MaBG} | BCNF |
| HOSODOITRA | {MaHS} | BCNF |
| LANNHANLAI | {MaNhanLai} | BCNF |
| PHIEUGUIHANG | {MaGui} | BCNF |
| BIENDONGSODU | {MaBD} | BCNF |
| CHITIETDONHANG | {MaDH, SoDong} | BCNF |
| CHITIETPHIEUNHAP | {MaPN, SoDong} | BCNF |
| CHITIETGIOHANG | {MaGio, MaSP} | BCNF |
| GIATRITHONGSO | {MaSP, MaTS} | BCNF |
| NHANVIEN_VAITRO | {MaNV, MaVT} | BCNF |
| CHITIETKIEMKE | {MaDot, MaSP} | BCNF |
| CHITIETGUIHANG | {MaGui, SoDong} | BCNF |

## 8.5. Bảng tổng hợp 38 quan hệ

| STT | Quan hệ | Loại | Khóa ứng viên | Vi phạm | Dạng chuẩn |
|---|---|---|---|---|---|
| 1 | LOAIHANG | Cơ bản | {MaLoai} | — | **BCNF** |
| 2 | THUONGHIEU | Cơ bản | {MaTH} | — | **BCNF** |
| 3 | MATHANG | Cơ bản | {MaSP}; {SKU} | — | **BCNF** |
| 4 | ANHMATHANG | Cơ bản | {MaAnh}; {MaSP, ViTri}; {MaSP, DuongDan} | — | **BCNF** |
| 5 | DINHNGHIATHONGSO | Cơ bản | {MaTS}; {MaLoai, TenTS} | — | **BCNF** |
| 6 | VAITRO | Cơ bản | {MaVT} | — | **BCNF** |
| 7 | KHACHHANG | Đối tượng ngoài | {MaKH} | — | **BCNF** |
| 8 | DIACHINHANHANG | Đối tượng ngoài | {MaDC} | — | **BCNF** |
| 9 | NHANVIEN | Đối tượng ngoài | {MaNV} | — | **BCNF** |
| 10 | NHACUNGCAP | Đối tượng ngoài | {MaNCC} | — | **BCNF** |
| 11 | TAIKHOAN | Nghiệp vụ | {MaTK}; {DinhDanhDangNhap} | — | **BCNF** |
| 12 | PHIEUNHAP | Nghiệp vụ | {MaPN}; {SoPhieu} | — | **BCNF** |
| 13 | HANGCOSERI | Nghiệp vụ | {MaSeri}; {SoSeri, MaSP}; {SoSeri, MaPN, SoDongNhap}; {SoSeri, MaDH, SoDongDon} | MaPN, SoDongNhap → MaSP (vế trái không là siêu khóa; vế phải là thuộc tính khóa); MaDH, SoDongDon → MaSP (vế trái không là siêu khóa; vế phải là thuộc tính khóa) | **3NF** |
| 14 | GIAODICHKHO | Nghiệp vụ | {MaGDK} | — | **BCNF** |
| 15 | DOTKIEMKE | Nghiệp vụ | {MaDot} | — | **BCNF** |
| 16 | GIOHANG | Nghiệp vụ | {MaGio} | — | **BCNF** |
| 17 | DONHANG | Nghiệp vụ | {MaDH}; {SoDH} | — | **BCNF** |
| 18 | DIEUCHINHDON | Nghiệp vụ | {MaDieuChinh} | — | **BCNF** |
| 19 | MAGIAMGIA | Nghiệp vụ | {MaMG}; {Code} | — | **BCNF** |
| 20 | GIUHANG | Nghiệp vụ | {MaGiu} | — | **BCNF** |
| 21 | THANHTOAN | Nghiệp vụ | {MaTT}; {MaGiaoDichNgoai, DonViThanhToan} | — | **BCNF** |
| 22 | KHOANHOAN | Nghiệp vụ | {MaHoan} | — | **BCNF** |
| 23 | PHIEUGIAO | Nghiệp vụ | {MaGiao}; {MaDH} | — | **BCNF** |
| 24 | LANGIAO | Nghiệp vụ | {MaGiao, SoLan} | — | **BCNF** |
| 25 | BANGIAOCOD | Nghiệp vụ | {MaBG} | — | **BCNF** |
| 26 | HOSODOITRA | Nghiệp vụ | {MaHS} | — | **BCNF** |
| 27 | LANNHANLAI | Nghiệp vụ | {MaNhanLai} | — | **BCNF** |
| 28 | PHIEUBAOHANH | Nghiệp vụ | {MaPhieuBH} | MaDH, SoDong → MaSP (vế phải không khóa); MaSeri → MaSP (vế phải không khóa) | **2NF** |
| 29 | PHIEUGUIHANG | Nghiệp vụ | {MaGui} | — | **BCNF** |
| 30 | BIENDONGSODU | Nghiệp vụ | {MaBD} | — | **BCNF** |
| 31 | CHITIETDONHANG | MKH | {MaDH, SoDong} | — | **BCNF** |
| 32 | CHITIETPHIEUNHAP | MKH | {MaPN, SoDong} | — | **BCNF** |
| 33 | CHITIETGIOHANG | MKH | {MaGio, MaSP} | — | **BCNF** |
| 34 | GIATRITHONGSO | MKH | {MaSP, MaTS} | — | **BCNF** |
| 35 | NHANVIEN_VAITRO | MKH | {MaNV, MaVT} | — | **BCNF** |
| 36 | CHITIETKIEMKE | MKH | {MaDot, MaSP} | — | **BCNF** |
| 37 | CHITIETTRA | MKH | {MaHS, SoDong} | MaHS → MaDH (phụ thuộc bộ phận) | **1NF** |
| 38 | CHITIETGUIHANG | MKH | {MaGui, SoDong} | — | **BCNF** |

**Thống kê:** BCNF: 35 quan hệ; 3NF: 1 (HANGCOSERI); 2NF: 1 (PHIEUBAOHANH); 1NF: 1 (CHITIETTRA).

## 8.6. Dạng chuẩn chung của lược đồ

Dạng chuẩn của lược đồ là dạng chuẩn thấp nhất trong các quan hệ:

**DC(lược đồ) = 1NF**, do CHITIETTRA (phụ thuộc bộ phận MaHS → MaDH).

Lược đồ **chưa đạt mức tối thiểu 3NF** mà bài giảng yêu cầu, vì có ba quan hệ chưa đạt BCNF:

| Quan hệ | Dạng chuẩn | Nguyên nhân |
|---|---|---|
| CHITIETTRA | 1NF | MaDH suy ra từ MaHS (một phần của khóa) |
| PHIEUBAOHANH | 2NF | MaSP suy ra từ dòng mua gốc và số seri (bắc cầu) |
| HANGCOSERI | 3NF | MaSP suy ra từ dòng nhập và dòng đơn (vế trái không là siêu khóa) |

**Thang cải tiến.** Nếu sửa lần lượt CHITIETTRA, PHIEUBAOHANH, HANGCOSERI thì lược đồ tăng dần: 1NF → 2NF → 3NF → BCNF. Cả ba lỗi cùng một kiểu: **lưu thêm `MaSP` hoặc `MaDH` dù đã suy ra được qua khóa ngoại**; còn lại 35 quan hệ đạt BCNF.

**Lưu ý về phương án 2 (8.2).** Nếu áp dụng tiêu chí họ tên của bài giảng thì lược đồ chưa đạt cả 1NF cho tới khi tách `HoTen`.

## 8.7. Kết luận thay đổi khi giả thiết thay đổi

Dạng chuẩn phụ thuộc tập PTH. Bảng dưới tính lại khi nhận một giả thiết hoặc một quyết định khác (đã kiểm tra bằng chương trình).

| Kịch bản | Quan hệ | Thay đổi | Kết quả |
|---|---|---|---|
| S1 | HANGCOSERI | Số seri duy nhất toàn cửa hàng (SoSeri → MaSeri thay cho MaSP, SoSeri → MaSeri) | Khóa {MaSeri}, {SoSeri}; MaSP không khóa → **2NF** |
| S2 | MATHANG | Chốt "mọi mặt hàng cùng loại cùng có hoặc không có seri" (MaLoai → CoSeri) | Bắc cầu MaSP → MaLoai → CoSeri → **2NF** |
| S3 | GIAODICHKHO | Chốt mỗi loại biến động chỉ một loại chứng từ (LoaiBienDong → LoaiChungTu) | **2NF** |
| S4 | CHITIETDONHANG, CHITIETPHIEUNHAP | Lưu sẵn thành tiền dòng (SoLuong, DonGiaChot → ThanhTien; tương tự với GiaNhap) | **2NF** mỗi quan hệ |
| S5 | DONHANG | Lưu sẵn tổng phải trả (TienHang, PhiGiao, GiamGia → TongPhaiTra), như DDL | **2NF** |
| S6 | THUONGHIEU, NHACUNGCAP | Chốt tên duy nhất (như DDL) | Thêm khóa {TenTH}, {TenNCC}; vẫn **BCNF** |
| S7 | CHITIETGUIHANG | Có ràng buộc nhất quán: MaPhieuBH → MaSeri, MaSP; MaSeri → MaSP | **2NF** |

Bảng cho thấy mỗi cột tính toán lưu sẵn hoặc mỗi PTH nghiệp vụ thêm vào đều có thể đẩy quan hệ khỏi 3NF; lý do v3 xếp thành tiền, tổng tiền, tồn kho vào dữ liệu tính toán (mục 3.7).

## 8.8. Chuẩn bị cho mục 9

Hướng cải tiến cho ba quan hệ chưa đạt BCNF (chi tiết, chứng minh bảo toàn thông tin và phụ thuộc hàm ở mục 9):

1. **CHITIETTRA:** tách MaDH ra khỏi quan hệ; MaDH đã có ở HOSODOITRA (MaHS → MaDH). Dòng đơn được xác định bằng (HOSODOITRA.MaDH, SoDong).
2. **PHIEUBAOHANH:** bỏ MaSP; mặt hàng suy ra từ CHITIETDONHANG theo (MaDH, SoDong). Phép tách bảo toàn thông tin vì CHITIETDONHANG đã chứa (MaDH, SoDong, MaSP).
3. **HANGCOSERI:** bỏ MaSP; mặt hàng suy ra từ CHITIETPHIEUNHAP theo (MaPN, SoDongNhap). **Điểm cần cân nhắc:** PTH (MaSP, SoSeri) → MaSeri (seri duy nhất trong cùng mặt hàng) sẽ không còn nằm trọn trong một quan hệ, tức phép tách làm mất bảo toàn phụ thuộc. Mục 9 so sánh giữ 3NF (không tách) với tách về BCNF.
4. **4NF:** ANHMATHANG và GIATRITHONGSO được tách vì ảnh và thông số của mặt hàng độc lập (phụ thuộc đa trị, mục 3.8); mục 9 chứng minh.

## 8.9. Câu hỏi giảng viên có thể hỏi

- *Vì sao ANHMATHANG có ba khóa mà vẫn đạt BCNF?* BCNF chỉ yêu cầu vế trái mọi PTH là siêu khóa; ba khóa đều là siêu khóa, và mọi PTH trong G có vế trái là một trong ba khóa.
- *Vì sao HANGCOSERI đạt 3NF nhưng không đạt BCNF?* PTH (MaPN, SoDongNhap) → MaSP có vế trái không là siêu khóa (vi phạm BCNF) nhưng vế phải MaSP là thuộc tính khóa (thuộc khóa {SoSeri, MaSP}), nên 3NF cho phép.
- *Vì sao PHIEUBAOHANH chỉ 2NF?* Khóa một thuộc tính nên đạt 2NF; có phụ thuộc bắc cầu MaPhieuBH → (MaDH, SoDong) → MaSP với MaSP không là thuộc tính khóa nên không đạt 3NF.
- *Vì sao CHITIETTRA chỉ 1NF?* MaHS là một phần của khóa (MaHS, SoDong) và xác định MaDH, là thuộc tính không khóa: phụ thuộc bộ phận, giống ví dụ KetQua trong bài giảng.
- *Dạng chuẩn của cả lược đồ là gì và vì sao?* 1NF, là dạng chuẩn thấp nhất trong 38 quan hệ (CHITIETTRA). Các quan hệ còn lại đạt BCNF, trừ hai quan hệ 2NF và 3NF; sau cải tiến (mục 9) cả lược đồ đạt BCNF.
- *Khóa Id có chứng minh BCNF không?* Không: ở đây kiểm tra theo mọi khóa ứng viên và theo từng PTH; ba quan hệ vi phạm dù đều có mã định danh riêng.
