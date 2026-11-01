Trần Trọng Bằng 2380600189

Lê Hoàng Mỹ 2380601381

Nguyễn Tất Khoa 2380601071

**CHƯƠNG 1. MÔ TẢ HỆ THỐNG Al Hỗ Trợ Ôn Toeic GETGOALS**

## 1.1. Bối cảnh, nghiệp vụ và phạm vi khảo sát

Trong những năm gần đây, việc học tiếng Anh và luyện thi TOEIC không còn giới hạn ở các lớp ôn tập cố định. Người học thường phải tự tìm đề, xác định trình độ, ghi lại câu sai rồi lựa chọn nội dung cần ôn. Khi kết quả làm bài, ghi chú và kế hoạch học tập nằm ở nhiều nơi khác nhau, việc đánh giá tiến bộ dễ thiếu liên tục. Vì vậy, nhóm xây dựng GetGoals nhằm tập trung các hoạt động luyện thi trên một hệ thống, giúp mỗi người học có cơ sở dữ liệu học tập xuyên suốt từ đánh giá ban đầu đến luyện tập và theo dõi kết quả.

GetGoals là ứng dụng hỗ trợ học tiếng Anh và ôn TOEIC trên web và thiết bị di động. Nội dung chính bao gồm kiểm tra đầu vào, luyện tập theo câu hỏi, thi thử, xem lại câu cần ôn, thẻ ghi nhớ từ vựng, lộ trình học theo kỹ năng và trao đổi với công cụ hỗ trợ giải thích. Những chức năng này dùng chung thông tin người dùng và ngân hàng câu hỏi, nhưng tạo ra các bản ghi nghiệp vụ khác nhau. Đối với báo cáo cơ sở dữ liệu nâng cao, nhóm tập trung vào 25 quan hệ thể hiện phần dữ liệu cần được giữ ổn định, tra cứu được và liên kết được giữa các hoạt động.

Mỗi người học có một MaNguoiDung không trùng lặp để quản lý hồ sơ. Người học có thể sử dụng thông tin đăng nhập được lưu trong hệ thống hoặc định danh từ nhà cung cấp đăng nhập bên ngoài. Hồ sơ quản lý HoTen, Email, MatKhauMaHoa, NhaCungCapDangNhap, MaNguoiDungNhaCungCap, DiemMucTieu, NgayThiDuKien, SoPhutHocMoiNgay, NgonNgu, CheDoGiaoDien, BatThongBaoEmail và TaoLuc. Email là thông tin tài khoản duy nhất theo quy tắc của lược đồ. Họ tên hoặc điểm mục tiêu không dùng để phân biệt người học vì có thể trùng và có thể thay đổi. Một người học có thể làm bài nhiều lần, có nhiều cuộc trao đổi, nhiều lộ trình và nhiều đơn thanh toán theo thời gian.

Ngân hàng TOEIC gồm các bộ đề và các nhóm ngữ liệu. BoDeToeic lưu MaBoDe, TenBoDe, LoaiBoDe, PhanThi, MoTa và DangHoatDong để mô tả phạm vi sử dụng của bộ đề. Một bộ đề có thể bao gồm nhiều nhóm. Mỗi NhomNguLieuToeic có MaNhomNguLieu, MaBoDe, PhanThi, TieuDe, NoiDung và ThuTu. Cặp MaBoDe và ThuTu không được trùng để giữ trật tự các nhóm trong cùng bộ đề; ThuTu được phép lặp ở các bộ đề khác nhau. PhanThi của bộ đề thể hiện phạm vi của toàn bộ đề, còn PhanThi của nhóm biểu thị phần mà nhóm đó thực sự phục vụ. Một bộ đề hỗn hợp có thể có các nhóm thuộc phần Nghe hiểu và Đọc hiểu nên không lấy riêng MaBoDe để suy ra PhanThi của từng nhóm.

Một nhóm ngữ liệu chứa các câu hỏi TOEIC. Mỗi câu trong CauHoiToeic có MaCauHoi, MaNhomNguLieu, MaKyNang, SoThuTuCau, DoKho, NoiDungCauHoi, GiaiThich và DangHoatDong. Câu hỏi chỉ nằm ở một nhóm trong thiết kế quan hệ đang phân tích, nhưng một nhóm có thể có nhiều câu. Cặp MaNhomNguLieu và SoThuTuCau phân biệt vị trí câu hỏi trong chính nhóm đó. MaKyNang liên kết câu hỏi đến kỹ năng được dùng để đánh giá; nhiều câu có thể cùng thuộc một kỹ năng. Thông tin độ khó, nội dung và lời giải được quản lý tại câu hỏi, không sao chép xuống từng lần làm bài.

Mỗi câu hỏi trắc nghiệm được trình bày cùng nhiều phương án. LuaChonCauHoi lưu riêng từng phương án bằng MaLuaChon, MaCauHoi, KyHieu, NoiDung, LaDapAnDung và ThuTu. Trong một câu hỏi, ký hiệu lựa chọn như A, B, C, D chỉ dùng một lần, nên cặp MaCauHoi và KyHieu cũng phân biệt được một phương án. Nội dung phương án và dấu hiệu đúng sai gắn với chính phương án đó; chúng không thể hoán đổi tùy ý giữa các ký hiệu của cùng một câu.

Câu hỏi TOEIC có thể dùng hình, âm thanh hoặc nội dung đọc đi kèm. TaiNguyenAnh(LoaiDoiTuong, MaDoiTuong, DuongDanAnh) lưu các tệp hình; TaiNguyenAmThanh(LoaiDoiTuong, MaDoiTuong, DuongDanAmThanh) lưu các tệp âm thanh. LoaiDoiTuong và MaDoiTuong xác định câu hỏi hoặc nhóm ngữ liệu được gắn tài nguyên. Mỗi dòng lưu đúng một đường dẫn và hai danh sách thay đổi độc lập, không tạo tích các cặp ảnh–âm thanh.

Các câu hỏi được phân loại theo KyNangToeic. Mỗi kỹ năng có MaKyNang, TenKyNang, LoaiKyNang và MaKyNangCha nếu là kỹ năng con. Một kỹ năng cha có thể có nhiều kỹ năng con, còn một kỹ năng con có tối đa một kỹ năng cha trong cấu trúc hiện tại. MaKyNang là định danh; tên kỹ năng có thể trùng về cách diễn đạt nên không được dùng làm khóa. Danh mục kỹ năng phục vụ ngân hàng câu hỏi, kết quả chẩn đoán và lộ trình học, nhưng việc một kỹ năng được tham chiếu ở nhiều nơi không đồng nghĩa các tập tham chiếu đó nằm trong bảng KyNangToeic.

Người học có thể bắt đầu bằng bài kiểm tra đầu vào. Hệ thống tạo một LanLamBai gắn với MaNguoiDung và MaBoDe; bản ghi này quản lý MaLanLamBai, LoaiLanLam, TrangThai, ThoiGianLamGiay, BatDauLuc và NopBaiLuc. Cùng một cách lưu lịch sử được sử dụng cho hoạt động luyện tập, kiểm tra ngắn hoặc thi thử vì các hoạt động này đều có người thực hiện, phiên làm bài và danh sách câu hỏi được đưa vào phiên. Một tài khoản có thể tạo nhiều lần làm bài, kể cả khi dùng lại cùng bộ đề.

Chi tiết của một lần làm bài được đặt trong CauHoiLanLamBai. Mỗi MaChiTiet gắn một MaLanLamBai với một MaCauHoi, lưu KyHieuDaChon, ThuTu, DaDanhDau và ThoiGianTraLoiGiay. Trong một lần làm bài, mỗi vị trí ThuTu chỉ dành cho một dòng chi tiết; cùng vị trí có thể xuất hiện ở các lần làm bài khác nhau. Khi người học đổi phương án hoặc đánh dấu câu hỏi, phần phát sinh được ghi nhận ở chi tiết phiên, không sửa nội dung gốc của ngân hàng câu hỏi. Thông tin đúng sai được suy từ lựa chọn và đáp án của câu hỏi thay vì lưu một bản sao đáp án trong mọi chi tiết.

Khi hoàn thành lượt kiểm tra chẩn đoán, KetQuaChanDoan ghi theo MaLanLamBai các giá trị Theta, DiemUocLuong và DiemToeicThuc. Mỗi lượt chẩn đoán có tối đa một bản kết quả gắn với chính mã lượt làm bài. Hệ thống còn xác định những kỹ năng yếu theo từng lượt. KyNangYeuChanDoan quản lý cặp MaLanLamBai và MaKyNang cùng MucDoYeu. Một lượt có thể có nhiều kỹ năng yếu và một kỹ năng có thể được nhận diện là yếu ở nhiều lượt khác nhau; mức độ yếu thuộc về đúng cặp lượt và kỹ năng, không phải một giá trị chung cho toàn bộ lượt.

Sau khi làm bài, người học có thể mở lại câu chưa chắc chắn hoặc câu trả lời sai. MucOnTap lưu MaMucOnTap, MaNguoiDung, MaCauHoi, MaLanLamBaiNguon, LyDoOnTap, TrangThai, ThemLuc và OnTapLuc. Mỗi mục là một nhu cầu ôn tập phát sinh riêng nên cùng người học và cùng câu hỏi vẫn có thể tạo nhiều mục ở những thời điểm hoặc lượt làm bài khác nhau. Thông tin nguồn giúp quay lại ngữ cảnh ban đầu. Trạng thái và thời điểm ôn giúp phân biệt mục còn chờ với mục đã hoàn thành.

Bên cạnh việc đưa câu vào danh sách ôn, người học có thể ghi chú, đánh dấu hoặc tô sáng nội dung. TuongTacCauHoi giữ MaTuongTac, MaNguoiDung, MaCauHoi, LoaiTuongTac, NoiDung, ViTriBatDau, ViTriKetThuc, MauSac và TaoLuc. Một thao tác gắn với một người học và một câu hỏi. Nội dung được dùng cho ghi chú; vị trí và màu phục vụ tô sáng. Các trường chỉ áp dụng cho một loại thao tác có thể để trống ở thao tác khác; một giá trị trống không phải là danh sách đa trị. Những tương tác này không làm thay đổi câu hỏi chung.

Thông tin mục tiêu và kết quả chẩn đoán được sử dụng để lập lộ trình học. Mỗi LoTrinhHoc có MaLoTrinh, MaNguoiDung, TieuDe, DiemMucTieu, NgayBatDau, TrangThai và TaoLuc. Một người dùng có thể tạo hoặc được cập nhật nhiều lộ trình ở các giai đoạn học khác nhau. Từng lộ trình được chia thành các tuần lưu trong TuanLoTrinh; mỗi tuần có MaTuan, MaLoTrinh, SoTuan, TieuDe, MoTa, SoCauDeXuat, SoPhutDuKien và TrangThai. Trong một lộ trình, SoTuan không được lặp. Số tuần tương tự ở những lộ trình khác nhau không xác định cùng một bản ghi tuần.

Một tuần học thường phải tập trung vào nhiều kỹ năng. KyNangConTuanLoTrinh lưu cặp MaTuan và MaKyNang, kèm MucUuTien của chính kỹ năng trong tuần đó. Cùng kỹ năng có thể nằm ở nhiều tuần hoặc nhiều lộ trình, và cùng một tuần có thể có nhiều kỹ năng cần cải thiện. Mức ưu tiên không chỉ phụ thuộc riêng vào tuần hay kỹ năng. Bảng liên kết giữ mỗi cặp đúng một lần thay vì lưu danh sách kỹ năng trong một trường của TuanLoTrinh.

Đối với việc học từ vựng, ChuDeTheGhiNho(MaChuDe, TenChuDe, MoTa) quản lý danh mục chủ đề. TheGhiNho(MaThe, MaChuDe, Tu, PhienAm, Nghia) lưu mỗi mục từ vựng gắn với đúng một chủ đề; cặp (MaChuDe, Tu) không trùng trong cùng chủ đề. Để hỗ trợ ôn luyện linh hoạt, một thẻ có thể có nhiều từ đồng nghĩa và nhiều câu ví dụ. TheDongNghia(MaThe, TuDongNghia) lưu riêng từng từ đồng nghĩa; ViDuTheGhiNho(MaThe, ViDu) lưu riêng từng câu ví dụ. Hai tập này được cập nhật độc lập theo MaThe: việc thêm từ đồng nghĩa không làm thay đổi tập ví dụ và ngược lại. Mỗi cặp (MaThe, TuDongNghia) và (MaThe, ViDu) chỉ xuất hiện một lần trong bảng tương ứng. Thiết kế này cho phép mở rộng kho flashcard mà không nhân bản các tổ hợp từ đồng nghĩa – ví dụ. Khi cần nghe phát âm, hệ thống có thể phát âm trực tiếp mà không phải lưu danh sách tệp âm thanh trong thẻ.

Khi cần giải thích một câu khó, người học sử dụng chức năng hội thoại hỗ trợ. CuocHoiThoai có MaCuocHoiThoai, MaNguoiDung, MaCauHoiNguCanh, TieuDe, TaoLuc và CapNhatLuc. Một cuộc hội thoại thuộc một người dùng và có thể liên hệ một câu đang được xem. Mỗi lần trao đổi chứa nhiều TinNhan, từng tin nhắn có MaTinNhan, MaCuocHoiThoai, VaiTro, NoiDung, YDinh và TaoLuc. Từng lời hỏi hoặc lời giải thích được lưu thành bản ghi riêng, giúp tái hiện thứ tự tương tác mà không gom cả cuộc trò chuyện thành một ô dữ liệu.

Đối với quyền truy cập tính năng nâng cao, hệ thống tạo DonThanhToan gắn với MaNguoiDung và MaGoi. Đơn lưu MaDonThanhToan, SoTien, TrangThai, MaDonPayOS, TaoLuc, HetHanLuc và ThanhToanLuc. Mỗi đơn thanh toán được định danh riêng và có mã đối chiếu PayOS duy nhất ở phạm vi những đơn đã tạo trên cổng. Sau khi đơn hoàn tất, hệ thống tạo DangKyGoiNguoiDung quản lý MaDangKy, MaNguoiDung, MaDonThanhToan, MaGoi, BatDauLuc, HetHanLuc và TrangThai. Mỗi đăng ký gắn với một đơn thanh toán riêng; một đơn đã cấp quyền không được sử dụng để phát hành hai đăng ký trùng nhau. Việc lưu lịch sử đăng ký độc lập cho phép tài khoản gia hạn qua nhiều thời kỳ mà không ghi đè quyền sử dụng trước đó.

# CHƯƠNG 2. MÔ TẢ VÀ PHÂN LOẠI THỰC THỂ

## 2.1. Thực thể CƠ BẢN

| **STT** | **Thực thể** | **Thuộc tính chính** | **Ý nghĩa và lý do phân loại** |
| --- | --- | --- | --- |
| 1 | KyNangToeic | MaKyNang, TenKyNang, LoaiKyNang, MaKyNangCha | Danh mục phân loại nội dung TOEIC thành kỹ năng và kỹ năng con; MaKyNangCha biểu diễn quan hệ phân cấp. Một mã kỹ năng được dùng để gắn nhãn câu hỏi, tổng hợp kết quả chẩn đoán và xác định nội dung luyện theo tuần. Dữ liệu kỹ năng được chuẩn bị để tái sử dụng, không sinh ra mỗi khi người học làm bài. |
| 2 | BoDeToeic | MaBoDe, TenBoDe, LoaiBoDe, PhanThi, MoTa, DangHoatDong | Lưu thông tin nhận diện bộ đề, loại đề, phần thi và tình trạng có thể sử dụng. Một bộ đề được cấu thành từ các nhóm ngữ liệu và có thể phục vụ nhiều lượt kiểm tra đầu vào, luyện tập hoặc thi thử. Vì nội dung đề tồn tại độc lập với mỗi lần người học mở phiên thi, quan hệ thuộc nhóm cơ bản. |
| 3 | NhomNguLieuToeic | MaNhomNguLieu, MaBoDe, PhanThi, TieuDe, NoiDung, ThuTu | Tổ chức các đoạn nghe, đoạn đọc hoặc cụm câu hỏi chung ngữ cảnh bên trong bộ đề. MaBoDe chỉ bộ đề chứa nhóm, còn ThuTu xác định vị trí nhóm trong bộ đề. Nội dung ngữ liệu được xây dựng trước và nhiều câu hỏi có thể dùng chung, nên nó là dữ liệu học liệu nền tảng. |
| 4 | CauHoiToeic | MaCauHoi, MaNhomNguLieu, MaKyNang, SoThuTuCau, DoKho, NoiDungCauHoi, GiaiThich | Quản lý câu hỏi, độ khó, lời giải thích, thứ tự và kỹ năng đánh giá. Một câu hỏi thuộc một nhóm ngữ liệu nhưng có nhiều phương án trả lời và có thể xuất hiện trong các lần làm bài khác nhau. Nội dung câu không thay đổi theo đáp án người học chọn nên được lưu như một thành phần của ngân hàng câu hỏi. |
| 5 | LuaChonCauHoi | MaLuaChon, MaCauHoi, KyHieu, NoiDung, LaDapAnDung, ThuTu | Lưu từng phương án A, B, C, D hoặc các ký hiệu tương đương của một câu hỏi. Thuộc tính LaDapAnDung gắn với phương án của ngân hàng đề, không phải câu trả lời trong một lần thi. Các phương án được quản lý sẵn để tái sử dụng ở nhiều lần làm bài, vì thế là dữ liệu cơ bản. |
| 6 | TaiNguyenAnh | LoaiDoiTuong, MaDoiTuong, DuongDanAnh | Lưu từng đường dẫn ảnh gắn với câu hỏi hoặc nhóm ngữ liệu; độc lập với tập âm thanh. |
| 7 | TaiNguyenAmThanh | LoaiDoiTuong, MaDoiTuong, DuongDanAmThanh | Lưu từng đường dẫn âm thanh gắn với câu hỏi hoặc nhóm ngữ liệu; độc lập với tập ảnh. |
| 8 | ChuDeTheGhiNho | MaChuDe, TenChuDe, MoTa | Là danh mục chủ đề dùng để gom thẻ từ vựng, với tên và mô tả của từng chủ đề. Một chủ đề có thể có nhiều thẻ, trong khi cùng chủ đề có thể được nhiều người học mở để luyện từ. Chủ đề được khai báo làm nền cho thư viện flashcard nên xếp vào nhóm cơ bản. |
| 9 | TheGhiNho | MaThe, MaChuDe, Tu, PhienAm, Nghia, SoChuDeHienThi (dẫn xuất trong khảo sát) | Quản lý một mục từ vựng thuộc một chủ đề. Thông tin từ, phiên âm và nghĩa gắn với MaThe; các từ đồng nghĩa và câu ví dụ không được lặp trong bảng này mà quản lý ở hai quan hệ riêng. |
| 10 | TheDongNghia | MaThe, TuDongNghia | Mỗi bản ghi gắn một từ đồng nghĩa với một thẻ ghi nhớ. Một thẻ có thể có nhiều từ đồng nghĩa; cặp (MaThe, TuDongNghia) là duy nhất và không phụ thuộc vào các câu ví dụ. |
| 11 | ViDuTheGhiNho | MaThe, ViDu | Lưu từng câu ví dụ minh họa cách dùng từ của một thẻ ghi nhớ. Một thẻ có thể có nhiều ví dụ; cặp (MaThe, ViDu) là duy nhất và độc lập với danh sách từ đồng nghĩa. |

Nhóm cơ bản bao gồm các danh mục và học liệu TOEIC: kỹ năng, bộ đề, nhóm ngữ liệu, câu hỏi, phương án và tài nguyên ảnh hoặc âm thanh. Thư viện flashcard gồm chủ đề, thẻ ghi nhớ, tập từ đồng nghĩa và tập câu ví dụ. Mỗi tài nguyên hoặc nội dung bổ trợ được quản lý theo đúng chủ thể và phạm vi của mình, giúp tránh lặp dữ liệu giữa các hoạt động học tập.

## 2.2. Thực thể ĐỐI TƯỢNG NGOÀI

| **STT** | **Thực thể** | **Thuộc tính chính** | **Ý nghĩa và lý do phân loại** |
| --- | --- | --- | --- |
| 1 | NguoiDung | MaNguoiDung, HoTen, Email, DiemMucTieu, NgayThiDuKien, SoPhutHocMoiNgay | Đại diện người học trực tiếp đăng ký, đăng nhập, kiểm tra trình độ và theo dõi lộ trình trên GetGoals. Hồ sơ giữ thông tin xác thực, tên, email, mục tiêu điểm và thiết lập học mỗi ngày. Một tài khoản có thể sinh nhiều lần làm bài, cuộc hội thoại, tương tác câu hỏi, đơn thanh toán; các hoạt động ấy được lưu riêng ở nhóm thực thể nghiệp vụ. |

NguoiDung là đối tượng ngoài trực tiếp tác động đến hệ thống qua các chức năng đăng nhập, làm bài, ôn tập và giao dịch. Thông tin tài khoản, mục tiêu TOEIC và cấu hình cá nhân tồn tại trong hồ sơ, còn thời điểm và kết quả của từng thao tác được lưu ở các quan hệ nghiệp vụ tương ứng.

## 2.3. Thực thể NGHIỆP VỤ

| **STT** | **Thực thể** | **Thuộc tính chính** | **Ý nghĩa và lý do phân loại** |
| --- | --- | --- | --- |
| 1 | LanLamBai | MaLanLamBai, MaNguoiDung, MaBoDe, LoaiLanLam, TrangThai, BatDauLuc, NopBaiLuc | Phát sinh khi một người dùng bắt đầu kiểm tra đầu vào, luyện tập hoặc thi thử. Mỗi lượt ghi nhận người học, bộ đề, loại hoạt động, trạng thái, thời điểm bắt đầu và nộp bài. Đây là sự kiện học tập theo thời gian, khác với bộ đề được sử dụng làm nguồn câu hỏi. |
| 2 | CauHoiLanLamBai | MaChiTiet, MaLanLamBai, MaCauHoi, KyHieuDaChon, ThuTu, DaDanhDau, ThoiGianTraLoiGiay | Lưu chi tiết mỗi câu xuất hiện trong một lần làm bài, bao gồm thứ tự hiển thị, phương án đã chọn, dấu đánh dấu và thời gian trả lời. MaLanLamBai nối chi tiết với phiên, còn MaCauHoi tham chiếu nội dung câu hỏi gốc. Một phiên có nhiều dòng chi tiết nên bảng phản ánh hành vi làm bài của người dùng. |
| 3 | KetQuaChanDoan | MaLanLamBai, Theta, DiemUocLuong, DiemToeicThuc, SoLanChanDoan | Được ghi khi xử lý kết quả của một bài đánh giá đầu vào, với theta hoặc điểm TOEIC ước lượng và điểm tham khảo nếu có. Bản ghi gắn trực tiếp với một MaLanLamBai đã thực hiện. Kết quả mang tính cá nhân, thay đổi theo từng lần kiểm tra nên là thực thể nghiệp vụ. |
| 4 | KyNangYeuChanDoan | MaLanLamBai, MaKyNang, MucDoYeu, SoLanChanDoan | Biểu diễn từng kỹ năng được phát hiện yếu trong kết quả chẩn đoán, kèm mức độ yếu. Khóa ghép giữa lần làm bài và kỹ năng cho phép một lần kiểm tra ghi nhận nhiều kỹ năng, đồng thời một kỹ năng có thể yếu ở nhiều phiên của các người học khác nhau. Đây là dữ liệu kết quả phân tích, không phải danh mục kỹ năng nền. |
| 5 | MucOnTap | MaMucOnTap, MaNguoiDung, MaCauHoi, LyDoOnTap, TrangThai, ThemLuc, OnTapLuc | Được thêm vào danh sách ôn của người học sau khi làm sai, chưa trả lời hoặc muốn xem lại một câu. Mỗi mục chứa câu hỏi cần ôn, lần làm bài nguồn nếu có, lý do, trạng thái và thời điểm thực hiện. Quan hệ quản lý việc ôn của từng người chứ không thay thế câu hỏi dùng chung. |
| 6 | TuongTacCauHoi | MaTuongTac, MaNguoiDung, MaCauHoi, LoaiTuongTac, NoiDung, ViTriBatDau, ViTriKetThuc, MauSac | Ghi nhận một thao tác ghi chú, đánh dấu hoặc tô sáng do người học thực hiện trên câu hỏi. Nội dung ghi chú hay các vị trí tô sáng và màu sắc thuộc một lần tương tác cụ thể. Dữ liệu phát sinh theo thao tác cá nhân, khác với nội dung và đáp án sẵn có của câu hỏi. |
| 7 | LoTrinhHoc | MaLoTrinh, MaNguoiDung, TieuDe, DiemMucTieu, NgayBatDau, TrangThai, TaoLuc | Sinh ra khi hệ thống xây dựng hoặc người học sử dụng một kế hoạch ôn luyện theo mục tiêu điểm. Mỗi lộ trình gắn với một người dùng, có tiêu đề, ngày bắt đầu, thời điểm tạo và trạng thái. Một người có thể có nhiều lộ trình qua các giai đoạn khác nhau nên đây là dữ liệu nghiệp vụ cá nhân hóa. |
| 8 | TuanLoTrinh | MaTuan, MaLoTrinh, SoTuan, TieuDe, SoCauDeXuat, SoPhutDuKien, TrangThai | Chia một lộ trình thành những tuần học theo thứ tự xác định, kèm nội dung dự kiến và trạng thái thực hiện. MaLoTrinh kết nối tuần với kế hoạch cha, còn SoTuan phân biệt vị trí bên trong kế hoạch. Tuần được tạo và cập nhật trong tiến trình quản lý lộ trình nên thuộc nhóm nghiệp vụ. |
| 9 | KyNangConTuanLoTrinh | MaTuan, MaKyNang, MucUuTien, MaLoTrinh, SoTuan | Ghi nhận các kỹ năng con cần tập trung trong từng tuần cùng mức ưu tiên. Một tuần có nhiều kỹ năng, và một kỹ năng có thể xuất hiện ở nhiều tuần; mỗi cặp tuần–kỹ năng tạo một dòng liên kết. Quan hệ phát sinh từ việc phân bổ nội dung học vào lộ trình cụ thể. |
| 10 | CuocHoiThoai | MaCuocHoiThoai, MaNguoiDung, MaCauHoiNguCanh, TieuDe, TaoLuc, CapNhatLuc | Được tạo khi người học bắt đầu trao đổi với trợ lý học tập, có thể gắn với câu hỏi đang xem. Cuộc hội thoại giữ tiêu đề, thời gian tạo và cập nhật, trong khi từng tin riêng được lưu tại TinNhan. Đây là phiên trao đổi phát sinh theo nhu cầu của tài khoản, không phải tài liệu ngân hàng học liệu. |
| 11 | TinNhan | MaTinNhan, MaCuocHoiThoai, VaiTro, NoiDung, YDinh, TaoLuc, SoTinTrongCuoc | Mỗi dòng ghi một nội dung trao đổi trong cuộc hội thoại, gồm vai trò người gửi, ý định xử lý và thời điểm gửi. Một cuộc có thể phát sinh nhiều tin theo trình tự. Tin nhắn phản ánh lịch sử tương tác thực tế với trợ lý nên là dữ liệu nghiệp vụ. |
| 12 | DonThanhToan | MaDonThanhToan, MaNguoiDung, MaGoi, SoTien, TrangThai, MaDonPayOS, ThanhToanLuc | Phát sinh khi người dùng tạo yêu cầu thanh toán cho gói sử dụng, ghi mã gói, số tiền, trạng thái, mã đơn phía cổng thanh toán và các thời điểm liên quan. Người học có thể thực hiện nhiều giao dịch theo thời gian. Đơn phản ánh một giao dịch cụ thể, không đồng nhất với quyền sử dụng gói sau thanh toán. |
| 13 | DangKyGoiNguoiDung | MaDangKy, MaNguoiDung, MaDonThanhToan, MaGoi, BatDauLuc, HetHanLuc, TrangThai | Ghi nhận quyền sử dụng gói của người học sau một giao dịch liên quan, với thời hạn bắt đầu, hết hạn và trạng thái. MaDonThanhToan kết nối với đơn thanh toán nguồn; người dùng có thể có các đăng ký ở những giai đoạn khác nhau. Đây là lịch sử quyền truy cập phát sinh theo giao dịch, không phải bản ghi danh mục gói. |

Các thực thể nghiệp vụ phản ánh hoạt động cụ thể: LanLamBai tạo phiên thi và CauHoiLanLamBai ghi câu trả lời; KetQuaChanDoan và KyNangYeuChanDoan ghi kết quả đánh giá; LoTrinhHoc chia thành TuanLoTrinh và phân bổ kỹ năng qua KyNangConTuanLoTrinh. CuocHoiThoai chứa TinNhan, trong khi DonThanhToan quản lý giao dịch và DangKyGoiNguoiDung quản lý quyền sau giao dịch. Phân tách này tránh nhầm học liệu nền với lịch sử riêng của người học.

# CHƯƠNG 3. PHÂN TÍCH PHỤ THUỘC HÀM, KHÓA VÀ DẠNG CHUẨN

## 3.1. Các quan hệ có dạng chuẩn cao nhất là 3NF

### 1. Quan hệ NhomNguLieuToeic

**Ý nghĩa nghiệp vụ:** MaBoDe xác định loại bộ đề. Trong phép chiếu phục vụ phân tích, SoBoDeTrongLoai được tính theo thứ tự mã bộ đề bên trong mỗi loại, nên (LoaiBoDe, SoBoDeTrongLoai) định danh đúng một MaBoDe.

**Lược đồ R:** NhomNguLieuToeic(MaNhomNguLieu, MaBoDe, PhanThi, TieuDe, NoiDung, ThuTu, LoaiBoDe, SoBoDeTrongLoai).

**Phụ thuộc hàm:** MaNhomNguLieu → {MaBoDe, PhanThi, TieuDe, NoiDung, ThuTu}; (MaBoDe, ThuTu) → {MaNhomNguLieu}; MaBoDe → {LoaiBoDe, SoBoDeTrongLoai}; (LoaiBoDe, SoBoDeTrongLoai) → {MaBoDe}.

**Phủ tối thiểu:** MaNhomNguLieu → MaBoDe; MaNhomNguLieu → PhanThi; MaNhomNguLieu → TieuDe; MaNhomNguLieu → NoiDung; MaNhomNguLieu → ThuTu; (MaBoDe, ThuTu) → MaNhomNguLieu; MaBoDe → LoaiBoDe; MaBoDe → SoBoDeTrongLoai; (LoaiBoDe, SoBoDeTrongLoai) → MaBoDe.

**Khóa chính:** {MaNhomNguLieu}.

**Tìm khóa chính:** {MaNhomNguLieu}+ = R. Vậy {MaNhomNguLieu} là khóa chính vì xác định toàn bộ thuộc tính của R và tối thiểu.

**Xét 1NF:** Các thuộc tính có giá trị đơn, nên quan hệ đạt 1NF.

**Xét 2NF:** Không có phụ thuộc bộ phận của thuộc tính không khóa vào khóa, nên đạt 2NF.

**Xét 3NF:** Các FD đều có vế trái là siêu khóa hoặc vế phải là thuộc tính khóa; riêng MaBoDe → LoaiBoDe được 3NF cho phép. Quan hệ đạt 3NF.

**Xét BCNF:** FD MaBoDe → LoaiBoDe có vế trái không là siêu khóa, nên quan hệ không đạt BCNF.

**Kết luận:** Dạng chuẩn cao nhất của quan hệ NhomNguLieuToeic là 3NF.

### 2. Quan hệ CauHoiToeic

**Ý nghĩa nghiệp vụ:** Mỗi nhóm thuộc một bộ đề. SoCauTrongBoDe là số thứ tự duy nhất của câu trong bộ đề, tính bằng cách sắp nhóm theo ThuTu và câu trong nhóm theo SoThuTuCau, dùng MaCauHoi xử lý trường hợp đồng hạng.

**Lược đồ R:** CauHoiToeic(MaCauHoi, MaNhomNguLieu, MaKyNang, SoThuTuCau, DoKho, NoiDungCauHoi, GiaiThich, DangHoatDong, MaBoDe, SoCauTrongBoDe).

**Phụ thuộc hàm:** MaCauHoi → {MaNhomNguLieu, MaKyNang, SoThuTuCau, DoKho, NoiDungCauHoi, GiaiThich, DangHoatDong, SoCauTrongBoDe}; (MaNhomNguLieu, SoThuTuCau) → {MaCauHoi}; MaNhomNguLieu → {MaBoDe}; (MaBoDe, SoCauTrongBoDe) → {MaCauHoi}.

**Phủ tối thiểu:** MaCauHoi → MaNhomNguLieu; MaCauHoi → MaKyNang; MaCauHoi → SoThuTuCau; MaCauHoi → DoKho; MaCauHoi → NoiDungCauHoi; MaCauHoi → GiaiThich; MaCauHoi → DangHoatDong; (MaNhomNguLieu, SoThuTuCau) → MaCauHoi; MaNhomNguLieu → MaBoDe; MaCauHoi → SoCauTrongBoDe; (MaBoDe, SoCauTrongBoDe) → MaCauHoi.

**Khóa chính:** {MaCauHoi}.

**Tìm khóa chính:** {MaCauHoi}+ = R. Vậy {MaCauHoi} là khóa chính vì xác định toàn bộ thuộc tính của R và tối thiểu.

**Xét 1NF:** Các thuộc tính có giá trị đơn, nên quan hệ đạt 1NF.

**Xét 2NF:** Không có phụ thuộc bộ phận của thuộc tính không khóa vào khóa, nên đạt 2NF.

**Xét 3NF:** Các FD đều có vế trái là siêu khóa hoặc vế phải là thuộc tính khóa; riêng MaNhomNguLieu → MaBoDe được 3NF cho phép. Quan hệ đạt 3NF.

**Xét BCNF:** FD MaNhomNguLieu → MaBoDe có vế trái không là siêu khóa, nên quan hệ không đạt BCNF.

**Kết luận:** Dạng chuẩn cao nhất của quan hệ CauHoiToeic là 3NF.

### 3. Quan hệ LuaChonCauHoi

**Ý nghĩa nghiệp vụ:** Một câu hỏi thuộc đúng một nhóm và vị trí trong nhóm; (MaNhomNguLieu, SoThuTuCau) xác định câu hỏi. Mỗi câu có nhiều ký hiệu phương án nên MaCauHoi không xác định toàn bộ dòng lựa chọn.

**Lược đồ R:** LuaChonCauHoi(MaLuaChon, MaCauHoi, KyHieu, NoiDung, LaDapAnDung, ThuTu, MaNhomNguLieu, SoThuTuCau).

**Phụ thuộc hàm:** MaLuaChon → {MaCauHoi, KyHieu, NoiDung, LaDapAnDung, ThuTu}; (MaCauHoi, KyHieu) → {MaLuaChon}; MaCauHoi → {MaNhomNguLieu, SoThuTuCau}; (MaNhomNguLieu, SoThuTuCau) → {MaCauHoi}.

**Phủ tối thiểu:** MaLuaChon → MaCauHoi; MaLuaChon → KyHieu; MaLuaChon → NoiDung; MaLuaChon → LaDapAnDung; MaLuaChon → ThuTu; (MaCauHoi, KyHieu) → MaLuaChon; MaCauHoi → MaNhomNguLieu; MaCauHoi → SoThuTuCau; (MaNhomNguLieu, SoThuTuCau) → MaCauHoi.

**Khóa chính:** {MaLuaChon}.

**Tìm khóa chính:** {MaLuaChon}+ = R. Vậy {MaLuaChon} là khóa chính vì xác định toàn bộ thuộc tính của R và tối thiểu.

**Xét 1NF:** Các thuộc tính có giá trị đơn, nên quan hệ đạt 1NF.

**Xét 2NF:** Không có phụ thuộc bộ phận của thuộc tính không khóa vào khóa, nên đạt 2NF.

**Xét 3NF:** Các FD đều có vế trái là siêu khóa hoặc vế phải là thuộc tính khóa; riêng MaCauHoi → MaNhomNguLieu được 3NF cho phép. Quan hệ đạt 3NF.

**Xét BCNF:** FD MaCauHoi → MaNhomNguLieu có vế trái không là siêu khóa, nên quan hệ không đạt BCNF.

**Kết luận:** Dạng chuẩn cao nhất của quan hệ LuaChonCauHoi là 3NF.

### 4. Quan hệ TheGhiNho

**Ý nghĩa nghiệp vụ:** SoChuDeHienThi là vị trí đánh số duy nhất của chủ đề trong lược đồ khảo sát, không phải cột lưu bền vững. Mỗi MaThe xác định một mục từ; trong cùng chủ đề, Tu không trùng. Danh sách từ đồng nghĩa và câu ví dụ được lưu riêng theo MaThe.

**Lược đồ R:** TheGhiNho(MaThe, MaChuDe, Tu, PhienAm, Nghia, SoChuDeHienThi).

**Phụ thuộc hàm:** MaThe → {MaChuDe, Tu, PhienAm, Nghia}; (MaChuDe, Tu) → MaThe; MaChuDe → SoChuDeHienThi; SoChuDeHienThi → MaChuDe; (SoChuDeHienThi, Tu) → MaThe.

**Phủ tối thiểu:** MaThe → MaChuDe; MaThe → Tu; MaThe → PhienAm; MaThe → Nghia; MaChuDe → SoChuDeHienThi; SoChuDeHienThi → MaChuDe; (MaChuDe, Tu) → MaThe.

**Khóa chính:** {MaThe}.

**Tìm khóa chính:** {MaThe}+ = R. Vậy {MaThe} là khóa chính vì xác định toàn bộ thuộc tính của R và tối thiểu.

**Xét 1NF:** Các thuộc tính có giá trị đơn, nên quan hệ đạt 1NF.

**Xét 2NF:** Không có phụ thuộc bộ phận của thuộc tính không khóa vào khóa, nên đạt 2NF.

**Xét 3NF:** Các FD đều có vế trái là siêu khóa hoặc vế phải là thuộc tính khóa; riêng MaChuDe → SoChuDeHienThi được 3NF cho phép. Quan hệ đạt 3NF.

**Xét BCNF:** FD MaChuDe → SoChuDeHienThi có vế trái không là siêu khóa, nên quan hệ không đạt BCNF.

**Kết luận:** Dạng chuẩn cao nhất của quan hệ TheGhiNho là 3NF.

## 3.2. Các quan hệ nghiệp vụ được chứng minh đạt BCNF

### 5. Quan hệ LanLamBai

**Ý nghĩa nghiệp vụ:** Mỗi bản ghi được nhận diện bằng khóa chính; các thuộc tính tham chiếu chỉ lưu mã liên kết, không chép thông tin mô tả hay các chỉ số phân tích từ bảng khác.

**Lược đồ R:** LanLamBai(MaLanLamBai, MaNguoiDung, MaBoDe, LoaiLanLam, TrangThai, ThoiGianLamGiay, BatDauLuc, NopBaiLuc).

**Phụ thuộc hàm:** MaLanLamBai → {MaNguoiDung, MaBoDe, LoaiLanLam, TrangThai, ThoiGianLamGiay, BatDauLuc, NopBaiLuc}.

**Phủ tối thiểu:** MaLanLamBai → MaNguoiDung; MaLanLamBai → MaBoDe; MaLanLamBai → LoaiLanLam; MaLanLamBai → TrangThai; MaLanLamBai → ThoiGianLamGiay; MaLanLamBai → BatDauLuc; MaLanLamBai → NopBaiLuc.

**Khóa chính:** {MaLanLamBai}.

**Tìm khóa chính:** {MaLanLamBai}+ = R; bỏ một thuộc tính khỏi khóa sẽ không xác định được toàn bộ R.

**Xét 1NF:** Mỗi thuộc tính có giá trị đơn.

**Xét 2NF:** Không có thuộc tính không khóa phụ thuộc vào một phần khóa chính.

**Xét 3NF:** Các phụ thuộc hàm không tầm thường đều có vế trái là siêu khóa, nên đạt 3NF.

**Xét BCNF:** Tất cả vế trái trong phụ thuộc hàm đã nêu đều xác định được toàn bộ R; không tồn tại phụ thuộc hàm không tầm thường vi phạm BCNF.

Xét 4NF: Chưa xác định đầy đủ các phụ thuộc đa trị từ ràng buộc nghiệp vụ của quan hệ; vì vậy chưa đủ cơ sở chứng minh quan hệ đạt 4NF.

Kết luận: Quan hệ LanLamBai đã được chứng minh đạt BCNF theo các phụ thuộc hàm đã xác định.

### 6. Quan hệ CauHoiLanLamBai

**Ý nghĩa nghiệp vụ:** Mỗi bản ghi được nhận diện bằng khóa chính; các thuộc tính tham chiếu chỉ lưu mã liên kết, không chép thông tin mô tả hay các chỉ số phân tích từ bảng khác.

**Lược đồ R:** CauHoiLanLamBai(MaChiTiet, MaLanLamBai, MaCauHoi, KyHieuDaChon, ThuTu, DaDanhDau, ThoiGianTraLoiGiay).

**Phụ thuộc hàm:** MaChiTiet → {MaLanLamBai, MaCauHoi, KyHieuDaChon, ThuTu, DaDanhDau, ThoiGianTraLoiGiay}; (MaLanLamBai, ThuTu) → MaChiTiet; (MaLanLamBai, MaCauHoi) → MaChiTiet.

**Phủ tối thiểu:** MaChiTiet → MaLanLamBai; MaChiTiet → MaCauHoi; MaChiTiet → KyHieuDaChon; MaChiTiet → ThuTu; MaChiTiet → DaDanhDau; MaChiTiet → ThoiGianTraLoiGiay; (MaLanLamBai, ThuTu) → MaChiTiet; (MaLanLamBai, MaCauHoi) → MaChiTiet.

**Khóa chính:** {MaChiTiet}.

**Tìm khóa chính:** {MaChiTiet}+ = R; bỏ một thuộc tính khỏi khóa sẽ không xác định được toàn bộ R.

**Xét 1NF:** Mỗi thuộc tính có giá trị đơn.

**Xét 2NF:** Không có thuộc tính không khóa phụ thuộc vào một phần khóa chính.

**Xét 3NF:** Các phụ thuộc hàm không tầm thường đều có vế trái là siêu khóa, nên đạt 3NF.

**Xét BCNF:** Tất cả vế trái trong phụ thuộc hàm đã nêu đều xác định được toàn bộ R; không tồn tại phụ thuộc hàm không tầm thường vi phạm BCNF.

Xét 4NF: Chưa xác định đầy đủ các phụ thuộc đa trị từ ràng buộc nghiệp vụ của quan hệ; vì vậy chưa đủ cơ sở chứng minh quan hệ đạt 4NF.

Kết luận: Quan hệ CauHoiLanLamBai đã được chứng minh đạt BCNF theo các phụ thuộc hàm đã xác định.

### 7. Quan hệ KetQuaChanDoan

**Ý nghĩa nghiệp vụ:** Mỗi bản ghi được nhận diện bằng khóa chính; các thuộc tính tham chiếu chỉ lưu mã liên kết, không chép thông tin mô tả hay các chỉ số phân tích từ bảng khác.

**Lược đồ R:** KetQuaChanDoan(MaLanLamBai, Theta, DiemUocLuong, DiemToeicThuc).

**Phụ thuộc hàm:** MaLanLamBai → {Theta, DiemUocLuong, DiemToeicThuc}.

**Phủ tối thiểu:** MaLanLamBai → Theta; MaLanLamBai → DiemUocLuong; MaLanLamBai → DiemToeicThuc.

**Khóa chính:** {MaLanLamBai}.

**Tìm khóa chính:** {MaLanLamBai}+ = R; bỏ một thuộc tính khỏi khóa sẽ không xác định được toàn bộ R.

**Xét 1NF:** Mỗi thuộc tính có giá trị đơn.

**Xét 2NF:** Không có thuộc tính không khóa phụ thuộc vào một phần khóa chính.

**Xét 3NF:** Các phụ thuộc hàm không tầm thường đều có vế trái là siêu khóa, nên đạt 3NF.

**Xét BCNF:** Tất cả vế trái trong phụ thuộc hàm đã nêu đều xác định được toàn bộ R; không tồn tại phụ thuộc hàm không tầm thường vi phạm BCNF.

Xét 4NF: Chưa xác định đầy đủ các phụ thuộc đa trị từ ràng buộc nghiệp vụ của quan hệ; vì vậy chưa đủ cơ sở chứng minh quan hệ đạt 4NF.

Kết luận: Quan hệ KetQuaChanDoan đã được chứng minh đạt BCNF theo các phụ thuộc hàm đã xác định.

### 8. Quan hệ KyNangYeuChanDoan

**Ý nghĩa nghiệp vụ:** Mỗi bản ghi được nhận diện bằng khóa chính; các thuộc tính tham chiếu chỉ lưu mã liên kết, không chép thông tin mô tả hay các chỉ số phân tích từ bảng khác.

**Lược đồ R:** KyNangYeuChanDoan(MaLanLamBai, MaKyNang, MucDoYeu).

**Phụ thuộc hàm:** (MaLanLamBai, MaKyNang) → {MucDoYeu}.

**Phủ tối thiểu:** (MaLanLamBai, MaKyNang) → MucDoYeu.

**Khóa chính:** {MaLanLamBai, MaKyNang}.

**Tìm khóa chính:** {MaLanLamBai, MaKyNang}+ = R; bỏ một thuộc tính khỏi khóa sẽ không xác định được toàn bộ R.

**Xét 1NF:** Mỗi thuộc tính có giá trị đơn.

**Xét 2NF:** Không có thuộc tính không khóa phụ thuộc vào một phần khóa chính.

**Xét 3NF:** Các phụ thuộc hàm không tầm thường đều có vế trái là siêu khóa, nên đạt 3NF.

**Xét BCNF:** Tất cả vế trái trong phụ thuộc hàm đã nêu đều xác định được toàn bộ R; không tồn tại phụ thuộc hàm không tầm thường vi phạm BCNF.

Xét 4NF: Chưa xác định đầy đủ các phụ thuộc đa trị từ ràng buộc nghiệp vụ của quan hệ; vì vậy chưa đủ cơ sở chứng minh quan hệ đạt 4NF.

Kết luận: Quan hệ KyNangYeuChanDoan đã được chứng minh đạt BCNF theo các phụ thuộc hàm đã xác định.

### 9. Quan hệ MucOnTap

**Ý nghĩa nghiệp vụ:** Mỗi bản ghi được nhận diện bằng khóa chính; các thuộc tính tham chiếu chỉ lưu mã liên kết, không chép thông tin mô tả hay các chỉ số phân tích từ bảng khác.

**Lược đồ R:** MucOnTap(MaMucOnTap, MaNguoiDung, MaCauHoi, MaLanLamBaiNguon, LyDoOnTap, TrangThai, ThemLuc, OnTapLuc).

**Phụ thuộc hàm:** MaMucOnTap → {MaNguoiDung, MaCauHoi, MaLanLamBaiNguon, LyDoOnTap, TrangThai, ThemLuc, OnTapLuc}.

**Phủ tối thiểu:** MaMucOnTap → MaNguoiDung; MaMucOnTap → MaCauHoi; MaMucOnTap → MaLanLamBaiNguon; MaMucOnTap → LyDoOnTap; MaMucOnTap → TrangThai; MaMucOnTap → ThemLuc; MaMucOnTap → OnTapLuc.

**Khóa chính:** {MaMucOnTap}.

**Tìm khóa chính:** {MaMucOnTap}+ = R; bỏ một thuộc tính khỏi khóa sẽ không xác định được toàn bộ R.

**Xét 1NF:** Mỗi thuộc tính có giá trị đơn.

**Xét 2NF:** Không có thuộc tính không khóa phụ thuộc vào một phần khóa chính.

**Xét 3NF:** Các phụ thuộc hàm không tầm thường đều có vế trái là siêu khóa, nên đạt 3NF.

**Xét BCNF:** Tất cả vế trái trong phụ thuộc hàm đã nêu đều xác định được toàn bộ R; không tồn tại phụ thuộc hàm không tầm thường vi phạm BCNF.

Xét 4NF: Chưa xác định đầy đủ các phụ thuộc đa trị từ ràng buộc nghiệp vụ của quan hệ; vì vậy chưa đủ cơ sở chứng minh quan hệ đạt 4NF.

Kết luận: Quan hệ MucOnTap đã được chứng minh đạt BCNF theo các phụ thuộc hàm đã xác định.

### 10. Quan hệ TuongTacCauHoi

**Ý nghĩa nghiệp vụ:** Mỗi bản ghi được nhận diện bằng khóa chính; các thuộc tính tham chiếu chỉ lưu mã liên kết, không chép thông tin mô tả hay các chỉ số phân tích từ bảng khác.

**Lược đồ R:** TuongTacCauHoi(MaTuongTac, MaNguoiDung, MaCauHoi, LoaiTuongTac, NoiDung, ViTriBatDau, ViTriKetThuc, MauSac, TaoLuc).

**Phụ thuộc hàm:** MaTuongTac → {MaNguoiDung, MaCauHoi, LoaiTuongTac, NoiDung, ViTriBatDau, ViTriKetThuc, MauSac, TaoLuc}.

**Phủ tối thiểu:** MaTuongTac → MaNguoiDung; MaTuongTac → MaCauHoi; MaTuongTac → LoaiTuongTac; MaTuongTac → NoiDung; MaTuongTac → ViTriBatDau; MaTuongTac → ViTriKetThuc; MaTuongTac → MauSac; MaTuongTac → TaoLuc.

**Khóa chính:** {MaTuongTac}.

**Tìm khóa chính:** {MaTuongTac}+ = R; bỏ một thuộc tính khỏi khóa sẽ không xác định được toàn bộ R.

**Xét 1NF:** Mỗi thuộc tính có giá trị đơn.

**Xét 2NF:** Không có thuộc tính không khóa phụ thuộc vào một phần khóa chính.

**Xét 3NF:** Các phụ thuộc hàm không tầm thường đều có vế trái là siêu khóa, nên đạt 3NF.

**Xét BCNF:** Tất cả vế trái trong phụ thuộc hàm đã nêu đều xác định được toàn bộ R; không tồn tại phụ thuộc hàm không tầm thường vi phạm BCNF.

Xét 4NF: Chưa xác định đầy đủ các phụ thuộc đa trị từ ràng buộc nghiệp vụ của quan hệ; vì vậy chưa đủ cơ sở chứng minh quan hệ đạt 4NF.

Kết luận: Quan hệ TuongTacCauHoi đã được chứng minh đạt BCNF theo các phụ thuộc hàm đã xác định.

### 11. Quan hệ LoTrinhHoc

**Ý nghĩa nghiệp vụ:** Mỗi bản ghi được nhận diện bằng khóa chính; các thuộc tính tham chiếu chỉ lưu mã liên kết, không chép thông tin mô tả hay các chỉ số phân tích từ bảng khác.

**Lược đồ R:** LoTrinhHoc(MaLoTrinh, MaNguoiDung, TieuDe, DiemMucTieu, NgayBatDau, TrangThai, TaoLuc).

**Phụ thuộc hàm:** MaLoTrinh → {MaNguoiDung, TieuDe, DiemMucTieu, NgayBatDau, TrangThai, TaoLuc}.

**Phủ tối thiểu:** MaLoTrinh → MaNguoiDung; MaLoTrinh → TieuDe; MaLoTrinh → DiemMucTieu; MaLoTrinh → NgayBatDau; MaLoTrinh → TrangThai; MaLoTrinh → TaoLuc.

**Khóa chính:** {MaLoTrinh}.

**Tìm khóa chính:** {MaLoTrinh}+ = R; bỏ một thuộc tính khỏi khóa sẽ không xác định được toàn bộ R.

**Xét 1NF:** Mỗi thuộc tính có giá trị đơn.

**Xét 2NF:** Không có thuộc tính không khóa phụ thuộc vào một phần khóa chính.

**Xét 3NF:** Các phụ thuộc hàm không tầm thường đều có vế trái là siêu khóa, nên đạt 3NF.

**Xét BCNF:** Tất cả vế trái trong phụ thuộc hàm đã nêu đều xác định được toàn bộ R; không tồn tại phụ thuộc hàm không tầm thường vi phạm BCNF.

Xét 4NF: Chưa xác định đầy đủ các phụ thuộc đa trị từ ràng buộc nghiệp vụ của quan hệ; vì vậy chưa đủ cơ sở chứng minh quan hệ đạt 4NF.

Kết luận: Quan hệ LoTrinhHoc đã được chứng minh đạt BCNF theo các phụ thuộc hàm đã xác định.

### 12. Quan hệ TuanLoTrinh

**Ý nghĩa nghiệp vụ:** Mỗi bản ghi được nhận diện bằng khóa chính; các thuộc tính tham chiếu chỉ lưu mã liên kết, không chép thông tin mô tả hay các chỉ số phân tích từ bảng khác.

**Lược đồ R:** TuanLoTrinh(MaTuan, MaLoTrinh, SoTuan, TieuDe, MoTa, SoCauDeXuat, SoPhutDuKien, TrangThai).

**Phụ thuộc hàm:** MaTuan → {MaLoTrinh, SoTuan, TieuDe, MoTa, SoCauDeXuat, SoPhutDuKien, TrangThai}; (MaLoTrinh, SoTuan) → MaTuan.

**Phủ tối thiểu:** MaTuan → MaLoTrinh; MaTuan → SoTuan; MaTuan → TieuDe; MaTuan → MoTa; MaTuan → SoCauDeXuat; MaTuan → SoPhutDuKien; MaTuan → TrangThai; (MaLoTrinh, SoTuan) → MaTuan.

**Khóa chính:** {MaTuan}.

**Tìm khóa chính:** {MaTuan}+ = R; bỏ một thuộc tính khỏi khóa sẽ không xác định được toàn bộ R.

**Xét 1NF:** Mỗi thuộc tính có giá trị đơn.

**Xét 2NF:** Không có thuộc tính không khóa phụ thuộc vào một phần khóa chính.

**Xét 3NF:** Các phụ thuộc hàm không tầm thường đều có vế trái là siêu khóa, nên đạt 3NF.

**Xét BCNF:** Tất cả vế trái trong phụ thuộc hàm đã nêu đều xác định được toàn bộ R; không tồn tại phụ thuộc hàm không tầm thường vi phạm BCNF.

Xét 4NF: Chưa xác định đầy đủ các phụ thuộc đa trị từ ràng buộc nghiệp vụ của quan hệ; vì vậy chưa đủ cơ sở chứng minh quan hệ đạt 4NF.

Kết luận: Quan hệ TuanLoTrinh đã được chứng minh đạt BCNF theo các phụ thuộc hàm đã xác định.

### 13. Quan hệ KyNangConTuanLoTrinh

**Ý nghĩa nghiệp vụ:** Mỗi bản ghi được nhận diện bằng khóa chính; các thuộc tính tham chiếu chỉ lưu mã liên kết, không chép thông tin mô tả hay các chỉ số phân tích từ bảng khác.

**Lược đồ R:** KyNangConTuanLoTrinh(MaTuan, MaKyNang, MucUuTien).

**Phụ thuộc hàm:** (MaTuan, MaKyNang) → {MucUuTien}.

**Phủ tối thiểu:** (MaTuan, MaKyNang) → MucUuTien.

**Khóa chính:** {MaTuan, MaKyNang}.

**Tìm khóa chính:** {MaTuan, MaKyNang}+ = R; bỏ một thuộc tính khỏi khóa sẽ không xác định được toàn bộ R.

**Xét 1NF:** Mỗi thuộc tính có giá trị đơn.

**Xét 2NF:** Không có thuộc tính không khóa phụ thuộc vào một phần khóa chính.

**Xét 3NF:** Các phụ thuộc hàm không tầm thường đều có vế trái là siêu khóa, nên đạt 3NF.

**Xét BCNF:** Tất cả vế trái trong phụ thuộc hàm đã nêu đều xác định được toàn bộ R; không tồn tại phụ thuộc hàm không tầm thường vi phạm BCNF.

Xét 4NF: Chưa xác định đầy đủ các phụ thuộc đa trị từ ràng buộc nghiệp vụ của quan hệ; vì vậy chưa đủ cơ sở chứng minh quan hệ đạt 4NF.

Kết luận: Quan hệ KyNangConTuanLoTrinh đã được chứng minh đạt BCNF theo các phụ thuộc hàm đã xác định.

### 14. Quan hệ CuocHoiThoai

**Ý nghĩa nghiệp vụ:** Mỗi bản ghi được nhận diện bằng khóa chính; các thuộc tính tham chiếu chỉ lưu mã liên kết, không chép thông tin mô tả hay các chỉ số phân tích từ bảng khác.

**Lược đồ R:** CuocHoiThoai(MaCuocHoiThoai, MaNguoiDung, MaCauHoiNguCanh, TieuDe, TaoLuc, CapNhatLuc).

**Phụ thuộc hàm:** MaCuocHoiThoai → {MaNguoiDung, MaCauHoiNguCanh, TieuDe, TaoLuc, CapNhatLuc}.

**Phủ tối thiểu:** MaCuocHoiThoai → MaNguoiDung; MaCuocHoiThoai → MaCauHoiNguCanh; MaCuocHoiThoai → TieuDe; MaCuocHoiThoai → TaoLuc; MaCuocHoiThoai → CapNhatLuc.

**Khóa chính:** {MaCuocHoiThoai}.

**Tìm khóa chính:** {MaCuocHoiThoai}+ = R; bỏ một thuộc tính khỏi khóa sẽ không xác định được toàn bộ R.

**Xét 1NF:** Mỗi thuộc tính có giá trị đơn.

**Xét 2NF:** Không có thuộc tính không khóa phụ thuộc vào một phần khóa chính.

**Xét 3NF:** Các phụ thuộc hàm không tầm thường đều có vế trái là siêu khóa, nên đạt 3NF.

**Xét BCNF:** Tất cả vế trái trong phụ thuộc hàm đã nêu đều xác định được toàn bộ R; không tồn tại phụ thuộc hàm không tầm thường vi phạm BCNF.

Xét 4NF: Chưa xác định đầy đủ các phụ thuộc đa trị từ ràng buộc nghiệp vụ của quan hệ; vì vậy chưa đủ cơ sở chứng minh quan hệ đạt 4NF.

Kết luận: Quan hệ CuocHoiThoai đã được chứng minh đạt BCNF theo các phụ thuộc hàm đã xác định.

### 15. Quan hệ TinNhan

**Ý nghĩa nghiệp vụ:** Mỗi bản ghi được nhận diện bằng khóa chính; các thuộc tính tham chiếu chỉ lưu mã liên kết, không chép thông tin mô tả hay các chỉ số phân tích từ bảng khác.

**Lược đồ R:** TinNhan(MaTinNhan, MaCuocHoiThoai, VaiTro, NoiDung, YDinh, TaoLuc).

**Phụ thuộc hàm:** MaTinNhan → {MaCuocHoiThoai, VaiTro, NoiDung, YDinh, TaoLuc}.

**Phủ tối thiểu:** MaTinNhan → MaCuocHoiThoai; MaTinNhan → VaiTro; MaTinNhan → NoiDung; MaTinNhan → YDinh; MaTinNhan → TaoLuc.

**Khóa chính:** {MaTinNhan}.

**Tìm khóa chính:** {MaTinNhan}+ = R; bỏ một thuộc tính khỏi khóa sẽ không xác định được toàn bộ R.

**Xét 1NF:** Mỗi thuộc tính có giá trị đơn.

**Xét 2NF:** Không có thuộc tính không khóa phụ thuộc vào một phần khóa chính.

**Xét 3NF:** Các phụ thuộc hàm không tầm thường đều có vế trái là siêu khóa, nên đạt 3NF.

**Xét BCNF:** Tất cả vế trái trong phụ thuộc hàm đã nêu đều xác định được toàn bộ R; không tồn tại phụ thuộc hàm không tầm thường vi phạm BCNF.

Xét 4NF: Chưa xác định đầy đủ các phụ thuộc đa trị từ ràng buộc nghiệp vụ của quan hệ; vì vậy chưa đủ cơ sở chứng minh quan hệ đạt 4NF.

Kết luận: Quan hệ TinNhan đã được chứng minh đạt BCNF theo các phụ thuộc hàm đã xác định.

### 16. Quan hệ DonThanhToan

**Ý nghĩa nghiệp vụ:** Mỗi bản ghi được nhận diện bằng khóa chính; các thuộc tính tham chiếu chỉ lưu mã liên kết, không chép thông tin mô tả hay các chỉ số phân tích từ bảng khác.

**Lược đồ R:** DonThanhToan(MaDonThanhToan, MaNguoiDung, MaGoi, SoTien, TrangThai, MaDonPayOS, TaoLuc, HetHanLuc, ThanhToanLuc).

**Phụ thuộc hàm:** MaDonThanhToan → {MaNguoiDung, MaGoi, SoTien, TrangThai, MaDonPayOS, TaoLuc, HetHanLuc, ThanhToanLuc}; MaDonPayOS → MaDonThanhToan.

**Phủ tối thiểu:** MaDonThanhToan → MaNguoiDung; MaDonThanhToan → MaGoi; MaDonThanhToan → SoTien; MaDonThanhToan → TrangThai; MaDonThanhToan → MaDonPayOS; MaDonThanhToan → TaoLuc; MaDonThanhToan → HetHanLuc; MaDonThanhToan → ThanhToanLuc; MaDonPayOS → MaDonThanhToan.

**Khóa chính:** {MaDonThanhToan}.

**Tìm khóa chính:** {MaDonThanhToan}+ = R; bỏ một thuộc tính khỏi khóa sẽ không xác định được toàn bộ R.

**Xét 1NF:** Mỗi thuộc tính có giá trị đơn.

**Xét 2NF:** Không có thuộc tính không khóa phụ thuộc vào một phần khóa chính.

**Xét 3NF:** Các phụ thuộc hàm không tầm thường đều có vế trái là siêu khóa, nên đạt 3NF.

**Xét BCNF:** Tất cả vế trái trong phụ thuộc hàm đã nêu đều xác định được toàn bộ R; không tồn tại phụ thuộc hàm không tầm thường vi phạm BCNF.

Xét 4NF: Chưa xác định đầy đủ các phụ thuộc đa trị từ ràng buộc nghiệp vụ của quan hệ; vì vậy chưa đủ cơ sở chứng minh quan hệ đạt 4NF.

Kết luận: Quan hệ DonThanhToan đã được chứng minh đạt BCNF theo các phụ thuộc hàm đã xác định.

### 17. Quan hệ DangKyGoiNguoiDung

**Ý nghĩa nghiệp vụ:** Mỗi bản ghi được nhận diện bằng khóa chính; các thuộc tính tham chiếu chỉ lưu mã liên kết, không chép thông tin mô tả hay các chỉ số phân tích từ bảng khác.

**Lược đồ R:** DangKyGoiNguoiDung(MaDangKy, MaNguoiDung, MaDonThanhToan, MaGoi, BatDauLuc, HetHanLuc, TrangThai).

**Phụ thuộc hàm:** MaDangKy → {MaNguoiDung, MaDonThanhToan, MaGoi, BatDauLuc, HetHanLuc, TrangThai}; MaDonThanhToan → MaDangKy.

**Phủ tối thiểu:** MaDangKy → MaNguoiDung; MaDangKy → MaDonThanhToan; MaDangKy → MaGoi; MaDangKy → BatDauLuc; MaDangKy → HetHanLuc; MaDangKy → TrangThai; MaDonThanhToan → MaDangKy.

**Khóa chính:** {MaDangKy}.

**Tìm khóa chính:** {MaDangKy}+ = R; bỏ một thuộc tính khỏi khóa sẽ không xác định được toàn bộ R.

**Xét 1NF:** Mỗi thuộc tính có giá trị đơn.

**Xét 2NF:** Không có thuộc tính không khóa phụ thuộc vào một phần khóa chính.

**Xét 3NF:** Các phụ thuộc hàm không tầm thường đều có vế trái là siêu khóa, nên đạt 3NF.

**Xét BCNF:** Tất cả vế trái trong phụ thuộc hàm đã nêu đều xác định được toàn bộ R; không tồn tại phụ thuộc hàm không tầm thường vi phạm BCNF.

Xét 4NF: Chưa xác định đầy đủ các phụ thuộc đa trị từ ràng buộc nghiệp vụ của quan hệ; vì vậy chưa đủ cơ sở chứng minh quan hệ đạt 4NF.

Kết luận: Quan hệ DangKyGoiNguoiDung đã được chứng minh đạt BCNF theo các phụ thuộc hàm đã xác định.

## 3.3. Các quan hệ cơ bản và tài nguyên đạt 4NF

### 18. Quan hệ NguoiDung

**Lược đồ R:** NguoiDung(MaNguoiDung, HoTen, Email, MatKhauMaHoa, NhaCungCapDangNhap, MaNguoiDungNhaCungCap, DiemMucTieu, NgayThiDuKien, SoPhutHocMoiNgay, NgonNgu, CheDoGiaoDien, BatThongBaoEmail, TaoLuc).

**Phụ thuộc hàm:** MaNguoiDung → {HoTen, Email, MatKhauMaHoa, NhaCungCapDangNhap, MaNguoiDungNhaCungCap, DiemMucTieu, NgayThiDuKien, SoPhutHocMoiNgay, NgonNgu, CheDoGiaoDien, BatThongBaoEmail, TaoLuc}; Email → {MaNguoiDung}.

**Phủ tối thiểu:** MaNguoiDung → HoTen; MaNguoiDung → Email; MaNguoiDung → MatKhauMaHoa; MaNguoiDung → NhaCungCapDangNhap; MaNguoiDung → MaNguoiDungNhaCungCap; MaNguoiDung → DiemMucTieu; MaNguoiDung → NgayThiDuKien; MaNguoiDung → SoPhutHocMoiNgay; MaNguoiDung → NgonNgu; MaNguoiDung → CheDoGiaoDien; MaNguoiDung → BatThongBaoEmail; MaNguoiDung → TaoLuc; Email → MaNguoiDung.

**Khóa chính:** {MaNguoiDung}.

**Tìm khóa chính:** {MaNguoiDung}+ = R. Vậy {MaNguoiDung} là khóa chính vì xác định toàn bộ thuộc tính của R và tối thiểu.

**Xét 1NF:** Các thuộc tính có giá trị đơn, nên quan hệ đạt 1NF.

**Xét 2NF:** Không có phụ thuộc bộ phận của thuộc tính không khóa vào khóa, nên đạt 2NF.

**Xét 3NF:** Các FD đều có vế trái là siêu khóa hoặc vế phải là thuộc tính khóa. Quan hệ đạt 3NF.

**Xét BCNF:** Bao đóng vế trái của từng FD trong phủ tối thiểu bằng R; không có FD vi phạm điều kiện siêu khóa. Quan hệ đạt BCNF.

Xét 4NF: Hồ sơ người dùng được định danh duy nhất bởi MaNguoiDung (hoặc Email theo điều kiện duy nhất). Các thuộc tính mô tả chỉ nhận một giá trị trên mỗi tài khoản; theo các ràng buộc đã nêu không có phụ thuộc đa trị không tầm thường nào có vế trái không là siêu khóa. Do đó mọi phụ thuộc đa trị không tầm thường đều có vế trái là siêu khóa; quan hệ đạt 4NF.

Kết luận: Quan hệ NguoiDung đạt 4NF theo các ràng buộc nghiệp vụ khảo sát.

### 19. Quan hệ KyNangToeic

**Lược đồ R:** KyNangToeic(MaKyNang, TenKyNang, LoaiKyNang, MaKyNangCha).

**Phụ thuộc hàm:** MaKyNang → {TenKyNang, LoaiKyNang, MaKyNangCha}.

**Phủ tối thiểu:** MaKyNang → TenKyNang; MaKyNang → LoaiKyNang; MaKyNang → MaKyNangCha.

**Khóa chính:** {MaKyNang}.

**Tìm khóa chính:** {MaKyNang}+ = R. Vậy {MaKyNang} là khóa chính vì xác định toàn bộ thuộc tính của R và tối thiểu.

**Xét 1NF:** Các thuộc tính có giá trị đơn, nên quan hệ đạt 1NF.

**Xét 2NF:** Không có phụ thuộc bộ phận của thuộc tính không khóa vào khóa, nên đạt 2NF.

**Xét 3NF:** Các FD đều có vế trái là siêu khóa hoặc vế phải là thuộc tính khóa. Quan hệ đạt 3NF.

**Xét BCNF:** Bao đóng vế trái của từng FD trong phủ tối thiểu bằng R; không có FD vi phạm điều kiện siêu khóa. Quan hệ đạt BCNF.

Xét 4NF: MaKyNang xác định duy nhất mô tả và mã kỹ năng cha. Danh sách câu hỏi hoặc tuần học không nằm trong quan hệ này; theo nghiệp vụ đã nêu không có phụ thuộc đa trị không tầm thường vi phạm điều kiện siêu khóa. Do đó mọi phụ thuộc đa trị không tầm thường đều có vế trái là siêu khóa; quan hệ đạt 4NF.

Kết luận: Quan hệ KyNangToeic đạt 4NF theo các ràng buộc nghiệp vụ khảo sát.

### 20. Quan hệ BoDeToeic

**Lược đồ R:** BoDeToeic(MaBoDe, TenBoDe, LoaiBoDe, PhanThi, MoTa, DangHoatDong).

**Phụ thuộc hàm:** MaBoDe → {TenBoDe, LoaiBoDe, PhanThi, MoTa, DangHoatDong}.

**Phủ tối thiểu:** MaBoDe → TenBoDe; MaBoDe → LoaiBoDe; MaBoDe → PhanThi; MaBoDe → MoTa; MaBoDe → DangHoatDong.

**Khóa chính:** {MaBoDe}.

**Tìm khóa chính:** {MaBoDe}+ = R. Vậy {MaBoDe} là khóa chính vì xác định toàn bộ thuộc tính của R và tối thiểu.

**Xét 1NF:** Các thuộc tính có giá trị đơn, nên quan hệ đạt 1NF.

**Xét 2NF:** Không có phụ thuộc bộ phận của thuộc tính không khóa vào khóa, nên đạt 2NF.

**Xét 3NF:** Các FD đều có vế trái là siêu khóa hoặc vế phải là thuộc tính khóa. Quan hệ đạt 3NF.

**Xét BCNF:** Bao đóng vế trái của từng FD trong phủ tối thiểu bằng R; không có FD vi phạm điều kiện siêu khóa. Quan hệ đạt BCNF.

Xét 4NF: MaBoDe xác định các thuộc tính mô tả của một bộ đề. Nhóm ngữ liệu và lượt làm bài được quản lý ở những quan hệ riêng; theo các ràng buộc đã nêu không tồn tại phụ thuộc đa trị không tầm thường vi phạm. Do đó mọi phụ thuộc đa trị không tầm thường đều có vế trái là siêu khóa; quan hệ đạt 4NF.

Kết luận: Quan hệ BoDeToeic đạt 4NF theo các ràng buộc nghiệp vụ khảo sát.

### 21. Quan hệ ChuDeTheGhiNho

**Lược đồ R:** ChuDeTheGhiNho(MaChuDe, TenChuDe, MoTa).

**Phụ thuộc hàm:** MaChuDe → {TenChuDe, MoTa}.

**Phủ tối thiểu:** MaChuDe → TenChuDe; MaChuDe → MoTa.

**Khóa chính:** {MaChuDe}.

**Tìm khóa chính:** {MaChuDe}+ = R. Vậy {MaChuDe} là khóa chính vì xác định toàn bộ thuộc tính của R và tối thiểu.

**Xét 1NF:** Các thuộc tính có giá trị đơn, nên quan hệ đạt 1NF.

**Xét 2NF:** Không có phụ thuộc bộ phận của thuộc tính không khóa vào khóa, nên đạt 2NF.

**Xét 3NF:** Các FD đều có vế trái là siêu khóa hoặc vế phải là thuộc tính khóa. Quan hệ đạt 3NF.

**Xét BCNF:** Bao đóng vế trái của từng FD trong phủ tối thiểu bằng R; không có FD vi phạm điều kiện siêu khóa. Quan hệ đạt BCNF.

Xét 4NF: MaChuDe xác định TenChuDe, MoTa. Các thẻ ghi nhớ thuộc quan hệ TheGhiNho; không có tập đa trị độc lập nằm trong lược đồ chủ đề theo nghiệp vụ đã nêu. Do đó mọi phụ thuộc đa trị không tầm thường đều có vế trái là siêu khóa; quan hệ đạt 4NF.

Kết luận: Quan hệ ChuDeTheGhiNho đạt 4NF theo các ràng buộc nghiệp vụ khảo sát.

### 22. Quan hệ TaiNguyenAnh

Ý nghĩa nghiệp vụ: Lưu riêng từng đường dẫn ảnh gắn với câu hỏi hoặc nhóm ngữ liệu, không kết cặp với loại tài nguyên khác.

Lược đồ R: TaiNguyenAnh(LoaiDoiTuong, MaDoiTuong, DuongDanAnh).

Phụ thuộc hàm: ∅ (không có phụ thuộc hàm không tầm thường theo ràng buộc đã xác định).

Phủ tối thiểu: ∅; không có phụ thuộc hàm cần rút gọn.

Khóa chính: {LoaiDoiTuong, MaDoiTuong, DuongDanAnh}.

Tìm khóa chính: {LoaiDoiTuong, MaDoiTuong, DuongDanAnh}+ = R; mỗi tập con thực sự không xác định được toàn bộ R theo tập phụ thuộc hàm đã nêu.

Xét 1NF: Mỗi thuộc tính chứa một giá trị đơn, nên đạt 1NF.

Xét 2NF: Không có thuộc tính không khóa phụ thuộc bộ phận vào khóa, nên đạt 2NF.

Xét 3NF: Không có phụ thuộc hàm không tầm thường vi phạm điều kiện 3NF, nên đạt 3NF.

Xét BCNF: Không có phụ thuộc hàm không tầm thường, nên đạt BCNF.

Xét 4NF: Đặt X = {LoaiDoiTuong, MaDoiTuong}. Phụ thuộc X ↠ DuongDanAnh là tầm thường vì X ∪ {DuongDanAnh} = R. Theo nghiệp vụ hai danh sách tài nguyên đã tách độc lập, không có phụ thuộc đa trị không tầm thường có vế trái không là siêu khóa. Quan hệ đạt 4NF.

Kết luận: Quan hệ TaiNguyenAnh đạt 4NF.

### 23. Quan hệ TaiNguyenAmThanh

Ý nghĩa nghiệp vụ: Lưu riêng từng đường dẫn âm thanh gắn với câu hỏi hoặc nhóm ngữ liệu, không kết cặp với loại tài nguyên khác.

Lược đồ R: TaiNguyenAmThanh(LoaiDoiTuong, MaDoiTuong, DuongDanAmThanh).

Phụ thuộc hàm: ∅ (không có phụ thuộc hàm không tầm thường theo ràng buộc đã xác định).

Phủ tối thiểu: ∅; không có phụ thuộc hàm cần rút gọn.

Khóa chính: {LoaiDoiTuong, MaDoiTuong, DuongDanAmThanh}.

Tìm khóa chính: {LoaiDoiTuong, MaDoiTuong, DuongDanAmThanh}+ = R; mỗi tập con thực sự không xác định được toàn bộ R theo tập phụ thuộc hàm đã nêu.

Xét 1NF: Mỗi thuộc tính chứa một giá trị đơn, nên đạt 1NF.

Xét 2NF: Không có thuộc tính không khóa phụ thuộc bộ phận vào khóa, nên đạt 2NF.

Xét 3NF: Không có phụ thuộc hàm không tầm thường vi phạm điều kiện 3NF, nên đạt 3NF.

Xét BCNF: Không có phụ thuộc hàm không tầm thường, nên đạt BCNF.

Xét 4NF: Đặt X = {LoaiDoiTuong, MaDoiTuong}. Phụ thuộc X ↠ DuongDanAmThanh là tầm thường vì X ∪ {DuongDanAmThanh} = R. Theo nghiệp vụ hai danh sách tài nguyên đã tách độc lập, không có phụ thuộc đa trị không tầm thường có vế trái không là siêu khóa. Quan hệ đạt 4NF.

Kết luận: Quan hệ TaiNguyenAmThanh đạt 4NF.

### 24. Quan hệ TheDongNghia

**Ý nghĩa nghiệp vụ:** Lưu mỗi từ đồng nghĩa của một thẻ thành một dòng; các từ đồng nghĩa không phụ thuộc vào tập ví dụ của thẻ.

**Lược đồ R:** TheDongNghia(MaThe, TuDongNghia).

**Phụ thuộc hàm:** ∅ (không xác lập phụ thuộc hàm không tầm thường).

**Phủ tối thiểu:** ∅; không có phụ thuộc hàm không tầm thường để tối giản.

**Khóa chính:** {MaThe, TuDongNghia}.

**Tìm khóa chính:** {MaThe, TuDongNghia}+ = R; từng thuộc tính đơn lẻ không xác định toàn bộ quan hệ nên khóa là tối thiểu.

**Xét 1NF:** Mỗi thuộc tính có giá trị đơn nên đạt 1NF.

**Xét 2NF:** Không có thuộc tính không khóa phụ thuộc bộ phận vào khóa ghép; đạt 2NF.

**Xét 3NF:** Không có phụ thuộc hàm không tầm thường vi phạm điều kiện 3NF; đạt 3NF.

**Xét BCNF:** Không có phụ thuộc hàm không tầm thường có vế trái không là siêu khóa; đạt BCNF.

**Xét 4NF:** MaThe ↠ TuDongNghia là phụ thuộc đa trị tầm thường vì {MaThe, TuDongNghia} = R. Theo ràng buộc nghiệp vụ, không có phụ thuộc đa trị không tầm thường nào vi phạm điều kiện siêu khóa; đạt 4NF.

**Kết luận:** Quan hệ TheDongNghia đạt 4NF.

### 25. Quan hệ ViDuTheGhiNho

**Ý nghĩa nghiệp vụ:** Lưu riêng từng câu ví dụ của một thẻ; các ví dụ được bổ sung hoặc điều chỉnh độc lập với danh sách từ đồng nghĩa.

**Lược đồ R:** ViDuTheGhiNho(MaThe, ViDu).

**Phụ thuộc hàm:** ∅ (không xác lập phụ thuộc hàm không tầm thường).

**Phủ tối thiểu:** ∅; không có phụ thuộc hàm không tầm thường để tối giản.

**Khóa chính:** {MaThe, ViDu}.

**Tìm khóa chính:** {MaThe, ViDu}+ = R; từng thuộc tính đơn lẻ không xác định toàn bộ quan hệ nên khóa là tối thiểu.

**Xét 1NF:** Mỗi thuộc tính có giá trị đơn nên đạt 1NF.

**Xét 2NF:** Không có thuộc tính không khóa phụ thuộc bộ phận vào khóa ghép; đạt 2NF.

**Xét 3NF:** Không có phụ thuộc hàm không tầm thường vi phạm điều kiện 3NF; đạt 3NF.

**Xét BCNF:** Không có phụ thuộc hàm không tầm thường có vế trái không là siêu khóa; đạt BCNF.

**Xét 4NF:** MaThe ↠ ViDu là phụ thuộc đa trị tầm thường vì {MaThe, ViDu} = R. Theo ràng buộc nghiệp vụ, không có phụ thuộc đa trị không tầm thường nào vi phạm điều kiện siêu khóa; đạt 4NF.

**Kết luận:** Quan hệ ViDuTheGhiNho đạt 4NF.

# CHƯƠNG 4. TỔNG HỢP VÀ XÁC ĐỊNH DẠNG CHUẨN CHUNG

## 4.1. Bảng tổng hợp dạng chuẩn các quan hệ

|  |  |  |  |
| --- | --- | --- | --- |
| STT | Quan hệ | Khóa chính | Kết quả chứng minh dạng chuẩn |
| 1 | NhomNguLieuToeic | {MaNhomNguLieu} | 3NF |
| 2 | CauHoiToeic | {MaCauHoi} | 3NF |
| 3 | LuaChonCauHoi | {MaLuaChon} | 3NF |
| 4 | TheGhiNho | {MaThe} | 3NF |
| 5 | LanLamBai | {MaLanLamBai} | BCNF |
| 6 | CauHoiLanLamBai | {MaChiTiet} | BCNF |
| 7 | KetQuaChanDoan | {MaLanLamBai} | BCNF |
| 8 | KyNangYeuChanDoan | {MaLanLamBai, MaKyNang} | BCNF |
| 9 | MucOnTap | {MaMucOnTap} | BCNF |
| 10 | TuongTacCauHoi | {MaTuongTac} | BCNF |
| 11 | LoTrinhHoc | {MaLoTrinh} | BCNF |
| 12 | TuanLoTrinh | {MaTuan} | BCNF |
| 13 | KyNangConTuanLoTrinh | {MaTuan, MaKyNang} | BCNF |
| 14 | CuocHoiThoai | {MaCuocHoiThoai} | BCNF |
| 15 | TinNhan | {MaTinNhan} | BCNF |
| 16 | DonThanhToan | {MaDonThanhToan} | BCNF |
| 17 | DangKyGoiNguoiDung | {MaDangKy} | BCNF |
| 18 | NguoiDung | {MaNguoiDung} | 4NF |
| 19 | KyNangToeic | {MaKyNang} | 4NF |
| 20 | BoDeToeic | {MaBoDe} | 4NF |
| 21 | ChuDeTheGhiNho | {MaChuDe} | 4NF |
| 22 | TaiNguyenAnh | {LoaiDoiTuong, MaDoiTuong, DuongDanAnh} | 4NF |
| 23 | TaiNguyenAmThanh | {LoaiDoiTuong, MaDoiTuong, DuongDanAmThanh} | 4NF |
| 24 | TheDongNghia | {MaThe, TuDongNghia} | 4NF |
| 25 | ViDuTheGhiNho | {MaThe, ViDu} | 4NF |

## 4.2. Xác định dạng chuẩn chung

Tập G gồm 25 quan hệ: 4 quan hệ có dạng chuẩn cao nhất được xác định là 3NF; 13 quan hệ đã được chứng minh đạt BCNF theo phụ thuộc hàm nhưng chưa đủ cơ sở kết luận về 4NF; và 8 quan hệ được đánh giá đạt 4NF theo các ràng buộc nghiệp vụ. Trong nhóm 4NF, TheDongNghia và ViDuTheGhiNho quản lý độc lập hai tập dữ liệu của thẻ ghi nhớ. Quan hệ khảo sát F trước phân rã không được tính vào G. Vì còn các quan hệ không đạt BCNF, dạng chuẩn chung của hệ thống khảo sát là DC(G) = 3NF.