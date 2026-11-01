# Phân tích `CSDL-NC/yeu-cau-giang-vien/` (24/10/2026)

Đây là phần phân tích để làm nền cho báo cáo mới. Nhãn: **[GV]** giảng viên nói hoặc viết; **[MẪU]** quan sát trong `BaoCaoCSDLNC_ThamKhao.docx`; **[Nhận định]** suy luận của tôi, giảng viên chưa xác nhận.

Hai điều chưa được kiểm chứng và ảnh hưởng đến cách đọc mọi thứ bên dưới:

- Cột số (0, 5, 6, 7) và chữ `v` trong hai file nhận xét chưa có chú thích. Không biết đó là điểm của phần nào.
- `BaoCaoCSDLNC_ThamKhao.docx` ghi năm 2023, tên sinh viên là AAA/BBB, giảng viên hướng dẫn ThS. Võ Hoàng Khang. Chưa rõ giảng viên lớp mình có phải người này và đây có phải báo cáo được chấm điểm cao hay chỉ là mẫu hình thức. **[Nhận định]** Dùng nó làm mẫu bố cục, không làm mẫu mức điểm.

## 1. Có bao nhiêu lớp yêu cầu, và chúng khớp nhau thế nào

| Lớp | Nguồn | Ngày | Nội dung |
|---|---|---|---|
| A | `Huong_dan_cach_viet_bao_cao_CSDLNC` | 18/10 | Danh sách 8 mục (mô tả → dạng chuẩn từng bảng) và đoạn "Cải tiến để đạt DC cao hơn… 4NF cộng điểm… chứng minh bảo toàn thông tin, bảo toàn PTH… đồ thị và con đường truy xuất" |
| B | `Cau truc bao cao mon CSDL Nang cao` (đề cương bài tập lớn, 2 slide) | 21/10 | **7 mục**, mới nhất (mục 7 ở dưới) |
| C | Giáo trình CSDL-NC-2015, Bài 12 | 2015 | 11 mục a–k và thang điểm 2 + 6 + 2 |
| D | `BaoCaoCSDLNC_ThamKhao.docx` | 24/10 | Một báo cáo hoàn chỉnh, 4 chương, 22 quan hệ |

Đề cương B (mới nhất, ưu tiên cao nhất): (1) mô tả tóm tắt; (2) đề nghị CSDL – 3 loại thực thể và thuộc tính; (3) tập PTH cho **từng** lược đồ, từ đó khóa của từng lược đồ; (4) dạng chuẩn từng lược đồ; vi phạm DC1, DC2 thì phân rã/tổng hợp/tổng hợp cải tiến để đạt DCBC, không được thì ít nhất DC3; kiểm tra bảo toàn thông tin và bảo toàn PTH; (5) phụ thuộc đa trị (nếu có, không có thì bỏ qua) → đa trị tầm thường → DC4; (6) đồ thị quan hệ, **các con đường truy xuất và ngữ nghĩa của từng con đường**; (7) truy vấn SQL **cho các truy xuất trên**. Nhóm 1–3 SV.

### Bảng đối chiếu

| Nội dung | A (hướng dẫn) | B (đề cương 21/10) | C (giáo trình) | D (báo cáo mẫu) |
|---|---|---|---|---|
| Mô tả, lĩnh vực cần tin học hóa | có | "mô tả tóm tắt" | đặc tả, mục đích, phạm vi, phân công, thu thập thông tin | Chương 1 dài: khảo sát, khả thi, đối tượng, nghiệp vụ, mục tiêu |
| 3 loại thực thể | có, kèm ERD, bản số | có, **không nhắc ERD** | mô hình quan niệm, quan niệm xử lý, quan hệ | liệt kê 3 loại, ERD là hình |
| PTH, phủ tối thiểu, khóa | có | PTH + khóa; **không nhắc riêng phủ tối thiểu** | có (Bài 3) | từng quan hệ: F, phủ 3 bước, N/TG/D |
| Dạng chuẩn | từng bảng và cả lược đồ | từng lược đồ; ít nhất DC3 | Bài 4 | 1NF → BCK từng bảng, bảng đánh giá, lược đồ = Min(Qᵢ) |
| Phân rã/tổng hợp + bảo toàn | có | có | Bài 6–7 | **không có** (mọi bảng đã BCK) |
| 4NF | cộng điểm | có nếu có MVD | Bài 4 | không có |
| Đồ thị, đường truy xuất, ngữ nghĩa | có | có | Bài 9–11 | B1–B7, 69 đường, ngữ nghĩa, SQL mẫu |
| SQL | không nhắc | **mục 7** | mục j | mẫu quy tắc + 5 câu |
| RBTV | không | không | mục h | "Ràng buộc" viết trong mỗi quan hệ |
| Giao diện, quan niệm xử lý | không | không | mục f, k | Class/Use Case (hình) |

### Mâu thuẫn và cách xử lý (đề xuất, chờ Twot chốt)

1. **ERD:** B không nhắc, A nói rõ có ERD và bản số, D có ERD. Giữ ERD, vì rẻ và an toàn. Báo cáo cũ đã có ERD đầy đủ bản số (53 mối kết hợp).
2. **Phủ tối thiểu:** B không đòi riêng, nhưng bài giảng và giáo trình dạy; D làm từng quan hệ. Giữ, nhưng chỉ trình bày chi tiết khi phủ có thay đổi.
3. **Độ dài mô tả:** B nói "tóm tắt", nhận xét D5/D6 nói "viết gọn", còn D có chương 1 dài. **[Nhận định]** Mô tả 1–2 trang kể nghiệp vụ, thêm các mục khảo sát, khả thi, mục tiêu ngắn như D.
4. **"Từng lược đồ":** B và D đều làm *từng* quan hệ. Báo cáo cũ gộp ("F ngắn gọn cho phần còn lại", "tóm tắt 26 quan hệ") là điểm cần đổi nếu giữ nhiều quan hệ (xem quyết định 1 ở mục 5).

## 2. Nhận xét của giảng viên về 28 nhóm (D5 15 nhóm, D6 13 nhóm)

Chi tiết từng nhận xét đã có ở `00_kinh_nghiem_viet_mo_ta_tu_D5_D6.md` (tôi đã đối chiếu lại với hai file `.md`, đúng nguyên văn). Điều mới cần nhấn:

1. **Toàn bộ nhận xét chỉ chạm giai đoạn mô tả và thực thể** **[GV]**. Không có nhận xét nào về PTH, khóa, dạng chuẩn. **[Nhận định]** Đây là vòng chấm đầu. Bài nộp cuối sẽ bị chấm cả phần kỹ thuật, theo đề cương B.
2. **Sáu nhóm lỗi lặp** (số nhóm bị nhắc): mô tả có thuật ngữ CNTT, khóa, FK, tên bảng (6 nhóm D5); nhầm thực thể với mối kết hợp (7 nhóm: `ChiTiet…`, `CT_`, `LichSu…`, `Showtimes`, `Công thức`); phạm vi quá rộng (8 nhóm); chưa xác định 3 loại thực thể trước khi vẽ ERD (3 nhóm); thiếu quy trình thanh toán, đặt cọc, hoàn trả (8 nhóm); chép từ mạng (2 nhóm).
3. **Giảng viên khen khi:** ý tưởng khác biệt hoặc mô tả cụ thể, có con số (nguyên liệu, trọng lượng; phiếu bữa ăn kèm hàm lượng). Lời khen nguyên văn: "Ý tưởng hay", "Đề tài hay", "Đề tài mô tả hay", "Đề tài này HAY".
4. **Giảng viên hỏi theo kiểu nghiệp vụ, không hỏi kỹ thuật:** "Ai kiểm tra?", "Thanh toán bằng cách nào?", "Tối đa mấy?", "Phí ra sao?", "Xử lý trường hợp lệch thế nào?". Có 11 loại câu hỏi đã gom ở mục 3 của file kinh nghiệm.
5. **Nhận xét riêng cho PowerTech (D6, nhóm 6):** "Bổ sung hình thức mua trực tiếp tại cửa hàng. Cơ chế bảo hành, đổi hàng... ra sao?" **[GV]**. Bản v3 đã trả lời; hai điểm bản v3 chưa thấy: đặt cọc và các khoản phí khi đổi trả, hoàn tiền (đã ghi ở kinh nghiệm).
6. **Cảnh báo "đề tài đã có nhiều người làm"** (D6/g13, quản lý phòng trọ) **[GV]**: PowerTech là đề tài có nhiều người làm kiểu "cửa hàng bán lẻ". Lợi thế cần nhấn: số seri, hàng chờ kiểm tra, bảo hành theo seri, bán tại quầy và trực tuyến. Giáo trình (Bài 14) còn gợi ý đúng đề tài "quản lý kinh doanh máy vi tính tại một cửa hàng" và dặn làm rõ bán sỉ/lẻ, một hay nhiều chi nhánh, phương thức thanh toán, báo cáo tồn kho theo kỳ.

## 3. Phân tích báo cáo tham khảo mới (`BaoCaoCSDLNC_ThamKhao.docx`)

Đề tài: HUTECH Classroom, 22 quan hệ: 17 thực thể (6 cơ bản, 2 đối tượng ngoài, 9 nghiệp vụ) và 5 quan hệ sinh từ mối kết hợp (CHITIETPHONGHOC, KETQUASINHVIEN, CHITIETBAITAP, CHITIETNHOM, CHITIETNHIEMVU). 11 hình ảnh (ERD x2, Class, 6 Use Case, 2 đồ thị).

### 3.1 Bố cục

Bìa → Lời mở đầu, Lời cảm ơn, Lời cam đoan → Mục lục, Danh mục hình → **Chương 1 Tổng quan** (1.1 khảo sát thực trạng, 1.2 tính khả thi, 1.3 đối tượng sử dụng, 1.4 mô tả nghiệp vụ, 1.5 mục tiêu nghiên cứu, 1.6 các loại thực thể, 1.7 ERD) → **Chương 2 Cơ sở lý thuyết** (2.1 mô hình quan hệ: 22 quan hệ, mỗi cái có *tân từ* và *ràng buộc*; 2.2 Class và Use Case; 2.3 từng quan hệ: F → phủ tối thiểu 3 bước → khóa → dạng chuẩn; 2.3.23 bảng đánh giá) → **Chương 3 Kết quả thực nghiệm** (3.1 đồ thị B1–B7, 3.2 ý nghĩa 69 đường truy xuất, 3.3 SQL) → **Chương 4 Kết luận và kiến nghị** (ưu, nhược điểm, tính năng đã làm và chưa làm, hướng phát triển) → Tài liệu tham khảo (4 sách, 3 website).

### 3.2 Cách làm từng phần, điểm đáng học

- **1.5 Mục tiêu** viết đúng theo nội dung bài tập lớn: khảo sát hiện trạng, tính khả thi, mô tả tóm tắt, đề nghị CSDL, quy tắc quản lý → phát hiện vi phạm DC2/DC3 → phân rã, đánh giá lược đồ (nhất quán, dễ khai thác, không trùng lắp), phụ thuộc đa trị → DC4, đồ thị quan hệ, đường truy xuất và ngữ nghĩa, truy vấn SQL. **[Nhận định]** Đây là cách nối 7 mục của đề cương B vào mở đầu báo cáo.
- **1.6** ghi mỗi thực thể bằng một dòng `TÊN(thuộc tính…): ý nghĩa`. Tên thuộc tính **có hậu tố phân biệt** (`HoNV` và `HoSV`, `ThoiGianTaoPH` và `ThoiGianTaoBT`), đúng tiêu chí 5 ở 13.2.3 của giáo trình. Thực thể nghiệp vụ nào cũng có `ThoiGianTao…`, `ThoiGianCapNhat…`.
- **Tân từ + Ràng buộc:** mỗi quan hệ kèm một đoạn tân từ (nói thuộc tính nào là gì) và một đoạn ràng buộc (kiểu, độ dài tối đa, NULL, định dạng, quy tắc mã, ràng buộc loại trừ, thời gian tạo trước thời gian cập nhật). Ví dụ ràng buộc loại trừ: bài đăng của sinh viên hoặc nhân viên, đúng một trong hai.
- **2.3, mỗi quan hệ:** (1) tân từ lại, (2) F, (3) phủ tối thiểu với câu mẫu cho từng bước ("Không thực hiện vì tất cả phụ thuộc hàm đã có vế phải là một thuộc tính"), (4) **N, TG, D** + bao đóng, (5) dạng chuẩn: bốn câu "Đạt dạng chuẩn k vì…", (6) kết luận. Khuôn cố định, dễ chấm.
- **2.3.23** bảng 4 cột (STT, quan hệ, khóa, dạng chuẩn) rồi kết luận dạng chuẩn lược đồ = Min(Qᵢ).
- **3.1** làm đủ B1–B7: liệt kê giao của từng cặp quan hệ để kiểm tra nút bản lề, bảng PTH/PTH_Thừa/LK/LK_Thừa/Cung (đúng Bảng 10.1), 31 quan hệ cung, hình.
- **3.2** có **5 nút vào** (11, 14, 17, 19, 22); đó là các nút không có cung nào đi tới. Từ mỗi nút vào liệt kê mọi đường đi theo cung đến hết, kèm một câu ngữ nghĩa "Cho biết thông tin …". Tổng 69 đường.
- **3.3** nêu quy tắc chung (`SELECT * FROM nút vào JOIN … ON khóa`), làm 5 đường và ghi "tương tự" cho phần còn lại. **[Nhận định]** Giảng viên chấp nhận mẫu và 5 ví dụ đại diện, nhưng đề cương B đòi "viết các truy vấn cho các truy xuất trên": an toàn hơn nếu có SQL (hoặc bảng sinh SQL) cho đủ các nhóm đường.

### 3.3 Lỗi trong chính báo cáo mẫu (để tránh, và để biết giảng viên có thể bỏ qua những lỗi này)

| # | Lỗi | Căn cứ **[MẪU]** |
|---|---|---|
| 1 | Số bảng không nhất quán | 2.1.1 ghi "21 bảng" nhưng liệt kê 22; mục 2.3 đánh số đến 22 |
| 2 | Dán nhầm tên | Phần KHOA ghi "Vậy FNHANVIEN"; phần câu nhận xét ghi "FNHANXET"; truy vấn dùng `CAUNHATXET` (gõ sai) |
| 3 | **Quan hệ chỉ có khóa bị kết luận 3NF** | 2.3.9 CHITIETPHONGHOC: F rỗng, ghi "Không đạt BCK vì … không có phụ thuộc hàm" → 3NF. Theo định nghĩa của giáo trình (mọi PTH không hiển nhiên có vế trái chứa khóa) thì điều kiện thỏa vì không có PTH nào; quan hệ đạt BCK. Cùng lỗi ở CHITIETBAITAP, CHITIETNHOM, CHITIETNHIEMVU |
| 4 | Phân tích F trên lược đồ *không có khóa ngoại* nhưng mô hình quan hệ có | NHANVIEN ở 2.3.3 không có MaChucVu, MaKhoa, MaNhanVienQuanLy, còn 2.1 có. Khóa ngoại không xuất hiện trong F. **[Nhận định]** Có thể đúng ý "phân tích thực thể", nhưng khi tính dạng chuẩn thật của quan hệ thì phải đưa khóa ngoại vào |
| 5 | Mọi PTH đều dạng `khóa → tất cả` | 22/22 quan hệ; các bước 2 và 3 của phủ tối thiểu luôn "không thực hiện"; không có chỗ nào để phân rã hay tìm 4NF |
| 6 | Mô tả có thuật ngữ kỹ thuật | UUID 36 ký tự, API, Website, Mobile, Google Drive trong 1.2 và 1.4. Giảng viên không nhận xét riêng nhưng đây là điều D5 nhiều nhóm bị nhắc |
| 7 | Điều kiện "nút vào" chỉ ghi "5 nút vào" | Không nói cách chọn; theo giáo trình nút vào là lựa chọn thiết kế (j(n)=1), không phải mọi nút không có cung vào |
| 8 | Hai dòng mâu thuẫn ở 3.1 bước 3 | "Q₈ ⋂ Q₁₂" xuất hiện hai lần; "Q₃ ⋂ Q₃ = {MaNhanVienQuanLy}" là quan hệ tự tham chiếu nhưng ghi khóa là `MaNhanVien` |

### 3.4 So với báo cáo cũ của nhóm (`bao-cao/`)

| Nội dung | Báo cáo mẫu | Báo cáo cũ |
|---|---|---|
| Số quan hệ | 22 | 38 (39 sau cải tiến) |
| Phân tích từng quan hệ | đủ, một khuôn cố định | đủ cho 5+4+8 quan hệ, "F ngắn gọn" cho phần còn lại |
| Phân rã, bảo toàn, 4NF | không có | có (3 quan hệ, tableau, 4NF ảnh – thông số) |
| Đồ thị | B1–B7, 69 đường theo 5 nút vào | B1–B7, 38 nút, 65 cung, 7 yêu cầu K1–K7 |
| Phần mở đầu và kết luận | có | chưa có |
| Tân từ + Ràng buộc từng quan hệ | có, rất cụ thể | có tân từ cho nhóm lớn, ràng buộc dạng bảng |
| Lỗi giảng viên chưa nhắc nhưng có thể bị chấm | CHITIET* 3NF, khóa ngoại thiếu | `HoTen` giữ nguyên; PHIEUBAOHANH 2NF, CHITIETTRA 1NF trong lược đồ gốc |

**[Nhận định]** Báo cáo cũ đã vượt báo cáo mẫu về chiều sâu kỹ thuật; điểm yếu là thiếu phần bao bọc (mở đầu, khảo sát, khả thi, kết luận) và độ nhất quán "từng quan hệ một khuôn".

## 4. Hệ quả cho báo cáo mới

### 4.1 Khung đề xuất (kết hợp B làm xương, D làm bố cục, C làm yêu cầu)

1. Lời mở đầu, cảm ơn, cam đoan; mục lục; danh mục hình, bảng.
2. **Chương 1 Tổng quan:** khảo sát thực trạng, tính khả thi (có phạm vi: một cửa hàng, bán quầy và trực tuyến), đối tượng sử dụng, mô tả nghiệp vụ (văn xuôi, trả lời 11 câu hỏi của giảng viên), mục tiêu nghiên cứu (nối 7 mục của B), 3 loại thực thể, ERD.
3. **Chương 2 Cơ sở dữ liệu quan hệ:** mô hình quan hệ (tân từ + ràng buộc), từng quan hệ: F → phủ tối thiểu → khóa → dạng chuẩn, bảng đánh giá, cải tiến (phân rã/tổng hợp, bảo toàn thông tin, bảo toàn PTH, 4NF), lược đồ sau cải tiến.
4. **Chương 3 Kết quả:** đồ thị quan hệ (B1–B7), con đường truy xuất và ngữ nghĩa, SQL.
5. **Chương 4 Kết luận:** ưu điểm, hạn chế, đã làm và chưa làm, hướng phát triển. Tài liệu tham khảo.

### 4.2 Điều phải làm tốt hơn mẫu

- Mỗi quan hệ một khuôn như D, nhưng **tính F trên quan hệ đầy đủ (có khóa ngoại)** và có **khóa ứng viên** (SKU, Email, OrderCode, cặp UNIQUE), không chỉ `Id`.
- Quan hệ chỉ có khóa: ghi **BCNF vì không có PTH không hiển nhiên**, giải thích điều kiện thỏa rỗng (điểm giảng viên dễ hỏi khi bảo vệ vì mẫu và giáo trình Bài 4 có thể bị hiểu khác).
- Có thật phần phân rã và bảo toàn (mẫu không có), 4NF chứng minh theo định nghĩa của giáo trình.
- Đồ thị: nêu rõ cách chọn nút vào; ngữ nghĩa từng đường; SQL chạy được trên dữ liệu seed.
- Mô tả thuần nghiệp vụ, không UUID, API, tên bảng.

## 5. Quyết định cần Twot chốt trước khi viết

1. **Phạm vi bảng.** Báo cáo cũ có 38 quan hệ. Giảng viên nhắc "giới hạn chức năng", "làm kịp"; mẫu chỉ 22. Gợi ý: chọn khoảng 20–24 quan hệ lõi (sản phẩm – thông số – ảnh, đơn hàng – thanh toán – giao hàng, nhập – kho, bảo hành – đổi trả), phần còn lại nêu là ngoài phạm vi và lý do.
2. **Chương hay mục:** bố cục 4 chương như mẫu hay giữ 10 mục? Gợi ý: 4 chương, mỗi chương gồm các mục tương ứng.
3. **`HoTen`:** tách `HoLot`, `Ten` theo bài giảng, hay giữ (xem file `01_ghi_chu_bai_giang_18_10.md` mục 2).
4. **Khách hàng có là thực thể không** khi bán lẻ tại quầy (giáo trình Bài 13: không cần nếu không lưu và khai thác).
5. **Hậu tố tên thuộc tính** như mẫu (`HoNV`, `HoSV`) hay tên đầy đủ (`TenKH`, `TenNCC`).
6. **SQL:** viết cho từng đường (script sinh) hay đại diện từng nhóm đường như mẫu.

## 6. Câu hỏi nên hỏi lại giảng viên

1. Cột số trong file nhận xét (5, 6, 7, 0, `v`) nghĩa là gì?
2. Báo cáo cuối có cần ERD không (đề cương 21/10 không nhắc)?
3. Quan hệ chỉ có khóa nên ghi BCNF hay 3NF?
4. Mục 7 "viết truy vấn cho các truy xuất" nghĩa là mọi đường hay đại diện?
5. Với nhóm 3 SV, mức chi tiết và số lượng quan hệ kỳ vọng?
