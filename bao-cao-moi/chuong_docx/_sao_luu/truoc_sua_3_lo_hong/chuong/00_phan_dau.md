# LỜI MỞ ĐẦU

Bán lẻ linh kiện máy tính và thiết bị công nghệ là công việc có nhiều đặc thù: mỗi mặt hàng có thông số riêng, nhiều món có số seri từng chiếc, giá đổi thường xuyên, hàng đã mở hộp không thể bán lại như hàng mới, và thời hạn bảo hành kéo dài qua nhiều bên. Khi ghi chép bằng sổ tay hoặc bảng tính rời rạc, cửa hàng dễ gặp tình trạng dữ liệu trùng lắp, mâu thuẫn và khó truy vết một sản phẩm từ lúc nhập, bán, đổi trả đến bảo hành.

Nhận thấy điều đó, nhóm chọn đề tài **PowerTech – cửa hàng bán lẻ linh kiện máy tính** làm đề tài cho học phần Cơ sở dữ liệu nâng cao. Mục tiêu của nhóm không phải xây dựng phần mềm mà là **áp dụng kiến thức môn học để thiết kế, chuẩn hóa và đánh giá cơ sở dữ liệu** cho cửa hàng: xác định ba loại thực thể, tập phụ thuộc hàm, khóa, dạng chuẩn của từng lược đồ; phân rã và tổng hợp những lược đồ chưa đạt dạng chuẩn cao, kiểm tra bảo toàn thông tin và bảo toàn phụ thuộc hàm; tìm tình huống dạng chuẩn 4; rồi biểu diễn lược đồ thành đồ thị quan hệ, nêu các con đường truy xuất và viết truy vấn SQL cho các con đường đó.

Báo cáo gồm bốn chương: Chương 1 giới thiệu bài toán, ba loại thực thể và mô hình ERD; Chương 2 trình bày mô hình quan hệ, phân tích từng quan hệ và cải tiến lược đồ; Chương 3 trình bày đồ thị quan hệ, các con đường truy xuất và truy vấn SQL; Chương 4 là kết luận. Do thời gian và kiến thức còn hạn chế nên báo cáo không tránh khỏi thiếu sót, nhóm mong nhận được góp ý của thầy cô.

Nhóm xin chân thành cảm ơn!

# LỜI CẢM ƠN

Nhóm xin gửi lời cảm ơn đến quý thầy cô Khoa Công nghệ Thông tin, Trường Đại học Công nghệ TP.HCM (HUTECH) đã truyền đạt kiến thức nền tảng về cơ sở dữ liệu và phân tích thiết kế hệ thống để nhóm thực hiện đồ án này.

Nhóm đặc biệt cảm ơn thầy ThS. Võ Hoàng Khang đã hướng dẫn, nhận xét đề tài từ giai đoạn mô tả và cung cấp đề cương, bài giảng và báo cáo mẫu để nhóm làm đúng yêu cầu của học phần.

Cuối cùng, nhóm cảm ơn gia đình và các bạn đã hỗ trợ nhóm trong suốt quá trình học tập và thực hiện đề tài.

# LỜI CAM ĐOAN

Nhóm xin cam đoan nội dung đồ án học phần Cơ sở dữ liệu nâng cao “PowerTech – cơ sở dữ liệu cửa hàng bán lẻ linh kiện máy tính” là sản phẩm của nhóm 6, lớp 23DTHD6. Các tài liệu tham khảo đều có xuất xứ rõ ràng và được nêu ở phần Tài liệu tham khảo. Các phép tính phụ thuộc hàm, khóa, dạng chuẩn, bảo toàn và đồ thị đã được nhóm kiểm tra lại bằng chương trình nhỏ đi kèm báo cáo (thư mục `tools`). Nhóm xin chịu hoàn toàn trách nhiệm về lời cam đoan của mình.
