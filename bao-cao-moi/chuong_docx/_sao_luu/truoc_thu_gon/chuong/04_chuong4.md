# CHƯƠNG 4: KẾT LUẬN VÀ KIẾN NGHỊ

## 4.1 KẾT QUẢ ĐẠT ĐƯỢC

Đối chiếu với bảy nội dung của đề cương bài tập lớn:

| Nội dung đề cương | Kết quả | Mục |
|---|---|---|
| 1. Mô tả tóm tắt bài toán | Khảo sát, tính khả thi, đối tượng, phạm vi và mô tả nghiệp vụ bằng lời đời thường cho cả bán tại quầy lẫn bán trên trang web: tài khoản, giỏ hàng, nhân viên – vai trò – trách nhiệm, thanh toán, đặt cọc, đổi trả, bảo hành | 1.1 – 1.4 |
| 2. Ba loại thực thể và thuộc tính | 23 thực thể (6 cơ bản, 4 đối tượng ngoài, 13 nghiệp vụ), 8 mối kết hợp có thuộc tính, ERD có bản số (min,max) | 1.6, 1.7 |
| 3. Phụ thuộc hàm và khóa từng lược đồ | 31 quan hệ ban đầu, mỗi quan hệ có F, phủ tối thiểu 3 bước, khóa (N, TG, D), mọi khóa ứng viên | 2.2 |
| 4. Dạng chuẩn, phân rã/tổng hợp, bảo toàn | Lược đồ ban đầu chưa đạt 1NF; cải tiến 5 quan hệ, chứng minh bảo toàn thông tin (bảng a/b) và bảo toàn PTH; 32 quan hệ đạt BCNF | 2.3 |
| 5. Phụ thuộc đa trị, dạng chuẩn 4 | Tình huống ảnh – thông số mặt hàng: R₂ đạt BCNF nhưng không đạt 4NF, tách thành ANHMATHANG và GIATRITHONGSO; 1.538 dòng so với 3.256 dòng trên dữ liệu seed | 2.3.8 |
| 6. Đồ thị quan hệ, con đường truy xuất, ngữ nghĩa | 31 nút, 49 cung, 12 nút vào, 66 con đường truy xuất dài và bảng ngữ nghĩa các đường cơ bản | 3.1, 3.2 |
| 7. Truy vấn SQL cho các truy xuất | 66 câu truy vấn cho 66 đường và 9 truy vấn khai thác (có truy trách nhiệm theo nhân viên và vai trò), đã chạy thử trên dữ liệu minh họa; 1 đường rỗng đúng quy tắc | 3.3 |

*Bảng 4.1: Đối chiếu kết quả với đề cương bài tập lớn*

## 4.2 ƯU ĐIỂM

- Lược đồ cuối đạt BCNF ở cả 32 quan hệ, giữ nguyên quy tắc nghiệp vụ “số seri duy nhất trong cùng mặt hàng” nhờ phương án tách bốn thành phần bảo toàn cả thông tin lẫn phụ thuộc hàm.
- Một mô hình phục vụ cả hai kênh: khách mua tại quầy và khách mua trên trang web (tài khoản, sổ địa chỉ, giỏ hàng, đơn) dùng chung đơn hàng, thanh toán, kho, đổi trả và bảo hành.
- **Truy được trách nhiệm:** mỗi khâu quan trọng ghi người thực hiện hoặc duyệt; nhật ký tình trạng đơn ghi từng lần đổi; lịch sử giữ vai trò theo thời gian cho biết lúc xảy ra việc người đó giữ vai trò gì (truy vấn K6–K8).
- Mọi phép tính (bao đóng, phủ tối thiểu, khóa, dạng chuẩn, bảo toàn, đồ thị) được trình bày từng bước và đối chiếu bằng chương trình; số liệu trong báo cáo sinh từ cùng một nguồn nên không mâu thuẫn.
- Giữ giá và tên hàng tại thời điểm bán trong từng dòng đơn, không lưu tồn kho thành cột, nên các dị thường cập nhật phổ biến của bán lẻ được loại bỏ.
- Truy vết được một chiếc hàng từ nhà cung cấp, phiếu nhập, đơn bán, đổi trả đến bảo hành bằng các con đường truy xuất đã xác định.

## 4.3 HẠN CHẾ

- Nhiều phụ thuộc hàm là giả thiết nghiệp vụ nhóm tự đặt (G1–G6) vì chưa có số liệu vận hành thật của cửa hàng; dữ liệu mẫu không chứng minh được phụ thuộc hàm.
- Kết luận 4NF cho các quan hệ ngoài tình huống ảnh – thông số dựa trên mô tả nghiệp vụ, chưa chứng minh tổng quát.
- Quy tắc đặt tên của thuộc tính kép (họ lót và tên) là quy ước nhập liệu, không kiểm tra được bằng phụ thuộc hàm.
- Quy tắc “đúng vai trò mới được làm khâu đó” (duyệt hoàn tiền, chi tiền, xác nhận phiếu nhập…) là giả thiết nghiệp vụ của nhóm và chỉ cưỡng chế được khi ghi dữ liệu, không bằng khóa hay phụ thuộc hàm.
- Một số ràng buộc nhất quán liên quan hệ (mục 2.3.6) cần cài đặt bằng khóa ngoại ghép, kiểm tra khi ghi hoặc trigger; tình trạng hiện tại của đơn là bản sao của dòng nhật ký mới nhất nên phải giữ đồng bộ; quy ước dấu của sổ kho chưa chốt với cửa hàng.
- Dữ liệu minh họa chỉ có vài chục dòng, đủ để kiểm tra truy vấn chạy đúng chứ không đủ để đánh giá hiệu năng; báo cáo chưa đo hiệu năng và các chỉ mục ở mục 3.4 mới là đề xuất.
- Phạm vi giới hạn (mục 1.3): một cửa hàng, một kho; chưa có kiểm kê, công nợ, trả góp, hỗ trợ khách bằng phiếu yêu cầu, đánh giá, thu cũ đổi mới, ví, thống kê; quản lý nhân sự chỉ dừng ở hồ sơ, vai trò và truy trách nhiệm, chưa có chấm công, lương, tuyển dụng.

## 4.4 HƯỚNG PHÁT TRIỂN

- Cài đặt lược đồ 32 quan hệ trên SQL Server, bổ sung ràng buộc toàn vẹn (kể cả ràng buộc vai trò – khâu) và bảng tầm ảnh hưởng, thủ tục và khung nhìn báo cáo (doanh thu, tồn kho theo kỳ, trách nhiệm theo nhân viên).
- Mở rộng phạm vi theo website PowerTech: phiếu yêu cầu hỗ trợ, đánh giá sản phẩm, thu cũ đổi mới, ví; thêm kiểm kê định kỳ, nhiều kho hoặc showroom, công nợ nhà cung cấp, trả hàng nhà cung cấp, trả góp.
- Mở rộng quản lý nhân sự: chấm công, ca làm, lương theo doanh số; phân quyền đến từng chức năng.
- Đo hiệu năng các truy vấn theo con đường truy xuất trên dữ liệu thật và điều chỉnh chỉ mục.
- Xác nhận các giả thiết G1–G6 với cửa hàng thực tế và cập nhật phụ thuộc hàm nếu quy tắc thay đổi (ví dụ chuyển sang “seri duy nhất toàn cửa hàng”).
