**Hệ thống quản lý cửa hàng thiết bị công nghệ PowerTech**

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

# MÔ TẢ THỰC THỂ

## 1 Thực thể CƠ BẢN

| **Thực thể** | **Thuộc tính chính** | **Ý nghĩa và lý do phân loại** |
| --- | --- | --- |
| Loại sản phẩm | MaLoai, TenLoai | Danh mục phân loại hàng hóa dùng chung; quan hệ cha con lưu ở PHANCAPLOAI. Tên loại chưa được giả định duy nhất. |
| Thương hiệu | MaTH, TenTH | Danh mục thương hiệu sản phẩm. Nhãn hiệu là thông tin phân loại; tổ chức ký hợp đồng cung ứng được quản lý bằng NHACUNGCAP. |
| Sản phẩm | MaSP, SKU, MaLoai, MaTH, TenSP, giá hiện tại, thời hạn bảo hành | Danh mục mặt hàng phục vụ nhiều giao dịch. MaSP và SKU hiện tại đều phân biệt; giá và tên hiện tại không thay thế snapshot của dòng bán cũ. |
| Định nghĩa thông số | MaTS, MaLoai, TenTS, KieuGiaTri, DonVi | Định nghĩa thuộc tính kỹ thuật theo loại hàng. GIATRITHONGSO là giá trị của từng sản phẩm; ảnh sản phẩm là thông tin thành phần. |
| Vai trò | MaVT, TenVTChuan | Danh mục quyền hạn sử dụng hệ thống. Phân quyền tài khoản hiện hành là liên kết nghiệp vụ, không phải một người. |
| Nhóm tình trạng kho | MaNhom, TenNhom | Ba nhóm kho: bán được; chờ kiểm tra; không bán được chờ xử lý. Chuyển nhóm là sự kiện nghiệp vụ và không làm tăng tổng lượng vật lý. |
| Chính sách trả hàng | MaCSTra, SoPBCSTra, nội dung, thời gian hiệu lực | Thông tin nền quy định điều kiện trả hàng; quản lý theo phiên bản để đối chiếu giao dịch cũ. Hồ sơ yêu cầu trả mới là nghiệp vụ. |
| Thiết bị cũ | MaThietBi, MaSPCu, MaCTTM | Tài sản vật lý được nhận diện riêng. Theo B6, một thiết bị có một mã hàng cũ và một chứng từ thu mua gốc; hồ sơ thẩm định, báo giá, thu mua thuộc nghiệp vụ. |
| Chủ đề hướng dẫn, bài hướng dẫn và trả lời mẫu | Mã chủ đề, mã bài, mã câu trả lời, tiêu đề và nội dung | Kho nội dung hướng dẫn và câu trả lời chuẩn được dùng lặp lại. Thời điểm soạn hoặc sửa nội dung không biến tài nguyên tham chiếu thành giao dịch bán hàng. |

Ảnh, vị trí ảnh, giá trị thông số và quan hệ phân cấp thuộc nhóm cơ bản vì mô tả danh mục. THIETBICU mô tả bản thân tài sản; GIAODICHKHO mô tả sự kiện làm thay đổi lượng của tài sản. Hai loại thông tin cần được phân biệt dù liên quan cùng một mặt hàng.

## 2 Thực thể ĐỐI TƯỢNG NGOÀI

| **Thực thể** | **Thuộc tính chính** | **Vai trò và lý do phân loại** |
| --- | --- | --- |
| Khách hàng | MaKH, HoTen, SDT, Email, NgayGhiNhan, TrangThai | Người mua, người yêu cầu hỗ trợ hoặc thu cũ. Khách tại quầy có thể chưa có tài khoản; một khách có nhiều địa chỉ. |
| Nhân viên | MaNV, HoTen, SDT, Email, TrangThaiLamViec | Người tiếp nhận, kiểm tra, giao hàng, duyệt hoàn hoặc quản lý. Thuộc công ty vẫn được xếp vào nhóm người tương tác với hệ thống. |
| Nhà cung cấp | MaNCC, TenNCC, NguoiLienHe, SDT, Email, DiaChi, MaSoThue | Tổ chức hoặc cá nhân cung ứng hàng. Tên và thông tin liên hệ có thể trùng; chưa coi mã số thuế là khóa khi chưa có quy tắc bắt buộc và duy nhất. |
| Đối tác thanh toán | MaNhaCungCapTT, TenDoiTac, LoaiDoiTac, TrangThai | Ngân hàng, cổng thanh toán hoặc ví điện tử xử lý tiền bên ngoài. K2 bổ sung hồ sơ riêng, dùng cùng mã đối tác với THU\_BENNGOAI. |

DIACHI là thành phần của hồ sơ khách nên được đặt cùng nhóm này. TAIKHOAN là hồ sơ truy cập, không đồng nhất với KHACHHANG hoặc NHANVIEN. TACNHAN còn chứa nguồn hệ thống nên không xếp toàn bộ quan hệ này thành đối tượng ngoài; nó là cấu trúc định danh hỗ trợ ghi nhận nghiệp vụ.

## 3 Thực thể NGHIỆP VỤ

| **Thực thể hoặc hồ sơ chính** | **Thuộc tính chính** | **Thời gian và ý nghĩa phát sinh** |
| --- | --- | --- |
| Tài khoản | MaTK, định danh đăng nhập, trạng thái | Hồ sơ được lập để truy cập; liên kết khách, nhân viên và vai trò được quản lý riêng. Không suy người gửi trong quá khứ từ liên kết hiện tại. |
| Phiếu nhập | MaPN, số phiếu, MaNCC, trạng thái | Phát sinh khi nhận hàng, có ngày lập và xác nhận. Dòng nhập và chi phí nhập thuộc cùng nghiệp vụ; cho phép cùng sản phẩm trên nhiều dòng. |
| Giao dịch kho và chuyển nhóm kho | MaGDK, MaSP, MaNhom, loại biến động, lượng, nguồn | Ghi nhận tăng giảm vật lý tại thời điểm phát sinh. Chuyển nhóm tạo hai biến động đối ứng; nguồn được xác nhận một lần. |
| Giữ hàng và sự kiện giữ hàng | MaGiu, MaDH, SoDong, SoPBDon, lượng, HanGiuDen | Giữ số lượng cho dòng đơn; sự kiện giải phóng hoặc kết thúc giữ có thời điểm riêng. Hàng đang giữ vẫn tồn tại vật lý. |
| Đợt kiểm kê và đề nghị điều chỉnh kho | Mã đợt, kết quả đếm từng sản phẩm nhóm, đề nghị, quyết định | Phát sinh khi kiểm kê và duyệt chênh lệch. B7 lưu kết quả đếm cuối; lịch sử đếm lại hoặc duyệt lại cần cấu trúc riêng. |
| Giỏ hàng | MaGio, MaTK qua liên kết, trạng thái | Tập lựa chọn tạm của khách. Có lịch sử nhiều giỏ; quy tắc tối đa một giỏ đang hoạt động chỉ áp dụng trên tập con. |
| Đơn hàng và phiên bản đơn | MaDH, SoDH, ngày lập, trạng thái, SoPBDon | Giao dịch mua hàng và các lần điều chỉnh được chấp thuận. Dòng ổn định có SoDong; chi tiết theo phiên bản giữ giá và thông tin đã chốt. |
| Mã giảm giá và phiên bản mã | MaMG, CodeChuan, SoPBMG, giới hạn và hiệu lực | Chương trình ưu đãi được lập và áp dụng có thời hạn. APDUNGMAGIAM liên kết đơn; SUKIENLUOTMA ghi giữ, dùng và hoàn lượt. |
| Lần thử thanh toán và khoản thu | MaLanThu hoặc MaThu, MaDH, phương thức, số tiền, kết quả | Một lần thử có thể thất bại; một khoản thu xác nhận là sự kiện tiền khác. Một đơn có thể có nhiều khoản thu hợp lệ. |
| Khoản hoàn | MaHoan, MaThu, MaDH, số tiền duyệt, kết quả | Phát sinh khi hoàn khoản thu gốc; có ngày duyệt và thực hiện. Nhiều khoản hoàn từng phần phải được cộng để kiểm tra hạn mức. |
| Ví và biến động ví | MaVi, MaTK; MaBDVi, số tiền, loại biến động, nguồn | Ví phát sinh theo tài khoản; từng lần tăng giảm có thời điểm. Số dư được tính từ sổ biến động, không phải thuộc tính trong lược đồ VI. |
| Bàn giao COD | MaBG, người giao nhận, khoản COD và số tiền | Chứng từ bàn giao tiền thu hộ; cần phân biệt lúc khách trả, lúc xác nhận và lúc nhân viên bàn giao tiền. |
| Hồ sơ giao, phân công và lần giao | MaGiao, MaPCGiao, SoLan, người giao, kết quả | Hồ sơ và lịch sử giao hàng. Một đơn có nhiều lần thử giao; quy tắc tối đa ba lần thất bại xét trên toàn đơn. |
| Hồ sơ trả và lần nhận trả | MaTra, MaDH, dòng trả; MaNhanTra, dòng thực nhận | Yêu cầu trả khác việc nhận lại hàng thật. Chỉ hàng đã nhận mới được tăng kho; nhóm bán được được xác định sau kiểm tra. |
| Tiếp nhận bảo hành | MaBaoHanh, sản phẩm, dòng mua gốc, nội dung | Ghi nhận lần tiếp nhận và đối chiếu điều kiện bảo hành đã bán. Không mở rộng sang hệ thống quản lý sửa chữa đầy đủ. |
| Đánh giá và hồ sơ hỗ trợ | Mã đánh giá hoặc hỗ trợ, người gửi, đơn hoặc đề nghị thu cũ | Phát sinh sau tương tác; phản hồi, phân công, ảnh và đính kèm có bản ghi riêng. Hồ sơ hỗ trợ liên kết đơn hoặc thu cũ theo quy tắc đã nêu. |
| Đề nghị thu cũ, thẩm định và báo giá | MaTC, mã thẩm định, mã báo giá, người xử lý | Hồ sơ đánh giá thiết bị của khách; nhiều lần thẩm định và báo giá theo thời điểm. Báo giá hiện hành là tập con, không thay toàn lịch sử. |
| Chứng từ thu mua và khoản chi | MaCTTM, MaTC, thiết bị nhận, khoản chi | Chứng từ mua thiết bị và việc chi tiền. Tối đa một chứng từ có hiệu lực mỗi đề nghị theo B6; nhận hàng và chi tiền có trạng thái riêng. |
| Thông báo và nhật ký | Mã bản ghi, tác nhân, nội dung, thời điểm | Kết quả gửi thông tin và chứng cứ thao tác; không thay thế chứng từ tiền hoặc kho. |
| Yêu cầu xử lý, nhật ký giao dịch và lệnh hoàn ngoài | Mã yêu cầu, khóa chống lặp; mã nhật ký; mã lệnh hoàn | K3 và K4 bổ sung: chống xử lý lặp, đo chờ khóa và lưu chỉ thị hoàn tiền để gửi sau khi transaction nội bộ đã kết thúc. |