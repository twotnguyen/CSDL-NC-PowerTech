<!-- Slide number: 1 -->
# ĐỀ CƯƠNG BÀI TẬP LỚN MÔN CSDLNC

YÊU CẦU
Mỗi nhóm chọn 1 đề tài (có thể lấy ĐACS hay ĐACN để làm). 1-3SV/nhóm. Nhóm có hơn 3 SV thì yêu cầu sẽ cao hơn, GV sẽ xem xét.

1. Mô tả tóm tắt bài toán cần quản lý (giống như mô tả tình huống trong môn PTTK HTTT).
2. Đề nghị CSDL thích hợp (Xác định 3 loại thực thể và các thuộc tính tương ứng).
3. Xác định tập phụ thuộc hàm tương ứng cho từng LĐQH, từ đó xác định khóa của từng lược đồ.
4. Xác định dạng chuẩn của từng lược đồ. Nếu vi phạm DC1, DC2 thì dùng thuật toán phân rã/tổng hợp/tổng hợp cải tiến để đạt DC cao hơn (DCBC, nếu ko được thì ít nhất là DC3). Kiểm tra tính bảo toàn thông tin và bảo toàn phụ thuộc hàm.

<!-- Slide number: 2 -->
# ĐỀ CƯƠNG BÀI TẬP LỚN MÔN CSDL NC
5. Tìm các phụ thuộc đa trị (nếu có, không có thì bỏ qua bước này) để phân rã thành đa trị tầm thường (không có ngữ cảnh) để đảm bảo lđ CSDL đạt dạng chuẩn 4.
6. Xây dựng đồ thị quan hệ. Nêu các con đường truy xuất  và ngữ nghĩa của từng con đường truy xuất trên.
7. Viết các truy vấn cho các truy xuất trên bằng ngôn ngữ SQL.