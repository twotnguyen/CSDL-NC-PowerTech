# MỤC 1. MÔ TẢ ĐỀ TÀI VÀ XÁC ĐỊNH LĨNH VỰC CẦN TIN HỌC HÓA

## 1.1. Bối cảnh đề tài và lĩnh vực cần tin học hóa

PowerTech là cửa hàng chuyên kinh doanh bán lẻ linh kiện máy tính (bộ vi xử lý, bo mạch chủ, bộ nhớ RAM, card đồ họa, ổ cứng lưu trữ, nguồn máy tính, vỏ case), máy tính đồng bộ, máy tính xách tay và các thiết bị ngoại vi công nghệ. Hoạt động kinh doanh của cửa hàng phục vụ cả hai kênh phân phối chính: bán hàng trực tiếp tại quầy và bán hàng trực tuyến thông qua nền tảng web.

Trong mô hình vận hành bán lẻ thiết bị công nghệ, hoạt động quản lý gặp phải nhiều khó khăn đặc thù:
1. **Tính chất phức tạp của hàng hóa:** Mỗi linh kiện máy tính có nhiều thông số kỹ thuật ràng buộc lẫn nhau (như chuẩn socket, chuẩn bus bộ nhớ, kích thước tương thích). Đồng thời, mỗi sản phẩm cụ thể xuất kho đều mang một mã nhận diện và số seri riêng biệt để phục vụ theo dõi nguồn gốc và bảo hành.
2. **Biến động giá và tồn kho liên tục:** Thị trường công nghệ có tốc độ thay đổi mẫu mã và đơn giá nhập - xuất rất nhanh. Việc tính toán lợi nhuận và theo dõi giá vốn đòi hỏi phải ghi nhận chính xác đơn giá tại từng thời điểm giao dịch thực tế.
3. **Áp lực đồng bộ tồn kho giữa hai kênh bán:** Hàng hóa lưu trữ tại cửa hàng phải đáp ứng đồng thời cho khách vào mua trực tiếp tại showroom và khách đặt qua mạng. Nếu không có cơ chế kiểm soát giữ hàng và phân loại kho rõ ràng, cửa hàng rất dễ rơi vào tình trạng bán trùng hàng, hứa giao cho khách online nhưng thực tế hàng đã bị bán cho khách tại quầy.
4. **Quy trình sau bán hàng phức tạp:** Các thiết bị phần cứng luôn gắn liền với chính sách bảo hành dài hạn (từ 12 đến 36 tháng) và chính sách đổi trả trong những ngày đầu sử dụng. Việc lưu trữ biên nhận, kiểm tra tem niêm phong và đối soát lịch sử giao dịch ban đầu nếu làm thủ công bằng sổ sách sẽ gây nhầm lẫn, chậm trễ và giảm uy tín của cửa hàng.

Do đó, lĩnh vực cần tin học hóa của đề tài là: **Xây dựng hệ thống quản lý cơ sở dữ liệu toàn diện cho hoạt động bán lẻ thiết bị công nghệ PowerTech**, bao gồm các phân hệ nghiệp vụ cốt lõi: quản trị danh mục sản phẩm và thông số kỹ thuật, quản lý đối tác (khách hàng, nhà cung cấp, nhân viên), quản lý bán hàng tại quầy và bán hàng trực tuyến, theo dõi dòng tiền và phương thức thanh toán, quản lý nhập hàng và biến động kho theo tình trạng, cùng quy trình tiếp nhận bảo hành và đổi trả hàng sau bán.

---

## 1.2. Mô tả chi tiết các quy trình nghiệp vụ của cửa hàng

### 1.2.1. Quản lý danh mục hàng hóa, ảnh và thông số kỹ thuật
Cửa hàng phân loại sản phẩm theo từng nhóm ngành hàng (loại hàng) và thương hiệu sản xuất. Các loại hàng có thể tổ chức phân cấp cha - con (ví dụ: nhóm lớn "Linh kiện máy tính" chứa các nhóm con "Bộ nhớ RAM", "Ổ cứng SSD"). Mỗi thương hiệu và loại hàng đều có mã nhận diện riêng cùng tên gọi và mô tả chi tiết.

Mỗi mặt hàng kinh doanh được định danh bằng một mã nội bộ và một mã phân loại thương mại duy nhất (mã SKU), cùng với tên gọi, mô tả giới thiệu, đơn giá niêm yết hiện tại, thời hạn bảo hành tiêu chuẩn tính theo tháng và trạng thái đang kinh doanh hay ngừng kinh doanh. Một mặt hàng chỉ thuộc về một loại hàng và một thương hiệu duy nhất.

Để hỗ trợ khách hàng tìm hiểu, mỗi mặt hàng có một bộ sưu tập ảnh minh họa. Trong một mặt hàng, các vị trí sắp xếp ảnh không được trùng nhau và bắt buộc phải chỉ định đúng một ảnh đại diện chính. Đồng thời, mỗi loại hàng có một bộ quy định các thông số kỹ thuật đặc thù (như dung lượng, tốc độ xung nhịp, công suất, chuẩn kết nối). Mỗi mặt hàng thuộc loại đó sẽ có một giá trị thông số cụ thể tương ứng. Việc cập nhật thêm ảnh minh họa hoàn toàn độc lập và không làm ảnh hưởng đến các thông số kỹ thuật của mặt hàng.

### 1.2.2. Quản lý hồ sơ khách hàng và chính sách khách hàng thân thiết
Đặc thù của ngành bán lẻ linh kiện và thiết bị công nghệ là gắn liền với vòng đời sản phẩm lâu dài (bảo hành từ 1 đến 3 năm, bảo dưỡng định kỳ và nâng cấp phần cứng). Vì vậy, ngay cả đối với khách mua trực tiếp tại quầy, cửa hàng vẫn áp dụng chính sách thu thập và quản lý thông tin khách hàng một cách bài bản, thống nhất dựa trên Số điện thoại định danh:
- **Khách hàng mua trực tiếp tại quầy:** Khi phát sinh giao dịch mua hàng, nhân viên bán hàng bắt buộc thu thập thông tin cơ bản gồm Họ tên và Số điện thoại của khách để lập hồ sơ khách hàng trên hệ thống. Việc lưu trữ này có ý nghĩa nghiệp vụ sống còn:
  1. *Căn cứ kích hoạt và tra cứu bảo hành điện tử:* Giúp khách hàng không lo bị mất quyền lợi bảo hành trong trường hợp làm mất phiếu bảo hành giấy.
  2. *Lưu trữ lịch sử cấu hình máy:* Phục vụ cho việc tư vấn tương thích khi khách hàng quay lại nâng cấp linh kiện (như nâng cấp RAM, nâng cấp card đồ họa, thay nguồn) hoặc kiểm tra lịch sử bảo dưỡng, vệ sinh máy định kỳ.
  3. *Tích lũy doanh số nâng hạng khách hàng thân thiết:* Mọi giá trị giao dịch mua tại quầy đều được cộng dồn vào hồ sơ khách hàng để xét nâng bậc thành viên (thành viên Bạc, Vàng, Kim Cương) kèm các chính sách ưu đãi giảm giá và quà tặng tri ân.
- **Khách hàng có tài khoản trực tuyến:** Khách hàng đăng ký tài khoản định danh để giao dịch trên hệ thống mạng, có thêm thông tin địa chỉ thư điện tử, ngày đăng ký và có thể lưu nhiều địa chỉ nhận hàng khác nhau để thuận tiện khi đặt giao hàng (trong đó tại mỗi thời điểm chỉ có tối đa một địa chỉ được chỉ định làm địa chỉ mặc định).
- **Cơ chế đồng bộ và chuyển đổi xuyên suốt:** Khi một khách hàng từng mua tại quầy tiến hành đăng ký tài khoản trực tuyến trên hệ thống bằng đúng Số điện thoại đã mua hàng, hệ thống sẽ tự động liên kết toàn bộ hồ sơ mua sắm trước đây tại quầy vào tài khoản trực tuyến mới. Nhờ đó, khách hàng có thể tự tra cứu trực tuyến toàn bộ lịch sử mua hàng, thời hạn bảo hành còn lại của từng linh kiện và điểm thưởng tích lũy của mình mà không bị gián đoạn dữ liệu.

Nhân viên làm việc tại cửa hàng gồm các bộ phận: nhân viên tư vấn bán hàng, nhân viên kỹ thuật kho, nhân viên giao hàng, nhân viên tiếp nhận chăm sóc khách hàng và người quản lý. Mỗi nhân viên có mã nhân viên, họ tên, số điện thoại và trạng thái làm việc.

### 1.2.3. Quy trình bán hàng trực tiếp tại quầy (Mua tại cửa hàng)
Khách hàng đến showroom của PowerTech sẽ được nhân viên tư vấn lựa chọn linh kiện hoặc cấu hình máy phù hợp. Khi khách đồng ý mua, quy trình bán hàng tại quầy diễn ra như sau:
1. Nhân viên bán hàng lập một chứng từ bán hàng trực tiếp (phiếu bán hàng tại quầy) ghi nhận thời điểm bán, nhân viên thực hiện và thông tin khách hàng (Họ tên và Số điện thoại nhằm kích hoạt bảo hành điện tử và tích lũy doanh số thành viên).
2. Phiếu bán hàng ghi rõ từng dòng sản phẩm được chọn, số lượng mua và đơn giá bán thực tế chốt tại thời điểm giao dịch.
3. Khách hàng thực hiện thanh toán ngay tại quầy thu ngân bằng tiền mặt hoặc chuyển khoản qua mã QR ngân hàng.
4. Nhân viên kỹ thuật xuất sản phẩm từ kho hàng trưng bày/kho bán, tiến hành dán tem bảo hành của cửa hàng lên linh kiện, mở hộp kiểm tra ngoại quan và bật máy chạy thử tính năng trước sự chứng kiến của khách hàng.
5. Sau khi kiểm tra hoàn tất, nhân viên bàn giao sản phẩm cùng phiếu bán hàng kiêm phiếu bảo hành cho khách mang về. Giao dịch được xác nhận hoàn tất ngay tại chỗ, số lượng hàng được trừ trực tiếp khỏi lượng tồn kho vật lý.

### 1.2.4. Quy trình bán hàng trực tuyến và điều phối giao hàng
Đối với kênh bán hàng qua mạng, quy trình được kiểm soát chặt chẽ nhằm tránh rủi ro thiếu hụt hàng hóa:
1. Khách hàng đăng nhập, tìm kiếm sản phẩm và đưa hàng vào giỏ hàng cá nhân. Mỗi sản phẩm chỉ xuất hiện trên một dòng của giỏ hàng với số lượng dự kiến mua.
2. Khi khách hàng nhấn gửi đơn mua hàng, hệ thống kiểm tra số lượng hàng thực tế đang có sẵn ở nhóm hàng đủ điều kiện bán. Nếu đủ số lượng, hệ thống sẽ tiến hành **giữ hàng tạm thời** cho đơn hàng đó. Lượng hàng đang giữ này sẽ ngăn không cho các đơn hàng khác đặt tiếp, nhưng vẫn tồn tại vật lý trong kho cho đến khi xuất đi.
3. Đơn hàng trực tuyến được ghi nhận với một mã số đơn duy nhất, ngày giờ lập, thông tin người nhận, số điện thoại, địa chỉ giao hàng, danh sách các mặt hàng cùng số lượng và đơn giá chốt tại thời điểm đặt. Đơn hàng có thể được áp dụng tối đa một mã ưu đãi giảm giá hợp lệ.
4. Khách hàng lựa chọn phương thức thanh toán: thanh toán trực tuyến trả trước (chuyển khoản ngân hàng, ví điện tử) hoặc thanh toán khi nhận hàng (COD). Với đơn hàng trả trước, chỉ khi hệ thống ghi nhận khoản thu tiền thành công thì đơn hàng mới được chuyển sang bộ phận kho để chuẩn bị xuất hàng.
5. Bộ phận kho tiến hành lấy hàng theo số lượng đang giữ, đóng gói niêm phong và bàn giao cho nhân viên giao vận kèm phiếu vận chuyển. Lúc này, việc giữ hàng kết thúc và lượng hàng chính thức được ghi giảm khỏi tồn kho vật lý.
6. Nhân viên giao vận chuyển hàng đến địa chỉ người nhận. Tại thời điểm nhận hàng:
   - Nếu khách hàng nhận hàng và thanh toán đủ tiền (đối với đơn COD), nhân viên giao hàng xác nhận phát hàng thành công, bàn giao tiền mặt về thủ quỹ cửa hàng và đơn hàng chuyển sang trạng thái hoàn tất.
   - Nếu khách hàng vắng mặt hoặc từ chối nhận hàng, nhân viên giao hàng ghi nhận lý do giao thất bại. Cửa hàng cho phép thử giao tối đa 3 lần cho một đơn hàng. Nếu sau 3 lần vẫn không giao được (khách bỏ đơn/boom hàng), đơn hàng sẽ bị hủy, hàng hóa được nhân viên giao vận chuyển trả lại kho và lượng hàng giữ trước đó được giải phóng hoàn toàn về lại nhóm hàng có thể bán.

### 1.2.5. Cơ chế tiếp nhận và xử lý bảo hành (Warranty)
Do đặc thù linh kiện điện tử có giá trị cao và thời gian bảo hành dài hạn, cơ chế bảo hành tại PowerTech được quy định nghiêm ngặt:
1. Mỗi sản phẩm khi bán ra đều được gắn số seri duy nhất cùng tem niêm phong ghi rõ tháng/năm bán của PowerTech. Thời hạn bảo hành tiêu chuẩn được chốt cố định theo thông tin giao dịch tại thời điểm mua ban đầu.
2. Khi thiết bị gặp sự cố kỹ thuật trong thời gian bảo hành, khách hàng mang thiết bị đến cửa hàng hoặc gửi chuyển phát về trung tâm bảo hành của PowerTech.
3. Nhân viên kỹ thuật tiếp nhận tiến hành kiểm tra các điều kiện tiên quyết: số seri trên thân máy có trùng khớp với hồ sơ mua hàng lưu trên hệ thống hay không; tem bảo hành còn nguyên vẹn, không bị rách, chắp vá hay tẩy xóa; thiết bị không có dấu hiệu bị chập cháy nổ, ngập nước, rơi vỡ biến dạng do lỗi người dùng.
4. Nếu đủ điều kiện, nhân viên lập **Phiếu tiếp nhận bảo hành** ghi rõ: mã phiếu, thông tin khách hàng, thiết bị nhận bảo hành, số seri, đối chiếu đơn mua ban đầu, mô tả chi tiết lỗi phát sinh, các phụ kiện đi kèm và thời gian hẹn trả kết quả xử lý.
5. Bộ phận kỹ thuật tiến hành xử lý theo quy chuẩn: xử lý sửa chữa lỗi linh kiện, đổi linh kiện tương đương đang có trong kho, hoặc chuyển gửi về trung tâm bảo hành của hãng sản xuất. Mọi diễn biến xử lý đều được cập nhật vào tiến trình của phiếu bảo hành.
6. Khi việc xử lý hoàn tất, nhân viên liên hệ khách hàng đến nhận lại thiết bị, cùng khách kiểm tra vận hành thử và bàn giao kèm biên bản trả bảo hành.

### 1.2.6. Cơ chế đổi trả hàng và phân loại kho (Returns & Stock Segregation)
Nhằm bảo vệ quyền lợi người tiêu dùng và duy trì chất lượng nguồn hàng bán ra, chính sách đổi trả hàng được vận hành như sau:
1. Cửa hàng áp dụng chính sách đổi trả trong vòng 7 ngày kể từ ngày khách nhận hàng thành công, áp dụng cho các lỗi phần cứng do nhà sản xuất hoặc trường hợp giao sai quy cách mặt hàng so với đơn đặt.
2. Khách hàng gửi yêu cầu đổi trả kèm theo hóa đơn/phiếu bán hàng gốc và sản phẩm còn nguyên hộp, phụ kiện.
3. Nhân viên kỹ thuật kiểm tra thực tế tình trạng sản phẩm. Khi được chấp thuận, cửa hàng lập một **Hồ sơ đổi trả hàng** ghi rõ mã hồ sơ, đơn mua hàng gốc, sản phẩm trả, số lượng và lý do trả.
4. **Quy tắc phân loại kho bắt buộc:** Hàng hóa được nhận trả về từ khách hàng **tuyệt đối không được phép cộng ngược ngay vào số lượng hàng có sẵn để bán tiếp**. Thay vào đó, toàn bộ hàng nhận lại bắt buộc phải được nhập vào khu vực **"Hàng chờ kiểm tra kỹ thuật"**. Tại đây, kỹ thuật viên sẽ tiến hành kiểm định chuyên sâu:
   - Nếu sản phẩm còn nguyên vẹn 100%, lỗi nhỏ do cấu hình phần mềm hoặc khách đổi ý khi chưa bóc seal: sau khi có biên bản thẩm định đạt yêu cầu, quản lý mới ký duyệt chuyển sản phẩm từ nhóm "Chờ kiểm tra" sang nhóm "Đủ điều kiện bán".
   - Nếu sản phẩm bị lỗi phần cứng xác thực: sản phẩm được chuyển sang nhóm "Hàng lỗi chờ đổi trả nhà cung cấp".
5. Xử lý quyền lợi cho khách hàng:
   - Nếu khách hàng chọn đổi sản phẩm mới: nhân viên xuất sản phẩm mới tương ứng (hoặc sản phẩm khác với giá trị tương đương/bù trừ chênh lệch) và lập một chứng từ bán hàng mới.
   - Nếu khách hàng chọn hoàn tiền: số tiền hoàn được tính toán dựa trên đơn giá thực tế đã thanh toán sau khi trừ các khoản ưu đãi giảm giá đã phân bổ trên dòng hàng đó. Tiền hoàn được chi trả trực tiếp bằng tiền mặt, chuyển khoản ngân hàng về tài khoản của khách, hoặc ghi tăng vào số dư tài khoản mua hàng nội bộ của khách theo thỏa thuận.

### 1.2.7. Quy trình nhập hàng từ nhà cung cấp và kiểm kê kho
Để duy trì nguồn hàng kinh doanh, cửa hàng nhập hàng từ các nhà cung cấp phân phối chính hãng:
1. Mỗi nhà cung cấp được quản lý bằng mã nhà cung cấp, tên công ty, thông tin người liên hệ, số điện thoại, địa chỉ và mã số thuế.
2. Khi hàng hóa từ nhà cung cấp được chuyển đến cửa hàng, nhân viên thủ kho cùng đại diện giao hàng tiến hành mở kiện, đối chiếu quy cách và kiểm đếm thực tế.
3. Nhân viên thủ kho lập một **Phiếu nhập hàng** có mã số phiếu duy nhất, ghi rõ ngày giờ nhận, nhà cung cấp, nhân viên lập phiếu và tình trạng tiếp nhận. Phiếu nhập chứa danh sách chi tiết các mặt hàng nhập, số lượng thực nhận và đơn giá nhập chốt tại thời điểm đó.
4. Sau khi các bên ký biên bản giao nhận, phiếu nhập được xác nhận hoàn tất. Lúc này hệ thống mới chính thức ghi nhận tăng số lượng hàng hóa vào nhóm "Đủ điều kiện bán" trong kho.
5. **Kiểm kê và xử lý chênh lệch kho:** Định kỳ hàng tháng hoặc đột xuất, cửa hàng tổ chức các đợt kiểm kê thực tế từng mặt hàng theo từng vị trí lưu trữ. Nhân viên kiểm kê đếm số lượng thực tế và đối chiếu với số liệu theo dõi trên hệ thống. Nếu phát hiện chênh lệch (do thất thoát, hư hỏng trong bảo quản, nhầm lẫn mã hàng), nhân viên lập biên bản kiểm kê và đề xuất điều chỉnh kho. Chỉ khi người quản lý cửa hàng phê duyệt biên bản đề nghị, số lượng hàng hóa trong kho mới được điều chỉnh tương ứng kèm lý do giải trình cụ thể.

---

## 1.3. Giới hạn phạm vi nghiên cứu của đề tài

Để đảm bảo tính khả thi và tập trung sâu vào nội dung lý thuyết chuẩn hóa cơ sở dữ liệu nâng cao, đề tài xác định phạm vi nghiên cứu như sau:
1. **Phạm vi không gian:** Đề tài tập trung phân tích mô hình quản lý cho **một cửa hàng bán lẻ PowerTech độc lập**, chưa mở rộng sang bài toán chuỗi nhiều chi nhánh phân tán theo vùng miền.
2. **Phạm vi nghiệp vụ:** Trọng tâm đặt vào dòng vận động của hàng hóa, tiền tệ và thông tin khách hàng xoay quanh các hoạt động: Nhập hàng - Quản lý tồn kho theo tình trạng - Bán lẻ tại quầy - Bán hàng trực tuyến - Giao nhận - Bảo hành - Đổi trả hàng.
3. **Phạm vi loại trừ:** Các nghiệp vụ kế toán tài chính chuyên sâu (khấu hao tài sản, báo cáo tài chính, tính lương nhân viên theo doanh số) và các thuật toán trí tuệ nhân tạo gợi ý sản phẩm không thuộc phạm vi xử lý trực tiếp của lược đồ cơ sở dữ liệu này.
