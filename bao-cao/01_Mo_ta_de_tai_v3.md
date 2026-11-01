# MỤC 1. MÔ TẢ ĐỀ TÀI VÀ XÁC ĐỊNH LĨNH VỰC CẦN TIN HỌC HÓA

## 1.1. Bối cảnh đề tài và lĩnh vực cần tin học hóa

PowerTech là cửa hàng bán lẻ linh kiện máy tính và thiết bị công nghệ. Cửa hàng bán bộ vi xử lý, bo mạch chủ, bộ nhớ RAM, card đồ họa, ổ cứng, nguồn máy tính, vỏ máy, màn hình, bàn phím, chuột, tai nghe, loa, thiết bị mạng, phụ kiện, phần mềm bản quyền, máy tính xách tay và máy tính bộ lắp sẵn. Cửa hàng có một điểm bán kèm kho, đồng thời nhận đơn qua trang web riêng, qua điện thoại và tin nhắn.

Hàng của PowerTech chủ yếu được nhập từ các nhà phân phối và đại lý chính hãng. Việc bảo hành do hãng hoặc nhà phân phối thực hiện; PowerTech là nơi bán hàng, ghi nhận thông tin mua, tiếp nhận sản phẩm lỗi, gửi đi bảo hành và trả lại cho khách.

Công việc của cửa hàng gặp những khó khăn đặc thù sau:

1. **Hàng nhiều thông số, giá trị cao.** Mỗi loại linh kiện có thông số riêng và phải phù hợp với linh kiện khác (loại chân cắm của bộ vi xử lý và bo mạch chủ, loại RAM, công suất nguồn). Nhiều mặt hàng có số seri riêng từng chiếc để hãng nhận biết khi bảo hành.
2. **Giá thay đổi thường xuyên.** Giá niêm yết, giá khuyến mãi và giá nhập thay đổi theo thị trường và theo từng đợt nhập. Cửa hàng cần biết rõ mỗi lần bán hoặc nhập đã dùng mức giá nào.
3. **Một kho cho nhiều kênh bán.** Hàng trong kho phải phục vụ khách mua tại quầy và khách đặt qua trang web, điện thoại. Nếu không giữ hàng cho đơn đã nhận thì dễ bán trùng: hẹn giao cho khách đặt từ xa nhưng hàng đã bán cho người đến mua tại quầy.
4. **Hàng đã mở hộp không bán lại như hàng mới.** Sản phẩm khách trả lại hoặc gửi bảo hành phải được kiểm tra trước khi quyết định bán lại, trả nhà cung cấp hay xử lý khác. Ghi chép bằng sổ tay hoặc sổ sách rời rạc dễ nhầm giữa hàng mới, hàng chờ kiểm tra và hàng lỗi.
5. **Bảo hành kéo dài và qua nhiều bên.** Thời hạn bảo hành từ 12 tháng đến 36 tháng với phần lớn mặt hàng, có dòng RAM, ổ cứng 5 năm và nguồn đến 10 năm. Sản phẩm gửi hãng có thể mất từ vài ngày đến khoảng một tháng; cửa hàng phải theo dõi sản phẩm của từng khách đang ở đâu và hẹn trả khi nào.

Vì vậy, lĩnh vực cần tin học hóa của đề tài là **quản lý hoạt động kinh doanh bán lẻ linh kiện máy tính và thiết bị công nghệ của PowerTech**, gồm: danh mục hàng hóa và thông số kỹ thuật; hồ sơ khách hàng, nhân viên và nhà cung cấp; bán tại quầy và bán từ xa; thanh toán, đặt cọc và hoàn tiền; giao hàng; nhập hàng và theo dõi hàng trong kho theo tình trạng; tiếp nhận bảo hành; đổi trả hàng.

---

## 1.2. Mô tả chi tiết các hoạt động của cửa hàng

### 1.2.1. Hàng hóa, ảnh và thông số kỹ thuật
Cửa hàng chia hàng theo loại hàng và thương hiệu. Các loại hàng có thể phân cấp, ví dụ nhóm lớn "Linh kiện máy tính" gồm các nhóm nhỏ "Bộ nhớ RAM", "Ổ cứng"; mỗi loại chỉ có một loại cha. Loại hàng và thương hiệu đều có mã riêng, tên và phần mô tả. Hai thương hiệu hoặc hai loại hàng có thể trùng tên gọi nên tên không dùng để phân biệt.

Mỗi mặt hàng có một mã nội bộ và một mã hàng thương mại (SKU) không trùng với mặt hàng nào khác, kèm tên, mô tả, giá niêm yết, giá khuyến mãi nếu đang áp dụng, thời hạn bảo hành tính theo tháng (phần mềm bản quyền không có bảo hành phần cứng) và tình trạng đang kinh doanh hay đã ngừng. Mỗi mặt hàng thuộc đúng một loại và một thương hiệu. Giá niêm yết và giá khuyến mãi thay đổi theo thị trường; thay đổi giá không làm đổi các đơn đã lập.

Mỗi mặt hàng có nhiều ảnh minh họa. Vị trí ảnh trong cùng một mặt hàng không được trùng nhau, và mặt hàng đang bán có một ảnh đại diện chính. Mỗi loại hàng quy định các thông số riêng, ví dụ dung lượng, tốc độ, công suất, chuẩn kết nối; mỗi thông số có tên, kiểu giá trị (chữ, số, có/không) và đơn vị nếu có. Mỗi mặt hàng có tối đa một giá trị cho một thông số của loại hàng mình thuộc về. Thêm hoặc đổi ảnh không làm đổi thông số của mặt hàng.

**Số seri.** Những mặt hàng thường có số seri riêng từng chiếc (bộ vi xử lý, bo mạch chủ, card đồ họa, ổ cứng, nguồn, màn hình, máy tính xách tay, máy tính bộ) được ghi số seri của từng chiếc khi nhập và khi bán. Các món nhỏ như cáp, tản nhiệt, phụ kiện chỉ theo dõi theo dòng hàng và chứng từ mua.

### 1.2.2. Nhân viên và khách hàng
Cửa hàng có các nhân viên tư vấn bán hàng, thu ngân kiêm thủ quỹ, nhân viên kỹ thuật, nhân viên kho, nhân viên giao hàng, nhân viên chăm sóc khách hàng và người quản lý. Mỗi nhân viên có mã, họ tên, số điện thoại và tình trạng làm việc. Cửa hàng nhỏ nên một nhân viên thường kiêm nhiều việc, ví dụ vừa bán hàng vừa phụ trách kho. Người quản lý duyệt việc điều chỉnh số lượng hàng sau kiểm kê, duyệt việc hoàn tiền và quyết định bán lại hàng trả về.

Khách hàng được lưu với mã khách hàng, họ tên và số điện thoại; email có thể có hoặc không. Họ tên, số điện thoại hay email không đủ để phân biệt hai khách vì có thể trùng hoặc thay đổi.

- **Khách mua tại quầy.** Cửa hàng đề nghị khách để lại họ tên và số điện thoại để tra cứu bảo hành khi mất phiếu và để tư vấn nâng cấp sau này. Khách không để lại vẫn được bán hàng; khi cần bảo hành, cửa hàng đối chiếu bằng chứng từ mua và số seri còn lưu trong sổ bán hàng.
- **Khách có tài khoản trên trang web.** Khách đăng ký tài khoản bằng số điện thoại hoặc email, có thể lưu nhiều địa chỉ nhận hàng; mỗi địa chỉ ghi tên người nhận, số điện thoại và địa chỉ chi tiết, và tại mỗi thời điểm chỉ có tối đa một địa chỉ mặc định. Một tài khoản gắn với tối đa một khách hàng.
- **Khách mua tại quầy rồi đăng ký tài khoản.** Khi khách đăng ký bằng đúng số điện thoại đã để lại ở quầy, cửa hàng chỉ nối hồ sơ cũ vào tài khoản sau khi khách xác nhận bằng mã gửi về số điện thoại đó. Sau khi nối, khách xem được lịch sử mua và thời hạn bảo hành còn lại của từng sản phẩm.

### 1.2.3. Bán hàng trực tiếp tại quầy
Khách đến cửa hàng được nhân viên tư vấn chọn linh kiện hoặc cấu hình phù hợp, có kiểm tra sự tương thích giữa các linh kiện. Khách mua nhiều linh kiện để lắp một máy có thể nhờ cửa hàng lắp ráp và chạy thử theo cấu hình đã chọn; bảo hành vẫn tính theo từng linh kiện. Khi khách đồng ý mua:

1. Nhân viên lập phiếu bán hàng ghi thời điểm bán, nhân viên bán, khách (nếu có), từng dòng hàng với số thứ tự dòng, mặt hàng, số lượng, đơn giá bán thực tế và số seri đối với hàng có seri. Một mặt hàng có thể xuất hiện ở nhiều dòng nếu giá hoặc điều kiện bán khác nhau (ví dụ một chiếc bán giá khuyến mãi, một chiếc bán giá thường).
2. Tổng tiền phải trả bằng tổng tiền các dòng trừ khoản giảm giá (nếu có); tiền tính bằng đồng Việt Nam, làm tròn đến một đồng.
3. Khách trả tiền tại quầy thu ngân bằng tiền mặt, chuyển khoản qua mã QR ngân hàng hoặc quẹt thẻ ngân hàng. Trả tiền khi nhận hàng không áp dụng tại quầy. Mua trả góp qua công ty tài chính không thuộc phạm vi đề tài.
4. Nhân viên lấy hàng từ kho, **kiểm tra ngoại quan và niêm phong ngay trước mặt khách**. Với máy tính xách tay, màn hình, máy tính bộ, nhân viên bật máy chạy thử trước khi giao. Với linh kiện còn niêm phong, nhân viên chỉ mở hộp chạy thử khi khách yêu cầu, vì hàng đã mở hộp không thể bán lại như hàng mới.
5. Nhân viên dán tem bảo hành của cửa hàng lên hộp hoặc vị trí không che tem của hãng, rồi giao hàng cùng phiếu bán hàng kiêm phiếu bảo hành. Khách là doanh nghiệp cần hóa đơn giá trị gia tăng thì cung cấp mã số thuế khi mua; cửa hàng cấp hóa đơn theo quy định về hóa đơn bán lẻ.
6. Giao dịch hoàn tất ngay tại quầy; số lượng hàng được trừ khỏi kho cùng lúc.

Khách muốn đặt trước mặt hàng đang hết hoặc máy tính lắp theo cấu hình riêng thì xử lý theo mục 1.2.5 (đặt cọc).

### 1.2.4. Bán hàng từ xa: đặt hàng, xác nhận và giữ hàng
1. **Kênh đặt hàng.** Khách đặt trên trang web của cửa hàng, hoặc gọi điện, nhắn tin để nhân viên lập đơn thay. Trên trang web, khách chọn hàng vào giỏ (mỗi mặt hàng chỉ có một dòng trong giỏ), được xem hàng khi chưa có tài khoản nhưng phải có tài khoản để gửi đơn.
2. **Gửi đơn và hủy đơn.** Đơn mới ở tình trạng chờ xác nhận. Khách tự hủy được khi cửa hàng chưa xác nhận; sau đó muốn hủy phải báo cửa hàng để xử lý theo mục 1.2.6.
3. **Xác nhận đơn.** Nhân viên bán hàng kiểm tra số lượng hàng đủ điều kiện bán, gọi điện xác nhận hàng, địa chỉ và cách thanh toán với khách. Nếu thiếu hàng, nhân viên báo khách để đổi hàng, chờ hàng hoặc hủy. Khi đã xác nhận, nhân viên **giữ hàng** cho đơn. Số lượng có thể nhận thêm đơn mới bằng số hàng đủ điều kiện bán trừ số đang giữ; hàng đang giữ vẫn nằm trong kho cho đến khi giao.
4. **Nội dung đơn.** Đơn có mã và số đơn không trùng, ghi ngày giờ lập, kênh bán (quầy, trang web, điện thoại hoặc tin nhắn), khách, tên người nhận, số điện thoại, địa chỉ giao và từng dòng hàng như phiếu bán tại quầy. Tên hàng, giá và thông tin người nhận được chốt khi cửa hàng xác nhận đơn; thay đổi giá hoặc địa chỉ về sau không sửa đơn cũ. Muốn đổi hàng hoặc số lượng trước khi giao, cửa hàng phải được khách đồng ý và ghi lại nội dung trước và sau.
5. **Tình trạng đơn.** Đơn đi qua các tình trạng: chờ xác nhận, đã xác nhận, đang chuẩn bị, đang giao, hoàn tất hoặc đã hủy.
6. **Mã giảm giá.** Mỗi đơn dùng tối đa một mã. Mã có tên chương trình, loại giảm (theo phần trăm hoặc theo số tiền) và mức giảm, thời gian áp dụng, giá trị đơn tối thiểu, mức giảm tối đa nếu có và số lượt dùng tối đa. Cửa hàng kiểm tra điều kiện của mã khi xác nhận đơn và chỉ giảm trên tiền hàng, không giảm phí giao. Tổng phải trả bằng tiền hàng trừ giảm giá cộng phí giao hàng.

### 1.2.5. Thanh toán và đặt cọc
1. **Cách trả tiền.** Khách trả trước bằng chuyển khoản ngân hàng, mã QR, ví điện tử hoặc cổng thanh toán trực tuyến, hoặc trả khi nhận hàng (COD). Chuyển khoản do nhân viên đối chiếu với đơn rồi mới xác nhận đã nhận tiền. Một đơn có thể có nhiều lần thanh toán, kể cả cọc và phần còn lại; mỗi lần ghi phương thức, số tiền, thời điểm, kết quả và người xác nhận. Lần chuyển không thành công không được tính là đã thu.
2. **Hạn trả trước.** Đơn trả trước chỉ được giao khi đã thu đủ. Đơn trả trước không thu đủ trong 24 giờ kể từ lúc xác nhận thì hủy, hàng đang giữ được trả về kho, khoản đã thu được hoàn lại.
3. **Đặt cọc.** Hàng không có sẵn trong kho, hàng cần đặt từ nhà cung cấp, máy tính lắp theo yêu cầu riêng và một số mặt hàng giá trị lớn chỉ được giữ khi khách đặt cọc một phần giá trị. Mức cọc do hai bên thỏa thuận và ghi trên phiếu đặt hàng; cửa hàng công bố điều kiện này cho khách trước khi nhận cọc. Tiền cọc được trừ vào tổng thanh toán khi nhận hàng. Nếu cửa hàng không có được hàng thì hoàn đủ tiền cọc; nếu khách tự hủy thì xử lý tiền cọc theo điều kiện đã ghi trên phiếu.
4. **Đơn trả sau.** Đơn giá trị lớn mà khách chọn trả khi nhận hàng, hoặc khách từng bỏ đơn, có thể bị yêu cầu đặt cọc hoặc trả trước.

### 1.2.6. Giao hàng
1. **Xuất hàng.** Nhân viên kho lấy đúng hàng đang giữ, ghi số seri hàng có seri, kiểm tra và đóng gói niêm phong, bàn giao cho nhân viên giao hàng cùng phiếu giao. Lúc này việc giữ hàng kết thúc và số lượng được trừ khỏi kho.
2. **Phí và thời gian giao.** Phí giao tính theo khu vực và giá trị đơn theo biểu phí niêm yết; đơn giá trị lớn trong nội thành thường được miễn phí. Đơn nội thành thường giao trong 1 đến 2 ngày làm việc. Cửa hàng tự giao trong nội thành; khu vực xa chuyển qua đơn vị vận chuyển, nhưng đề tài chỉ xét ghi nhận kết quả giao.
3. **Nhận hàng.** Người giao gọi báo trước khi đến. Khách kiểm tra bên ngoài, niêm phong và số seri trước khi nhận, và được khuyến khích quay video khi mở hộp để làm bằng chứng. Hộp rách, móp, ướt hoặc mất niêm phong thì khách có quyền từ chối nhận; đơn được hoàn về kho và hủy.
4. **Thu tiền khi giao.** Với đơn COD, người giao thu tiền, ghi số tiền đã thu và nộp về thủ quỹ; nhân viên bán hàng hoặc người quản lý xác nhận khoản thu.
5. **Giao không thành công.** Nếu khách vắng hoặc từ chối nhận, người giao ghi lý do. Mỗi đơn được thử giao tối đa 3 lần. Sau 3 lần không thành công, đơn bị hủy, hàng được mang về kho, hàng đang giữ và lượt dùng mã giảm giá được trả lại. Khách bỏ đơn từ lần thứ hai trở đi chỉ được bán khi trả trước.
6. **Hoàn tất và hủy.** Đơn hoàn tất khi khách đã nhận hàng và tiền phải thu đã được xác nhận đủ. Hủy trước khi xuất hàng thì chỉ cần trả lại hàng đang giữ và lượt mã giảm giá. Hủy sau khi xuất hàng thì hàng phải được mang về kho; chỉ khi cửa hàng nhận lại hàng thực tế mới ghi nhận hàng vào kho, theo mục 1.2.8.

### 1.2.7. Tiếp nhận và xử lý bảo hành
Bảo hành linh kiện do hãng hoặc nhà phân phối chịu trách nhiệm theo thời hạn đã ghi trên mặt hàng. PowerTech là đầu mối tiếp nhận. Chính sách bảo hành được niêm yết tại quầy và trên trang web.

1. Khi bán, sản phẩm được dán tem bảo hành của cửa hàng và, với hàng có seri, được ghi số seri vào phiếu bán hàng. Thời hạn bảo hành tính từ ngày mua và được chốt theo chứng từ mua, không đổi khi cửa hàng sau này đổi chính sách.
2. Khi sản phẩm lỗi trong thời hạn bảo hành, khách mang đến cửa hàng, gửi qua đơn vị vận chuyển hoặc tự mang đến trung tâm bảo hành của hãng. Chi phí sửa chữa và vận chuyển sản phẩm bảo hành do cửa hàng chịu, không thu của khách.
3. Nhân viên kỹ thuật kiểm tra: còn trong thời hạn; có thông tin mua của cửa hàng; số seri trùng với chứng từ mua; tem còn nguyên, không rách hoặc tẩy xóa; sản phẩm không bị rơi vỡ, vào nước, cháy nổ do sử dụng sai hoặc đã bị người khác tháo sửa; còn đủ phụ kiện đi kèm nếu bảo hành theo bộ. Dữ liệu lưu trong ổ cứng không thuộc phạm vi bảo hành; khách tự sao lưu trước khi gửi.
4. Nếu đủ điều kiện, nhân viên lập **phiếu tiếp nhận bảo hành**: mã phiếu, khách, sản phẩm và số seri, chứng từ mua gốc, mô tả lỗi, phụ kiện đi kèm, ngày nhận và ngày hẹn trả. Thời gian hẹn trả ghi trên phiếu; thường từ 7 đến 30 ngày tùy hãng và loại hàng. Nếu không đủ điều kiện, nhân viên ghi lý do từ chối và trả sản phẩm cho khách.
5. Kỹ thuật viên kiểm tra lỗi. Có thể sửa tại cửa hàng nếu nhà sản xuất cho phép, hoặc gửi sản phẩm cho hãng hoặc nhà phân phối. Mỗi bước gửi đi, nhận về và kết quả được ghi vào phiếu. Nếu kiểm tra không thấy lỗi, sản phẩm được trả lại cho khách. Trong thời gian chờ, cửa hàng có thể cho khách mượn sản phẩm tương tự nếu còn hàng.
6. Thời gian sản phẩm nằm ở bảo hành không tính vào thời hạn bảo hành. Nếu thay linh kiện hoặc đổi sản phẩm mới thì thời hạn bảo hành được tính lại từ ngày giao sản phẩm mới.
7. Nếu hết thời hạn hẹn mà sản phẩm vẫn không sửa được, hoặc đã bảo hành từ 3 lần mà lỗi vẫn còn, cửa hàng đổi sản phẩm mới tương tự hoặc thu hồi và hoàn tiền cho khách.
8. Khi có kết quả, nhân viên báo khách đến nhận, cùng khách kiểm tra rồi ký biên bản trả bảo hành.

### 1.2.8. Đổi trả hàng, hoàn tiền và hàng trong kho
**Ba trường hợp đổi trả.** Cửa hàng áp dụng:
- **Giao sai, thiếu, hư hỏng bên ngoài.** Hàng không đúng mẫu so với đơn, thiếu phụ kiện hoặc quà tặng, hộp rách, vỡ khi giao: khách báo trong 48 giờ kể từ khi nhận. Cửa hàng đổi lại hoặc hoàn tiền và chịu chi phí vận chuyển.
- **Sản phẩm lỗi do nhà sản xuất.** Đổi sản phẩm mới cùng loại trong 30 ngày kể từ ngày mua đối với linh kiện và gaming gear, trong 7 ngày đối với máy tính xách tay và màn hình. Sản phẩm phải còn như mới, hộp không hư hại và đủ phụ kiện. Nếu hết hàng cùng loại thì đổi sang sản phẩm tương đương hoặc hoàn tiền. Quá thời hạn này thì xử lý theo bảo hành ở mục 1.2.7.
- **Khách đổi ý, sản phẩm không lỗi.** Chỉ nhận lại trong 7 ngày nếu sản phẩm còn nguyên niêm phong, chưa mở hộp, đủ phụ kiện. Khách chịu chi phí vận chuyển và cửa hàng có thể thu một khoản phí xử lý theo thông báo niêm yết. Sản phẩm đã mở hộp hoặc đã lắp vào máy không nhận trả. Phần mềm bản quyền đã kích hoạt không đổi trả.

**Quy trình.**
1. Khách mang hóa đơn hoặc phiếu bán gốc đến. Khách mua tại quầy mà không để lại thông tin phải có chứng từ mua. Nhân viên kỹ thuật kiểm tra sản phẩm.
2. Nếu được chấp nhận, cửa hàng lập **hồ sơ đổi trả**: mã hồ sơ, đơn gốc, người đề nghị, ngày, lý do, và từng dòng hàng cùng số lượng trả. Một đơn có thể được trả nhiều lần, miễn tổng số lượng trả không vượt số đã giao.
3. **Hàng nhận lại không bán ngay.** Mọi sản phẩm nhận về được đưa vào nhóm **chờ kiểm tra**. Cửa hàng chia hàng trong kho thành ba nhóm: *đủ điều kiện bán*, *chờ kiểm tra* và *không bán được, chờ xử lý*. Chỉ nhóm đủ điều kiện bán mới được bán.
4. Kỹ thuật viên kiểm tra. Nếu hàng còn nguyên niêm phong, không lỗi, người quản lý duyệt chuyển sang nhóm đủ điều kiện bán. Nếu hàng đã mở hộp nhưng không lỗi, người quản lý quyết định bán lại dưới dạng hàng đã mở hộp với giá giảm và ghi rõ trên phiếu bán, hoặc để ở nhóm chờ xử lý. Nếu hàng lỗi thật, chuyển sang nhóm không bán được và gửi trả nhà cung cấp theo mục 1.2.9. Việc chuyển nhóm không làm tăng tổng số hàng thực tế trong kho.
5. **Hoàn tiền và đổi hàng.** Khách đổi sang sản phẩm khác: cửa hàng lập đơn bán mới và tính chênh lệch. Khách muốn hoàn tiền: người quản lý duyệt; số tiền hoàn bằng giá đã trả của dòng hàng đó trừ phần giảm giá đã chia cho dòng, trừ phí xử lý nếu có. Tiền hoàn trả theo phương thức khách đã trả, hoặc theo thỏa thuận có thể cộng vào số dư tài khoản mua hàng của khách. Mỗi khoản hoàn gắn với khoản thu gốc; có thể hoàn nhiều lần nhưng tổng không vượt số tiền đã thu.

### 1.2.9. Nhập hàng, kiểm kê và trả hàng nhà cung cấp
1. Nhà cung cấp (nhà phân phối, đại lý chính hãng) có mã, tên công ty, người liên hệ, số điện thoại, địa chỉ, mã số thuế và tình trạng hợp tác. Tên công ty và thông tin liên hệ có thể trùng nên không dùng để phân biệt. Một nhà cung cấp giao nhiều mặt hàng và một mặt hàng có thể nhập từ nhiều nhà cung cấp.
2. Khi hàng về, nhân viên kho cùng người giao mở kiện, đối chiếu với đơn đặt và hóa đơn của nhà cung cấp, đếm số lượng, kiểm tra ngoại quan và ghi số seri hàng có seri.
3. Nhân viên kho lập **phiếu nhập**: mã phiếu và số phiếu không trùng, nhà cung cấp, người lập, thời điểm nhận, tình trạng; các dòng ghi số dòng, mặt hàng, số lượng thực nhận và giá nhập. Mỗi phiếu là một lần nhận hàng thực tế và phải có ít nhất một dòng. Cùng một mặt hàng có thể ở nhiều dòng nếu khác giá hoặc khác lô.
4. Sau khi hai bên ký biên bản giao nhận, phiếu được xác nhận và hàng được ghi tăng vào nhóm đủ điều kiện bán, **chỉ một lần**. Hàng nhập về có lỗi hoặc thiếu được lập biên bản và ghi vào nhóm chờ xử lý. Việc thanh toán tiền cho nhà cung cấp và công nợ thuộc phần kế toán, không thuộc phạm vi đề tài.
5. **Trả hàng nhà cung cấp.** Hàng lỗi từ khách trả và hàng khách gửi bảo hành được cửa hàng gửi cho nhà cung cấp hoặc hãng. Cửa hàng ghi ngày gửi, ngày nhận kết quả (đổi hàng mới, sửa xong hoặc ghi giảm tiền) và nhập hàng đổi về theo phiếu nhập.
6. **Số lượng ban đầu và kiểm kê.** Khi bắt đầu quản lý, số lượng từng mặt hàng được ghi nhận bằng một lần kiểm kê đầu kỳ có biên bản. Sau đó, hằng tháng hoặc đột xuất, nhân viên đếm hàng thực tế theo từng mặt hàng và so với sổ. Số lượng thực tế khác sổ (thất thoát, hư hỏng, nhầm mã) thì nhân viên lập biên bản đề nghị điều chỉnh, ghi lý do. Chỉ khi người quản lý duyệt, số lượng mới được điều chỉnh.
7. Mọi lần hàng vào hoặc ra kho (nhập, bán, giao, trả, chuyển nhóm, điều chỉnh) được ghi lại với mặt hàng, số lượng, thời điểm, người thực hiện và chứng từ gốc.

---

## 1.3. Giới hạn phạm vi nghiên cứu của đề tài

1. **Không gian:** một cửa hàng PowerTech độc lập, một kho; số lượng hàng được theo dõi theo mặt hàng và theo tình trạng, chưa theo vị trí kệ hay nhiều chi nhánh.
2. **Nghiệp vụ:** nhập hàng; hàng trong kho theo tình trạng; bán tại quầy; bán từ xa và đặt cọc; thanh toán và hoàn tiền; giao hàng; bảo hành; đổi trả; trả hàng nhà cung cấp.
3. **Loại trừ:** kế toán và thuế chuyên sâu (công nợ, báo cáo tài chính, tính lương theo doanh số); trả góp qua công ty tài chính; bán buôn cho đại lý; chương trình khách hàng thân thiết (hạng thành viên, điểm thưởng); đánh giá sản phẩm và hỗ trợ khách ngoài bảo hành, đổi trả; thu mua thiết bị cũ; quy trình lắp ráp chi tiết và bảo hành cả bộ máy; việc đơn vị vận chuyển bên ngoài xử lý hàng ngoài khu vực giao của cửa hàng.
