# MỤC 5. TÌM KHÓA

Căn cứ: phủ tối thiểu G của từng quan hệ ở [04_Phu_toi_thieu.md](04_Phu_toi_thieu.md). Vì G ≡ F nên tập khóa tìm từ G cũng là tập khóa của F. Ưu tiên các quan hệ có nhiều khóa ứng viên (mục 5.4); quan hệ chỉ có một khóa ở mục 5.5; chọn khóa chính ở mục 5.6.

## 5.1. Thuật toán của bài giảng

**Định nghĩa.** *Siêu khóa* của Q là tập thuộc tính K có K⁺ = Q⁺. *Khóa* (khóa ứng viên) là siêu khóa tối thiểu, tức không bỏ được thuộc tính nào mà vẫn là siêu khóa. Một quan hệ có thể có nhiều khóa; khi cài đặt chọn một khóa làm *khóa chính* (PK), ưu tiên ít thuộc tính và đơn giản nhất.

**Phân loại thuộc tính theo G:**

| Tập | Nội dung | Vai trò |
|---|---|---|
| **N (nguồn)** | Thuộc tính chỉ xuất hiện ở vế trái, hoặc không xuất hiện trong PTH nào | Không suy ra được từ thuộc tính khác nên **bắt buộc có trong mọi khóa** |
| **M (trung gian)** | Thuộc tính xuất hiện ở cả hai vế | Có thể thuộc khóa hoặc không; phải xét |
| **D (đích)** | Thuộc tính chỉ xuất hiện ở vế phải | Không giúp suy ra thuộc tính nào, nên **không thuộc khóa nào** |

**Các bước:**

1. Tính N, M, D từ G.
2. Nếu N⁺ = Q⁺ thì N là khóa duy nhất; dừng.
3. Ngược lại, lập bảng gồm mọi tập con Mᵢ của M: Kᵢ = N ∪ Mᵢ rồi tính Kᵢ⁺. Kᵢ⁺ = Q⁺ thì Kᵢ là siêu khóa.
4. Loại các siêu khóa chứa một siêu khóa khác. Phần còn lại là các khóa. Chọn một khóa làm PK.

Vì mọi khóa chứa N và không chứa D nên khóa nằm trong N ∪ M; chỉ cần duyệt 2^|M| tập con (thay vì 2^|Q|).

**Quy ước.** Dùng chữ cái đặt tên như mục 4 (bảng đặt tên nhắc lại ở từng quan hệ). Q⁺ là tập mọi thuộc tính của quan hệ. Ký hiệu tập thuộc tính viết liền, ví dụ BC là {B, C}.

## 5.2. Phân biệt khóa theo phụ thuộc hàm với mã định danh `Id`

Các quan hệ đều có mã định danh nội bộ (`MaSP`, `MaDH`...) nên mã luôn là khóa. Tuy vậy, **khóa tìm bằng thuật toán** có thể có thêm khóa thay thế (SKU, SoDH, cặp UNIQUE). Trình bày cả hai: khóa theo PTH cho thấy các cách định danh bản ghi theo nghiệp vụ; mã nội bộ là khóa được chọn làm PK để các quan hệ khác tham chiếu gọn và không bị đổi khi nghiệp vụ đổi.

## 5.3. Tổng quan kết quả cho các quan hệ có nhiều PTH

| Quan hệ | N | M | D | Số siêu khóa trong N ∪ M | Khóa ứng viên | PK chọn |
|---|---|---|---|---|---|---|
| MATHANG | ∅ | AB | CDEGHIKLM | 3 | {MaSP}; {SKU} | MaSP |
| ANHMATHANG | ∅ | ABCD | EG | 11 | {MaAnh}; {MaSP, ViTri}; {MaSP, DuongDan} | MaAnh |
| DINHNGHIATHONGSO | ∅ | ABC | DEG | 5 | {MaTS}; {MaLoai, TenTS} | MaTS |
| DONHANG | ∅ | AB | CDEGHIKLMNOPQR | 3 | {MaDH}; {SoDH} | MaDH |
| PHIEUNHAP | ∅ | AB | CDEGHI | 3 | {MaPN}; {SoPhieu} | MaPN |
| THANHTOAN | ∅ | AIK | BCDEGHL | 5 | {MaTT}; {MaGiaoDichNgoai, DonViThanhToan} | MaTT |
| MAGIAMGIA | ∅ | AB | CDEGHIKL | 3 | {MaMG}; {Code} | MaMG |
| TAIKHOAN | ∅ | AB | CDEG | 3 | {MaTK}; {DinhDanhDangNhap} | MaTK |
| HANGCOSERI | ∅ | ABCDEGH | IK | 87 | {MaSeri}; {SoSeri, MaSP}; {SoSeri, MaPN, SoDongNhap}; {SoSeri, MaDH, SoDongDon} | MaSeri |
| PHIEUBAOHANH | A | DEG | BCHIKLMNOPQ | 8 | {MaPhieuBH} | MaPhieuBH |
| PHIEUGIAO | ∅ | AB | CDE | 3 | {MaGiao}; {MaDH} | MaGiao |

**Có nhiều khóa ứng viên (ưu tiên):** HANGCOSERI (4 khóa), ANHMATHANG (3), MATHANG, DINHNGHIATHONGSO, DONHANG, PHIEUNHAP, THANHTOAN, MAGIAMGIA, TAIKHOAN, PHIEUGIAO (2). **Một khóa duy nhất:** PHIEUBAOHANH (N⁺ = Q⁺).

## 5.4. Tính chi tiết

### 5.4.1. HANGCOSERI (bốn khóa ứng viên)

**Đặt tên:** A = MaSeri, B = SoSeri, C = MaSP, D = MaPN, E = SoDongNhap, G = MaDH, H = SoDongDon, I = TinhTrang, K = ThoiDiemNhap.

**G (từ mục 4):** A → BDEGHIK; BC → A; DE → C; GH → C.

**Tính N, M, D.**

- A (MaSeri): xuất hiện ở vế trái (A → …) và vế phải (CB → A) → M.
- B (SoSeri): vế phải của A → B, vế trái của CB → A → M.
- C (MaSP): vế trái của CB → A, vế phải của DE → C và GH → C → M.
- D, E (MaPN, SoDongNhap): vế trái của DE → C, vế phải của A → D, A → E → M. Tương tự G, H (MaDH, SoDongDon) → M.
- I, K (TinhTrang, ThoiDiemNhap): chỉ ở vế phải → D (không thuộc khóa nào).
- **N = ∅**, **M = {A, B, C, D, E, G, H}**, **D = {I, K}**.

N⁺ = ∅⁺ = ∅ ≠ Q⁺ nên phải lập bảng tổ hợp. M có 7 thuộc tính nên có 2⁷ = 128 tập con; bảng đầy đủ ở **Phụ lục A**. Có **87 siêu khóa** trong 128 tập con.

**Tìm khóa (lập luận gọn, khớp với bảng).**

1. A⁺ = Q⁺ (A → B, D, E, G, H, I, K; rồi DE → C) → **{A}** là siêu khóa; một thuộc tính nên là khóa.
2. Khóa không chứa A: muốn có A phải nhờ CB → A, nên cần B và C. B chỉ được suy ra từ A, nên **B bắt buộc nằm trong khóa**. C có thể nằm trong khóa hoặc được suy ra: từ DE → C hay GH → C.
3. Các khóa không chứa A:
   - **BC**: (BC)⁺ = {B, C} ∪ {A} (CB → A) ∪ mọi thứ A suy ra = Q⁺. Tối thiểu vì B⁺ = {B}, C⁺ = {C}.
   - **BDE**: (BDE)⁺: DE → C nên có C; CB → A nên có A; từ A có mọi thuộc tính = Q⁺. Tối thiểu vì BD⁺ = {B, D}, BE⁺ = {B, E}, DE⁺ = {D, E, C}, đều ≠ Q⁺.
   - **BGH**: lập luận tương tự BDE qua GH → C.
4. Các siêu khóa khác đều chứa một trong bốn khóa trên.

**Kết luận:** HANGCOSERI có **4 khóa**: {MaSeri}; {SoSeri, MaSP}; {SoSeri, MaPN, SoDongNhap}; {SoSeri, MaDH, SoDongDon}.

**Lưu ý.** Hai khóa sau cùng có nghĩa: một chiếc hàng có seri được xác định bởi (số seri, dòng nhập) hoặc (số seri, dòng đơn). Chúng dựa trên giả thiết HS.f2 (seri duy nhất trong cùng mặt hàng); nếu chốt seri duy nhất toàn cửa hàng thì SoSeri là khóa một thuộc tính và tập khóa thu gọn lại (xem mục 5.7).

### 5.4.2. ANHMATHANG (ba khóa ứng viên)

**Đặt tên:** A = MaAnh, B = MaSP, C = ViTri, D = DuongDan, E = LaAnhChinh, G = MoTaAnh.

**G:** A → BCDEG; BC → A; BD → A.

**N, M, D.** A (vế trái và vế phải của BC → A) → M; B, C, D (vế phải của A → B, A → C, A → D và vế trái của BC → A, BD → A) → M; E, G chỉ ở vế phải → D. **N = ∅, M = {A, B, C, D}, D = {E, G}.**

N⁺ = ∅ ≠ Q⁺ nên lập bảng 2⁴ = 16 dòng:

| STT | Mᵢ | Kᵢ = N ∪ Mᵢ | Kᵢ⁺ | Kết luận |
|---|---|---|---|---|
| 1 | ∅ | ∅ | ∅ | không phải siêu khóa |
| 2 | A | A | ABCDEG = Q⁺ | **Khóa** (siêu khóa tối thiểu) |
| 3 | B | B | B | không phải siêu khóa |
| 4 | C | C | C | không phải siêu khóa |
| 5 | D | D | D | không phải siêu khóa |
| 6 | AB | AB | ABCDEG = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 7 | AC | AC | ABCDEG = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 8 | AD | AD | ABCDEG = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 9 | BC | BC | ABCDEG = Q⁺ | **Khóa** (siêu khóa tối thiểu) |
| 10 | BD | BD | ABCDEG = Q⁺ | **Khóa** (siêu khóa tối thiểu) |
| 11 | CD | CD | CD | không phải siêu khóa |
| 12 | ABC | ABC | ABCDEG = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 13 | ABD | ABD | ABCDEG = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 14 | ACD | ACD | ABCDEG = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 15 | BCD | BCD | ABCDEG = Q⁺ | siêu khóa, không tối thiểu (chứa khóa BD) |
| 16 | ABCD | ABCD | ABCDEG = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |

Có 11 siêu khóa. Siêu khóa tối thiểu: A, BC, BD.

**Kết luận:** 3 khóa: {MaAnh}; {MaSP, ViTri}; {MaSP, DuongDan}. Ý nghĩa: một ảnh được xác định bởi mã ảnh, hoặc bởi mặt hàng cùng vị trí, hoặc bởi mặt hàng cùng đường dẫn.

### 5.4.3. DINHNGHIATHONGSO (hai khóa ứng viên)

**Đặt tên:** A = MaTS, B = MaLoai, C = TenTS, D = KieuGiaTri, E = DonVi, G = BatBuoc. **G:** A → BCDEG; BC → A.

**N, M, D.** A, B, C ở cả hai vế → M; D, E, G chỉ ở vế phải → D. **N = ∅, M = {A, B, C}, D = {D, E, G}.** Bảng 2³ = 8 dòng:

| STT | Mᵢ | Kᵢ = N ∪ Mᵢ | Kᵢ⁺ | Kết luận |
|---|---|---|---|---|
| 1 | ∅ | ∅ | ∅ | không phải siêu khóa |
| 2 | A | A | ABCDEG = Q⁺ | **Khóa** (siêu khóa tối thiểu) |
| 3 | B | B | B | không phải siêu khóa |
| 4 | C | C | C | không phải siêu khóa |
| 5 | AB | AB | ABCDEG = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 6 | AC | AC | ABCDEG = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 7 | BC | BC | ABCDEG = Q⁺ | **Khóa** (siêu khóa tối thiểu) |
| 8 | ABC | ABC | ABCDEG = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |

**Kết luận:** 2 khóa: {MaTS}; {MaLoai, TenTS} (loại hàng, tên thông số).

### 5.4.4. THANHTOAN (hai khóa ứng viên, một khóa có thể trống)

**Đặt tên:** A = MaTT, B = MaDH, C = LoaiKhoan, D = PhuongThuc, E = SoTien, G = ThoiDiem, H = KetQua, I = MaGiaoDichNgoai, K = DonViThanhToan, L = MaNVXacNhan. **G:** A → BCDEGHIKL; IK → A.

**N, M, D.** A, I, K ở cả hai vế (A ở vế phải của KI → A; I, K ở vế phải của A → I, A → K và vế trái của KI → A) → M; B, C, D, E, G, H, L chỉ ở vế phải → D. **N = ∅, M = {A, I, K}, D = {B, C, D, E, G, H, L}.** Bảng 2³ = 8 dòng:

| STT | Mᵢ | Kᵢ = N ∪ Mᵢ | Kᵢ⁺ | Kết luận |
|---|---|---|---|---|
| 1 | ∅ | ∅ | ∅ | không phải siêu khóa |
| 2 | A | A | ABCDEGHIKL = Q⁺ | **Khóa** (siêu khóa tối thiểu) |
| 3 | I | I | I | không phải siêu khóa |
| 4 | K | K | K | không phải siêu khóa |
| 5 | AI | AI | ABCDEGHIKL = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 6 | AK | AK | ABCDEGHIKL = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 7 | IK | IK | ABCDEGHIKL = Q⁺ | **Khóa** (siêu khóa tối thiểu) |
| 8 | AIK | AIK | ABCDEGHIKL = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |

**Kết luận:** 2 khóa: {MaTT}; {MaGiaoDichNgoai, DonViThanhToan} (đơn vị thanh toán, mã giao dịch ngoài).

**Lưu ý NULL.** Khóa {DonViThanhToan, MaGiaoDichNgoai} chỉ định danh được các lần thanh toán có cả hai giá trị (qua ngân hàng, ví, cổng thanh toán); thanh toán tiền mặt tại quầy không có. Vì thế nó không thể làm khóa chính (khóa chính không NULL) và chỉ là khóa thay thế có điều kiện.

### 5.4.5. Các quan hệ "mã định danh cộng một khóa thay thế"

Sáu quan hệ dưới đây đều có G = { A → các thuộc tính còn lại ; B → A } nên **N = ∅, M = {A, B}, D = các thuộc tính còn lại**. Bảng 2² = 4 dòng giống nhau về cấu trúc.

**MATHANG** — A = MaSP, B = SKU, C = TenSP, D = MoTa, E = GiaNiemYet, G = GiaKhuyenMai, H = ThoiHanBaoHanh, I = TinhTrangKinhDoanh, K = CoSeri, L = MaLoai, M = MaTH. Khóa: {MaSP}; {SKU}.

| STT | Mᵢ | Kᵢ = N ∪ Mᵢ | Kᵢ⁺ | Kết luận |
|---|---|---|---|---|
| 1 | ∅ | ∅ | ∅ | không phải siêu khóa |
| 2 | A | A | ABCDEGHIKLM = Q⁺ | **Khóa** (siêu khóa tối thiểu) |
| 3 | B | B | ABCDEGHIKLM = Q⁺ | **Khóa** (siêu khóa tối thiểu) |
| 4 | AB | AB | ABCDEGHIKLM = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |

**DONHANG** — A = MaDH, B = SoDH, C = ThoiDiemLap, D = KenhBan, E = LoaiDon, G = MaKH, H = MaNVBan, I = TenNguoiNhan, K = SDTNhan, L = DiaChiGiao, M = PhiGiao, N = GiamGia, O = MaMG, P = TinhTrang, Q = DieuKienCoc, R = GhiChu. Khóa: {MaDH}; {SoDH}.

| STT | Mᵢ | Kᵢ = N ∪ Mᵢ | Kᵢ⁺ | Kết luận |
|---|---|---|---|---|
| 1 | ∅ | ∅ | ∅ | không phải siêu khóa |
| 2 | A | A | ABCDEGHIKLMNOPQR = Q⁺ | **Khóa** (siêu khóa tối thiểu) |
| 3 | B | B | ABCDEGHIKLMNOPQR = Q⁺ | **Khóa** (siêu khóa tối thiểu) |
| 4 | AB | AB | ABCDEGHIKLMNOPQR = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |

**PHIEUNHAP** — A = MaPN, B = SoPhieu, C = MaNCC, D = MaNV, E = ThoiDiemNhan, G = TinhTrang, H = SoHoaDonNCC, I = GhiChu. Khóa: {MaPN}; {SoPhieu}.

| STT | Mᵢ | Kᵢ = N ∪ Mᵢ | Kᵢ⁺ | Kết luận |
|---|---|---|---|---|
| 1 | ∅ | ∅ | ∅ | không phải siêu khóa |
| 2 | A | A | ABCDEGHI = Q⁺ | **Khóa** (siêu khóa tối thiểu) |
| 3 | B | B | ABCDEGHI = Q⁺ | **Khóa** (siêu khóa tối thiểu) |
| 4 | AB | AB | ABCDEGHI = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |

**MAGIAMGIA** — A = MaMG, B = Code, C = TenChuongTrinh, D = LoaiGiam, E = MucGiam, G = DonToiThieu, H = GiamToiDa, I = NgayBatDau, K = NgayKetThuc, L = GioiHanLuot. Khóa: {MaMG}; {Code}.

| STT | Mᵢ | Kᵢ = N ∪ Mᵢ | Kᵢ⁺ | Kết luận |
|---|---|---|---|---|
| 1 | ∅ | ∅ | ∅ | không phải siêu khóa |
| 2 | A | A | ABCDEGHIKL = Q⁺ | **Khóa** (siêu khóa tối thiểu) |
| 3 | B | B | ABCDEGHIKL = Q⁺ | **Khóa** (siêu khóa tối thiểu) |
| 4 | AB | AB | ABCDEGHIKL = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |

**TAIKHOAN** — A = MaTK, B = DinhDanhDangNhap, C = MaKH, D = TinhTrang, E = NgayDangKy, G = ThoiDiemNoiHoSo. Khóa: {MaTK}; {DinhDanhDangNhap}.

| STT | Mᵢ | Kᵢ = N ∪ Mᵢ | Kᵢ⁺ | Kết luận |
|---|---|---|---|---|
| 1 | ∅ | ∅ | ∅ | không phải siêu khóa |
| 2 | A | A | ABCDEG = Q⁺ | **Khóa** (siêu khóa tối thiểu) |
| 3 | B | B | ABCDEG = Q⁺ | **Khóa** (siêu khóa tối thiểu) |
| 4 | AB | AB | ABCDEG = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |

**PHIEUGIAO** — A = MaGiao, B = MaDH, C = MaNVGiao, D = ThoiDiemXuat, E = TinhTrang. Khóa: {MaGiao}; {MaDH}.

| STT | Mᵢ | Kᵢ = N ∪ Mᵢ | Kᵢ⁺ | Kết luận |
|---|---|---|---|---|
| 1 | ∅ | ∅ | ∅ | không phải siêu khóa |
| 2 | A | A | ABCDE = Q⁺ | **Khóa** (siêu khóa tối thiểu) |
| 3 | B | B | ABCDE = Q⁺ | **Khóa** (siêu khóa tối thiểu) |
| 4 | AB | AB | ABCDE = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |

**Nhận xét chung.** Cả hai khóa đều là một thuộc tính nên là khóa ngay từ dòng Mᵢ = A và Mᵢ = B; dòng AB là siêu khóa không tối thiểu. Hai khóa phản ánh hai cách gọi cùng một bản ghi: mã nội bộ và mã nghiệp vụ (SKU, số đơn, số phiếu, mã giảm giá, định danh đăng nhập; riêng PHIEUGIAO là mã đơn, theo giả thiết mỗi đơn giao một đợt).

### 5.4.6. PHIEUBAOHANH (khóa duy nhất, N⁺ = Q⁺)

**Đặt tên:** A = MaPhieuBH, B = MaKH, C = MaSP, D = MaSeri, E = MaDH, G = SoDong, H = MoTaLoi, I = PhuKienDiKem, K = NgayNhan, L = NgayHenTra, M = NgayTraThucTe, N = TinhTrang, O = KetQua, P = LyDoTuChoi, Q = MaNVTiepNhan. **G:** A → BDEGHIKLMNOPQ; EG → C; D → C.

**N, M, D.** A (MaPhieuBH) chỉ ở vế trái → **N = {A}**. D, E, G ở cả hai vế (D, E, G là vế phải của A → D, A → E, A → G và vế trái của D → C, EG → C) → M. Các thuộc tính còn lại chỉ ở vế phải → D.

**Tính N⁺.** A⁺ ⊇ {B, D, E, G, H, I, K, L, M, N, O, P, Q} (nhờ A → …); vì D, E, G ∈ A⁺ nên D → C (và EG → C) cho C. Vậy **A⁺ = Q⁺**.

Theo thuật toán, N⁺ = Q⁺ nên **N = {A} là khóa duy nhất**, không cần bảng tổ hợp. Hai thuộc tính MaSeri (D) và cặp (MaDH, SoDong) = (E, G) **không phải khóa**: D⁺ = {D, C}, (EG)⁺ = {E, G, C}; mỗi chiếc hàng hoặc mỗi dòng đơn có thể có nhiều phiếu bảo hành theo thời gian.

**Kết luận:** khóa duy nhất {MaPhieuBH}.

## 5.5. Quan hệ chỉ có một khóa

Với các quan hệ chỉ có một PTH `X → Y…` (mục 4.4), mọi thuộc tính của X chỉ ở vế trái nên **N = X**; N⁺ = Q⁺ nên N là khóa duy nhất. Không cần bảng tổ hợp.

| Quan hệ | N = khóa duy nhất |
|---|---|
| LOAIHANG | MaLoai |
| THUONGHIEU | MaTH |
| VAITRO | MaVT |
| KHACHHANG | MaKH |
| DIACHINHANHANG | MaDC |
| NHANVIEN | MaNV |
| NHACUNGCAP | MaNCC |
| GIAODICHKHO | MaGDK |
| GIUHANG | MaGiu |
| GIOHANG | MaGio |
| DOTKIEMKE | MaDot |
| DIEUCHINHDON | MaDieuChinh |
| KHOANHOAN | MaHoan |
| BANGIAOCOD | MaBG |
| HOSODOITRA | MaHS |
| LANNHANLAI | MaNhanLai |
| PHIEUGUIHANG | MaGui |
| BIENDONGSODU | MaBD |
| CHITIETPHIEUNHAP | MaPN, SoDong |
| CHITIETDONHANG | MaDH, SoDong |
| GIATRITHONGSO | MaSP, MaTS |
| CHITIETGIOHANG | MaGio, MaSP |
| LANGIAO | MaGiao, SoLan |
| CHITIETKIEMKE | MaDot, MaSP |
| CHITIETGUIHANG | MaGui, SoDong |
| CHITIETTRA | MaHS, SoDong (xem ghi chú dưới) |
| NHANVIEN_VAITRO | MaNV, MaVT (không có PTH nào: mọi thuộc tính đều thuộc N) |

Với khóa ghép, hai điều cần chú ý:

- **CHITIETDONHANG**: (MaDH, MaSP) **không phải khóa**, vì v3 cho phép một mặt hàng ở nhiều dòng của một đơn; khóa là (MaDH, SoDong). Tương tự CHITIETPHIEUNHAP: khóa là (MaPN, SoDong).
- **CHITIETGIOHANG**: khóa là (MaGio, MaSP), vì v3 quy định mỗi mặt hàng một dòng trong giỏ.
- **CHITIETTRA**: theo phủ tối thiểu ở mục 4 (4.3.7), G = { AC → D, AC → E, A → B } với A = MaHS, B = MaDH, C = SoDong. N = {A, C} (chỉ ở vế trái), N⁺ = {A, C, B, D, E} = Q⁺ nên **khóa duy nhất là (MaHS, SoDong)**; MaDH là thuộc tính đích (suy ra từ MaHS).

## 5.6. Chọn khóa chính

**Nguyên tắc** (bài giảng): ưu tiên ít thuộc tính nhất, đơn giản; thêm các tiêu chí: **không NULL**, **ổn định** (không đổi theo thời gian), **không mang ý nghĩa thương mại dễ thay đổi**.

| Quan hệ | Khóa ứng viên | PK chọn | Lý do | Khóa thay thế (UNIQUE) |
|---|---|---|---|---|
| MATHANG | MaSP; SKU | MaSP | SKU có thể đổi khi hãng đổi mã hàng; mã nội bộ ổn định | SKU (DDL đã có UNIQUE) |
| ANHMATHANG | MaAnh; (MaSP, ViTri); (MaSP, DuongDan) | MaAnh | Một thuộc tính; vị trí và đường dẫn có thể đổi | (MaSP, DuongDan) có UNIQUE trong DDL; (MaSP, ViTri) cần thêm |
| DINHNGHIATHONGSO | MaTS; (MaLoai, TenTS) | MaTS | Một thuộc tính; tên thông số có thể sửa | (MaLoai, TenTS), DDL đã có UNIQUE |
| DONHANG | MaDH; SoDH | MaDH | Số đơn hiển thị cho khách, định dạng có thể đổi | SoDH, DDL đã có UNIQUE |
| PHIEUNHAP | MaPN; SoPhieu | MaPN | Như trên | SoPhieu, DDL đã có UNIQUE |
| THANHTOAN | MaTT; (DonViThanhToan, MaGiaoDichNgoai) | MaTT | Khóa còn lại có thể NULL | UNIQUE có điều kiện (cả hai khác NULL); DDL chưa có |
| MAGIAMGIA | MaMG; Code | MaMG | Mã khuyến mãi có thể đổi giữa các đợt | Code, DDL đã có UNIQUE |
| TAIKHOAN | MaTK; DinhDanhDangNhap | MaTK | Định danh đăng nhập (số điện thoại, email) có thể đổi | DinhDanhDangNhap |
| PHIEUGIAO | MaGiao; MaDH **[GT]** | MaGiao | MaDH → MaGiao chỉ đúng khi mỗi đơn giao một đợt | MaDH nếu chốt giả thiết |
| HANGCOSERI | MaSeri; (MaSP, SoSeri); (SoSeri, MaPN, SoDongNhap); (SoSeri, MaDH, SoDongDon) | MaSeri | Một thuộc tính; ba khóa còn lại ghép nhiều thuộc tính, một khóa phụ thuộc giả thiết | (MaSP, SoSeri) |
| PHIEUBAOHANH | MaPhieuBH | MaPhieuBH | Khóa duy nhất | không |
| Các quan hệ ở 5.5 | như bảng 5.5 | khóa duy nhất | | |

**Khóa mã nội bộ trong DDL.** DDL hiện tại dùng cột `Id` làm PK cho mọi bảng, kể cả bảng dòng chi tiết (`OrderItems`, `PurchaseReceiptItems`). Với CHITIETDONHANG và CHITIETPHIEUNHAP, khóa tự nhiên theo PTH là (MaDH, SoDong) và (MaPN, SoDong); quyết định dùng khóa tự nhiên hay thêm `Id` để làm PK được để lại ở mục 7 (chuyển ERD sang mô hình quan hệ), nhưng không làm đổi tập khóa ứng viên ở đây.

## 5.7. Kiểm tra bằng cách khác

Ngoài bảng tổ hợp trên N ∪ M, tập khóa đã được kiểm tra bằng **duyệt toàn bộ tập con của Q** (không dùng N, M, D): chương trình lấy mọi tập con theo kích thước tăng dần, giữ các tập có bao đóng bằng Q⁺ và không chứa tập đã chọn. Kết quả trùng với bảng cho cả 11 quan hệ ([tools/timkhoa.py](tools/timkhoa.py)). Lời giải trong báo cáo vẫn trình bày tay từng bước.

**Thử nghiệm giả thiết HS.f2.** Nếu chốt số seri duy nhất toàn cửa hàng, PTH `CB → A` (MaSP, SoSeri → MaSeri) được thay bằng `B → A` (SoSeri → MaSeri). Khi đó B⁺ = Q⁺ nên B là khóa; các tập BC, BDE, BGH chứa B nên không còn tối thiểu, và HANGCOSERI chỉ còn hai khóa {MaSeri} và {SoSeri}. Tập khóa phụ thuộc trực tiếp vào giả thiết nghiệp vụ.

## 5.8. Hệ quả cho mục 8 (dạng chuẩn) và câu hỏi giảng viên có thể hỏi

**Hệ quả.**

- Dạng chuẩn xét theo **mọi khóa ứng viên**, không chỉ PK. Ví dụ ANHMATHANG có khóa ghép (MaSP, ViTri): mọi thuộc tính không khóa phụ thuộc đầy đủ vào khóa nên vẫn đạt 2NF.
- Thuộc tính **khóa** (có trong ít nhất một khóa) và **không khóa** quyết định 3NF. Ở HANGCOSERI, MaSP (C) là thuộc tính khóa vì thuộc khóa {MaSP, SoSeri}, nên PTH DE → C **không vi phạm 3NF** (vế phải là thuộc tính khóa) nhưng **vi phạm BCNF** (vế trái DE không là siêu khóa). Ở PHIEUBAOHANH, MaSP không thuộc khóa nào nên EG → C và D → C vi phạm cả 3NF.
- Nếu chốt số seri duy nhất toàn cửa hàng (mục 5.7) thì MaSP không còn thuộc khóa nào, và HANGCOSERI vi phạm cả 3NF. Vì vậy, kết luận về HANGCOSERI ở mục 3 và mục 4 cần đọc là "không đạt BCNF"; mục 8 sẽ kết luận dạng chuẩn sau khi chốt giả thiết HS.f2.

**Câu hỏi có thể gặp.**

- *Vì sao D không thuộc khóa nào?* D chỉ ở vế phải nên không giúp suy ra thuộc tính nào; bỏ nó khỏi một siêu khóa thì vẫn là siêu khóa.
- *Vì sao N phải thuộc mọi khóa?* Thuộc tính của N không được suy ra từ thuộc tính nào khác, nên nếu thiếu nó thì không bao giờ có trong bao đóng.
- *Nhiều khóa thì chọn thế nào?* Theo nguyên tắc ở 5.6; các khóa còn lại giữ làm khóa thay thế bằng ràng buộc UNIQUE.
- *Một quan hệ có thể không có khóa không?* Không: Q⁺ luôn là siêu khóa nên luôn có ít nhất một khóa.


## Phụ lục A. Bảng tổ hợp đầy đủ của HANGCOSERI (128 dòng)

Đặt tên: A = MaSeri, B = SoSeri, C = MaSP, D = MaPN, E = SoDongNhap, G = MaDH, H = SoDongDon, I = TinhTrang, K = ThoiDiemNhap. N = ∅, M = {A, B, C, D, E, G, H}. Mᵢ sắp theo kích thước, rồi theo thứ tự chữ cái.

| STT | Mᵢ | Kᵢ = N ∪ Mᵢ | Kᵢ⁺ | Kết luận |
|---|---|---|---|---|
| 1 | ∅ | ∅ | ∅ | không phải siêu khóa |
| 2 | A | A | ABCDEGHIK = Q⁺ | **Khóa** (siêu khóa tối thiểu) |
| 3 | B | B | B | không phải siêu khóa |
| 4 | C | C | C | không phải siêu khóa |
| 5 | D | D | D | không phải siêu khóa |
| 6 | E | E | E | không phải siêu khóa |
| 7 | G | G | G | không phải siêu khóa |
| 8 | H | H | H | không phải siêu khóa |
| 9 | AB | AB | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 10 | AC | AC | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 11 | AD | AD | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 12 | AE | AE | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 13 | AG | AG | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 14 | AH | AH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 15 | BC | BC | ABCDEGHIK = Q⁺ | **Khóa** (siêu khóa tối thiểu) |
| 16 | BD | BD | BD | không phải siêu khóa |
| 17 | BE | BE | BE | không phải siêu khóa |
| 18 | BG | BG | BG | không phải siêu khóa |
| 19 | BH | BH | BH | không phải siêu khóa |
| 20 | CD | CD | CD | không phải siêu khóa |
| 21 | CE | CE | CE | không phải siêu khóa |
| 22 | CG | CG | CG | không phải siêu khóa |
| 23 | CH | CH | CH | không phải siêu khóa |
| 24 | DE | DE | CDE | không phải siêu khóa |
| 25 | DG | DG | DG | không phải siêu khóa |
| 26 | DH | DH | DH | không phải siêu khóa |
| 27 | EG | EG | EG | không phải siêu khóa |
| 28 | EH | EH | EH | không phải siêu khóa |
| 29 | GH | GH | CGH | không phải siêu khóa |
| 30 | ABC | ABC | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 31 | ABD | ABD | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 32 | ABE | ABE | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 33 | ABG | ABG | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 34 | ABH | ABH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 35 | ACD | ACD | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 36 | ACE | ACE | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 37 | ACG | ACG | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 38 | ACH | ACH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 39 | ADE | ADE | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 40 | ADG | ADG | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 41 | ADH | ADH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 42 | AEG | AEG | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 43 | AEH | AEH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 44 | AGH | AGH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 45 | BCD | BCD | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa BC) |
| 46 | BCE | BCE | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa BC) |
| 47 | BCG | BCG | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa BC) |
| 48 | BCH | BCH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa BC) |
| 49 | BDE | BDE | ABCDEGHIK = Q⁺ | **Khóa** (siêu khóa tối thiểu) |
| 50 | BDG | BDG | BDG | không phải siêu khóa |
| 51 | BDH | BDH | BDH | không phải siêu khóa |
| 52 | BEG | BEG | BEG | không phải siêu khóa |
| 53 | BEH | BEH | BEH | không phải siêu khóa |
| 54 | BGH | BGH | ABCDEGHIK = Q⁺ | **Khóa** (siêu khóa tối thiểu) |
| 55 | CDE | CDE | CDE | không phải siêu khóa |
| 56 | CDG | CDG | CDG | không phải siêu khóa |
| 57 | CDH | CDH | CDH | không phải siêu khóa |
| 58 | CEG | CEG | CEG | không phải siêu khóa |
| 59 | CEH | CEH | CEH | không phải siêu khóa |
| 60 | CGH | CGH | CGH | không phải siêu khóa |
| 61 | DEG | DEG | CDEG | không phải siêu khóa |
| 62 | DEH | DEH | CDEH | không phải siêu khóa |
| 63 | DGH | DGH | CDGH | không phải siêu khóa |
| 64 | EGH | EGH | CEGH | không phải siêu khóa |
| 65 | ABCD | ABCD | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 66 | ABCE | ABCE | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 67 | ABCG | ABCG | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 68 | ABCH | ABCH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 69 | ABDE | ABDE | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 70 | ABDG | ABDG | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 71 | ABDH | ABDH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 72 | ABEG | ABEG | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 73 | ABEH | ABEH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 74 | ABGH | ABGH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 75 | ACDE | ACDE | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 76 | ACDG | ACDG | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 77 | ACDH | ACDH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 78 | ACEG | ACEG | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 79 | ACEH | ACEH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 80 | ACGH | ACGH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 81 | ADEG | ADEG | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 82 | ADEH | ADEH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 83 | ADGH | ADGH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 84 | AEGH | AEGH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 85 | BCDE | BCDE | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa BC) |
| 86 | BCDG | BCDG | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa BC) |
| 87 | BCDH | BCDH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa BC) |
| 88 | BCEG | BCEG | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa BC) |
| 89 | BCEH | BCEH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa BC) |
| 90 | BCGH | BCGH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa BC) |
| 91 | BDEG | BDEG | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa BDE) |
| 92 | BDEH | BDEH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa BDE) |
| 93 | BDGH | BDGH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa BGH) |
| 94 | BEGH | BEGH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa BGH) |
| 95 | CDEG | CDEG | CDEG | không phải siêu khóa |
| 96 | CDEH | CDEH | CDEH | không phải siêu khóa |
| 97 | CDGH | CDGH | CDGH | không phải siêu khóa |
| 98 | CEGH | CEGH | CEGH | không phải siêu khóa |
| 99 | DEGH | DEGH | CDEGH | không phải siêu khóa |
| 100 | ABCDE | ABCDE | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 101 | ABCDG | ABCDG | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 102 | ABCDH | ABCDH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 103 | ABCEG | ABCEG | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 104 | ABCEH | ABCEH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 105 | ABCGH | ABCGH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 106 | ABDEG | ABDEG | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 107 | ABDEH | ABDEH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 108 | ABDGH | ABDGH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 109 | ABEGH | ABEGH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 110 | ACDEG | ACDEG | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 111 | ACDEH | ACDEH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 112 | ACDGH | ACDGH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 113 | ACEGH | ACEGH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 114 | ADEGH | ADEGH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 115 | BCDEG | BCDEG | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa BC) |
| 116 | BCDEH | BCDEH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa BC) |
| 117 | BCDGH | BCDGH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa BC) |
| 118 | BCEGH | BCEGH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa BC) |
| 119 | BDEGH | BDEGH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa BGH) |
| 120 | CDEGH | CDEGH | CDEGH | không phải siêu khóa |
| 121 | ABCDEG | ABCDEG | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 122 | ABCDEH | ABCDEH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 123 | ABCDGH | ABCDGH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 124 | ABCEGH | ABCEGH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 125 | ABDEGH | ABDEGH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 126 | ACDEGH | ACDEGH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
| 127 | BCDEGH | BCDEGH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa BC) |
| 128 | ABCDEGH | ABCDEGH | ABCDEGHIK = Q⁺ | siêu khóa, không tối thiểu (chứa khóa A) |
