# Đánh giá báo cáo mẫu của thầy Khang so với đề cương 7 mục, và bài học rút ra (24/10/2026)

**Tài liệu đối chiếu:** `CSDL-NC/yeu-cau-giang-vien/Cau truc bao cao mon CSDL Nang cao.md` (bản `.pptx` ngày 21/10; đây là yêu cầu mới nhất và được ưu tiên cao nhất) và `CSDL-NC/bao-cao-mau/BaoCaoCSDLNC_ThamKhao.md` (bản `.docx` cùng nội dung, nằm ở `bao-cao-mau/`, không phải `yeu-cau-giang-vien/`; bản `.md` bị cắt các hình nên tôi đã mở ảnh từ `.docx` để xem ERD và đồ thị). Nhãn: **[MẪU]** quan sát trong báo cáo mẫu; **[GV]** lời giảng viên; **[Nhận định]** suy luận của tôi.

## 0. Đã đọc gì trong lượt này

| Nguồn | Mức đọc |
|---|---|
| `BaoCaoCSDLNC_ThamKhao` | Toàn văn, kể cả 2.1.2–2.1.3 (từ điển dữ liệu), 2.3 (nhiều quan hệ), 3.1–3.3, chương 4; xem ảnh ERD (Hình 1.1) và hai đồ thị (Hình 3.1, 3.2) |
| `[studocu] Quản lý rạp chiếu phim` (2022, TS Cao Tùng Anh) | Toàn văn; **có ghi chú bên lề của người chấm** (mục 3) |
| `[studocu] Nhóm 6 – Dimensional Modeling` | Chỉ mục lục và 260 dòng đầu; **lạc đề** (kho dữ liệu, không phải CSDL quan hệ), không dùng |
| D6: Giao thông đô thị, Giao tác và khóa, Tìm bạn đồng hành | Toàn văn |
| D5: OnThiToeic | Chương 3–4 (phân tích dạng chuẩn, 4NF, tổng hợp) |
| D5: 7 báo cáo còn lại | **Không đọc lại**; dùng kết luận của `00_kinh_nghiem_viet_mo_ta_tu_D5_D6.md` (đọc ngày 18/10) và grep từ khóa "bảo toàn, phân rã, đa trị, đồ thị" trên cả 14 file `.md` |

Kết quả grep: **không** báo cáo mẫu nào (kể cả `ThamKhao`) có phân rã kèm chứng minh bảo toàn thông tin hoặc bảo toàn phụ thuộc hàm. Chỉ hai báo cáo có đồ thị quan hệ: `ThamKhao` và `Quản lý rạp chiếu phim`. Báo cáo cũ ở `bao-cao/` có cả hai phần này.

## 1. Báo cáo mẫu của thầy Khang đã đáp ứng 7 yêu cầu chưa

Thang: **Đạt** · **Một phần** · **Thiếu** · **Không áp dụng** (đề cương ghi điều kiện "nếu").

| # | Yêu cầu của đề cương 21/10 | Mức | Bằng chứng **[MẪU]** | Điều cần cải thiện cho báo cáo của mình |
|---|---|---|---|---|
| 1 | Mô tả tóm tắt bài toán "giống mô tả tình huống môn PTTK HTTT" | **Một phần** | Chương 1 dài (1.1 đến 1.5): khảo sát thực trạng, tính khả thi, đối tượng, khoảng 25 đoạn nghiệp vụ, mục tiêu. Nội dung nghiệp vụ rõ, có quy tắc đặt mã, số lượng ("tối thiểu 8 ký tự", "gần 60 sinh viên"). Nhưng **không tóm tắt**, và lẫn thuật ngữ kỹ thuật: UUID 36 ký tự, API, Website/Mobile, Google Drive, "hệ thống Scan" | Mô tả 1–2 trang kể nghiệp vụ, rồi đặt khảo sát, khả thi, mục tiêu ngắn. Không UUID, API. Trả lời các câu giảng viên hay hỏi (thanh toán, đặt cọc, hoàn trả, ai duyệt, tối đa mấy) |
| 2 | Đề nghị CSDL: 3 loại thực thể và thuộc tính | **Đạt** | 1.6 có đủ 3 loại, mỗi thực thể ghi `TÊN(thuộc tính): ý nghĩa`; tên thuộc tính **có hậu tố phân biệt** (`HoNV`/`HoSV`, `ThoiGianTaoPH`/`ThoiGianTaoBT`); `CHITIET…` và `KETQUASINHVIEN` được vẽ là **mối kết hợp** (oval xanh) ở ERD, đúng lời nhắc của giảng viên. ERD có **bản số (min,max) cả hai đầu** và tên mối kết hợp. 2.1.3 có từ điển dữ liệu: kiểu, độ dài, PK/FK/PFK | Giữ cách ghi này. Thêm lý do xếp loại cho từng thực thể (như D6/g10). Tránh nhầm như mẫu: `Cấp bậc` là danh từ, không phải động từ; `LOAIDIEM` xếp nghiệp vụ vì có thời gian tạo dù là danh mục |
| 3 | PTH cho **từng** LĐQH, từ đó khóa của từng lược đồ | **Một phần** | Cả 22 quan hệ đều có F, phủ tối thiểu 3 bước (câu mẫu cho từng bước), khóa N/TG/D. Nhưng F **luôn dạng `khóa → tất cả`**, chỉ tính trên lược đồ **không có khóa ngoại** (NHANVIEN ở 2.3.3 thiếu `MaChucVu`, `MaKhoa`, `MaNhanVienQuanLy`), không có khóa ứng viên nào (email, số điện thoại không được xét là UNIQUE), quy tắc nghiệp vụ như "NhomThucHanh rỗng khi không phải phòng thực hành" không thành PTH | Tính F trên **quan hệ đầy đủ có FK**; liệt kê **mọi khóa ứng viên** và các PTH không phải `khóa → tất cả` (SKU, OrderCode, Email, seri…); mỗi PTH có căn cứ nghiệp vụ |
| 4a | Dạng chuẩn từng lược đồ | **Một phần** | Bốn mức 1NF→BCK có câu lý do, có bảng tổng hợp 2.3.23 và kết luận Min(Qᵢ) = BCK. **Lỗi:** CHITIETPHONGHOC, CHITIETBAITAP, CHITIETNHOM, CHITIETNHIEMVU (chỉ có khóa, F rỗng) bị ghi **3NF** với lý do "không có PTH nào có vế trái chứa khóa". Theo định nghĩa của giáo trình (mọi PTH không hiển nhiên có vế trái chứa khóa) điều kiện được thỏa vì không có PTH nào; quan hệ đạt BCK. Ngoài ra không có câu nào về 4NF dù mục 1.5 hứa tìm phụ thuộc đa trị | Ghi BCNF cho quan hệ chỉ có khóa và nêu điều kiện thỏa rỗng; đưa một câu hỏi cho giảng viên nếu muốn chắc |
| 4b | Phân rã/tổng hợp nếu vi phạm DC1, DC2; bảo toàn thông tin và PTH | **Không áp dụng** (nhưng thiếu minh họa) | Không quan hệ nào vi phạm vì mọi F là `khóa → tất cả`. 1.5 nêu "phân rã" và "xây dựng phép kết bảo toàn thông tin" nhưng **không có trang nào làm** | Đây là chỗ báo cáo của mình có thể khác biệt: có lược đồ gốc vi phạm thật (dòng đổi trả, phiếu bảo hành…), làm phân rã/tổng hợp, tableau, kiểm tra F' ≡ F |
| 4c | Sai ở bước 2 của phủ tối thiểu | **Lỗi** | 2.3.11 KETQUASINHVIEN: F = {SV, PH, LĐ → Điểm}, bước 2 ghi "thay bằng {SV → Điểm; PH → Điểm; LĐ → Điểm}". Đây là **sai**: PTH đã đầy đủ (không thuộc tính nào thừa), và ba PTH mới là sai về nghiệp vụ | Kiểm từng thuộc tính vế trái bằng bao đóng (như bài giảng): chỉ bỏ A khỏi X khi `(X − A)⁺` vẫn chứa vế phải |
| 5 | PTH đa trị (nếu có) → 4NF | **Thiếu** | Không tìm MVD, không nói đến 4NF trong thân bài | Tìm MVD thật (ảnh và thông số của mặt hàng); chứng minh theo định nghĩa của giáo trình. OnThiToeic (D5) làm mẫu cách tách tập độc lập (`TheDongNghia`, `ViDuTheGhiNho`) nhưng chưa chứng minh MVD |
| 6 | Đồ thị quan hệ, con đường truy xuất **và ngữ nghĩa từng đường** | **Đạt** (phần mạnh nhất) | 3.1 làm B1→B7: giao từng cặp, bảng PTH/PTH_Thừa/LK/LK_Thừa/Cung (đúng Bảng 10.1), 31 quan hệ cung; Hình 3.1 (22 nút, một khuyên ở nút 3), Hình 3.2 có **cung vô hướng 5—19** (đường đỏ) khi B7 thay nút 20 (CHITIETNHIEMVU). 3.2 có **69 đường** từ **5 nút vào** (11, 14, 17, 19, 22), mỗi đường một câu "Cho biết …" | Giữ cấu trúc. Thiếu trong mẫu: **lý do chọn nút vào** (mẫu coi nút không có cung đi tới là nút vào; giáo trình coi đó là lựa chọn thiết kế); không ghi (m, A, M) trên cung; hình ảnh không đánh nhãn tên quan hệ cạnh số |
| 7 | Viết truy vấn SQL cho các truy xuất | **Một phần, có lỗi** | Quy tắc chung `SELECT … FROM nút vào JOIN … ON` + **5 câu mẫu**, còn lại ghi "tương tự". Câu cho "đường 38" (`19 → 5 → 1`) viết `NHIEMVU JOIN SINHVIEN ON NV.MaSoSinhVien = SV.MaSoSinhVien` nhưng NHIEMVU **không có cột `MaSoSinhVien`** (sinh viên – nhiệm vụ nằm ở quan hệ `CHITIETNHIEMVU`, chính là quan hệ của cung vô hướng 5—19); câu không chạy được. Câu cuối dùng bảng `CAUNHATXET` (gõ sai) | SQL phải chạy trên seed. Mỗi cung vô hướng thì JOIN qua quan hệ cung gốc. Có bảng "đường → SQL" hoặc script sinh; kiểm bằng cách chạy thật |

**Tóm tắt:** báo cáo mẫu **làm đủ 5 trên 7 mục ở mức hình thức** (1, 2, 3, 4a, 6), **chưa làm** 4b (không cần), 5 (bỏ), và 7 chỉ làm một phần. Các mục kỹ thuật khó nhất (4b, 5) là chỗ mẫu để trống.

### Các lỗi và điểm lệch khác trong mẫu (không nằm trong 7 mục)

1. **Số bảng không nhất quán:** 2.1.1 ghi "21 bảng", liệt kê 22. 1.6 mô tả 17 thực thể; 5 quan hệ còn lại từ mối kết hợp.
2. **Ràng buộc và từ điển không khớp:** 2.1.1 ghi `GioiTinhNV` chỉ thuộc "Nam, Nữ, Khác" nhưng 2.1.3 kiểu `Integer`; tương tự `KieuPhong`.
3. **Lỗi dán:** phần KHOA ghi "FNHANVIEN"; "FNHANXET" ở CAUNHANXET; hai dòng "Q₈ ⋂ Q₁₂" lặp ở 3.1 bước 3.
4. **Phân rã đồng nhất B1** ghi "C đã là phân rã đồng nhất" không có kiểm tra (thực ra phải xét mỗi cặp quan hệ có khóa tương hỗ hay không).
5. **Chương 4** là nhận xét chung (ưu, nhược điểm) hơi "sách giáo khoa"; chương "tính năng đã làm / chưa làm" là của đồ án phần mềm, không phải bắt buộc cho môn này.

## 2. Điều rút ra từ ghi chú bên lề của người chấm (báo cáo Rạp chiếu phim, 2022)

Bản này giữ nguyên các ghi chú của giảng viên (TS Cao Tùng Anh, một giảng viên khác). **[GV]** nguyên văn:

- Đầu báo cáo, danh sách yêu cầu của người chấm: "1. Khảo sát hiện trạng. **Thiếu mục lục**", "1- Mô tả yêu cầu", "2- Thiết kế mô hình dữ liệu: **ERD/DFD** các quan hệ (khóa, phụ thuộc hàm)", "3- **Ràng buộc toàn vẹn**", "4- **Đồ thị quan hệ**", "5- **Slide báo cáo đồ án** để trình bày và trả lời câu hỏi".
- "4. Mô hình ERD // **thiếu DFD** nếu class – use case – activity or sequence".
- Ở quan hệ HOADONBANPHIM (khóa {MAHDBANPHIM, MAPHIM}, F ghi `MAHDBANPHIM, MAPHIM → NGAYLAP, SOTIEN, MACTY, MANV` và kết luận BCNF): "**Sai dạng chuẩn 1nf**". **[Nhận định]** Ngày lập, số tiền, nhân viên chỉ phụ thuộc vào `MAHDBANPHIM` (một phần khóa) nên quan hệ không đạt 2NF; giảng viên đọc từng PTH và kiểm khóa ghép.
- Ở bảng PHIM, ô Khóa của thuộc tính `BOMTAN` ghi "????" (người chấm hỏi thuộc tính cờ này là gì). Câu kết luận của nhóm "Tất và cả các phụ thuộc hàm đều đạt BCNF không đa trị => 4NF" không có ghi chú kèm theo.
- Các bảng RBTV có "bảng tầm ảnh hưởng" (thêm/sửa/xóa) đầy đủ cho khóa, khóa ngoại, miền giá trị; ghi chú "*: thao tác có kiểm tra // không được thay đổi".

**[Nhận định]** Năm 2022 giảng viên khác đòi RBTV, đồ thị, ERD/DFD và slide. Đề cương 21/10 của thầy Khang không nhắc RBTV hay slide, nhưng giáo trình Bài 12 vẫn có RBTV (mục h), thuyết trình (2 điểm) và giao diện (mục k). Nên **chuẩn bị slide** và để RBTV là mục tùy chọn ngắn.

## 3. Bài học rút ra, theo mức quan trọng

### 3.1 Cái giảng viên thật sự chấm (suy từ nhận xét 28 nhóm, mẫu 2022, mẫu 2023)

1. **Mô tả và phân loại thực thể là vòng đầu.** Mọi nhận xét D5/D6 chỉ nói về mô tả, thực thể, phạm vi, quy trình nghiệp vụ. Đây là chỗ mất điểm sớm và "mất tiếp ở các bước sau" (giáo trình 13.2.2).
2. **Quy tắc nghiệp vụ cụ thể, đo được** được khen (nguyên liệu, trọng lượng, số ghế tối đa, thời hạn nộp). Thiếu: thanh toán, đặt cọc, hoàn trả, ai duyệt.
3. **Kiểm tra từng PTH và từng khóa ghép:** ghi chú "Sai dạng chuẩn 1nf" cho thấy người chấm đọc thật.
4. **Phần kỹ thuật khó thường bị bỏ** (phân rã, bảo toàn, 4NF): 14 trong 14 báo cáo mẫu không có chứng minh. Hướng dẫn 18/10 nói rõ "Nếu phát hiện DC4 thì quá tốt (cộng điểm)". Đây là cơ hội lớn nhất, nếu làm đúng.
5. **Đồ thị và đường truy xuất** là phần đề cương nhấn ở mục 6–7 và giáo trình dành 1/3 bài tập lớn (Bài 12.2.1). Mẫu 2023 làm đủ B1–B7 nhưng SQL còn lỗi.

### 3.2 Lỗi hay gặp trong mẫu, cần tránh

| Nhóm lỗi | Ví dụ trong mẫu |
|---|---|
| Phủ tối thiểu sai bước 2 | ThamKhao 2.3.11 (KETQUASINHVIEN); bài giảng 18/10 (ví dụ 3 bước) |
| Kết luận dạng chuẩn sai do bỏ sót khóa ứng viên | Rạp phim (khóa ghép); bài tập 3 trong bài giảng 18/10 (thiếu hai khóa AB, AD) |
| Quan hệ chỉ có khóa ghi 3NF | ThamKhao 4 quan hệ |
| Số liệu không nhất quán trong cùng báo cáo | "21 bảng" vs 22; AI Task Manager lẫn thuộc tính giữa bảng; EduPlay `room_cod` |
| Mô tả có công nghệ, tên bảng, khóa | JWT, TensorFlow.js, UUID, API, `host_id` |
| SQL không chạy được | ThamKhao đường 38 |
| Khẳng định 4NF không có chứng minh | OnThiToeic ("chưa xác định đủ phụ thuộc đa trị" rồi vẫn gán 4NF cho 8 quan hệ), FitTrack (làm đúng: chỉ khẳng định BCNF) |
| Tạo "3NF không BCNF" bằng thuộc tính phái sinh | OnThiToeic thêm `LoaiBoDe`, `SoBoDeTrongLoai`, `SoChuDeHienThi` vào "phép chiếu phục vụ phân tích" |

### 3.3 Cách làm tốt nên học

1. **Một khuôn cố định cho mỗi quan hệ** (ThamKhao, OnThiToeic, HanGo): tân từ → F → phủ → khóa → từng mức dạng chuẩn → kết luận; cuối có bảng tổng hợp và "dạng chuẩn lược đồ = Min(Qᵢ)".
2. **Tân từ + ràng buộc** cho từng quan hệ (kiểu, độ dài, NULL, quy tắc mã, ràng buộc loại trừ như "hoặc sinh viên hoặc nhân viên").
3. **Từ điển dữ liệu** với PK/FK/PFK, kiểu, độ dài (2.1.3 của mẫu). Giảng viên PTTK cũng yêu cầu "kiểu dữ liệu và độ rộng" (TH_PTTKHT Bài 1.2).
4. **Nêu giả định nghiệp vụ trước phân tích** (FitTrack), và **nói rõ cái chưa đủ cơ sở** (FitTrack về 4NF, OnThiToeic ở 8 quan hệ BCNF).
5. **Phạm vi nêu ngay đầu** ("chưa thu tiền", "chưa xác minh danh tính" ở Tìm bạn đồng hành; "xét … chưa xét …" ở Fitness).
6. **Ngữ nghĩa đường truy xuất bằng câu hỏi "Cho biết …"** (ThamKhao 3.2).
7. **Bảng tình huống / quy tắc kèm kỹ thuật** (Giao tác và khóa) khiến người đọc thấy ngay lý do thiết kế.

## 4. Hệ quả cho báo cáo mới: danh sách bổ sung (ưu tiên giảm dần)

| # | Việc | Căn cứ |
|---|---|---|
| 1 | Thêm **Lời mở đầu, khảo sát, tính khả thi, mục tiêu, kết luận, tài liệu tham khảo** (ngắn) | ThamKhao có; báo cáo cũ chưa |
| 2 | Giữ **phân rã/tổng hợp, tableau, bảo toàn PTH, 4NF**, nhưng chỉ làm ở những quan hệ vi phạm thật; ghi rõ cách tính | Đề cương mục 4–5; mẫu để trống |
| 3 | **Từng quan hệ một khuôn** (như ThamKhao) với F trên quan hệ có FK và đủ khóa ứng viên; quan hệ chỉ có khóa ghi BCNF kèm lời giải thích | Đề cương mục 3–4; sửa lỗi mẫu |
| 4 | **Từ điển dữ liệu** (kiểu, độ dài) và **tân từ + ràng buộc** cho mỗi quan hệ | ThamKhao 2.1; TH_PTTKHT |
| 5 | **Đồ thị:** lý do chọn nút vào; (m, A, M) trên cung; hình dựng rõ; bảng đường truy xuất đủ + ngữ nghĩa | Đề cương mục 6; giáo trình Bài 9–10 |
| 6 | **SQL chạy được** trên dữ liệu seed cho từng nhóm đường, JOIN qua quan hệ cung gốc; kiểm bằng cách chạy thật | Đề cương mục 7; lỗi đường 38 |
| 7 | **Mô tả thuần nghiệp vụ**, trả lời 11 câu hỏi hay gặp, đặc biệt đặt cọc, phí đổi trả, ai kiểm tra hàng trả | Nhận xét D6/g6 |
| 8 | **Slide** thuyết trình và câu hỏi ôn bảo vệ | Giáo trình 12.3 (2 điểm); mẫu 2022 |
| 9 | RBTV và bảng tầm ảnh hưởng: tùy chọn, ngắn | Giáo trình Bài 12 (h); mẫu 2022 |
| 10 | ERD đủ bản số, tên mối kết hợp là **động từ**, `CHITIET…` là mối kết hợp | Giáo trình 13.2.4; mẫu ThamKhao đạt phần lớn |

## 5. Điều chưa chắc, cần hỏi giảng viên

1. Báo cáo mẫu ThamKhao do ai viết và có được chấm điểm cao không, hay chỉ là mẫu hình thức?
2. Quan hệ chỉ có khóa nên ghi BCNF hay 3NF theo lớp?
3. "Viết các truy vấn cho các truy xuất trên" là cho mọi đường hay đại diện?
4. Có cần RBTV và slide trình bày không?
5. Nút vào của đồ thị nên chọn thế nào: nút không có cung đi tới (như mẫu) hay theo nhu cầu khai thác (như giáo trình)?
6. Cột số trong file nhận xét có nghĩa gì?
