# MỤC 1. MÔ TẢ ĐỀ TÀI VÀ XÁC ĐỊNH LĨNH VỰC CẦN TIN HỌC HÓA

## 1.1. Bối cảnh đề tài và lĩnh vực cần tin học hóa

PowerTech là cửa hàng bán lẻ linh kiện máy tính và thiết bị công nghệ: bộ vi xử lý, bo mạch chủ, bộ nhớ RAM, card đồ họa, ổ cứng, nguồn máy tính, vỏ máy, tản nhiệt, màn hình, máy tính xách tay, máy tính bộ lắp sẵn và các thiết bị ngoại vi. Cửa hàng có một điểm bán kèm kho, đồng thời nhận đặt hàng qua trang web riêng của cửa hàng.

Hàng của PowerTech chủ yếu được nhập từ các nhà phân phối và đại lý chính hãng. Việc bảo hành do hãng hoặc nhà phân phối thực hiện; PowerTech là nơi bán hàng, ghi nhận thông tin mua, tiếp nhận sản phẩm lỗi, gửi đi bảo hành và trả lại cho khách.

Công việc của cửa hàng gặp những khó khăn đặc thù sau:

1. **Hàng nhiều thông số, giá trị cao.** Mỗi loại linh kiện có thông số riêng và phải phù hợp với linh kiện khác (loại chân cắm của bộ vi xử lý và bo mạch chủ, loại RAM, công suất nguồn). Nhiều mặt hàng có số seri riêng từng chiếc để hãng nhận biết khi bảo hành.
2. **Giá thay đổi thường xuyên.** Giá niêm yết, giá khuyến mãi và giá nhập thay đổi theo thị trường và theo từng đợt nhập. Cửa hàng cần biết rõ mỗi lần bán hoặc nhập đã dùng mức giá nào.
3. **Một kho cho hai kênh bán.** Hàng trong kho phải phục vụ cả khách mua tại quầy lẫn khách đặt qua mạng. Nếu không giữ hàng cho đơn đã nhận thì dễ bán trùng: hẹn giao cho khách đặt qua mạng nhưng hàng đã bán cho người đến mua tại quầy.
4. **Hàng đã mở hộp không bán lại như hàng mới.** Sản phẩm khách trả lại hoặc gửi bảo hành phải được kiểm tra trước khi quyết định bán lại, trả nhà cung cấp hay xử lý khác. Ghi chép bằng sổ tay hoặc sổ sách rời rạc dễ nhầm giữa hàng mới, hàng chờ kiểm tra và hàng lỗi.
5. **Bảo hành kéo dài và qua nhiều bên.** Thời hạn bảo hành thường từ 12 đến 36 tháng, có dòng hàng dài hơn. Sản phẩm gửi hãng có thể mất từ vài ngày đến khoảng một tháng, cửa hàng phải theo dõi sản phẩm của từng khách đang ở đâu và hẹn trả khi nào.

Vì vậy, lĩnh vực cần tin học hóa của đề tài là **quản lý hoạt động kinh doanh bán lẻ linh kiện máy tính và thiết bị công nghệ của PowerTech**, gồm: danh mục hàng hóa và thông số kỹ thuật; hồ sơ khách hàng, nhân viên và nhà cung cấp; bán tại quầy và bán qua mạng; thanh toán, đặt cọc và hoàn tiền; giao hàng; nhập hàng và theo dõi hàng trong kho theo tình trạng; tiếp nhận bảo hành; đổi trả hàng.

---

## 1.2. Mô tả chi tiết các hoạt động của cửa hàng

### 1.2.1. Hàng hóa, ảnh và thông số kỹ thuật
Cửa hàng chia hàng theo loại hàng và thương hiệu. Các loại hàng có thể phân cấp, ví dụ nhóm lớn "Linh kiện máy tính" gồm các nhóm nhỏ "Bộ nhớ RAM", "Ổ cứng SSD"; mỗi loại chỉ có một loại cha. Loại hàng và thương hiệu đều có mã riêng, tên và phần mô tả. Hai thương hiệu hoặc hai loại hàng có thể trùng tên gọi nên tên không dùng để phân biệt.

Mỗi mặt hàng có một mã nội bộ và một mã hàng thương mại (SKU) không trùng với mặt hàng nào khác, kèm tên, mô tả, giá niêm yết, giá khuyến mãi nếu đang áp dụng, thời hạn bảo hành tính theo tháng và tình trạng đang kinh doanh hay đã ngừng. Mỗi mặt hàng thuộc đúng một loại và một thương hiệu. Giá niêm yết và giá khuyến mãi thay đổi theo thị trường; thay đổi giá không làm đổi các đơn đã lập.

Mỗi mặt hàng có nhiều ảnh minh họa. Vị trí ảnh trong cùng một mặt hàng không được trùng nhau, và mặt hàng đang bán có một ảnh đại diện chính. Mỗi loại hàng quy định các thông số riêng, ví dụ dung lượng, tốc độ, công suất, chuẩn kết nối; mỗi thông số có tên, kiểu giá trị (chữ, số, có/không) và đơn vị nếu có. Mỗi mặt hàng có tối đa một giá trị cho một thông số của loại hàng mình thuộc về. Thêm hoặc đổi ảnh không làm đổi thông số của mặt hàng.

**Số seri.** Những mặt hàng thường có số seri riêng từng chiếc (bộ vi xử lý, bo mạch chủ, card đồ họa, ổ cứng, nguồn, màn hình, máy tính xách tay, máy tính bộ) được ghi số seri của từng chiếc khi nhập và khi bán. Các món nhỏ như cáp, tản nhiệt, phụ kiện chỉ theo dõi theo dòng hàng và chứng từ mua.

### 1.2.2. Nhân viên và khách hàng
Cửa hàng có các nhân viên tư vấn bán hàng, thu ngân kiêm thủ quỹ, nhân viên kỹ thuật, nhân viên kho, nhân viên giao hàng, nhân viên chăm sóc khách hàng và người quản lý. Mỗi nhân viên có mã, họ tên, số điện thoại và tình trạng làm việc. Một nhân viên có thể kiêm nhiệm nhiều việc. Người quản lý duyệt việc điều chỉnh số lượng hàng sau kiểm kê, duyệt việc hoàn tiền và quyết định bán lại hàng trả về.

Khách hàng được lưu với mã khách hàng, họ tên và số điện thoại; email có thể có hoặc không. Họ tên, số điện thoại hay email không đủ để phân biệt hai khách vì có thể trùng hoặc thay đổi.

- **Khách mua tại quầy.** Cửa hàng đề nghị khách để lại họ tên và số điện thoại để tra cứu bảo hành khi mất phiếu và để tư vấn nâng cấp sau này. Khách không để lại vẫn được bán hàng; khi cần bảo hành, cửa hàng đối chiếu bằng chứng từ mua và số seri còn lưu trong sổ bán hàng.
- **Khách có tài khoản trên trang web.** Khách đăng ký tài khoản bằng số điện thoại hoặc email, có thể lưu nhiều địa chỉ nhận hàng; mỗi địa chỉ ghi tên người nhận, số điện thoại và địa chỉ chi tiết, và tại mỗi thời điểm chỉ có tối đa một địa chỉ mặc định. Một tài khoản gắn với tối đa một khách hàng.
- **Khách mua tại quầy rồi đăng ký tài khoản.** Khi khách đăng ký bằng đúng số điện thoại đã để lại ở quầy, cửa hàng chỉ nối hồ sơ cũ vào tài khoản sau khi khách xác nhận bằng mã gửi về số điện thoại đó. Sau khi nối, khách xem được lịch sử mua và thời hạn bảo hành còn lại của từng sản phẩm.

### 1.2.3. Bán hàng trực tiếp tại quầy
Khách đến cửa hàng được nhân viên tư vấn chọn linh kiện hoặc cấu hình phù hợp, có kiểm tra sự tương thích giữa các linh kiện. Khi khách đồng ý mua:

1. Nhân viên lập phiếu bán hàng ghi thời điểm bán, nhân viên bán, khách (nếu có), từng dòng hàng với số thứ tự dòng, mặt hàng, số lượng, đơn giá bán thực tế và số seri đối với hàng có seri. Một mặt hàng có thể xuất hiện ở nhiều dòng nếu giá hoặc điều kiện bán khác nhau (ví dụ một chiếc bán giá khuyến mãi, một chiếc bán giá thường).
2. Tổng tiền phải trả bằng tổng tiền các dòng trừ khoản giảm giá (nếu có); tiền tính bằng đồng Việt Nam, làm tròn đến một đồng.
3. Khách trả tiền tại quầy thu ngân bằng tiền mặt, chuyển khoản qua mã QR ngân hàng hoặc quẹt thẻ ngân hàng. Mua trả góp qua công ty tài chính không thuộc phạm vi đề tài.
4. Nhân viên lấy hàng từ kho, **kiểm tra ngoại quan và niêm phong ngay trước mặt khách**. Với máy tính xách tay, màn hình, máy tính bộ, nhân viên bật máy chạy thử trước khi giao. Với linh kiện còn niêm phong, nhân viên chỉ mở hộp chạy thử khi khách yêu cầu, vì hàng đã mở hộp không thể bán lại như hàng mới.
5. Nhân viên dán tem bảo hành của cửa hàng lên hộp hoặc vị trí không che tem của hãng, rồi giao hàng cùng phiếu bán hàng kiêm phiếu bảo hành. Khách là doanh nghiệp cần hóa đơn giá trị gia tăng thì cung cấp mã số thuế khi mua; cửa hàng cấp hóa đơn theo quy định về hóa đơn bán lẻ.
6. Giao dịch hoàn tất ngay tại quầy; số lượng hàng được trừ khỏi kho cùng lúc.

Khách muốn đặt trước mặt hàng đang hết hoặc máy tính lắp theo cấu hình riêng thì xử lý theo mục 1.2.4 (đặt cọc).

### 1.2.4. Bán hàng qua mạng, đặt cọc, thanh toán và giao hàng
1. Khách chọn hàng vào giỏ; mỗi mặt hàng chỉ có một dòng trong giỏ. Khách có thể xem hàng khi chưa có tài khoản nhưng phải có tài khoản để gửi đơn.
2. Khi khách gửi đơn, nhân viên bán hàng kiểm tra số lượng hàng đủ điều kiện bán, gọi điện xác nhận địa chỉ và thanh toán với khách, rồi **giữ hàng** cho đơn đó. Số lượng có thể nhận thêm đơn mới bằng số hàng đủ điều kiện bán trừ số đang giữ. Hàng đang giữ vẫn nằm trong kho cho đến khi giao.
3. Đơn có mã và số đơn không trùng, ghi ngày giờ lập, kênh bán (quầy hoặc qua mạng), khách, tên người nhận, số điện thoại, địa chỉ giao và từng dòng hàng như phiếu bán tại quầy. Tên hàng, giá và thông tin người nhận được chốt khi cửa hàng xác nhận đơn; thay đổi giá hoặc địa chỉ về sau không sửa đơn cũ. Muốn đổi hàng hoặc số lượng trước khi giao, cửa hàng phải được khách đồng ý và ghi lại nội dung trước và sau.
4. **Mã giảm giá.** Mỗi đơn dùng tối đa một mã. Mã có tên chương trình, loại giảm (theo phần trăm hoặc theo số tiền) và mức giảm, thời gian áp dụng, giá trị đơn tối thiểu, mức giảm tối đa nếu có và số lượt dùng tối đa. Cửa hàng kiểm tra điều kiện của mã khi xác nhận đơn và chỉ giảm trên tiền hàng, không giảm phí giao. Tổng phải trả bằng tiền hàng trừ giảm giá cộng phí giao hàng. Phí giao tính theo khu vực giao và giá trị đơn theo biểu phí của cửa hàng, có thể được miễn.
5. **Đặt cọc.** Hàng không có sẵn trong kho, hàng cần đặt từ nhà cung cấp và máy tính lắp theo yêu cầu riêng chỉ được giữ khi khách đặt cọc một phần giá trị; mức cọc do hai bên thỏa thuận và ghi trên phiếu đặt hàng. Tiền cọc được trừ vào tổng thanh toán khi nhận hàng. Nếu cửa hàng không có được hàng thì hoàn đủ tiền cọc; nếu khách tự hủy thì xử lý tiền cọc theo điều kiện đã ghi trên phiếu. Đơn có giá trị lớn mà khách chọn trả tiền khi nhận hàng, hoặc khách từng bỏ đơn, cũng có thể được yêu cầu đặt cọc hoặc trả trước.
6. **Thanh toán.** Khách trả trước bằng chuyển khoản ngân hàng, mã QR hoặc ví điện tử, hoặc trả khi nhận hàng (COD). Một đơn có thể có nhiều lần thanh toán, kể cả cọc và phần còn lại; mỗi lần ghi phương thức, số tiền, thời điểm, kết quả và người xác nhận. Lần chuyển không thành công không được tính là đã thu. Đơn trả trước chỉ được giao khi đã thu đủ; đơn trả trước không thu đủ trong 24 giờ kể từ lúc xác nhận thì hủy, hàng đang giữ được trả về kho, khoản đã thu được hoàn lại.
7. **Xuất hàng.** Nhân viên kho lấy đúng hàng đang giữ, ghi số seri hàng có seri, kiểm tra và đóng gói niêm phong, bàn giao cho nhân viên giao hàng cùng phiếu giao. Lúc này việc giữ hàng kết thúc và số lượng được trừ khỏi kho.
8. **Giao hàng.** Cửa hàng tự giao trong nội thành; khu vực xa chuyển qua đơn vị vận chuyển, nhưng đề tài chỉ xét ghi nhận kết quả giao. Khách được kiểm tra bên ngoài, niêm phong và số seri trước khi nhận, và được khuyến khích quay video khi mở hộp để làm bằng chứng nếu có lỗi. Với đơn COD, người giao thu tiền, ghi số tiền đã thu và nộp về thủ quỹ; nhân viên bán hàng hoặc người quản lý xác nhận khoản thu.
9. **Giao không thành công.** Nếu khách vắng hoặc từ chối nhận, người giao ghi lý do. Mỗi đơn được thử giao tối đa 3 lần. Sau 3 lần không thành công, đơn bị hủy, hàng được mang về kho, hàng đang giữ và lượt dùng mã giảm giá được trả lại. Khách bỏ đơn từ lần thứ hai trở đi chỉ được bán khi trả trước. Đơn hoàn tất khi khách đã nhận hàng và tiền phải thu đã được xác nhận đủ.
10. **Hủy đơn.** Hủy trước khi xuất hàng thì chỉ cần trả lại hàng đang giữ và lượt mã giảm giá. Hủy sau khi xuất hàng thì hàng phải được mang về kho; chỉ khi cửa hàng nhận lại hàng thực tế mới ghi nhận hàng vào kho, theo mục 1.2.6.

### 1.2.5. Tiếp nhận và xử lý bảo hành
Bảo hành linh kiện do hãng hoặc nhà phân phối chịu trách nhiệm theo thời hạn đã ghi trên mặt hàng. PowerTech là đầu mối tiếp nhận.

1. Khi bán, sản phẩm được dán tem bảo hành của cửa hàng và, với hàng có seri, được ghi số seri vào phiếu bán hàng. Thời hạn bảo hành tính từ ngày mua và được chốt theo chứng từ mua, không đổi khi cửa hàng sau này đổi chính sách.
2. Khi sản phẩm lỗi trong thời hạn bảo hành, khách mang đến cửa hàng hoặc gửi qua đơn vị vận chuyển. Nhân viên kỹ thuật kiểm tra: còn trong thời hạn; có thông tin mua của cửa hàng; số seri trùng với chứng từ mua; tem còn nguyên, không rách hoặc tẩy xóa; sản phẩm không bị rơi vỡ, vào nước, cháy nổ do sử dụng sai hoặc đã bị người khác tháo sửa; còn đủ phụ kiện đi kèm nếu bảo hành theo bộ. Dữ liệu lưu trong ổ cứng không thuộc phạm vi bảo hành; khách tự sao lưu trước khi gửi.
3. Nếu đủ điều kiện, nhân viên lập **phiếu tiếp nhận bảo hành**: mã phiếu, khách, sản phẩm và số seri, chứng từ mua gốc, mô tả lỗi, phụ kiện đi kèm, ngày nhận và ngày hẹn trả. Thời gian hẹn trả ghi trên phiếu; thường từ 7 đến 30 ngày tùy hãng và loại hàng. Nếu không đủ điều kiện, nhân viên ghi lý do từ chối và trả sản phẩm cho khách.
4. Kỹ thuật viên kiểm tra lỗi. Có thể sửa tại cửa hàng nếu nhà sản xuất cho phép, hoặc gửi sản phẩm cho hãng hoặc nhà phân phối. Mỗi bước gửi đi, nhận về và kết quả được ghi vào phiếu. Nếu kiểm tra không thấy lỗi, sản phẩm được trả lại cho khách.
5. Nếu hết thời hạn hẹn mà sản phẩm vẫn không sửa được, hoặc đã bảo hành từ 3 lần mà lỗi vẫn còn, cửa hàng đổi sản phẩm mới tương tự hoặc thu hồi và hoàn tiền cho khách.
6. Khi có kết quả, nhân viên báo khách đến nhận, cùng khách kiểm tra rồi ký biên bản trả bảo hành.

### 1.2.6. Đổi trả hàng, hoàn tiền và hàng trong kho
**Điều kiện đổi trả.** Cửa hàng áp dụng:
- Sản phẩm lỗi do nhà sản xuất hoặc giao sai hàng so với đơn: đổi sản phẩm mới cùng loại trong 30 ngày kể từ ngày mua đối với linh kiện và gaming gear, trong 7 ngày đối với máy tính xách tay và màn hình. Sản phẩm phải còn như mới, hộp không hư hại và đủ phụ kiện. Nếu hết hàng cùng loại thì đổi sang sản phẩm tương đương hoặc hoàn tiền.
- Khách đổi ý, sản phẩm không lỗi: chỉ nhận lại trong 7 ngày nếu sản phẩm còn nguyên niêm phong, chưa mở hộp, đủ phụ kiện. Cửa hàng có thể thu một khoản phí xử lý theo thông báo niêm yết. Sản phẩm đã mở hộp hoặc đã lắp vào máy không nhận trả.

**Quy trình.**
1. Khách mang hóa đơn hoặc phiếu bán gốc đến. Khách mua tại quầy mà không để lại thông tin phải có chứng từ mua. Nhân viên kỹ thuật kiểm tra sản phẩm.
2. Nếu được chấp nhận, cửa hàng lập **hồ sơ đổi trả**: mã hồ sơ, đơn gốc, người đề nghị, ngày, lý do, và từng dòng hàng cùng số lượng trả. Một đơn có thể được trả nhiều lần, miễn tổng số lượng trả không vượt số đã giao.
3. **Hàng nhận lại không bán ngay.** Mọi sản phẩm nhận về được đưa vào nhóm **chờ kiểm tra**. Cửa hàng chia hàng trong kho thành ba nhóm: *đủ điều kiện bán*, *chờ kiểm tra* và *không bán được, chờ xử lý*. Chỉ nhóm đủ điều kiện bán mới được bán. Số lượng nhận khách đặt mua mới bằng số đủ điều kiện bán trừ số đang giữ.
4. Kỹ thuật viên kiểm tra. Nếu hàng còn nguyên niêm phong, không lỗi, người quản lý duyệt chuyển sang nhóm đủ điều kiện bán. Nếu hàng đã mở hộp nhưng không lỗi, người quản lý quyết định bán lại dưới dạng hàng đã mở hộp với giá giảm và ghi rõ trên phiếu bán, hoặc để ở nhóm chờ xử lý. Nếu hàng lỗi thật, chuyển sang nhóm không bán được và gửi trả nhà cung cấp theo mục 1.2.7. Việc chuyển nhóm không làm tăng tổng số hàng thực tế trong kho.
5. **Hoàn tiền và đổi hàng.** Khách đổi sang sản phẩm khác: cửa hàng lập đơn bán mới và tính chênh lệch. Khách muốn hoàn tiền: người quản lý duyệt; số tiền hoàn bằng giá đã trả của dòng hàng đó trừ phần giảm giá đã chia cho dòng, trừ phí xử lý nếu có. Tiền hoàn trả theo phương thức khách đã trả, hoặc theo thỏa thuận có thể cộng vào số dư tài khoản mua hàng của khách. Mỗi khoản hoàn gắn với khoản thu gốc; có thể hoàn nhiều lần nhưng tổng không vượt số tiền đã thu.

### 1.2.7. Nhập hàng, kiểm kê và trả hàng nhà cung cấp
1. Nhà cung cấp (nhà phân phối, đại lý chính hãng) có mã, tên công ty, người liên hệ, số điện thoại, địa chỉ, mã số thuế và tình trạng hợp tác. Tên công ty và thông tin liên hệ có thể trùng nên không dùng để phân biệt. Một nhà cung cấp giao nhiều mặt hàng và một mặt hàng có thể nhập từ nhiều nhà cung cấp.
2. Khi hàng về, nhân viên kho cùng người giao mở kiện, đối chiếu với đơn đặt và hóa đơn của nhà cung cấp, đếm số lượng, kiểm tra ngoại quan và ghi số seri hàng có seri.
3. Nhân viên kho lập **phiếu nhập**: mã phiếu và số phiếu không trùng, nhà cung cấp, người lập, thời điểm nhận, tình trạng; các dòng ghi số dòng, mặt hàng, số lượng thực nhận và giá nhập. Mỗi phiếu là một lần nhận hàng thực tế và phải có ít nhất một dòng. Cùng một mặt hàng có thể ở nhiều dòng nếu khác giá hoặc khác lô.
4. Sau khi hai bên ký biên bản giao nhận, phiếu được xác nhận và hàng được ghi tăng vào nhóm đủ điều kiện bán, **chỉ một lần**. Hàng nhập về có lỗi hoặc thiếu được lập biên bản và ghi vào nhóm chờ xử lý. Việc thanh toán tiền cho nhà cung cấp và công nợ thuộc phần kế toán, không thuộc phạm vi đề tài.
5. **Trả hàng nhà cung cấp.** Hàng lỗi từ khách trả và hàng khách gửi bảo hành được cửa hàng gửi cho nhà cung cấp hoặc hãng. Cửa hàng ghi ngày gửi, ngày nhận kết quả (đổi hàng mới, sửa xong hoặc ghi giảm tiền) và nhập hàng đổi về theo phiếu nhập.
6. **Kiểm kê.** Hằng tháng hoặc đột xuất, nhân viên đếm hàng thực tế theo từng mặt hàng và so với sổ. Số lượng thực tế khác sổ (thất thoát, hư hỏng, nhầm mã) thì nhân viên lập biên bản đề nghị điều chỉnh, ghi lý do. Chỉ khi người quản lý duyệt, số lượng mới được điều chỉnh. Mọi lần hàng vào hoặc ra kho (nhập, bán, giao, trả, chuyển nhóm, điều chỉnh) được ghi lại với mặt hàng, số lượng, thời điểm, người thực hiện và chứng từ gốc.

---

## 1.3. Giới hạn phạm vi nghiên cứu của đề tài

1. **Không gian:** một cửa hàng PowerTech độc lập, một kho; số lượng hàng được theo dõi theo mặt hàng và theo tình trạng, chưa theo vị trí kệ hay nhiều chi nhánh.
2. **Nghiệp vụ:** nhập hàng; hàng trong kho theo tình trạng; bán tại quầy; bán qua mạng và đặt cọc; thanh toán và hoàn tiền; giao hàng; bảo hành; đổi trả; trả hàng nhà cung cấp.
3. **Loại trừ:** kế toán và thuế chuyên sâu (công nợ, báo cáo tài chính, tính lương theo doanh số); trả góp qua công ty tài chính; quy trình lắp ráp và bảo hành cả bộ máy do cửa hàng lắp; chăm sóc khách hàng thân thiết (hạng thành viên, điểm thưởng); đánh giá sản phẩm; thu mua thiết bị cũ; việc đơn vị vận chuyển bên ngoài xử lý hàng ngoài khu vực giao của cửa hàng.
