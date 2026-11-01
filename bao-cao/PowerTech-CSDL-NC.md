**Hệ thống quản lý cửa hàng thiết bị công nghệ PowerTech**

> **Ghi chú (18/10/2026).** Mô tả chính của đề tài là [01_Mo_ta_de_tai_v2.md](01_Mo_ta_de_tai_v2.md). Đoạn "Mô tả" dưới đây là bản đã nộp lần đầu, giữ nguyên để đối chiếu; phần "Mô tả thực thể" đã cập nhật theo v2. Bản nộp đầu nguyên văn: `PowerTech-CSDL-NC_ban_nop.md`.

# Mô tả

Một cửa hàng kinh doanh linh kiện máy tính, máy tính nguyên bộ và thiết bị công nghệ cần tin học hóa việc quản lý hàng hóa, nhập hàng, bán hàng và phục vụ khách hàng. Khách có thể mua trực tiếp tại cửa hàng hoặc đặt hàng trực tuyến. Đề tài xét một cửa hàng, quản lý số lượng theo sản phẩm, chưa xét nhiều chi nhánh, lắp ráp máy và kế toán tài chính đầy đủ.

Cửa hàng có các nhân viên bán hàng, quản lý kho, hỗ trợ, giao hàng và quản trị. Mỗi nhân viên được phân biệt bằng mã nhân viên, có họ tên, thông tin liên hệ và tình trạng làm việc. Nhân viên thao tác trên hệ thống có tài khoản riêng; mỗi tài khoản có mã và tên đăng nhập duy nhất, có thể được giao nhiều vai trò. Người quản trị tạo tài khoản và phân quyền; nhân viên bán hàng xác nhận đơn, nhân viên kho kiểm nhận và bàn giao hàng, nhân viên giao hàng thực hiện giao, nhân viên hỗ trợ tiếp nhận phản ánh. Người quản lý duyệt điều chỉnh kho và hoàn tiền.

Khách hàng được quản lý bằng mã khách hàng, họ tên, số điện thoại và email nếu có. Một khách hàng có thể chưa có tài khoản hoặc liên kết với một tài khoản; một tài khoản liên kết tối đa một khách hàng. Khách có tài khoản có thể lưu nhiều địa chỉ giao hàng, mỗi địa chỉ có mã riêng, tên người nhận, số điện thoại và địa chỉ chi tiết; tại một thời điểm chỉ có tối đa một địa chỉ mặc định. Khách vãng lai mua tại quầy không bắt buộc có hồ sơ hoặc tài khoản. Họ tên, điện thoại, email, tên thương hiệu và tên nhà cung cấp không được dùng riêng để phân biệt các đối tượng vì có thể trùng.

Cửa hàng kinh doanh nhiều sản phẩm thuộc các loại như bộ xử lý, bộ nhớ, bo mạch chủ, thiết bị lưu trữ, màn hình và thiết bị ngoại vi. Mỗi sản phẩm có mã nội bộ và mã SKU duy nhất, tên, mô tả, giá niêm yết, giá ưu đãi nếu có, thời hạn bảo hành và tình trạng kinh doanh. Một sản phẩm thuộc một loại và một thương hiệu; mỗi loại hoặc thương hiệu có thể có nhiều sản phẩm. Loại sản phẩm và thương hiệu có mã riêng, tên và thông tin mô tả. Các loại có thể phân cấp, mỗi loại có tối đa một loại cha và không được tạo vòng.

Một sản phẩm có nhiều ảnh, mỗi ảnh có mã riêng; cùng vị trí ảnh không được ghi lặp trong một sản phẩm. Sản phẩm công bố bán phải có một ảnh chính và đủ thông số bắt buộc. Thông số được định nghĩa theo loại hàng, có mã, tên phân biệt trong loại, kiểu giá trị và đơn vị nếu có. Mỗi sản phẩm có tối đa một giá trị cho một thông số, đúng kiểu và thuộc loại phù hợp. Việc thêm ảnh không làm thay đổi các giá trị thông số của sản phẩm.

Để bổ sung hàng bán, cửa hàng nhập từ các nhà cung cấp. Mỗi nhà cung cấp có mã riêng, tên tổ chức, người liên hệ, điện thoại, địa chỉ và tình trạng hợp tác. Một nhà cung cấp có thể giao nhiều sản phẩm; một sản phẩm có thể được nhập từ nhiều nhà cung cấp. Khi nhận hàng, nhân viên kho lập phiếu nhập có mã, số phiếu duy nhất, nhà cung cấp, người lập, thời điểm nhận và tình trạng xử lý. Mỗi phiếu biểu diễn một lần nhận thực tế, gồm các dòng ghi số dòng, sản phẩm, số lượng và đơn giá nhập. Số dòng phân biệt trong phiếu; cùng sản phẩm có thể xuất hiện nhiều dòng. Phiếu xác nhận phải có ít nhất một dòng và chỉ được ghi tăng kho một lần; chi phí bổ sung phải có căn cứ riêng.

Hàng tại cửa hàng được theo dõi theo ba nhóm: đủ điều kiện bán, chờ kiểm tra và không đủ điều kiện bán đang chờ xử lý. Cửa hàng ghi tồn đầu có căn cứ kiểm kê và các lần nhập, xuất, nhận lại, chuyển nhóm hoặc điều chỉnh. Mỗi lần phát sinh có mã, sản phẩm, số lượng, thời điểm, người thực hiện và chứng từ nguồn. Chuyển nhóm không làm tăng tổng tồn vật lý. Khi kiểm kê có chênh lệch, nhân viên lập đề nghị điều chỉnh để người quản lý duyệt.

Khách trực tuyến có thể chọn hàng vào giỏ; một sản phẩm chỉ có một dòng trong giỏ. Giỏ tạm chưa cần tài khoản, nhưng khi gửi đơn khách phải đăng nhập; mỗi tài khoản có tối đa một giỏ đang sử dụng. Đơn mua được phân biệt bằng mã và số đơn duy nhất, ghi ngày lập, kênh bán, khách nếu có, người nhận, điện thoại, địa chỉ giao và phương thức thanh toán dự kiến. Mỗi đơn có ít nhất một dòng, ghi số dòng, sản phẩm, số lượng và đơn giá bán. Số dòng phân biệt trong đơn; cùng sản phẩm có thể xuất hiện nhiều dòng với giá hoặc điều kiện khác nhau.

Giá, tên sản phẩm và thông tin nhận hàng được chốt khi tiếp nhận đơn; thay đổi danh mục hoặc địa chỉ sau đó không sửa giao dịch cũ. Mỗi đơn được áp dụng tối đa một mã giảm giá. Chương trình giảm giá có mã sử dụng duy nhất, loại và giá trị giảm, khoảng hiệu lực, mức đơn tối thiểu, trần giảm nếu có và giới hạn lượt. Mã được kiểm tra, chốt điều kiện khi xác nhận đơn và chỉ giảm tiền hàng. Tổng phải trả bằng tổng tiền các dòng cộng phí giao, trừ khoản giảm; tiền tính bằng đồng Việt Nam, làm tròn đến một đồng.

Nhân viên bán hàng kiểm tra khả năng cấp hàng trước khi xác nhận đơn trực tuyến và giữ hàng tương ứng. Lượng có thể nhận bán mới bằng lượng đủ điều kiện bán trừ lượng đang giữ. Giữ hàng chưa làm giảm tồn vật lý; khi bàn giao thực tế mới ghi xuất và kết thúc lượng giữ. Nếu cần đổi hàng, số lượng hoặc chi phí trước xuất, cửa hàng phải có sự chấp thuận của khách, lưu nội dung trước–sau và tính lại hàng giữ, giảm giá cùng tiền phải thu. Đề tài giao toàn bộ một đơn trong một đợt; dữ kiện đã bàn giao được giữ để xử lý sau bán.

Khách thanh toán bằng tiền mặt, chuyển khoản, ví hoặc thu tiền khi giao hàng. Một đơn có thể có nhiều lần thử và nhiều khoản thu; mỗi khoản ghi mã, phương thức, số tiền, thời điểm, kết quả và người xác nhận. Lần thất bại không được tính là đã thu. Mã giao dịch bên ngoài, nếu có, phân biệt trong phạm vi nhà cung cấp thanh toán. Đơn trả trước chỉ được bàn giao khi đã thu đủ; đơn trả trước chưa trả đủ đến hạn được xử lý hủy và hoàn khoản đã thu theo quy định. Mỗi khoản hoàn liên kết khoản thu gốc; có thể hoàn nhiều lần nhưng tổng không vượt tiền còn có thể hoàn.

Nhân viên giao hàng nhận phân công và ghi từng lần giao, thời điểm, kết quả cùng lý do thất bại. Khi đổi người giao vẫn giữ lịch sử phân công. Đề tài cho tối đa ba lần giao không thành công trên toàn đơn, sau đó chuyển sang thu hồi và xử lý hủy. Với thu tiền khi giao hàng, người giao ghi căn cứ khách đã trả; nhân viên bán hàng hoặc người quản lý xác nhận khoản thu, còn việc nộp tiền về cửa hàng được đối soát riêng. Đơn hoàn tất khi khách đã nhận hàng và tiền phải thu đã được xác nhận đủ. Mua tại quầy được lập đơn, giao trực tiếp và cấp chứng từ bán theo cùng quy tắc.

Khi hủy trước xuất, cửa hàng giải phóng hàng và lượt mã giảm giá đang giữ. Hủy sau xuất không tự tăng tồn mà phải nhận hàng thực tế về. Khi trả hàng đã nhận, cửa hàng lập hồ sơ có mã, đơn gốc, người đề nghị, ngày, lý do và các dòng cùng số lượng trả. Một đơn có thể được trả nhiều lần nhưng tổng lượng nhận lại không vượt lượng đã giao. Khách vãng lai được xử lý bằng chứng từ mua đã xác minh. Hàng nhận lại vào nhóm chờ kiểm tra, chỉ hàng đạt yêu cầu mới chuyển sang bán được. Tiền hoàn căn cứ giá, phần giảm đã phân bổ và chính sách của giao dịch gốc; đổi sản phẩm được ghi thành trả hàng và một đơn bán mới.

Khách có tài khoản đã nhận sản phẩm có thể gửi đánh giá gồm mã, khách, sản phẩm, điểm từ một đến năm, nội dung, ảnh và tình trạng duyệt; mỗi khách có tối đa một đánh giá hiện tại cho một sản phẩm. Yêu cầu tư vấn, khiếu nại hoặc bảo hành được lập thành hồ sơ hỗ trợ có mã, số hồ sơ duy nhất, người gửi, liên hệ, nội dung, thời điểm và tình trạng. Một hồ sơ có thể liên quan một đơn hoặc một đề nghị thu cũ, không đồng thời cả hai. Hồ sơ có tối đa một người phụ trách chính tại một thời điểm, có nhiều phản hồi và giữ lịch sử phân công, đóng hoặc mở lại. Bảo hành được đối chiếu căn cứ mua và điều kiện đã chốt; quy trình sửa chữa kỹ thuật chưa thuộc phạm vi đề tài.

Cửa hàng tiếp nhận đề nghị thu mua thiết bị cũ từ cả người có và chưa có tài khoản. Mỗi đề nghị có mã, thông tin liên hệ, một thiết bị, model, tình trạng và ảnh; có tối đa một hồ sơ hỗ trợ chính. Nhân viên có thể thẩm định, báo giá nhiều lần và lưu từng kết quả. Khi hai bên đồng ý, cửa hàng lập chứng từ thu mua có số duy nhất, đề nghị gốc, người giao, người nhận, thiết bị thực nhận và giá chốt. Mỗi đề nghị có tối đa một chứng từ thu mua có hiệu lực. Thiết bị nhận có mã riêng, tương ứng một mã sản phẩm hàng cũ, nhập vào nhóm chờ kiểm tra và chỉ được bán sau khi đủ điều kiện; không cộng vào tồn hàng mới cùng model.

Nếu khách đồng ý, khoản hoàn hoặc tiền thu cũ có thể được ghi tăng ví thay cho trả trực tiếp. Mỗi tài khoản có tối đa một ví; mỗi lần tăng, giảm ghi mã, số tiền, thời điểm và nguồn. Ví chỉ nhận tăng từ hoàn, thu cũ hoặc số dư mở đầu có căn cứ, dùng để trả đơn và không được âm. Một nguồn không tạo biến động hai lần; tiền dùng ví và tiền người giao nộp về không được tính thành khoản thu mới từ khách.

Cửa hàng lưu bài hướng dẫn theo chủ đề, mẫu trả lời hỗ trợ và thông báo cho từng tài khoản. Người quản lý cần thống kê nhập hàng, tồn theo nhóm, hàng đang giữ, lượng bán hoàn tất, thu và hoàn tiền, giao thất bại, hỗ trợ chưa giải quyết và thu cũ đang xử lý. Báo cáo xác định rõ kỳ và thời điểm ghi nhận; phân loại sản phẩm dùng thông tin đã chốt khi bán. Chứng từ và các lần xử lý được giữ lịch sử để tra cứu, kể cả khi khách, nhân viên hoặc sản phẩm ngừng sử dụng.

# MÔ TẢ THỰC THỂ (cập nhật theo bản mô tả v2)

Phân loại theo bài giảng: **cơ bản** là tài nguyên có trước khi vận hành, ổn định, không có thuộc tính thời gian; **đối tượng ngoài** là con người hoặc tổ chức; **nghiệp vụ** phát sinh khi vận hành và luôn có thuộc tính thời gian. Dòng chi tiết (dòng đơn, dòng phiếu nhập, dòng giỏ...) là mối kết hợp, không liệt kê như thực thể. Tồn kho, tổng tiền và thống kê là dữ liệu tính toán, không phải thực thể. Nhãn **[giả thiết]** là chính sách do PowerTech tự đặt trong bản mô tả v2, chưa có nguồn xác minh.

## 1 Thực thể CƠ BẢN

| **Thực thể** | **Thuộc tính chính** | **Ý nghĩa và lý do phân loại** |
| --- | --- | --- |
| Loại hàng | MaLoai, TenLoai, MoTa, MaLoaiCha | Danh mục phân loại, có thể phân cấp, mỗi loại tối đa một loại cha. Tên loại chưa được giả định duy nhất. |
| Thương hiệu | MaTH, TenTH, MoTa | Danh mục thương hiệu. Tên thương hiệu chưa được giả định duy nhất; tổ chức cung ứng hàng là nhà cung cấp. |
| Mặt hàng | MaSP, SKU, MaLoai, MaTH, TenSP, MoTa, GiaNiemYet, GiaKhuyenMai, ThoiHanBaoHanh, TinhTrangKinhDoanh, CoSeri | Danh mục hàng phục vụ nhiều giao dịch. MaSP và SKU đều phân biệt được mặt hàng. Giá, tên hiện tại không thay cho giá và tên đã chốt ở dòng bán cũ. CoSeri cho biết mặt hàng ghi số seri từng chiếc. |
| Ảnh mặt hàng | MaAnh, MaSP, ViTri, DuongDan, LaAnhChinh | Thành phần của mặt hàng. Vị trí không trùng trong cùng mặt hàng, mặt hàng đang bán có một ảnh chính. Ảnh độc lập với thông số; đây là ứng viên cho phân tích 4NF. |
| Định nghĩa thông số | MaTS, MaLoai, TenTS, KieuGiaTri, DonVi | Thông số kỹ thuật theo loại hàng. Giá trị thông số của từng mặt hàng là mối kết hợp giữa mặt hàng và định nghĩa thông số, mỗi cặp tối đa một giá trị. |
| Vai trò công việc | MaVT, TenVT | Các việc trong cửa hàng: tư vấn bán hàng, thu ngân kiêm thủ quỹ, kỹ thuật, kho, giao hàng, chăm sóc khách hàng, quản lý. Một nhân viên có thể kiêm nhiều việc nên liên kết nhân viên–vai trò là mối kết hợp. |
| Nhóm tình trạng kho | MaNhom, TenNhom | Ba nhóm: đủ điều kiện bán, chờ kiểm tra, không bán được chờ xử lý. Chuyển nhóm là sự kiện nghiệp vụ và không làm tăng tổng số hàng thực tế. |
| Chính sách đổi trả | MaCS, MaLoai, LoaiTruongHop, SoNgay, DieuKien, PhiXuLy | **[giả thiết]** Điều kiện đổi trả theo loại hàng và theo trường hợp: lỗi nhà sản xuất hoặc giao sai (30 ngày với linh kiện, 7 ngày với máy tính xách tay và màn hình), khách đổi ý (7 ngày, còn nguyên niêm phong). Nếu cần lưu lịch sử chính sách theo thời gian hiệu lực thì tách thành thực thể nghiệp vụ. |

## 2 Thực thể ĐỐI TƯỢNG NGOÀI

| **Thực thể** | **Thuộc tính chính** | **Vai trò và lý do phân loại** |
| --- | --- | --- |
| Khách hàng | MaKH, HoTen, SDT, Email, MaSoThue, TinhTrang | Người mua, người đề nghị bảo hành hoặc đổi trả. Khách tại quầy có thể chưa có tài khoản. MaSoThue chỉ có khi khách là doanh nghiệp cần hóa đơn. Họ tên, số điện thoại, email không đủ phân biệt hai khách. |
| Địa chỉ nhận hàng | MaDC, MaKH, TenNguoiNhan, SDT, DiaChiChiTiet, LaMacDinh | Thành phần của hồ sơ khách: một khách có nhiều địa chỉ, tại mỗi thời điểm tối đa một địa chỉ mặc định. |
| Nhân viên | MaNV, HoTen, SDT, TinhTrangLamViec | Người bán hàng, thu ngân, kỹ thuật, kho, giao hàng, chăm sóc khách hàng, quản lý. Là con người thuộc cửa hàng nên xếp vào nhóm đối tượng ngoài. |
| Nhà cung cấp | MaNCC, TenNCC, NguoiLienHe, SDT, DiaChi, MaSoThue, TinhTrangHopTac | Nhà phân phối hoặc đại lý chính hãng giao hàng, đồng thời nhận hàng lỗi và hàng gửi bảo hành. Tên và thông tin liên hệ có thể trùng; chưa coi mã số thuế là khóa khi chưa có quy tắc bắt buộc và duy nhất. |

Hãng sản xuất nhận bảo hành được xem là thương hiệu hoặc nhà cung cấp; chưa tách thành thực thể riêng.

## 3 Thực thể NGHIỆP VỤ

| **Thực thể hoặc hồ sơ chính** | **Thuộc tính chính** | **Thời gian và ý nghĩa phát sinh** |
| --- | --- | --- |
| Tài khoản khách | MaTK, DinhDanhDangNhap, MaKH, TinhTrang, NgayDangKy, ThoiDiemNoiHoSo | Lập khi khách đăng ký bằng số điện thoại hoặc email, gắn với tối đa một khách. Hồ sơ mua tại quầy chỉ được nối vào tài khoản sau khi khách xác nhận bằng mã gửi về số điện thoại. |
| Biến động số dư tài khoản (tùy chọn) | MaBD, MaTK, SoTien, LoaiBienDong, NguonBienDong, ThoiDiem | Chỉ cần nếu giữ cách hoàn tiền bằng ghi tăng số dư tài khoản mua hàng. Số dư là dữ liệu tính từ các biến động, không phải thuộc tính độc lập. |
| Phiếu nhập | MaPN, SoPhieu, MaNCC, MaNV, ThoiDiemNhan, TinhTrang | Phát sinh khi nhận hàng. Dòng nhập (số dòng, mặt hàng, số lượng, giá nhập) là mối kết hợp; cùng mặt hàng có thể ở nhiều dòng. Chỉ được ghi tăng kho một lần. |
| Hàng có seri | SoSeri, MaSP, MaPN, SoDongNhap, TinhTrang, ThoiDiemNhap | Mỗi chiếc hàng có seri phát sinh khi nhập. Tình trạng: trong kho, đã bán, đang bảo hành, đã gửi hãng, đã trả nhà cung cấp. **[giả thiết]** SoSeri chỉ được giả định duy nhất trong cùng mặt hàng. Bán ra thì gắn với dòng đơn. |
| Giao dịch kho | MaGDK, MaSP, MaNhom, LoaiBienDong, SoLuong, ThoiDiem, MaNV, ChungTuNguon | Mỗi lần nhập, bán, giao, trả, chuyển nhóm hoặc điều chỉnh. Chuyển nhóm tạo hai biến động đối ứng. Là nguồn để tính tồn theo nhóm. |
| Đợt kiểm kê và đề nghị điều chỉnh | MaDot, ThoiDiem, kết quả đếm theo mặt hàng, lý do, MaNVDeNghi, MaNVDuyet | Phát sinh khi kiểm kê. Chênh lệch chỉ được điều chỉnh sau khi người quản lý duyệt. |
| Giỏ hàng | MaGio, MaTK, TrangThai, ThoiDiemTao | Tập hàng khách chọn qua mạng. Mỗi mặt hàng một dòng trong giỏ; mỗi tài khoản tối đa một giỏ đang dùng. |
| Đơn hàng | MaDH, SoDH, NgayLap, KenhBan, LoaiDon, MaKH, MaNVBan, TenNguoiNhan, SDTNhan, DiaChiGiao, PhiGiao, MaMG, TrangThai, SoPhienBan | Gồm phiếu bán tại quầy và đơn đặt qua mạng, kể cả đơn đặt trước có đặt cọc. LoaiDon: có sẵn, đặt trước hoặc lắp theo yêu cầu. Dòng đơn là mối kết hợp (số dòng, mặt hàng, số lượng, đơn giá đã chốt, seri nếu có). Mỗi lần sửa đơn được khách đồng ý tạo phiên bản mới. Tổng phải trả là dữ liệu tính từ các dòng, giảm giá và phí giao. |
| Mã giảm giá | MaMG, CodeChuan, LoaiGiam, MucGiam, NgayBatDau, NgayKetThuc, DonToiThieu, GiamToiDa, GioiHanLuot | Chương trình có thời gian áp dụng. Mỗi đơn dùng tối đa một mã, chỉ giảm tiền hàng. Số lượt đã dùng là dữ liệu tính từ các đơn. |
| Giữ hàng | MaGiu, MaDH, SoDong, SoLuong, ThoiDiemGiu, ThoiDiemKetThuc, LyDoKetThuc | Giữ số lượng cho dòng đơn sau khi nhân viên xác nhận. Kết thúc khi xuất hàng, hủy đơn hoặc giao thất bại. Hàng đang giữ vẫn tồn tại vật lý. |
| Thanh toán | MaTT, MaDH, LoaiKhoan, PhuongThuc, SoTien, ThoiDiem, KetQua, MaNVXacNhan | Mỗi lần trả tiền, gồm cọc, phần còn lại, thu khi giao. Lần không thành công không được tính là đã thu. PhuongThuc (tiền mặt, chuyển khoản, thẻ, ví điện tử, COD) là thuộc tính, không phải thực thể. |
| Khoản hoàn | MaHoan, MaTT, MaDH, SoTien, PhuongThucHoan, MaNVDuyet, ThoiDiemDuyet, ThoiDiemChi | Phát sinh khi hoàn tiền, gắn khoản thu gốc và do người quản lý duyệt. Có thể hoàn nhiều lần nhưng tổng không vượt số tiền đã thu. |
| Phiếu giao và lần giao | MaGiao, MaDH, MaNVGiao, ThoiDiemXuat; SoLan, ThoiDiem, KetQua, LyDoThatBai | Phiếu giao lập khi xuất hàng. Mỗi đơn thử giao tối đa 3 lần; sau 3 lần không thành công thì hủy. |
| Bàn giao tiền COD | MaBG, MaGiao, MaNVGiao, MaNVNhan, SoTien, ThoiDiem | Người giao nộp tiền thu hộ về thủ quỹ. Cần phân biệt lúc khách trả, lúc xác nhận khoản thu và lúc nộp tiền. |
| Hồ sơ đổi trả | MaHS, MaDH, MaKH, NgayDeNghi, LyDo, LoaiTruongHop, TrangThai | Đề nghị đổi hoặc trả. Dòng trả (đơn gốc, số dòng, số lượng, seri) là mối kết hợp; một đơn có thể trả nhiều lần nhưng tổng không vượt số đã giao. |
| Lần nhận lại và kiểm tra | MaNhanLai, MaHS, ThoiDiemNhan, MaNVKiemTra, KetLuan, NhomSauKiemTra, MaNVDuyet | Hàng nhận về luôn vào nhóm chờ kiểm tra; chỉ sau khi kỹ thuật viên kiểm tra và người quản lý duyệt mới chuyển nhóm. |
| Phiếu tiếp nhận bảo hành | MaPhieuBH, MaKH, MaSP, SoSeri, MaDH, SoDong, MoTaLoi, PhuKien, NgayNhan, NgayHenTra, KetQua, NgayTra | Lập khi sản phẩm đủ điều kiện bảo hành. Ghi sản phẩm, dòng mua gốc, hẹn trả và kết quả (sửa xong, đổi mới, hoàn tiền, từ chối kèm lý do). Cửa hàng là đầu mối, không là nơi sửa chữa chính. |
| Phiếu gửi nhà cung cấp hoặc hãng | MaGui, MaNCC, LyDo, NgayGui, NgayNhanKetQua, KetQua | Lập khi gửi hàng bảo hành hoặc trả hàng lỗi. Dòng gửi (seri hoặc mặt hàng, nguồn là phiếu bảo hành hoặc hồ sơ đổi trả) là mối kết hợp. Kết quả: đổi hàng mới, đã sửa hoặc ghi giảm tiền. |

### Mối kết hợp, không phải thực thể
Dòng đơn; dòng phiếu nhập; dòng giỏ hàng; giá trị thông số của mặt hàng; nhân viên–vai trò; dòng trả; dòng gửi nhà cung cấp.

### Dữ liệu tính toán, không phải thực thể
Tồn kho theo nhóm, số lượng có thể nhận bán (đủ điều kiện bán trừ đang giữ), thành tiền từng dòng, tổng phải trả, số lượt đã dùng của mã giảm giá, số dư tài khoản mua hàng, các báo cáo thống kê. Nếu lưu sẵn thì phải ghi rõ là cột suy diễn.

### Chưa xếp thành thực thể
Phương thức thanh toán, kênh bán, trạng thái đơn: thuộc tính phân loại. Biểu phí giao hàng theo khu vực và hóa đơn bán lẻ: tham số hoặc chứng từ xuất theo quy định, chưa mô hình hóa; sẽ thêm nếu cần truy vấn.

### Đã bỏ so với bản nộp đầu (theo bản mô tả v2)
Đánh giá sản phẩm và hồ sơ hỗ trợ; thu mua thiết bị cũ (đề nghị, thẩm định, báo giá, chứng từ thu mua, thiết bị cũ); thông báo; bài hướng dẫn và trả lời mẫu; đối tác thanh toán; tài khoản nhân viên và vai trò quyền hạn; phân công giao hàng theo lịch sử; phiên bản mã giảm giá; yêu cầu xử lý, nhật ký giao dịch và lệnh hoàn ngoài. Bản nộp đầu nguyên văn lưu ở `PowerTech-CSDL-NC_ban_nop.md`.

### Cần xác nhận
1. Có giữ ghi tăng số dư tài khoản khi hoàn tiền không (quyết định có thực thể biến động số dư hay không).
2. Có tách "hãng sản xuất nhận bảo hành" thành thực thể riêng không.
3. Các chính sách **[giả thiết]** (30 ngày và 7 ngày, đổi ý trong 7 ngày, seri duy nhất trong mặt hàng) cần hỏi giảng viên hoặc chốt trong nhóm.
4. `database/data.sql` không có cấu trúc riêng cho seri, phiếu bảo hành, hồ sơ đổi trả, đặt cọc, phân công giao: danh sách trên là thiết kế đề xuất, không phải mô tả CSDL hiện có.
