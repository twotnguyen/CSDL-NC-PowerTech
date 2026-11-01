**Đề tài: Ứng dụng kỹ thuật quản lý giao dịch (Transaction) và cơ chế khóa (Locking) trong xây dựng hệ thống đặt vé trực tuyến.**

**HỆ THỐNG ĐẶT VÉ TRỰC TUYẾN**

Công ty cổ phần dịch vụ vé trực tuyến (gọi tắt là Công ty) vận hành một nền tảng bán vé cho các nhà tổ chức sự kiện như hòa nhạc, phim, kịch, thể thao... tại nhiều địa điểm khác nhau. Mỗi đợt mở bán, hàng chục nghìn khách hàng truy cập cùng lúc để chọn chỗ, trong khi mỗi ghế của một suất diễn chỉ được bán cho duy nhất một người. Nếu việc xử lý đồng thời không được kiểm soát, hệ thống dễ xảy ra tình trạng bán trùng ghế, bán vượt số lượng vé phát hành, ghế bị giữ mãi mà không thanh toán, hoặc khách đã bị trừ tiền nhưng không nhận được vé. Vì vậy, cần xây dựng hệ thống đặt vé trực tuyến có áp dụng kỹ thuật quản lý giao dịch (Transaction) và cơ chế khóa (Locking) để bảo đảm tính nhất quán của dữ liệu, với các yêu cầu quản lý thông tin sự kiện, suất diễn, chỗ ngồi, giữ chỗ, đặt vé, thanh toán, hoàn vé và soát vé như sau:

Nhà tổ chức là đơn vị sở hữu sự kiện và thuê nền tảng để bán vé. Thông tin của nhà tổ chức được phân biệt bằng mã nhà tổ chức, tên nhà tổ chức, địa chỉ, số điện thoại, email, mã số thuế... Một nhà tổ chức có thể tổ chức nhiều sự kiện. Thông tin của một sự kiện được phân biệt bằng mã sự kiện, tên sự kiện, mô tả, ngày mở bán, ngày đóng bán... và thuộc một loại sự kiện duy nhất (hòa nhạc, phim, kịch, thể thao...). Một loại sự kiện bao gồm nhiều sự kiện, một sự kiện chỉ thuộc một nhà tổ chức.

Sự kiện được tổ chức tại các địa điểm (nhà hát, rạp chiếu, sân vận động...). Thông tin của một địa điểm gồm mã địa điểm, tên địa điểm, địa chỉ, sức chứa... Mỗi địa điểm được chia thành nhiều khu vực (khán đài A, tầng 1, khu đứng...), mỗi khu vực có nhiều ghế. Ghế được phân biệt bằng mã ghế, hàng, số ghế và thuộc một khu vực duy nhất. Hạng vé (VIP, thường, đứng...) được lưu với mã hạng, tên hạng và mô tả quyền lợi.

Một sự kiện có thể diễn ra nhiều suất, mỗi suất diễn tại một địa điểm với thời điểm bắt đầu, thời điểm kết thúc và trạng thái (chưa mở bán, đang bán, hết vé, đã diễn, đã hủy). Với mỗi suất, nhà tổ chức quy định bảng giá theo hạng vé gồm giá vé, số lượng phát hành và số lượng còn lại. Đối với hạng vé có chỉ định chỗ, hệ thống quản lý trạng thái của từng ghế trong từng suất diễn (trống, đang giữ, đã bán, bị khóa) kèm số phiên bản và thời điểm cập nhật. Tại một thời điểm, một ghế trong một suất diễn chỉ ở một trạng thái duy nhất và chỉ được bán cho một khách hàng. Đối với hạng vé không chỉ định chỗ (khu đứng, vé tự do), hệ thống quản lý bằng số lượng còn lại của hạng vé trong suất đó.

Khách hàng đăng ký tài khoản để mua vé, thông tin gồm mã khách hàng, họ tên, ngày sinh, số điện thoại, email... Nhân viên của Công ty gồm nhân viên vận hành, nhân viên chăm sóc khách hàng, nhân viên soát vé; thông tin của nhân viên phân biệt bằng mã nhân viên, họ tên, chức vụ, số điện thoại, email... Chỉ nhân viên có thẩm quyền mới được khóa ghế, hủy suất diễn và duyệt yêu cầu hoàn vé.

Khi khách hàng chọn ghế hoặc số lượng vé của một hạng, hệ thống tạo một phiên giữ chỗ ghi rõ khách hàng, suất diễn, thời điểm giữ và thời điểm hết hạn giữ (ví dụ 10 phút); mỗi lần giữ tối đa 6 vé. Các ghế hoặc số lượng theo hạng được ghi nhận qua chi tiết giữ chỗ. Việc giữ chỗ phải thực hiện trong một giao dịch: kiểm tra ghế còn trống, khóa ghế, chuyển sang trạng thái đang giữ; nếu có bất kỳ ghế nào không còn trống thì toàn bộ giao dịch bị hoàn tác (rollback) và khách được thông báo để chọn lại. Tại một thời điểm, một ghế chỉ thuộc một phiên giữ chỗ còn hiệu lực. Khi quá hạn mà chưa thanh toán, hệ thống tự động giải phóng các ghế đã giữ.

Từ phiên giữ chỗ còn hiệu lực, khách hàng xác nhận đặt vé; hệ thống lập đơn đặt vé gồm mã đơn, ngày đặt, tổng tiền, trạng thái (chờ thanh toán, đã thanh toán, đã hủy, hết hạn). Mỗi đơn có thể áp dụng tối đa một mã giảm giá; thông tin mã giảm giá gồm mã giảm giá, tên chương trình, giá trị giảm, số lượng phát hành, số lượng đã dùng, ngày bắt đầu, ngày hết hạn. Số lần sử dụng không được vượt số lượng phát hành và mỗi khách hàng chỉ dùng một mã một lần. Khách hàng thanh toán thông qua đối tác thanh toán (ngân hàng, ví điện tử, cổng thẻ); mỗi lần thanh toán tạo một giao dịch thanh toán gồm mã giao dịch, mã tham chiếu của đối tác, số tiền, thời điểm thanh toán và trạng thái. Một đơn có thể có nhiều lần thanh toán khi các lần trước thất bại nhưng chỉ có tối đa một giao dịch thành công. Thông báo kết quả (callback) từ đối tác có thể được gửi lặp lại nhiều lần; hệ thống phải bảo đảm một kết quả chỉ được ghi nhận một lần.

Khi thanh toán thành công, hệ thống thực hiện trong một giao dịch duy nhất các bước: chuyển ghế sang trạng thái đã bán, trừ số lượng còn lại của hạng vé không chỉ định chỗ, tăng số lượng đã dùng của mã giảm giá, phát hành vé và cập nhật trạng thái đơn; các bước này hoặc cùng thành công hoặc cùng bị hoàn tác (all-or-nothing). Nếu thanh toán thất bại hoặc phiên giữ chỗ hết hạn, giao dịch bị hoàn tác, ghế được trả về trạng thái trống và mã giảm giá được hoàn lại. Mỗi vé được phân biệt bằng mã vé (mã QR) và ghi rõ đơn đặt vé, suất diễn, ghế (nếu có chỉ định chỗ), hạng vé, giá bán, ngày phát hành, trạng thái (hợp lệ, đã sử dụng, đã hoàn, đã hủy). Một ghế trong một suất diễn tại một thời điểm chỉ có tối đa một vé hợp lệ.

Tại cổng vào, nhân viên soát vé quét mã vé; mỗi vé chỉ được xác nhận sử dụng một lần dù có nhiều cổng quét cùng lúc. Trước thời điểm bắt đầu suất diễn theo thời hạn quy định, khách hàng có thể gửi yêu cầu hoàn vé ghi rõ lý do và ngày yêu cầu; nhân viên có thẩm quyền xem xét, duyệt và lưu số tiền hoàn, ngày xử lý, trạng thái. Khi yêu cầu hoàn vé được duyệt, vé chuyển sang trạng thái đã hoàn, ghế trở về trạng thái trống (hoặc số lượng còn lại được cộng lại) và hệ thống hoàn tiền cho khách hàng. Vé đã sử dụng không được hoàn; khi hoàn vé và soát vé xảy ra đồng thời trên cùng một vé thì chỉ một thao tác được thành công.

Nhân viên có thẩm quyền có thể khóa một số ghế (dành cho ban tổ chức, ghế hư hỏng) hoặc hủy một suất diễn. Các thao tác này diễn ra đồng thời với việc khách hàng đang đặt vé nhưng không được làm sai lệch dữ liệu; khi hủy suất diễn, toàn bộ vé của suất đó phải được chuyển sang đã hủy và hoàn tiền cho khách hàng.

Để theo dõi và điều chỉnh hiệu năng xử lý đồng thời, mọi giao dịch quan trọng (giữ chỗ, thanh toán, hoàn vé, hủy suất, giải phóng ghế) được ghi vào nhật ký giao dịch gồm mã nhật ký, loại thao tác, đối tượng bị khóa, loại khóa, mức cô lập, kết quả (hoàn tất, hoàn tác, hết thời gian chờ khóa, bế tắc), thời điểm bắt đầu và thời điểm kết thúc.

Hàng tháng và sau mỗi suất diễn, ban quản trị xem báo cáo thống kê về số vé bán ra, doanh thu, tỷ lệ lấp đầy, tỷ lệ phiên giữ chỗ hết hạn, số lần xung đột, hoàn tác, bế tắc và thời gian chờ khóa trung bình theo từng sự kiện, địa điểm, để lập kế hoạch mở bán, điều chỉnh thời gian giữ chỗ và tối ưu cơ chế khóa của hệ thống.

**MÔ TẢ THỰC THỂ**

**1. Thực thể CƠ BẢN**

| **STT** | **Thực thể** | **Thuộc tính chính** | **Lý do xếp vào Cơ bản** |
| --- | --- | --- | --- |
| 1 | LOẠI\_SỰ\_KIỆN | Mã loại sự kiện, tên loại sự kiện | Danh mục phân loại, số lượng cố định |
| 2 | ĐỊA\_ĐIỂM | Mã địa điểm, tên địa điểm, địa chỉ, sức chứa | Cơ sở vật chất có trước hệ thống, ít thay đổi |
| 3 | KHU\_VỰC | Mã khu vực, địa điểm, tên khu vực | Cách chia khu cố định của từng địa điểm |
| 4 | GHẾ | Mã ghế, khu vực, hàng, số ghế | Tài sản vật lý của địa điểm, không phụ thuộc suất diễn; trạng thái bán theo từng suất lưu ở GHẾ\_SUẤT\_DIỄN |
| 5 | HẠNG\_VÉ | Mã hạng, tên hạng, mô tả | Danh mục phân loại, ổn định |

**2. Thực thể ĐỐI TƯỢNG NGOÀI**

| **STT** | **Thực thể** | **Thuộc tính chính** | **Loại** | **Lý do** |
| --- | --- | --- | --- | --- |
| 1 | KHÁCH\_HÀNG | Mã khách hàng, họ tên, ngày sinh, số điện thoại, email | Con người | Người mua vé, đăng ký tài khoản trên hệ thống |
| 2 | NHÀ\_TỔ\_CHỨC | Mã nhà tổ chức, tên, địa chỉ, số điện thoại, email, mã số thuế | Tổ chức | Đơn vị sở hữu sự kiện, thuê nền tảng để bán vé |
| 3 | NHÂN\_VIÊN | Mã nhân viên, họ tên, chức vụ, số điện thoại, email | Con người | Vận hành, chăm sóc khách hàng, soát vé; có thẩm quyền khóa ghế, hủy suất, duyệt hoàn vé |
| 4 | ĐỐI\_TÁC\_THANH\_TOÁN | Mã đối tác, tên đối tác, loại đối tác, phí giao dịch | Tổ chức | Ngân hàng, ví điện tử, cổng thẻ bên ngoài xử lý tiền |

**3. Thực thể NGHIỆP VỤ**

| **STT** | **Thực thể** | **Thuộc tính chính** | **Thuộc tính thời gian** | **Lý do** |
| --- | --- | --- | --- | --- |
| 1 | SỰ\_KIỆN | Mã sự kiện, tên, mô tả, loại sự kiện, nhà tổ chức | Ngày mở bán, ngày đóng bán | Do nhà tổ chức tạo, có thời hạn bán vé |
| 2 | SUẤT\_DIỄN | Mã suất, sự kiện, địa điểm, trạng thái | Thời điểm bắt đầu, thời điểm kết thúc | Mỗi sự kiện diễn ra nhiều suất |
| 3 | BẢNG\_GIÁ\_SUẤT | Suất diễn, hạng vé, giá vé, số lượng phát hành, số lượng còn lại | (theo suất diễn) | Giá và số lượng theo hạng; số lượng còn lại là dữ liệu bị tranh chấp khi nhiều người mua cùng lúc |
| 4 | GHẾ\_SUẤT\_DIỄN | Suất diễn, ghế, hạng vé, trạng thái, phiên bản | Thời điểm cập nhật | Tài nguyên tranh chấp chính; mỗi ghế mỗi suất một mẫu tin, được khóa khi giữ chỗ |
| 5 | GIỮ\_CHỖ | Mã giữ chỗ, khách hàng, suất diễn, trạng thái | Thời điểm giữ, thời điểm hết hạn | Phát sinh mỗi lần khách chọn chỗ, có thời hạn hiệu lực |
| 6 | CHI\_TIẾT\_GIỮ\_CHỖ | Mã chi tiết, giữ chỗ, hạng vé, ghế, số lượng | (theo giữ chỗ) | Thực thể kết hợp giữa Giữ chỗ với Ghế / Hạng vé; ghế để trống nếu hạng không chỉ định chỗ |
| 7 | MÃ\_GIẢM\_GIÁ | Mã giảm giá, tên chương trình, giá trị giảm, số lượng phát hành, số lượng đã dùng | Ngày bắt đầu, ngày hết hạn | Có số lượng giới hạn và thời hạn; số lượng đã dùng bị tranh chấp |
| 8 | ĐƠN\_ĐẶT\_VÉ | Mã đơn, khách hàng, giữ chỗ, mã giảm giá, tổng tiền, trạng thái | Ngày đặt | Phát sinh khi khách xác nhận đặt vé |
| 9 | VÉ | Mã vé, đơn đặt vé, suất diễn, ghế, hạng vé, giá bán, trạng thái, nhân viên soát vé | Ngày phát hành, thời điểm soát vé | Chỉ được phát hành sau khi thanh toán thành công |
| 10 | GIAO\_DỊCH\_THANH\_TOÁN | Mã giao dịch, đơn đặt vé, đối tác, mã tham chiếu, số tiền, trạng thái | Thời điểm thanh toán | Mỗi lần thanh toán là một mẫu tin; mã tham chiếu duy nhất để chống ghi nhận lặp |
| 11 | YÊU\_CẦU\_HOÀN\_VÉ | Mã yêu cầu, vé, nhân viên xử lý, lý do, số tiền hoàn, trạng thái | Ngày yêu cầu, ngày xử lý | Phát sinh khi khách muốn trả vé |
| 12 | NHẬT\_KÝ\_GIAO\_DỊCH | Mã nhật ký, loại thao tác, đối tượng bị khóa, loại khóa, mức cô lập, kết quả | Thời điểm bắt đầu, thời điểm kết thúc | Ghi lại mỗi giao dịch quan trọng để phân tích xung đột, bế tắc |

**PHẦN PHỤ THUỘC HÀM**

**Nhóm thực thể cơ bản**

| **STT** | **Tên bảng** | **Phụ thuộc hàm** |
| --- | --- | --- |
| 1 | LOAI\_SU\_KIEN | MaLoaiSK → TenLoaiSK |
| 2 | DIA\_DIEM | MaDiaDiem → TenDiaDiem, DiaChi, SucChua |
| 3 | KHU\_VUC | MaKhuVuc → MaDiaDiem, TenKhuVuc |
| 4 | GHE | MaGhe → MaKhuVuc, Hang, SoGhe |
| 5 | HANG\_VE | MaHang → TenHang, MoTa |

**Nhóm thực thể đối tượng ngoài**

| **STT** | **Tên bảng** | **Phụ thuộc hàm** |
| --- | --- | --- |
| 1 | KHACH\_HANG | MaKH → HoTen, NgaySinh, SoDienThoai, Email |
| 2 | NHA\_TO\_CHUC | MaNTC → TenNTC, DiaChi, SoDienThoai, Email, MaSoThue |
| 3 | NHAN\_VIEN | MaNV → HoTen, ChucVu, SoDienThoai, Email |
| 4 | DOI\_TAC\_THANH\_TOAN | MaDoiTac → TenDoiTac, LoaiDoiTac, PhiGiaoDich |

**Nhóm thực thể nghiệp vụ**

| **STT** | **Tên bảng** | **Phụ thuộc hàm** |
| --- | --- | --- |
| 1 | SU\_KIEN | MaSK → TenSK, MoTa, MaLoaiSK, MaNTC, NgayMoBan, NgayDongBan |
| 2 | SUAT\_DIEN | MaSuat → MaSK, MaDiaDiem, TrangThai, ThoiDiemBatDau, ThoiDiemKetThuc |
| 3 | BANG\_GIA\_SUAT | MaSuat, MaHang → GiaVe, SoLuongPhatHanh, SoLuongCon |
| 4 | GHE\_SUAT\_DIEN | MaSuat, MaGhe → MaHang, TrangThai, PhienBan, ThoiDiemCapNhat |
| 5 | GIU\_CHO | MaGiuCho → MaKH, MaSuat, TrangThai, ThoiDiemGiu, ThoiDiemHetHan |
| 6 | CHI\_TIET\_GIU\_CHO | MaCTGiuCho → MaGiuCho, MaHang, MaGhe, SoLuong |
| 7 | MA\_GIAM\_GIA | MaGiamGia → TenChuongTrinh, GiaTriGiam, SoLuongPhatHanh, SoLuongDaDung, NgayBatDau, NgayHetHan |
| 8 | DON\_DAT\_VE | MaDon → MaKH, MaGiuCho, MaGiamGia, TongTien, TrangThai, NgayDat |
| 9 | VE | MaVe → MaDon, MaSuat, MaGhe, MaHang, GiaBan, TrangThai, NgayPhatHanh, ThoiDiemSoatVe, MaNVSoat |
| 10 | GIAO\_DICH\_THANH\_TOAN | MaGiaoDich → MaDon, MaDoiTac, MaThamChieu, SoTien, TrangThai, ThoiDiemThanhToan |
| 11 | YEU\_CAU\_HOAN\_VE | MaYeuCau → MaVe, MaNV, LyDo, SoTienHoan, TrangThai, NgayYeuCau, NgayXuLy |
| 12 | NHAT\_KY\_GIAO\_DICH | MaNhatKy → LoaiThaoTac, DoiTuongKhoa, LoaiKhoa, MucCoLap, KetQua, ThoiDiemBatDau, ThoiDiemKetThuc |

**TÌNH HUỐNG GIAO DỊCH VÀ CƠ CHẾ KHÓA CẦN GIẢI QUYẾT**

Từ các yêu cầu nghiệp vụ trên, hệ thống phải xử lý các tình huống truy cập đồng thời sau; đây là cơ sở để thiết kế giao dịch và lựa chọn kỹ thuật khóa, mức cô lập ở các bước tiếp theo.

| **STT** | **Tình huống đồng thời** | **Giao dịch liên quan** | **Vấn đề có thể xảy ra** | **Kỹ thuật xử lý (Transaction / Locking)** |
| --- | --- | --- | --- | --- |
| 1 | Hai khách cùng chọn một ghế của một suất | Giữ chỗ | Bán trùng ghế (double booking); mất dữ liệu cập nhật (lost update) | Khóa ghi (exclusive lock) mức dòng trên GHE\_SUAT\_DIEN bằng SELECT … FOR UPDATE (NOWAIT hoặc SKIP LOCKED); hoặc khóa lạc quan bằng cột PhienBan; kiểm tra trạng thái ghế và cập nhật trong cùng một giao dịch. |
| 2 | Nhiều khách mua cùng hạng vé không chỉ định chỗ | Giữ chỗ, Đặt vé | Bán vượt số lượng phát hành (overselling) do cập nhật SoLuongCon bị ghi đè | Cập nhật có điều kiện nguyên tử: UPDATE … SET SoLuongCon = SoLuongCon − n WHERE SoLuongCon ≥ n; hoặc khóa dòng BANG\_GIA\_SUAT trước khi trừ. |
| 3 | Nhiều khách dùng cùng một mã giảm giá | Đặt vé | Vượt SoLuongPhatHanh; một khách dùng nhiều lần | Khóa dòng MA\_GIAM\_GIA, cập nhật SoLuongDaDung có điều kiện; ràng buộc duy nhất theo (khách hàng, mã giảm giá). |
| 4 | Khách giữ nhiều ghế, hai giao dịch khóa ghế theo thứ tự ngược nhau | Giữ chỗ nhiều ghế | Bế tắc (deadlock) | Khóa theo thứ tự cố định (sắp xếp theo MaGhe); đặt thời gian chờ khóa (lock timeout); phát hiện bế tắc và tự động thử lại giao dịch bị chọn làm nạn nhân. |
| 5 | Thanh toán thành công đúng lúc phiên giữ chỗ hết hạn | Thanh toán, Giải phóng ghế | Ghế vừa bán vừa được trả về trống; khách trả tiền nhưng không có vé | Khóa dòng GIU\_CHO; kiểm tra lại trạng thái và hạn giữ trong giao dịch để chỉ một bên thành công; nếu đã thu tiền mà giữ chỗ hết hạn thì hoàn tiền tự động. |
| 6 | Đối tác thanh toán gửi callback nhiều lần | Ghi nhận thanh toán | Phát hành vé trùng; ghi nhận tiền hai lần | Xử lý idempotent: ràng buộc duy nhất trên MaThamChieu; kiểm tra trạng thái đơn trong giao dịch trước khi phát hành vé. |
| 7 | Hoàn vé và soát vé cùng lúc trên một vé | Hoàn vé, Soát vé | Vé vừa hoàn vừa được sử dụng | Khóa ghi dòng VE; kiểm tra TrangThai rồi mới cập nhật trong cùng một giao dịch. |
| 8 | Lập báo cáo trong khi đang bán vé | Thống kê, báo cáo | Đọc không lặp lại (non-repeatable read); bản ghi ma (phantom) | Giao dịch chỉ đọc ở mức cô lập Snapshot / Repeatable Read (MVCC), không chặn các giao dịch ghi. |
| 9 | Hủy suất diễn hoặc khóa hàng loạt ghế khi khách đang đặt vé | Hủy suất, Khóa ghế | Xung đột giữa thao tác hàng loạt và nhiều thao tác nhỏ | Khóa phân cấp (multi-granularity): khóa ý định (IS/IX) ở mức suất, khóa độc quyền (X) trên SUAT\_DIEN cho thao tác hàng loạt; xử lý theo từng lô nhỏ. |