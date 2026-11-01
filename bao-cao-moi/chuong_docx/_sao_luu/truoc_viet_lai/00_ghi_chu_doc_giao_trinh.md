# Ghi chú sau khi đọc `CSDL-NC/giao-trinh/` (24/10/2026)

Mục đích: giữ lại những điểm cần dùng khi viết báo cáo mới, để phiên sau không đọc lại cả giáo trình. Mọi điểm dưới đây (a) có trong tài liệu; chỗ ghi **[lưu ý]** là nhận xét của tôi khi đọc.

## 1. Đã đọc gì

| File | Mức đọc | Vai trò |
|---|---|---|
| `CSDL-NC-2015.md` (Văn Như Bích) | Đọc hết Bài 1–15 | Nguồn chuẩn: định nghĩa, thuật toán, yêu cầu bài tập lớn, sai sót thường gặp |
| `Do thi quan he.md/.pptx` (24/10) | Đọc hết, 1 slide | Bài tập của giảng viên: phân rã Q1…Q10, bảng PTH, PTH_T, LK, LK_T, cung (đúng Bảng 10.1 của Bài 10) |
| `Dạng chuẩn 4.md` | Đọc hết | Tóm tắt 4NF, có ví dụ giảng viên/môn/ngôn ngữ |
| `TH_PTTKHT_2022.md` | Đọc hết | 8 đề mô tả tình huống mẫu của giảng viên PTTK; cách viết mô tả và câu hỏi ERD |
| `cos135-…v2023.md` | Đọc Bài 4 (RBTV), 5 (PTH, khóa), 6 (dạng chuẩn, Delobel) | Bản nhập môn của cùng nội dung; chỉ dùng đối chiếu |
| `Thuc Hanh Quan Tri Co So Du Lieu.md` | Đọc Bài 2 (bán hàng) | Mẫu câu truy vấn, view, procedure, trigger kiểu giảng viên |
| `cos323-thuc-hanh-…md` | Không đọc | Mất dấu tiếng Việt, chỉ là thực hành SQL (CSDL địa lý); bỏ qua |

## 2. Định nghĩa và thuật toán theo giáo trình (dùng đúng ký hiệu này)

- **Ký hiệu:** Q(A₁…Aₙ), Q⁺, tân từ ‖Q‖, F_Q, F⁺, X⁺_F, siêu khóa, khóa chỉ định (candidate key). F chỉ ghi PTH không hiển nhiên.
- **Khóa (Bài 3.2.3):** N = thuộc tính không xuất hiện ở vế phải; M = xuất hiện ở cả hai vế. N⁺ = Q⁺ thì N là khóa duy nhất. Ngược lại lập bảng 2ᵐ dòng `Mᵢ | Kᵢ = N ∪ Mᵢ | Kᵢ⁺`; Kᵢ chứa khóa đã có thì là siêu khóa, loại. **[lưu ý]** AGENTS.md định nghĩa N hơi khác (có thêm "không xuất hiện trong PTH nào"); kết quả không đổi, nhưng thuộc tính không xuất hiện ở đâu cũng phải thuộc mọi khóa.
- **Phủ tối thiểu:** G là phủ của F, thỏa (i) vế phải một thuộc tính, (ii) mọi PTH đầy đủ, (iii) không PTH thừa. Thuật toán b1 tách vế phải; b2 thay PTH không đầy đủ bằng PTH đầy đủ; b3 loại PTH dư thừa. Kết quả phụ thuộc thứ tự xét; ví dụ giáo trình cho nhiều phủ.
- **Dạng chuẩn:**
  - DC1: mọi thuộc tính là thuộc tính đơn (ngày dương lịch xem là đơn).
  - DC2: DC1 và mọi thuộc tính không khóa phụ thuộc đầy đủ vào khóa; khóa một thuộc tính thì tự đạt DC2.
  - DC3: DC2 và không thuộc tính không khóa nào **phụ thuộc bắc cầu** vào khóa. PTBC có 4 điều kiện: X→Y, Y→A, Y↛X, A∉X∪Y.
  - BCK (BC): mọi PTH không hiển nhiên có vế trái chứa khóa (là siêu khóa).
  - DC4: BCK và mọi phụ thuộc đa trị X↠Y đều hiển nhiên, tức Q⁺ \ XY = ∅. Định nghĩa MVD đòi X∩Y = ∅, Z = Q⁺ \ {X,Y}.
  - Dạng chuẩn của lược đồ = thấp nhất trong các quan hệ.
  - **[lưu ý]** `cos135` định nghĩa DC3 và BC bắt đầu từ "Q ở DC1", còn `CSDL-NC-2015` bắt đầu từ DC2. Theo thứ tự ưu tiên của AGENTS.md (bài giảng > giáo trình), dùng bản của CSDL-NC-2015 và bài giảng.
  - Ví dụ chuẩn của giáo trình: `TK(MSHH, MSKho, TenKho, SLT)` đạt DC3 nhưng không đạt BCK vì có hai khóa {MSHH, MSKho}, {MSHH, TenKho} (Bài 4.4.2, 4.5.2).
- **Bảo toàn (Bài 6):** (i.1) ∪Qᵢ⁺ = Q⁺, không sót thuộc tính. Bảo toàn PTH: ∪Fᵢ⁺ = F⁺, chứng minh bằng F' = ∪Fᵢ, rồi ∀f' ∈ F'\F: f' ∈ F⁺ và ∀f ∈ F\F': f ∈ F'⁺. Bảo toàn thông tin: bảng a_j/b_k, áp PTH đến khi có dòng toàn a (b1–b4). "Biểu diễn trọn vẹn" = đồng thời bảo toàn thông tin và PTH.
- **Phân rã (Delobel, Bài 7.1):** f: X→A ∈ F⁺ với XA ⊊ Q⁺ thì tách Q₁(X,A), Q₂(Q⁺\A), luôn bảo toàn thông tin; kết quả BCK nhưng có thể mất PTH; thứ tự chọn PTH ảnh hưởng kết quả; ưu tiên PTH không chứa khóa hoặc PTH gây PTBC/không đầy đủ.
- **Tổng hợp (Bài 7.2, 7.3):** B1 phủ tối thiểu; B2 nhóm theo vế trái; B3 gộp nhóm có vế trái phụ thuộc lẫn nhau; B4 tạo quan hệ. Cải tiến: B5 tìm khóa, B6 nếu không quan hệ nào chứa khóa của Q thì thêm Q'(K). Kết quả DC3, bảo toàn PTH, bảo toàn thông tin sau cải tiến, nhưng có thể còn trùng lắp và không đủ khóa.
- **So sánh (Bảng 7.4):** phân rã – DC4/BCK, BTTT có, BTPTH không, không còn trùng lắp; tổng hợp – DC3, BTTT có, BTPTH có, có thể còn trùng lắp.
- **Đồ thị (Bài 9):** ĐTCĐTX = (N, C, R, Cđ, f, g, h, i, j); cung kèm (m, A, M); nút vào j(n)=1; "–" là trung bình chưa biết. ĐTCĐTX **thô**: cung có chiều ngược và mọi nút là nút vào. ĐTQH: một cung giữa hai nút, có hướng (k=1) hoặc vô hướng (k=0). Đổi ĐTCĐTX thô → ĐTQH: max>1 ở cả hai chiều thì vô hướng; max≤1 thì có hướng. Chuỗi kết được cài đặt trên đồ thị nếu có một "dòng có gốc" phủ đủ các quan hệ.
- **Thuật toán B1–B7 (Bài 10):** B1 phân rã đồng nhất (gộp khóa tương hỗ, quan hệ chứa khóa này phải chứa mọi khóa kia); B2 nút; B3 nút bản lề; B4 cung theo PTH(N), PTH_Thừa, LỒNG_KHÓA, LỒNG_KHÓA_THỪA, Cung(N); B5 hủy bản lề thừa; B6 mịn hóa; B7 cung vô hướng. Bài 10.4: một lược đồ cho nhiều đồ thị, thuật toán coi mọi khóa ngang nhau; khi cài đặt chọn khóa ưu tiên (đã dùng làm quy ước Q1 ở mục 10 cũ).
- **RBTV (cos135 Bài 4):** mỗi RBTV có bối cảnh, điều kiện, tầm ảnh hưởng (bảng +/− cho thêm, xóa, sửa); phân loại theo miền giá trị, liên thuộc tính, liên bộ, khóa ngoại, liên bộ liên quan hệ, chu trình. Dùng nếu viết phần RBTV tùy chọn.

## 3. Yêu cầu bài tập lớn và chấm điểm (CSDL-NC-2015, Bài 12–14)

- Nội dung (12.2.3): a đặc tả bài toán; b mục đích, tính cần thiết tin học hóa, phạm vi; c phân công nhóm; d thu thập thông tin (mẫu biểu, quy định, quy tắc quản lý; khảo sát thật hoặc giả lập); e mô hình quan niệm dữ liệu; f mô hình quan niệm xử lý; g mô hình quan hệ; h RBTV; i đồ thị quan hệ, con đường truy xuất và ý nghĩa; j khai thác bằng SQL theo ý nghĩa đường truy xuất; k giao diện.
- Chấm (12.3): chọn đề tài **2đ** (tính mới, khả thi, ứng dụng cao); nội dung **6đ** (tập thể 5, cá nhân 1); trình bày và tranh luận **2đ**. Tính vào điểm giữa kỳ 30%.
- 2/3 đề tài là kiến thức đã học, 1/3 là khai thác theo con đường truy xuất (Bài 10–11).
- **[lưu ý]** Giáo trình ghi nhóm 2–4 SV; đề cương mới (21/10) ghi 1–3 SV, theo đề cương mới.

### Sai sót thường gặp về thực thể (13.2.3), cần đối chiếu với mục 2 của báo cáo

1. Thực thể **độc lập**: sự tồn tại không phụ thuộc thực thể khác. `HóaĐơn(SốHĐ, NgLập)` là thực thể; `HóaĐơn(SốHĐ, NgLập, MKH)` là lược đồ quan hệ.
2. Phải có **giá trị lưu trữ và khai thác**. Ví dụ giáo trình: để quản lý mua bán lẻ tại cửa hàng **không cần** thực thể Khách hàng. **[lưu ý]** PowerTech có bán tại quầy cho khách vãng lai; cần cân nhắc khách hàng chỉ là thực thể khi có nhu cầu lưu và khai thác.
3. Phải có **từ hai thể hiện trở lên**: không có thực thể Khoa hay Trường khi chỉ quản lý một khoa CNTT.
4. Tên loại thực thể là **danh từ**.
5. Được làm rõ bằng tên, thuộc tính và vài thể hiện. **Tên thuộc tính không được trùng giữa các thực thể**: `KhachHang(MKH, HoTen, Phai, DC, DT)` thì `NhanVien(MNV, HoTenNV, PhaiNV, DCNV, DTNV)`.
6. Thuộc tính trong một thực thể **không phụ thuộc lẫn nhau**, trừ phụ thuộc đầy đủ vào khóa.
7. Mỗi thực thể thuộc một danh mục: cơ bản (ổn định, không thuộc tính thời gian), đối tượng ngoài (người, tổ chức), nghiệp vụ (luôn có thuộc tính thời gian).

### Mối kết hợp (13.2.4)

Có ngữ nghĩa cần cho quản lý; có giá trị lưu trữ và khai thác; hai thực thể có thể có nhiều mối kết hợp, mỗi mối chỉ một ngữ nghĩa; khóa của mối kết hợp suy từ khóa các thực thể và bản số; thuộc tính của mối kết hợp gồm thuộc tính khóa của các thực thể tham gia cộng thuộc tính riêng (không thuộc khóa).

### Sai sót và nhận xét ở nhóm bài toán kinh doanh (Bài 14)

- Gợi ý đề tài có sẵn: "Quản lý kinh doanh máy vi tính tại một cửa hàng" (gần PowerTech).
- Phải làm rõ: bán sỉ hay lẻ; một trung tâm hay nhiều chi nhánh; phương thức thanh toán (tiền mặt, chuyển khoản, thanh toán liền, nợ, trả góp; bán trên mạng thì thanh toán thế nào).
- Báo cáo kết quả mua bán phải rõ, nhất là **tồn kho theo kỳ**: `TONKHO(THANG, NAM, MHG, TON_DAUKY, NHAP_TK, XUAT_TK, TON_CK)`, tính bằng view từ phiếu nhập, phiếu xuất. **[lưu ý]** cột tồn trong PowerTech là dữ liệu tính toán; hợp với lập luận ở mục 2 của báo cáo cũ.
- Tiêu chí nhận xét: tính mới, tính thực tiễn (biểu mẫu khảo sát thật), tính chính xác (không sai kiến thức và mô hình), điểm khuyến khích (làm việc nhóm, thuyết trình).

## 4. Cách viết mô tả của giảng viên (TH_PTTKHT_2022, Bài 1–8)

- Mô tả mở bằng một câu nói ai cần tin học hóa việc gì ("Một thư viện cần tin học hóa khâu quản lý … như sau"), rồi kể theo chuỗi: người làm việc, danh mục hàng/sách, đối tượng ngoài, từng nghiệp vụ theo thứ tự thời gian, rồi quy định số (tối đa 3 cuốn, tối đa 3 đợt giao, phạt 1%–50%), cuối cùng là thống kê cần có.
- Có các quy tắc quản lý dạng số cụ thể và trường hợp đặc biệt (khách quen được trả chậm, khách vãng lai thanh toán ngay).
- Câu hỏi chuẩn: xác định thực thể, thuộc tính, **kiểu dữ liệu và độ rộng** (giải thích vì sao), gạch chân khóa chính; vẽ ERD **đủ bản số (min,max)**; vẽ bằng Case Studio/Toad Data Modeler; sinh SQL. **[lưu ý]** mục 2 cũ đã có kiểu và miền giá trị; nên có thêm độ rộng và lý do chọn kiểu.
- Ký hiệu ERD trong giáo trình: `KHÁCH HÀNG (0,n) — Mua — (1,1) HÓA ĐƠN`; mối kết hợp n–n có thuộc tính riêng (SL, Đơn giá).

## 5. Bài tập mẫu của giảng viên về đồ thị (`Do thi quan he.pptx`)

- Phân rã: Q1(ABX1), Q2(AX2), Q3(ABCX3DEG), Q4(BDEX4), Q5(CEGX5), Q6(CEX6), Q7(EHX7), Q8(HX8), Q9(HG), Q10(ABCH). Bảng lời giải có cột `PTH | PTH_T | LK | LK_T | cung`, ví dụ nút 3: PTH {1,2}, PTH_Thừa {2}, LK {1,2}, LK_Thừa {0}, cung {1,2}; nút 5: cung {3,4,6}; nút 10: cung {3,8}.
- Đề bài trùng Bài 11.2 của giáo trình (khác ở Q4 và Q7). **[lưu ý]** Ký hiệu Xᵢ là thuộc tính riêng của Qᵢ (chưa xác nhận trong tài liệu); nên tự dựng lại bảng này bằng `dothi.py` cũ làm phép thử cho thuật toán B1–B7 trước khi làm đồ thị PowerTech.

## 6. Điểm cần nhớ khi so với báo cáo cũ (`bao-cao/`)

1. Tiêu chí 5 ở 13.2.3 (tên thuộc tính không trùng giữa các thực thể): kiểm tra tên viết tắt ở mục 2 và 3 cũ.
2. Tiêu chí 2 ở 13.2.3 (giá trị lưu trữ và khai thác) và ví dụ "không cần Khách hàng": cần quyết định rõ cho KHACHHANG, NHANVIEN, các thực thể phụ.
3. Tiêu chí 6 ở 13.2.3: thuộc tính trong một thực thể không phụ thuộc lẫn nhau → mục 8 cũ ghi CHITIETTRA 1NF, PHIEUBAOHANH 2NF, HANGCOSERI 3NF là thực thể hay quan hệ? Giáo trình coi lược đồ đã gộp khóa ngoại là *quan hệ*, không phải thực thể.
4. Đề cương mới đòi phát hiện MVD "nếu có"; mục 9 cũ chọn ảnh – thông số. Cần chứng minh theo định nghĩa của giáo trình (X∩Y = ∅, Z = Q⁺ \ {X,Y}, tập Y của mỗi x không phụ thuộc Z).
5. `Dạng chuẩn 4.md` của Twot có hai dòng LaTeX lỗi (dòng 108, 148) và chữ "RRR"; không dùng làm nguồn trích.
