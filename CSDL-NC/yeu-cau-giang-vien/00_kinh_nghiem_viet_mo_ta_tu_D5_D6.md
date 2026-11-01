# Kinh nghiệm viết báo cáo CSDL-NC, rút từ lớp 23DTHD5 và 23DTHD6

Cập nhật 18/10/2026, sau khi đọc lại toàn bộ nhận xét của giảng viên và các báo cáo mẫu; sửa ngày 01/11/2026 cho khớp đề cương mới và báo cáo hiện hành. Đây là điều rút ra từ nhận xét thật, không phải quy định chính thức. Yêu cầu chính nằm ở [Cau truc bao cao mon CSDL Nang cao.md](<Cau truc bao cao mon CSDL Nang cao.md>) (đề cương 7 nội dung, mới nhất); [Huong_dan_cach_viet_bao_cao_CSDLNC.md](Huong_dan_cach_viet_bao_cao_CSDLNC.md) là yêu cầu trước đó, dùng bổ sung, khi khác nhau thì theo đề cương.

## 0. Nguồn và độ tin cậy

| Nguồn | Nội dung | Ghi chú |
|---|---|---|
| `23DTHD5.xlsx - Sheet1` | Nhận xét ngày 9/10/2026, 16 nhóm | 15 nhóm có nhận xét (nhóm 1 để trống) |
| `23DTHD6.xlsx - Sheet1` | Nhận xét ngày 5/10/2026, 15 nhóm | 13 nhóm có nhận xét (nhóm 5 và 14 không có) |
| `.csv` và `.md` của hai file trên | Cùng nội dung | Đã so sánh từng ô, 2 cặp file giống hệt |
| `bao-cao-mau/D5` và `D6` | **11 báo cáo** (8 của D5, 3 của D6) | Phạm vi đọc ở mục 4 |

Quy ước nhãn trong file này:

- **[GV]** nhận xét của giảng viên, trích từ hai file nhận xét.
- **[BC]** điều quan sát được trong báo cáo mẫu.
- **[Nhận định]** suy luận của người ghi chép, giảng viên chưa xác nhận.

Cột số trong file nhận xét (0, 5, 6, 7) và ký hiệu `v` chưa có chú thích, nên chưa xác định là điểm của phần nào. Chỉ có thể nói: nhóm PowerTech ở mức 7; 10 trong 11 báo cáo mẫu ở mức 7, riêng AI Task Manager ở mức 6. Các báo cáo trong `D5/`, `D6/` là bản ban đầu của từng nhóm (Twot xác nhận 01/11/2026), không phải sản phẩm cuối. Thư mục chỉ chứa báo cáo của một số nhóm, nên không suy ra được báo cáo nào điểm thấp trông như thế nào.

Nhận xét của cả 28 nhóm (15 của D5, 13 của D6) chỉ bàn về **mô tả, thực thể, phạm vi và quy trình nghiệp vụ**. Không nhận xét nào chấm phần phụ thuộc hàm, phủ tối thiểu, khóa hay dạng chuẩn. **[Nhận định]** Có thể giảng viên mới chấm giai đoạn đầu; không có căn cứ trong hai file để biết chuẩn chấm của các phần sau.

## 1. Nhận xét dành cho nhóm PowerTech (D6, nhóm 6)

> **[GV]** "Bổ sung hình thức mua trực tiếp tại cửa hàng. Cơ chế bảo hành, đổi hàng... ra sao?"

Trạng thái: Chương 1 hiện hành (`bao-cao-moi/chuong_docx/Chuong1_Tong_quan.docx`) đã có bán tại quầy, bảo hành, đổi trả, đặt cọc và phí xử lý khi đổi trả (đối chiếu 01/11/2026). Bản cũ [01_Mo_ta_de_tai.md](../../bao-cao/01_Mo_ta_de_tai.md) chưa có đặt cọc và các khoản phí; chỉ giữ làm tham khảo. Chưa kiểm từng chi tiết khác.

## 2. Lỗi giảng viên nhắc, theo loại

Số nhóm viết theo lớp, ví dụ D5/g6 là lớp D5, nhóm 6.

| Lỗi | Căn cứ **[GV]** | Cách tránh |
|---|---|---|
| Mô tả lẫn thuật ngữ CNTT, khóa, FK, tên bảng | D5/g3 "Khi mô tả, ta chưa đưa FK vào"; D5/g4 "ko đưa các từ ngữ chuyên ngành"; D5/g6 "ko nên đưa khóa {UserID, TuVungID} vào"; D5/g7 "chưa lạm dụng CNTT", "chưa xđ các Table"; D5/g8 "chưa đưa FK vào"; D5/g9 "chưa viết Tin học vào" | Mô tả như người làm nghề kể. Tên bảng, khóa, FK chỉ xuất hiện từ phần thực thể trở đi. **[Nhận định]** Câu "ta chưa..." là "ở bước này chưa nên"; cách hiểu này khớp với D5/g6. |
| Nhầm thực thể với mối kết hợp (MKH) | D5/g9 LichSuDocNghe; D5/g10 Công thức, Buoc_thuc_hien; D5/g14 "xác định cho đúng loại thực thể và MKH"; D5/g15 Showtimes; D6/g1 ChiTiet...; D6/g4 CHI_TIET_; D6/g15 CT_ ("MKH n-n") | Dòng chi tiết và bảng liên kết N–N là mối kết hợp, không liệt kê như thực thể. Áp cho `OrderItems`, `PurchaseReceiptItems`, `CartItems`. |
| Nhầm thuộc tính với bảng | D5/g7 "Giới tính, Điểm đánh giá là thuộc tính, ko là Table" | Giá trị chỉ để phân loại là thuộc tính. |
| Nhầm thống kê với thực thể | D6/g1 "TonKho, LichSu... là thống kê, ko là thực thể" | Tồn kho, tổng tiền, doanh thu là dữ liệu tính toán. Nếu lưu sẵn thì ghi rõ là cột suy diễn. |
| Chưa xác định 3 loại thực thể trước khi vẽ ERD | D5/g7 "xđ 3 loại thực thể cho đúng"; D5/g8 "xác định lại 3 loại thực thể và thuộc tính"; D6/g8 "Bổ sung 3 loại thực thể trước khi vẽ ERD. Sau đó mới chuyển sang mô hình quan hệ, xđ PTH" | Giữ thứ tự: mô tả, 3 loại thực thể, ERD, mô hình quan hệ, phụ thuộc hàm. |
| Phạm vi quá rộng | D5/g3 "giới hạn chức năng chứ ko làm kịp"; D5/g4 "Giới hạn lại số môn"; D6/g8 "làm ko nỗi (do tham khảo trên mạng)"; D6/g9, g11 "viết gọn"; D6/g12 "Bỏ qua các chức năng hệ thống"; D6/g15 "Quá LIỀU! ... Bỏ chức năng TRANSACTION VÀ LOCKING"; D6/g3 "bớt các chức năng mu/trả vé, dịch vụ" | Nêu phạm vi ngay đầu mô tả và làm sâu vài nhóm nghiệp vụ. |
| Nội dung dài không cần thiết | D5/g4 "Nội dung các MH ko nên đưa vào" | Không đưa nội dung chi tiết của dữ liệu (ví dụ nội dung từng môn học) vào mô tả. |
| Chép trên mạng | D5/g9 "Ko copy trên mạng và dán hình vào thay thế cho nội dung"; D6/g8 | Tự viết và tự vẽ. |
| Mô tả sai thực tế Việt Nam | D6/g10 "Đã sáp nhập Quận/Huyện, chỉ còn Phường/Xã"; D6/g9 "bệnh viện đã tích hợp thông tin vào Thẻ bệnh án (CCCD)" | Kiểm tra đơn vị hành chính, giấy tờ, quy định còn hiệu lực. |
| Đề tài trùng nhiều người | D6/g13 "đã có nhiều người làm" | Nhấn vào điểm riêng của PowerTech (bán tại quầy và trực tuyến, số seri, kho chờ kiểm tra). |

## 3. Những câu giảng viên hay hỏi khi đọc mô tả

Gom từ nhận xét của nhiều nhóm; dùng làm checklist trước khi nộp mục 1.

1. **Thanh toán bằng cách nào?** D5/g12, g15, g16; D6/g1, g11, g15.
2. **Có đặt cọc không?** D5/g12; D6/g11, g13 ("Tiền cọc?").
3. **Trả, đổi, hủy, hoàn tiền thế nào, tính phí ra sao?** D5/g16 ("Trả tiền/Trả vé/Đổi suất/Hủy vé"); D6/g11 ("Trả vé thì tính phí ra sao?"); D5/g5 (hàng không đúng mô tả thì trả thế nào).
4. **Bảo hành, hóa đơn, linh kiện thay thế có bảo hành không?** D5/g12 (biên lai tính tiền, bảo hành); D6/g15; D6/g6 (PowerTech).
5. **Ai kiểm tra, ai duyệt, ai chịu trách nhiệm?** D6/g2 ("Ai ktra và xác thực thông tin để tránh lừa đảo"); D6/g4 ("Ai làm tester?"); D6/g10 ("điều tiết giao thông ai làm? CA hay GTVT?").
6. **Có chế tài khi khách lạm dụng không?** D5/g5 ("chế tài KH boom hàng").
7. **Xác thực danh tính người dùng thế nào?** D6/g11 (CCCD, QR, OCR); D6/g2.
8. **Con số giới hạn là bao nhiêu?** D5/g15 ("1 lần đặt mua tối đa mấy ghế?"); D6/g13 (thời gian thuê, giá, giá dịch vụ).
9. **Chi tiết cụ thể, đo được:** D5/g10 (mỗi món gồm nguyên liệu gì, trọng lượng bao nhiêu); D5/g14 (phiếu bữa ăn kèm chi tiết các món và hàm lượng); D5/g2 (đánh giá hoàn thành tách hai cột: tự đánh giá và lead đánh giá).
10. **Phân tách rõ đối tượng:** D5/g2 (công việc cá nhân và công việc chung, phân quyền, AI dùng ở đâu); D6/g13 (một khách thuê nhiều phòng theo từng hợp đồng).
11. **Xử lý trường hợp lệch:** D6/g9 (khám trái tuyến); D5/g12 (thiết bị không sửa được thì thay mới và phải hỏi ý khách); D5/g11 (kiểm tra sức khỏe để tránh bài tập quá sức).

Lời khen nguyên văn trong file nhận xét: "Ý tưởng hay" (D5/g2, g13; D6/g2, g3), "Đề tài hay" (D5/g10), "Đề tài mô tả hay" (D5/g14), "Đề tài này HAY" (D6/g10).

## 4. Báo cáo mẫu: đã đọc gì, học được gì, lỗi thấy được

Phạm vi đọc: **toàn văn** cho EduPlay, Fitness, HanGo, NutriCook, My Wallet và cả ba báo cáo D6. AI Task Manager: đọc mô tả, thực thể, 8 bảng đầu và phần kết (mọi bảng theo cùng một khuôn). GetGoals/OnThiToeic: đọc chương 1, 2, 4 và các quan hệ 1–3, 18–20, 24–25. FitTrack: đọc mô tả, thực thể, giả định, mối quan hệ, ràng buộc, quan hệ 4.1, 4.12 và chương 5–6; chưa đọc các quan hệ 4.2–4.11 và 4.13.

| Báo cáo | Điểm thấy ở file nhận xét | Có trong báo cáo | Điểm đáng học | Điểm yếu **[BC]** |
|---|---|---|---|---|
| **Giao thông đô thị** (D6/g10) | 7 | Mô tả, 3 loại thực thể, danh sách phụ thuộc hàm | Văn xuôi theo từng nhóm đối tượng, cuối đoạn có quy tắc ("một GPLX còn hiệu lực cho mỗi hạng"). Bảng nghiệp vụ có cột "thuộc tính thời gian" để chứng minh loại | Dừng ở phụ thuộc hàm. **[Nhận định]** `NGUOI_DIEU_KHIEN → SoGPLX` mâu thuẫn với việc một người có nhiều GPLX |
| **Giao tác và khóa, đặt vé** (D6/g3) | 7 | Như trên, thêm bảng tình huống đồng thời | Bảng "tình huống đồng thời, vấn đề, kỹ thuật xử lý" | Vẫn liệt kê `CHI_TIET_GIU_CHO` trong thực thể nghiệp vụ |
| **Tìm bạn đồng hành** (D6/g2) | 7 | Mô tả, thực thể, bản số, phụ thuộc hàm | Văn phong đời thường nhất; nêu rõ phạm vi ("chưa thu tiền", "chưa xác minh danh tính"); phụ thuộc hàm gồm cả khóa phụ UNIQUE | Tên bảng tiếng Anh, giá trị liệt kê tiếng Anh; có hàng lặp trong bảng đối tượng ngoài; mô tả có chi tiết thiết bị (QR, GPS) |
| **GetGoals / OnThiToeic** (D5/g3) | 7 | 25 quan hệ, mỗi quan hệ đủ F, phủ, khóa, 1NF–4NF | Tìm được quan hệ **3NF nhưng không BCNF**; tách ảnh/âm thanh và đồng nghĩa/ví dụ vì độc lập; tổng hợp 3NF 4, BCNF 13, 4NF 8, dạng chuẩn chung 3NF | Mô tả vẫn ghi tên cột, mã và khóa (trái lời nhắc của chính nhóm này). 3NF-không-BCNF đến từ thuộc tính dẫn xuất thêm vào "phép chiếu phục vụ phân tích". 4NF lập luận bằng "phụ thuộc đa trị tầm thường" sau khi đã tách; không thấy chứng minh phép tách |
| **FitTrack AI** (D5/g11) | 7 | 13 quan hệ, ràng buộc toàn vẹn, 11 giả định nghiệp vụ | Giả định nghiệp vụ nêu trước phân tích (một hồ sơ mỗi người, snapshot, giá trị tính toán không lưu). Nói rõ chưa đủ cơ sở kết luận 4NF. Ghi chú: nếu dinh dưỡng luôn tính từ giá trị chuẩn thì phải phân tích lại | Phụ thuộc hàm hầu hết `Id → tất cả`; không phân rã. Mô tả nêu Supabase, Gemini, Python |
| **Fitness & Lifestyle** (D5/g14) | 7 | Mô tả, 3 loại thực thể | Có đoạn phạm vi "xét... chưa xét..."; có lý do từng nhóm thực thể; giải thích ca tranh luận (danh mục nhỏ, BMI là dữ liệu tính, dashboard không lưu bảng) | Dừng ở thực thể. Mô tả có JWT, TensorFlow.js, MoveNet, React Native |
| **HanGo** (D5/g6) | 7 | 5 quan hệ, phân tích nghiệp vụ trước phụ thuộc hàm, PTT 3 bước, bảng khóa L/R/M, 1NF–BCNF | Trình bày PTT, tìm khóa và dạng chuẩn theo từng bảng; có khóa phụ Email | Mô tả in đậm tên cột và khóa. Tên cột không nhất quán (`Chuoi` và `ChuoiStreak`; `ThoiGian` và `ThoiGianPhut`). Chia "mạnh/yếu/kết hợp" thay vì 3 loại bài giảng. Nhận xét "tối ưu hóa tuyệt đối" quá mức |
| **NutriCook** (D5/g10) | 7 | Mô tả, 3 loại thực thể, 18 bảng phụ thuộc hàm, Fmin | Mô tả quy trình tủ lạnh, đi chợ, nấu ăn rất cụ thể | Liệt kê bảng liên kết N–N và bước thực hiện như thực thể nghiệp vụ (đúng lỗi giảng viên nhắc). PTT chỉ tách vế phải. **[Nhận định]** `BUOC_THUC_HIEN` có thể có khóa ứng viên (công thức, thứ tự bước) nhưng không xét |
| **EduPlay** (D5/g13) | 7 | 4 bảng, phụ thuộc hàm, PTT, khóa, dạng chuẩn | PTT bước 3 có nội dung thật (khóa phụ `email` và `room_code` làm một số phụ thuộc dư thừa). Giải thích rõ bảng nào có khóa phụ | Mô tả viết theo màn hình và công nghệ (IndexedDB, đăng nhập Google/Facebook). "Thực thể cơ bản" là danh mục giá trị. Cột JSON (`game_data`, `extra_data`) nhưng kết luận BCNF không bàn 1NF. Lỗi gõ (`room_cod`) |
| **My Wallet** (D5/g8) | 7 | Mô tả, thực thể, một phần phụ thuộc hàm | Mô tả rất đầy đủ chức năng | Mô tả ghi mã người dùng, mã danh mục (kiểu FK). Thực thể ghi kiểu và ràng buộc SQL. "Đối tượng ngoài" là Google, Apple, Facebook, Email. Một bảng bị dán lặp. Phần phụ thuộc hàm dừng sau `NGUOI_DUNG` |
| **AI Task Manager** (D5/g2) | 6 | 10 bảng, mỗi bảng có khóa, 1NF–BCNF, PTT | PTT làm đủ 3 bước, thử loại từng phụ thuộc bằng bao đóng, giải thích vì sao thuộc tính không phải khóa | Mọi phụ thuộc đều `Id → ...` nên 3 bước gần như trống; câu "đạt 2NF vì khóa Id một thuộc tính" lặp ở mọi bảng. Lỗi dán: phân tích bảng Project dùng thuộc tính của ProjectMember; bao đóng có `ProfilePicture` không có trong bảng; Fmin của ProjectTask có `DependsOnTaskId` không có trong bảng. Xếp `AspNetUser` vào cơ bản, bảng AI vào "thực thể ngoài" |

## 5. Điều rút ra về phần kỹ thuật

- **Không báo cáo mẫu nào có phân rã hoặc tổng hợp kèm chứng minh bảo toàn thông tin và bảo toàn phụ thuộc hàm**, cũng không có bảng tableau, ERD dạng hình, đồ thị quan hệ hay con đường truy xuất (tra từ khóa "bảo toàn", "phân rã" trên cả 11 file; chữ "phân rã" xuất hiện trong AI Task Manager chỉ là bước "phân rã vế phải"). **[Nhận định]** Đây là phần hướng dẫn của giảng viên yêu cầu và các mẫu để trống nên PowerTech có thể làm khác biệt, nhưng đồng thời chưa có mẫu nào cho thấy giảng viên chấm các phần này thế nào.
- **Sáu báo cáo có kết luận dạng chuẩn.** Năm báo cáo kết luận BCNF cho (hầu như) mọi bảng; chỉ GetGoals tìm ra bảng không đạt BCNF. Hầu hết tập phụ thuộc chỉ có dạng "khóa → tất cả thuộc tính", nên kết luận BCNF gần như hiển nhiên. Các báo cáo xét khóa phụ (`email`, cặp UNIQUE): EduPlay, HanGo, FitTrack, GetGoals và Tìm bạn đồng hành.
- **4NF:** GetGoals đạt 4NF cho 8 quan hệ; FitTrack nói rõ chưa đủ cơ sở để kết luận 4NF. Các báo cáo còn lại không nói đến 4NF.
- **Dữ liệu snapshot và cột tính toán:** FitTrack và Fitness nêu rõ giá trị lưu tại thời điểm ghi và dữ liệu tính toán không lưu. Đây là điểm trùng với bẫy của PowerTech (`UnitPrice`, `LineTotal`, `TotalAmount`, `StockQuantity`).
- **Thuật ngữ kỹ thuật trong mô tả:** JWT, TensorFlow.js, Supabase, IndexedDB xuất hiện trong các báo cáo đạt 7 mà giảng viên không nhận xét riêng (Fitness, FitTrack, NutriCook, EduPlay). Nhận xét "không đưa thuật ngữ CNTT, khóa, FK" chỉ ghi cho D5 nhóm 3, 4, 6, 7, 8, 9. **[Nhận định]** Không nên coi đó là cho phép; giữ mô tả thuần nghiệp vụ là cách an toàn.

## 6. Những chỗ bản cũ của file này sai hoặc chưa chính xác

| Bản cũ | Bản sửa |
|---|---|
| "12 báo cáo được 6 đến 7 điểm" | Có **11** báo cáo; điểm thấy ở file nhận xét: 10 báo cáo ở mức 7, AI Task Manager ở mức 6. Ý nghĩa cột số chưa xác nhận |
| Đường dẫn `CSDL-NC/BAO_CAO/D5` | `CSDL-NC/bao-cao-mau/D5` và `D6` |
| "Chỉ OnThiToeic và AI Task Manager nhắc nhiều đến phân rã/bảo toàn" | Không báo cáo nào phân rã hay chứng minh bảo toàn; AI Task Manager chỉ có bước "phân rã vế phải" |
| "Chỉ FitTrack và OnThiToeic nhắc đến 4NF" | Đúng về số lượng, nhưng khác nhau: GetGoals kết luận 4NF cho 8 quan hệ; FitTrack nói chưa đủ cơ sở. Chưa đọc đủ để đánh giá chất lượng chứng minh của GetGoals ngoài các quan hệ đã nêu ở mục 4 |
| "Chưa đọc kỹ từng phần chứng minh nên chưa đánh giá chất lượng" | Đã đọc thêm: xem mục 4 và 5 |
| "Giảng viên nhắc JWT, TensorFlow.js, PayOS ở nhiều nhóm" | Giảng viên không nhận xét riêng các báo cáo có những từ này (Fitness, NutriCook); lời nhắc về CNTT, khóa, FK nằm ở D5 nhóm 3, 4, 6, 7, 8, 9 |
| "Tìm khóa theo bảng L, R, M (HanGo)" | HanGo lập bảng L, R, M và D (tập nguồn, đích, trung gian, không xuất hiện). Bài giảng dùng N, M, D; tên thuật ngữ cần theo bài giảng mới nhất |
| "Đề tài giao tác/khóa được điểm nhờ bảng tình huống" | Giảng viên nhận xét "Ý tưởng hay" và yêu cầu tập trung cơ chế khóa; không có căn cứ trong hai file rằng bảng tình huống là lý do được điểm |

## 7. Áp vào báo cáo PowerTech

1. Mô tả viết văn xuôi như chủ cửa hàng kể, không có tên bảng, khóa, FK; nêu phạm vi một cửa hàng ngay đầu (D5/g14 làm tốt phần này).
2. Trả lời trực tiếp 11 câu ở mục 3, đặc biệt **đặt cọc** và **phí khi đổi trả hoặc hoàn tiền** (đã có trong Chương 1 hiện hành, xem mục 1), thanh toán, ai kiểm tra hàng trả, ai duyệt hoàn tiền, chế tài khách boom hàng.
3. Dòng đơn, dòng phiếu nhập, chi tiết giỏ là mối kết hợp; tồn kho, tổng tiền, doanh thu là dữ liệu tính toán; giới tính, điểm đánh giá là thuộc tính.
4. Hoàn tất 3 loại thực thể trước khi vẽ ERD và trước khi lập phụ thuộc hàm.
5. Tìm khóa đầy đủ, kể cả khóa ứng viên như `SKU`, `OrderCode`, `Email`, cặp UNIQUE; không dừng ở `Id`. Nêu các giả định nghiệp vụ (snapshot, cột tính toán) trước khi phân tích, như FitTrack.
6. Dành thời gian cho phân rã, chứng minh bảo toàn thông tin và phụ thuộc hàm, và tìm 4NF thật (ảnh và thông số sản phẩm) với chứng minh tính độc lập của hai tập giá trị. Chưa có mẫu nào làm phần này nên cần bám hướng dẫn của giảng viên và bài giảng mới nhất.
7. Mỗi bảng nêu lập luận dạng chuẩn riêng; tránh một câu lặp cho mọi bảng và tránh lỗi dán lẫn thuộc tính giữa các bảng.
