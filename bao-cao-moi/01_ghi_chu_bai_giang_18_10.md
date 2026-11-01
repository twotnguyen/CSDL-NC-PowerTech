# Ghi chú bài giảng `Bai giang CSDLNC-18-10` (đọc ngày 24/10/2026)

Nguồn: `CSDL-NC/bai-giang/Bai giang CSDLNC-18-10.md` (đây là bản duy nhất, hiện hành). Các hình trong bản `.md` đã bị cắt (ảnh base64), nên đề của một số bài (bài về nhà phủ tối thiểu, đề bảo toàn thông tin) chỉ còn lời giải; muốn đọc đề phải mở `.docx`.

Phần (a) là nội dung bài giảng; phần "Kiểm lại" là kết quả tôi tính lại bằng script (`scratchpad/kiem_tra_bai_giang.py`), theo yêu cầu của AGENTS.md rằng bài giảng có thể sai.

## 1. Nội dung bài giảng, theo thứ tự trong buổi

1. **Khái niệm và ký hiệu:** Q(A₁…Aₙ), Q⁺, ‖Q‖ (tân từ), q (bộ), siêu khóa; phép chiếu Π_X(Q) = Q[X] ↔ `select distinct`; phép chọn Q_{điều kiện}[X] ↔ `where`. Một bảng có nhiều siêu khóa; chọn một làm PK, **ưu tiên ít thuộc tính nhất, đơn giản nhất** (ví dụ thay "HoLot, Ten, NTNS, Phai, DT" bằng MSSV).
2. **Tìm khóa:** thuật toán N, M, bảng `Mᵢ | Kᵢ = N ∪ Mᵢ | Kᵢ⁺`. Ví dụ R(ABCDEGH), F = {B→A, DA→CE, D→H, GH→C, AC→D}: N = {B,G}, M = {A,C,D,H}, ba khóa BGH, BGD, BGC. Chọn một khóa làm PK khi cài đặt.
3. **Ba loại thực thể** (ôn tập cho vai BA/DBA/DA/Tester):
   - **Cơ bản:** nguồn tài nguyên của hệ thống, ổn định cao, có trước khi tin học hóa, thường không có thuộc tính thời gian (nếu có thì chỉ là ngày sinh, ngày tạo, ngày đưa vào sử dụng), số lượng ít đổi. Ví dụ: Phòng học, Môn học; Sản phẩm/Mặt hàng, Loại hàng; Sách, Thể loại, Chức vụ.
   - **Đối tượng ngoài:** con người hoặc tổ chức. Ví dụ: SV, GV, Khoa/Viện/Phòng ban; Khách hàng, Nhân viên; Độc giả, NXB, Thủ thư.
   - **Nghiệp vụ:** sinh ra khi hệ thống vận hành, luôn có thuộc tính thời gian, số mẫu tin tăng dần. Ví dụ: Phiếu đăng ký môn học, Hóa đơn (ngày bán), Phiếu nhập (ngày nhập), Phiếu mượn, Phiếu trả, Phiếu phạt, Thẻ độc giả, Phiếu nộp lệ phí.
   - Thứ tự làm: xác định ba loại thực thể → thuộc tính → phụ thuộc hàm của từng loại → khóa.
4. **Phụ thuộc hàm** là *quy tắc do hệ thống quy định*; khóa tìm từ tập PTH.
5. **Phủ tối tiểu**, ba bước: B1 vế phải một thuộc tính; B2 chỉ còn PTH đầy đủ (không thừa vế trái, chỉ xét PTH vế trái từ 2 thuộc tính); B3 loại PTH dư thừa. Một F có thể cho nhiều phủ (ví dụ 2: G₁ và G₂ khác nhau, đều đúng).
6. **Dạng chuẩn** (cách dạy):
   - DC1: thuộc tính đơn. Cách thử bằng truy vấn: nếu phải `like N'%Mỹ'` hay `like N'%Hoàng%'` để lọc theo một phần của `HoTen` thì `HoTen` là thuộc tính kép → tách `HoLot`, `Ten`.
   - DC2: không phụ thuộc một phần vào khóa. DC3: không phụ thuộc bắc cầu vào khóa. BC: vế trái mọi PTH không hiển nhiên chứa khóa.
   - **"DC3 là dạng chuẩn tối thiểu của lược đồ CSDL"** (để cài đặt).
   - Bài tập mẫu 1–5 (xem mục 3 dưới).
7. **Kiểm tra phân rã:** F' = ∪Fᵢ; bảo toàn PTH khi (1) ∀f' ∈ F'\F: f' ∈ F⁺ và (2) ∀f ∈ F\F': f ∈ F'⁺. Bảo toàn thông tin bằng bảng a/b: chọn dòng có ít ô b nhất để biến đổi; tìm PTH có vế phải là cột cần đổi và vế trái tại hai dòng đã trùng "a". Chiếu PTH lên Qᵢ lấy từ F⁺, không chỉ từ F.
8. **Chuẩn hóa ba cách:** phân rã (Delobel; B1 bỏ PTH có VT ∪ VP = Q⁺; **ưu tiên chọn PTH gây xấu: vế trái không chứa khóa**), tổng hợp (B1 phủ tối thiểu, B2 nhóm theo vế trái, B3 gộp các nhóm có vế trái phụ thuộc lẫn nhau, B4 tạo quan hệ), tổng hợp cải tiến (B5 tìm khóa, B6 thêm Q'(K) nếu không quan hệ nào chứa khóa). Ví dụ Logistics Q(MsKH, TP, CTyVC, MsHH, SL) và Q(MAKH, TENKH, MAHD, NGAYHD, MAHG, TENHG, SOLG, DG); đề yêu cầu làm đủ ba cách và chứng minh bảo toàn thông tin, bảo toàn PTH.
9. **Chưa dạy:** DC4 (bài về nhà "coi trước DC4"), đồ thị quan hệ, con đường truy xuất, SQL cho đường truy xuất. Phần này lấy từ giáo trình và `Do thi quan he.pptx`.

## 2. Điểm cần chuyển thành quyết định cho báo cáo mới

1. **`HoTen` có tách không.** Bài giảng dùng chính `SV(MSSV, HoTen)` làm ví dụ vi phạm DC1 và sửa thành `HoLot, Ten`. Báo cáo cũ (`bao-cao/QUYET_DINH.md` mục 4) đã chọn *giữ* `HoTen` là một thuộc tính. Hai điều này trái nhau; giảng viên dễ hỏi khi bảo vệ. Cần Twot quyết định (xem hộp câu hỏi cuối lượt).
2. **Phép thử DC1 bằng truy vấn:** cột nào PowerTech phải lọc theo một phần (họ tên, địa chỉ gộp, mô tả) thì xét là thuộc tính kép.
3. **Ví dụ thực thể của giảng viên** (mục 1.3) là chuẩn phân loại: *Chức vụ* là cơ bản; *NXB* là đối tượng ngoài (tổ chức); *thẻ độc giả* là nghiệp vụ. Dùng làm điểm đối chiếu khi phân loại Coupons, UserAddresses, Carts ở mục 2.
4. **Làm đủ ba cách** (phân rã, tổng hợp, tổng hợp cải tiến) và chứng minh cả bảo toàn thông tin lẫn bảo toàn PTH cho từng quan hệ cần chuẩn hóa; chiếu PTH từ F⁺.

## 3. Kiểm lại: chỗ lời giải trên lớp không khớp định nghĩa

Đã tính lại bằng bao đóng; xem các số liệu trong script. Mỗi chỗ nên trình bày phép kiểm tra cho Twot và gợi ý hỏi lại giảng viên, không ghi "thầy sai" trong báo cáo.

| # | Chỗ trong bài giảng | Bài giảng ghi | Tính lại | Kết luận |
|---|---|---|---|---|
| A | Bài tập 3: Q(ABCD), F = {AB→C, D→B, C→ABD} | Khóa {C}; đạt DC3; không đạt BC vì "AB→C và D→B có vế trái không chứa khóa" | Khóa: **C, AB, AD**; AB là khóa nên AB→C không vi phạm; chỉ D→B vi phạm BC (B là thuộc tính khóa nên vẫn đạt DC3) | Kết luận 3NF, không BCNF đúng, nhưng thiếu 2 khóa và lập luận BC sai |
| B | Bài tập 4: Q(ABCDEI), F = {ACD→EBI, CE→AD} | Không đạt BC vì C là một phần của khóa | Khóa: **CE, ACD**; vế trái ACD→EBI là khóa, CE→AD là khóa | **Đạt BCNF**, bài giảng kết luận sai |
| C | Ví dụ bảo toàn PTH: F = {A→C, C→A, D→C, BD→A}; Q₁(AB), Q₂(ACD), Q₃(BCD) | Không bảo toàn vì BD→A ∉ F'⁺ (nhưng chính dòng trên đã viết D→A ∈ F'⁺) | BD⁺ theo F' = {A→C, C→A, D→C} chứa A; F' ≡ F | **Bảo toàn PTH**; ngoài ra F₂ (chiếu lên ACD) thiếu D→A |
| D | Phủ tối thiểu ví dụ 3 bước: F = {AB→C, AB→D, B→C, C→D} | "Thừa B": G = {A→C, A→D, B→C, C→D} | Vì B→C đã có, phải bỏ **A** (không phải B): AB→C thành B→C. G của bài giảng **không tương đương** F (A⁺ = A theo F) | Phủ đúng: {B→C, C→D} |
| E | Logistics, tổng hợp: F' = {MsKH→TP, MsKH,MsHH→SL, TP→CtyVC} | Không bảo toàn PTH vì chỉ có f2 | f2: MsKH→CtyVC suy ra từ f1 và f4; F' ≡ F | **Bảo toàn PTH** (giáo trình cũng ghi vậy) |
| F | Tổng hợp MSCD: nhóm F₃ (CD,MSSV→HG) và F₄ (MSCD,HG→MSSV) | Để thành hai quan hệ Q₂, Q₃ riêng | CD,MSSV ↔ MSCD,HG phụ thuộc lẫn nhau → theo B3 **phải gộp**, giáo trình ghi Q₃₄(CĐ, MSSV, MSCD, HG) | Gộp F₃₄ |
| G | Tổng hợp ví dụ 3: Q(ABCD) | Q₃₄(A,B,C,D) với F₃₄ = {BC→D, AD→B} có khóa ABC, ACD → "DC1" | Theo F đầy đủ, khóa **AB, AD, BC, CD**; Q₃₄ đạt **3NF** (không BCNF vì A→C); thuật toán tổng hợp luôn cho DC3 | Bài giảng chỉ xét một phần F nên ra DC1 |
| H | Tìm khóa R(ABCDEGH) | 14 siêu khóa | Khóa BGH, BGD, BGC đúng. Số siêu khóa là **28**: 14 tập có dạng N ∪ Mᵢ, mỗi tập thêm hoặc không thêm E (thuộc tính đích) | Con số 14 chỉ đúng khi không đếm E |
| I | Đầu mục tìm khóa | "Có 24 bao đóng" cho 4 thuộc tính | 2⁴ = 16 tập con (kể cả ∅) | Ghi nhầm |

Những ý còn lại của bài giảng (bài tập 1, 2, 5; BTTT; ví dụ Q(ABC); ví dụ Q(MAKH…) cách 1) khớp khi tính lại, trừ một chỗ chưa chặt: lời giải *cách 1 phân rã* bài MAKH kết thúc ở `Q₂₂₂₂(MAHD, SOLG, DG)` bỏ mất MAHG nên không còn biết dòng hàng nào của hóa đơn (bài giảng tự nhận "lđ vô nghĩa"); cần chọn thứ tự PTH khác để giữ quan hệ (MAHD, MAHG, SOLG, DG).

## 4. Việc phải nhớ khi viết

- Mọi phép tính dạng chuẩn, khóa, phủ tối thiểu trong báo cáo phải tính lại bằng định nghĩa (đã có `bao-cao/tools/*.py` dùng được); không chép lời giải trên lớp.
- Khi báo cáo cần đúng "cách giảng viên làm" mà bài giảng sai (A–G), trình bày kết quả đúng kèm bước kiểm tra, để nếu giảng viên đối chiếu với đáp án lớp vẫn thấy lập luận rõ.
