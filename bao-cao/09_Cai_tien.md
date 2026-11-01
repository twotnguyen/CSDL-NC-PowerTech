# MỤC 9. CẢI TIẾN LƯỢC ĐỒ: PHÂN RÃ, CHỨNG MINH BẢO TOÀN VÀ DẠNG CHUẨN 4

Căn cứ: kết quả ở [08_Dang_chuan.md](08_Dang_chuan.md): 35 quan hệ đạt BCNF, ba quan hệ chưa đạt (CHITIETTRA 1NF, PHIEUBAOHANH 2NF, HANGCOSERI 3NF), dạng chuẩn chung 1NF. Mục này cải tiến ba quan hệ đó, chứng minh phép tách **bảo toàn thông tin** và **bảo toàn phụ thuộc hàm**, so sánh trước và sau, rồi tìm tình huống **4NF**. Kết quả tay được đối chiếu bằng [tools/phanra.py](tools/phanra.py).

## 9.1. Phương pháp

**Thuật toán phân rã** (bài giảng, đưa lược đồ về BCNF):

1. B1: bỏ khỏi F các PTH f có VT(f) ∪ VP(f) = Q⁺ (tập F*).
2. B2: nếu F* = ∅ thì dừng (giữ Q). Ngược lại chọn PTH X → A "gây xấu" (vế trái không chứa khóa), tách thành Q₁ = {X, A} và Q₂ = Q⁺ \ A, với Fᵢ là PTH chiếu từ F⁺; rồi phân rã đệ quy Q₁, Q₂.

**Thuật toán tổng hợp (Bernstein) cải tiến:** B1 tìm phủ tối thiểu; B2 nhóm các PTH cùng vế trái; B3 gộp nhóm có vế trái phụ thuộc lẫn nhau; B4 mỗi nhóm thành một quan hệ con; B5 tìm các khóa của Q; B6 nếu chưa quan hệ con nào chứa khóa của Q thì thêm một quan hệ chứa một khóa.

**Chứng minh** (theo bài giảng):

- **Bảo toàn PTH:** đặt F' = ∪Fᵢ; cần (1) mọi f' ∈ F' \ F thuộc F⁺ và (2) mọi f ∈ F \ F' thuộc F'⁺.
- **Bảo toàn thông tin:** lập bảng tableau (cột là thuộc tính của Q, dòng là các Qᵢ; ô là aⱼ nếu thuộc tính ∈ Qᵢ, ngược lại bₖ), áp các PTH của F để đồng nhất ký hiệu; có một dòng toàn a thì phép tách bảo toàn thông tin. Với phép tách hai thành phần có thể dùng định lý: (Q₁ ∩ Q₂) → (Q₁ \ Q₂) hoặc (Q₁ ∩ Q₂) → (Q₂ \ Q₁).

**Chữ cái đặt tên** như mục 4 (bảng đặt tên nhắc lại ở từng quan hệ). F là phủ tối thiểu G.

## 9.2. CHITIETTRA: từ 1NF lên BCNF

**Đặt tên:** A = MaHS, B = MaDH, C = SoDong, D = SoLuongTra, E = MaSeri. **F:** AC → DE; A → B. Khóa: AC. Vi phạm: A → B (phụ thuộc bộ phận, MaDH chỉ phụ thuộc MaHS).

**Phân rã theo thuật toán:** B1: không PTH nào có VT ∪ VP = Q⁺ (thiếu B hoặc thiếu D, E). B2: chọn **A → B** (vế trái là một phần của khóa, dễ gây vi phạm 2NF). Tách:

- **Q₁(A, B) = (MaHS, MaDH)**, F₁ = {A → B}; với Q₁ thì F₁ \ {A → B} = ∅ (vế trái ∪ vế phải = Q₁⁺) nên dừng (BCNF, khóa A).
- **Q₂(A, C, D, E) = (MaHS, SoDong, SoLuongTra, MaSeri)**, F₂ = {AC → DE}; dừng (BCNF, khóa AC).

Q₁ **trùng với phép chiếu (MaHS, MaDH) của HOSODOITRA** nên không tạo quan hệ mới: chỉ **bỏ cột MaDH khỏi CHITIETTRA**.

**Các quan hệ con và PTH chiếu (Fᵢ):**

- **Q1(A, B)**: F = {A → B}
- **Q2(A, C, D, E)**: F = {AC → DE}

**Bảng khởi tạo:**

| T | A | B | C | D | E |
|---|---|---|---|---|---|
| Q1 | a1 | a2 | b1 | b2 | b3 |
| Q2 | a1 | b4 | a3 | a4 | a5 |

**Biến đổi theo PTH của F:**

- Hai dòng Q1 và Q2 cùng giá trị ở A; theo PTH A → B, ô cột B: b4 thành a2.

**Bảng sau biến đổi:**

| T | A | B | C | D | E |
|---|---|---|---|---|---|
| Q1 | a1 | a2 | b1 | b2 | b3 |
| Q2 | a1 | b4 ⇒ a2 | a3 | a4 | a5 |

Dòng Q2 chứa toàn ký hiệu a → **bảo toàn thông tin**.

**Kiểm tra bảo toàn PTH** (cách làm của bài giảng):

- F' = ∪Fᵢ = {A → B; AC → DE}.
- (1) F' \ F ⊆ F⁺: hiển nhiên, vì mỗi Fᵢ là tập PTH chiếu từ F⁺.
- (2) AC → DE: (AC)⁺_F' = {ABCDE} ⊇ DE → thỏa.
- (2) A → B: (A)⁺_F' = {AB} ⊇ B → thỏa.

**Kết luận: bảo toàn PTH.**

**Kết quả.** Hai quan hệ con đều BCNF (khóa A và AC), phép tách bảo toàn thông tin và PTH. CHITIETTRA nâng từ **1NF lên BCNF**.

## 9.3. PHIEUBAOHANH: từ 2NF lên BCNF

**Đặt tên:** A = MaPhieuBH, B = MaKH, C = MaSP, D = MaSeri, E = MaDH, G = SoDong, H = MoTaLoi, I = PhuKienDiKem, K = NgayNhan, L = NgayHenTra, M = NgayTraThucTe, N = TinhTrang, O = KetQua, P = LyDoTuChoi, Q = MaNVTiepNhan. **F:** A → BDEGHIKLMNOPQ; EG → C; D → C. Khóa: A. Vi phạm: EG → C và D → C (vế trái không là siêu khóa, MaSP không là thuộc tính khóa).

Trong các bảng tableau, ký hiệu **Z** gộp mười thuộc tính B, H, I, K, L, M, N, O, P, Q: chúng chỉ có trong quan hệ chứa A và chỉ ở vế phải của A → Z, nên không ảnh hưởng đến kết quả biến đổi.

### Cách 1: thuật toán phân rã

B1: không PTH nào có VT ∪ VP = Q⁺ (thiếu C hoặc quá ít thuộc tính). B2: chọn **D → C** (MaSeri → MaSP). Tách Q₁(D, C) = (MaSeri, MaSP) và Q₂ = Q⁺ \ C (MaSP bị bỏ khỏi phiếu).

**Các quan hệ con và PTH chiếu (Fᵢ):**

- **Q1(C, D)**: F = {D → C}
- **Q2(A, B, D, E, G, H, I, K, L, M, N, O, P, Q)**: F = {A → BDEGHIKLMNOPQ}

**Bảng khởi tạo:**

| T | A | C | D | E | G | Z |
|---|---|---|---|---|---|---|
| Q1 | b1 | a2 | a3 | b2 | b3 | b4 |
| Q2 | a1 | b5 | a3 | a4 | a5 | a6 |

**Biến đổi theo PTH của F:**

- Hai dòng Q1 và Q2 cùng giá trị ở D; theo PTH D → C, ô cột C: b5 thành a2.

**Bảng sau biến đổi:**

| T | A | C | D | E | G | Z |
|---|---|---|---|---|---|---|
| Q1 | b1 | a2 | a3 | b2 | b3 | b4 |
| Q2 | a1 | b5 ⇒ a2 | a3 | a4 | a5 | a6 |

Dòng Q2 chứa toàn ký hiệu a → **bảo toàn thông tin**.

**Kiểm tra bảo toàn PTH** (cách làm của bài giảng):

- F' = ∪Fᵢ = {D → C; A → BDEGHIKLMNOPQ}.
- (1) F' \ F ⊆ F⁺: hiển nhiên, vì mỗi Fᵢ là tập PTH chiếu từ F⁺.
- (2) A → BDEGHIKLMNOPQ: (A)⁺_F' = {ABCDEGHIKLMNOPQ} ⊇ BDEGHIKLMNOPQ → thỏa.
- (2) EG → C: (EG)⁺_F' = {EG} ⊉ C → **không thỏa**.
- (2) D → C: (D)⁺_F' = {CD} ⊇ C → thỏa.

**Kết luận: không bảo toàn PTH** (thỏa (1), không thỏa (2)).

Phép tách **bảo toàn thông tin nhưng mất PTH EG → C** (MaDH, SoDong → MaSP). Tách theo EG → C thì ngược lại mất D → C.

### Cách 2: thuật toán tổng hợp cải tiến

- B1: phủ tối thiểu G = {A → B, A → D, ..., A → Q, EG → C, D → C} (mục 4).
- B2, B3: nhóm theo vế trái: F₁ vế trái A; F₂ vế trái EG; F₃ vế trái D. Không có hai vế trái phụ thuộc lẫn nhau.
- B4: R₁ = A ∪ {B, D, E, G, H, I, K, L, M, N, O, P, Q}; R₂(E, G, C) = (MaDH, SoDong, MaSP); R₃(D, C) = (MaSeri, MaSP).
- B5, B6: khóa của Q là A, nằm trong R₁, nên không thêm quan hệ.

**Các quan hệ con và PTH chiếu (Fᵢ):**

- **R1(A, B, D, E, G, H, I, K, L, M, N, O, P, Q)**: F = {A → BDEGHIKLMNOPQ}
- **R2(C, E, G)**: F = {EG → C}
- **R3(C, D)**: F = {D → C}

**Bảng khởi tạo:**

| T | A | C | D | E | G | Z |
|---|---|---|---|---|---|---|
| R1 | a1 | b1 | a3 | a4 | a5 | a6 |
| R2 | b2 | a2 | b3 | a4 | a5 | b4 |
| R3 | b5 | a2 | a3 | b6 | b7 | b8 |

**Biến đổi theo PTH của F:**

- Hai dòng R1 và R2 cùng giá trị ở E,G; theo PTH E,G → C, ô cột C: b1 thành a2.

**Bảng sau biến đổi:**

| T | A | C | D | E | G | Z |
|---|---|---|---|---|---|---|
| R1 | a1 | b1 ⇒ a2 | a3 | a4 | a5 | a6 |
| R2 | b2 | a2 | b3 | a4 | a5 | b4 |
| R3 | b5 | a2 | a3 | b6 | b7 | b8 |

Dòng R1 chứa toàn ký hiệu a → **bảo toàn thông tin**.

**Kiểm tra bảo toàn PTH** (cách làm của bài giảng):

- F' = ∪Fᵢ = {A → BDEGHIKLMNOPQ; EG → C; D → C}.
- (1) F' \ F ⊆ F⁺: hiển nhiên, vì mỗi Fᵢ là tập PTH chiếu từ F⁺.
- (2) A → BDEGHIKLMNOPQ: (A)⁺_F' = {ABCDEGHIKLMNOPQ} ⊇ BDEGHIKLMNOPQ → thỏa.
- (2) EG → C: (EG)⁺_F' = {CEG} ⊇ C → thỏa.
- (2) D → C: (D)⁺_F' = {CD} ⊇ C → thỏa.

**Kết luận: bảo toàn PTH.**

**Kết quả.** Cả ba quan hệ con BCNF; phép tách bảo toàn thông tin **và** PTH. Trong cơ sở dữ liệu, **R₂ là một phép chiếu của CHITIETDONHANG** và **R₃ nằm trong SERIMATHANG** (mục 9.4), nên không tạo quan hệ mới. Chỉ có R₁ thay PHIEUBAOHANH: **bỏ cột MaSP**. Tên hàng được lấy bằng phép nối với CHITIETDONHANG theo (MaDH, SoDong). **PHIEUBAOHANH nâng từ 2NF lên BCNF.**

## 9.4. HANGCOSERI: từ 3NF lên BCNF

**Đặt tên:** A = MaSeri, B = SoSeri, C = MaSP, D = MaPN, E = SoDongNhap, G = MaDH, H = SoDongDon, I = TinhTrang, K = ThoiDiemNhap. **F:** A → BDEGHIK; CB → A; DE → C; GH → C. Khóa: A; CB; BDE; BGH. Đang 3NF vì MaSP (C) là thuộc tính khóa; vi phạm BCNF: DE → C và GH → C.

### Cách 1: phân rã theo thuật toán

B1: không PTH nào có VT ∪ VP = Q⁺. B2: chọn **DE → C** (vế trái không chứa khóa). Tách Q₁(D, E, C) = (MaPN, SoDongNhap, MaSP) và Q₂ = Q⁺ \ C.

**Các quan hệ con và PTH chiếu (Fᵢ):**

- **Q1(C, D, E)**: F = {DE → C}
- **Q2(A, B, D, E, G, H, I, K)**: F = {A → BGH; BDE → GH; BGH → ADEIK}

**Bảng khởi tạo:**

| T | A | B | C | D | E | G | H | I | K |
|---|---|---|---|---|---|---|---|---|---|
| Q1 | b1 | b2 | a3 | a4 | a5 | b3 | b4 | b5 | b6 |
| Q2 | a1 | a2 | b7 | a4 | a5 | a6 | a7 | a8 | a9 |

**Biến đổi theo PTH của F:**

- Hai dòng Q1 và Q2 cùng giá trị ở D,E; theo PTH D,E → C, ô cột C: b7 thành a3.

**Bảng sau biến đổi:**

| T | A | B | C | D | E | G | H | I | K |
|---|---|---|---|---|---|---|---|---|---|
| Q1 | b1 | b2 | a3 | a4 | a5 | b3 | b4 | b5 | b6 |
| Q2 | a1 | a2 | b7 ⇒ a3 | a4 | a5 | a6 | a7 | a8 | a9 |

Dòng Q2 chứa toàn ký hiệu a → **bảo toàn thông tin**.

**Kiểm tra bảo toàn PTH** (cách làm của bài giảng):

- F' = ∪Fᵢ = {DE → C; A → BGH; BDE → GH; BGH → ADEIK}.
- (1) F' \ F ⊆ F⁺: hiển nhiên, vì mỗi Fᵢ là tập PTH chiếu từ F⁺.
- (2) A → BDEGHIK: (A)⁺_F' = {ABCDEGHIK} ⊇ BDEGHIK → thỏa.
- (2) BC → A: (BC)⁺_F' = {BC} ⊉ A → **không thỏa**.
- (2) DE → C: (DE)⁺_F' = {CDE} ⊇ C → thỏa.
- (2) GH → C: (GH)⁺_F' = {GH} ⊉ C → **không thỏa**.

**Kết luận: không bảo toàn PTH** (thỏa (1), không thỏa (2)).

**Nhận xét.** Phép tách **bảo toàn thông tin** nhưng **mất hai PTH**: CB → A, tức (MaSP, SoSeri) → MaSeri, là quy tắc "số seri duy nhất trong cùng mặt hàng" (cần MaSP và SoSeri cùng ở một quan hệ); và GH → C, quy tắc dòng đơn xác định mặt hàng. Q₂ vì thế có khóa A, BDE, BGH nhưng không còn khóa CB.

### Cách 2: thuật toán tổng hợp

B1: phủ tối thiểu G. B2: nhóm theo vế trái: F₁ (A), F₂ (CB), F₃ (DE), F₄ (GH). B3: A → CB (A → B, A → DE → C) và CB → A, nên gộp F₁ với F₂: quan hệ gộp chứa mọi thuộc tính A, B, C, D, E, G, H, I, K, tức là **chính Q**. Q₃(D, E, C) và Q₄(G, H, C) là tập con của Q nên bị loại. Kết quả của tổng hợp là **Q nguyên vẹn (3NF)**: thuật toán tổng hợp chỉ bảo đảm 3NF.

### Phương án C: bốn thành phần (BCNF và bảo toàn đủ)

Tách thành bốn quan hệ con: hai quan hệ giữ lại hai PTH của MaSP (DE → C, GH → C), một quan hệ giữ phần còn lại của chiếc hàng, và một quan hệ riêng cho bộ ba nhận diện (MaSeri, SoSeri, MaSP) để giữ khóa CB:

- Q₁(D, E, C) = (MaPN, SoDongNhap, MaSP), PTH DE → C;
- Q₂(G, H, C) = (MaDH, SoDongDon, MaSP), PTH GH → C;
- Q₃(A, D, E, G, H, I, K) = (MaSeri, MaPN, SoDongNhap, MaDH, SoDongDon, TinhTrang, ThoiDiemNhap), PTH A → DEGHIK;
- Q₄(A, B, C) = (MaSeri, SoSeri, MaSP), PTH A → B, A → C, CB → A (hai khóa A và CB).

Q₁ và Q₂ **trùng với phép chiếu của CHITIETPHIEUNHAP và CHITIETDONHANG** (đã có) nên không tạo quan hệ mới. Hai quan hệ cần tạo: **HANGCOSERI** rút gọn (Q₃) và **SERIMATHANG** mới (Q₄).

**Các quan hệ con và PTH chiếu (Fᵢ):**

- **Q1(C, D, E)**: F = {DE → C}
- **Q2(C, G, H)**: F = {GH → C}
- **Q3(A, D, E, G, H, I, K)**: F = {A → DEGHIK}
- **Q4(A, B, C)**: F = {A → BC; BC → A}

**Bảng khởi tạo:**

| T | A | B | C | D | E | G | H | I | K |
|---|---|---|---|---|---|---|---|---|---|
| Q1 | b1 | b2 | a3 | a4 | a5 | b3 | b4 | b5 | b6 |
| Q2 | b7 | b8 | a3 | b9 | b10 | a6 | a7 | b11 | b12 |
| Q3 | a1 | b13 | b14 | a4 | a5 | a6 | a7 | a8 | a9 |
| Q4 | a1 | a2 | a3 | b15 | b16 | b17 | b18 | b19 | b20 |

**Biến đổi theo PTH của F:**

- Hai dòng Q3 và Q4 cùng giá trị ở A; theo PTH A → G, ô cột G: b17 thành a6.
- Hai dòng Q3 và Q4 cùng giá trị ở A; theo PTH A → B, ô cột B: b13 thành a2.
- Hai dòng Q3 và Q4 cùng giá trị ở A; theo PTH A → H, ô cột H: b18 thành a7.
- Hai dòng Q3 và Q4 cùng giá trị ở A; theo PTH A → E, ô cột E: b16 thành a5.
- Hai dòng Q3 và Q4 cùng giá trị ở A; theo PTH A → K, ô cột K: b20 thành a9.
- Hai dòng Q3 và Q4 cùng giá trị ở A; theo PTH A → I, ô cột I: b19 thành a8.
- Hai dòng Q3 và Q4 cùng giá trị ở A; theo PTH A → D, ô cột D: b15 thành a4.
- Hai dòng Q1 và Q3 cùng giá trị ở D,E; theo PTH D,E → C, ô cột C: b14 thành a3.

**Bảng sau biến đổi:**

| T | A | B | C | D | E | G | H | I | K |
|---|---|---|---|---|---|---|---|---|---|
| Q1 | b1 | b2 | a3 | a4 | a5 | b3 | b4 | b5 | b6 |
| Q2 | b7 | b8 | a3 | b9 | b10 | a6 | a7 | b11 | b12 |
| Q3 | a1 | b13 ⇒ a2 | b14 ⇒ a3 | a4 | a5 | a6 | a7 | a8 | a9 |
| Q4 | a1 | a2 | a3 | b15 ⇒ a4 | b16 ⇒ a5 | b17 ⇒ a6 | b18 ⇒ a7 | b19 ⇒ a8 | b20 ⇒ a9 |

Dòng Q3, Q4 chứa toàn ký hiệu a → **bảo toàn thông tin**.

**Kiểm tra bảo toàn PTH** (cách làm của bài giảng):

- F' = ∪Fᵢ = {DE → C; GH → C; A → BCDEGHIK; BC → A}.
- (1) F' \ F ⊆ F⁺: hiển nhiên, vì mỗi Fᵢ là tập PTH chiếu từ F⁺.
- (2) A → BDEGHIK: (A)⁺_F' = {ABCDEGHIK} ⊇ BDEGHIK → thỏa.
- (2) BC → A: (BC)⁺_F' = {ABCDEGHIK} ⊇ A → thỏa.
- (2) DE → C: (DE)⁺_F' = {CDE} ⊇ C → thỏa.
- (2) GH → C: (GH)⁺_F' = {CGH} ⊇ C → thỏa.

**Kết luận: bảo toàn PTH.**

Mọi quan hệ con đều BCNF; phép tách **bảo toàn thông tin và PTH**.

### Phương án phụ: seri duy nhất toàn cửa hàng

Nếu chốt số seri duy nhất toàn cửa hàng (kịch bản S1 ở mục 8.7), PTH CB → A đổi thành B → A. Khi đó phân rã Delobel chỉ mất GH → C, và thêm thành phần Q(G, H, C) (đã có trong CHITIETDONHANG) thì bảo toàn đủ với ba thành phần Q₁(D, E, C), Q₂(G, H, C), Q₃(A, B, D, E, G, H, I, K):

**Các quan hệ con và PTH chiếu (Fᵢ):**

- **Q1(C, D, E)**: F = {DE → C}
- **Q2(C, G, H)**: F = {GH → C}
- **Q3(A, B, D, E, G, H, I, K)**: F = {A → B; B → ADEGHIK}

**Bảng khởi tạo:**

| T | A | B | C | D | E | G | H | I | K |
|---|---|---|---|---|---|---|---|---|---|
| Q1 | b1 | b2 | a3 | a4 | a5 | b3 | b4 | b5 | b6 |
| Q2 | b7 | b8 | a3 | b9 | b10 | a6 | a7 | b11 | b12 |
| Q3 | a1 | a2 | b13 | a4 | a5 | a6 | a7 | a8 | a9 |

**Biến đổi theo PTH của F:**

- Hai dòng Q1 và Q3 cùng giá trị ở D,E; theo PTH D,E → C, ô cột C: b13 thành a3.

**Bảng sau biến đổi:**

| T | A | B | C | D | E | G | H | I | K |
|---|---|---|---|---|---|---|---|---|---|
| Q1 | b1 | b2 | a3 | a4 | a5 | b3 | b4 | b5 | b6 |
| Q2 | b7 | b8 | a3 | b9 | b10 | a6 | a7 | b11 | b12 |
| Q3 | a1 | a2 | b13 ⇒ a3 | a4 | a5 | a6 | a7 | a8 | a9 |

Dòng Q3 chứa toàn ký hiệu a → **bảo toàn thông tin**.

**Kiểm tra bảo toàn PTH** (cách làm của bài giảng):

- F' = ∪Fᵢ = {DE → C; GH → C; A → B; B → ADEGHIK}.
- (1) F' \ F ⊆ F⁺: hiển nhiên, vì mỗi Fᵢ là tập PTH chiếu từ F⁺.
- (2) A → BDEGHIK: (A)⁺_F' = {ABCDEGHIK} ⊇ BDEGHIK → thỏa.
- (2) B → A: (B)⁺_F' = {ABCDEGHIK} ⊇ A → thỏa.
- (2) DE → C: (DE)⁺_F' = {CDE} ⊇ C → thỏa.
- (2) GH → C: (GH)⁺_F' = {CGH} ⊇ C → thỏa.

**Kết luận: bảo toàn PTH.**

Phương án này gọn hơn (chỉ bỏ cột MaSP, không cần quan hệ SERIMATHANG) nhưng **đổi một quy tắc nghiệp vụ**: hai hãng có thể in cùng số seri.

### So sánh và lựa chọn

| Phương án | Dạng chuẩn | Bảo toàn thông tin | Bảo toàn PTH | Quan hệ mới | Ghi chú |
|---|---|---|---|---|---|
| Giữ nguyên | 3NF | không cần tách | có | không | MaSP lưu thừa ở mỗi chiếc |
| Phân rã (Delobel) | BCNF | có | **không** (mất CB → A, GH → C) | không | Mất bảo đảm seri duy nhất theo mặt hàng |
| Tổng hợp | 3NF | có | có | không | Trả lại đúng Q |
| **C: bốn thành phần** | **BCNF** | **có** | **có** | **SERIMATHANG** | Cần ràng buộc nhất quán MaSP (xem 9.5) |
| Seri toàn cửa hàng | BCNF | có | có (ba thành phần) | không | Đổi quy tắc nghiệp vụ |

**Chọn phương án C**: giữ nguyên quy tắc "seri duy nhất theo mặt hàng" của v3, đạt BCNF và không mất PTH. Phương án "seri toàn cửa hàng" là lựa chọn thay thế nếu giảng viên hoặc cửa hàng chấp nhận quy tắc đó.

## 9.5. Lược đồ sau cải tiến

Lược đồ có **39 quan hệ** (38 cũ, thêm SERIMATHANG). Bốn quan hệ thay đổi (gạch chân liền là khóa chính, gạch nét đứt là khóa ngoại, theo quy ước ở mục 7):

- **CHITIETTRA**(<u>MaHS</u><sup>FK</sup>, <u>SoDong</u>, SoLuongTra, <span style="text-decoration: underline dashed">MaSeri</span>): bỏ MaDH. Dòng đơn được trả là (HOSODOITRA.MaDH, SoDong).
- **PHIEUBAOHANH**(<u>MaPhieuBH</u>, <span style="text-decoration: underline dashed">MaKH</span>, <span style="text-decoration: underline dashed">MaSeri</span>, <span style="text-decoration: underline dashed">MaDH</span>, <span style="text-decoration: underline dashed">SoDong</span>, MoTaLoi, PhuKienDiKem, NgayNhan, NgayHenTra, NgayTraThucTe, TinhTrang, KetQua, LyDoTuChoi, <span style="text-decoration: underline dashed">MaNVTiepNhan</span>): bỏ MaSP; (MaDH, SoDong) là khóa ngoại ghép tới CHITIETDONHANG.
- **HANGCOSERI**(<u>MaSeri</u><sup>FK</sup>, <span style="text-decoration: underline dashed">MaPN</span>, <span style="text-decoration: underline dashed">SoDongNhap</span>, <span style="text-decoration: underline dashed">MaDH</span>, <span style="text-decoration: underline dashed">SoDongDon</span>, TinhTrang, ThoiDiemNhap): MaSeri vừa là khóa chính vừa là khóa ngoại tới SERIMATHANG; bỏ SoSeri và MaSP; (MaPN, SoDongNhap) tới CHITIETPHIEUNHAP (không rỗng); (MaDH, SoDongDon) tới CHITIETDONHANG (cho rỗng).
- **SERIMATHANG**(<u>MaSeri</u>, SoSeri, <span style="text-decoration: underline dashed">MaSP</span>): quan hệ mới; UNIQUE (MaSP, SoSeri).

**Ràng buộc nhất quán** không biểu diễn được bằng PTH trong một quan hệ (cưỡng chế bằng khóa ngoại ghép hoặc kiểm tra khi ghi):

1. MaSP của SERIMATHANG phải bằng MaSP của dòng nhập (MaPN, SoDongNhap) và của dòng đơn (MaDH, SoDongDon) nếu có.
2. Phiếu bảo hành có MaSeri thì MaSP suy ra từ SERIMATHANG phải bằng MaSP của dòng mua gốc (MaDH, SoDong).
3. Dòng đơn trong CHITIETTRA phải thuộc đơn của hồ sơ; nếu muốn khóa ngoại khai báo được ở mức cơ sở dữ liệu thì khi cài đặt giữ thêm cột MaDH và khóa ngoại ghép (MaHS, MaDH) tới HOSODOITRA (mục 7); về lý thuyết đó là cột nhân bản có kiểm soát, không thuộc lược đồ logic.

**Mã SQL đề xuất** (T-SQL, chỉ minh họa, chưa áp dụng vào cơ sở dữ liệu nào):

```sql
CREATE TABLE SERIMATHANG (
    MaSeri INT PRIMARY KEY,
    SoSeri NVARCHAR(100) NOT NULL,
    MaSP   INT NOT NULL REFERENCES MATHANG(MaSP),
    CONSTRAINT UQ_SERIMATHANG UNIQUE (MaSP, SoSeri)
);
CREATE TABLE HANGCOSERI (
    MaSeri INT PRIMARY KEY REFERENCES SERIMATHANG(MaSeri),
    MaPN INT NOT NULL, SoDongNhap INT NOT NULL,
    MaDH INT NULL,     SoDongDon  INT NULL,
    TinhTrang NVARCHAR(30) NOT NULL, ThoiDiemNhap DATETIME2 NOT NULL,
    FOREIGN KEY (MaPN, SoDongNhap) REFERENCES CHITIETPHIEUNHAP(MaPN, SoDong),
    FOREIGN KEY (MaDH, SoDongDon)  REFERENCES CHITIETDONHANG(MaDH, SoDong)
);
-- Khung nhìn trả lại hình dạng cũ khi cần (kèm MaSP, SoSeri)
CREATE VIEW vw_HangCoSeri AS
SELECT h.*, s.SoSeri, s.MaSP
FROM HANGCOSERI h JOIN SERIMATHANG s ON s.MaSeri = h.MaSeri;
```

## 9.6. So sánh trước và sau cải tiến

| Quan hệ | Dư thừa trước | Dị thường trước | Sau cải tiến | Chi phí |
|---|---|---|---|---|
| CHITIETTRA | MaDH lặp lại ở mỗi dòng trả của cùng hồ sơ | **Cập nhật:** sửa đơn gốc của hồ sơ nhưng bỏ sót một dòng thì hồ sơ có hai đơn. **Thêm:** dòng trả có MaDH khác đơn của hồ sơ | MaDH chỉ ở HOSODOITRA | Muốn biết đơn của dòng trả phải nối với HOSODOITRA (một phép nối) |
| PHIEUBAOHANH | MaSP lặp ở mỗi phiếu của cùng dòng đơn hoặc cùng chiếc | **Cập nhật:** đổi mặt hàng của dòng đơn mà không sửa phiếu. **Thêm:** phiếu ghi MaSP không khớp dòng mua gốc | MaSP chỉ ở CHITIETDONHANG và SERIMATHANG | Một phép nối với CHITIETDONHANG để lấy tên hàng |
| HANGCOSERI | MaSP lặp ở mỗi chiếc của cùng dòng nhập; SoSeri gắn MaSP | **Cập nhật:** sửa mặt hàng của dòng nhập mà bỏ sót chiếc. **Thêm:** nhập chiếc có MaSP khác MaSP của dòng nhập mà nó thuộc về | Về hình thức MaSP không còn là PTH vi phạm trong một quan hệ, nhưng vẫn có ở cả SERIMATHANG và dòng nhập nên phải kiểm soát bằng ràng buộc nhất quán (9.5) | Thêm một quan hệ và một phép nối; thêm ràng buộc nhất quán |

**Ràng buộc.** Sau cải tiến, các khóa của mọi quan hệ đều là siêu khóa của mọi PTH nên lược đồ không còn PTH nào ngoài khóa; ràng buộc "seri duy nhất theo mặt hàng" vẫn được cưỡng chế (UNIQUE (MaSP, SoSeri)). **Lưu ý trung thực:** với CHITIETTRA và PHIEUBAOHANH, cải tiến loại hẳn dữ liệu thừa. Với HANGCOSERI, cải tiến đưa lược đồ về BCNF nhưng lượng MaSP lưu không giảm (mỗi chiếc vẫn một MaSP trong SERIMATHANG); lợi ích là mỗi quan hệ không còn PTH vi phạm và khóa (MaSP, SoSeri) được cưỡng chế, còn tính nhất quán liên quan hệ phải do ràng buộc ở 9.5 bảo đảm. Chưa đo hiệu năng: việc thêm một phép nối làm chậm hay nhanh truy vấn cần đo trên dữ liệu thật.

**Ví dụ truy vấn sau cải tiến** (mặt hàng của phiếu bảo hành):

```sql
SELECT b.MaPhieuBH, d.MaSP
FROM PHIEUBAOHANH b
JOIN CHITIETDONHANG d ON d.MaDH = b.MaDH AND d.SoDong = b.SoDong;
```

## 9.7. Tình huống dạng chuẩn 4 (4NF)

**Khái niệm.** Quan hệ đạt 4NF nếu đạt BCNF và mọi phụ thuộc đa trị (MVD) X ↠ Y không tầm thường có X là siêu khóa. MVD xuất hiện khi hai tập giá trị **độc lập** của cùng một đối tượng nằm chung trong một quan hệ.

**Tình huống: ảnh và thông số của mặt hàng.** Theo v3 (mục 1.2.1), một mặt hàng có nhiều ảnh và nhiều thông số, và "thêm hoặc đổi ảnh không làm đổi thông số", tức hai tập độc lập.

*Bước 1. Nếu lưu chung* một quan hệ M(MaSP, DuongDan, MaTS, GiaTri) (mỗi dòng là một cặp ảnh – thông số của mặt hàng):

- PTH: (MaSP, MaTS) → GiaTri. Khóa: (MaSP, DuongDan, MaTS). PTH này có vế trái là một phần của khóa nên M **không đạt 2NF**.
- Tách theo PTH: **R₁(MaSP, MaTS, GiaTri)** (chính là GIATRITHONGSO) và **R₂(MaSP, DuongDan, MaTS)**.

*Bước 2. R₂ đạt BCNF nhưng không đạt 4NF.* R₂ toàn khóa (khóa là cả ba thuộc tính), không có PTH không tầm thường nên **đạt BCNF**. Nhưng do tập ảnh và tập thông số độc lập nên với mỗi mặt hàng R₂ phải chứa **mọi cặp** (ảnh, thông số):

- **MaSP ↠ DuongDan** (và MaSP ↠ MaTS) là MVD không tầm thường mà MaSP không là siêu khóa → R₂ **vi phạm 4NF**.
- Phép tách R₂ thành **R₂₁(MaSP, DuongDan)** (chính là ANHMATHANG) và **R₂₂(MaSP, MaTS)** (đã có trong R₁) bảo toàn thông tin: (R₂₁ ∩ R₂₂) = MaSP và MaSP ↠ DuongDan (theo định lý về MVD, phép tách theo MVD luôn bảo toàn thông tin).

**Kết quả: ANHMATHANG và GIATRITHONGSO đạt 4NF; lược đồ không chứa R₂.**

**Số liệu minh họa từ dữ liệu mẫu** (`database/data.seed.sql`, 120 mặt hàng có cả ảnh và thông số; ảnh trung bình 2,58, thông số trung bình 10,23 mỗi mặt hàng):

| Cách lưu | Số dòng |
|---|---|
| M (lưu chung, mỗi dòng một cặp ảnh – thông số) | **3.256** (tổng của tích số ảnh × số thông số theo từng mặt hàng) |
| ANHMATHANG và GIATRITHONGSO (tách) | **1.538** = 310 ảnh + 1.228 thông số |

Lưu chung nhiều dòng hơn khoảng 2,1 lần chỉ để lặp lại cùng những thông tin. Ví dụ mặt hàng `MOU-GLORIOUS-WIRED-BLACK` có 3 ảnh và 3 thông số: lưu chung cần 9 dòng, tách chỉ 6 dòng; thêm một ảnh thứ tư buộc thêm 3 dòng ở dạng chung nhưng chỉ 1 dòng ở dạng tách (dị thường thêm).

**Về các quan hệ còn lại.** Sau cải tiến, 39 quan hệ đạt BCNF. Với 4NF cần chứng minh không có MVD không tầm thường ngoài PTH. Theo mô tả v3, mỗi quan hệ chỉ chứa **một** tập giá trị của đối tượng chính (dòng chi tiết, lần giao, lần nhận lại... đã tách thành quan hệ riêng), nên các quan hệ khác không chứa hai tập độc lập; kết luận này dựa trên mô tả nghiệp vụ, **chưa chứng minh tổng quát**.

## 9.8. Dạng chuẩn sau cải tiến

| Quan hệ | Trước | Sau |
|---|---|---|
| CHITIETTRA | 1NF | BCNF |
| PHIEUBAOHANH | 2NF | BCNF |
| HANGCOSERI | 3NF | BCNF |
| SERIMATHANG (mới) | — | BCNF (khóa MaSeri và (MaSP, SoSeri)) |
| 35 quan hệ còn lại | BCNF | BCNF |

**Dạng chuẩn chung của lược đồ cải tiến: BCNF** (39 quan hệ), và đạt 4NF theo các giả định độc lập ở 9.7. So với mục 8: từ **1NF lên BCNF**. Tình huống ảnh – thông số cho thấy việc tách theo phụ thuộc đa trị.

**Điều kiện đi kèm:** (a) hai quy tắc nhất quán về MaSP ở 9.5; (b) lựa chọn phương án C thay cho "seri toàn cửa hàng"; (c) họ tên giữ nguyên theo phương án 1 của mục 8.

## 9.9. Câu hỏi giảng viên có thể hỏi

- *Vì sao chọn phân rã hay tổng hợp?* Phân rã đưa tới BCNF nhưng có thể mất PTH (đã chứng minh ở HANGCOSERI); tổng hợp bảo toàn PTH nhưng chỉ bảo đảm 3NF. Phương án C kết hợp: tách về BCNF rồi thêm thành phần để giữ các PTH.
- *Phép tách bảo toàn thông tin được chứng minh thế nào?* Bằng tableau: có một dòng toàn ký hiệu a sau khi áp các PTH; với hai thành phần dùng định lý (Q₁ ∩ Q₂) → (Q₁ \ Q₂).
- *Vì sao bảo toàn PTH quan trọng ở HANGCOSERI?* Vì (MaSP, SoSeri) → MaSeri là quy tắc seri duy nhất theo mặt hàng; nếu MaSP và SoSeri nằm ở hai quan hệ khác nhau thì không cưỡng chế được bằng một khóa.
- *Có phải mọi lược đồ đều tách được về BCNF mà bảo toàn PTH?* Không; BCNF có thể không bảo toàn PTH, đó là lý do dùng thêm thành phần hoặc dừng ở 3NF.
- *4NF khác BCNF ở đâu?* BCNF xét PTH; 4NF xét phụ thuộc đa trị. R(MaSP, DuongDan, MaTS) toàn khóa nên đạt BCNF nhưng ảnh và thông số độc lập nên không đạt 4NF.
- *Cải tiến này có làm chậm truy vấn không?* Thêm phép nối (CHITIETTRA với HOSODOITRA, PHIEUBAOHANH với CHITIETDONHANG); chưa đo hiệu năng nên không khẳng định.
