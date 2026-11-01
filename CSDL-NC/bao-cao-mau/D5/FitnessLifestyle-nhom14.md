**Hệ thống quản lý thể chất và lối sống thông minh Fitness & Lifestyle**

# Mô tả

Fitness & Lifestyle là hệ thống web và mobile hỗ trợ người dùng cá nhân tập luyện đúng kỹ thuật, theo dõi tiến độ và quản lý dinh dưỡng. Người dùng có thể tập tại nhà hoặc phòng tập, cần ghi nhận hồ sơ sức khỏe, buổi tập, kết quả phân tích tư thế và nhật ký ăn uống để theo dõi lâu dài. Web app và mobile app dùng chung một máy chủ API và một cơ sở dữ liệu. Đề tài xét một người dùng tập một mình trước camera, chưa xét huấn luyện viên, nhóm tập, cộng đồng, trò chuyện (chatbox), nhận diện thực phẩm qua ảnh, thiết bị đeo và thanh toán.

Mỗi người dùng đăng ký một tài khoản có mã, tên đăng nhập, email, mật khẩu và thời điểm tạo. Tên đăng nhập và email được chuẩn hóa và không được trùng nhau; mật khẩu chỉ được lưu dưới dạng băm. Mỗi tài khoản có một vai trò là người dùng hoặc quản trị viên. Người chưa đăng nhập chỉ được xem phần giới thiệu, đăng ký và đăng nhập. Sau khi đăng nhập, hệ thống cấp JWT chứa mã, tên đăng nhập, email và vai trò; các chức năng cá nhân chỉ trả về dữ liệu của chính tài khoản trong token, còn chức năng quản trị chỉ dành cho vai trò quản trị viên.

Mỗi người dùng có tối đa một hồ sơ sức khỏe gồm chiều cao, cân nặng, tuổi, giới tính, mức hoạt động và mục tiêu. Mức hoạt động thuộc năm mức với hệ số 1,2; 1,375; 1,55; 1,725 và 1,9. Mục tiêu gồm giảm cân, duy trì cân nặng hoặc tăng cơ. Khi hồ sơ được lưu, hệ thống tính BMI bằng cân nặng chia bình phương chiều cao theo mét, tính BMR theo công thức Mifflin-St Jeor, tính TDEE bằng BMR nhân hệ số hoạt động, rồi lưu cùng hồ sơ. BMI được xếp vào bốn mức: thiếu cân, bình thường, thừa cân và béo phì. Các chỉ số chỉ mang tính tham khảo, được giải thích trên giao diện và không thay thế tư vấn y tế.

Danh mục bài tập do quản trị viên quản lý. Mỗi bài tập có mã, tên, nhóm cơ, mô tả, hình ảnh hoặc video minh họa, giá trị MET tham khảo và lượng calo mỗi phút. Các bài tập được AI Coach hỗ trợ gồm squat, push-up, plank, lunge và jumping jack có thêm cấu hình phân tích: các keypoints chính, các pha chuyển động (hạ xuống, đẩy lên) cùng ngưỡng góc và điều kiện đánh giá. Một buổi tập hoặc một kết quả phân tích luôn thuộc đúng một bài tập; một bài tập có thể xuất hiện trong nhiều buổi tập của nhiều người dùng.

Thực phẩm cũng do quản trị viên quản lý, mỗi thực phẩm có mã, tên, lượng calo, protein, carbs, fat và hình ảnh nếu có, tính theo một khẩu phần chuẩn của thực phẩm đó. Người dùng chỉ tra cứu và chọn thực phẩm, không tự sửa dữ liệu danh mục. Tên thực phẩm không được dùng riêng để phân biệt vì có thể trùng. Dữ liệu ưu tiên các món phổ biến của Việt Nam và được mở rộng dần.

Người dùng ghi nhật ký dinh dưỡng theo từng lần ăn. Mỗi bản ghi có mã, người dùng, thực phẩm, số lượng, loại bữa ăn và ngày ghi. Cùng một thực phẩm có thể được ghi nhiều lần trong ngày hoặc ở các bữa khác nhau. Tổng calo, protein, carbs và fat của một ngày bằng tổng giá trị dinh dưỡng của thực phẩm nhân với số lượng của các bản ghi trong ngày đó. Hệ thống đối chiếu lượng nạp vào với TDEE và đưa ra gợi ý theo mục tiêu: giảm cân thì mức khuyến nghị thấp hơn TDEE, tăng cơ thì cao hơn TDEE kèm lưu ý về protein, duy trì thì quanh TDEE. Gợi ý chỉ mang tính tham khảo.

Khi người dùng hoàn thành một lượt tập, hệ thống ghi nhận buổi tập gồm mã, người dùng, bài tập, số rep, số set, thời lượng, lượng calo tiêu hao, độ chính xác và thời điểm. Calo tiêu hao bằng MET của bài tập nhân cân nặng trong hồ sơ sức khỏe nhân thời gian tập tính theo giờ; vì vậy người dùng cần có hồ sơ sức khỏe trước khi ghi buổi tập. Lượng calo đã ghi của buổi tập không được tính lại khi hồ sơ thay đổi về sau.

AI Coach là chức năng trọng tâm. Người dùng chọn bài tập, bật camera hoặc tải video lên, hệ thống dùng mô hình MoveNet SinglePose Lightning chạy bằng TensorFlow.js ngay trên thiết bị để nhận diện 17 keypoints, mỗi điểm gồm tọa độ x, y và điểm tin cậy. Chỉ các keypoints vượt ngưỡng tin cậy mới được dùng để tính góc khớp; nếu một điểm quan trọng bị che khuất, hệ thống không kết luận lỗi mà nhắc người dùng chỉnh camera hoặc đứng trọn trong khung hình. Hệ thống xác định pha chuyển động, chỉ tính một rep khi đủ chu kỳ, tính độ chính xác theo mức đạt điều kiện tư thế và chỉ phân tích một người trong khung hình. Video thô được xử lý tại thiết bị, máy chủ nhận kết quả đã xử lý.

Khi kết thúc phân tích, thiết bị gửi về máy chủ số rep, số set, thời lượng, calo, độ chính xác, phản hồi, các lỗi tư thế phát hiện được và dữ liệu thô cần thiết để lưu thành kết quả phân tích. Mỗi kết quả thuộc một người dùng và một bài tập, có thể gắn với tối đa một buổi tập, nhưng việc gắn này không bắt buộc. Phản hồi được diễn đạt theo hành động cụ thể, ví dụ hạ người sâu hơn hoặc đặt camera xa hơn, và được xếp theo ba mức: duy trì form hiện tại, chỉnh nhẹ, ưu tiên sửa tư thế trước khi tăng cường độ. Tệp ảnh hoặc video tải lên phải được kiểm soát định dạng, dung lượng và tên tệp.

Dashboard và trang tiến độ không có dữ liệu nhập riêng mà tổng hợp từ buổi tập, kết quả phân tích, nhật ký dinh dưỡng và hồ sơ sức khỏe của chính người dùng. Theo ngày hoặc khoảng thời gian được chọn, hệ thống hiển thị tổng số rep, set, thời gian tập, calo đốt cháy, điểm form trung bình, lượng calo và macro nạp vào, biểu đồ xu hướng và lịch sử buổi tập, kèm các nhãn đánh giá dễ hiểu như Form tốt, Cần chỉnh nhẹ hoặc Nên ưu tiên sửa tư thế. Quản trị viên xem thêm thống kê chung của hệ thống.

Quản trị viên thêm, sửa, xóa hoặc ngừng sử dụng bài tập và thực phẩm, xem danh sách người dùng và thay đổi vai trò khi cần. Bài tập hoặc thực phẩm đã có buổi tập, kết quả phân tích hay nhật ký tham chiếu không được xóa theo cách làm mất lịch sử của người dùng. Các thông tin kỹ thuật phục vụ phát triển như địa chỉ máy chủ hay trạng thái kết nối không hiển thị trên giao diện người dùng cuối.

Mobile app xây dựng bằng React Native và Expo, dùng lại các API của web app để đăng nhập, xem hồ sơ, chọn bài tập, dùng camera, lưu kết quả phân tích, ghi dinh dưỡng và xem tiến độ. Dữ liệu trên web và mobile là một, một người dùng đăng nhập ở thiết bị nào cũng thấy cùng lịch sử. Cơ sở dữ liệu còn có bảng huy hiệu và huy hiệu người dùng để dự phòng cho gamification, nhưng chưa thuộc chức năng trọng tâm. Các nội dung như chatbox, nhận diện thực phẩm qua ảnh, phân tích nhiều người, thực đơn gợi ý và kết nối thiết bị đeo là hướng phát triển sau này.

# MÔ TẢ THỰC THỂ

## 1 Thực thể CƠ BẢN

| **Thực thể** | **Thuộc tính chính** | **Ý nghĩa và lý do phân loại** |
| --- | --- | --- |
| Bài tập | MaBT, TenBT, NhomCo, MoTa, HinhAnhVideo, MET, CaloPhut | Danh mục bài tập do quản trị viên quản lý, dùng chung cho buổi tập và phân tích tư thế. Không phụ thuộc người dùng cụ thể nên xếp vào nhóm cơ bản; MET là căn cứ tính calo tiêu hao. |
| Cấu hình phân tích tư thế | MaBT, keypoints chính, pha chuyển động, ngưỡng góc, điều kiện đánh giá | Quy tắc để AI Coach nhận biết rep và lỗi cho từng bài (squat, push-up, plank, lunge, jumping jack). Là thông tin nền của bài tập, khác với kết quả phân tích của từng lần tập. |
| Thực phẩm | MaTP, TenTP, Calo, Protein, Carbs, Fat, HinhAnh | Danh mục thực phẩm dùng chung cho mọi nhật ký ăn uống. Tên thực phẩm chưa được giả định duy nhất; giá trị dinh dưỡng hiện tại không thay thế các bản ghi đã lập. |
| Mức hoạt động | MaMucHD, TenMuc, HeSo | Năm mức hoạt động với hệ số 1,2 đến 1,9 dùng tính TDEE. Giá trị cố định, người dùng chỉ chọn mà không chỉnh sửa. |
| Mục tiêu | MaMucTieu, TenMucTieu | Giảm cân, duy trì hoặc tăng cơ. Xác định hướng điều chỉnh lượng calo khuyến nghị so với TDEE. |
| Loại bữa ăn | MaBua, TenBua | Danh mục phân nhóm bản ghi nhật ký theo bữa trong ngày. Chỉ là giá trị phân loại. |
| Phân loại BMI | MaPL, TenMuc, BMITu, BMIDen, GoiYHienThi | Bốn mức thiếu cân, bình thường, thừa cân, béo phì với khoảng giá trị và gợi ý hiển thị. Giá trị BMI của từng người là dữ liệu tính, không thuộc thực thể này. |
| Vai trò | MaVaiTro, TenVaiTro | Người dùng và quản trị viên. Danh mục quyền hạn, phân biệt chức năng được truy cập; một tài khoản chỉ có một vai trò. |
| Huy hiệu | MaHuyHieu, TenHuyHieu, MoTa | Bảng phụ có sẵn trong cơ sở dữ liệu cho gamification, không thuộc chức năng trọng tâm của đề tài. |

Các danh mục nhỏ như mức hoạt động, mục tiêu, loại bữa ăn và phân loại BMI có thể được cài đặt dưới dạng kiểu liệt kê trong mã nguồn; ở mức mô tả vẫn tách ra để làm rõ miền giá trị. BMI, BMR và TDEE của từng người là giá trị tính toán lưu cùng hồ sơ sức khỏe, không phải danh mục. Ảnh, video minh họa và cấu hình AI là thông tin thành phần của bài tập.

## 2 Thực thể ĐỐI TƯỢNG NGOÀI

| **Thực thể** | **Thuộc tính chính** | **Vai trò và lý do phân loại** |
| --- | --- | --- |
| Người dùng | MaND, TenDangNhap, Email, MatKhauBam, MaVaiTro, NgayTao | Người tập luyện sử dụng hệ thống qua web hoặc mobile, đồng thời là chủ sở hữu tài khoản và toàn bộ dữ liệu cá nhân. Tên đăng nhập và email phải duy nhất; mật khẩu chỉ lưu dạng băm. |
| Quản trị viên | Cùng bảng người dùng, MaVaiTro là quản trị | Người quản lý dữ liệu nền và tài khoản. Không tách bảng riêng vì cùng cấu trúc truy cập với người dùng, chỉ khác vai trò. |

Web app, mobile app và backend API là tác nhân kỹ thuật, chỉ gửi yêu cầu và xử lý dữ liệu nên không được xem là thực thể lưu trữ. Mô hình MoveNet chạy trên thiết bị người dùng và không phải đối tượng ngoài của cơ sở dữ liệu.

## 3 Thực thể NGHIỆP VỤ

| **Thực thể hoặc hồ sơ chính** | **Thuộc tính chính** | **Thời gian và ý nghĩa phát sinh** |
| --- | --- | --- |
| Hồ sơ sức khỏe | MaHS, MaND, ChieuCao, CanNang, Tuoi, GioiTinh, MucHD, MucTieu, BMI, BMR, TDEE | Phát sinh khi người dùng nhập lần đầu và được cập nhật về sau. Quan hệ một-một với người dùng; BMI, BMR, TDEE được tính tại thời điểm lưu và dùng cho dinh dưỡng, dashboard và tính calo. |
| Nhật ký dinh dưỡng | MaNK, MaND, MaTP, SoLuong, LoaiBua, NgayGhi | Phát sinh mỗi lần người dùng ghi một món ăn. Cùng thực phẩm có thể ghi nhiều lần; tổng calo và macro theo ngày được suy ra từ các bản ghi. |
| Buổi tập | MaBuoiTap, MaND, MaBT, Reps, Sets, ThoiLuong, CaloTieuHao, Accuracy, ThoiDiem | Phát sinh khi hoàn thành một lượt tập. Calo tiêu hao chốt theo cân nặng tại thời điểm ghi; một người dùng có nhiều buổi tập theo thời gian. |
| Kết quả phân tích tư thế | MaPT, MaND, MaBT, MaBuoiTap nếu có, Reps, Sets, ThoiLuong, Calo, Accuracy, Feedback, LoiPhatHien, DuLieuTho, ThoiDiem | Phát sinh khi AI Coach kết thúc phân tích từ camera hoặc video. Chỉ lưu kết quả đã xử lý, có thể gắn một buổi tập; dùng để xem lại lịch sử và cập nhật dashboard. |
| Dashboard, tiến độ và thống kê quản trị | Kỳ thống kê, tổng rep, set, thời gian, calo đốt, điểm form trung bình, calo nạp vào | Không lưu thành bảng riêng mà tính theo yêu cầu từ các dữ liệu trên, tại một kỳ xác định. Không thay thế dữ liệu gốc của buổi tập và nhật ký. |
| Huy hiệu người dùng | MaND, MaHuyHieu, NgayNhan | Bảng phụ ghi việc người dùng nhận huy hiệu, phục vụ mở rộng gamification; chưa thuộc phạm vi trọng tâm. |