**Đề tài: NutriCook – Mạng xã hội ẩm thực**

Nguyễn Thành Danh

Võ Trương Bảo Thuận

Phạm Trần Hoàng An

**MÔ TẢ:**

NutriCook – mạng xã hội ẩm thực là ứng dụng web giúp người dùng cá nhân và nhóm quản trị tin học hóa toàn bộ quy trình quản lý thực phẩm gia đình, lập danh sách mua sắm, theo dõi chế độ dinh dưỡng và chia sẻ kiến thức ẩm thực. Hệ thống phục vụ nhiều thành viên làm việc với các vai trò khác nhau như quản trị viên, người kiểm duyệt, người dùng thành viên... Thông tin của một người dùng được phân biệt bằng mã người dùng, tên đăng nhập, họ tên, email, ảnh đại diện, danh sách vai trò, trạng thái khóa tài khoản và thời gian mở khóa. Người dùng thực hiện đăng ký, đăng nhập và xác thực hệ thống thông qua mã JSON web token (JWT). Mã token này được lưu trữ phía người dùng và tự động đính kèm khi gửi các yêu cầu đến hệ thống. Người dùng có thể cập nhật hồ sơ cá nhân, đổi mật khẩu hoặc thực hiện quy trình quên và đặt lại mật khẩu thông qua email.

Nội dung trên hệ thống được chia thành hai loại bài viết chính là công thức nấu ăn và mẹo vặt vào bếp. Mỗi bài viết chỉ thuộc sở hữu của duy nhất một người dùng làm tác giả. Đối với công thức nấu ăn, thông tin quản lý gồm mã công thức, chuỗi định danh, tiêu đề, mô tả, ảnh đại diện, thời gian nấu, độ khó (dễ, trung bình, khó), tổng năng lượng calo, các chỉ số dinh dưỡng (protein, chất béo, tinh bột), số lượt thích, số lượt lưu, ngày tạo và trạng thái kiểm duyệt (chờ duyệt, đã duyệt, đã xóa...). Mỗi công thức gồm nhiều thành phần nguyên liệu (ghi rõ mã nguyên liệu, số lượng, đơn vị đo) và nhiều bước thực hiện (thứ tự bước, nội dung hướng dẫn, ảnh minh họa). Công thức có thể thuộc một hoặc nhiều danh mục thực phẩm. Đối với mẹo vặt vào bếp, thông tin gồm mã mẹo, chuỗi định danh, tiêu đề, nội dung chi tiết, ảnh minh họa, lượt thích, lượt lưu, ngày tạo và trạng thái kiểm duyệt. Các danh mục bài viết và thực phẩm được tổ chức theo cấu trúc cây gồm danh mục cha và các danh mục con, mỗi danh mục có mã, tên, loại và danh mục cha tương ứng. Người dùng có thể xem lại các bài viết do chính mình tạo ra hoặc lưu các bài viết yêu thích vào sổ tay nấu ăn cá nhân.

Mỗi người dùng quản lý một tủ lạnh thông minh cá nhân chứa các nguyên liệu thực phẩm hiện có. Thông tin một mục trong tủ lạnh gồm mã mục, mã nguyên liệu, tên nguyên liệu, số lượng, đơn vị đo lường (gam, kg, ml, quả...) và ngày cập nhật. Dựa trên nguyên liệu hiện có trong tủ, hệ thống tự động so sánh với tất cả công thức trên ứng dụng để tính toán tỷ lệ phù hợp, số nguyên liệu còn thiếu và gợi ý các món ăn tối ưu nhất. Khi chuẩn bị nấu, người dùng kiểm tra nguyên liệu để xem tủ lạnh đã đủ hay còn thiếu nguyên liệu nào. Nếu thiếu, người dùng có thể tự động đẩy các nguyên liệu còn thiếu từ công thức vào danh sách đi chợ. Danh sách đi chợ chứa các mục cần mua gồm mã mục, tên nguyên liệu, số lượng, đơn vị, trạng thái đã mua và bài viết liên quan. Khi người dùng tích chọn đã mua nguyên liệu trên danh sách đi chợ, hệ thống tự động cộng dồn số lượng nguyên liệu đó vào tủ lạnh cá nhân và cho phép dọn dẹp các mục đã mua. Khi người dùng bấm xác nhận nấu một món ăn, hệ thống tự động trừ số lượng thực phẩm tương ứng trong tủ lạnh và lưu bản ghi vào lịch sử nấu ăn. Mỗi bản ghi lịch sử gồm mã lịch sử, mã công thức, tên món, ảnh minh họa, thời điểm nấu và danh sách nguyên liệu đã dùng; người dùng có thể thực hiện đánh giá món ăn từ 1 đến 5 sao và viết ghi chú nhận xét kinh nghiệm nấu.

Để hỗ trợ việc nhập liệu nhanh chóng, hệ thống kết nối với dịch vụ AI phân tích hình ảnh qua chuẩn kết nối API. Người dùng chỉ cần tải lên ảnh chụp hóa đơn mua hàng hoặc ảnh chụp thực phẩm, AI sẽ tự động trích xuất danh sách tên nguyên liệu cùng số lượng tương ứng để đưa thẳng vào tủ lạnh hoặc danh sách đi chợ. Ngoài ra, người dùng có thể sử dụng công cụ tính toán dinh dưỡng bằng cách chọn các nguyên liệu kèm số lượng và đơn vị, hệ thống sẽ tự động quy đổi và tính toán tổng chỉ số Calo, Protein, Chất béo và Tinh bột. Trong quá trình sử dụng, người dùng có thể tương tác xã hội bằng cách thả tim thích bài viết, lưu bài viết, hoặc đăng bình luận trao đổi. Khi phát hiện bài viết hoặc bình luận có nội dung vi phạm, người dùng gửi báo cáo vi phạm ghi rõ lý do. Mọi sự kiện quan trọng như bài viết được duyệt, có bình luận mới hay lượt thích mới đều kích hoạt hệ thống tự động tạo thông báo gửi đến người dùng. Thông báo ghi rõ mã, nội dung, loại thông báo, thời gian tạo và trạng thái đã đọc, cho phép người dùng theo dõi số thông báo chưa đọc trên giao diện và đánh dấu đã đọc một hoặc tất cả.

Quản trị viên thực hiện việc kiểm duyệt các công thức và mẹo vặt mới đăng trước khi cho phép hiển thị công khai. Đồng thời, quản trị viên xử lý các báo cáo vi phạm bình luận hoặc bài viết từ người dùng, với các lựa chọn xóa nội dung vi phạm hoặc khóa tài khoản của người dùng vi phạm. Các bài viết và bình luận bị xóa sẽ được chuyển vào thùng rác dưới dạng xóa mềm; quản trị viên có thể xem lại và khôi phục khi cần thiết. Quản trị viên cũng quản lý cây danh mục thực phẩm và phân quyền người dùng. Hàng tháng, quản trị viên xem bảng thống kê và biểu đồ phân tích tổng số người dùng, tổng số công thức, tổng mẹo vặt, số bài viết chờ duyệt, số bài viết trong thùng rác và dữ liệu tương tác để lên kế hoạch cải thiện chất lượng nội dung và định hướng phát triển hệ thống một cách hiệu quả.

**MÔ TẢ THỰC THỂ**

**1. Thực thể cơ bản**

|  |  |  |  |
| --- | --- | --- | --- |
| **STT** | **Thực thể** | **Thuộc tính chính** | **Lý do xếp vào Cơ bản** |
| 1 | DANH\_MUC | Mã danh mục, Tên danh mục, Loại danh mục, Mã danh mục cha | Danh mục phân loại bài viết/công thức, ít thay đổi |
| 2 | DINH\_DUONG\_NGUYEN\_LIEU | Mã nguyên liệu, Tên nguyên liệu, Calo, Protein, Chất béo, Tinh bột | Từ điển dinh dưỡng chuẩn (tính trên 100g) dùng làm căn cứ tính toán |
| 3 | TRANG\_THAI\_BAO\_CAO | Mã trạng thái, Tên trạng thái (Chờ xử lý, Đã giải quyết, Bỏ qua) | Danh mục trạng thái cố định để xử lý báo cáo vi phạm |

**2. Thực thể đối tượng ngoài**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **STT** | **Thực thể** | **Thuộc tính chính** | **Loại** | **Lý do** |
| 1 | NGUOI\_DUNG | Mã người dùng, Họ và tên, Đường dẫn ảnh đại diện | Con người | Thành viên vận hành và tham gia mạng xã hội |

**3. Thực thể nghiệp vụ**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **STT** | **Thực thể** | **Thuộc tính chính** | **Thuộc tính thời gian** | **Lý do** |
| 1 | BAI\_VIET | Mã bài viết, Tiêu đề, Chuỗi định danh (Slug), Đường dẫn ảnh, Mã người tạo, Trạng thái phê duyệt, Số lượt thích, Số lượt lưu | Ngày tạo, Ngày xóa | Quản lý chung các bài đăng trên nền tảng |
| 2 | CONG\_THUC | Mã công thức (FK -> BAI\_VIET), Mô tả ngắn, Thời gian nấu (phút), Độ khó (Dễ/Trung bình/Khó) | — | Kế thừa từ BAI\_VIET, chứa thông tin riêng của công thức nấu ăn |
| 3 | MEO\_VAT | Mã mẹo vặt (FK -> BAI\_VIET), Nội dung chia sẻ | — | Kế thừa từ BAI\_VIET, chứa nội dung mẹo vặt nhà bếp |
| 4 | BUOC\_THUC\_HIEN | Mã bước, Mã công thức, Thứ tự bước, Nội dung thực hiện, Đường dẫn ảnh minh họa | — | Các bước chi tiết để nấu theo công thức |
| 5 | NGUYEN\_LIEU\_CONG\_THUC | Mã công thức, Mã nguyên liệu, Số lượng, Đơn vị tính | — | Danh sách nguyên liệu cần thiết cho một công thức |
| 6 | DANH\_MUC\_CONG\_THUC | Mã công thức, Mã danh mục | — | Liên kết phân loại nhiều - nhiều giữa công thức và danh mục |
| 7 | TU\_LANH\_NGUOI\_DUNG | Mã tủ lạnh, Mã người dùng, Mã nguyên liệu, Số lượng tồn, Đơn vị tính | Ngày cập nhật | Quản lý nguyên liệu hiện có trong tủ lạnh của người dùng |
| 8 | LICH\_SU\_NAU\_AN | Mã lịch sử, Mã người dùng, Mã công thức, Đánh giá (1-5 sao), Ghi chú | Ngày nấu | Ghi nhận hoạt động thực hành nấu ăn của người dùng |
| 9 | DANH\_SACH\_DI\_CHO | Mã mục đi chợ, Mã người dùng, Mã bài viết, Mã nguyên liệu, Số lượng, Đơn vị tính, Trạng thái đã mua | Ngày tạo | Quản lý danh sách mua sắm nguyên liệu |
| 10 | BINH\_LUAN | Mã bình luận, Nội dung, Mã người dùng, Mã bài viết | Ngày bình luận, Ngày xóa | Tương tác thảo luận trên bài viết |
| 11 | HOAT\_DONG\_NGUOI\_DUNG | Mã hoạt động, Mã người dùng, Mã bài viết, Trạng thái thích, Trạng thái lưu bài | — | Quản lý tương tác Yêu thích / Lưu bài của người dùng |
| 12 | THONG\_BAO | Mã thông báo, Mã người nhận, Nội dung, Loại thông báo, Mã đối tượng tham chiếu, Trạng thái đã đọc | Ngày tạo | Gửi thông báo hệ thống đến người dùng |
| 13 | BAO\_CAO\_BAI\_VIET | Mã báo cáo, Lý do, Mã trạng thái, Mã người báo cáo, Mã bài viết | Ngày tạo | Xử lý vi phạm nội dung bài viết |
| 14 | BAO\_CAO\_BINH\_LUAN | Mã báo cáo, Lý do, Mã trạng thái, Mã người báo cáo, Mã bình luận | Ngày tạo | Xử lý vi phạm nội dung bình luận |

**PHẦN PHỤ THUỘC HÀM:**

|  |  |  |
| --- | --- | --- |
| **STT** | **Tên bảng** | **Phụ thuộc hàm** |
| 1 | DANH\_MUC | MaDanhMuc -> TenDanhMuc, LoaiDanhMuc, MaDanhMucCha |
| 2 | DINH\_DUONG\_NGUYEN\_LIEU | MaNguyenLieu -> TenNguyenLieu, Calo, Protein, ChatBeo, TinhBot |
| 3 | TRANG\_THAI\_BAO\_CAO | MaTrangThai -> TenTrangThai |
| 4 | NGUOI\_DUNG | MaNguoiDung -> HoTen, DuongDanAnhDaiDien, NgayTao |
| 5 | BAI\_VIET | MaBaiViet -> TieuDe, Slug, DuongDanAnh, NgayTao, MaNguoiTao, TrangThaiPheDuyet, SoLuotThich, SoLuotLuu, IsDeleted, NgayXoa |
| 6 | CONG\_THUC | MaCongThuc -> MoTaNgan, ThoiGianNau, DoKho |
| 7 | MEO\_VAT | MaMeoVat -> NoiDungChiaSe |
| 8 | BUOC\_THUC\_HIEN | MaBuoc -> MaCongThuc, ThuTuBuoc, NoiDung, DuongDanAnh |
| 9 | NGUYEN\_LIEU\_CONG\_THUC | MaCongThuc, MaNguyenLieu -> SoLuong, DonViTinh |
| 10 | DANH\_MUC\_CONG\_THUC | MaCongThuc, MaDanhMuc -> (không phụ thuộc thuộc tính khác) |
| 11 | TU\_LANH\_NGUOI\_DUNG | MaTuLanh -> MaNguoiDung, MaNguyenLieu, SoLuongTon, DonViTinh, NgayCapNhat |
| 12 | LICH\_SU\_NAU\_AN | MaLichSu -> MaNguoiDung, MaCongThuc, NgayNau, DanhGia, GhiChu |
| 13 | DANH\_SACH\_DI\_CHO | MaMucDiCho -> MaNguoiDung, MaBaiViet, MaNguyenLieu, SoLuong, DonViTinh, IsChecked, NgayTao |
| 14 | BINH\_LUAN | MaBinhLuan -> NoiDung, NgayBinhLuan, MaNguoiDung, MaBaiViet, IsDeleted, NgayXoa |
| 15 | HOAT\_DONG\_NGUOI\_DUNG | MaHoatDong -> MaNguoiDung, MaBaiViet, IsVoted, IsSaved |
| 16 | THONG\_BAO | MaThongBao -> MaNguoiNhan, NoiDung, LoaiThongBao, MaThamChieu, IsRead, NgayTao |
| 17 | BAO\_CAO\_BAI\_VIET | MaBaoCao -> LyDo, NgayTao, MaTrangThai, MaNguoiBaoCao, MaBaiViet |
| 18 | BAO\_CAO\_BINH\_LUAN | MaBaoCao -> LyDo, NgayTao, MaTrangThai, MaNguoiBaoCao, MaBinhLuan |

**XÁC ĐỊNH PTH VÀ TÌM PHỦ TỐI TIỂU:**

**1. Bảng DANH\_MUC**

Tập PTH ban đầu:

$F\_{1}=\left\{MaDanhMuc\rightarrow TenDanhMuc, LoaiDanhMuc, MaDanhMucCha\right\}$

Fmin**:**

* 1. $MaDanhMuc\rightarrow TenDanhMuc$
  2. $MaDanhMuc\rightarrow LoaiDanhMuc$
  3. $MaDanhMuc\rightarrow MaDanhMucCha$

Khóa chính: MaDanhMuc

Dạng chuẩn cao nhất: BCNF

**2. Bảng DINH\_DUONG\_NGUYEN\_LIEU**

Tập PTH ban đầu:

$$F\_{2}=\left\{MaNguyenLieu\rightarrow TenNguyenLieu, Calo, Protein, ChatBeo, TinhBot\right\}$$

Fmin**:**

* 1. $MaNguyenLieu\rightarrow TenNguyenLieu$
  2. $MaNguyenLieu\rightarrow Calo$
  3. $MaNguyenLieu\rightarrow Protein$
  4. $MaNguyenLieu\rightarrow ChatBeo$
  5. $MaNguyenLieu\rightarrow TinhBot$

Khóa chính: MaNguyenLieu

Dạng chuẩn cao nhất: BCNF

**3. Bảng TRANG\_THAI\_BAO\_CAO**

Tập PTH ban đầu:

$$F\_{3}=\left\{MaTrangThai\rightarrow TenTrangThai\right\}$$

Fmin**:** Đã tối tiểu sẵn:

* 1. $MaTrangThai\rightarrow TenTrangThai$

Khóa chính: MaTrangThai

Dạng chuẩn cao nhất: BCNF.

**4. Bảng NGUOI\_DUNG**

Tập PTH ban đầu:

$$F\_{4}=\left\{MaNguoiDung\rightarrow HoTen, DuongDanAnhDaiDien, NgayTao\right\}$$

Fmin**:**

* 1. $MaNguoiDung\rightarrow HoTen$
  2. $MaNguoiDung\rightarrow DuongDanAnhDaiDien$
  3. $MaNguoiDung\rightarrow NgayTao$

Khóa chính: MaNguoiDung

Dạng chuẩn cao nhất: BCNF.

**5. Bảng BAI\_VIET**

Tập PTH ban đầu:

F5  = { MaBaiViet 🡪 TieuDe, Slug, DuongDanAnh, NgayTao, MaNguoiTao, TrangThaiPheDuyet, SoLuotThich, SoLuotLuu, IsDeleted, NgayXoa}

Fmin**:**

* 1. $MaBaiViet\rightarrow TieuDe$
  2. $MaBaiViet\rightarrow Slug$
  3. $MaBaiViet\rightarrow DuongDanAnh$
  4. $MaBaiViet\rightarrow NgayTao$
  5. $MaBaiViet\rightarrow MaNguoiTao$
  6. $MaBaiViet\rightarrow TrangThaiPheDuyet$
  7. $MaBaiViet\rightarrow SoLuotThich$
  8. $MaBaiViet\rightarrow SoLuotLuu$
  9. $MaBaiViet\rightarrow IsDeleted$
  10. $MaBaiViet\rightarrow NgayXoa$

Khóa chính: MaBaiViet

Dạng chuẩn cao nhất: BCNF.

**6. Bảng CONG\_THUC**

Tập PTH ban đầu:

$$F\_{6}=\left\{MaCongThuc\rightarrow MoTaNgan, ThoiGianNau, DoKho\right\}$$

Fmin**:**

* 1. $MaCongThuc\rightarrow MoTaNgan$
  2. $MaCongThuc\rightarrow ThoiGianNau$
  3. $MaCongThuc\rightarrow DoKho$

Khóa chính: MaCongThuc

Dạng chuẩn cao nhất: BCNF.

**7. Bảng MEO\_VAT**

Tập PTH ban đầu:

$$F\_{7}=\left\{MaMeoVat\rightarrow NoiDungChiaSe\right\}$$

Fmin**:** Đã tối tiểu sẵn:

* 1. $MaMeoVat\rightarrow NoiDungChiaSe$

Khóa chính: MaMeoVat

Dạng chuẩn cao nhất: BCNF.

**8. Bảng BUOC\_THUC\_HIEN**

Tập PTH ban đầu:

$$F\_{8}=\left\{MaBuoc\rightarrow MaCongThuc, ThuTuBuoc, NoiDung, DuongDanAnh\right\}$$

Fmin:

* 1. $MaBuoc\rightarrow MaCongThuc$
  2. $MaBuoc\rightarrow ThuTuBuoc$
  3. $MaBuoc\rightarrow NoiDung$
  4. $MaBuoc\rightarrow DuongDanAnh$

Khóa chính: MaBuoc

Dạng chuẩn cao nhất: BCNF.

**9. Bảng NGUYEN\_LIEU\_CONG\_THUC**

Tập PTH ban đầu:

$$F\_{9}=\left\{MaCongThuc, MaNguyenLieu\rightarrow SoLuong, DonViTinh\right\}$$

Fmin:

* 1. $MaCongThuc, MaNguyenLieu\rightarrow SoLuong$
  2. $MaCongThuc, MaNguyenLieu\rightarrow DonViTinh$

**10. Bảng DANH\_MUC\_CONG\_THUC**

Tập PTH ban đầu: Bảng chỉ đóng vai trò bảng liên kết (nhiều - nhiều) giữa MaCongThuc và MaDanhMuc.

Khóa chính: MaCongThuc, MaDanhMuc

Dạng chuẩn cao nhất: BCNF

**11. Bảng TU\_LANH\_NGUOI\_DUNG**

Tập PTH ban đầu:

F11={MaTuLanh → MaNguoiDung, MaNguyenLieu, SoLuongTon, DonViTinh, NgayCapNhat}

Fmin:

* 1. $MaTuLanh\rightarrow MaNguoiDung$
  2. $MaTuLanh\rightarrow MaNguyenLieu$
  3. $MaTuLanh\rightarrow SoLuongTon$
  4. $MaTuLanh\rightarrow DonViTinh$
  5. $MaTuLanh\rightarrow NgayCapNhat$

Khóa chính: MaTuLanh

Dạng chuẩn cao nhất: BCNF.

**12. Bảng LICH\_SU\_NAU\_AN**

Tập PTH ban đầu:

F12={MaLichSu →MaNguoiDung, MaCongThuc, NgayNau, DanhGia, GhiChu}

Fmin:

* 1. $MaLichSu\rightarrow MaNguoiDung$
  2. $MaLichSu\rightarrow MaCongThuc$
  3. $MaLichSu\rightarrow NgayNau$
  4. $MaLichSu\rightarrow DanhGia$
  5. $MaLichSu\rightarrow GhiChu$

Khóa chính: MaLichSu

Dạng chuẩn cao nhất: BCNF.

**13. Bảng DANH\_SACH\_DI\_CHO**

Tập PTH ban đầu:

F13={MaMucDiCho →MaNguoiDung, MaBaiViet, MaNguyenLieu, SoLuong, DonViTinh, IsChecked, NgayTao" }

Fmin:

* 1. $MaMucDiCho\rightarrow MaNguoiDung$
  2. $MaMucDiCho\rightarrow MaBaiViet$
  3. $MaMucDiCho\rightarrow MaNguyenLieu$
  4. $MaMucDiCho\rightarrow SoLuong$
  5. $MaMucDiCho\rightarrow DonViTinh$
  6. $MaMucDiCho\rightarrow IsChecked$
  7. $MaMucDiCho\rightarrow NgayTao$

Khóa chính: MaMucDiCho

Dạng chuẩn cao nhất: BCNF.

**14. Bảng BINH\_LUAN**

Tập PTH ban đầu:

F14={MaBinhLuan → NoiDung, NgayBinhLuan, MaNguoiDung, MaBaiViet, IsDeleted, NgayXoa}

Fmin:

* 1. $MaBinhLuan\rightarrow NoiDung$
  2. $MaBinhLuan\rightarrow NgayBinhLuan$
  3. $MaBinhLuan\rightarrow MaNguoiDung$
  4. $MaBinhLuan\rightarrow MaBaiViet$
  5. $MaBinhLuan\rightarrow IsDeleted$
  6. $MaBinhLuan\rightarrow NgayXoa$

Khóa chính: MaBinhLuan

Dạng chuẩn cao nhất: BCNF.

**15. Bảng HOAT\_DONG\_NGUOI\_DUNG**

Tập PTH ban đầu:

$$F\_{15}=\left\{MaHoatDong\rightarrow MaNguoiDung, MaBaiViet, IsVoted, IsSaved\right\}$$

Fmin:

* 1. $MaHoatDong\rightarrow MaNguoiDung$
  2. $MaHoatDong\rightarrow MaBaiViet$
  3. $MaHoatDong\rightarrow IsVoted$
  4. $MaHoatDong\rightarrow IsSaved$

Khóa chính: MaHoatDong

Dạng chuẩn cao nhất: BCNF.

**16. Bảng THONG\_BAO**

Tập PTH ban đầu:

F16={MaThongBao → MaNguoiNhan, NoiDung, LoaiThongBao, MaThamChieu, IsRead, NgayTao}

Fmin:

* 1. $MaThongBao\rightarrow MaNguoiNhan$
  2. $MaThongBao\rightarrow NoiDung$
  3. $MaThongBao\rightarrow LoaiThongBao$
  4. $MaThongBao\rightarrow MaThamChieu$
  5. $MaThongBao\rightarrow IsRead$
  6. $MaThongBao\rightarrow NgayTao$

Khóa chính: MaThongBao

Dạng chuẩn cao nhất: BCNF.

**17. Bảng BAO\_CAO\_BAI\_VIET**

Tập PTH ban đầu:

F17={MaBaoCao → LyDo, NgayTao, MaTrangThai, MaNguoiBaoCao, MaBaiViet}

Fmin:

* 1. $MaBaoCao\rightarrow LyDo$
  2. $MaBaoCao\rightarrow NgayTao$
  3. $MaBaoCao\rightarrow MaTrangThai$
  4. $MaBaoCao\rightarrow MaNguoiBaoCao$
  5. $MaBaoCao\rightarrow MaBaiViet$

Khóa chính: MaBaoCao

Dạng chuẩn cao nhất: BCNF.

**18. Bảng BAO\_CAO\_BINH\_LUAN**

Tập PTH ban đầu:

F18={MaBaoCao →LyDo, NgayTao, MaTrangThai, MaNguoiBaoCao, MaBinhLuan}

Fmin:

* 1. $MaBaoCao\rightarrow LyDo$
  2. $MaBaoCao\rightarrow NgayTao$
  3. $MaBaoCao\rightarrow MaTrangThai$
  4. $MaBaoCao\rightarrow MaNguoiBaoCao$
  5. $MaBaoCao\rightarrow MaBinhLuan$

Khóa chính: MaBaoCao

Dạng chuẩn cao nhất: BCNF.