# SỔ TAY TRA CỨU BÀI GIẢNG CƠ SỞ DỮ LIỆU NÂNG CAO

> Giảng viên: ThS. Võ Hoàng Khang (HUTECH). Cập nhật 01/11/2026 sau khi đối chiếu từng bài với slide xuất từ file `.ppt` gốc, với cả 29 ảnh trong `hinh_so_do/`, với PDF giáo trình và với ảnh nhúng trong hai file `.docx` (`Bai giang CSDLNC-18-10.docx`, `Do_thi_va_CDTX.docx`).
> Sổ tay này là **bản tóm tắt**, không thay slide. Khi cần trích định nghĩa vào báo cáo, mở `Bai N.md` đúng slide. Ký hiệu: `→` phụ thuộc hàm, `↠` phụ thuộc đa trị, `⋈` phép kết, `Q⁺` tập thuộc tính của Q, `X⁺_F` bao đóng, `‖Q‖` tân từ; `⊃` theo thầy nghĩa là "chứa" (có thể bằng).

## 0. Độ tin cậy của nguồn

| Nguồn | Dùng thế nào |
|---|---|
| `Bai N.md` (chuyển từ `.ppt`) | Nguồn chính. Chữ đã đối chiếu; ký hiệu bị mất trong file gốc có ghi chú `[Ghi chú]` |
| `hinh_so_do/*.png` (29 ảnh) | Hình và bảng mà `.md` không có. Đã xem đủ 29 ảnh (01/11/2026). `DANH_MUC_SO_DO.md` mô tả lệch ba ảnh, xem ghi chú dưới bảng |
| File `.ppt` gốc (13 bài) | Đã xuất sang PDF và đối chiếu các slide có hình hoặc chữ nghi ngờ. Dùng khi cần kiểm chứng `.md` |
| `Bai giang CSDLNC-18-10.md` | Ghi chép buổi 18/10, **có lỗi trong bài giải** (mục 5). Ảnh đề bài nằm trong `.docx` (7 ảnh), đã xem |
| `Do_thi_va_CDTX.docx` | 3 ảnh: ERD bảng đen, ERD Case Studio, **lời giải viết tay bài bóng đá** mà bản `.md` không có (mục 3, Bài 10–11) |
| `Do thi quan he.pptx` | Chỉ có bảng chữ, không ảnh. Bảng chưa điền hết, không khớp lược đồ slide 24 (mục 3) |
| Giáo trình `CSDL-NC-2015.md` | Lý thuyết đầy đủ nhưng **cũng có chỗ sai** (mục 5). Bản `.md` hỏng phần công thức và hình ở Bài 9–10; khi cần xem `.pdf`, ở Bài 9–10 lấy số trang in cộng 13 |
| `TH_PTTKHT_2022.md` | Hướng dẫn Case Studio và 8 đề bài tình huống. **Không có lý thuyết ERD**: thực thể và mối kết hợp xem giáo trình 2015 mục 13.2.3–13.2.4. `TH_PTTKHT_HDT_Final-2022.pdf` (không có `.md`) dùng cùng 8 đề, hướng dẫn Star UML, use case, activity, sequence |

Ghi chú khi đọc ảnh và `.ppt`:

- Bài 10 slide 16–17 **không có hình**, chỉ có chữ; bốn đồ thị chỉ được liệt kê bằng dòng chữ như `4 <- 2->3`.
- `Bai 9` slide 19 có hình chưa trích vào `hinh_so_do/`: hình 9.7 thêm cung đỏ 1→3 và mũi tên đỏ chỉ nút vào 2 để minh họa đồ thị thô.
- `DANH_MUC_SO_DO.md` mô tả lệch: ảnh `Bai3_Slide26` là **bảng tổ hợp tìm khóa**, không phải đồ thị bao đóng; ảnh `Bai9_Slide30` là ví dụ 3 nút chung, không phải CSDL quản lý dự án (hình 9.9 thật ở giáo trình trang in 70); ảnh `Bai11_Slide08` chỉ có chữ các câu c–g, không có đồ thị.
- `Bai 7.md` slide 7 chèn nhầm ảnh cây phân rã; ảnh này thuộc `Bai 7_Bo sung` slide 7.

## 1. Tài liệu yêu cầu của giảng viên (nơi nằm "hướng dẫn viết báo cáo")

Thư mục `CSDL-NC/yeu-cau-giang-vien/`:

| File | Nội dung | Vai trò |
|---|---|---|
| `Huong_dan_cach_viet_bao_cao_CSDLNC.md` / `.docx` | **Hướng dẫn cách viết báo cáo** (25 dòng). Hai danh sách: (a) mô tả đề tài → lĩnh vực tin học hóa → 3 loại thực thể + ERD có mối kết hợp và bản số → phụ thuộc hàm, phủ tối thiểu, khóa → dạng chuẩn từng loại thực thể → cải tiến bằng phân rã/tổng hợp ("phát hiện DC4 thì quá tốt, cộng điểm"), chứng minh bảo toàn thông tin và PTH → đồ thị và con đường truy xuất; (b) 8 mục: mô tả, 3 loại thực thể + thuộc tính, tập PTH, phủ tối thiểu, khóa, ERD, chuyển ERD sang quan hệ (**gạch chân liền khóa chính, gạch chân nét đứt khóa ngoại**), dạng chuẩn từng bảng → dạng chuẩn chung của lược đồ | Hướng dẫn cách viết bổ sung, dùng để hiểu cách trình bày; khi khác đề cương thì theo đề cương |
| `Cau truc bao cao mon CSDL Nang cao.md` / `.pptx` | **Đề cương bài tập lớn, 7 nội dung** (2 slide): mô tả bài toán; 3 loại thực thể và thuộc tính; PTH và khóa từng lược đồ; dạng chuẩn + phân rã/tổng hợp + bảo toàn; phụ thuộc đa trị → 4NF; đồ thị quan hệ + con đường truy xuất + ngữ nghĩa; SQL cho các truy xuất. Nhóm 1–3 sinh viên | **Yêu cầu chính của báo cáo** (mới nhất). File `.pptx` và `.md` cùng nội dung (đã đối chiếu: 2 slide, không ảnh) |
| `23DTHD5/6.xlsx - Sheet1.md` | Nhận xét của giảng viên cho từng nhóm | Học từ lỗi của nhóm khác. Nhóm 6 (PowerTech): "Bổ sung hình thức mua trực tiếp tại cửa hàng. Cơ chế bảo hành, đổi hàng… ra sao?" |
| `00_kinh_nghiem_viet_mo_ta_tu_D5_D6.md` | Kinh nghiệm rút từ nhận xét và báo cáo mẫu | Không phải quy định chính thức |

Khung 4 chương của báo cáo lấy từ `CSDL-NC/bao-cao-mau/BaoCaoCSDLNC_ThamKhao.md`/`.docx`. Giáo trình 2015 mục 12.2.3 còn đòi thêm ràng buộc toàn vẹn (đại số/SQL), mô hình xử lý, giao diện; đề cương 7 nội dung không liệt kê các phần này.

## 2. Mục lục nhanh

| Bài | File | Nội dung | Hình |
|:-:|---|---|---|
| 0 | `Bai 0` (9 slide) | Mục tiêu, nội dung 12 bài, 45 tiết, **50% kiểm tra + 50% bài tập lớn** | — |
| 1–2 | `Bai1_2` (25) | Chu kỳ sống CSDL: phân tích nhu cầu → quan niệm → logic → vật lý → thử nghiệm/khai thác | slide 4, 8, 12 |
| 3 | `Bai 3` (38) | Mô hình quan hệ, phụ thuộc hàm, Armstrong, bao đóng, khóa N–M, phủ tối thiểu, tính chiếu | slide 26 |
| 4 | `Bai 4` (37) | 1NF, 2NF, 3NF, BCNF, phụ thuộc đa trị, 4NF | slide 9, 11 |
| 5 | `Bai 5` (6) | Bài tập PTH, bao đóng, khóa, phủ tối thiểu, PTH chiếu, dạng chuẩn | — |
| 6 | `Bai 6` (18) | Tiêu chuẩn đánh giá lược đồ: bảo toàn PTH, bảo toàn thông tin (bảng a/b) | slide 16 |
| 7 | `Bai 7` (20) | Phân rã Delobel; tổng hợp Bernstein | — |
| 7+ | `Bai 7_Bo sung` (19) | Delobel + Rissanen, nguyên tắc chọn PTH, tổng hợp cải tiến (B5–B6), bài tập | slide 7 (cây phân rã) |
| 8 | `Bai 8` (8) | 6 bài tập phân rã/tổng hợp; slide 8: kiểm tra giữa kỳ | — |
| 9 | `Bai 9` (35); `Bai 8_Bo sung` là bản khác của cùng nội dung | Đồ thị, đồ thị con đường truy xuất (CĐTX), đồ thị quan hệ (ĐTQH), chuỗi kết | slide 7, 8, 11, 17, 21, 29–31, 33, 34 |
| 10 | `Bai 10` (25) | Thuật toán B1–B7 chuyển CSDL sang ĐTQH | slide 10, 11, 21, 23, 24 |
| 11 | `Bai 11` (9) | Bài tập CĐTX (6 bài) | slide 3–8 |
| — | `Bai giang CSDLNC-18-10` | Ghi chép buổi 18/10: 3 loại thực thể, khóa, phủ tối thiểu, dạng chuẩn, bảo toàn, chuẩn hóa 3 cách | ảnh trong `.docx` |
| — | `Do_thi_va_CDTX`, `Do thi quan he` | Bài tập 10 quan hệ, bài bóng đá 7 quan hệ, ERD bảng đen | ảnh trong `.docx` |

Bài 12 (hướng dẫn đồ án) không có file slide trong thư mục.

## 3. Nội dung từng bài

### Bài 0
Môn tiên quyết CSDL&QTCSDL → PTTKHT → CSDLNC. Nhóm thiết kế CSDL và thuyết trình. Mục tiêu: "CSDL tốt", phụ thuộc hàm, dạng chuẩn, bảo toàn thông tin và quy tắc quản lý, đồ thị quan hệ, con đường truy xuất.

### Bài 1–2: các giai đoạn thiết kế
- Tiêu chí CSDL hiệu quả (slide 5): không trùng lắp, nhất quán, dễ khai thác, dễ kiểm tra ràng buộc toàn vẹn, dễ nâng cấp. Slide 6: thời gian truy xuất, phục hồi, chi phí, bảo trì.
- Chu kỳ sống (slide 9–12): xây dựng = phân tích nhu cầu → quan niệm → logic → vật lý; thử nghiệm và khai thác = cài đặt chạy thử → khai thác → thích ứng nhu cầu mới.
- Phân tích nhu cầu (slide 13–15): bước khó nhất; phỏng vấn trực tiếp hoặc gián tiếp; hỏi ban giám đốc và các phòng ban.
- Quan niệm (slide 16–18): xác định nội dung dữ liệu và quan hệ giữa dữ liệu, chưa quan tâm cài đặt, loại bỏ dữ liệu thừa; chia nhu cầu thành mảng rồi tích hợp, lập từ điển dữ liệu và ràng buộc toàn vẹn.
- Logic (slide 19–20): thường dùng mô hình quan hệ; ở đây cân nhắc có cài đặt thông tin trùng lắp hay không theo hiệu quả xử lý.
- Vật lý (slide 21–24): chọn phần mềm, phần cứng, an toàn và phục hồi, danh mục quan hệ, chỉ mục, kích thước trang.
- **Không có** trong các slide này: quy ước gạch chân khóa (nằm ở hướng dẫn viết báo cáo) và lời dặn "mô tả bằng ngôn ngữ đời sống" (rút từ nhận xét D5/D6).

### Bài 3: phụ thuộc hàm
- Slide 4–9: thuộc tính (tên, kiểu, miền giá trị), Q(A₁…Aₙ), Q⁺, tân từ ‖Q‖, bộ, thể hiện, siêu khóa, khóa chỉ định, thuộc tính khóa, phép chiếu Π_X(Q) = Q[X].
- Slide 12–13: X → Y khi ∀q₁, q₂: q₁.X = q₂.X ⟹ q₁.Y = q₂.Y; PTH hiển nhiên khi Y ⊆ X; F chỉ ghi PTH không hiển nhiên.
- Slide 14: **LD1** phản xạ (Y ⊆ X ⟹ X→Y); **LD2** thêm vào (X→Y và Z ⊆ W ⟹ XW→YZ); **LD3** bắc cầu; dẫn suy: phân rã, hội, bắc cầu giả.
- Slide 15–19: F⁺; X⁺_F lặp đến khi không đổi; bài toán thành viên (kiểm tra X→Y ∈ F⁺ bằng Y ⊆ X⁺).
- Slide 20–24 (khóa): siêu khóa S → Q⁺; khóa chỉ định là siêu khóa tối thiểu; nếu đồ thị PTH không có chu trình thì khóa duy nhất. **N** = thuộc tính không nằm bên vế phải (chỉ ở vế trái hoặc không xuất hiện); **M** = ở cả hai vế. N⁺ = Q⁺ thì N là khóa duy nhất; ngược lại thử Kᵢ = N ∪ Mᵢ với mọi tập con Mᵢ ⊆ M, bỏ các Kᵢ chứa khóa đã tìm. Slide không nêu tập D (chỉ ở vế phải); D không thuộc khóa nào.
- Slide 27–33 (phủ tối thiểu): F ≡ G khi F⁺ = G⁺; G là phủ tối thiểu khi (1) vế phải một thuộc tính, (2) PTH đầy đủ (không thừa vế trái), (3) không PTH dư thừa. Ba bước b1–b3. Ví dụ F={A→B; B→A; B→C; A→C; C→A} có **hai** phủ tối thiểu khác nhau (slide 33): kết quả phụ thuộc thứ tự xét.
- Slide 34: tính chiếu (Q'=Q[W], W ⊃ X, W∩Y≠∅ thì Q' có X→(W∩Y)) và tính phản chiếu.
- Bài tập: slide 35–37 (xem lời giải đã kiểm ở mục 5).

### Bài 4: dạng chuẩn
- Slide 5–7: ví dụ QLHT(MsSV, Ten, NS, Phai, ĐC, MsLop, TenLop, MsMH, TenMH, Diem) với 5 PTH; dị thường sửa, xóa, thêm.
- **DC1** (slide 8–11): mọi thuộc tính đơn. Thuộc tính đơn: giá trị không là kết hợp nhiều thông tin có nghĩa khác nhau và hệ thống luôn truy xuất cả giá trị. Sửa: tách thuộc tính hoặc tách dòng.
- **DC2** (slide 12–18): đạt DC1 và mọi thuộc tính không khóa phụ thuộc đầy đủ vào khóa. Khóa chỉ một thuộc tính thì đạt DC2. Thuật toán: tìm mọi khóa, tính bao đóng mọi tập con thật sự của khóa; có bao đóng chứa thuộc tính không khóa thì không đạt.
- **DC3** (slide 19–22): đạt DC2 và không phụ thuộc bắc cầu. Thuật toán (slide 21): mọi X→A (vế phải một thuộc tính, A∉X) có X là siêu khóa **hoặc** A là thuộc tính khóa. Ví dụ TK(MSHH, MSKho, TenKho, SLT) đạt DC3 nhưng còn trùng lắp.
- **BCK/BC** (slide 23–24): mọi X→A không hiển nhiên có X là siêu khóa.
- **Phụ thuộc đa trị** (slide 25–30): X↠Y khi tập giá trị Y ứng với x không phụ thuộc Z; hiển nhiên khi X∪Y = Q⁺; nếu X↠Y thì Q = Q[X,Y] ⋈ Q[X,Z]. Luật dẫn: bù, thêm vào, bắc cầu, X→Y ⟹ X↠Y, LD5.
- **DC4** (slide 31–33): xem mục 4 (ba định nghĩa khác nhau). Ví dụ LICHTHI(Ngay, Giờ, Phong, Mon) với Mon↠Phong tách thành LT1(Mon, Phong) và LT2(Ngay, Gio, Mon).
- Slide 34–35: nên chọn DC3 hay BCK/DC4 tùy khối lượng dữ liệu, tần suất cập nhật, chi phí kiểm tra ràng buộc. Giáo trình 4.7: dạng chuẩn của lược đồ là dạng chuẩn thấp nhất trong các quan hệ.

### Bài 5: bài tập
BT1 Q(ABCD) F={A→C; D→C; BD→A} tìm khóa; BT2 Q(ABCDEHK); BT3 Q(ABCDEG) (a: {BD}⁺, b: khóa); BT4 Q(ABCEGH) (a: AB→GH?, b: khóa); BT5 phủ tối thiểu (a, b); BT6 PTH chiếu lên Q₁(AB), Q₂(ACD), Q₃(BCD); BT7 Q(ABCD) F={A→B; B→C; A→D; D→C}, C={AB, AC, BD}: chiếu, bảo toàn thông tin, bảo toàn PTH; bài dạng chuẩn BT1: phủ tối thiểu, phân rã DC3 bảo toàn PTH, PTH chiếu, bảo toàn thông tin.

### Bài 6: đánh giá lược đồ
- Hai cách bắt đầu: C = {⟨Qᵢ, Fᵢ⟩} theo kinh nghiệm, hoặc một quan hệ phổ quát Q₀ (slide 4–5). Hai tiêu chuẩn: dạng chuẩn cao nhất và tương đương lược đồ ban đầu (slide 6–8).
- **Bảo toàn PTH** (slide 9–10): (i.1) ∪Qᵢ⁺ = Q⁺, (i.2) (∪Fᵢ)⁺ = F⁺. Cách chứng minh: đặt F' = ∪Fᵢ; ∀f' ∈ F'∖F: f' ∈ F⁺ **và** ∀f ∈ F∖F': f ∈ F'⁺ (tính bao đóng theo F').
- **Bảo toàn thông tin** (slide 11–16), bảng a/b: cột là thuộc tính Q, dòng là Qᵢ; ô là aⱼ nếu Aⱼ ∈ Qᵢ, ngược lại bₖ. Với f: X→Y, chọn hai dòng trùng ở X; nếu một ô cột Y đã là a thì ô kia đổi thành a. Lặp đến khi có dòng toàn a (bảo toàn) hoặc không còn đổi (không bảo toàn). Hình slide 16: Q₁(MSCD,CD), Q₂(MSCD,HG), Q₃(CD,HG,MSSV): dùng f2 (CD→MSCD) cho dòng Q₁, Q₃ thì b₅ thành a₁ và Q₃ toàn a.
- Slide 17: biểu diễn trọn vẹn = đồng thời bảo toàn thông tin và PTH.

### Bài 7 và Bài 7 bổ sung: chuẩn hóa
- **Phân rã (Delobel, 1973)** — slide 5: nếu X→A ∈ F⁺ và X∪A ⊂ Q⁺ thật sự thì tách thành **Q₁(X, A)** và **Q₂(Q⁺∖A)**, bảo toàn thông tin. Bản `Bai 7_Bo sung` slide 3 phát biểu tương đương: R₁ = Π_AB(R), R₂ = Π_AC(R) khi A→B.
- Thuật toán (Bài 7 slide 6–7): B1 bỏ khỏi F các PTH có VT∪VP = Q⁺; B2 nếu F* = ∅ thì dừng (thêm Q vào C), ngược lại chọn f, tách, đệ quy Q₁ và Q₂.
- Bài 7 bổ sung slide 4–5: chỉ chọn PTH X→A **vi phạm BCNF** (X không là siêu khóa). Slide 10, ba nguyên tắc **không chọn**: (1) PTH có vế trái là siêu khóa; (2) PTH có vế phải là vế trái của PTH khác; (3) PTH mà mất vế phải làm mất PTH không suy lại được.
- **Rissanen (1977)**: tách ρ(R₁, R₂) không tổn thất ⟺ R₁∩R₂ → R₁∖R₂ **hoặc** R₁∩R₂ → R₂∖R₁. Slide 3 viết vế thứ hai là `R₂ ∪ R₁ → R₂∖R₁` (gõ nhầm ∪ thay ∩).
- Nhận xét: luôn bảo toàn thông tin, đạt BCK, **có thể mất PTH**, kết quả phụ thuộc thứ tự chọn PTH. Ví dụ Q(MsKH, TP, CTyVC, MsHH, SL) tách thành Q₁(TP,CTyVC), Q₂₁(MsKH,TP), Q₂₂(MsKH,MsHH,SL). Hình cây slide 7 (BS): R(CTHRSG), F={C→T; CS→G; HR→C; HS→R; HT→R}, khóa HS, tách thành R1(CSG), R21(CT), R221(CHR), R222(CHS); **HT→R bị mất** (đã kiểm bằng bao đóng), đúng nguyên tắc (3).
- **Tổng hợp (Bernstein)**: B1 phủ tối thiểu; B2 nhóm PTH cùng vế trái; B3 gộp nhóm có vế trái phụ thuộc lẫn nhau (Kᵢ→Kⱼ và Kⱼ→Kᵢ); B4 mỗi nhóm thành một quan hệ. Kết quả đạt DC3, bảo toàn PTH, có thể không bảo toàn thông tin (ví dụ Q(ABCD) F={AB→C; C→B} thiếu D).
- **Tổng hợp cải tiến** (BS slide 15): thêm B5 tìm mọi khóa của Q; B6 nếu không Qᵢ nào chứa khóa của Q thì thêm Q'(Kᵢ).
- Bảng so sánh giáo trình 7.4: phân rã → DC4 hoặc BCK, bảo toàn thông tin có, bảo toàn PTH **không**, không còn trùng lắp; tổng hợp (có cải tiến) → DC3, thông tin có, PTH có, **có thể còn trùng lắp**.

### Bài 8: bài tập (làm ở nhà, thay nhau sửa trên lớp)
BT1 Q(ABCD) F={A→C; D→C; BD→A}, phân rã Q₁(AB), Q₂(ACD), Q₃(BCD): khóa, dạng chuẩn, PTH chiếu, BTTT, BTPTH; BT2 bán hàng Q(MAKH…DG); BT3 Q(MsKH, TP, CTyVC, MsHH, SL); BT4 Q(CV, VP, CĐ, SL, CP, L) với hai phân rã C₁, C₂; BT5 Q(Tàu, LoạiTàu, VậnChuyển, LôHàng, Cảng, Ngày); BT6 thời khóa biểu lý thuyết (tự xác định PTH). Slide 8: kiểm tra giữa kỳ, nộp lên Classroom 9h00, nộp trễ bị trừ điểm.

### Bài 9: lý thuyết đồ thị quan hệ
- Slide 4–5: phép kết là thao tác chính; chỉ mục (khóa) cần đủ và vừa; đồ thị làm nổi bật thuộc tính chung (cơ sở của phép kết).
- Slide 6–11: đồ thị có hướng/vô hướng, cung kề cận, khuyên, đường đi (vô hướng), mạch đi (có hướng), chu trình, dòng có gốc.
- **ĐT CĐTX** (slide 12–15) = (N, C, R, Cđ, f, g, h, i, j): f nút → quan hệ nút; g cung → quan hệ cung (tối đa hai cung ngược chiều cùng quan hệ cung); h cung ↔ con đường truy xuất; **i: (m, A, M)** số bộ tối thiểu, trung bình, tối đa; j nút vào. Cung → truy xuất **1 bộ**, cung ↠ truy xuất **n bộ**. Hình 9.7 (slide 17) và slide 34 xác nhận nhãn: cung đơn `(1,1,1)`, cung kép `(1,-,n)`; nút vào vẽ mũi tên rỗng chỉ vào.
- **ĐT CĐTX thô** (slide 18): (1) giữa hai nút có một cung thì có cung ngược chiều; (2) mọi nút là nút vào.
- **ĐTQH** (slide 22–24) = (N_Q, C_Q, R_Q, f_Q, g_Q, k_Q), k_Q = 1 cung có hướng, 0 vô hướng. Điều kiện đúng: f_Q(N_Q) ∪ g_Q(C_Q) = R_Q (slide ghi thiếu chỉ số Q).
- Biến đổi hai chiều (slide 25–29): cặp cung ngược c, c' cùng quan hệ cung: nếu max(c) > 1 **và** max(c') > 1 thì cung vô hướng (k_Q = 0); nếu max(c) = 1 **hoặc** max(c') = 1 thì cung có hướng (k_Q = 1) theo chiều có max = 1. Chiều ngược lại ở slide 28 dùng cùng quy tắc. Hình slide 29 xác nhận: cặp (1,1,1) và (1,-,n) thành cung 1→2, cặp (1,-,n) và (1,-,n) thành cung vô hướng 3—4. **Chỉ dùng `Bai 9` slide 26, 28**: giáo trình 9.5 và `Bai 8_Bo sung` slide 25, 27 viết sai (mục 5, #16–17).
- Giáo trình trang in 70: cung vô hướng n_i—n_j đổi được thành nút N_ij với hai cung có hướng tới N_i và N_j; đây là chiều ngược của B7 Bài 10.
- Chuỗi kết (slide 31–33): ρ = (AX)⋈(AB)⋈(BY)⋈(BC)⋈(CZ) cài đặt được trên (a), (b), (d), không trên (c). Slide 32: bài tập vẽ ĐT CĐTX cho đơn hàng – giao hàng (một giao hàng tối đa 9 chi tiết). Slide 34 có ghi chú đỏ: GiaoHang(SoGH, NgGH) **thiếu SoDH** nên không biết giao cho đơn nào (khác ví dụ Bài 10 có SoDH).

### Bài 10: thuật toán chuyển CSDL sang ĐTQH (B1–B7)
Input: phân rã C = {Qᵢ} có tập khóa. Mọi khóa của một quan hệ có vai trò ngang nhau (chọn khóa ưu tiên ở giai đoạn vật lý).

| Bước | Nội dung |
|---|---|
| **B1** | Biến C thành phân rã đồng nhất C_d: 1.1 hai quan hệ có Kᵢ ↔ Kⱼ thì gộp; 1.2 nếu Qᵢ⁺ chứa một khóa của Qⱼ thì phải chứa mọi khóa của Qⱼ |
| **B2** | Mỗi Qᵢ là một nút Nᵢ, Q_Nᵢ = Qᵢ |
| **B3** | **Nút bản lề:** Qᵢⱼ = Qᵢ ∩ Qⱼ (chỉ tính thuộc tính khóa); nếu không quan hệ Qₕ nào có khóa trùng khóa của Qᵢⱼ thì tạo nút bản lề Q_bl = KQᵢⱼ |
| **B4** | Bảng 6 cột: PTH(Nᵢ) = {Nⱼ: Qᵢ⁺ ⊃ KQⱼ⁺}; PTH_Thừa = {Nⱼ ∈ PTH: ∃Nₕ ∈ PTH, KQₕ⁺ ⊃ KQⱼ⁺}; Lồng_khóa(Nᵢ) = {Nⱼ: KQᵢ⁺ ⊃ KQⱼ⁺}; LK_Thừa tương tự; **Cung(Nᵢ) = (PTH − PTH_Thừa) ∪ (LK − LK_Thừa)**; tạo cung Nᵢ→Nⱼ với Qᵢⱼ = Qᵢ[KQᵢ⁺ ∪ KQⱼ⁺] |
| **B5** | Hủy nút bản lề thừa: Q_k chỉ có khóa, **chỉ một cung vào** → nhập vào nút cha, hủy cung |
| **B6** | Mịn hóa quan hệ nút: bỏ khỏi Qᵢ⁺ các thuộc tính khóa của Qⱼ (Nⱼ ∈ Cung(Nᵢ)) mà không là khóa của Qᵢ |
| **B7** | Cung vô hướng: nút N_k có Q_k⁺ = KQ_k⁺ (không thuộc tính không khóa), **đúng 2 cung ra, không cung vào**, KQ_k = KQᵢ ∪ KQⱼ → thay bằng cung vô hướng Nᵢ—Nⱼ, hủy N_k. Toàn cung vô hướng thì không làm B7 |

- Ví dụ 5 bảng DDH, MatHang, CTDH, GiaoHang, CTGH (slide 8–13): không có nút bản lề; Cung(CTGH) = {2, 3, 4}; hai mạch 5→4→1 và 5→3→1 dùng để kiểm tra GiaoHang của CTGH phải cùng đơn với CTDH.
- Slide 14: biến đổi ngược C₁ = {Qᵢ} ∪ {Qᵢⱼ} để kiểm tra tương đương (BTTT và BTPTH).
- Trường hợp 1 (slide 15–17): bốn cách biểu diễn ĐTQH; **ĐT 1 chặt chẽ nhất** (không có PTH bắc cầu) và là kết quả của thuật toán. Slide ghi ĐT 1 là `4 <- 2->3`, giáo trình ghi `4 <- 1->3 (Rbtv: 3,4->2)`. **Kết quả tự tính, chưa phải đáp án của thầy:** chạy B4 cho Cung(1) = {2}, Cung(2) = {3, 4}, tức đồ thị 1→2, 2→3, 2→4, khớp slide (dòng chữ của slide không liệt kê 1→2). Theo slide (mục 5, #18).
- Trường hợp 2 (slide 18–19): do lồng khóa CDE ⊃ CD ⊃ C mất cung; khi cài đặt **chọn khóa ưu tiên** sao cho không mất cung.
- Bài tập 1–3 (slide 20–24). Khóa gạch chân trong ảnh slide 24: Q₁(**AB**X₁), Q₂(**A**X₂), Q₃(**ABC**X₃DEG), Q₄(**BDE**X₄), Q₅(**CEG**X₅), Q₆(**CE**X₆), Q₇(**EH**X₇), Q₈(**H**X₈), Q₉(**HG**), Q₁₀(**ABCH**). **Kết quả tính theo thuật toán (đã chạy, chưa phải đáp án của thầy):** B3 tạo 4 nút bản lề Q₁₄(B), Q₃₅(C), Q₄₅(E), Q₅₉(G); Cung: 1→{2, 14}; 3→{1, 4, 5, 35}; 4→{14, 45}; 5→{6, 59}; 6→{35, 45}; 7→{8, 45}; 9→{8, 59}; 10→{3, 8}; B5 giữ cả 4 nút bản lề; B7 hủy **Q₉ và Q₁₀** (cung vô hướng Q₅₉—Q₈ và Q₃—Q₈). Q₄ **không** hủy được vì có thuộc tính không khóa X₄ và KQ₄ = BDE ≠ B ∪ E. Lời giải trong ghi chép lớp hủy cả Q₄ (mục 5).

### Bài 11: bài tập con đường truy xuất
Đọc đồ thị trong ảnh: giáo trình 11.5 quy ước quan hệ có 2 khóa thì khóa thứ nhất gạch chân, khóa thứ hai in đậm (BT5: Q₂ có khóa MP và NE, Q₅ có khóa P và BA). BT5c có 4 nút vào 1, 2, 3, 4; nút 5 không có nút vào.

BT1 C₁={Q₁(ABCX); Q₂(BCY); Q₃(CZ)}; BT2 phân rã 10 quan hệ (trùng Bài 10 BT3); BT3, BT4 chỉ ra 2 chỗ trùng lắp trong ĐTQH và định nghĩa ĐTQH tương đương không trùng lắp; BT5 (11 nút): trích F_Q, dạng chuẩn, SQL liệt kê A[MNP], khai báo SQL cho ĐT CĐTX, cải tiến để đạt 3 tiêu chuẩn và cho phép tạo Q[DP] không qua Q[DMNPE]; BT6 (10 nút AIMNLTVXYZ): a–e và **g** (không có f), gồm đề nghị ĐT CĐTX thỏa 3 yêu cầu (kiểm tra PTH thuận tiện nhất, truy xuất trực tiếp mọi nút, truy tìm nhanh các bộ Q[aMNZ]…) và khai báo cấu trúc vật lý.

### Ghi chép buổi 18/10
- Siêu khóa, phép chiếu = `select distinct`, phép chọn = `where`; ưu tiên PK ít thuộc tính nhất.
- Tìm khóa: ví dụ R(ABCDEGH) cho 3 khóa BGH, BGD, BGC.
- **Ba loại thực thể:** cơ bản (tài nguyên có trước, ổn định, thường không có thuộc tính thời gian), đối tượng ngoài (con người hoặc tổ chức), nghiệp vụ (sinh ra khi vận hành, luôn có thuộc tính thời gian, số lượng tăng dần). Ví dụ thư viện: cơ bản = Sách, Thể loại, Chức vụ; đối tượng ngoài = Độc giả, NXB, Thủ thư; nghiệp vụ = Phiếu mượn, trả, phạt, Thẻ độc giả.
- Phủ tối thiểu 3 bước; DC1 thử bằng truy vấn (`like N'%Mỹ'` nghĩa là HoTen là thuộc tính kép → tách HoLot, Ten); DC2, DC3, BC; "DC3 là dạng chuẩn tối thiểu của lược đồ".
- Bảo toàn PTH, bảo toàn thông tin, chuẩn hóa bằng phân rã, tổng hợp, tổng hợp cải tiến (**yêu cầu làm đủ ba cách** cho bài MAKH…).

### Ghi chép Đồ thị và CĐTX (`Do_thi_va_CDTX`)
- ERD bảng đen (ảnh 1): THẺ (1,1) — Của — KHÁCH HÀNG (0,1); KHÁCH HÀNG (1,n) — Có — HÓA ĐƠN (1,1); HÓA ĐƠN (1,n) — CTHD(SL, Giá, Thành tiền) — MẶT HÀNG (1,n). **Bản số (min,max) ghi cạnh thực thể, cho biết mỗi thể hiện của thực thể đó tham gia mối kết hợp bao nhiêu lần**; CTHD là mối kết hợp có thuộc tính. Ảnh 2 là bản Case Studio (PK, FK, PFK).
- Bài tập bóng đá 7 quan hệ (DOI, TRANDAU, BANG_TDAU, CAUTHU, BANTHANG_CAUTHU, CTIET_TRANDAU, DUDOAN_KQTD): **ảnh 3 là lời giải viết tay** (B3 không tạo bản lề; bảng Q₅: PTH {2,4}, Cung {2,4}; Q₆: PTH {1,2,3,5}, PTH_Thừa {1}, LK {2,3,5}, Cung {2,3,5}; Q₇: Cung {6}). Bản `.md` chỉ có bảng gõ lại với Q₆, Q₇ có Cung {1,2}, **khác ảnh**, kèm câu "Xem và sửa bài giải của lớp 19DTJB1". Đề không ghi khóa nên chưa tính lại được; khi dùng nên theo ảnh viết tay.
- `Do thi quan he.pptx`: bảng 10 quan hệ chưa điền hết (hàng 6, 8, 9 trống) và hàng 4, 5 không khớp lược đồ slide 24 (Q₄ không chứa khóa AB của Q₁); không dùng làm đáp án.

## 4. Ba định nghĩa dạng chuẩn 4 trong tài liệu

| Nguồn | Định nghĩa |
|---|---|
| Bài giảng Bài 4 slide 31 | Đạt BCK và với mọi X↠Y không hiển nhiên thì X chứa một khóa của Q⁺∖Y, tức ∀A ∈ Q⁺∖Y: X→A ∈ F⁺ |
| Giáo trình 2015 mục 4.6.6 | Đạt BCK và **không có** phụ thuộc đa trị không hiển nhiên nào (chặt hơn) |
| `giao-trinh/Dạng chuẩn 4.md` | Đạt BCNF và mọi X↠Y không tầm thường có X là **siêu khóa** (định nghĩa chuẩn quốc tế). File này giống bản tóm tắt tự sinh, có LaTeX hỏng và lẫn 5NF, chỉ nên dùng để hiểu ý |

Khi viết báo cáo, nêu định nghĩa đang dùng. Với ca ảnh – thông số sản phẩm của PowerTech, R₂(MaSP, DuongDanAnh, MaTS) vi phạm 4NF theo cả ba định nghĩa.

## 5. Sai sót đã kiểm trong tài liệu

Tính lại bằng vét cạn tập con thuộc tính (độc lập với `bao-cao-moi/tools/fd.py`). Khi trình bày nên đưa phép kiểm, không viết "thầy sai".

| # | Chỗ | Tài liệu ghi | Tính lại |
|---|---|---|---|
| 1 | Bài 4 BT3: Q(ABCD), F={AB→C; D→B; C→ABD} | Khóa {C}; "AB→C, D→B vế trái không chứa khóa" | Khóa **C, AB, AD**; AB→C không vi phạm; chỉ D→B vi phạm BC (B là thuộc tính khóa) → **3NF, không BCNF** |
| 2 | Bài 4 BT4: Q(ABCDEI), F={ACD→EBI; CE→AD} | "Không đạt BC vì C là một phần của khóa" | Khóa **CE, ACD**; cả hai vế trái đều là khóa → **đạt BCNF** |
| 3 | Ghi chép 18/10 (cũng Bài 6 slide 10): F={A→C; C→A; D→C; BD→A}; Q₁(AB), Q₂(ACD), Q₃(BCD) | "Không bảo toàn PTH" vì BD→A ∉ F'⁺ (dòng trên đã viết D→A ∈ F'⁺) | BD⁺ theo F' chứa A → **bảo toàn PTH**; bảo toàn thông tin cũng đúng |
| 4 | Ghi chép 18/10: phủ tối thiểu của {AB→CD; B→C; C→D} (ảnh đề ở `.docx`) | AB→C "thừa B", G={A→C; A→D; B→C; C→D} | Phải bỏ **A** (B→C đã có), phủ đúng {B→C; C→D}; G của lớp không tương đương F (A⁺ = A theo F) |
| 5 | Ghi chép 18/10: Logistics, tổng hợp | F' = {f1, f3, f4} "không bảo toàn" vì thiếu f2 | f2: MsKH→CTyVC suy từ f1 và f4 → **bảo toàn PTH** |
| 6 | Ghi chép 18/10: tổng hợp MSCD | F₃ và F₄ thành hai quan hệ riêng | Hai vế trái CD,MSSV và MSCD,HG phụ thuộc lẫn nhau → B3 phải **gộp** (Bài 7 slide 16 gộp đúng) |
| 7 | Ghi chép 18/10 và BS slide 13: Q(ABCD) với A↔C, F₃₄={BC→D; AD→B} | Khóa ABC, ACD; "DC1" | Khóa **AB, AD, BC, CD**; Q₃₄ đạt **3NF**; Q₁(AC) có khóa A và C (không phải {AC}) |
| 8 | Ghi chép 18/10: R(ABCDEGH) | 14 siêu khóa | 3 khóa đúng; **28** siêu khóa (14 tập N∪Mᵢ, mỗi tập thêm hoặc không thêm E) |
| 9 | Ghi chép 18/10 | "Có 24 bao đóng" cho 4 thuộc tính | 2⁴ = 16 tập con |
| 10 | Ghi chép 18/10: Q(MAKH…DG), phân rã cách 1 | Q₂₂₂₂(MAHD, SOLG, DG), Q₂₂₁ lặp Q₂₁, F₂₂ chứa PTH có thuộc tính không còn trong Q₂₂ | Mất MAHG nên không biết dòng hóa đơn là hàng nào; cần chọn thứ tự PTH khác để giữ (MAHD, MAHG, SOLG, DG). Khóa của Q là {MAHD,MAHG} **và** {MAHD,TENHG} (ghi chép chỉ nêu một) |
| 11 | Giáo trình 7.3: Q(ABCD), F={AB→C; C→B} | Khóa {ABD} | Khóa **ABD và ACD** |
| 12 | Bài 7 bổ sung slide 3 | Rissanen: `R₂ ∪ R₁ → R₂∖R₁` | Dạng đúng `R₁ ∩ R₂ → R₂∖R₁` |
| 13 | Bài 4 slide 17 | PTH MsSV,MsMH→Diem gọi f4 | Slide 5 gọi là f5 |
| 14 | Bài 9 slide 24 | f(N) ∪ g(N) = R | Đúng ra f_Q(N_Q) ∪ g_Q(C_Q) = R_Q |
| 15 | Ghi chép Đồ thị và CĐTX, bài 10 quan hệ | Xóa Q₄, Q₉, Q₁₀ ở B7 | Theo B7 chỉ Q₉ và Q₁₀ đủ điều kiện (mục 3, Bài 10) |
| 16 | Giáo trình 9.5.1 (trang in 71), `Bai 8_Bo sung` slide 25 | Có hướng khi max(c) ≤ 1 **và** max(c') ≤ 1 | Cung 1–n có max = 1, max' = n nên không rơi vào nhánh nào. `Bai 9` slide 26 đúng: max(c) = 1 **hoặc** max(c') = 1 |
| 17 | Giáo trình 9.5.2 (trang in 72), `Bai 8_Bo sung` slide 27 | k_Q = 1 thì cả hai max > 1; k_Q = 0 thì có max ≤ 1 | Đảo ngược: k_Q = 1 là có hướng. `Bai 9` slide 28 đúng: k_Q = 0 thì cả hai max > 1; k_Q = 1 thì max(c) = 1 hoặc max(c') = 1 |
| 18 | Giáo trình 10.4.1 (trang in 83) | `DT 1: 4 <- 1->3 (Rbtv: 3,4->2)` | Bài 10 slide 16 ghi `4 <- 2->3`; B4 cho Cung(1) = {2}, Cung(2) = {3, 4}, khớp slide. Kết quả tự tính, chưa phải đáp án của thầy |
| 19 | Bài 9 slide 33 (viết tay) | Ghi "đường truy xuất thô" | Cung 4→1 và 5→2 không có cung ngược, chưa vẽ nút vào nên chưa thỏa định nghĩa thô (slide 18) |
| 20 | Bài 9 slide 34 | Q₃,₁(SoDH), Q₅₄(SoGH) | Theo B4 Bài 10, quan hệ cung gồm khóa của hai nút: Q₃₁(MaH, SoDH), Q₅₄(MaH, SoGH) như Bài 10 slide 11–12 |
| 21 | Bài 9 slide 20–21 | Đề có KetQua(MaSV, MaMH, Diem, KetQua), hình lại vẽ LichHoc(MaLop, MaMH) | Hình không khớp đề; làm bài cần hỏi lại thầy dùng lược đồ nào |
| 22 | Bài 11 slide 3 (BT3) | Nút 2 ghi Q₃(CY); cung 1→3 ghi Q₁₂, cung 1→2 ghi Q₁₃ | Nút 2 phải là Q₂(CY), và hai nhãn cung bị đảo chỉ số so với số nút |

Các kết quả khớp khi tính lại (dùng làm đáp án mẫu): Bài 3 BT1 khóa {BD}; BT2 khóa {ABH}; BT3 {BD}⁺ = ABCDEG, 7 khóa (AB, BC, BD, BE, CD, CE, CG); BT4 AB→GH đúng, khóa {AB}, đạt 2NF; Bài 3 slide 25 hai khóa BDEF, CDEF; Bài 4 BT1 (khóa AB, BC) chỉ đạt 1NF; BT2 (khóa G) đạt 2NF, không 3NF; Bài 5 BT6 chiếu Q₂(ACD) = {A→C; D→C; AD→C}, Q₃(BCD) = {D→C; BD→C}, BTTT và BTPTH đều **không** (mất BD→A); Bài 8 BT3 khóa {MsKH, MsHH} đạt 1NF; BT4 khóa {CĐ, CP}, phân rã C₂ bảo toàn thông tin nhưng **mất** CV→VP; BT5 khóa {NT, NV} (Ngày+Tàu, Ngày+VậnChuyển), C₁ bảo toàn cả thông tin lẫn PTH; giáo trình 15.1.1 R(ABCDEGH), F={B→A; C→D; BA→CE; DE→H; H→E}: khóa {BG}, phân rã {ABCEH, CD, DEH, BG} bảo toàn thông tin và PTH.

## 6. Tra cứu nhanh khi viết báo cáo PowerTech

Khung báo cáo hiện hành: 7 nội dung của đề cương, 4 chương (`bao-cao-moi/chuong/`).

| Cần làm | Xem |
|---|---|
| Mô tả nghiệp vụ, 3 loại thực thể (nội dung 1–2, chương 1) | `Bai1_2.md` slide 13–18; ghi chép 18/10 mục "3 loại thực thể"; giáo trình 13.2.3–13.2.4 (điều kiện của thực thể và mối kết hợp); `00_kinh_nghiem…`; nhận xét nhóm 6 |
| ERD, bản số | Lý thuyết: giáo trình 2015 mục 13.2.3–13.2.4. Mẫu: ảnh bảng đen trong `Do_thi_va_CDTX.docx` (bản số ghi cạnh thực thể), ví dụ và cách vẽ Case Studio trong `TH_PTTKHT_2022.md` |
| Tìm khóa N–M | `Bai 3.md` slide 20–25; ghi chép 18/10 (bảng Mᵢ) |
| Phủ tối thiểu | `Bai 3.md` slide 27–33; ghi chép 18/10 (**bỏ qua lời giải sai, mục 5 #4**) |
| Dạng chuẩn từng bảng, dạng chuẩn lược đồ | `Bai 4.md` slide 8–24, 35; giáo trình 4.7 |
| Phân rã, tổng hợp, so sánh | `Bai 7.md`, `Bai 7_Bo sung.md` (nguyên tắc chọn PTH slide 10); giáo trình 7.4 |
| Chứng minh bảo toàn | `Bai 6.md` slide 9–16 |
| Phụ thuộc đa trị, 4NF | `Bai 4.md` slide 25–34; mục 4 của sổ tay |
| Đồ thị quan hệ, CĐTX | `Bai 9.md` slide 12–28; `Bai 10.md` B1–B7 và slide 15–19; `Bai 11.md` |
| SQL theo con đường truy xuất | `Bai 9.md` slide 31–33; `Bai 11.md` BT5, BT6; giáo trình 15.1.2(b) |

Giáo trình 14.2 (sai sót thường gặp ở đề tài kinh doanh): chưa rõ quy mô (sỉ hay lẻ, một hay nhiều chi nhánh), chưa rõ phương thức thanh toán, báo cáo tồn kho theo kỳ không rõ ràng.
