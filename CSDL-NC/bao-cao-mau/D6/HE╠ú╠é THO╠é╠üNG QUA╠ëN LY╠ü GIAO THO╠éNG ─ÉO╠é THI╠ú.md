### **Đề tài: CSDL phân tán cho quản lý giao thông đô thị.**

### **HỆ THỐNG QUẢN LÝ GIAO THÔNG ĐÔ THỊ**

Sở Giao thông Vận tải (GTVT) của một đô thị lớn chịu trách nhiệm quản lý hạ tầng giao thông, còn Phòng Cảnh sát giao thông (CSGT) chịu trách nhiệm đăng ký phương tiện, cấp giấy phép lái xe và xử lý vi phạm. Do dữ liệu của hai đơn vị nằm rải rác, việc điều phối, tra cứu và xử phạt còn chậm, thiếu nhất quán. Vì vậy, cần tin học hóa khâu quản lý thông tin hạ tầng, phương tiện, vi phạm và sự cố giao thông như sau:

Thành phố được chia thành nhiều quận/huyện. Thông tin của một quận/huyện được phân biệt bằng mã quận/huyện, tên quận/huyện, diện tích, dân số... Mỗi quận/huyện do một đơn vị xử lý phụ trách (đội CSGT quận, phòng quản lý đô thị). Thông tin của đơn vị xử lý gồm mã đơn vị, tên đơn vị, địa chỉ, số điện thoại... Một đơn vị xử lý có nhiều cán bộ làm việc như cán bộ điều hành trung tâm, cán bộ xử lý vi phạm, cán bộ đăng ký, cán bộ kỹ thuật, CSGT hiện trường. Thông tin của một cán bộ phân biệt bằng mã cán bộ, họ tên, phái, ngày sinh, chức vụ, số điện thoại... Một cán bộ chỉ thuộc một đơn vị xử lý tại một thời điểm.

Trên địa bàn có rất nhiều tuyến đường, mỗi tuyến đường được phân biệt bằng mã tuyến đường, tên tuyến đường, chiều dài, số làn xe, tốc độ tối đa, ngày đưa vào sử dụng... và thuộc một loại đường duy nhất (quốc lộ, đường nội đô, cao tốc...). Một loại đường bao gồm nhiều tuyến đường, một tuyến đường nằm trong một quận/huyện. Các tuyến đường giao cắt nhau tại các nút giao; thông tin của nút giao gồm mã nút giao, tên nút giao, tọa độ, loại nút giao... Một nút giao là nơi giao cắt của từ hai tuyến đường trở lên, một tuyến đường có thể đi qua nhiều nút giao.

Tại các nút giao hoặc dọc theo tuyến đường, Sở GTVT lắp đặt các thiết bị giao thông như đèn tín hiệu, camera giám sát, cảm biến đếm xe. Thông tin thiết bị được phân biệt bằng mã thiết bị, tên thiết bị, vị trí lắp đặt, ngày lắp đặt, tình trạng hoạt động... Mỗi thiết bị thuộc một loại thiết bị duy nhất (mã loại thiết bị, tên loại thiết bị, chu kỳ bảo trì) và được lắp đặt tại một nút giao hoặc một tuyến đường cụ thể. Khi thiết bị hư hỏng hoặc đến kỳ bảo trì, cán bộ kỹ thuật lập phiếu bảo trì ghi rõ thiết bị, ngày yêu cầu, nội dung công việc, ngày hoàn thành và chi phí.

Chủ phương tiện là cá nhân hoặc doanh nghiệp có nhu cầu đăng ký phương tiện, thông tin gồm mã chủ phương tiện, họ tên (hoặc tên doanh nghiệp), số CCCD (hoặc mã số thuế), địa chỉ, số điện thoại, email... Một chủ phương tiện có thể sở hữu nhiều phương tiện. Phương tiện được phân biệt bằng số khung, số máy, kèm các thông tin như hãng xe, màu sắc, năm sản xuất... và thuộc một loại phương tiện duy nhất (xe máy, ô tô con, xe tải, xe khách...). Khi đăng ký, cán bộ đăng ký kiểm tra hồ sơ, cấp biển số và lập hồ sơ đăng ký ghi rõ phương tiện, chủ phương tiện, biển số, ngày đăng ký. Khi phương tiện được sang tên hoặc đổi chủ thì lập hồ sơ đăng ký mới; tại một thời điểm, một phương tiện chỉ có một hồ sơ đăng ký đang có hiệu lực. Định kỳ, phương tiện phải đến trung tâm đăng kiểm để lập phiếu đăng kiểm gồm số phiếu, ngày kiểm định, kết quả, ngày hết hạn. Nếu kết quả đạt thì phương tiện được cấp thời hạn lưu hành mới; nếu hết hạn đăng kiểm thì hệ thống cảnh báo và hạn chế các thủ tục hành chính liên quan.

Người điều khiển phương tiện phải có giấy phép lái xe (GPLX) do CSGT cấp. Thông tin người điều khiển gồm mã người điều khiển, họ tên, ngày sinh, số CCCD, địa chỉ... Mỗi hạng bằng (A1, A2, B1, B2, C...) được lưu với mã hạng, tên hạng và loại phương tiện được phép điều khiển. Mỗi lần cấp, đổi hoặc cấp lại, cán bộ lập một GPLX ghi rõ số GPLX, hạng bằng, ngày cấp, ngày hết hạn. Tại một thời điểm, một người điều khiển chỉ có một GPLX còn hiệu lực cho mỗi hạng bằng.

Trong quá trình vận hành, các camera và cảm biến liên tục thu thập dữ liệu về giao thông. Hệ thống ghi nhận thành các bản ghi lưu lượng gồm thiết bị thu thập, thời điểm, mật độ phương tiện, vận tốc trung bình. Khi mật độ vượt ngưỡng quy định, cán bộ điều hành trung tâm nhận cảnh báo, điều chỉnh chu kỳ đèn tín hiệu và điều động lực lượng ra hiện trường. Mỗi lần điều chỉnh được lưu thành một lệnh điều tiết ghi rõ đèn tín hiệu được điều chỉnh, cán bộ thực hiện, thời điểm, chu kỳ cũ, chu kỳ mới và lý do. Chỉ cán bộ có thẩm quyền mới được thực hiện lệnh điều tiết.

Khi camera AI hoặc CSGT hiện trường phát hiện hành vi sai phạm, hệ thống tạo một vi phạm gồm mã vi phạm, thời điểm, địa điểm, nguồn phát hiện (camera hoặc CSGT), gắn với phương tiện thông qua biển số, thiết bị hoặc cán bộ phát hiện. Mỗi vi phạm thuộc một lỗi duy nhất trong danh mục lỗi; mỗi lỗi được phân biệt bằng mã lỗi, tên lỗi, khung phạt từ mức thấp nhất đến mức cao nhất, hình thức phạt bổ sung (tước GPLX, tạm giữ xe...). Một vi phạm phải có ít nhất một bằng chứng (ảnh hoặc video) kèm thời gian và vị trí. Đối với vi phạm do camera phát hiện, cán bộ xử lý phải xác minh bằng chứng; nếu hợp lệ sẽ lập quyết định xử phạt ghi rõ số quyết định, ngày ra quyết định, mức phạt, hình thức bổ sung và hạn nộp, rồi thông báo cho chủ phương tiện. Mức phạt được xác định dựa vào lỗi vi phạm, loại phương tiện và số lần tái phạm. Một vi phạm chỉ có một quyết định xử phạt.

Sau khi nhận quyết định, chủ phương tiện có thể nộp phạt trực tuyến hoặc tại quầy; mỗi lần nộp tạo một giao dịch thanh toán gồm mã giao dịch, ngày nộp, số tiền, kênh thanh toán. Một quyết định có thể được thanh toán nhiều lần cho đến khi đủ số tiền. Chủ phương tiện cũng có quyền gửi đơn khiếu nại ghi rõ nội dung, ngày gửi để cán bộ xem xét lại; kết quả xử lý khiếu nại được lưu cùng ngày xử lý. Nếu quá hạn mà chưa nộp phạt và không có khiếu nại hợp lệ, quyết định chuyển sang trạng thái cưỡng chế.

Khi xảy ra tai nạn hoặc sự cố, thông tin có thể đến từ hotline, camera hoặc người dân. Cán bộ trung tâm tạo sự cố gồm mã sự cố, loại sự cố, thời điểm, vị trí, mức độ nghiêm trọng, đơn vị xử lý phụ trách, rồi điều động lực lượng cứu hộ và CSGT ra hiện trường. Các phương tiện và người điều khiển liên quan được ghi nhận qua chi tiết sự cố, trong đó ghi rõ vai trò và mức độ thiệt hại của từng phương tiện. Một sự cố có thể liên quan đến nhiều phương tiện, một phương tiện có thể tham gia nhiều sự cố khác nhau. Khi xử lý xong, cán bộ lập hồ sơ kết thúc sự cố. Ngoài ra, người dân có thể gửi phản ánh kèm hình ảnh, vị trí; thông tin phản ánh gồm mã phản ánh, nội dung, ngày gửi, người gửi. Phản ánh được chuyển cho đơn vị xử lý phụ trách và phải được phản hồi trong thời hạn quy định, ngày phản hồi và nội dung phản hồi được lưu lại.

Hàng tháng, lãnh đạo xem báo cáo thống kê về số vụ vi phạm, tai nạn, lưu lượng giao thông, điểm đen giao thông và doanh thu tiền phạt theo từng khu vực, tuyến đường, để lập kế hoạch bảo trì hạ tầng, bố trí lực lượng và điều chỉnh chính sách điều tiết giao thông hiệu quả.

**MÔ TẢ THỰC THỂ**

1. Thực thể CƠ BẢN

| STT | Thực thể | Thuộc tính chính | Lý do xếp vào Cơ bản |
| --- | --- | --- | --- |
| 1 | LOẠI\_ĐƯỜNG | Mã loại đường, tên loại đường | Danh mục phân loại, số lượng cố định |
| 2 | TUYẾN\_ĐƯỜNG | Mã tuyến, tên tuyến, chiều dài, số làn, tốc độ tối đa, ngày đưa vào sử dụng | Hạ tầng có trước hệ thống; thời gian duy nhất là ngày đưa vào sử dụng |
| 3 | NÚT\_GIAO | Mã nút giao, tên nút giao, tọa độ, loại nút giao | Hạ tầng cố định, ít thay đổi |
| 4 | LOẠI\_THIẾT\_BỊ | Mã loại, tên loại, chu kỳ bảo trì | Danh mục phân loại, ổn định |
| 5 | THIẾT\_BỊ\_GIAO\_THÔNG | Mã thiết bị, tên thiết bị, vị trí lắp đặt, ngày lắp đặt, tình trạng | Tài sản có sẵn; chỉ có ngày lắp đặt |
| 6 | LOẠI\_PHƯƠNG\_TIỆN | Mã loại, tên loại | Danh mục phân loại, ổn định |
| 7 | PHƯƠNG\_TIỆN | Số khung, số máy, hãng xe, màu sắc, năm sản xuất | Tồn tại trước hệ thống; chỉ có năm sản xuất |
| 8 | HẠNG\_BẰNG | Mã hạng, tên hạng, loại phương tiện được phép điều khiển | Danh mục quy định sẵn, ít thay đổi |
| 9 | DANH\_MỤC\_LỖI | Mã lỗi, tên lỗi, khung phạt thấp nhất, khung phạt cao nhất, hình thức phạt bổ sung | Bộ quy định pháp luật có trước hệ thống, ít thay đổi |

2. Thực thể ĐỐI TƯỢNG NGOÀI

| STT | Thực thể | Thuộc tính chính | Loại | Lý do |
| --- | --- | --- | --- | --- |
| 1 | QUẬN\_HUYỆN | Mã quận/huyện, tên, diện tích, dân số | Tổ chức (đơn vị hành chính) | Đơn vị hành chính cố định, là đối tượng bên ngoài mà hệ thống quản lý theo khu vực |
| 2 | ĐƠN\_VỊ\_XỬ\_LÝ | Mã đơn vị, tên đơn vị, địa chỉ, số điện thoại | Tổ chức | Đội CSGT quận, phòng quản lý đô thị |
| 3 | CÁN\_BỘ | Mã cán bộ, họ tên, phái, ngày sinh, chức vụ, số điện thoại | Con người | Người vận hành hệ thống, có thuộc tính ngày sinh |
| 4 | CHỦ\_PHƯƠNG\_TIỆN | Mã chủ, họ tên/tên doanh nghiệp, CCCD/MST, địa chỉ, số điện thoại, email | Con người / Tổ chức | Cá nhân hoặc doanh nghiệp sở hữu xe |
| 5 | NGƯỜI\_ĐIỀU\_KHIỂN | Mã người điều khiển, họ tên, ngày sinh, CCCD, địa chỉ | Con người | Người có GPLX |
| 6 | NGƯỜI\_DÂN | Mã người dân, họ tên, số điện thoại | Con người | Người gửi phản ánh |

3. Thực thể NGHIỆP VỤ

| STT | Thực thể | Thuộc tính chính | Thuộc tính thời gian | Lý do |
| --- | --- | --- | --- | --- |
| 1 | HỒ\_SƠ\_ĐĂNG\_KÝ | Số hồ sơ, biển số, phương tiện, chủ phương tiện | Ngày đăng ký | Phát sinh mỗi lần đăng ký, sang tên, đổi chủ |
| 2 | PHIẾU\_ĐĂNG\_KIỂM | Số phiếu, kết quả | Ngày kiểm định, ngày hết hạn | Phát sinh định kỳ theo từng phương tiện |
| 3 | GIẤY\_PHÉP\_LÁI\_XE | Số GPLX, hạng bằng, người điều khiển | Ngày cấp, ngày hết hạn | Mỗi lần cấp, đổi, cấp lại là một mẫu tin |
| 4 | PHIẾU\_BẢO\_TRÌ | Số phiếu, thiết bị, cán bộ kỹ thuật, nội dung, chi phí | Ngày yêu cầu, ngày hoàn thành | Phát sinh khi thiết bị hỏng hoặc đến kỳ bảo trì |
| 5 | BẢN\_GHI\_LƯU\_LƯỢNG | Thiết bị thu thập, mật độ, vận tốc trung bình | Thời điểm ghi nhận | Phát sinh liên tục, số lượng tăng rất nhanh |
| 6 | LỆNH\_ĐIỀU\_TIẾT | Đèn tín hiệu, cán bộ, chu kỳ cũ, chu kỳ mới, lý do | Thời điểm điều chỉnh | Mỗi lần điều chỉnh đèn là một mẫu tin |
| 7 | VI\_PHẠM | Mã vi phạm, lỗi, biển số, nguồn phát hiện, địa điểm, thiết bị/cán bộ phát hiện | Thời điểm vi phạm | Phát sinh khi vận hành, tăng dần |
| 8 | BẰNG\_CHỨNG | Mã bằng chứng, vi phạm, loại (ảnh/video), vị trí | Thời gian ghi nhận | Gắn với từng vi phạm |
| 9 | QUYẾT\_ĐỊNH\_XỬ\_PHẠT | Số quyết định, vi phạm, cán bộ xử lý, mức phạt, hình thức bổ sung, trạng thái | Ngày ra quyết định, hạn nộp | Chỉ sinh ra sau khi xác minh vi phạm |
| 10 | GIAO\_DỊCH\_THANH\_TOÁN | Mã giao dịch, quyết định, số tiền, kênh thanh toán | Ngày nộp | Mỗi lần nộp phạt là một mẫu tin |
| 11 | ĐƠN\_KHIẾU\_NẠI | Mã đơn, quyết định, nội dung, kết quả xử lý | Ngày gửi, ngày xử lý | Phát sinh khi chủ phương tiện không đồng ý |
| 12 | SỰ\_CỐ | Mã sự cố, loại sự cố, vị trí, mức độ nghiêm trọng, đơn vị phụ trách | Thời điểm xảy ra | Phát sinh khi vận hành, tăng dần |
| 13 | CHI\_TIẾT\_SỰ\_CỐ | Sự cố, phương tiện, người điều khiển, vai trò, mức độ thiệt hại | (theo sự cố) | Thực thể kết hợp N–N giữa Sự cố và Phương tiện |
| 14 | PHẢN\_ÁNH | Mã phản ánh, người dân, nội dung, hình ảnh, vị trí, nội dung phản hồi | Ngày gửi, ngày phản hồi | Phát sinh khi người dân gửi ý kiến |

**PHẦN PHỤ THUỘC HÀM**

| **STT** | **Tên bảng** | **Phụ thuộc hàm** |
| --- | --- | --- |
| 1 | LOAI\_DUONG | MaLoaiDuong → TenLoaiDuong |
| 2 | TUYEN\_DUONG | MaTuyen → TenTuyen, ChieuDai, SoLan, TocDoToiDa, NgayDung |
| 3 | NUT\_GIAO | MaNutGiao → TenNutGiao, ToaDo, LoaiNutGiao |
| 4 | LOAI\_THIET\_BI | MaLoaiThietBi → TenLoaiThietBi, ChuKyBaoTri |
| 5 | THIET\_BI\_GIAO\_THONG | MaThietBi → TenThietBi, ViTriLapDat, NgayLapDat, TinhTrang, MaLoaiThietBi |
| 6 | LOAI\_PHUONG\_TIEN | MaLoaiPT → TenLoaiPT |
| 7 | PHUONG\_TIEN | SoKhung → SoMay, MaLoaiPT, MaHang, MauSac, NamSanXuat |
| 8 | HANG\_BANG | MaHang → TenHang, LoaiPhuongTien, PhepDieuKhien |
| 9 | DANH\_MUC\_LOI | MaLoi → TenLoi, PhatThapNhat, PhatCaoNhat, HinhThucPhat |

Nhóm thực thể đối tượng ngoài

| **STT** | **Tên bảng** | **Phụ thuộc hàm** |
| --- | --- | --- |
| 1 | QUAN\_HUYEN | MaQuanHuyen → TenQuanHuyen, DienTich, DanSo |
| 2 | DON\_VI\_XU\_LY | MaDonVi → TenDonVi, DiaChi, SoDienThoai |
| 3 | CAN\_BO | MaCanBo → HoTen, Phai, NgaySinh, ChucVu, SoDienThoai |
| 4 | CHU\_PHUONG\_TIEN | MaChu → HoTen\_TenDoanhNghiep, CCCD\_MST, DiaChi, SoDienThoai, Email |
| 5 | NGUOI\_DIEU\_KHIEN | MaNguoiDK → HoTen, NgaySinh, CCCD, DiaChi, SoGPLX |
| 6 | NGUOI\_DAN | MaNguoiDan → HoTen, SoDienThoai |

Nhóm thực thể nghiệp vụ

| **STT** | **Tên bảng** | **Phụ thuộc hàm** |
| --- | --- | --- |
| 1 | HO\_SO\_DANG\_KY | SoHoSo → BienSo, SoKhung, MaChu, NgayDangKy |
| 2 | PHIEU\_DANG\_KIEM | SoPhieu, SoKhung → NgayKiemDinh, NgayHetHan, KetQua |
| 3 | GIAY\_PHEP\_LAI\_XE | SoGPLX → MaHang, MaNguoiDK, NgayCap, NgayHetHan |
| 4 | PHIEU\_BAO\_TRI | SoPhieu, MaThietBi → NgayYeuCau, NgayHoanThanh, MaCanBo, NoiDung, ChiPhi |
| 5 | BAN\_GHI\_LUONG | MaThietBi, ThoiDiem → MatDoVanToc, SoLuongXe |
| 6 | LENH\_DIEU\_TIET | MaLenh → MaThietBi, ThoiDiem, MaCanBo, NoiDung, LyDo |
| 7 | VI\_PHAM | MaViPham → BienSo, MaLoi, NgayViPham, DiaDiem, MaThietBi, MaCanBo |
| 8 | BANG\_CHUNG | MaBangChung, MaViPham → LoaiBangChung, AnhVideo, ViTri, ThoiGianGhi |
| 9 | QUYET\_DINH\_XU\_PHAT | SoQuyetDinh → MaViPham, MaCanBo, MucPhat, HinhThucXuPhat, NgayQuyetDinh, HanNop |
| 10 | GIAO\_DICH\_THANH\_TOAN | MaGiaoDich → SoQuyetDinh, SoTien, NgayNop, TrangThai |
| 11 | DON\_KHIEU\_NAI | MaDon → SoQuyetDinh, NoiDung, NgayGui, NgayXuLy, KetQua |
| 12 | SU\_CO | MaSuCo → LoaiSuCo, ViTri, MucDo, ThoiDiem, MaNguoiDan |
| 13 | CHI\_TIET\_SU\_CO | MaSuCo, SoKhung → MaNguoiDK, VaiTro, MucDoThietHai |
| 14 | PHAN\_ANH | MaPhanAnh → MaNguoiDan, NoiDung, HinhAnh, ViTri, NgayGui, NgayPhanHoi |