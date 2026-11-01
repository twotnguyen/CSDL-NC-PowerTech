# Đối chiếu phần mô tả đề tài (mục 1.1–1.4) với các tài liệu khác

Ghi ngày 25/10/2026. Mục đích: trả lời "mô tả trong báo cáo mới có giống và đủ so với các bản mô tả khác không".

## 1. Nguồn đã đối chiếu

| Ký hiệu | Tài liệu | Ghi chú |
|---|---|---|
| WEB | `Documents/PowerTech.docx` (và `.pdf`) | Báo cáo môn Lập trình web. Đã đọc chữ của bản docx; chưa đọc riêng bản pdf và các hình sơ đồ trong đó (giả định pdf trùng nội dung docx). |
| NỘP1 | `bao-cao/PowerTech-CSDL-NC.docx` | Bản đầu nộp cho thầy (thầy chấm 7 điểm). Phần mô tả gồm 19 đoạn dạng đặc tả. |
| CŨ | `bao-cao/PowerTech_CSDLNC_Bao_cao.docx` | Báo cáo CSDL-NC làm trước đó, mục 1.1–1.3. |
| MỚI | `bao-cao-moi/…Bao_cao_moi.docx` mục 1.1–1.4 | Bản đang xét. |
| DB | `database/data.sql` | Hiện trạng cơ sở dữ liệu thật của web (tài liệu có thẩm quyền cao nhất về hiện trạng). |

Nhận xét của thầy về nhóm 6 (`23DTHD6.xlsx - Sheet1.md`): "Bổ sung hình thức mua trực tiếp tại cửa hàng. Cơ chế bảo hành, đổi hàng... ra sao?"

## 2. Kết luận ngắn

- **Đáp ứng nhận xét của thầy:** có. MỚI mô tả bán tại quầy (1.4.3), đổi trả với ba trường hợp, thời hạn và phí (1.4.7), bảo hành từng bước (1.4.8). NỘP1 chỉ nhắc quầy và bảo hành qua loa; WEB không có đổi trả và bảo hành chỉ là ticket.
- **Giống:** phần hàng hóa (loại, thương hiệu, SKU, ảnh, thông số), nhập hàng, mã giảm giá, thanh toán COD và chuyển khoản, giao hàng tối đa 3 lần, giá chốt tại thời điểm bán, ba nhóm tình trạng kho, trạng thái đơn.
- **Không đủ so với WEB và NỘP1:** MỚI cố ý thu hẹp phạm vi, bỏ nhiều phân hệ mà WEB, NỘP1 và DB đều có (bảng ở mục 3). Thu hẹp được phép (giảng viên đã nhắc nhiều nhóm phải giới hạn chức năng) nhưng danh sách "ngoài phạm vi" ở 1.3 **chưa nêu hết** các phần bị bỏ.
- **Có chỗ MỚI tự mâu thuẫn** (mục 4).

## 3. Bảng đối chiếu theo nội dung

Ký hiệu: ✔ có đủ; ~ có một phần; ✘ không có.

| Nội dung | WEB | NỘP1 | CŨ | MỚI | Nhận xét |
|---|---|---|---|---|---|
| Loại hàng phân cấp, thương hiệu, SKU, giá, giá khuyến mãi, thời hạn bảo hành | ✔ | ✔ | ✔ | ✔ | Khớp |
| Ảnh sản phẩm, thông số theo loại hàng (WEB gọi EAV) | ✔ | ✔ | ✔ | ✔ | Khớp |
| Số seri từng chiếc | ✘ (DB không có) | ✘ | ✔ | ✔ | Nhóm bổ sung từ thực tế cửa hàng, không có trong web hiện trạng. Nên nói rõ là "giả thiết nghiệp vụ" khi bảo vệ |
| Bán tại quầy (POS) | ✔ mã vạch, tiền mặt/thẻ/chuyển khoản, in hóa đơn, trừ kho | ~ | ✔ | ✔ | Đã bổ sung theo nhận xét của thầy |
| Bán từ xa, trạng thái đơn, khách tự hủy khi chưa xác nhận | ✔ | ✔ | ✔ | ✔ | Khớp (DB: Pending, Confirmed, Processing, Shipping, Completed, Cancelled, Returned; MỚI chưa có "đã trả") |
| Giỏ hàng | ✔ | ✔ | ✔ | ✘ (ngoài phạm vi, có nêu) | Có nêu ở 1.3 |
| Tài khoản đăng nhập, phân quyền nhiều vai trò (Admin, Sales, Kho, Hỗ trợ, Shipper, Khách) | ✔ | ✔ | ✔ | ✘ | Chỉ nêu "tài khoản trên trang web" ở 1.3; **không nêu** tài khoản và phân quyền nhân viên |
| Vai trò nhân viên | Admin, Sales, Warehouse, Support, Shipper | quản trị, bán hàng, kho, hỗ trợ, giao hàng, quản lý | thêm kỹ thuật, CSKH | tư vấn bán hàng, thu ngân, kỹ thuật, kho, giao hàng, quản lý | MỚI **không có quản trị và hỗ trợ**, thêm thu ngân và kỹ thuật |
| Sổ địa chỉ nhiều địa chỉ, địa chỉ mặc định | ✔ | ✔ | ✔ | ✘ | **Không nêu** ở 1.3 |
| Mã giảm giá (loại, hiệu lực, tối thiểu, tối đa, giới hạn lượt) | ✔ (thêm bật/tắt) | ✔ | ✔ | ✔ | Thiếu "kích hoạt/tạm dừng" (nhỏ) |
| Thanh toán nhiều lần, hoàn tiền | ~ | ✔ | ✔ | ✔ | MỚI chi tiết hơn |
| Đặt cọc | ✘ | ✘ | ✔ | ✔ | Nhóm thêm; DB không có |
| Giao hàng, tối đa 3 lần thất bại thì hủy, shipper | ✔ | ✔ | ✔ | ✔ | Khớp. WEB: shipper xác nhận thu COD; MỚI/NỘP1: bán hàng hoặc quản lý xác nhận (khác nhỏ) |
| Nhập hàng, nhà cung cấp, phiếu nhập | ✔ | ✔ | ✔ | ✔ | Khớp |
| Ba nhóm tình trạng kho, sổ kho | ✔ (sổ cái StockTransactions) | ✔ | ✔ | ✔ | Khớp. WEB còn có **cảnh báo tồn tối thiểu**, MỚI không nêu |
| Giữ hàng cho đơn | ✘ | ✔ | ✔ | ✘ (có nêu ngoài phạm vi) | |
| Kiểm kê, điều chỉnh kho có duyệt | ✘ | ✔ | ✔ | ✘ (có nêu ngoài phạm vi) | Xem mâu thuẫn ở mục 4 |
| Đổi trả hàng | ✘ (chỉ trạng thái "Returned") | ~ | ✔ | ✔ | Đã bổ sung theo nhận xét của thầy |
| Bảo hành | ~ (qua ticket, có số tháng) | ~ | ✔ | ✔ | Đã bổ sung theo nhận xét của thầy. WEB: khách gửi yêu cầu bảo hành online; MỚI: tiếp nhận tại cửa hàng |
| Đánh giá sản phẩm | ✔ | ✔ | ✘ | ✘ (có nêu ngoài phạm vi) | |
| Hỗ trợ khách: ticket, khiếu nại, tư vấn, chat, FAQ, mẫu trả lời | ✔ | ✔ | ✘ | ✘ | **Không nêu** ở 1.3 (chỉ bảo hành và đổi trả có trong MỚI) |
| Thu cũ đổi mới | ✔ | ✔ | ✘ | ✘ (có nêu ngoài phạm vi) | |
| Ví (số dư tài khoản) | ✔ (DB có cột số dư ví) | ✔ | ~ | ✘ | **Không nêu** ở 1.3 |
| Thông báo, nhật ký đơn | ✔ | ✔ | ✘ | ✘ | **Không nêu** |
| Báo cáo thống kê, dashboard doanh thu | ✔ | ✔ | ✘ | ✘ | **Không nêu** |

## 4. Chỗ MỚI tự mâu thuẫn hoặc chưa khớp

1. **Số dư tài khoản.** 1.4.5 (hoàn tiền) cho phép "cộng vào số dư theo thỏa thuận", nhưng mô hình không có ví hay tài khoản. Cần bỏ câu này hoặc thêm ví vào phạm vi.
2. **Duyệt điều chỉnh.** 1.3 liệt kê người quản lý "duyệt điều chỉnh" và 1.4.6 coi "điều chỉnh" là một loại biến động kho, nhưng cùng mục 1.3 lại loại kiểm kê kho và điều chỉnh khỏi phạm vi. Cần nói rõ điều chỉnh kho là gì (một loại biến động ghi trong sổ kho, không có quy trình kiểm kê và duyệt) hoặc bỏ chữ này.
3. **Danh sách ngoài phạm vi thiếu** các mục: tài khoản và phân quyền nhân viên, sổ địa chỉ, hỗ trợ khách (ticket, chat, FAQ), ví, thông báo, báo cáo thống kê, cảnh báo tồn tối thiểu. Ai đã xem NỘP1 hoặc WEB sẽ hỏi các mục này.
4. **Vai trò.** Báo cáo web có người quản trị và nhân viên hỗ trợ; MỚI không có, trong khi 1.3 nói "người quản lý duyệt hoàn tiền". Cần nói quản lý tương ứng vai trò nào ở web (Admin).
5. **Hiện trạng và đề xuất.** Seri, đặt cọc, hồ sơ đổi trả, phiếu bảo hành, hạn thanh toán 24 giờ, phí xử lý không có trong web hiện trạng (DB). Báo cáo nên ghi đây là nghiệp vụ nhóm đề xuất theo nhận xét của thầy, không phải mô tả lại web đã làm.

## 5. Hai hướng xử lý (Twot chọn)

- **A. Giữ phạm vi hẹp, sửa cho khớp (ít việc):** bổ sung vào danh sách ngoài phạm vi các mục ở điểm 3; sửa điểm 1, 2, 4; thêm một đoạn ngắn ở 1.3 nói rõ MỚI tập trung vào bán hàng, kho, đổi trả, bảo hành và liên hệ với web PowerTech. Không đổi 25 quan hệ, phủ tối thiểu, khóa, dạng chuẩn, đồ thị.
- **B. Mở rộng cho giống web và NỘP1:** thêm tài khoản và vai trò, sổ địa chỉ, giỏ hàng, đánh giá, ticket hỗ trợ, thu cũ, ví. Phải làm lại thực thể, phụ thuộc hàm, phủ tối thiểu, khóa, dạng chuẩn, đồ thị và SQL; báo cáo dài hơn nhiều và khó bảo vệ hơn.
