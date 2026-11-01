# MỤC 4. TÌM PHỦ TỐI THIỂU

Căn cứ: tập phụ thuộc hàm F của từng quan hệ trong [03_Phu_thuoc_ham.md](03_Phu_thuoc_ham.md). Ưu tiên các quan hệ có F nhiều hơn một PTH (mục 4.3); quan hệ chỉ có PTH của khóa tổng hợp ở mục 4.4.

## 4.1. Phương pháp

**Phủ tối thiểu (minimal cover)** của F là tập G tương đương F (F⁺ = G⁺) thỏa ba điều kiện: vế phải của mọi PTH chỉ có một thuộc tính; không PTH nào có thuộc tính thừa ở vế trái; không PTH nào dư thừa trong G.

**Ba bước:**

| Bước | Việc làm |
|---|---|
| **B1** | Tách vế phải: X → A₁A₂… thành X → A₁, X → A₂, … |
| **B2** | Loại thuộc tính thừa ở vế trái: với X → A, \|X\| ≥ 2, thử bỏ B ∈ X; nếu A ∈ (X − B)⁺ (tính theo F hiện tại) thì B thừa, thay bằng (X − B) → A |
| **B3** | Loại PTH dư thừa: với mỗi f: X → A, nếu A ∈ X⁺ theo (F − {f}) thì bỏ f |

**Quy ước.** Thứ tự xét là thứ tự liệt kê ở B1 (từ trên xuống), mỗi lần bỏ một PTH thì các lần xét sau dùng tập đã bỏ. Thứ tự xét khác có thể cho phủ khác; ở các quan hệ dưới đây tôi đã thử nhiều thứ tự ngẫu nhiên và chỉ ra **một phủ duy nhất**. Để tính gọn, mỗi quan hệ dùng chữ cái thay tên thuộc tính (bỏ F và J để không lẫn với tập F); có bảng đặt tên. Dấu "→" viết liền các thuộc tính ở vế trái, ví dụ `CB → A` là {C, B} → A.

**Kiểm tra tương đương.** Với G thu được, G ⊆ F sau B1 là hiển nhiên; ta chứng minh mỗi PTH bị loại suy ra được từ G (bằng bao đóng), nên G ≡ F.

**Đối chiếu bằng chương trình.** Kết quả tay đã được đối chiếu bằng một chương trình nhỏ tính bao đóng và kiểm tra F ≡ G ([tools/mincover.py](tools/mincover.py)). Lời giải trong báo cáo vẫn trình bày tay từng bước.

## 4.2. Phạm vi

- **Mười hai quan hệ có F nhiều hơn một PTH** (mã định danh cộng khóa thay thế hoặc quy tắc bắc cầu): MATHANG, ANHMATHANG, DINHNGHIATHONGSO, DONHANG, PHIEUNHAP, THANHTOAN, MAGIAMGIA, TAIKHOAN, HANGCOSERI, PHIEUBAOHANH, PHIEUGIAO, CHITIETTRA. Tính chi tiết ở 4.3.
- **Hai mươi lăm quan hệ chỉ có một PTH** (khóa → tất cả): tóm tắt ở 4.4.
- NHANVIEN_VAITRO là quan hệ toàn khóa, không có PTH không tầm thường, nên không có gì để rút gọn.

Hai quan hệ **có PTH dư thừa thật sự** là HANGCOSERI và PHIEUBAOHANH (mục 4.3.1, 4.3.2); quan hệ **có thuộc tính thừa ở vế trái** là CHITIETTRA (mục 4.3.7). Chúng sẽ là tình huống cho phần cải tiến.

## 4.3. Quan hệ có F nhiều hơn một PTH

### 4.3.1. HANGCOSERI (có một PTH dư thừa)

**Đặt tên:** A = MaSeri, B = SoSeri, C = MaSP, D = MaPN, E = SoDongNhap, G = MaDH, H = SoDongDon, I = TinhTrang, K = ThoiDiemNhap.

**F gốc** (theo 03, mục 3.5):

- f1: A → BCDEGHIK
- f2: CB → A  (mỗi mặt hàng, mỗi số seri đúng một chiếc; **[GT]**)
- f3: DE → C  (dòng nhập xác định mặt hàng)
- f4: GH → C  (dòng đơn xác định mặt hàng)

**B1. Tách vế phải** (11 PTH):

| # | PTH | # | PTH | # | PTH |
|---|---|---|---|---|---|
| 1 | A → B | 5 | A → G | 9 | CB → A |
| 2 | A → C | 6 | A → H | 10 | DE → C |
| 3 | A → D | 7 | A → I | 11 | GH → C |
| 4 | A → E | 8 | A → K | | |

**B2. Thuộc tính thừa ở vế trái** (chỉ xét PTH có vế trái ≥ 2 thuộc tính):

| PTH | Thử bỏ | Bao đóng | Kết luận |
|---|---|---|---|
| CB → A | bỏ C | B⁺ = {B}, không chứa A | C không thừa |
| | bỏ B | C⁺ = {C}, không chứa A | B không thừa |
| DE → C | bỏ D | E⁺ = {E}, không chứa C | D không thừa |
| | bỏ E | D⁺ = {D}, không chứa C | E không thừa |
| GH → C | bỏ G, bỏ H | H⁺ = {H}, G⁺ = {G}, đều không chứa C | Không thừa |

Không có thuộc tính thừa; sau B2 vẫn 11 PTH.

**B3. PTH dư thừa** (xét lần lượt từ #1):

| PTH xét | Tập còn lại | Bao đóng của vế trái | Kết luận |
|---|---|---|---|
| #1 A → B | bỏ #1 | A⁺ = {A, C, D, E, G, H, I, K}, không có B | Cần giữ |
| **#2 A → C** | bỏ #2 | A⁺ ⊇ {A, B, D, E, G, H, I, K}; vì D, E ∈ A⁺ nên theo #10 (DE → C) có C | **Dư thừa, loại** |
| #3 A → D | bỏ #3 | A⁺ = {A, B, E, G, H, I, K, C (theo #11)}, không có D | Cần giữ |
| #4 A → E | bỏ #4 | A⁺ = {A, B, D, G, H, I, K, C (theo #11)}, không có E | Cần giữ |
| #5 A → G | bỏ #5 | A⁺ = {A, B, D, E, H, I, K, C (theo #10)}, không có G | Cần giữ |
| #6 A → H | bỏ #6 | A⁺ không có H | Cần giữ |
| #7 A → I | bỏ #7 | A⁺ không có I | Cần giữ |
| #8 A → K | bỏ #8 | A⁺ không có K | Cần giữ |
| #9 CB → A | bỏ #9 | (CB)⁺ = {C, B}, không có A | Cần giữ |
| #10 DE → C | bỏ #10 | (DE)⁺ = {D, E}, không có C | Cần giữ |
| #11 GH → C | bỏ #11 | (GH)⁺ = {G, H}, không có C | Cần giữ |

**Phủ tối thiểu G (10 PTH):**

G_HANGCOSERI = { A → B, A → D, A → E, A → G, A → H, A → I, A → K, CB → A, DE → C, GH → C }

**Tương đương:** A → C suy ra từ G: A⁺_G ∋ D, E (nhờ A → D, A → E), mà DE → C nên C ∈ A⁺_G. Vậy F ≡ G.

**Ý nghĩa.** MaSP (C) có thể suy ra từ dòng nhập (DE) hoặc dòng đơn (GH) nên A → C dư thừa: lưu MaSP trong HANGCOSERI là lưu thừa. Chuỗi A → DE → C là phụ thuộc có vế trái DE không phải siêu khóa, nên HANGCOSERI không đạt BCNF; việc có đạt 3NF hay không còn tùy MaSP có thuộc khóa nào không, xem mục 5.8 và mục 8.

### 4.3.2. PHIEUBAOHANH (có một PTH dư thừa)

**Đặt tên:** A = MaPhieuBH, B = MaKH, C = MaSP, D = MaSeri, E = MaDH, G = SoDong, H = MoTaLoi, I = PhuKienDiKem, K = NgayNhan, L = NgayHenTra, M = NgayTraThucTe, N = TinhTrang, O = KetQua, P = LyDoTuChoi, Q = MaNVTiepNhan.

**F gốc:**

- f1: A → BCDEGHIKLMNOPQ
- f2: EG → C  (dòng mua gốc xác định mặt hàng)
- f3: D → C  (số seri xác định mặt hàng)

**B1.** f1 tách thành 14 PTH A → B, A → C, A → D, A → E, A → G, A → H, A → I, A → K, A → L, A → M, A → N, A → O, A → P, A → Q; thêm EG → C và D → C. Tổng 16 PTH, đánh số lần lượt #1 đến #16 với A → C là #2.

**B2.** EG → C: bỏ E được G⁺ = {G}, bỏ G được E⁺ = {E}, đều không chứa C → không thừa. Các PTH còn lại có vế trái một thuộc tính.

**B3.**

| PTH xét | Bao đóng khi bỏ PTH đó | Kết luận |
|---|---|---|
| **A → C** | A⁺ chứa D (theo A → D) nên có C (theo D → C); cũng có E, G nên có C theo EG → C | **Dư thừa, loại** |
| A → X với X ∈ {B, D, E, G, H, I, K, L, M, N, O, P, Q} | X chỉ xuất hiện ở vế phải của chính A → X, nên khi bỏ nó X ∉ A⁺ | Cần giữ cả 13 PTH |
| D → C | D⁺ = {D} | Cần giữ |
| EG → C | (EG)⁺ = {E, G} | Cần giữ |

**Phủ tối thiểu G (15 PTH):**

G_PHIEUBAOHANH = { A → B, A → D, A → E, A → G, A → H, A → I, A → K, A → L, A → M, A → N, A → O, A → P, A → Q, EG → C, D → C }

**Tương đương:** A → C suy ra từ G vì A → D, D → C. Vậy F ≡ G.

**Ý nghĩa và lưu ý.** Cũng như HANGCOSERI, MaSP suy ra được từ dòng mua gốc hoặc số seri; phiếu lưu thừa MaSP. MaSeri (D) có thể trống với hàng không có seri; khi đó PTH D → C chỉ áp dụng cho những dòng có seri.

### 4.3.3. ANHMATHANG (ba khóa ứng viên, không có PTH dư thừa)

**Đặt tên:** A = MaAnh, B = MaSP, C = ViTri, D = DuongDan, E = LaAnhChinh, G = MoTaAnh.

**F gốc:** f1: A → BCDEG; f2: BC → A; f3: BD → A.

**B1** (7 PTH): A → B, A → C, A → D, A → E, A → G, BC → A, BD → A.

**B2:**

| PTH | Thử bỏ | Bao đóng | Kết luận |
|---|---|---|---|
| BC → A | bỏ B | C⁺ = {C}, không có A | B không thừa |
| | bỏ C | B⁺ = {B}, không có A | C không thừa |
| BD → A | bỏ B | D⁺ = {D}, không có A | B không thừa |
| | bỏ D | B⁺ = {B}, không có A | D không thừa |

**B3:**

| PTH xét | Bao đóng khi bỏ PTH đó | Kết luận |
|---|---|---|
| A → B | A⁺ = {A, C, D, E, G}; BC → A và BD → A đều cần B | Giữ |
| A → C | A⁺ = {A, B, D, E, G}; BD → A chỉ cho A, không có C | Giữ |
| A → D | A⁺ = {A, B, C, E, G}; không có D | Giữ |
| A → E, A → G | E, G chỉ ở vế phải của chính nó | Giữ |
| BC → A | (BC)⁺ = {B, C} | Giữ |
| BD → A | (BD)⁺ = {B, D} | Giữ |

**Phủ tối thiểu G (7 PTH):** G_ANHMATHANG = { A → B, A → C, A → D, A → E, A → G, BC → A, BD → A } (trùng B1).

**Nhận xét.** Quan hệ có ba khóa ứng viên là {A}, {B, C}, {B, D}. Mỗi khóa ghép vừa suy ra A vừa được suy ra từ A, nhưng không PTH nào dư thừa vì A không được suy ra bởi các PTH còn lại khi bỏ chính nó. Phủ giống hệt tập sau khi tách vế phải.

### 4.3.4. MATHANG (hai khóa ứng viên A và B)

**Đặt tên:** A = MaSP, B = SKU, C = TenSP, D = MoTa, E = GiaNiemYet, G = GiaKhuyenMai, H = ThoiHanBaoHanh, I = TinhTrangKinhDoanh, K = CoSeri, L = MaLoai, M = MaTH.

**F gốc:** f1: A → BCDEGHIKLM; f2: B → A.

**B1** (11 PTH): A → B, A → C, A → D, A → E, A → G, A → H, A → I, A → K, A → L, A → M, B → A.

**B2:** mọi vế trái một thuộc tính, không có thuộc tính thừa.

**B3:**

| PTH xét | Bao đóng khi bỏ PTH đó | Kết luận |
|---|---|---|
| A → B | A⁺ = {A, C, D, E, G, H, I, K, L, M}; B→A không dùng được vì B ∉ A⁺ | Giữ |
| A → X với X ∈ {C, D, E, G, H, I, K, L, M} | X chỉ sinh ra từ chính A → X | Giữ cả 9 PTH |
| B → A | B⁺ = {B} | Giữ |

**Phủ tối thiểu G (11 PTH):** G_MATHANG = { A → B, A → C, A → D, A → E, A → G, A → H, A → I, A → K, A → L, A → M, B → A }.

**Nhận xét.** A → B và B → A tạo một vòng nhưng cả hai đều cần: A → B cho ra B, B → A cho ra A từ B. Đây là minh họa rằng PK nội bộ và khóa thương mại đều là khóa ứng viên (sẽ làm rõ ở mục 5).

### 4.3.5. DINHNGHIATHONGSO

**Đặt tên:** A = MaTS, B = MaLoai, C = TenTS, D = KieuGiaTri, E = DonVi, G = BatBuoc.

**F gốc:** f1: A → BCDEG; f2: BC → A.

**B1** (6 PTH): A → B, A → C, A → D, A → E, A → G, BC → A.

**B2:** BC → A: bỏ B còn C⁺ = {C}; bỏ C còn B⁺ = {B}; đều không chứa A → không thừa.

**B3:** A → B (bỏ đi: A⁺ = {A, C, D, E, G}, BC → A cần B → không suy ra được B) giữ; A → C (bỏ đi: A⁺ = {A, B, D, E, G}, không có C) giữ; A → D, A → E, A → G (chỉ ở vế phải của chính nó) giữ; BC → A ((BC)⁺ = {B, C}) giữ.

**Phủ tối thiểu G (6 PTH):** G_DNTS = { A → B, A → C, A → D, A → E, A → G, BC → A }.

### 4.3.6. Nhóm "mã định danh cộng một khóa thay thế"

Sáu quan hệ có cùng khuôn: **A → (các thuộc tính còn lại)** và **một khóa thay thế → A** (đơn thuộc tính, trừ THANHTOAN có khóa ghép). Cách làm giống nhau nên trình bày chung.

| Quan hệ | Đặt tên | F gốc | B1 | Khóa thay thế |
|---|---|---|---|---|
| DONHANG | A = MaDH, B = SoDH, C = ThoiDiemLap, D = KenhBan, E = LoaiDon, G = MaKH, H = MaNVBan, I = TenNguoiNhan, K = SDTNhan, L = DiaChiGiao, M = PhiGiao, N = GiamGia, O = MaMG, P = TinhTrang, Q = DieuKienCoc, R = GhiChu | A → BCDEGHIKLMNOPQR; B → A | 16 PTH | B (SoDH) |
| PHIEUNHAP | A = MaPN, B = SoPhieu, C = MaNCC, D = MaNV, E = ThoiDiemNhan, G = TinhTrang, H = SoHoaDonNCC, I = GhiChu | A → BCDEGHI; B → A | 8 PTH | B (SoPhieu) |
| MAGIAMGIA | A = MaMG, B = Code, C = TenChuongTrinh, D = LoaiGiam, E = MucGiam, G = DonToiThieu, H = GiamToiDa, I = NgayBatDau, K = NgayKetThuc, L = GioiHanLuot | A → BCDEGHIKL; B → A | 10 PTH | B (Code) |
| TAIKHOAN | A = MaTK, B = DinhDanhDangNhap, C = MaKH, D = TinhTrang, E = NgayDangKy, G = ThoiDiemNoiHoSo | A → BCDEG; B → A | 6 PTH | B (DinhDanhDangNhap) |
| PHIEUGIAO | A = MaGiao, B = MaDH, C = MaNVGiao, D = ThoiDiemXuat, E = TinhTrang | A → BCDE; B → A (**[GT]**: mỗi đơn giao trọn trong một đợt) | 5 PTH | B (MaDH) |
| THANHTOAN | A = MaTT, B = MaDH, C = LoaiKhoan, D = PhuongThuc, E = SoTien, G = ThoiDiem, H = KetQua, I = MaGiaoDichNgoai, K = DonViThanhToan, L = MaNVXacNhan | A → BCDEGHIKL; **KI → A** | 10 PTH | KI (DonViThanhToan, MaGiaoDichNgoai) |

**B2.** Mọi PTH có vế trái là một thuộc tính (A hoặc B), nên không có gì để xét, **trừ THANHTOAN** có KI → A. Bỏ K còn I⁺ = {I}; bỏ I còn K⁺ = {K}; đều không chứa A nên K, I đều không thừa.

**B3 (lập luận chung).**

- Với mỗi PTH A → X trong đó X ≠ khóa thay thế: X chỉ xuất hiện ở vế phải của chính A → X (PTH còn lại chỉ có vế phải A). Bỏ nó thì X ∉ A⁺, nên cần giữ.
- A → B (hoặc A → {B}): bỏ nó thì B ∉ A⁺ vì PTH B → A chỉ cho ra A. Cần giữ.
- B → A (hoặc KI → A): bỏ nó thì B⁺ = {B} (hoặc (KI)⁺ = {K, I}), không chứa A. Cần giữ.

**Kết quả:** phủ tối thiểu trùng với tập sau B1: G_DONHANG 16 PTH; G_PHIEUNHAP 8; G_MAGIAMGIA 10; G_TAIKHOAN 6; G_PHIEUGIAO 5; G_THANHTOAN 10.

**Lưu ý với THANHTOAN.** Khóa thay thế KI chỉ có hiệu lực với các thanh toán qua ngân hàng, ví hoặc cổng thanh toán (cả hai thuộc tính đều có giá trị); thanh toán tiền mặt tại quầy không có mã giao dịch ngoài nên không có PTH này cho dòng đó.

### 4.3.7. CHITIETTRA (có thuộc tính thừa ở vế trái)

**Đặt tên:** A = MaHS, B = MaDH, C = SoDong, D = SoLuongTra, E = MaSeri.

**F:** f1: ABC → DE; f2: A → B (mỗi hồ sơ đổi trả có đúng một đơn gốc, [v3] 1.2.8; PTH này được bổ sung ở mục 3 khi chuyển sang mô hình quan hệ).

**B1** (3 PTH): #1 ABC → D, #2 ABC → E, #3 A → B.

**B2. Thuộc tính thừa ở vế trái:**

| PTH | Thử bỏ | Bao đóng | Kết luận |
|---|---|---|---|
| ABC → D | bỏ **B** | (AC)⁺ = {A, C, B (theo A → B)}, rồi ABC → D cho D | D ∈ (AC)⁺ nên **B thừa**, thay bằng AC → D |
| AC → D (sau khi bỏ B) | bỏ A | C⁺ = {C}, không có D | A không thừa |
| | bỏ C | A⁺ = {A, B}, không có D | C không thừa |
| ABC → E | bỏ B | (AC)⁺ ∋ B, mà ABC → E nên E ∈ (AC)⁺ | **B thừa**, thay bằng AC → E |

Sau B2: AC → D, AC → E, A → B.

**B3:** AC → D: bỏ đi thì (AC)⁺ = {A, C, B, E}, không có D, giữ. AC → E: bỏ đi thì (AC)⁺ = {A, C, B, D}, không có E, giữ. A → B: bỏ đi thì A⁺ = {A}, giữ.

**Phủ tối thiểu G (3 PTH):** G_CHITIETTRA = { AC → D, AC → E, A → B }.

**Tương đương:** ABC → D suy ra từ G vì (ABC)⁺ ⊇ (AC)⁺ ∋ D; tương tự ABC → E; A → B có sẵn. Vậy F ≡ G.

**Ý nghĩa.** MaDH thừa trong khóa vì hồ sơ đã xác định đơn. Vì vậy khóa của CHITIETTRA là (MaHS, SoDong), không phải (MaHS, MaDH, SoDong); MaDH vẫn được giữ làm cột để tạo khóa ngoại ghép tới dòng đơn (mục 7), nhưng là thuộc tính phụ thuộc vào một phần của khóa (xem mục 8).

## 4.4. Quan hệ chỉ có một PTH (khóa → tất cả)

Với các quan hệ dưới đây F chỉ gồm một PTH X → Y₁…Yₙ. **B1** tách thành n PTH. **B2** chỉ cần xét khi X có nhiều thuộc tính; **B3** không loại được PTH nào vì mỗi Yᵢ chỉ được sinh ra bởi X → Yᵢ.

Với vế trái gồm 2 thuộc tính (CHITIETPHIEUNHAP, CHITIETDONHANG, GIATRITHONGSO, CHITIETGIOHANG, LANGIAO, CHITIETKIEMKE, CHITIETGUIHANG) : không có PTH nào có vế trái là tập con thực sự của X, nên bao đóng của từng thuộc tính lẻ trong X chỉ là chính nó; không thuộc tính nào của X thừa.

| Quan hệ | Vế trái X | Số PTH sau B1 | B2 | B3 | \|G\| |
|---|---|---|---|---|---|
| LOAIHANG | MaLoai | 3 | không có vế trái nhiều thuộc tính | không loại | 3 |
| THUONGHIEU | MaTH | 2 | như trên | không loại | 2 |
| VAITRO | MaVT | 1 | như trên | không loại | 1 |
| KHACHHANG | MaKH | 4 | như trên | không loại | 4 |
| DIACHINHANHANG | MaDC | 7 | như trên | không loại | 7 |
| NHANVIEN | MaNV | 3 | như trên | không loại | 3 |
| NHACUNGCAP | MaNCC | 6 | như trên | không loại | 6 |
| GIAODICHKHO | MaGDK | 9 | như trên | không loại | 9 |
| GIUHANG | MaGiu | 6 | như trên | không loại | 6 |
| GIOHANG | MaGio | 3 | như trên | không loại | 3 |
| DOTKIEMKE | MaDot | 6 | như trên | không loại | 6 |
| DIEUCHINHDON | MaDieuChinh | 6 | như trên | không loại | 6 |
| KHOANHOAN | MaHoan | 7 | như trên | không loại | 7 |
| BANGIAOCOD | MaBG | 6 | như trên | không loại | 6 |
| HOSODOITRA | MaHS | 8 | như trên | không loại | 8 |
| LANNHANLAI | MaNhanLai | 7 | như trên | không loại | 7 |
| PHIEUGUIHANG | MaGui | 6 | như trên | không loại | 6 |
| BIENDONGSODU | MaBD | 5 | như trên | không loại | 5 |
| CHITIETPHIEUNHAP | MaPN, SoDong | 3 | không thừa | không loại | 3 |
| CHITIETDONHANG | MaDH, SoDong | 5 | không thừa | không loại | 5 |
| GIATRITHONGSO | MaSP, MaTS | 1 | không thừa | không loại | 1 |
| CHITIETGIOHANG | MaGio, MaSP | 1 | không thừa | không loại | 1 |
| LANGIAO | MaGiao, SoLan | 3 | không thừa | không loại | 3 |
| CHITIETKIEMKE | MaDot, MaSP | 3 | không thừa | không loại | 3 |
| CHITIETGUIHANG | MaGui, SoDong | 5 | không thừa | không loại | 5 |

## 4.5. Tổng hợp

| Nhóm | Quan hệ | Kết quả |
|---|---|---|
| Có thuộc tính thừa ở vế trái (loại MaDH) | CHITIETTRA (ABC → DE thành AC → DE) | Thêm PTH A → B; khóa là (MaHS, SoDong) |
| Có PTH dư thừa (loại 1 PTH) | HANGCOSERI (11 → 10), PHIEUBAOHANH (16 → 15) | PTH dư thừa đều là `Khóa → MaSP`, suy ra được qua dòng đơn, dòng nhập hoặc số seri |
| Không loại gì, F gốc có ≥ 2 PTH | MATHANG, ANHMATHANG, DINHNGHIATHONGSO, DONHANG, PHIEUNHAP, THANHTOAN, MAGIAMGIA, TAIKHOAN, PHIEUGIAO | G trùng tập sau B1 |
| Chỉ một PTH | 25 quan hệ ở 4.4 | G trùng tập sau B1 |
| Toàn khóa | NHANVIEN_VAITRO | Không có PTH không tầm thường |

**Nhận xét.**

1. **B2 chỉ loại thuộc tính ở CHITIETTRA** (MaDH thừa vì MaHS → MaDH); ở các quan hệ khác các vế trái ghép (khóa ghép hoặc cặp UNIQUE) đều đã tối thiểu.
2. **B3 chỉ loại được ở hai quan hệ**, đều do thuộc tính `MaSP` lưu thêm dù đã suy ra từ khóa ngoại khác. Đây là tín hiệu vi phạm dạng chuẩn cao (BCNF ở HANGCOSERI, 3NF ở PHIEUBAOHANH vì MaSP không thuộc khóa nào) mà mục 8 sẽ chứng minh và mục 9 sẽ cải tiến (bỏ `MaSP` khỏi hai quan hệ hoặc tách quan hệ).
3. **Phủ tối thiểu không thay đổi khóa**: khóa ứng viên ở mục 5 sẽ tìm từ G; vì G ≡ F nên cùng tập khóa.
4. **Các quan hệ ở 4.3.6 và 4.4 có phủ "tầm thường"** vì F gốc chỉ gồm PTH của khóa. Điều này không có nghĩa lược đồ tốt: đó là hệ quả của việc F gốc được rút từ quy tắc nghiệp vụ mà chưa tính các PTH sinh từ cột lưu sẵn (xem 03, mục 3.7). Nếu giữ các cột lưu sẵn, F của DONHANG, CHITIETDONHANG và các quan hệ tương tự có thêm PTH không khóa và phủ tối thiểu sẽ khác.

## 4.6. Câu hỏi giảng viên có thể hỏi

- *Vì sao phải làm B1 trước B2 và B3?* Để mỗi vế phải chỉ còn một thuộc tính; khi đó "thuộc tính thừa" ở vế trái và "PTH dư thừa" có định nghĩa chính xác bằng bao đóng.
- *Vì sao ở HANGCOSERI loại A → C chứ không loại DE → C?* Vì DE → C không suy ra được từ các PTH còn lại ((DE)⁺ = {D, E}), còn A → C thì suy ra được qua A → D, A → E rồi DE → C. Mọi thứ tự xét đều cho cùng phủ.
- *Phủ tối thiểu có duy nhất không?* Không phải lúc nào cũng duy nhất. Ở các quan hệ này đã thử nhiều thứ tự và chỉ ra một phủ.
- *Vì sao F ≡ G?* Mỗi PTH bị loại suy ra được từ G bằng bao đóng (đã chứng minh ở 4.3.1 và 4.3.2); G là tập con của F sau B1.
- *PTH A → C dư thừa có nghĩa là có thể xóa cột MaSP không?* Về logic, MaSP suy ra được nên không cần lưu. Nhưng khi xóa phải bảo đảm vẫn tìm được MaSP qua dòng đơn hoặc dòng nhập; đây là nội dung phần cải tiến.
