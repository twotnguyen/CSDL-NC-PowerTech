**ĐỀ TÀI: HỆ THỐNG WEB HỌC TIẾNG HÀN THÔNG MINH - HANGO**

**Thành viên thực hiện:**• Nguyễn Như Khuê – 2380601113
• Nguyễn Ngọc Khánh – 2380614602
• Lê Huỳnh Kim Thư – 2280603175

**1. Mô tả hệ thống**

Trong bối cảnh hội nhập quốc tế và làn sóng văn hóa Hàn Quốc (Hallyu) phát triển mạnh mẽ, nhu cầu học tiếng Hàn phục vụ cho học tập, du học và làm việc ngày càng tăng cao. Tuy nhiên, việc tự học tiếng Hàn theo các phương thức truyền thống qua sách vở hay các nền tảng rời rạc thường gặp nhiều rào cản lớn: học viên dễ xao nhãng mất tập trung, nhanh quên từ vựng do thiếu phương pháp ghi nhớ khoa học, thiếu môi trường luyện nói chuẩn bản xứ và các kỳ thi thử TOPIK chưa mô phỏng sát với thực tế. Chính vì vậy, Hệ thống Web học tiếng Hàn thông minh - HANGO được thiết kế và xây dựng như một giải pháp chuyển đổi số toàn diện trong lĩnh vực giáo dục ngoại ngữ. Mục tiêu cốt lõi của hệ thống là kết hợp hài hòa giữa các phương pháp học tập khoa học (kỹ thuật Pomodoro, lặp lại ngắt quãng SRS) với công nghệ Trí tuệ nhân tạo (AI) hiện đại, tạo ra một không gian học tập trực quan, cá nhân hóa và duy trì động lực bền bỉ cho người học.

Hệ thống Web học tiếng Hàn thông minh **HANGO** là một nền tảng học tập trực tuyến hoàn toàn miễn phí, được thiết kế nhằm số hóa toàn diện học liệu và hỗ trợ người học rèn luyện từ vựng, ngữ pháp cũng như luyện thi chứng chỉ TOPIK một cách có lộ trình và khoa học. Khi tham gia vào hệ thống, mỗi học viên được khởi tạo một tài khoản người dùng gắn liền với mã định danh (**UserID**) và địa chỉ **Email** duy nhất dùng để đăng nhập bảo mật; trong suốt quá trình học tập, hệ thống sẽ tự động theo dõi, tích lũy điểm kinh nghiệm (**DiemXP**), cập nhật chuỗi ngày học liên tục (**Chuoi**) trên bảng điều khiển cá nhân, đồng thời cho phép Ban quản trị dễ dàng quản lý danh sách và kiểm soát trạng thái hoạt động (**TrangThai**) của từng tài khoản học viên. Về phân hệ học liệu, hệ thống lưu trữ kho dữ liệu từ vựng phong phú (**TuVungID**) gồm từ gốc tiếng Hàn, phiên âm Romaja, nghĩa tiếng Việt, phân loại cấp độ TOPIK, câu ví dụ ngữ cảnh và file âm thanh phát âm chuẩn (**AudioUrl**). Kho học liệu này được quản trị viên quản lý linh hoạt, đặc biệt có thể nạp tự động hàng trăm từ mới vào cơ sở dữ liệu SQL Server từ file Excel/CSV chỉ với một thao tác.

Học viên sẽ tiếp cận từ vựng thông qua giao diện thẻ Flashcard 3D sinh động, cho phép lật mặt trước để xem từ, mặt sau để xem nghĩa và bấm nghe phát âm mẫu, sau đó học viên tự đánh giá mức độ ghi nhớ của bản thân qua ba lựa chọn "Quên - Khó - Nhớ" (**MucDoNho**); ngay lập tức, hệ thống sẽ tạo mới hoặc cập nhật bản ghi tiến độ (**TIENDO**) tương ứng với cặp khóa {UserID, TuVungID}, đồng thời áp dụng thuật toán lặp lại ngắt quãng (SRS) để tự động tính toán số ngày dãn cách (**KhoangCachNgay**) và lên lịch chính xác ngày nhắc ôn tập tiếp theo (**NgayOnTiepTheo**) nhằm giúp học viên ôn lại đúng thời điểm vàng của trí nhớ. Bên cạnh việc trau dồi từ vựng, học viên có thể tham gia thi thử với ngân hàng đề thi TOPIK I và TOPIK II (**DeThiID**) có quy định thời lượng làm bài cụ thể (**ThoiGian**) và tổng số câu hỏi, mỗi đề thi được cấu thành từ tập hợp các câu hỏi trắc nghiệm (**CAUHOI**) được định danh duy nhất theo mã đề và số thứ tự câu (**STTCau**), lưu trữ đầy đủ nội dung, bốn phương án lựa chọn, đáp án chính xác (**DapAnDung**), lời giải thích chi tiết (**GiaiThich**) và file âm thanh (**AudioUrl**) cho phần Nghe.

Học viên vào làm bài có đồng hồ đếm ngược theo thời gian thực, bấm nghe audio trực tiếp trong từng câu hỏi và chọn đáp án, khi nộp bài hệ thống sẽ tự động so khớp để chấm điểm ngay tức thì, bôi màu nhận diện câu đúng/sai và mở ra khung giải thích chi tiết cho từng câu hỏi. Để tối ưu hóa trải nghiệm tự học mỗi ngày, hệ thống còn mang đến không gian học tập ảo (Virtual Study Room) tích hợp đồng hồ Pomodoro giúp học viên quản lý chu kỳ tập trung 25 phút, bộ trộn âm thanh môi trường Ambient Mixer cho phép tùy chỉnh âm lượng nhạc Lofi, tiếng mưa hay tiếng quán cà phê theo sở thích, cùng bảng To-do List để học viên tự lập và đánh dấu hoàn thành mục tiêu học trong ngày; song song đó là các công cụ Trí tuệ nhân tạo (AI) miễn phí hỗ trợ học viên thu âm giọng đọc qua micro để phân tích và chấm điểm phát âm trực tiếp theo từng âm tiết, cũng như tính năng Chatbot đóng vai giao tiếp tiếng Hàn theo các tình huống thực tế với khả năng tự động phát hiện và gợi ý chỉnh sửa lỗi sai ngữ pháp một cách thông minh.

**2. Xác định 3 loại thực thể cùng thuộc tính**

**a) Thực thể mạnh (Thực thể cơ bản)**

**• Thực thể NGUOIDUNG:** Bảng mô tả thuộc tính thực thể NGUOIDUNG (Người dùng / Học viên):

| **Thuộc Tính** | **Kiểu Dữ Liệu** | **Khóa** | **Ý Nghĩa / Mô Tả** |
| --- | --- | --- | --- |
| UserID | VARCHAR(50) | PK | Mã định danh duy nhất của học viên trong hệ thống |
| Email | VARCHAR(100) | Unique | Địa chỉ email dùng để đăng nhập và nhận thông báo |
| MatKhauHash | VARCHAR(255) | - | Mật khẩu tài khoản đã được băm bảo mật |
| HoTen | NVARCHAR(100) | - | Họ và tên đầy đủ của học viên |
| DiemXP | INT | - | Điểm kinh nghiệm tích lũy khi học bài và thi thử |
| Chuoi | INT | - | Chuỗi số ngày học liên tục để duy trì động lực |
| TrangThai | TINYINT | - | Trạng thái tài khoản (1: Hoạt động, 0: Bị khóa) |

**• Thực thể TUVUNG:** Bảng mô tả thuộc tính thực thể TUVUNG (Kho từ vựng tiếng Hàn):

| **Thuộc Tính** | **Kiểu Dữ Liệu** | **Khóa** | **Ý Nghĩa / Mô Tả** |
| --- | --- | --- | --- |
| TuVungID | VARCHAR(50) | PK | Mã định danh duy nhất của từ vựng |
| TuTiengHan | NVARCHAR(100) | - | Từ gốc viết bằng chữ tiếng Hàn (Hangul) |
| NghiaTiengViet | NVARCHAR(255) | - | Ý nghĩa giải thích từ vựng bằng tiếng Việt |
| PhienAm | VARCHAR(100) | - | Phiên âm cách đọc Latinh chuẩn (Romaja) |
| CapDoTOPIK | TINYINT | - | Cấp độ phân loại từ vựng theo TOPIK (1 đến 6) |
| ViDu | NVARCHAR(500) | - | Câu ví dụ minh họa ngữ cảnh sử dụng kèm nghĩa |
| AudioUrl | VARCHAR(255) | - | Đường dẫn file âm thanh phát âm mẫu của người bản xứ |

**• Thực thể DETHI:** Bảng mô tả thuộc tính thực thể DETHI (Ngân hàng đề thi TOPIK):

| **Thuộc Tính** | **Kiểu Dữ Liệu** | **Khóa** | **Ý Nghĩa / Mô Tả** |
| --- | --- | --- | --- |
| DeThiID | VARCHAR(50) | PK | Mã định danh duy nhất của đề thi |
| TenDeThi | NVARCHAR(200) | - | Tên đề thi (ví dụ: Đề thi thử TOPIK I số 01) |
| ThoiGian | INT | - | Thời lượng làm bài quy định (tính theo phút) |
| CapDoTOPIK | TINYINT | - | Cấp độ kỳ thi TOPIK (1: TOPIK I, 2: TOPIK II) |
| TongSoCau | INT | - | Tổng số lượng câu hỏi trắc nghiệm có trong đề |

**b) Thực thể yếu (Thực thể phụ thuộc)**

**• Thực thể CAUHOI:** Bảng mô tả thuộc tính thực thể CAUHOI (Thuộc đề thi DETHI):

| **Thuộc Tính** | **Kiểu Dữ Liệu** | **Khóa** | **Ý Nghĩa / Mô Tả** |
| --- | --- | --- | --- |
| DeThiID | VARCHAR(50) | PK, FK | Mã đề thi chứa câu hỏi (khóa ngoại trỏ về DETHI) |
| STTCau | INT | PK | Số thứ tự câu hỏi trong đề (Khóa bộ phận) |
| NoiDung | NVARCHAR(MAX) | - | Nội dung câu hỏi trắc nghiệm |
| DapAnA | NVARCHAR(255) | - | Nội dung lựa chọn A |
| DapAnB | NVARCHAR(255) | - | Nội dung lựa chọn B |
| DapAnC | NVARCHAR(255) | - | Nội dung lựa chọn C |
| DapAnD | NVARCHAR(255) | - | Nội dung lựa chọn D |
| DapAnDung | CHAR(1) | - | Đáp án chính xác (A, B, C hoặc D) |
| GiaiThich | NVARCHAR(MAX) | - | Lời giải thích chi tiết lý do đáp án đúng |
| AudioUrl | VARCHAR(255) | - | Đường dẫn file âm thanh MP3 cho câu hỏi Nghe |

**c) Thực thể kết hợp**

**• Thực thể TIENDO:** Bảng mô tả thuộc tính thực thể TIENDO (Tiến độ học giữa NGUOIDUNG và TUVUNG):

| **Thuộc Tính** | **Kiểu Dữ Liệu** | **Khóa** | **Ý Nghĩa / Mô Tả** |
| --- | --- | --- | --- |
| UserID | VARCHAR(50) | PK, FK | Mã học viên (khóa ngoại trỏ về NGUOIDUNG) |
| TuVungID | VARCHAR(50) | PK, FK | Mã từ vựng (khóa ngoại trỏ về TUVUNG) |
| MucDoNho | TINYINT | - | Mức độ ghi nhớ phản hồi (0: Quên, 1: Khó, 2: Nhớ) |
| KhoangCachNgay | INT | - | Số ngày dãn cách cho lần ôn tập kế tiếp |
| NgayOnTiepTheo | DATE | - | Mốc thời gian hệ thống sẽ nhắc học viên ôn lại |
| NgayCapNhat | DATETIME | - | Thời điểm học viên bấm nút đánh giá gần nhất |

**Bảng tổng hợp các thực thể và thuộc tính**

| **Tên Thực Thể** | **Loại Thực Thể** | **Danh Sách Thuộc Tính** | **Khóa Chính (PK)** | **Khóa Ngoại (FK)** |
| --- | --- | --- | --- | --- |
| NGUOIDUNG | Thực thể mạnh | UserID, Email, MatKhauHash, HoTen, DiemXP, ChuoiStreak, TrangThai | UserID | Không có |
| TUVUNG | Thực thể mạnh | TuVungID, TuTiengHan, NghiaTiengViet, PhienAm, CapDoTOPIK, ViDu, AudioUrl | TuVungID | Không có |
| DETHI | Thực thể mạnh | DeThiID, TenDeThi, ThoiGianPhut, CapDoTOPIK, TongSoCau | DeThiID | Không có |
| CAUHOI | Thực thể yếu | DeThiID, STTCau, NoiDung, DapAnA, DapAnB, DapAnC, DapAnD, DapAnDung, GiaiThich, AudioUrl | {DeThiID, STTCau} | DeThiID (trỏ DETHI) |
| TIENDO | Thực thể kết hợp | UserID, TuVungID, MucDoNho, KhoangCachNgay, NgayOnTiepTheo, NgayCapNhat | {UserID, TuVungID} | UserID (NGUOIDUNG) TuVungID (TUVUNG) |

**3. Xác định tập phụ thuộc hàm của từng bảng**

Dựa vào các quy tắc nghiệp vụ thực tế trong quá trình vận hành hệ thống HANGO, tập phụ thuộc hàm (F) của từng quan hệ được xác định như sau:

**3.1. Bảng NGUOIDUNG**

**• Tập thuộc tính:** U1 = { UserID, Email, MatKhauHash, HoTen, DiemXP, ChuoiStreak, TrangThai }

**• Phân tích nghiệp vụ 1:** Mỗi người dùng được cấp một mã duy nhất UserID xác định toàn bộ thông tin cá nhân và dữ liệu tích lũy.

**• Phân tích nghiệp vụ 2:** Địa chỉ Email của mỗi người dùng là độc nhất trong hệ thống, được dùng để đăng nhập nên Email cũng xác định duy nhất toàn bộ thông tin tài khoản.

**f1:** UserID → Email, MatKhauHash, HoTen, DiemXP, ChuoiStreak, TrangThai

**f2:** Email → UserID, MatKhauHash, HoTen, DiemXP, ChuoiStreak, TrangThai

**3.2. Bảng TUVUNG**

**• Tập thuộc tính:** U2 = { TuVungID, TuTiengHan, NghiaTiengViet, PhienAm, CapDoTOPIK, ViDu, AudioUrl }

**• Phân tích nghiệp vụ:** Mỗi từ vựng có một mã số TuVungID duy nhất trong từ điển hệ thống, từ mã này xác định chính xác từ vựng, phiên âm, nghĩa tiếng Việt, cấp độ TOPIK, ví dụ minh họa và link phát âm.

**f1:** TuVungID → TuTiengHan, NghiaTiengViet, PhienAm, CapDoTOPIK, ViDu, AudioUrl

**3.3. Bảng DETHI**

**• Tập thuộc tính:** U\_DT = { DeThiID, TenDeThi, ThoiGianPhut, CapDoTOPIK, TongSoCau }

**• Phân tích nghiệp vụ:** Mã đề thi DeThiID xác định duy nhất tên đề thi, thời gian làm bài, cấp độ và số lượng câu hỏi.

**f1:** DeThiID → TenDeThi, ThoiGianPhut, CapDoTOPIK, TongSoCau

**3.4. Bảng CAUHOI (Thực thể yếu)**

**• Tập thuộc tính:** U3 = { DeThiID, STTCau, NoiDung, DapAnA, DapAnB, DapAnC, DapAnD, DapAnDung, GiaiThich, AudioUrl }

**• Phân tích nghiệp vụ:** Một câu hỏi chỉ được xác định duy nhất khi biết chính xác câu đó thuộc đề thi nào (DeThiID) và có số thứ tự là bao nhiêu (STTCau). Riêng lẻ từng thuộc tính không thể xác định nội dung.

**f1:** {DeThiID, STTCau} → NoiDung, DapAnA, DapAnB, DapAnC, DapAnD, DapAnDung, GiaiThich, AudioUrl

**3.5. Bảng TIENDO (Thực thể kết hợp)**

**• Tập thuộc tính:** U4 = { UserID, TuVungID, MucDoNho, KhoangCachNgay, NgayOnTiepTheo, NgayCapNhat }

**• Phân tích nghiệp vụ:** Cặp {UserID, TuVungID} xác định duy nhất mức độ ghi nhớ hiện tại, chu kỳ giãn cách ngày ôn và mốc ngày cần nhắc ôn tập tiếp theo của người dùng đối với từ vựng đó.

**f1:** {UserID, TuVungID} → MucDoNho, KhoangCachNgay, NgayOnTiepTheo, NgayCapNhat

**4. Tìm phủ tối tiểu của từng bảng**

Theo lý thuyết cơ sở dữ liệu, một tập phụ thuộc hàm Fc được gọi là Phủ tối tiểu (Minimal Cover / Canonical Cover) khi thỏa mãn 3 điều kiện: (1) Vế phải của mọi phụ thuộc hàm chỉ chứa đúng một thuộc tính đơn lẻ; (2) Không tồn tại thuộc tính dư thừa ở vế trái; (3) Không tồn tại phụ thuộc hàm dư thừa trong tập.

**4.1. Tìm phủ tối tiểu của bảng NGUOIDUNG**

**• Bước 1:** Tách các phụ thuộc hàm vế phải thành thuộc tính đơn lẻ:

UserID → Email; UserID → MatKhauHash; UserID → HoTen; UserID → DiemXP; UserID → ChuoiStreak; UserID → TrangThai.

Email → UserID; Email → MatKhauHash; Email → HoTen; Email → DiemXP; Email → ChuoiStreak; Email → TrangThai.

**• Bước 2:** Tất cả các phụ thuộc hàm đều có vế trái là một thuộc tính đơn (UserID hoặc Email), do đó không có thuộc tính dư thừa ở vế trái.

**• Bước 3:** Loại bỏ phụ thuộc hàm dư thừa qua tính toán bao đóng:

Xét Email → MatKhauHash: Có Email → UserID và UserID → MatKhauHash nên (Email)+ chứa MatKhauHash => Dư thừa, loại bỏ.

Tương tự loại bỏ: Email → HoTen, Email → DiemXP, Email → ChuoiStreak, Email → TrangThai.

Kiểm tra UserID → Email và Email → UserID: Cả hai đều không thể bị loại bỏ vì không thể dẫn xuất gián tiếp.

**• Kết luận Phủ tối tiểu F1c:** F1c = { UserID → Email, UserID → MatKhauHash, UserID → HoTen, UserID → DiemXP, UserID → ChuoiStreak, UserID → TrangThai, Email → UserID }

**4.2. Tìm phủ tối tiểu của bảng TUVUNG**

**• Bước 1:** Tách vế phải thành thuộc tính đơn lẻ: TuVungID → TuTiengHan, TuVungID → NghiaTiengViet, TuVungID → PhienAm, TuVungID → CapDoTOPIK, TuVungID → ViDu, TuVungID → AudioUrl.

**• Bước 2:** Vế trái là khóa đơn TuVungID => Không dư thừa vế trái.

**• Bước 3:** Không có phụ thuộc hàm nào suy ra được từ các phụ thuộc hàm còn lại => Không có PTH dư thừa.

**• Kết luận Phủ tối tiểu F2c:** F2c = { TuVungID → TuTiengHan, TuVungID → NghiaTiengViet, TuVungID → PhienAm, TuVungID → CapDoTOPIK, TuVungID → ViDu, TuVungID → AudioUrl }

**4.3. Tìm phủ tối tiểu của bảng CAUHOI**

**• Bước 1:** Tách vế phải: {DeThiID, STTCau} → NoiDung; {DeThiID, STTCau} → DapAnA; ...; {DeThiID, STTCau} → AudioUrl.

**• Bước 2:** Vế trái {DeThiID, STTCau} không thể bỏ bớt bất kỳ thuộc tính nào vì (DeThiID)+ và (STTCau)+ riêng lẻ không thể xác định được nội dung câu hỏi => Không dư thừa vế trái.

**• Bước 3:** Không có phụ thuộc hàm nào dư thừa.

**• Kết luận Phủ tối tiểu F3c:** F3c gồm 8 phụ thuộc hàm có vế trái là {DeThiID, STTCau} trỏ tới từng thuộc tính đơn lẻ ở vế phải.

**4.4. Tìm phủ tối tiểu của bảng TIENDO**

**• Bước 1:** Tách vế phải thành thuộc tính đơn: {UserID, TuVungID} → MucDoNho; {UserID, TuVungID} → KhoangCachNgay; {UserID, TuVungID} → NgayOnTiepTheo; {UserID, TuVungID} → NgayCapNhat.

**• Bước 2:** Vế trái {UserID, TuVungID} không có thuộc tính dư thừa vì cần cả người học và từ vựng mới xác định được tiến độ.

**• Bước 3:** Không có phụ thuộc hàm dư thừa.

**• Kết luận Phủ tối tiểu F4c:** F4c = { {UserID, TuVungID} → MucDoNho, {UserID, TuVungID} → KhoangCachNgay, {UserID, TuVungID} → NgayOnTiepTheo, {UserID, TuVungID} → NgayCapNhat }

**5. Xác định khóa của từng bảng**

Thuật toán xác định khóa dựa trên phân loại thuộc tính thành các tập L (chỉ ở vế trái), R (chỉ ở vế phải), M (ở cả hai vế), D (không ở vế nào) và tiến hành tính toán bao đóng:

| **Tên Bảng** | **Tập Nguồn (L)** | **Tập Đích (R)** | **Tập Trung Gian (M)** | **Bao Đóng & Khóa Ứng Viên** | **Khóa Chính Được Chọn** |
| --- | --- | --- | --- | --- | --- |
| NGUOIDUNG | ∅ | {MatKhauHash, HoTen, DiemXP, ChuoiStreak, TrangThai} | {UserID, Email} | (UserID)+ = U1 => K1 = {UserID} (Email)+ = U1 => K2 = {Email} | UserID |
| TUVUNG | {TuVungID} | {TuTiengHan, NghiaTiengViet, PhienAm, CapDoTOPIK, ViDu, AudioUrl} | ∅ | (TuVungID)+ = U2 => Duy nhất 1 khóa K = {TuVungID} | TuVungID |
| DETHI | {DeThiID} | {TenDeThi, ThoiGianPhut, CapDoTOPIK, TongSoCau} | ∅ | (DeThiID)+ = U\_DT => Duy nhất 1 khóa K = {DeThiID} | DeThiID |
| CAUHOI | {DeThiID, STTCau} | {NoiDung, DapAnA, DapAnB, DapAnC, DapAnD, DapAnDung, GiaiThich, AudioUrl} | ∅ | ({DeThiID, STTCau})+ = U3 => Duy nhất 1 khóa K = {DeThiID, STTCau} | {DeThiID, STTCau} |
| TIENDO | {UserID, TuVungID} | {MucDoNho, KhoangCachNgay, NgayOnTiepTheo, NgayCapNhat} | ∅ | ({UserID, TuVungID})+ = U4 => Duy nhất 1 khóa K = {UserID, TuVungID} | {UserID, TuVungID} |

**6. Xác định dạng chuẩn của từng bảng**

Tiến hành kiểm tra tuần tự các tiêu chuẩn từ 1NF đến BCNF cho từng bảng quan hệ:

**6.1. Bảng NGUOIDUNG**

**• Kiểm tra 1NF:** Mọi trường dữ liệu đều nguyên tố, đơn trị, không có nhóm lặp => Đạt 1NF.

**• Kiểm tra 2NF:** Hai khóa ứng viên UserID và Email đều là khóa đơn, không có phụ thuộc một phần vào khóa => Đạt 2NF.

**• Kiểm tra 3NF:** Mọi thuộc tính không khóa đều phụ thuộc trực tiếp vào khóa, không có phụ thuộc bắc cầu => Đạt 3NF.

**• Kiểm tra BCNF:** Mọi phụ thuộc hàm không tầm thường đều có vế trái là UserID hoặc Email (đều là siêu khóa) => Đạt BCNF.

**6.2. Bảng TUVUNG**

**• Kiểm tra 1NF:** Các thuộc tính đều đơn trị và nguyên tố => Đạt 1NF.

**• Kiểm tra 2NF:** Khóa chính là khóa đơn TuVungID => Đạt 2NF.

**• Kiểm tra 3NF:** Không có phụ thuộc hàm bắc cầu giữa các thuộc tính không khóa => Đạt 3NF.

**• Kiểm tra BCNF:** Vế trái duy nhất là TuVungID (siêu khóa) => Đạt BCNF.

**6.3. Bảng DETHI**

**• Kiểm tra 1NF:** Các thuộc tính đều nguyên tố => Đạt 1NF.

**• Kiểm tra 2NF:** Khóa chính là khóa đơn DeThiID => Đạt 2NF.

**• Kiểm tra 3NF & BCNF:** Vế trái của phụ thuộc hàm là DeThiID (siêu khóa) => Đạt 3NF và BCNF.

**6.4. Bảng CAUHOI**

**• Kiểm tra 1NF:** Các cột lưu dữ liệu nguyên tố => Đạt 1NF.

**• Kiểm tra 2NF:** Khóa chính là {DeThiID, STTCau}. Tất cả các thuộc tính ngoài khóa đều phụ thuộc đầy đủ vào toàn bộ khóa chính => Đạt 2NF.

**• Kiểm tra 3NF:** Không có phụ thuộc hàm bắc cầu => Đạt 3NF.

**• Kiểm tra BCNF:** Vế trái {DeThiID, STTCau} là siêu khóa của quan hệ => Đạt BCNF.

**6.5. Bảng TIENDO**

**• Kiểm tra 1NF:** Các trường MucDoNho, KhoangCachNgay, NgayOnTiepTheo đều nguyên tố => Đạt 1NF.

**• Kiểm tra 2NF:** Khóa chính là {UserID, TuVungID}. Mọi thuộc tính tiến độ phụ thuộc đầy đủ vào toàn bộ khóa chính => Đạt 2NF.

**• Kiểm tra 3NF:** Không có phụ thuộc bắc cầu giữa các thuộc tính không khóa => Đạt 3NF.

**• Kiểm tra BCNF:** Vế trái {UserID, TuVungID} là siêu khóa => Đạt BCNF.

**7. Dạng chuẩn của cả lược đồ**

| **STT** | **Tên Lược Đồ Quan Hệ (Bảng)** | **Khóa Chính (PK)** | **Dạng Chuẩn Đạt Được** | **Đánh Giá** |
| --- | --- | --- | --- | --- |
| 1 | NGUOIDUNG | UserID | BCNF | Không dư thừa dữ liệu, không dị thường |
| 2 | TUVUNG | TuVungID | BCNF | Dữ liệu từ vựng tối ưu hóa tuyệt đối |
| 3 | DETHI | DeThiID | BCNF | Chuẩn hóa độc lập |
| 4 | CAUHOI | {DeThiID, STTCau} | BCNF | Bảo toàn toàn vẹn tham chiếu thực thể yếu |
| 5 | TIENDO | {UserID, TuVungID} | BCNF | Tối ưu hóa bảng kết hợp N - N |

**KẾT LUẬN**

Vì tất cả các bảng thành phần trong cơ sở dữ liệu đều đạt chuẩn BCNF, nên toàn bộ lược đồ cơ sở dữ liệu của dự án HANGO đạt dạng chuẩn BOYCE-CODD (BCNF).