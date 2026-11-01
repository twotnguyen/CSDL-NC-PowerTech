lOMoARcPSD|56030397
CCOOSS113355--GGiiaaoo TTrriinnhh NNhhaapp MMoonn CCSSDDLL--VV22002233
NNhhậậpp mmôônn ccơơ ssởở ddữữ lliiệệuu ((HHUUTTEECCHH UUnniivveerrssiittyy ooff TTeecchhnnoollooggyy))
SSccaann ttoo ooppeenn oonn SSttuuddooccuu
SSttuuddooccuu iiss nnoott ssppoonnssoorreedd oorr eennddoorrsseedd bbyy aannyy ccoolllleeggee oorr uunniivveerrssiittyy
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
NHẬP MÔN
CƠ SỞ DỮ LIỆU
Biên soạn: Cao Tùng Anh
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
NHÂP MÔN CƠ SỞ DỮ LIỆU
Ấn bản 2023
Tài Liệu Lưu Hành Tại HUTECH www.hutech.edu.vn
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
I
MỤC LỤC
MỤC LỤC
MỤC LỤC .................................................................................................................. 1
HƯỚNG DẪN ............................................................................................................. 3
BÀI 1: TỔNG QUAN VỀ CƠ SỞ DỮ LIỆU ........................................................................ 1
1.1 HỆ CSDL DỮ LIỆU ................................................................................................ 1
1.1.1 Định nghĩa hệ CSDL ......................................................................................... 1
1.1.2 Các mức biểu diễn CSDL .................................................................................. 1
1.1.3 Đặc tính của môi trường CSDL .......................................................................... 2
1.2 HỆ QUẢN TRỊ CSDL VÀ CÁC MÔ HÌNH DỮ LIỆU .................................................... 3
1.2.1 Khái niệm Hệ Quản Trị CSDL ............................................................................ 3
1.2.2 Các thành phần của hệ quản trị CSDL ................................................................ 3
1.2.3 Các Loại mô hình dữ liệu .................................................................................. 4
BÀI TẬP ................................................................................................................. 11
BÀI 2: CƠ SỞ DỮ LIỆU QUAN HỆ ............................................................................... 12
2.1 CÁC KHÁI NIỆM CƠ BẢN ................................................................................... 12
2.1.1 Thuộc tính .................................................................................................... 12
2.1.2 Lược đồ quan hệ ........................................................................................... 13
2.1.3 Bộ (Tuple / Record /Row) ............................................................................... 13
2.1.4 Quan hệ (Relation) ........................................................................................ 14
2.1.5 Lược đồ cơ sở dữ liệu ..................................................................................... 14
2.1.6 Tình trạng của lược đồ CSDL ........................................................................... 14
2.1.7 Siêu khóa và khóa của một quan hệ ................................................................ 14
2.2 NGÔN NGỮ ĐẠI SỐ QUAN HỆ ............................................................................. 15
2.2.1 Các phép toán trên tập hợp ............................................................................ 15
2.2.2 Các phép toán trên quan hệ............................................................................ 18
BÀI TẬP ................................................................................................................. 26
BÀI 3: NGÔN NGỮ HỎI CÓ CẤU TRÚC ........................................................................ 28
3.1 TRUY VẤN DỮ LIỆU VỚI CÂU LỆNH SELECT........................................................ 28
3.1.1 Cú pháp: ...................................................................................................... 28
3.1.2 Mệnh đề Order By ......................................................................................... 29
3.1.3 Mệnh đề Where ............................................................................................. 29
3.1.4 Phát biểu Group By và Having ......................................................................... 32
3.1.5 Thứ tự dịch của lệnh Select: ........................................................................... 32
3.2 CÁC LỆNH ĐỊNH NGHĨA DỮ LIỆU: ...................................................................... 33
3.2.1 Lệnh Tạo Cấu Trúc Quan Hệ Mới: .................................................................... 33
3.2.2 Lệnh Xóa Một Quan Hệ: ................................................................................. 35
3.2.3 Lệnh Thay Đổi Cấu Trúc Của Quan Hệ: ............................................................ 35
3.2.4 Các Lệnh cập nhật dữ liệu: ............................................................................. 35
BÀI TẬP ................................................................................................................. 37
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
II
MỤC LỤC
BÀI 4: RÀNG BUỘC TOÀN VẸN ................................................................................... 41
4.1 CÁC YẾU TỐ CỦA RBTV ...................................................................................... 41
4.1.1 Khái niệm...................................................................................................... 41
4.1.2 Các yếu tố Của RBTV: ..................................................................................... 42
4.2 PHÂN LOẠI CÁC RBTV ....................................................................................... 43
4.2.1 RBTV có bối cảnh là một quan hệ ..................................................................... 43
4.2.2 RBTV Có bối cảnh trên nhiều quan hệ ............................................................... 44
BÀI TẬP ................................................................................................................. 49
BÀI 5: THIẾT KẾ CƠ SỞ DỮ LIỆU ............................................................................... 52
5.1 PHỤ THUỘC HÀM .............................................................................................. 52
5.1.1 Định nghĩa: ................................................................................................... 53
5.1.2 Các phụ thuộc hàm đặc biệt ............................................................................ 53
5.1.3 Hệ tiên đề Amstrong và ứng dụng .................................................................... 54
5.1.4 Bao đóng của tập phụ thuộc hàm ..................................................................... 56
5.1.5 Bao đóng của tập thuộc tính ............................................................................ 56
5.2 KHÓA VÀ CÁCH XÁC ĐỊNH ................................................................................. 58
5.2.1 Định nghĩa .................................................................................................... 58
5.2.2 Cách xác định khóa của một quan hệ ................................................................ 58
BÀI TẬP ................................................................................................................. 63
BÀI 6: DẠNG CHUẨN ................................................................................................. 64
6.1 CÁC DẠNG CHUẨN ............................................................................................ 65
6.1.1 Dạng chuẩn 1 ................................................................................................ 65
6.1.2 Dạng chuẩn 2 ................................................................................................ 66
6.1.3 Dạng chuẩn 3 ................................................................................................ 67
6.1.4 Dạng chuẩn BC (Boyce - Codd) ........................................................................ 69
6.1.5 Dạng chuẩn của một LĐCSDL .......................................................................... 69
6.2 CHUẨN HÓA MỘT LĐQH BẰNG PHÂN RÃ: ........................................................... 70
6.2.1 Khái Niệm Chuẩn Hóa ..................................................................................... 70
6.2.2 Định lý Delobel .............................................................................................. 70
6.2.3 Thuật toán phân rã ......................................................................................... 70
TÀI LIỆU THAM KHẢO ............................................................................................. 75
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
III
HƯỚNG DẪN
HƯỚNG DẪN
MÔ TẢ MÔN HỌC
Nhập môn cơ sở dữ liệu (CSDL) là một trong những môn quan trọng nhất đối với
sinh viên khi theo học các ngành học liên quan đến Công nghệ thông tin. Nó giúp sinh
viên có thể nắm vững về CSDL và thực hiện được các truy vấn trên CSDL từ cơ bản
đến nâng cao. Kết hợp CSDL với ngôn ngữ lập trình, sinh viên có thể xây dựng được
các phần mềm, web site theo yêu cầu thực tế.
Giáo trình này được viết để phục vụ nhu cầu học tập của sinh viên đại học, cao
đẳng chuyên ngành về khoa học máy tính, công nghệ thông tin, an toàn thông tin và
mạng máy tính. Môn học tập hợp các khái niệm cơ bản về cơ sở dữ liệu, tiếp cận ngôn
ngữ hình thức là đại số quan hệ và ngôn ngữ truy vấn có cấu trúc (SQL), giúp sinh
viên hiểu rõ về cách tổ chức, quản lý và tương tác với dữ liệu trong môi trường máy
tính, đặc biệt là trong ngữ cảnh của các ứng dụng và hệ thống thông tin doanh
nghiệp. Các bài học quan trọng bao gồm lý thuyết về CSDL, Ngôn ngữ đại số quan hệ,
ngôn ngữ truy vấn, ràng buộc toàn vẹn và thiết kế CSDL.
Mục đích của giáo trình Nhập môn cơ sở dữ liệu nhằm trình bày các khái niệm cơ
bản về cơ sở dữ liệu, thiết kế CSDL để sinh viên có thể nắm vững và vận dụng trong
tế. Có phần giảng dạy về sử dụng ngôn ngữ SQL trong truy vấn dữ liệu, xây dựng
CSDL trên một hệ quản trị CSDL mạnh sẽ giúp sinh viên làm việc được trên CSDL
quan hệ và thực hiện tốt công việc tại các đơn vị công tác của mình sau này.
NỘI DUNG MÔN HỌC
− Bài 1: Tổng quan về cơ sở dữ liệu: Bài này cung cấp cho sinh viên các khái
niệm cơ bản về dữ liệu, cơ sở dữ liệu và hệ quản trị dữ liệu, các mô hình dữ liệu
được sử dụng trong thiết kế, mô tả và cài đặt CSDL .
− Bài 2: Cơ sở dữ liệu quan hệ: Cung cấp cho sinh viên các khái niệm, ký hiệu,
quy ước được sử dụng trong CSDL quan hệ, cách sử dụng các phép toán đại số
quan hệ trên CSDL quan hệ.
− Bài 3: Ngôn ngữ hỏi có cấu trúc: cung cấp cho sinh viên các lệnh của ngôn ngữ
hỏi có cấu trúc (Structure Query Language - SQL) sử dụng để thực hiện các truy
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
IV
HƯỚNG DẪN
vấn dữ liệu từ CSDL đã có. Đồng thời cũng cung cấp các lệnh định nghĩa dữ liệu để
sinh viên có thể tạo CSDL từ các mô hình dữ liệu quan hệ đã thiết kế được.
− Bài 4: Ràng buộc toán vẹn: Bài học này cung cấp cho sinh viên khả năng phát
hiện đầy đủ, chính xác các ràng buộc toàn vẹn (RBTV) trong cơ sở dữ liệu (CSDL)
và mô tả được chúng rõ ràng trong hồ sơ thiết kế CSDL. Đồng thời, có thể đọc các
bản thiết kế để cài đặt chính xác các RBTV, nhằm đảm bảo cho CSDL luôn ở trạng
thái chính xác và đúng ngữ nghĩa.
− Bài 5: Thiết kế cơ sở dữ liệu: Bài học cung cấp cho sinh viên khái niệm về Phụ
thuộc hàm (Functional Dependency), hệ tiên đề Amstrong áp dụng cho phụ thuộc
hàm (PTH). Phụ thuộc hàm cũng là công cụ để biểu diễn một số Ràng buộc toàn
vẹn. Thông qua cách biễu diễn PTH, ta có thể dễ dàng xác định khóa của quan hệ,
cũng như xác định nhóm các thuộc tính dùng để nhận dạng, tìm kiếm duy nhất
một đối tượng hoặc một sự kiện của thế giới thực được mô hình hóa trong CSDL.
− Bài 6: Dạng chuẩn: Bài học cung cấp cho sinh viên định nghĩa về các dạng chuẩn
liên quan đến phụ thuộc hàm, từ đó sinh viên có thể xác định chính xác dạng
chuẩn của 1 lược đồ quan hệ từ đó suy ra dạng chuẩn của một CSDL. Phương pháp
phân rã sẽ giúp sinh viên có thể áp dụng để nâng cấp dạng chuẩn của quan hệ từ
dạng chuẩn thấp lên dạng chuẩn cao.
KIẾN THỨC TIỀN ĐỀ
Nhập môn cơ sở dữ liệu là môn học bắt buộc cho tât cả sinh viên theo học các
ngành tại khoa Công nghệ thông tin. Môn học sẽ học vào học kỳ 3 sau khi sinh viên
đã nắm được các phần cơ bản về ngành học liên quan đến máy tinh và công nghệ
thông tin.
YÊU CẦU MÔN HỌC
Người học phải tham gia học đầy đủ các buổi lên lớp và làm bài tập đầy đủ ở nhà.
PHƯƠNG PHÁP ĐÁNH GIÁ MÔN HỌC
Môn học được đánh giá gồm:
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
V
HƯỚNG DẪN
− Điểm quá trình: 50% bao gồm: Điểm chuyên cần 20%, điểm kiểm tra giữa kỳ
30%.
− Điểm cuối kỳ: 50%. Hình thức bài thi trắc nghiêm.
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
BÀI 1: TỔNG QUAN VỀ 1
CƠ SỞ DỮ LIỆU
BÀI 1: TỔNG QUAN VỀ
CƠ SỞ DỮ LIỆU
Sau khi học xong bài này, sinh viên có thể:
- Nắm được các khái niệm cơ bản về cơ sở dữ liệu (CSDL);
- Nắm được các khái niệm chính về hệ quản trị CSDL, các mô hình dữ liệu sử dụng
trong CSDL quan hệ.
Từ các khái niệm cơ bản sinh viên sẽ phân biệt được các loại CSDL hiện có, phân
biệt được các hệ quản trị CSDL đang phát triển hiện nay và nhận biết cơ bản về mô
hình dữ liệu sử dụng trong CSDL quan hệ.
1.1 HỆ CSDL DỮ LIỆU
1.1.1 Định nghĩa hệ CSDL
Một hệ CSDL (Database System) là một tập hợp dữ liệu được tổ chức một cách có
chọn lọc, ghi trên các thiết bị trữ tin, nhằm phục vụ đồng thời cho nhiều người với
nhiều mục đích khác nhau.
1.1.2 Các mức biểu diễn CSDL
Khi thiết kế hay đánh giá một CSDL người ta dựa trên 3 mức mô tả (Theo tiêu chuẩn
của ANSI/X3/SPARC)
Mức lược đồ ngoài (External Schema Level):
Là mức ngoài cùng, dành cho người sử dụng. Mỗi người sử dụng hay mỗi nhóm
làm việc sẽ yêu cầu xử lý dữ liệu theo một mục đích riêng.
Ví dụ: Bộ phận quản lý tiền lương cần lập bảng lương cho đơn vị gồm các thông
tin: Số thứ tự (STT), họ tên, bậc lương, phụ cấp, tiền lương (trong đó, phụ cấp được
tính theo hệ số dựa trên bậc lương).
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
2 BÀI 1: TỔNG QU AN VỀ
CƠ SỞ DỮ LIỆU
Bộ phận quản lý công trình cần lập danh sách công nhân viên theo công trình với
các thông tin: STT, họ tên, chuyên môn, công trình đã tham gia (trong đó, nhân
viên được phân công phải có chuyên môn phù hợp với yêu cầu chuyên môn của từng
công trình)
Mức quan niệm (Conceptial Schema Level):
Là mức mô tả tổng thể về CSDL, cho biết CSDL chứa được đối tượng dữ liệu nào,
các mối quan hệ giữa các đối tượng, các yêu cầu ràng buộc về dữ liệu trên các đối
tượng được lưu trữ.
Ví dụ: Dựa trên các yêu cầu của hai nhóm công tác trong ví dụ trên, CSDL cần
chứa các đối tượng như sau:
Nhân viên : Họ tên, bậc lương, chuyên môn
Chế độ phụ cấp: Bậc lương, hệ số phụ cấp
Công trình: Tên công trình, yêu cầu chuyên môn
Mức vật lý (Physical Schema Level):
Là mức cài đặt thật sự của CSDL, liên quan đến cách tổ chức dữ liệu, cách truy
xuất các dữ liệu được lưu trữ.
Ví dụ: Từ ví dụ ở mức quan niệm ta hình thành ra mức vật lý gồm: cách tổ chức
tập tin chứa dữ liệu, cấu trúc mẫu tin, kiểu dữ liệu và cách truy cập mẫu tin,…
Lược đồ ngoài 1
Lược đồ vật lý Lược đồ
quan niệm Lược đồ ngoài 2
Hình 1.1: Sơ đồ liên quan giữa các mức biểu diễn CSDL
1.1.3 Đặc tính của môi trường CSDL
a- Dữ liệu được chia sẻ cho nhiều người sử dụng khác nhau, để tiết kiệm được
không gian lưu trữ, tăng hiệu quả khai thác.
b- Làm giảm tình trạng dữ liệu bị lưu trữ trùng lắp, bảo đảm được tính nhất quán
trong việc truy xuất dữ liệu và tính toàn vẹn dữ liệu.
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
BÀI 1: TỔNG QUAN VỀ 3
CƠ SỞ DỮ LIỆU
c- Có tính độc lập giữa dữ liệu và chương trình ứng dụng:
- Tính độc lập vật lý: Người dùng chỉ quan tâm đến nội dung dữ liệu, không quan
tâm đến tổ chức bên trong, cũng như cách thức truy xuất dữ liệu (phụ thuộc vào
chất lượng của hệ quản trị CSDL).
- Tính độc lập logic: Nếu ta sửa cấu trúc CSDL thì không cần viết lại những chương
trình ứng dụng sẵn có (phụ thuộc vào chất lượng thiết kế).
Để xây dựng và quản lý CSDL chúng ta cần có các phần mềm được gọi là các Hệ
Quản Trị CSDL (DBMS – Data Base Management System).
1.2 HỆ QUẢN TRỊ CSDL VÀ CÁC MÔ HÌNH DỮ LIỆU
1.2.1 Khái niệm Hệ Quản Trị CSDL
Hệ quản trị CSDL là một môi trường phần mềm cho phép xây dựng, quản lý và
khai thác CSDL của các đề án tin học hóa. Ví dụ: Oracle, SQL Server, MS Access, My
SQL, mSQL, Foxpro, …
Các hệ quản trị CSDL có nhiệm vụ hỗ trợ tích cực cho các nhà phân tích thiết kế
CSDL cũng như những người quản trị, sử dụng, khai thác CSDL. Để thực hiện nhiệm
vụ đó, hệ quản trị CSDL cần phải có các thành phần cho phép khai báo cấu trúc lưu
trữ dữ liệu và xây dựng các thao tác xử lý chúng.
1.2.2 Các thành phần của hệ quản trị CSDL
a- Ngôn ngữ định nghĩa dữ liệu (data definition language): Là phương tiện cho
phép khai báo cấu trúc lưu trữ dữ liệu, khai báo các mối liên hệ giữa các loại dữ liệu,
cũng như các quy tắc quản lý áp đặt trên các dữ liệu được lưu trữ.
Ngôn ngữ định nghĩa dữ liệu được xây dựng dựa trên một loại mô hình dữ liệu nào
đó. Hiện nay, phần lớn các hệ quản trị CSDL đều dựa trên mô hình dữ liệu quan hệ.
b- Ngôn ngữ thao tác dữ liệu (data manipulation Language): Cho phép người sử
dụng xây dựng cơ sở dữ liệu, thực hiện các thao tác cặp nhật (thêm, xóa, sửa) dữ
liệu và khai thác dữ liệu với nhiều mục đích khác nhau.
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
4 BÀI 1: TỔNG QU AN VỀ
CƠ SỞ DỮ LIỆU
c- Từ điển dữ liệu (data dictionnary): Chứa thông tin về các thành phần cấu trúc
CSDL (Các thuộc tính, các mối liên hệ...), các quan hệ, các ràng buộc dữ liệu. Thông
qua từ điển dữ liệu, Các hệ quản trị CSDL cung cấp thêm các công cụ trợ giúp khai
thác dữ liệu, lập hồ sơ sưu liệu (documentation) về cấu trúc của CSDL, tạo lập các
CSDL mới...
Để mô tả dữ liệu ở mức quan niệm, người ta đưa ra nhiều loại mô hình.
1.2.3 Các Loại mô hình dữ liệu
1.2.3.1 ĐỊNH NGHĨA
Mô hình dữ liệu là một tập hợp các khái niệm, các quy ước biểu diễn dữ liệu cần
quản lý ở mức quan niệm. Thông qua mô hình dữ liệu, người thiết kế sẽ mô tả toàn
cảnh CSDL được thiết kế bao gồm:
a. Các đối tượng, thực thể được quản lý.
b. Các mối quan hệ giữa các đối tượng.
c. Các ràng buộc dữ liệu thể hiện các quy tắc quản lý ảnh hưởng đến các đối tượng
quản lý.
Có nhiều mô hình được đề nghị, ở đây chúng ta sẽ khảo sát 4 mô hình đặc trưng
nhất là: Mô hình dữ liệu Phân Cấp, Mô hình dữ liệu Mạng, Mô hình Quan Hệ,
Mô hình Thực Thể Kết Hợp. Trong đó, mô hình Thực thể kết hợp thường được sử
dụng nhiều nhất khi mô tả dữ liệu ở mức quan niệm trong qui trình thiết kế CSDL.
1.2.3.2 MÔ HÌNH THỰC THỂ KẾT HỢP
Mô hình thực thể kết hợp (ERD - Entity Relation Diagram): Do Peter Chen đề xuất
vào năm 1976. Đây là mô hình được sử dụng phổ biến để thiết kế CSDL quan hệ ở
mức quan niệm.
CÁC KHÁI NIỆM CHÍNH TRONG MÔ HÌNH GỒM:
Thực thể (Entity): là một đối tượng cụ thể hay trừu tượng trong thế giới thực
Ví dụ: Nhân viên Nguyễn Văn A. Lớp CNTT1. Xe hơi có biển số 60E-1689
Thuộc tính (Attribute): Là các yếu tố thông tin để nhận biết được thực thể
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
BÀI 1: TỔNG QUAN VỀ 5
CƠ SỞ DỮ LIỆU
Ví dụ: Họ tên, ngày sinh, nơi sinh ... của nhân viên
Loại thực thể (Entity Type): Tập các thực thể có chung các thuộc tính.
Ví dụ: Loại thực thể Nhân viên
Khóa của loại thực thể: Là tập thuộc tính mà giá trị của nó xác định duy nhất 1
thực thể
Ví dụ: Mã số nhân viên (MSNV) là khóa của loại thực thể Nhân_Viên , Mã số phòng
ban (MSPB) là khóa của loại thực thể Phòng_Ban.
Ký hiệu hình thức của loại thực thể:
Trong đó: Số thuộc tính phải lớn hơn hay bằng 1.
Ví dụ: Loại thực thể NHÂN VIÊN và loại thực thể PHÒNG BAN
Loại mối kết hợp (Relationship): dùng diễn tả các liên hệ ngữ nghĩa giữa các loại
thực thể.
Ví dụ:
- Giữa thực thể Nhân viên và thực thể Phòng Ban có mối liên hệ ngữ nghĩa về quá
trình công tác của một nhân viên ở phòng ban nào đó.
- Giữa thực thể Sinh viên và thực thể Lớp có mối liên hệ ngữ nghĩa: Mỗi sinh viên
thuộc vào một Lớp học.
Ký hiệu hình thức của mối kết hợp:
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
6 BÀI 1: TỔNG QU AN VỀ
CƠ SỞ DỮ LIỆU
Tên MKH
Thuộc tính 1
…
……….
Trong đó: Thuộc tính của mối kết hợp có thể có hoặc không tuy theo các quy tắc
quản lý khác nhau
Ví dụ:
Quá trình CT
Ngày vào làm
Thuộc tính của mối kết hợp: là thuộc tính chung của các loại thực thể tham gia mối
kết hợp.
Bản số mỗi nhánh của mối kết hợp: là 1 bộ gồm 2 thành phần (min, max), đây là
một ràng buộc toàn vẹn về số lượng tối thiểu và tối đa của 1 thực thể của nhánh đó
tham gia vào các thể hiện của mối kết hợp.
Chú ý: Cận tối thiểu có thể là 0 hay 1
Nếu bài toán không qui định Min thì mặc định min = 1.
Nếu bài toán không qui định Max thì đặt max = n với (n >1).
Thường xuất hiện các bản số:(0, 1); (0, n); (1, 1); (1, n)
CÁC BƯỚC THIẾT LẬP MÔ HÌNH THỰC THỂ KẾT HỢP:
B : Phân tích yêu cầu bài toán, chọn ra các thông tin cần quản lý, từ đó hình thành
1
từ điển dữ liệu.
B : Tiến hành gom nhóm các thuộc tính theo các thực thể thật.
2
B : Xác định các mối kết hợp giữa các thực thể.
3
B : Xác định các thuộc tính của các mối kết hợp.
4
B : Xác định bản số của mối kết hợp.
5
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
BÀI 1: TỔNG QUAN VỀ 7
CƠ SỞ DỮ LIỆU
Ví dụ: Xây dựng mô hình dữ liệu phục vụ cho việc quản lý điểm thi các môn học
để tính điểm trung bình của từng học kỳ của sinh viên các lớp, với quy tắc quản lý
như sau: Mỗi môn học, mỗi sinh viên phải có đủ hai cột điểm là: điểm giữa kỳ và
điểm cuối kỳ.
MỘT SỐ QUI ĐỊNH CỦA MÔ HÌNH THỰC THỂ KẾT HỢP:
Không có các thuộc tính trùng tên giữa các thực thể.
Mọi thuộc tính của thực thể phải phụ thuộc trực tiếp vào khóa của thực thể.
Thuộc tính có liên quan với các thực thể của một MKH thì đặt ở mối kết hợp.
Ví dụ: Hãy lập mô hình ER cho bài toán quản lý siêu thị với các quy tắc như sau:
- Siêu thị chia thành nhiều khu vực, mỗi khu vực được đánh 1 mã số và có 1 tên,
chuyên bán 1 loại mặt hàng nào đó, có 1 người quản lý và nhiều nhân viên làm việc
trong khu vực đó.
- Mỗi mặt hàng trong siêu thị có thể cung cấp bởi nhiều nhà cung ứng. Mỗi nhà
cung ứng cần lưu tên công ty, địa chỉ, số phone, số fax và các mặt hàng mà nhà
cung ứng đó cung cấp.
- Mỗi khách hàng mua hàng thì chọn lựa hàng và sau đó đến quầy tính tiền. Ở
quầy tính tiền sẽ in ra 1 hóa đơn gồm: số hóa đơn, ngày lập hóa đơn, tên khách
mua, và danh sách các mặt hàng mua kèm theo đơn giá bán của các mặt hàng đó.
- Đối với khách hàng mua sỉ thì phải lưu trữ lại thông tin khách hàng gồm: họ tên
khách, địa chỉ, số phone, số fax.
- Các nhân viên làm việc được lưu trữ các thành phần: Msnv, họ tên, ngày sinh,
địa chỉ, ngày vào làm việc, và khu vực mà nhân viên đó trực thuộc.
1.2.3.3 MÔ HÌNH DỮ LIỆU MẠNG
Mô hình mạng (Network Data Model) sử dụng các khái niệm:
Loại mẫu tin (Record Type): thay cho khái niệm loại thực thể, chứa các mẫu tin
mà mỗi mẫu tin là một thực thể.
Loại liên hệ (Set Type): là sự quan hệ ngữ nghiã giữa 1 loại mẫu tin chủ và một
loại mẫu tin thành viên.
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
8 BÀI 1: TỔNG QU AN VỀ
CƠ SỞ DỮ LIỆU
Ví dụ:
SINH VIEN
1:n
1:n
LOP KHOA
Ký hiệu 1:n: diễn tả ý nghĩa: 1 mẫu tin chủ liên hệ với nhiều mẫu tin thành viên
(một lớp có thể gồm nhiều sinh viên hay một khoa có thể có nhiều lớp).
Ký hiệu 1:1: ý nghĩa 1 mẫu tin chủ liên hệ với 1 mẫu thành viên.
Cách chuyển từ mô hình ER sang mô hình mạng:
Qui tắc 1: Mỗi thực thể hình thành 1 kiểu mẫu tin.
Qui tắc 2: Mối kết hợp thuộc loại (?,1) - (?,n) hay (?,1) - (?,1) thì hình thành 1 loại
liên hệ chiều mũi tên đi từ (?,n) --> (?,1).
Qui tắc 3: Mối kết hợp thuộc loại (?,n) - (?,n) thì hình thành 1 kiểu mẫu tin mới,
kiểu mẫu tin này chứa các thuộc tính khóa của 2 thực thể liên quan.
1.2.3.4 MÔ HÌNH DỮ LIỆU PHÂN CẤP
Mô hình dữ liệu phân cấp (Hierarchical Data Model) giống như mô hình mạng, với
các khái niệm: Kiểu mẫu tin và Loại liên hệ. Nhưng 1 kiểu mẫu tin thành viên chỉ có
thể phụ thuộc duy nhất 1 kiểu mẫu tin cha. Nghĩa là chỉ có những kiểu liên hệ: 1:1,
1:n. Do đó, mô hình được thể hiện như một rừng cây.
Những kiểu mẫu tin không có Cha là gốc của cây. Các kiểu mẫu tin cuối cùng
không con tạo thành các lá của cây.
Ví dụ: về mô hình phân cấp
Lớp Sinh viên Môn học
Kết quả Kết quả
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
BÀI 1: TỔNG QUAN VỀ 9
CƠ SỞ DỮ LIỆU
1.2.3.5 MÔ HÌNH DỮ LIỆU QUAN HỆ
Mô hình dữ liệu quan hệ (Relational Data Model) là mô hình được phát triển vào
năm 1970 do Edgar F. Codd thuộc công ty IBM đề xuất. Các đối tượng trong mô
hình này chỉ gồm các bảng 2 chiều được gọi là các quan hệ (Relation Table) với các
khái niệm: Thuộc tính, khóa, Lược đồ Quan hệ. Mô hình này có một cơ sở lý thuyết
vững chắc nên là mô hình được phát triển rộng rãi nhất hiện nay.
Cách chuyển từ mô hình ER sang mô hình quan hệ:
Quy tắc 1: Chuyển mỗi thực thể thành 1 quan hệ
Quy tắc 2: Mối quan hệ (?,n) - (?,n) thành 1 quan hệ có khóa là khóa của các thực
thể tham gia.
Quy tắc 3: Mối kết hợp (?,1) - (?,n) thì tạo thêm thuộc tính khóa của bên thực thề
(1,1) vào trong thực thể phía (1,n) để làm khóa ngoại.
Quy tắc 4: Mối kết hợp (1,1) - (1,1) có thể gộp 2 thực thể thành một thực thể hoặc
chọn khóa của một bên để thêm vào bên còn lại làm khóa ngoại
Ví dụ: Mô hình quan hệ quản lý học tập
Trong mô hình quan hệ trên ta thấy: Trong quan hệ SINH VIÊN có thuộc tính MaLOP
là thuộc tính khóa của quan hệ LOP được thêm vào làm khóa ngoại.
Do mối kết hợp giữa hai loại thực thể SINH VIEN và loại thực thể MON HOC là (?,n)
- (?,n) nên hình thành quan hệ mới là KET QUA có chứa khóa của 2 loại thực thể liên
quan(MaSV, MaMH).
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
10 BÀI 1: TỔNG QU AN VỀ
CƠ SỞ DỮ LIỆU
MÔ HÌNH DỮ LIỆU HƯỚNG ĐỐI TƯỢNG
Mô hình dữ liệu hướng đối tượng (Object Oriented Data Model) ra đời đầu những
năm 1980, dựa trên cách tiếp cận hướng đối tượng. Nhưng hiện nay chưa được sử
dụng rộng rãi do chưa có nhiều hệ quản trị CSDL hỗ trợ cài đặt theo mô hình này.
Ví Dụ: về một mô hình lớp (hướng đối tượng) quản lý nhân viên
Trong mô hình lớp trên chúng ta nhận thấy: ngoài phần thông tin (dữ liệu) các lớp
còn có các hành động (phương thức – phần để () phía dưới thông tin) của lớp.
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
BÀI 1: TỔNG QUAN VỀ 11
CƠ SỞ DỮ LIỆU
BÀI TẬP
Bài 1: Thiết lập mô hình thực thể kết hợp và mô hình quan hệ dùng cho việc quản
lý cho mượn sách tại một thư viện (xem tại chỗ hoặc mang về nhà) với các quy tắc
quản lý như sau:
Sách gồm mã sách, tên, nguyên tác (tiếng Việt hoặc nườc ngoài), tác giả. Sách
được phân chia theo thể loại gồm MaTL và tên thể loại.
Đọc giả muốn mượn sách phải lập thẻ Đọc giả. Thẻ ghi nhận các thông tin gồm:
MaDG, Ten DG, địa chỉ, ngày cấp, thông tin các sách đã mượn, ngày mượn, ngày
trả. Hàng năm, Đọc giả phải đóng lệ phí để gia hạn thẻ mới được mượn sách, trên
sổ có ghi thêm thông tin: Năm, Ngày nộp, Số tiền.
Bài 2: Hãy thiết lập mô hình thực thể kết hợp và mô hình quan hệ cho bài toán
quản lý siêu thị với các quy tắc quản lý như sau:
Siêu thị chia thành nhiều khu vực, mỗi khu vực được đánh một mã số và có một
tên, chuyên bán một loại mặt hàng nào đó, có một người quản lý và nhiều nhân
viên làm việc trong khu vực đó.
Mỗi mặt hàng trong siêu thị có thể được cung cấp bởi nhiều nhà cung cấp. Mỗi nhà
cung cấp cần lưu tên công ty, địa chỉ, số điện thoại và các mặt hàng mà nhà cung
cấp đó có thể cung cấp.
Mỗi khách hàng mua hàng thị chọn hàng sau đó đến quẩy tính tiền. Ở đây sẽ in ra
hóa đơn gồm: số hóa đơn, ngày lập hóa đơn, tên khách mua, và danh sách các mặt
hàng mua kèm theo đơn giá bán.
Đối với khách hàng thân thiết thì phải lưu mã số khách hàng, họ tên, địa chỉ và số
điện thoại khách hàng.
Các nhân viên làm việc được lưu trữ các thành phần gồm: mã nhân viên, họ tên,
ngày sinh, địa chỉ, ngày vào làm việc và khu vực mà nhân viên đó trực thuộc.
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
12
BÀI 2: CƠ SỞ DỮ LIỆU QUAN HỆ
BÀI 2: CƠ SỞ DỮ LIỆU QUAN HỆ
- Sau khi học xong bài này sinh viên sẽ nắm được:
- Các ký hiệu sử dụng trong quá trình mô tả, thiết kế, truy vấn CSDL quan hệ.
- Hiểu và áp dụng được ngôn ngữ đại số quan hệ trong các lệnh truy vấn dữ liệu từ
CSDL đã có, từ đó sinh viên có thể sử dụng tốt các câu lệnh truy vấn trong ngôn
ngữ SQL ở bài học tiếp theo.
2.1 CÁC KHÁI NIỆM CƠ BẢN
2.1.1 Thuộc tính
Là các đặc tính riêng biệt của mỗi đối tượng được quản lý.
Thuộc tính được xác định bởi:
Tên gọi: Thuờng được đặt một cách gợi nhớ, không nên đặt trùng tên 2 thuộc tính
của 2 loại đối tượng khác nhau.
Ví dụ: Hai loại đối tượng: SinhVien và GiangVien đều có thuộc tính tên thì đặt
TenSV, TenGV (tránh đặt thuộc tính là hoten cho cả hai loại đối tượng).
Qui ước: Trong lý thuyết, để ngắn gọn người ta thường dùng các chữ in hoa đại
diện cho tên các thuộc tính. (VD: A, B, C, D)
Kiểu dữ liệu: Vô hướng: Số, văn bản, Boolean; Có cấu trúc: Date/Time…
Miền giá trị (Domain): Ký hiệu Dom(A)
Ví dụ: Điểm có miền giá trị trong khoảng [0..10]
Hay: Dom (Ngày_Sinh)  [1,31]/[1,12]/[1900,2023]
Qui ước: Miền giá trị còn chứa thêm giá trị rỗng (NULL) đặc trưng cho 1 trong 2 ngữ
nghĩa: Chưa xác định tại thời điểm đang xét hoặc không thể xác định.
Ví dụ: TinhTrạngGiaĐình: chứa giá trị rỗng khi chưa xác định là có vợ/chồng.
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
13
BÀI 2: CƠ SỞ DỮ LIỆU QUAN HỆ
2.1.2 Lược đồ quan hệ
Một lược đồ quan hệ (LĐQH), là một sự biểu diễn các đối tượng có chung các thuộc
tính. Được biểu diễn bởi một cặp r=<U, F>. Trong đó: r là LĐQH, U là tập thuộc tính
và F là tập phụ thuộc hàm.
Ví dụ: Loại đối tượng tồn tại khách quan: Sinh viên, Giảng viên, Đơn đặt hàng, …
Loại đối tượng trừu tượng: Thời khóa biểu, Hợp đồng, …
Một LĐQH gồm có:
Một tên gọi: như quan hệ NhânVien, HọcSinh, HoSoBenhAn, …
Qui ước: Trong Lý thuyết, thường dùng ký tự như: r, v, u, …
Một tập hợp hữu hạn các thuộc tính: A , A , …, A , ký hiệu: Q+ = {A , A , …, A }
1 2 n 1 2 n
Số thuộc tính của 1 LĐQH là gọi là số ngôi của LĐQH, ký hiệu: Card(Q+).
LĐQH r có tập thuộc tính A , …, A được ký hiệu: Q=(A , …, A )
1 n 1 n
Một Tân từ, Ký hiệu:||Q||, dùng mô tả ý nghĩa của LĐQH, các quy tắc, qui định về
giá trị và sự liên hệ của các thuộc tính.
Ví dụ: LĐQH KetQuaHT (MSSV, MSMon, HocKy, DiemL , DiemL )
1 2
Tân từ: Một bộ dữ liệu của kết quả học tập được xác định bởi 2 thuộc tính là (MSSV,
MSMon). Mỗi môn học (MSMon) sinh viên (MSSV) được thi tối đa 2 lần.
Ví dụ: LĐQH KhachHang (MSKH, TenKH, DiaChi, SoDT)
Tân từ: Mỗi khách hàng có một mã số (MSKH) để phân biệt với các khách hàng
khác, phải có tên (TenKH), địa chỉ (DiaChi), xác định và có thể có hay không có điện
thoại (SoDT).
2.1.3 Bộ (Tuple / Record /Row)
Một bộ của một LĐQH Q là tập giá trị tất cả thuộc tính của một đối tượng thỏa mãn
tân từ ||Q|| của lược đồ quan hệ đó.
Ký hiệu: q = (a , a , …, a )  Dom(a )xDom(a )x...xDom(a ) và ||Q(q)|| = TRUE
1 2 n 1 2 n
Ví dụ: TRUONG_ĐH (Mã_Truong, Ten_Truong, ĐT)
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
| 14  |                              |     |     |     |
| --- | ---------------------------- | --- | --- | --- |
|     | BÀI 2: CƠ SỞ DỮ LIỆU QUAN HỆ |     |     |     |

         q = (‘DHKHTN’, ‘Đại học Khoa Học Tự  nhiên’, ‘02838124321’)
2.1.4 Quan hệ (Relation)
Một quan hệ của một lược đồ quan hệ Q, ký hiệu T , là một tình trạng, một thể hiện
Q
của lược đồ quan hệ Q ở một thời điểm nào đó.
Khi đó quan hệ T  chứa các bộ q có giá trị cụ thể thỏa mãn tân từ của lược đồ quan
Q
hệ Q:
|     | T Q  = { q= (a | 1 ,a 2 ,.., a | n ) / a, Dom(a), ||Q(q)|| = TRUE }  i | i   |
| --- | -------------- | ------------- | ------------------------------------- | --- |
2.1.5 Lược đồ cơ sở dữ liệu
Một lược đồ cơ sở dữ liệu C là một tập hợp các lược đồ quan hệ , Ký hiệu:
C = {Q}t

i i = 1
2.1.6 Tình trạng của lược đồ CSDL
Tình trạng của một LĐCSDL là tập hợp tình trạng T  của các lược đồ quan hệ Q có
Qi i
trong lược đồ cơ sở dữ liệu C = {Q}t
i i=1
| Ký hiệu: T | = {T }t | .   |     |     |
| ---------- | ------- | --- | --- | --- |
|            | C Qi    | i=1 |     |     |
2.1.7 Siêu khóa và khóa của một quan hệ
| Cho một quan hệ Q=(A |     | , A , ..., A | )   |     |
| -------------------- | --- | ------------ | --- | --- |
|                      |     | 1 2          | n   |     |
Siêu khóa: Cho tập thuộc tính S, S  Q+, S được gọi là Siêu khóa (Super Key) của
quan hệ Q nếu S có thể dùng làm cơ sở để phân biệt 2 bộ khác nhau tùy ý.
|     | q, q  T | , q.S = q.S thì q ≡ q  |     |     |
| --- | --------- | ---------------------- | --- | --- |
|     | i j       | Q i j                  | i j |     |
Lưu ý:
Một quan hệ Q luôn luôn có ít nhất 1 siêu khóa và có thể có nhiều siêu khóa.
Thuộc tính tham gia vào siêu khóa không được chứa giá trị rỗng
   Ví dụ: KhachHang(MSKH, TenKH, DiaChi, SoDT)
   có các siêu khóa: S ={MSKH}, S ={MSKH,TenKH}, S  = {MSKH,DiaChi},
|     |     | 1   | 2   | 3   |
| --- | --- | --- | --- | --- |
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
  15

BÀI 2: CƠ SỞ DỮ LIỆU QUAN HỆ

      S ={MSKH, TenKH, DiaChi},…
4
Khóa chính (primary Key):
Là một siêu khóa tối tiểu không chứa bất kỳ một siêu khóa nào.
Ví dụ: trong các siêu khóa trong ví dụ trên thì K ={MSKH} là khóa chính
1
Nếu một quan hệ có nhiều khóa chính, khi cài đặt nên chọn một khóa chính cho
việc truy xuất đến các bộ. Các khóa còn lại được xem là các khóa phụ (Secondary
key) hay khóa tương đương.
Thuộc tính khóa và thuộc tính không khóa: Các thuộc tính tham gia vào ít
nhất một khóa nào đó của LĐQH thì gọi là thuộc tính khóa, các thuộc tính không
tham gia vào khóa nào gọi là các thuộc tính không khóa. Khi Ký hiệu Q  là tập thuộc
k
| tính khóa và Q |  là tập thược tính không khóa ta có:  |     |     |     |     |     |
| -------------- | ------------------------------------- | --- | --- | --- | --- | --- |
o
|     |   Q =Q-Q |     |     |     |     |     |
| --- | -------- | --- | --- | --- | --- | --- |
|     | o        | k   |     |     |     |     |
2.2 NGÔN NGỮ ĐẠI SỐ QUAN HỆ
Để truy xuất, khai thác lược đồ CSDL, F.F. Codd đã định nghĩa các toán tử chính để
thao tác trên các quan hệ:
5 toán tử truyền thống trên tập hợp: Hội, Giao, Hiệu, Tích, Bù.
4 toán tử đặc thù cho các thao tác trên các quan hệ: Chiếu, chọn, kết, chia.
2.2.1 Các phép toán trên tập hợp
2.2.1.1 PHÉP HỘI (UNION)
Định nghĩa: Giả sử Q  và Q  là 2 quan hệ có cùng tập thuộc tính {A , A , …, A }
|     |     | 1   | 2   |     | 1 2 | n   |
| --- | --- | --- | --- | --- | --- | --- |
Hội 2 quan hệ Q , Q  hình thành quan hệ mới Q  mới có cùng tập thuộc tính {A , A ,
|                                              | 1          | 2             |                | 3        |     | 1 2 |
| -------------------------------------------- | ---------- | ------------- | -------------- | -------- | --- | --- |
| …, A } và chứa tất cả các bộ của 2 quan hệ Q |            |               |                |  và Q .  |     |     |
| n                                            |            |               |                | 1 2      |     |     |
| Ký hiệu:                                     | Q  = Q     |   Q          |                |          |     |     |
|                                              | 3          | 1 2           |                |          |     |     |
|   Q += {A                                    | , A , …, A | }             |                |          |     |     |
| 3                                            | 1 2        | n             |                |          |     |     |
|   T Q3  = T                                  | Q1   T Q2 |  = {q / q  T | Q1  Hoặc q  T | Q2 }     |     |     |
| Ví dụ: Hội 2 quan hệ: SV                     |            |  và SV        |                |          |     |     |
|                                              |            | 1             | 2              |          |     |     |
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
| 16  |                                |     |     |     |     |     |     |     |     |     |     |
| --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |   BÀI 2: CƠ SỞ DỮ LIỆU QUAN HỆ |     |     |     |     |     |     |     |     |     |     |

|     |     | SV   |     |     |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1
|     |     |      |       | MaSV  | Tên Sinh Viên   |     |     |     | Phái  |     |     |
| --- | --- | ---- | ----- | ----- | --------------- | --- | --- | --- | ----- | --- | --- |
|     |     |      | SV03  |       | Nguyễn Hòa      |     |     |     | Nam   |     |     |
|     |     |      | SV04  |       | Phạm Bằng       |     |     |     | Nam   |     |     |
|     |     |      | SV05  |       | Nguyễn Thị Hoa  |     |     |     | Nu    |     |     |
|     |     | SV   |       |       |                 |     |     |     |       |     |     |
2
|     |     |            | MaSV  |     | Tên Sinh Viên    |     |     |     | Phái  |     |     |
| --- | --- | ---------- | ----- | --- | ---------------- | --- | --- | --- | ----- | --- | --- |
|     |     |            | SV07  |     | Nguyễn Văn Minh  |     |     |     | Nam   |     |     |
|     |     |            | SV04  |     | Phạm Bằng        |     |     |     | Nam   |     |     |
|     |     | SV 1   SV | 2     |     |                  |     |     |     |       |     |     |
|     |     |            | MaSV  |     | Tên Sinh Viên    |     |     |     | Phái  |     |     |
|     |     |            | SV03  |     | Nguyễn Hòa       |     |     |     | Nam   |     |     |
|     |     |            | SV04  |     | Phạm Bằng        |     |     |     | Nam   |     |     |
|     |     |            | SV05  |     | Nguyễn Thị Hoa   |     |     |     | Nu    |     |     |
|     |     |            | SV07  |     | Nguyễn Văn Minh  |     |     |     | Nam   |     |     |
2.2.1.2 PHÉP GIAO (INTERSECTION)
Định nghĩa: Giả sử Q  và Q  là 2 quan hệ có cùng tập thuộc tính {A , A , ..., A }
|     |     |     |     | 1   | 2   |     |     |     |     | 1 2 | n   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Giao của 2 quan hệ Q , Q  hình thành quan hệ mới Q  có cùng tập thuộc tính {A ,
|            |                                         |            | 1             | 2   |           |                |     |       | 3   |     | 1   |
| ---------- | --------------------------------------- | ---------- | ------------- | --- | --------- | -------------- | --- | ----- | --- | --- | --- |
| A          | 2 , …, A n } và chứa các bộ vừa thuộc Q |            |               |     |           | 1  vừa thuộc Q |     | 2 .   |     |     |     |
| Ký hiệu:   |                                         | Q  = Q     |   Q          |     |           |                |     |       |     |     |     |
|            |                                         | 3          | 1             | 2   |           |                |     |       |     |     |     |
|            | Q += {A                                 | , A , …, A |               | }   |           |                |     |       |     |     |     |
|            | 3                                       | 1 2        | n             |     |           |                |     |       |     |     |     |
|            | T  = T                                  |   T       |  = {q / q  T |     |  và q  T |                | }   |       |     |     |     |
|            | Q3                                      | Q1 Q2      |               |     | Q1        |                | Q2  |       |     |     |     |
Ví dụ: với 2 quan hệ: SV  và SV như ví dụ trên, Giao 2 quan hệ này ta có:
|     |     |            |       | 1   | 2              |     |     |     |       |     |     |
| --- | --- | ---------- | ----- | --- | -------------- | --- | --- | --- | ----- | --- | --- |
|     |     | SV 1   SV | 2     |     |                |     |     |     |       |     |     |
|     |     |            | MaSV  |     | Tên Sinh Viên  |     |     |     | Phái  |     |     |
|     |     |            | SV04  |     | Phạm Bằng      |     |     |     | Nam   |     |     |
2.2.1.3 PHÉP HIỆU (EXCEPT)
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
|     |     |     |     |     |     |     |     |     |     |     |     |     |     | 17  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

BÀI 2: CƠ SỞ DỮ LIỆU QUAN HỆ

Định nghĩa: Giả sử Q  và Q  là hai quan hệ có cùng tập thuộc tính {A , A , …, A }.
|     |     |     |     |     | 1   | 2   |     |     |     |     |     |     | 1 2 | n   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Hiệu của 2 quan hệ Q , Q  hình thành quan hệ mới Q  có cùng tập thuộc tính {A ,
|            |        |                          |         |               | 1 2 |     |                      |     |       |     | 3   |     |     | 1   |
| ---------- | ------ | ------------------------ | ------- | ------------- | --- | --- | -------------------- | --- | ----- | --- | --- | --- | --- | --- |
| A          | , …, A | } và chứa các bộ thuộc Q |         |               |     |     |  nhưng không thuộc Q |     |       |     |     |     |     |     |
|            | 2      | n                        |         |               |     |     | 1                    |     |       |     | 2   |     |     |     |
| Ký hiệu:   |        |                          | Q  = Q  |  - Q          |     |     |                      |     |       |     |     |     |     |     |
|            |        |                          | 3       | 1             | 2   |     |                      |     |       |     |     |     |     |     |
|            | Q      | += {A                    | ,A ,…,A | }             |     |     |                      |     |       |     |     |     |     |     |
|            | 3      |                          | 1 2     | n             |     |     |                      |     |       |     |     |     |     |     |
|            | T Q3   |  = T Q1                  |  - T Q2 |  = {q / q  T |     | Q1  |  và q  T            |     | Q2 }  |     |     |     |     |     |
Ví dụ: với 2 quan hệ SV  và SV như ví dụ trên hiệu 2 quan hệ này ta có:
|     |     |     |          |       | 1   | 2   |                 |     |     |     |       |     |     |     |
| --- | --- | --- | -------- | ----- | --- | --- | --------------- | --- | --- | --- | ----- | --- | --- | --- |
|     |     |     | SV  – SV |       |     |     |                 |     |     |     |       |     |     |     |
|     |     |     | 1        | 2     |     |     |                 |     |     |     |       |     |     |     |
|     |     |     |          | MaSV  |     |     | Tên Sinh Viên   |     |     |     | Phái  |     |     |     |
|     |     |     |          | SV03  |     |     | Nguyễn Hòa      |     |     |     | Nam   |     |     |     |
|     |     |     |          | SV05  |     |     | Nguyễn Thị Hoa  |     |     |     | Nu    |     |     |     |
2.2.1.4 PHÉP TÍCH DESCARTES (CARTESIAN PRODUCT)
Định nghĩa: Giả sử quan hệ Q  có tập thuộc tính {A , A , …, A } và quan hệ Q  có
|     |     |     |     |     |     | 1   |     |     |     | 1   | 2   | n   |     | 2   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tập thuộc tính {B , B , …, B }. Tích Descartes của 2 quan hệ Q , Q  hình thành một
|                  |                  |        |               | 1 2              |         | m        |        |         |          |       |     | 1 2 |     |     |
| ---------------- | ---------------- | ------ | ------------- | ---------------- | ------- | -------- | ------ | ------- | -------- | ----- | --- | --- | --- | --- |
| quan hệ mới Q    |                  |        | 3  có:        |                  |         |          |        |         |          |       |     |     |     |     |
|                  | Tập thuộc tính Q |        |               | + = {A           | , A     | , ..., A |        | , B , B | , ..., B | } và  |     |     |     |     |
|                  |                  |        |               | 3                | 1       | 2        | n      | 1       | 2        | m     |     |     |     |     |
|   Chứa các bộ (q |                  |        |               | , q ) trong đó q |         |          |   T   |  và q   |   T     |       |     |     |     |     |
|                  |                  |        | 1             | 2                |         |          | 1      | Q1      | 2        | Q2    |     |     |     |     |
| Ký hiệu:         |                  |        | Q  = Q        |  x Q             |         |          |        |         |          |       |     |     |     |     |
|                  |                  |        | 3             | 1                | 2       |          |        |         |          |       |     |     |     |     |
|     Q            | += {A            |        | , A , ..., A  |                  | , B , B | , ..., B |        | }       |          |       |     |     |     |     |
|                  | 3                | 1      | 2             | n                | 1       | 2        | m      |         |          |       |     |     |     |     |
|     T            | Q3               |  = {(q | 1 , q 2 ) / q | 1   T           | Q1      |  và q    | 2   T | Q2 }    |          |       |     |     |     |     |
Ví dụ: Tích 2 quan hệ: Sinh Viên và Lớp
|     |     |     |     | SV    |     |     |                  |     |     |     |       |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | ---------------- | --- | --- | --- | ----- | --- | --- | --- |
|     |     |     |     | MaSV  |     |     | Tên Sinh Viên    |     |     |     | Phái  |     |     |     |
|     |     |     |     | SV07  |     |     | Nguyễn Văn Minh  |     |     |     | Nam   |     |     |     |
|     |     |     |     | SV04  |     |     | Phạm Bằng        |     |     |     | Nam   |     |     |     |
|     |     |     |     |       |     |     |                  |     |     |     |       |     |     |     |

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
| 18  |                              |     |     |     |     |     |     |     |     |     |
| --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | BÀI 2: CƠ SỞ DỮ LIỆU QUAN HỆ |     |     |     |     |     |     |     |     |     |

|     |     |     | LOP  |        |     |                   |     |     |     |     |
| --- | --- | --- | ---- | ------ | --- | ----------------- | --- | --- | --- | --- |
|     |     |     |      | MaLop  |     | Tên Lớp           |     |     |     |     |
|     |     |     |      | V01    |     | Lập trình viên 1  |     |     |     |     |
|     |     |     |      | M02    |     | Mạng máy tính 2   |     |     |     |     |
    SV x LOP
|     | MaSV  |     | Tên sinh viên    |     |     | Phái  | MaLop  |     | Tên Lớp           |     |
| --- | ----- | --- | ---------------- | --- | --- | ----- | ------ | --- | ----------------- | --- |
|     | SV07  |     | Nguyễn Văn Minh  |     |     | Nam   | V01    |     | Lập trình viên 1  |     |
|     | SV07  |     | Nguyễn Văn Minh  |     |     | Nam   | M02    |     | Mạng máy tính 2   |     |
|     | SV04  |     | Phạm Bằng        |     |     | Nam   | V01    |     | Lập trình viên 1  |     |
|     | SV04  |     | Phạm Bằng        |     |     | Nam   | M02    |     | Mạng máy tính 2   |     |
2.2.1.5 PHÉP BÙ (COMPLEMENT)
Định nghĩa: Cho quan hệ Q (A , A , …, A ); T  là một tình trạng được định nghĩa
|     |     |     |     |     | 1   | 2   | n   | Q   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
trên Q. Miền giá trị hiện hành của một thuộc tính A trên T  là tập giá trị phân biệt
|     |     |     |     |     |     |     |     | i   |     | Q   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
trên thuộc tính A hiện tồn tại trong T  (MGT (A)). Phép bù trên lược đồ quan hệ Q
|     |     |     | i   |     |     | Q   | i   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tạo thành một lược đồ quan hệ Q' sao cho:
Ký hiệu:     Q'+ = Q+ và
|     T       |  = {q=(a |     | , a , .., a | ) / a  MGT(A) và q  T |     |     |     |  }  |      |     |
| ----------- | -------- | --- | ----------- | ----------------------- | --- | --- | --- | --- | ---- | --- |
| Q'          |          | 1   | 2           | n i                     |     | i   |     | Q   |      |     |
|   Ví dụ:    |          |     |      Q      |                         |     |     |     |     |  !Q  |     |
|             |          |     | A           | B                       |     |     |     | A   |      | B   |
|             |          |     | a           | b                       |     |     |     | a   |      | b   |
|             |          |     | 1           | 1                       |     |     |     | 2   |      | 2   |
|             |          |     | a           | b                       |     |     |     | a   |      | b   |
|             |          |     | 2           | 1                       |     |     |     | 3   |      | 1   |
|             |          |     | a           | b                       |     |     |     |     |      |     |
|             |          |     | 3           | 2                       |     |     |     |     |      |     |
|             |          |     | a           | b                       |     |     |     |     |      |     |
|             |          |     | 1           | 2                       |     |     |     |     |      |     |
2.2.2 Các phép toán trên quan hệ
2.2.2.1 PHÉP CHIẾU (PROJECTION)
a.  Phép chiếu của một bộ lên tập thuộc tính S:
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
  19

BÀI 2: CƠ SỞ DỮ LIỆU QUAN HỆ

Giả sử ta chiếu bộ q = (a , a , …, a ) lên tập thuộc tính S = (A , A , …, A )  Q+ là
|     |     | 1 2 | n   |     | s1 s2 | sm  |
| --- | --- | --- | --- | --- | ----- | --- |
phép trích ra từ bộ q một bộ con s = (a , a ,..,a ) (m<=n) sao cho a   Dom(A )
|            |          |                  | s1 s2 | sm  |     | si si |
| ---------- | -------- | ---------------- | ----- | --- | --- | ----- |
| Ký hiệu:   | s = q.(A | s1 , A s2 , …, A | sn )  |     |     |       |
Ví dụ: trong quan hệ SinhVien (MSSV, MSLop, HoTen, NgaySinh, Phai) nếu ta chiếu
một bộ q bất kỳ lên 2 thuộc tính MSSV và MSLop thì ta có: giá trị của 2 thuộc tính
i
MSSV và MSLop của bộ dữ liệu q đó: q.MSSV, MSLop = (‘01234’, ‘A01’)
i
b.  Chiếu một quan hệ lên tập thuộc tính X:
Giả sử X là tập hợp con của tập thuộc tính của quan hệ Q: (X  Q+). Phép chiếu Q
lên tập thuộc tính X sẽ tạo thành một lược đồ quan hệ Q' Có tập thuộc tính X và
|       T = {q' / qT |                 | , q’.X = q.X}  |     |     |     |     |
| -------------------- | --------------- | -------------- | --- | --- | --- | --- |
| Q'                   |                 | Q              |     |     |     |     |
|     Ký hiệu:        | (Q) hoặc Q[X].  |                |     |     |     |     |
X
    Ví dụ: SinhVien(MaSV, Tên sinh vien, Phai, MaLop, Tên Lớp)

|       |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- |

    Câu hỏi: Liệt kê danh sách sinh viên gồm các thông tin: MaSV, Tên sinh viên?
|        Trả lời:   |     |     |  (SinhVien)  |     |     |     |
| ------------------ | --- | --- | ------------ | --- | --- | --- |
MaSV, Tên sinh viên

2.2.2.2 PHÉP CHỌN (SELECTION)
Định nghĩa: Cho quan hệ Q(A , A , ..., A ), E là biểu thức logic được phát biểu trên
1 2 n
các thuộc tính của Q+. Phép chọn trên Q theo điều kiện E sẽ hình thành một quan hệ
mới Q' có cùng tập thuộc tính với Q và chứa các bộ thuộc Q và thỏa điều kiện E.
    T = {q' / q'  Q và q' thỏa E}
Q’

|     Ký hiệu:  Q' =  |     | (Q) hoặc Q' = Q : (E)  |     |     |     |     |
| ------------------- | --- | ---------------------- | --- | --- | --- | --- |
E
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
| 20  |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
  BÀI 2: CƠ SỞ DỮ LIỆU QUAN HỆ

Ví dụ: Chọn trên quan hệ SinhVien(MSSV, MSLop, HoTen, NgaySinh, Phai) những
sinh viên sinh trước năm 1975
   
(SinhVien) hay (SinhVien):(Ngaysinh< ‘1/1/1990’ )
Ngaysinh< ‘1/1/1990’
Các điều kiện được sử dụng các phép so sánh: =, >, <, >=,<= , <>  và có thể kết
hợp nhiều điều kiện đơn giản bằng các phép toán logic: and, or
| Ví dụ: KetQuaHT(MSSV, MSMon, DiemL |     |     |     | , DiemL | )   |     |     |     |
| ---------------------------------- | --- | --- | --- | ------- | --- | --- | --- | --- |
|                                    |     |     |     | 1       | 2   |     |     |     |
Chọn ra những học sinh có điểm thi lần 1 hoặc điểm thi lần 2  lớn hơn 8.
| E = (DiemL |  >8) OR (DiemL |     |  >8)  |     |     |     |     |     |
| ---------- | -------------- | --- | ----- | --- | --- | --- | --- | --- |
|            | 1              |     | 2     |     |     |     |     |     |

| T Q' = | (E) (KetQuaHT) hay T |     | Q’  = (KetQuaHT):(E)  |     |     |     |     |     |
| ------ | -------------------- | --- | --------------------- | --- | --- | --- | --- | --- |
Kết quả thực hiện sẽ cho các bộ của quan hệ KetQuaHT thỏa điều kiện E
Ví dụ: Trong quan hệ Sinh Viên, Cho biết những sinh viên học lớp ‘Lập trình viên 1’?

 
|     |     | (SinhVien)               |     |     |     |     |     |     |
| --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- |
TenLop=‘Lập trình vien 1’

2.2.2.3 PHÉP KẾT (JOIN)
Định nghĩa: Cho 2 quan hệ Q (A , A , …, A ) và Q (B , B2, …, B ) có Dom(A) =
|     |     |     | 1 1 | 2   | n   | 2 1 | m   | i   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Dom(B),  là 1 phép so sánh trên miền giá trị của A. Phép kết Theta () giữa Q
| j                                                     |     |     |     |     |     | i     |     | 1  và  |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | ----- | --- | ------ |
| Q  dựa trên A và B sẽ tạo thành một lược đồ quan hệ Q |     |     |     |     |     |  có:  |     |        |
| 2                                                     | i j |     |     |     |     | 3     |     |        |
- Tập thuộc tính bằng tập thuộc tính của tích Descartes Q 1 xQ 2  và
- Chứa các bộ thỏa điều kiện so sách A  B.
i j
|     |     | ): Ai  Bj = {(q |     |     |     |     | .A  q |     |
| --- | --- | ---------------- | --- | --- | --- | --- | ------ | --- |
Nghĩa là:  Q  = (Q  x Q , q ) / q   Q , q Q , q .B is TRUE}
|     | 3 1 | 2   |     | 1 2 | 1   | 1 2 2 | 1 i 2 j |     |
| --- | --- | --- | --- | --- | --- | ----- | ------- | --- |
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
  21

BÀI 2: CƠ SỞ DỮ LIỆU QUAN HỆ

A  B
|              |     |      | i j  |     |     |     |     |     |     |     |
| ------------ | --- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- |
|   Ký hiệu:   | Q   |  = Q |    Q |     |     |     |     |     |     |     |
|              |     | 3    | 1    | 2   |     |     |     |     |     |     |
Ví dụ: Giả sử có hai quan hệ Q (ABC) và Q (DE). Hãy xác định quan hệ Q  dựa trên
|                      |        |     |                                           | 1                       |     | 2   |     |     |     | 3   |
| -------------------- | ------ | --- | ----------------------------------------- | ----------------------- | --- | --- | --- | --- | --- | --- |
| phép kết 2 quan hệ Q |        |     |  và Q                                     |  với điều kiện : D>=B  |     |     |     |     |     |     |
|                      |        |     | 1 2                                       |                         |     |     |     |     |     |     |
|                      | Q  = Q |     |  Q điều kiện là chọn ra các bộ thỏa D>=B  |                         |     |     |     |     |     |     |
|                      | 3      | 1   | 2                                         |                         |     |     |     |     |     |     |
|                      |        |     | Q                                         |                         |     |     |     | Q   |     |     |
|                      |        |     | 1                                         |                         |     |     |     |     | 2   |     |
|                      | A      |     | B                                         |                         | C   |     |     | D   | E   |     |
|                      | 1      |     | 2                                         |                         | 3   |     |     | 3   | 1   |     |
|                      | 4      |     | 5                                         |                         | 6   |     |     | 6   | 2   |     |
|                      | 7      |     | 8                                         |                         | 9   |     |     |     |     |     |
|                      |        |     |                                           |                         | Q   |     |     |     |     |     |
3
|     |     | A   | B   |     | C   |     | D   | E   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | 1   | 2   |     | 3   |     | 3   | 1   |     |     |
|     |     | 1   | 2   |     | 3   |     | 6   | 2   |     |     |
|     |     | 4   | 5   |     | 6   |     | 6   | 2   |     |     |
Các trường hợp đặc biệt:
Kết bằng: Nếu  là phép so sánh với phép toán bằng (=)
Kết tự nhiên: Là phép nối kết bằng trên các thuộc tính trùng tên trong Q  và Q .
1 2
(thường là phép kết giữa khóa chính và khóa ngoại nên có trùng tên). Quan hệ kết
quả không giữ các thuộc tính trùng.
| Ký hiệu:  Q |     | 3  = Q | 1    Q | 2   |     |     |     |     |     |     |
| ----------- | --- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
Ví dụ: Nối kết hai quan hệ: SinhVien và KetQuaHT dựa trên MSSV.
SinhVien(MSSV, MSLop, HoTen, NgaySinh, Phai)
KetQuaHT(MSSV, MSMon, HocKy, DiemL1,DiemL2)
| BangĐiem = (SinhVien  |     |     |     |  KetQua)  |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
Chúng ta có thể mở rộng phép kết dựa trên việc so sánh nhiều cặp thuộc tính với
các phép toán And, Or
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
| 22  |                              |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | BÀI 2: CƠ SỞ DỮ LIỆU QUAN HỆ |     |     |     |     |     |     |     |     |     |     |     |

Ví dụ:  kết 3 quan hệ SinhVien, KetQuaHT và MonHoc ta có:
MonHoc(MSMH, TenMH, SoTCLT, SoTCTH)
| BangĐiem = ((SinhVien  |     |     |     |     |  KetQua)  |     |  MonHoc)  |     |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --------- | --- | --------- | --- | --- | --- | --- | --- |
Kết trái: Là phép kết nối ưu tiên lấy hết các dòng dữ liệu từ quan hệ bên trái, các
dòng dữ liệu tương ứng của quan hệ bên phải nếu không có thì nhận giá trị NULL.
|     Ký hiệu: Q |     | 3 = Q 1  |        Q | 2   |     |     |     |     |     |     |     |     |
| -------------- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    Ví dụ:
|     |     |  Q     |     |        Q |     |       |     |     |     | Q     |       |     |
| --- | --- | ------ | --- | -------- | --- | ----- | --- | --- | --- | ----- | ----- | --- |
|     |     | 1      |     |          |     | 2     |     |     |     | 3     |       |     |
|     | X   | Z      |     |          | X   | Y     |     | X   |     | Z     | Y     |     |
|     | 1   | Z      |     |          | 1   | Y     |     | 1   |     | Z     | Y     |     |
|     |     | 1      |     |          |     | 1     |     |     |     | 1     | 1     |     |
|     | 2   | Z 2    |     |          | 2   | Y 2   |     | 2   |     | Z 2   | Y 2   |     |
|     | 3   | Z      |     |          | 4   | Y     |     | 3   |     | Z     | NULL  |     |
|     |     | 3      |     |          |     | 4     |     |     |     | 3     |       |     |

Kết phải: Là phép kết nối ưu tiên bên phải, quan hệ kết quả sẽ lấy hết các dòng
của quan hệ bên phải của phép kết nối. Sau đó các dòng tương ứng của quan hệ
bên trái sẽ được lấy, nếu dòng nào không có giá trị sẽ nhận giá trị NULL.
|     Ký hiếu: Q |     | = Q |          Q |     |     |     |     |     |     |     |     |     |
| -------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                |     | 3 1 |            | 2   |     |     |     |     |     |     |     |     |
    Ví dụ:
|                    Q |     | 1     |     |        Q |     | 2    |     |     |       | Q 3   |     |     |
| -------------------- | --- | ----- | --- | -------- | --- | ---- | --- | --- | ----- | ----- | --- | --- |
|                      | X   | Z     |     |          | X   | Y    |     | X   |       | Z     | Y   |     |
|                      | 1   | Z     |     |          | 1   | Y    |     | 1   |       | Z     | Y   |     |
|                      |     | 1     |     |          |     | 1    |     |     |       | 1     | 1   |     |
|                      | 2   | Z     |     |          | 2   | Y    |     | 2   |       | Z     | Y   |     |
|                      |     | 2     |     |          |     | 2    |     |     |       | 2     | 2   |     |
|                      | 3   | Z     |     |          | 4   | Y    |     | 4   | NULL  |       | Y   |     |
|                      |     | 3     |     |          |     | 4    |     |     |       |       | 4   |     |
2.2.2.4 PHÉP CHIA (DIVISION)
Định nghĩa: Cho 2 quan hệ Q (A , A , …, A , A , …, A ) và Q (A , A , …, A ), Q +
|     |     |     |     |     | 1   | 1 2 | p   | p+1 |     | n   | 2 1 2 | p 2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
Q +. Phép chia Q  cho Q  sẽ tạo thành quan hệ mới Q (A , …, A ) chứa các bộ mà
| 1   |     | 1   |     | 2   |     |     |     |     | 3   | p+1 | n   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
khi ghép nối những bộ đó với các bộ của Q 2  sẽ cho ra 1 bộ của Q 1 .
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
  23

BÀI 2: CƠ SỞ DỮ LIỆU QUAN HỆ

|            | Q  = {q / q | Q , q   | Q , q = q |     | .Q + và q |  = q | .Q +}  |     |
| ---------- | ----------- | -------- | ---------- | --- | --------- | ---- | ------ | --- |
|            | 3           | 2 2      | 1 1        | 1   | 3         | 2    | 1 2    |     |
| Ký hiệu: Q |  = Q        |   Q     |            |     |           |      |        |     |
|            | 3           | 1 2      |            |     |           |      |        |     |
Công dụng: Chọn ra những bộ con của một quan hệ có liện hệ đồng thời với tất cả
các bộ con của quan hệ khác.
Ví dụ: Chọn ra những sinh viên cùng có điểm môn CSDL là 8 và điểm CTDL là 7
|     | Q  = KetQuaHT  Q |     |     |     |     |     |     |     |
| --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
|     | 3                 |     | 2   |     |     |     |     |     |
        KetQuaHT                                Q                  Q
|       |        |       |     |        | 2   |       |     | 3   |
| ----- | ------ | ----- | --- | ------ | --- | ----- | --- | --- |
| Mssv  | MsMon  | Điểm  |     |        |     |       |     |     |
|       |        |       |     | MsMon  |     | Điểm  |     |     |
Mssv
| 01  | Csdl  | 8   |     |       |     |     |     |     |
| --- | ----- | --- | --- | ----- | --- | --- | --- | --- |
| 01  | Ctdl  | 7   |     | Csdl  |     | 8   |     | 01  |
| 02  | Csdl  | 8   |     |       |     |     |     |     |
|     |       |     |     | Ctdl  |     | 7   |     | 03  |
| 02  | Ctdl  | 9   |     |       |     |     |     |     |
| 03  | Csdl  | 8   |     |       |     |     |     |     |

| 03  | Ctdl  | 7   |     |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- |
2.2.2.5 PHÉP ĐỔI TÊN (RENAME)
Công dụng: Dùng để đặt lại tên cho một quan hệ hoặc tên thuộc tính hoặc cả hai.
| Ký hiệu:     ρ  |     | (R)  |     |     |     |     |     |     |
| --------------- | --- | ---- | --- | --- | --- | --- | --- | --- |
S(B1,B2,…,Bn)
Trong đó ký hiệu ρ là phép đổi tên quan hệ R với S là tên quan hệ mới và các B ,
1
| B , …, B |  là tên các thuộc tính mới từ quan hệ R.  |     |     |     |     |     |     |     |
| -------- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| 2        | n                                         |     |     |     |     |     |     |     |
    ρ (R): Chỉ đổi tên quan hệ R thành S, tên các thuộc tính vẫn giữ nguyên tên.
S
    ρ (B1,B2,…Bn) (R): chỉ đổi tên các thuộc tính của R thành B 1 ,B 2 ,…,B n  tên quan hệ
không thay đổi
Ví dụ: giả sử có quan hệ SV(MSV, HoTen, Ngaysinh, Phai)
Để đổi tên quan hệ SV thành quan hệ Sinh_Viên ta thực hiện lệnh:
    ρ (SV) ta có quan hệ mới Sinh_Viên(MSV, HoTen, Ngaysinh, Phai)
Sinh_Viên
2.2.2.6 PHÉP GOM NHÓM (GROUP BY)
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
24
BÀI 2: CƠ SỞ DỮ LIỆU QUAN HỆ
Công dụng: Phép gom nhóm sử dụng để nhóm các bộ trong một quan hệ theo một
giá trị của một số các thuộc tính của chúng, sau đó ta có thể áp dụng các hàm
thống kê một cách độc lập cho từng nhóm.
Ký hiệu:  ;  (Quan hệ)
<Các thuộc tính nhóm> <Các hàm thống kê>
Ví dụ: thực hiện yêu cầu: nhóm các bộ của quan hệ NHÂNVIÊN theo Mã_Phòng.
Như vậy, mỗi nhóm bao gồm các nhân viên cùng làm việc trong một phòng. Từ đó
ta có thể tính lương trung bình của nhân viên theo từng phòng
Nhân viên
Yêu cầu, Tính lương trung bình theo phòng?
Trả lời: ρ (  (NHÂN_VIÊN))
Lương_TB(Phòng, LươngTB) (Mã_Phòng) Mã_Phòng, Avg(Lương)
Lương_TB
Các hàm thống kê
❖ Tổng (SUM)
Ví dụ: sum(số_lương_tồn) cho kết quả là tổng số lượng tồn kho
❖ Trungbình (AVERAGE)
Ví dụ: Avg(Điểm) cho kết quả là điểm trung bình của các sinh viên
❖ Tính giá trị lớn nhất (MAX)
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
  25

BÀI 2: CƠ SỞ DỮ LIỆU QUAN HỆ

          Ví dụ: Max(Đơn_Giá) cho kết quả là đơn giá cao nhất
| ❖   | Giá trị bé nhất (MIN).   |     |     |     |     |     |
| --- | ------------------------ | --- | --- | --- | --- | --- |
            Ví dụ: Min(Đơn_Giá) cho kết quả là đơn giá thấp nhất
| ❖   | Hàm Đếm (COUNT) được sử dụng để đếm các bộ giá trị.  |     |     |     |     |     |
| --- | ---------------------------------------------------- | --- | --- | --- | --- | --- |
           Ví dụ: Count(MaSV) cho kết quả là tổng số sinh viên hiện có
Một số ví dụ: Xét 1 lược đồ CSDL như sau:
|     | HH(MSHH, TenHH, DVT, SoTon, ĐG)  |     |     |     |     |     |
| --- | -------------------------------- | --- | --- | --- | --- | --- |
KH(MSKH, TenKH, DC, DT, Fax)
DDH(SoDDH, NgayLap, MSKH)
CTDDH(SoDDH, MSHH, SL, Dg)
Câu hỏi 1: Cho biết danh sách các khách hàng gồm (TenKH, DC, DT) đã đặt mặt
hàng có mã số 01
|     |              | ((DDH |  KH) |                  |     | (CTDDH))  |
| --- | ------------- | ----- | ---- | ----------------- | --- | --------- |
|     | TenKH, DC, DT |       |      | CTDDH.MSHH = ’01’ |     |           |
Câu hỏi 2: Cho biết các CTDDH của DDH có số đơn đặt hàng là 111 gồm: TenHH,
DVT, SL, Dg.
|     |                   | (HH |                    |     | (CTDDH))  |     |
| --- | ------------------ | --- | ------------------- | --- | --------- | --- |
|     | TenHH, DVT, SL, Dg |     | CTDDH.SoDDH = "111" |     |           |     |
   Câu hỏi 3: Cho biết doanh thu của mặt hàng có mã =’03’
|          ρ  |              |  (        |  (  |              | (CTDDH)))  |     |
| ----------- | ------------ | ---------- | ---- | ------------ | ---------- | --- |
|             | Q(Doanh thu) | sum(SL*Dg) |      | MSHH = ’03’  |            |     |

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
26
BÀI 2: CƠ SỞ DỮ LIỆU QUAN HỆ
BÀI TẬP
Bài 1: Cho một phần CSDL quản lý đặt hàng như sau :
Khách_Hàng(MãKH,TênKH,ĐịaChỉ,ĐiệnThoại)
Diễn giải: Trong quan hệ khách hàng gồm có các thông tin: Mã khách hàng(MãKH)
để phân biệt các khách hàng với nhau, tên khách hàng(TênKH), địa chỉ của khách
hàng (ĐịaChỉ) và điện thoại của khách hàng (ĐiệnThoại).
Đơn_Đặt_Hàng(Số_ĐĐH,NgàyĐặt,MãKH)
Diễn giải: Trong quan hệ đơn đặt hàng gồm các thông tin: Số đơn đăt
hàng(Số_ĐĐH) để phân biệt các đơn đặt hàng, ngày đặt (NgàyĐặt) và mã khách
hàng (MãKH).
CT_ĐĐH(Số_ĐĐH,MãHg,SL,ĐG_Bán)
Diễn giải: Trong quan hệ chi tiết đơn đặt hàng (CT_ĐĐH) gồm các thông tin: Số đơn
đặt hàng (Số_ĐĐH) và mã hàng (MãHg) để xác định hai bộ dữ liệu khác nhau, số
lượng bán (SL) và đơn giá bán (ĐG_Bán) mặt hàng đó.
Mặt_Hàng(MãHg,TênHg,SL_Tồn,ĐG_Mua)
Diễn giải: Trong quan hệ mặt hàng gồm các thông tin : mã hàng (MãHg) để phân
biệt các mặt hàng, tên hàng (TênHg), số lượng tồn (SL_Tồn) của mặt hàng và đơn
giá mua mặt hàng đó (ĐG_Mua).
Câu hỏi: Hãy trả lới các câu hỏi sau bằng ngôn ngữ đại số quan hệ.
a. Cho biết tên khách hàng đã đặt mua tất cả các mặt hàng?
b. Cho biết tên các mặt hàng mà chưa có ai đặt mua?
c. Cho biết tên các khách hàng đã đặt hàng trong ngày 20/11/2011?
d. Cho biết số lượng các mặt hàng đã được đặt trong ngày 12/05/2013?
e. Cho biết tên khách hàng đã đặt mua hơn 10 mặt hàng (tại nhiều chi tiết khác
nhau)?
Bài 2: Cho một phần CSDL quane lý sinh viên như sau:
SinhViên(MãSV, TênSV, NS, Phái, ĐịaChỉ)
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
27
BÀI 2: CƠ SỞ DỮ LIỆU QUAN HỆ
Diễn giải : mỗi sinh viên có một mã số để phân biệt (MãSV), một tên sinh viên
(TênSV), một ngày sinh (NS), thuộc một phái (Phái) và có địa chỉ để liên lạc(ĐịaChỉ)
MônHọc(MãMH, TênMH, SốTiếtLT, SốTiếtTH)
Diễn giải: mỗi môn học có một mã số để phân biệt (MãMH), có tên môn học
(TênMH) và có số tiết lý thuyết (SốTiếtLT) luôn lớn hơn hay bằng số tiết thực hành
(SốTiếtTH)
KếtQuả(MãSV, MãMH, Điểm)
Diễn giải: mỗi kết quả của sinh viên cho từng môn học (Điểm) được xác định bới
MãSV và MãMH.
Ghi chú : Khóa của các quan hệ được gạch dưới
Câu hỏi: Hãy trả lời các câu hỏi sau bằng ngôn ngữ đại số quan hệ.
a. Cho biết tên các sinh viên có điểm môn học có mã môn là ‘CSDL’ dưới 5 ?
b. Cho biết tên môn học và điểm các môn học của sinh viên ‘Nguyễn Văn An’?
c. Cho biết tên các môn học chưa thi (chưa có điểm của sinh viên)?
d. Cho biết tên sinh viên đã thi môn ‘Kỹ thuật lập trình’?
e. Cho biết tên các môn học có số tiết lý thuyết bằng số tiềt thực hành?
f. Cho biết tên các sinh viên có điểm trung bình cao nhất?
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
28
BÀI 3: NGÔN NGỮ HỎI CÓ CẤU TRÚC
BÀI 3: NGÔN NGỮ HỎI CÓ CẤU TRÚC
Ngôn ngữ hỏi có cấu trúc (SQL - Structured Query Language) là ngôn ngữ truy vấn
dữ liệu của công ty IBM phát triển vào thập niên 70, Được ANSI công nhận và phát
triển thành một ngôn ngữ chuẩn quốc tế vào năm 1986.
Khởi đầu SQL được gọi là SEQUEL (Structured English QUEry Language). Bản cài đặt
đầu tiên: SYSTEM R của IBM được thực hiện vào năm 1978.
Chuẩn mới (SQL-99) được cài đặt trong hầu hết các hệ quản trị CSDL cho phép
người sử dụng: Truy vấn dữ liệu, cặp nhật dữ liệu, thao tác với các đối tượng dữ liệu
như Table, Index, Procedure,…
SQL là một ngôn ngữ truy vấn có cấu trúc, được sử dụng để lưu trữ, thao tác và truy
xuất dữ liệu được lưu trữ trong một cơ sở dữ liệu quan hệ. SQL được sử dụng rộng rãi
trong các hệ thống quản lý cơ sở dữ liệu quan hệ như: MySQL, Oracle, Microsoft SQL
Server, PostgreSQL, SQLite và nhiều hệ thống khác. SQL cho phép bạn truy cập và
thao tác với các cơ sở dữ liệu để tạo, xóa, sửa đổi và trích xuất dữ liệu. Ngoài ra, SQL
còn được sử dụng để tạo các báo cáo, thống kê và phân tích dữ liệu.
3.1 TRUY VẤN DỮ LIỆU VỚI CÂU LỆNH SELECT
3.1.1 Cú pháp:
SELECT [predicate] { * | table.* | <Danh sách Field>
FROM <Danh sách Quan hệ>
[WHERE <Điều kiện> ]
[GROUP BY <Danh sách Thuộc tính> ]
[HAVING <Điều kiện của nhóm> ]
[ORDER BY Field1 [ACS|DESC],... ]
Công dụng: Tạo ra 1 quan hệ mới từ các quan hệ ghi sau từ khóa From.
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
29
BÀI 3: NGÔN NGỮ HỎI CÓ CẤU TRÚC
predicate: [ALL | DISTINCT | DISTINCTROW | [TOP n [PERCENT]]]
<Danh sách Field>: Thể hiện phép chiếu trên tập thuộc tính. Tên 1 thuộc tính của
quan hệ tham gia: [table].Field
Mở rộng: Có thể là một biểu thức: <Biểu thức> As <Alias> Trong đó, sử dụng các
toán tử số học như: ^, *, /, \ (chia nguyên), MOD, +, - và có thể là các hàm thống
kê như: sum, count, avg, …
Ví dụ: Cho lược đồ CSDL quản lý bán hàng:
HH(MSHH, TenHH, DVT, SoTon, ĐG)
KH(MSKH, TenKH, DC, DT, Fax)
DDH(SoDDH, NgayLap, MSKH)
CTDDH(SoDDH, MSHH, SL, Dg, GiamGia)
Câu hỏi 1: Hiện danh sách các mặt hàng gồm các thông tin: MSHH, TenHH, SoTon
SELECT MSHH, TenHH, SoTon FROM HH;
Câu hỏi 2: Tính tiền bán từng mặt hàng cho từng hóa đơn trong CTDDH:
SELECT SoDDH,MSHH,SL,Dg,GiamGia,SL*DG-GiamGia as ThanhTien
FROM CTDDH;
3.1.2 Mệnh đề Order By
Sắp thứ tự các bộ theo giá trị tăng hoặc giảm của các thuộc tính xuất hiện sau từ
khóa Order by (Giá trị mặc định là tăng dần).
Câu hỏi 3: Tính tiền bán từng mặt hàng trong CTDDH và sắp thứ tự giảm dần theo
thành tiền bán hàng.
SELECT SoDDH, MSHH, SL, Dg, GiamGia, SL*DG-GiamGia as ThanhTien
FROM CTDDH
Order By ThanhTien Desc
3.1.3 Mệnh đề Where
Dùng chọn ra những bộ thỏa một hoặc nhiều điều kiện cho trước
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
30
BÀI 3: NGÔN NGỮ HỎI CÓ CẤU TRÚC
Điều kiện: Được thiết lập với các toán tử:
a. So sánh: =, <>, >, <, >=, <=.
Ví dụ: Hiện danh sách các mặt hàng có số lượng tồn kho < 10 gồm các thông tin:
MSHH, TenHHH, SoTon:
SELECT MSHH, TenHHH, SoTon FROM HangHoa Where SoTon < 10;
b. Logic: And, Or, Not.
Ví dụ: Hãy Liệt kê những DDH được lập trong tháng 10 năm 1999:
SELECT * FROM DDH
Where NgayLap>=’1/10/1999’ and NgayLap <= ‘30/10/1999’;
Ví dụ: Hiển thị danh sách các CTDH với các thông tin: SoDDH, TenHang, SL,
GiaBan, ThanhTien trong đơn đặt hàng có số là 10001
SELECT SoDDH, TenHH, SL, DG as GiaBan, GiaBan* SL As ThanhTien
FROM CTDH, DDH
Where CTDDH.SoDDH = DDH.SoDDH and DDH.SoDDH = ‘10001’;
c. Thuộc miền giá trị: <biểu thức> [Not] Between Value1 And Value2
Chức năng: So sánh giá trị biểu thức thuộc miền giá trị [Value1, Value2].
Ví dụ: Danh sách các mặt hàng có đơn giá từ 20 đến 50
Select * From HH Where DG Between 20 And 50;
d. Thuộc tập giá trị: <biểu thức> [Not] In (Value Set)
Chức năng: Kiểm tra giá trị biểu thức thuộc tập giá trị cho trước.
Ví dụ: Danh sách các khách hàng có mã số 3, 6, 9
Select * From KH Where MSKH in (3,6,9);
Ví dụ: Danh sách các khách hàng đặt hàng ngày 1/5/2000
Select Distinct *
From KH
Where MSKH in (Select MSKH From DDH Where NgayLap = ‘1/5/2000’)
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
31
BÀI 3: NGÔN NGỮ HỎI CÓ CẤU TRÚC
Ví dụ: Danh sách các mặt hàng không bán được
Select * From HH Where MSHH not in (Select MSHH From CTDH)
e. Not Exists (Subquery): Chọn ra các bộ có giá trị field thỏa điều kiện trong Sub
Query
Ví dụ: Cho biết danh sách các mặt hàng không bán được
Select * From HH as A
Where Not Exists (Select * From CTDH as B Where A.MsHH = B.MsHH)
Biểuthức <comparison> ALL (subquery): Kiểm tra giá trị thỏa phép so sánh với
tất cả các giá trị trong (sub query).
Ví dụ: In ra SoDDH và SL đã mua mặt hàng số 3 trong số các DDH đã mua mặt
hàng số 3 nhiều nhất.
Select A.SoDDH, A.SL
From CTDH As A
Where A.MsHH=3 and A.SL >= ALL
(Select B.SL From CTHH As B Where B.MSHH = 3)
f. Đối sánh mẫu với toán tử Like
Chức năng: So sánh giá trị biểu thức với ‘Mẫu’. Sử dụng ký tự đại diện ‘%’, ‘_’
Tróng đó % thay thế cho nhiều ký tự và _ thay thế cho một ký tự
Ví dụ: Chọn ra danh sách khách hàng họ ‘Nguyễn’
Select * From KH Where TenKH Like N‘Nguyễn%’
g. Biểuthức <comparison> ANY | SOME (subquery)
Kiểm tra giá trị thỏa phép so sánh với ít nhất 1 giá trị tạo bởi subquery.
Ví dụ: hiện tên khách hàng mua hàng ít nhất một lần trong năm 2014
Select TenKH
From KH
Where mskh any (select mskh from DDH where year(ngaylap)=2014)
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
32
BÀI 3: NGÔN NGỮ HỎI CÓ CẤU TRÚC
3.1.4 Phát biểu Group By và Having
Dùng tổng hợp, thống kê dữ liệu theo từng nhóm được hình thành dựa trên giá trị
của các thuộc tính xuất hiện sau từ khóa Group by. Trong đó, phát biểu Having
dùng chọn ra những nhóm thỏa điều kiện nào đó.
Các hàm tổng hợp theo nhóm:
Sum(Biểu thức): Tính tổng giá trị các biểu thức số trên các bộ thuộc nhóm
Max(Biểu thức): Chọn ra giá trị lớn nhất trên các bộ thuộc nhóm
Min(Biểu thức): Chọn ra giá trị thấp nhất trên các bộ thuộc nhóm
Avg(Biểu thức): Tính trung bình cộng giá trị biểu thức trên các bộ thuộc nhóm
Count(* | Biểu thức | Distinct Biểu thức): Đếm các bộ trong từng nhóm.
Count(*): Đếm tất cả các bộ kể cả những bộ có tất cả các thuộc tính đều = NULL
Count(biểu thức): Chỉ đếm những bộ mà có giá trị biểu thức khác NULL.
Count(Distinct Biểu thức): Chỉ đếm những bộ mà có giá trị biểu thức khác nhau
và khác NULL.
Ví dụ: Đếm tổng số DDH của từng khách hàng:
Select MSKH, Count(*) Form DDH Group By MSKH
Ví dụ: Liệt kê danh sách DDH và số tiền của mỗi DDH:
Select SoDDH, Sum(DG*SL) From CTDH Group By SoDDH
Ví dụ: Liệt kê danh sách DDH và số tiền của mỗi DDH nhưng chỉ hiện những DDH có
tổng trị giá > 5000.
Select SoDDH, Sum(DG*SL) From CTDH
Group By SoDDH Having Sum(DG*SL)>5000
3.1.5 Thứ tự dịch của lệnh Select:
From --> Where --> Group By --> Having --> Select --> Order
Ví dụ: Hiển thị danh sách các khách hàng có tổng trị giá mua trên 10 triệu
Select KH.MSKH, TenKH, Sum(DG*SL) As TongTien
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
33
BÀI 3: NGÔN NGỮ HỎI CÓ CẤU TRÚC
From KH, CTDH, DDH
Where KH.MSKH = DDH.MSKH and DDH.SoDDH=CTDH.SoDDH
Group By KH.MSKH, TenKH
Having Sum(DG*SL)>100000.
3.2 CÁC LỆNH ĐỊNH NGHĨA DỮ LIỆU:
3.2.1 Lệnh Tạo Cấu Trúc Quan Hệ Mới:
Cú pháp: CREATE TABLE <Tên Quan Hệ>
(field1 type [(size)] [NOT NULL] [index1]
[, field2 type [(size)] [NOT NULL] [index2] [, ...]]
[, CONSTRAINT multifieldindex [, ...]])
Một số kiểu dữ liệu thường sử dụng:
Char(n) Kiểu chuỗi gồm n ký tự, mặc định là 1
Integer Số nguyên 4 byte
Smallint Số nguyên 2 byte
Bigint Số nguyên lớn 8 byte
Real số thực 4 byte
Float, Double số thực 8 byte
Date, Time Ngay giờ
Boolean 1 Bit
Varchar(v) Kiểu chuỗi gồm n ký tự
Nvarchar(n) Kiểu chuỗi gồm n ký tự có sử dụng unicode
Ví dụ: Tạo quan hệ Nhanvien(msnv, HoTen, NS, Nu, HsLg)
Create Table Nhanvien (msnv Char(5), HoTen Char(30), NS Date, Nu Boolean, HsLg
Float);
Các biểu thức ràng buộc:
Ràng buộc liên quan đến 1 thuộc tính:
CONSTRAINT name {PRIMARY KEY : Khóa chính | UNIQUE |: không lặp lại giá trị
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
34
BÀI 3: NGÔN NGỮ HỎI CÓ CẤU TRÚC
REFERENCES foreigntable [(foreignfield1, foreignfield2)]}: Ràng buộc tồn tại
NOT NULL: Không thể rỗng
Check (điều kiện): Ràng buộc miền giá trị. Điều kiện có thể là một biểu thức hoặc
danh sách giá trị.
Ví dụ:
Create Table NV (msnv varchar(5) Primary Key, HoTen Nvarchar(30) Not Null,
NgaySinh date, Phái Boolean, Hệsốlương Float);
Ràng buộc quan hệ: Liên quan đến nhiều thuộc tính.
Primary Key (f , …, f ):
1 n
Unique (f , …, f )
1 n
Foreign Key (f , …, f ) References tenQH2 [(fg , …, fg )]
1 n 1 n
Check (điềukiện)
Ví dụ: Create Table NV (msnv Char(5) Not Null, HoTen Char(30) Not Null, NS Date,
Nu Boolean, HsLg Float, Primary Key(msnv));
Access: CONSTRAINT name {PRIMARY KEY (primary1[, primary2 [, ...]]) |
UNIQUE (unique1[, unique2 [, ...]]) |
FOREIGN KEY (ref1[, ref2 [, ...]]) REFERENCES foreigntable [(foreignfield1 [,
foreignfield2 [, ...]])]}
Ví dụ: Create Table NV (msnv Char (5) Not Null Constraint rb1 Primary Key(msnv),
HoTen Char (30) Not Null,
NS Date,
Phai Boolean,
HsLg Float,
MsPB Char (5) Not Null Constraint References PhBan (MP));
Hay có thể viết:
Create Table NV (msnv Char (5) Not Null,
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
35
BÀI 3: NGÔN NGỮ HỎI CÓ CẤU TRÚC
HoTen Char (30) Not Null,
NS Date, Phai Boolean,
HsLg Float,
MsPB Char (5) Not Null,
Constraint RB1 Primary Key(msnv),
Constraint RB2 Foreign Key (MsPB) References PhBan (MP))
3.2.2 Lệnh Xóa Một Quan Hệ:
DROP TABLE <TênQH>
Ví dụ: Drop table NhanVien
3.2.3 Lệnh Thay Đổi Cấu Trúc Của Quan Hệ:
Cú pháp:
a. Thêm thuộc tính:
ALTER TABLE TenQH ADD COLUMN fieldname type[(size)]
[NOT NULL] [CONSTRAINT <index>];
b. Xóa thuộc tính:
ALTER TABLE TênQH DROP COLUMN fieldname;
Chú ý: Lệnh không hợp lệ nếu thuộc tính được xóa là thuộc tính khóa.
3.2.4 Các Lệnh cập nhật dữ liệu:
a. Thêm bộ mới vào bảng:
Cú pháp 1: INSERT INTO TenQH VALUES (value1[, value2[, ...])
Ví dụ: Thêm một nhân viên mới
INSERT INTO NHANVIEN VALUES (5, 'Anh', #1/5/78#)
Cú pháp 2: Thêm 1 bộ với các giá trị không đầy đủ (Các Field không liệt kê sẽ có giá
trị NULL). INSERT INTO TenQH [(field1[, field2[, ...]])]
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
36
BÀI 3: NGÔN NGỮ HỎI CÓ CẤU TRÚC
VALUES (value1[, value2[, ...]);
Ví dụ: Thêm 1 nhân viên mới chỉ biết Msnv, Tên, Giới tính
INSERT INTO NHANVIEN (Msnv, Ten, GT) VALUES (5, 'Anh', 'Nam')
Cú pháp 3: Thêm vào QH các bộ là kết quả của câu lệnh Select.
INSERT INTO TenQH [(field1[, field2[, ...]])]
SELECT [source.] field1[, field2[, ...] FROM table_expression...;
Ví dụ: Chèn các dòng đặt hàng của DDH = 12 vào bảng CTGiaoHang
INSERT INTO CTGiaoHang (SoDDH, MSHH,SL,DG)
SELECT SoDDH, MSHH, SL, DG FROM CTDH WHERE SoDDH = 12
b. Xóa các bộ của một quan hệ
DELETE FROM TênQH [WHERE <điều kiện>];
Ví dụ: Xóa các DDH trước ngày 1/1/2000
DELETE FROM DDH WHERE NgayLHD <= ‘1/1/2000’
c. Cập nhật giá trị của các bộ
UPDATE tênQH SET <Field1>=<BT1>,<Field2>=<BT2>...
WHERE <ĐiềuKiện>;
Ví dụ: Cập nhật đơn giá của sản phẩm 2,4,6 lên 5%
UPDATE HH SET DonGia = [DonGia]*1.05 WHERE Mshh In (2,4,6);
d. Hội các bộ của các quan hệ
[TABLE] query UNION [ALL] [TABLE] query UNION [ALL] [TABLE]… query [...]
1 2 n
Ví dụ: Tạo quan hệ chứa danh sách các DDH tháng 1/99 và tháng 4/99
Select * from DDH Where ngaylap between ‘1/1/99’ and ‘31/1/99’
union
Select * from DDH
Where ngaylap between ‘1/4/99’ and ‘30/4/99’
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
37
BÀI 3: NGÔN NGỮ HỎI CÓ CẤU TRÚC
BÀI TẬP
Bài 1: Địa Lý Việt Nam Cho CSDL địa lý có cấu trúc như sau:
Tinh_TP (T_TP, DT, DS, Ten_T, Mien)
Bien_Gioi (Nuoc, T_TP)
Lang_Gieng (T_TP, T_TP_LG)
Hãy trả lời các câu hỏi sau bằng ngôn ngữ SQL
1. Cho biết dân số cùng tên tỉnh của các tỉnh thành phố có diện tích 7000 km2.
2. Cho biết dân số cùng với tên tỉnh của các tỉnh miền Bắc
3. Cho biết mã các nước biên giới của các tỉnh miền Nam
4. Cho biết diện tích trung bình của các tỉnh
5. Cho biết mật độ dân cư cùng tên tỉnh của tất cả các tỉnh
6. Cho biết tên những tỉnh có diện tích có 1 diện tích lớn hơn tất cả các tỉnh láng
giềng của nó.
7. Cho biết tên những tỉnh mà ta có thể đến bằng cách đi từ TP HCM xuyên qua 3
tỉnh khác nhau và cũng khác với điểm xuất phát, nhưng láng giềng với nhau.
Giải
Câu 1: Select Ten_T, DS From Tinh_TP Where DT>=7000
Câu 2: Select Ten_T, DS From Tinh_TP
Where Mien.T_TP= Tinh_TP.T_TP And Mien=N’Bắc’;
Câu 3: Select Nuoc From Bien_Gioi, Tinh_TP
Where Tinh_TP.T_TP= Bien_Gioi.T_TP And Mien=N’Nam’
Câu 4: Select AVG(DT) From Tinh_TP;
Câu 5: Select Ten_T, DS / DT As MDDC From Tinh_TP;
Câu 6: Select a.TenTinh, a.DT From Tinh_TP as a
WHERE a.DT>All (Select max(b.DT) From Tinh_TP b, LG c
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
38
|     | BÀI 3: NGÔN NGỮ HỎI CÓ CẤU TRÚC |     |
| --- | ------------------------------- | --- |

           Where b.T_TP = c.T_TP_LG and a.T_TP=c.T_TP);
Bài 2: Thể Thao Đội Cho CSDL có cấu trúc như sau:
Thuộc tính:
| Tên tắc  | Diễn giải                 | Miền giá trị           |
| -------- | ------------------------- | ---------------------- |
| MsCLB    | Mã số câu lạc bộ          | Nguyên (1..100)        |
| DcCLB    | Địa chỉ CLB               | Văn bản                |
| MsDoi    | Mã số đội                 | Nguyên (1..50)         |
| MsLT     | mã số lứa tuổi            | {LT1<LT2<LT3<LT4<LT5}  |
| Phai     | Phái, giới tính           | Mã {"Nam", "Nữ"}       |
| MsTD     | Mã số trận đấu            | Nguyên                 |
| GioTD    | Giờ bắt đầu trận đấu      | Time                   |
| NgayTD   | Ngày diễn ra trận đấu     | Date                   |
| MsPh     | Mã số phòng thi đấu       | Nguyên                 |
| DcPh     | Địa chỉ phòng             | Văn bản                |
| SoSan    | Số lượng sân của 1 phòng  | Nguyên (1,5)           |
TGTĐ_LT  Thời gian thi đấu phù hợp cho 1 lứa tuổi  (đvt là phút)
|         | Nguyên (0,20)          |          |
| ------- | ---------------------- | -------- |
| MsVĐV   | Mã số vận động viên    | Nguyên   |
| TenVDV  | Tên vận động viên      | Văn bản  |
| DcVDV   | Địa chỉ vận động viên  | Văn bản  |
Quan hệ:
1.  CLB( MsCLB , DcCLB)
Tân từ: Mỗi CLB có 1 mã số (MSCLB) để phân biệt với các CLB khác, và địa chỉ của
CLB  (DcCLB)
2.  DOI(MsCLB, MsDoi, MsLT, Phai)
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
39
BÀI 3: NGÔN NGỮ HỎI CÓ CẤU TRÚC
Tân từ: Mỗi đội có 1 mã số đội (MsDoi) để phân biệt với các đội khác của cùng một
Câu lạc bộ (MsCLB); Mỗi đội thuộc về 1 lứa tuổi duy nhất (MsLT) và một phái (nam
hay nữ). Tất cả các vận động viên của đội phải có cùng lứa tuổi của đội hoặc thấp
hơn lứa tuổi của đội.
3. TD(MsTD, MsPh, GioTD, NgayTD)
Tân từ: Mỗi trận đấu có 1 mã số (mstd) để phân biệt với những trận đấu khác, diễn ra
trong 1 phòng, vào 1 ngày (NgayTD) và bắt đầu ở một giờ (GioTD) đã quy định.
4. DOI_TD(MsTD, MsDoi, MsCLB)
Tân từ: Mỗi trận đấu là một cuộc gặp gỡ giữa 2 đội. Cả 2 đội phải thuộc cùng 1 lứa
tuổi và cùng một phái.
5. PHÒNG(MsPh, DCPh, SốSân)
Tân từ: Mỗi phòng có 1 mã số (MSPh) để phân biệt với các phòng khác, có 1 địa chỉ
và 1 số lượng sân (SốSân) nhất định, nơi đó có thể diễn ra các trận đấu.
6. LỨA_TUỔI(MsLT, TGTĐ_LT)
Tân từ: Mỗi lứa tuổi được phân biệt bởi mã lứa tuổi (MsLT) và có thời gian trận đấu
dành cho lứa tuổi đó.
7. VĐV(MsVDV, TenVDV, DcVDV, MsCLB, Phai, MsLT)
Tân từ: Mỗi vận động viên có 1 mã số (MsVDV) dùng để phân biệt với các VDV khác,
có 1 tên, 1 địa chỉ, thuộc 1 CLB, 1 phái và 1 lứa tuổi.
8. VĐV_ĐỘI(MsVDV, MsDoi)
Tân từ: Mỗi VĐV đăng ký chơi ở 1 đội. Họ có thể đăng ký vào nhiều đội khác nhau.
Yêu cầu:
1. Hãy xác định khóa của các quan hệ từ tân từ của các quan hệ
2. Thực hiện các câu hỏi sau:
a. Danh sách tên các VĐV của CLB có mả số 45
b. Tên tất cả các VĐV của đội số 3 của CLB mã số 27
c. Số lượng các trận đấu LT1 diễn ra ngày 16/06/90
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
40
BÀI 3: NGÔN NGỮ HỎI CÓ CẤU TRÚC
d. Mã số các CLB và mã số các đội trong đó có quy tụ các VĐV thuộc 1 lứa tuổi nhỏ
hơn lứa tuổi của đội.
e. Địa chỉ và mã số các CLB có 1 hay nhiều đội tham dự trận đấu diễn ra trong
phòng mã số 17 ngày 06/12/90.
f. Danh sách các trận đấu bắt đầu hoặc kết thúc trong khỏng thời gian từ 13g và
16g diễn ra trên 1 sân của phòng mã số 49 ngày 05/08/90
g. Địa chỉ và tên các vận động viên đã chơi hoặc sẽ chơi đối lại đội mã số 1 của các
CLB mã số 50.
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
41
BÀI 4: RÀNG BUỘC TOÀN VẸN
BÀI 4: RÀNG BUỘC TOÀN VẸN
Trong bài này, chúng ta sẽ học về: ràng buộc toàn vẹn và kiểm tra ràng buộc toàn
vẹn (RBTV) là hai trong số những vấn đề quan trọng của qúa trình phân tích, thiết
kế và khai thác CSDL. Trong quá trình phân tích, thiết kế CSDL, nều không quan
tâm đúng mức đền các vấn đề của RBTV, có thể sẽ dẫn đến những hậu quả nghiêm
trọng về tính an toàn và toàn vẹn của dữ liệu. Đặc biệt đối với các CSDL lớn.
Vì vậy, khi xây dựng một chương trình ứng dụng, ngoài việc xây dựng các quan hệ
để lưu trữ các đối tượng dữ liệu cần quản lý, người phân tích, thiết kế còn phải nắm
rõ các quy tắc quản lý áp đặt trên các đối tượng dữ liệu đó, các quy tắc đó gọi là
RBTV. Người phân tích, thiết kế phải phát hiện đầy đủ và mô tả một cách chính xác,
rõ ràng trong hồ sơ thiết kế. Đồng thời chỉ rõ các thao tác cặp nhận dữ liệu nào cần
được kiểm tra xử lý vi phạm RBTV, nhằm đảm bảo cho CSDL luôn được biểu diễn
chính xác và đúng ngữ nghĩa của thực tế.
4.1 CÁC YẾU TỐ CỦA RBTV
4.1.1 Khái niệm
Ràng buộc toàn vẹn là những điều kiện ràng buộc giá trị trên một thuộc tính hoặc
giữa các thuộc tính, giữa các bộ trong một hay nhiều quan hệ. Các ràng buộc này là
bất biến, thỏa mãn ở bất kỳ thời điểm nào khi khai thác CSDL.
Ví dụ: Cho CSDL bán hàng gồm các quan hệ
HangHoa (MSHH, TenHH, DVT, SoTon, ĐG)
KhachHang (MSKH, TenKH, DC, DT, Fax)
DonDatHang (SoDDH, NgayLap, MSKH)
ChiTietDonDatHang (SoDDH, MSHH, SL, Dg, GiamGia)
Dựa vào tân từ ta có một số ràng buộc toàn vẹn như:
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
42
BÀI 4: RÀNG BUỘC TOÀN VẸN
RB : Mỗi mặt hàng phải có một mã số để phân biệt với các mặt hàng khác.
1
RB : Mỗi CTDDH (chi tiết đơn đặt hàng) phải có mã hàng phân biệt trong cùng một
2
đơn hàng và mã hàng phải thuộc danh sách các mặt hàng có trong quan hệ MH.
RB : Giá trị của các thuộc tính SoTon, Dg,SL, GiamGia phải ≥ 0.
3
4.1.2 Các yếu tố của RBTV:
Một RBTV có 3 yếu tố: Bối cảnh, điều kiện và tầm ảnh hưởng của RBTV.
a. Bối cảnh của RBTV:
Là các quan hệ mà RBTV được định nghĩa
b. Điều kiện:
Mô tả điều kiện của ràng buộc mà dữ liệu của các quan hệ xuất hiện trong bối cảnh
của ràng buộc đó phải thỏa.
Điều kiện có thể được biểu diễn bằng ngôn ngữ tự nhiên, mã giả (tựa Pascal), ngôn
ngữ đại số tập hợp, ngôn ngữ vị từ ...
c. Tầm ảnh hưởng:
Chỉ định những thao tác cơ sở (thêm, xóa, sửa) trên những quan hệ nào thuộc bối
cảnh RBTV có thể gây nên nguy cơ vi phạm điều kiện ràng buộc, cần phải được kiểm
tra khi thực hiện thao tác đó (dấu ‘+’ là phải kiểm tra, dấu ‘–‘ là không phải kiểm tra).
Ví dụ: RB1: Mỗi mặt hàng phải có 1 mã số phân biệt với các mặt hàng khác
HangHoa (MSHH, TenHH, DVT, SoTon, ĐG)
Bối cảnh: HangHoa
Điều kiện: q, q  HangHoa :
i j
q.MSHH <> q.MSHH => i ≠ j
i j
Tầm ảnh hưởng:
Thêm Xóa Sửa
HangHoa + - + [MSHH]
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

43
BÀI 4: RÀNG BUỘC TOÀN VẸN
4.2 PHÂN LOẠI CÁC RBTV
Dựa trên bối cảnh, RBTV có thể được chia làm 2 loại:
- RBTV có bối cảnh là 1 quan hệ
- RBTV có bối cảnh gồm nhiều quan hệ
4.2.1 RBTV có bối cảnh là một quan hệ
4.2.1.1 RBTV TRÊN MIỀN GIÁ TRỊ CỦA THUỘC TÍNH
Là ràng buộc qui định giá trị hợp lệ của một thuộc tính.
Ví dụ: KetQuaHT(MSSV, MSMon, DiemGK, DiemCK)
Tân từ: Điểm cuối kỳ lấy giá trị từ 0 đến 10 và có độ chính xác là 0.5
Bối cảnh: KetQuaHT
Điều kiện: 
lOMoARcPSD|56030397
q  T
ketQuaHT
(q.DiemCK= NULL) Or
(q.DiemCK >= 0 And q.DiemCK <=10 And (q.DiemCK * 4) mod 2 = 0)
Tầm ảnh hưởng:
Thêm Xóa Sửa
KetQuaHT + - + [DiemCK]
4.2.1.2 RBTV LIÊN THUỘC TÍNH:
Là mối liên hệ giữa các thuộc tính trên 1 bộ trong cùng 1 lược đồ quan hệ
Ví dụ: Lang_Gieng(T_TP, T_TP_LG)
Ràng buộc(RB): Mã số thành phố và mã số thành phố láng giềng phải khác nhau.
Bối cảnh: Lang_Gieng
Điều kiện: q  Lang_Gieng: q.T_TP <> q. T_TP_LG
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
| 44  |                           |     |     |     |     |
| --- | ------------------------- | --- | --- | --- | --- |
|     | BÀI 4: RÀNG BUỘC TOÀN VẸN |     |     |     |     |

Tầm ảnh hưởng:
|     |     |             | Thêm  | Xóa  Sửa              |     |
| --- | --- | ----------- | ----- | --------------------- | --- |
|     |     | Lang_Gieng  | +     | -  + [T_TP, T_TP_LG]  |     |
4.2.1.3 RBTV LIÊN BỘ:
Là sự ràng buộc giữa các bộ trong một quan hệ. Đặc biệt là các ràng buộc duy nhất
về giá trị của các thuộc tính khóa.
Ví dụ: Mỗi sinh viên học được nhiều môn, điểm thi mỗi môn phải có MSMom (Mã số
môn học) để phân biệt điểm thi các môn khác của 1 sinh viên.
KetQuaHT (MSSV, MSMon, DiemGK, DiemCK)
Bối cảnh: KetQuaHT
| Điều kiện:  |  q, q  KetQuaHT (i ≠ j):  |     |     |     |     |
| ----------- | --------------------------- | --- | --- | --- | --- |
|             | i                           | j   |     |     |     |
q.MSSV <> q.MSSV Or q.MSMon <> q.MSMon
|     |     | i   | j   | i   | j   |
| --- | --- | --- | --- | --- | --- |
Tầm ảnh hưởng:
|     |     |           | Thêm  | Xóa  Sửa            |     |
| --- | --- | --------- | ----- | ------------------- | --- |
|     |     | KetQuaHT  | +     | -  + [MSSV, MSMon]  |     |
4.2.2 RBTV Có bối cảnh trên nhiều quan hệ
4.2.2.1 RBTV PHỤ THUỘC TỒN TẠI (KHÓA NGOẠI)
Là điều kiện tồn tại 1 bộ trong 1 quan hệ (R) phụ thuộc vào sự tồn tại của 1 bộ nằm
trong 1 quan hệ khác (Q). Điều kiện tồn tại này dựa trên khóa của quan hệ Q nằm
trong quan hệ R. Còn được gọi là ràng buộc về khóa ngoại (Foreign key).
Ví dụ: Xét 2 quan hệ CTDDH và DDH, Mỗi chi tiết đặt hàng phải thuộc một DDH.
Bối cảnh: DDH, CTDDH
Điều kiện: CTDDH[SoDDH]  DDH[SoDDH] hay
|       | q  CTDHH:  q      |     |  DHH:  |     |     |
| ----- | -------------------- | --- | ------- | --- | --- |
|       | i                    |     | j       |     |     |
|       |   q.SoDDH = q.SoDDH  |     |         |     |     |
|       |                      | i   | j       |     |     |

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
  45

BÀI 4: RÀNG BUỘC TOÀN VẸN

Tầm ảnh hưởng:
|        |     | Thêm  Xóa  | Sửa        |
| ------ | --- | ---------- | ---------- |
| CTDDH  |     | +  -       | + [SoDDH]  |
| DDH    |     | -  +       | + [SoDDH]  |
4.2.2.2 RBTV LIÊN BỘ, LIÊN QUAN HỆ:
Là ràng buộc đối với từng nhóm các bộ của nhiều quan hệ khác nhau.
Ví dụ: Mỗi DDH (Đơn Đặt Hàng) chỉ bao gồm tối đa 5 mặt hàng khác nhau
Bối cảnh: DDH, CTDDH

Điều kiện:  q j   DHH :
Card({q  CTDDH : q.SoDDH = q.SoDDH}) ≤ 5
|     | i   | i   | j   |
| --- | --- | --- | --- |
Tầm ảnh hưởng:
|       |     | Thêm  Xóa  | Sửa        |
| ----- | --- | ---------- | ---------- |
| CTDH  |     | +  -       | + [SoDDH]  |
| DDH   |     | -  +       | + [SoDDH]  |
Ví dụ: Giả sử trên mỗi DDH có lưu trữ Tổng trị giá của DDH. Ta có ràng buộc như
sau: Tổng trị giá của 1 DDH phải bằng tổng giá trị của tất cả các mặt hàng trên DDH
đó.
Bối cảnh: DDH, CTDH
Điều kiện: ct  CTDDH,  dh  DDH:  ct.SoDDH = dh.SoDDH
       dh.TongGT = (ct.SL*ct.DG(1-ct.Giamgia)*100)
Tầm ảnh hưởng:
|        |     | Thêm  Xóa  | Sửa                |
| ------ | --- | ---------- | ------------------ |
| CTDDH  |     | +  +       | + [SL,DG,GiamGia]  |
| DDH    |     | +  +       | + [TongGT]         |
4.2.2.3 RBTV LIÊN THUỘC TÍNH, LIÊN QUAN HỆ
Là sự ràng buộc giữa các thuộc tính khác nhau trên các quan hệ khác nhau.
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

46
BÀI 4: RÀNG BUỘC TOÀN VẸN
Ví dụ: Trong CSDL bán hàng đã cho ta có ràng buộc đối với cùng mặt hàng, số lượng
bán trong CTDDH phải nhỏ hơn số lượng tồn trong quan hệ HH.
Bối cảnh: CTDDH, HH
Điều kiện: 
lOMoARcPSD|56030397
q  CTDDH , q  HH :
i j
q.MSMH = q.MSMH and q.SoTon>=q.SL
i j j i
Tầm ảnh hưởng:
Thêm Xóa Sửa
CTDDH + - + [SL]
HH - - + [SoTon]
4.2.2.4 RBTV DO ĐỒ THỊ LĐCSDL CÓ CHU TRÌNH:
Để thấy được mối liên hệ giữa các quan hệ trong một LĐCSDL, người ta thường biểu
diễn LĐCSDL bằng một đồ thị vô hướng, trong đó:
- Mỗi LĐQH được ký hiệu bởi 1 nút có dạng: 0
- Mỗi thuộc tính của LĐQH được ký hiệu bởi 1 nút dạng: *
- Giữa nút LĐQH và nút thuộc tính của nó được nối với nhau bởi 1 cung vô hướng.
Ví dụ: Từ cơ sở dữ liệu quản lý bán hàng
HH (MSHH, TenHH, DVT, SoTon, ĐG)
Quan hệ Hàng hóa (HH) có các thuộc tính (Mã số hàng hóa (MSHH), tên hàng hóa
(TENHH), đơn vị tính (DVT), số lượng tồn (SoTon) và đơn giá của mặt hàng đó (ĐG))
KH(MSKH, TenKH, DC, DT, Email)
Quan hệ khách hàng (KH) có các thuộc tính (Mã số khách hàng (MSKH), tên khách
hàng (TenKH), địa chỉ (DC), số điện thoại (DT) và email của khách hàng)
DDH(SoDDH, NgayLap, MSKH)
Quan hệ đơn đặt hàng (DDH) có các thuộc tính (số đơn đặt hàng (SoDDH), ngày lập
đơn đạt hàng (NgayLap) và mã số của khách hàng đặt đơn đặt hàng này (MSKH))
CTDDH(SoDDH, MSHH, SL, DG)
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
47
BÀI 4: RÀNG BUỘC TOÀN VẸN
Quan hệ chi tiết đơn đặt hàng (CTDDH) có các thuộc tính (số đơn đặt hàng (SoDDH),
mã số các mặt hàng có trong đơn đặt hàng (MSHH), số lượng đặt của mặt hàng theo
đơn đặt hàng (SL), đơn giá bán của mặt hàng theo đơn (DG))
Ta có đồ thị của lược đồ như sau:
HH 0
MSHH *
0 KH
CTDDH 0 * MSKH
SoDDH *
0 DDH
Chu trình của đồ thị LĐCSDL là một đường cong khép kín có ít nhất 3 đỉnh quan hệ
Ví dụ: cho CSDL quản lý phân công thực hiện đề án như sau:
NhânViên (MsNv, MsPh)
NV 0
QuanLy (MsPh, MsDa)
MsPh * * MsNv
PhânCông (MsNv, MsDa)
QL 0
Khi vẽ đồ thị ta thấy có chu trình
0 PC
Như hình bên.
MsDa *
Ràng buộc có chu trình là thể hiện sự phụ thuộc tồn tại của một bộ trong quan hệ này
với các bộ trong quan hệ khác có cùng chu trình. Trong ví dụ trên nếu chúng ta quản
lý theo 3 nguyên tắc khác nhau thì có thể có ràng buộc có chu trình.
Nguyên tắc quản lý 1: Mỗi nhân viên của phòng ban được phân công vào tất cả các
đề án mà phòng đó quản lý.
Nguyên tắc quản lý 2: Mỗi nhân viên của phòng ban được phân công làm các đề án
trong số các đề án mà phòng đó quản lý.
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
| 48  |                             |     |     |     |     |     |     |     |     |     |     |
| --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |   BÀI 4: RÀNG BUỘC TOÀN VẸN |     |     |     |     |     |     |     |     |     |     |

Nguyên tắc quản lý 3: Mỗi nhân viên được phân vào đề án bất kỳ tùy theo năng lực
chuyên môn.
Trường hợp theo nguyên tắc quản lý thứ 2 sẽ phát sinh ràng buộc có chu trình, vì lúc
này đề án phân cho nhân viên của phòng ban nào phải nằm trong số đề án mà phòng
ban đó quản lý.
Bối cảnh: PhânCông, NhânViên, QuảnLý
| Điều kiện: (PC  |     |     |  NV)[MaNv,MsDa]  (NV  |     |     |     |  QL)[MaNv, maDa]  |     |     |     |     |
| --------------- | --- | --- | ---------------------- | --- | --- | --- | ----------------- | --- | --- | --- | --- |
Tầm ảnh hưởng:
|     |     |     |           |     | Thêm  | Xóa  |                | Sửa  |     |     |     |
| --- | --- | --- | --------- | --- | ----- | ---- | -------------- | ---- | --- | --- | --- |
|     |     |     | PhânCông  |     | +     | -    | + [MaNv,MaDa]  |      |     |     |     |
|     |     |     | NhânViên  |     | -     | +    | + [MaNv,MaPh]  |      |     |     |     |
|     |     |     | QuảnLý    |     | -     | +    | + [MaDa,MaPh]  |      |     |     |     |
Bảng tầm ảnh hưởng tổng hợp: Là bảng tầm ảnh hưởng của tất cả các RBTV có trong
một CSDL. Người ta làm bảng tầm ảnh hưởng tổng hợp để người lập trình tiện theo
dõi khi cài đặt ứng dụng với CSDL đã được thiết kế.
Bảng tầm ảnh hưởng tổng hợp cùa một CSDL

|     | RB  |        | Q    |      |       | Q    |      | …   |       | Q    |      |
| --- | --- | ------ | ---- | ---- | ----- | ---- | ---- | --- | ----- | ---- | ---- |
|     |     |        | 1    |      |       | 2    |      |     |       | n    |      |
|     |     | Thêm   | Xóa  | Sửa  | Thêm  | Xóa  | Sửa  |     | Thêm  | Xóa  | Sửa  |
|     | RB  | 1   +  | -    | -    | -     | +    | +    |     |       |      |      |

|     | RB  |   -  | +   | +   |     |     |     |     | +   | +   | -   |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2
|     | …   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | RB  |     |     |     | +   | -   | +   |     |     |     |     |
|     | m   |     |     |     |     |     |     |     |     |     |     |

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
49
BÀI 4: RÀNG BUỘC TOÀN VẸN
BÀI TẬP
Bài 1: Cho CSDL sau
SinhViên(MãSV, TênSV, NS, Phái, ĐịaChỉ)
Diễn giải : Mỗi sinh viên có một mã số để phân biệt (MãSV), một tên sinh viên
(TênSV), một ngày sinh (NS), thuộc một phái (Phái) và có địa chỉ để liên lạc
MônHọc(MãMH, TênMH, SốTiếtLT, SốTiếtTH)
Diễn giải: mỗi môn học có một mã số để phân biệt (MãMH), có tên môn học (TênMH)
và có số tiết lý thuyết (SốTiếtLT) luôn lớn hơn hay bằng số tiết thực hành
(SốTiếtTH)
KếtQuả(MãSV, MãMH, Điểm)
Diễn giải: mỗi kết quả của sinh viên cho từng môn học (Điểm) được xác định bới
MãSV và MãMH.
Ghi chú : Khóa của các quan hệ được gạch dưới
Hãy phát biểu các ràng buộc toàn vẹn có trong cơ sở dữ liệu một cách chặt chẽ
Bài 2: Cho CSDL như sau
LOAI_XE(MãLX, TênLX)
Diễn giải : Mỗi loại xe (xe gắn máy 2 bánh, xe du lịch 4-7 chỗ, xe tải…) có một mã để
phân biệt(MãLX) và một tên gọi(TênLX)
CHỦ_XE(MãChủXe, TênChủXe, ĐịaChỉ )
Diễn giải : Mỗi chủ xe có một mã số để phân biệt, một tên, một địa chỉ.
GPLX(Số_GPLX, NgàyCấp_GPLX, MãChủXe)
Diễn giải : Mỗi giấy phép lái xe có một số để phân biệt, một ngày cấp và một người
chủ xe được cấp giấy phép lái xe
CT_GPLX(Số_GPLX, STT, NgàyCấp_CT, MãLX)
Diễn giải : Mỗi một chi tiết của một giấy phép lái xe có một số thứ tự để phân biệt với
những chi tiết khác của cùng một giấy phép, có ngày cấp cho chi tiết này và một mã
lọai xe.
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
50
BÀI 4: RÀNG BUỘC TOÀN VẸN
Ghi chú : - Khóa của các quan hệ được gach dưới.
- Ngày cấp của một chi tiết giấy phép lái xe có thể khác ngày cấp giấy phép lái xe, đó
là trường hợp chủ xe thi đậu một loại xe khác và được bổ sung giấy phép của loại xe
mới vào giấy phép đang có. Đối với mỗi giấy phép, các loại xe được cấp phép không
được trùng nhau.
Câu hỏi: Hãy phát biểu các ràng buộc toàn vẹn có trong cơ sở dữ liệu trên một cách
chặt chẽ.
Bài 3: Cho CSDL như sau
TOUR (#T,Tên_T,Gía_T_Người)
Diễn giải: Mỗi Tour du lịch có một mã số duy nhất (#T) để phân biệt, có một tên
duy nhất (Tên_T), một giá duy nhất cho một người đi tour (Gía_T_Người)
KHÁCH_CÁ_NHÂN (#KCN, Tên_KCN, #T, Ngày_Đi_Tour_KCN, #KĐ,
Bảng_Số_Xe, Ngày_BĐ_ĐI)
Diễn giải: Mỗi khách cá nhân có một mã số duy nhất (#KCN) để phân biệt với những
khác khác, một tên duy nhất (Tên_KCN), đăng ký đi một tour duy nhất – đó là tour
đăng ký sau cùng – (#T) vào một ngày (Ngày_Đi_Tour_KCN) và được phân vào một
xe duy nhất để đi tour (Bảng_Số_Xe, Ngày_BĐ_ĐI). Nếu khách cá nhân là thành
viên của một đoàn thì có một mã khách đoàn (#KĐ), nếu không đó là khách lẻ.
KHÁCH_ĐOÀN (#KĐ , Tên_Đ, TS_TV, #T, Ngày_Đi_Tour_KĐ)
Diễn giải : Mỗi đòan khách có một mã số duy nhất (#KĐ) để phân biệt với đòan
khách khác, một tên duy nhất (Tên_Đ), có một tổng số thành viên duy nhất
(TS_TV), đăng ký đi một tour duy nhất – đó là tour đăng ký sau cùng (#T) vào một
ngày (Ngày_Đi_ Tour_KĐ).
PC_XE (Bảng_Số_Xe, Ngày_BĐ_Đi, #T, #KĐ)
Diễn giải: Mỗi phân công xe liên quan đến một bảng số xe và một ngày bắt đầu đi
(Bảng_Số_Xe, Ngày_BĐ_Đi), liên quan đến một tour duy nhất (#T) và mã khách
đoàn duy nhất (#KĐ).
Ghi chú:
- Khóa của các quan hệ được gạch dưới.
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
51
BÀI 4: RÀNG BUỘC TOÀN VẸN
Các thuộc tính : #T, Ngay_Đi_Tour_KCN, #KĐ, trong quan hệ KHÁCH_CÁ_NHÂN có
thể có giá trị ‘trống’ (NULL). Trong trường hợp #KĐ có trị trống, Khách cá nhân
được xem là khách lẻ.
Thuộc tính #KĐ trong quan hệ PC_XE có thể có giá trị ‘trống’ (NULL).
Câu hỏi: Hãy phát biểu các ràng buộc toàn vẹn có trong CSDL trên một cách chặt
chẽ bằng ngôn ngữ đại số quan hệ hoặc SQL.
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
52
BÀI 5: THIẾT KẾ CƠ SỞ DỮ LIỆU
BÀI 5: THIẾT KẾ CƠ SỞ DỮ LIỆU
Thiết kế CSDL là quá trình thực hiện gồm nhiều bước, từ thu thập yêu cầu đến
thiết kế các mô hình dữ liệu, xác định các RBTV là xây dựng kế hoạch cài đặt, bảo
mật dữ liệu,… Trong bài này của môn Nhập môn CSDL chỉ hướng tới một phần nhỏ
trong quá trình xây dựng các mô hình dữ liệu gồm : hiểu biết về phụ thuộc hàm,
khóa, cách xác định khóa của một quan hệ dựa vào phụ thuộc hàm để từ đó có thể
đánh giá được một lược đồ CSDL đã được thiết kế là tốt hay xấu.
Học xong bài này cho sinh viên biết về khái niệm về Phụ thuộc hàm (Functional
Dependency), hệ tiên đề Amstrong áp dụng cho phụ thuộc hàm (PTH). Phụ thuộc hàm
cũng là công cụ để biểu diễn một số ràng buộc toàn vẹn. Thông qua cách biễu diễn
PTH, ta có thể dễ dàng xác định khóa của quan hệ, cũng như xác định nhóm các
thuộc tính dùng để nhận dạng, tìm kiếm duy nhất một đối tượng hoặc một sự kiện
của thế giới thực được mô hình hóa trong CSDL.
5.1 PHỤ THUỘC HÀM
Phụ thuộc hàm (Functional Dependency) là công cụ dùng để biểu diễn, một cách hình
thức, một số RBTV. Thông qua cách biễu diễn phụ thuộc hàm (PTH), ta có thể dễ
dàng xác định khóa của quan hệ, cũng như nhóm thuộc tính dùng để nhận dạng, tìm
kiếm duy nhất một đối tượng hoặc một sự kiện của thế giới thực được mô hình hóa
trong CSDL.
Phương pháp biểu diễn phụ thuộc hàm có vai trò quan trọng trong quá trình thiết kế
một lược đồ quan niệm của CSDL, nhằm tạo ra những quan hệ độc lập nhau, giảm
thiểu sự trùng lắp, dư thừa dữ liệu lưu trữ. Do đó giảm bớt các sai xót trong các thao
tác cập nhật, xóa và sửa dữ liệu của người sử dụng. Ngoài ra, còn dùng để đánh giá
chất lượng thiết kế một CSDL là tốt hay xấu.
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
53
BÀI 5: THIẾT KẾ CƠ SỞ DỮ LIỆU
5.1.1 Định nghĩa:
Cho một lược đồ quan hệ Q(X,Y,Z) với X,Y,Z là các tập thuộc tính con của Q+ và với
X,Y khác rỗng. Một Phụ thuộc hàm X → Y được xác định trên Q nếu và chỉ nếu
 q, q  T : q.X = q.X => q.Y = q.Y
i j Q i j i j
Khi đó ta nói: X xác định hàm Y hay Y phụ thuộc hàm vào X
Quy ước: Nếu Y không phụ thuộc hàm vào X ta ký hiệu: X -/-> Y
Ví dụ: trong quan hệ Trận_Đấu(MsTD, MsPh, GioTD, NgayTD)
Có quy ước : mỗi trận đấu diễn ra trong một phòng, vào 1 ngày và 1 giờ bắt đầu đã
qui định
Ta có phụ thuộc hàm: MsTD → MsPh, GioTD, NgayTD
Ví dụ: Đội_TD(MsTD, MsDoi, MsCLB)
Mỗi trận đấu là 1 cuộc gặp gỡ giữa 2 đội do vậy MsTD -/-> MsDoi, MsCLB
5.1.2 Các phụ thuộc hàm đặc biệt
5.1.2.1 PHỤ THUỘC HÀM HIỂN NHIÊN
Nếu Y  X thì X → Y là phụ thuộc hàm hiển nhiên
Ví dụ: X → X hay AB → B được coi là các phụ thuộc hàm hiển nhiên
5.1.2.2 PHỤ THUỘC HÀM NGUYÊN TỐ
X → Y là PTH nguyên tố (hay Y phụ thuộc hàm đầy đủ vào X ) khi và chỉ khi:
 X'  X và X' <> X mà X' → Y
Ví dụ: trong quan hệ Đội(MsCLB, MsDoi, MsLuaTuoi, Phai) ta có:
MsCLB, MsDoi → MsLuaTuoi là phụ thuộc hàm nguyên tố do:
MsCLB -/-> MsLuaTuoi và MsDoi -/-> MsLuaTuoi
5.1.2.3 TẬP PHỤ THUỘC HÀM
Tập hợp các phụ thuộc hàm của quan hệ Q được ký hiệu là F
Q
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
| 54  |                               |     |     |     |
| --- | ----------------------------- | --- | --- | --- |
|     | BÀI 5: THIẾT KẾ CƠ SỞ DỮ LIỆU |     |     |     |

|     F |  = {fi : X → Y xác định trên Q}  |     |     |     |
| ----- | -------------------------------- | --- | --- | --- |
Q
Qui ước: Chỉ mô tả các phụ thuộc hàm không hiển nhiên trong tập F.
5.1.2.4 BIỂU DIỄN TẬP PTH BẰNG ĐỒ THỊ CÓ HƯỚNG
Đồ thị tập phụ thuộc hàm gồm:
- Hai loại nút: Nút thuộc tính và nút PTH
- Hai loại cung: Cung từ nút thuộc tính đến nút PTH và cung từ nút PTH đến nút thuộc
tính.
Ví dụ: Cho 1 lược đồ quan hệ u=(Q,F) với Q=(ABCDEG) và tập PTH F:
|       | F = { f : A → B, f | : CD → E, f | : E → G, f | : A → CE}  |
| ----- | ------------------ | ----------- | ---------- | ---------- |
|       | 1                  | 2           | 3          | 4          |
Ta có đồ thị của tập PTH F như sau:
                           *B
A*
                         O
C*                                 * E
          o             * G
  D  *

5.1.3 Hệ tiên đề Amstrong và ứng dụng
5.1.3.1 HỆ TIÊN ĐỀ AMSTRONG
Cho lược đồ quan hệ Q và X, Y, W, Z  Q+.
| LD : Tính phản xạ:   |     | Nếu Y  X thì X → Y  |     |     |
| -------------------- | --- | -------------------- | --- | --- |
1
| LD 2 : Luật thêm vào:  |     | Nếu X → Y và Z  W thì X,W → Y,Z  |     |     |
| ---------------------- | --- | --------------------------------- | --- | --- |
| LD : Luật bắc cầu:     |     | Nếu X → Y và Y → Z thì X → Z      |     |     |
3
Một số luật dẫn suy từ hệ tiên đề Amstrong:

| LD : Luật phân rã:   |     | Nếu X → Y,Z thì X → Y và X |     | → Z  |
| -------------------- | --- | -------------------------- | --- | ---- |
4
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
  55

BÀI 5: THIẾT KẾ CƠ SỞ DỮ LIỆU

| LD : Luật hội:   |     | Nếu X → Y và X → Z thì X → Y,Z  |     |     |
| ---------------- | --- | ------------------------------- | --- | --- |
5
| LD : Luật bắc cầu giả:   |     | Nếu X → Y và YZ → W thì XZ → W  |     |     |
| ------------------------ | --- | ------------------------------- | --- | --- |
6
Chứng minh:
LD : Y  YZ => YZ → Y (luật phản xạ)
4
      Z  YZ => YZ → Z
     Áp dụng luật bắc cầu (LD3) ta có kết quả : X → Y và X → Z
LD 5 :  X → Y và X  X => X → X,Y (1) (luật thêm vào)
      X → Z và Y  Y => XY → Z (2)
         từ (1) và (2): X → YZ (luật bắc cầu)
LD :  X → Y và Z  Z => XZ → YZ và YZ → W => XZ → W
6
5.1.3.2 ỨNG DỤNG
Với tập PTH F xác định trên một quan hệ Q cho trước ta có thể suy diễn thêm nhiều
phụ thuộc hàm khác dựa trên các luật dẫn của hệ tiên đề Amstrong hay nói cách
khác, ta có thể kiểm tra một PTH f có thể suy ra từ F hay không?
Ví dụ: Cho Q=(ABCDEH) và
|           F = {f | : AB→C, f | :AE→D, f | :BC→D, f | :C→E, f :ED→H}  |
| ---------------- | --------- | -------- | -------- | --------------- |
|                  | 1         | 2        | 3        | 4 5             |
Kiểm tra xem từ F có thể suy ra AB→EH hay không?
Giải:
|   Từ f  và f                               |  áp dụng luật bắc cầu:        |     |     | => AB → E (1)  |
| ------------------------------------------ | ----------------------------- | --- | --- | -------------- |
| 1                                          | 4                             |     |     |                |
|   Từ f  và f                               |  áp dụng luật bắc cầu giả:    |     |     | => AE → H (2)  |
| 2                                          | 5                             |     |     |                |
|   Từ (1) và (2) áp dụng luật bắc cầu giả   |                               |     |     | => AB → H (3)  |
|   Từ (1) và (3) áp dụng luật hội :         |                               |     |     | => AB → EH     |
Vậy từ F dựa vào các luật trong hệ luật dẫn Amstrong chúng ta suy ra được AB → EH.
Kết luận là từ F có thể suy ra AB → EH.
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
56
BÀI 5: THIẾT KẾ CƠ SỞ DỮ LIỆU
5.1.4 Bao đóng của tập phụ thuộc hàm
5.1.4.1 ĐỊNH NGHĨA
Cho một quan hệ Q có tập các phụ thuộc hàm F = { X-->Y xác định trên Q}. Bao
đóng của F, ký hiệu F+, là tập hợp tất cả các PTH có thể suy diễn từ F dựa vào hệ luật
dẫn Amstrong.
Ký hiệu: F + = { X → Y / F |= X → Y}
Q
Ví dụ: Q(A,B,C) và F = {f1: A → B, f2: B → C}
F + = { A→B; A→C; A→A,C; A→ABC;...}
Q
Nhận xét: Trong thực tế, việc tìm F+ là rất khó khăn. Vì vậy, từ một tập PTH F cho
trước, người ta sẽ tìm cách giải quyết bài toán: Tìm một tập phụ thuộc hàm nhỏ nhất
mà từ đó có thể suy diễn ra các phụ thuộc hàm khác. Tập đó gọi là phủ tối tiểu của
tập phụ thuộc hàm F ban đầu (ký hiệu: F ). Ngoài ra bài toán thành viên (xác định
tt
một phụ thuộc hàm có thuộc F+ không?) cũng được giải quyết.
Ví dụ : Cho LĐQH u=(Q,F) với Q=(ABCDEG) và
F={AE → C, CG → A, DB → G, GA → E}
Kiểm tra phụ thuộc hàm BDC → Q có thuộc F+ không?
(dựa vào ví dụ của phần 5.1.3.2 sinh viên tự giải ví dụ này)
5.1.4.2 ỨNG DỤNG:
Dựa trên bao đóng F+ của F ta có thể xác định được tập tất cả các thuộc tính phụ
thuộc vào một tập thuộc tính X cho trước và có thể kiểm tra một PTH nào đó có thuộc
vào bao đóng F+ hay không.
Tuy nhiên, việc xây dựng bao đóng F+ là một bài toán khó. Để dễ dàng giải quyết các
bài toán trên người ta dựa vào 1 khái niệm mới: Bao đóng của tập thuộc tính.
5.1.5 Bao đóng của tập thuộc tính
5.1.5.1 ĐINH NGHĨA
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
  57

BÀI 5: THIẾT KẾ CƠ SỞ DỮ LIỆU

Cho 1 lược đồ quan hệ u=(Q,F) với Q là tập thuộc tính và F là tập các phụ thuộc hàm,
F={f , f ,..,f } và X  Q+. Bao đóng của tập thuộc tính X dựa trên F, ký hiệu X+ , là
| 1 2 | n   |     |     |     | F   |
| --- | --- | --- | --- | --- | --- |
tập các thuộc tính phụ thuộc hàm vào X dựa trên F.
|         | X+  = {Y  Q+ / X → Y  F+}  |     |     |     |     |
| ------- | ---------------------------- | --- | --- | --- | --- |
F
Nhận xét:
X  X+
| 1.         | F                     |     |     |     |     |
| ---------- | --------------------- | --- | --- | --- | --- |
| 2.  Y  X+ |  <=> f: X → Y  F+.  |     |     |     |     |
F
Dựa vào nhận xét 2 ta có thể giải quyết bài toán thành viên bằng cách xác định bao
đóng của tập thuộc tính.
Thuật toán xác định bao đóng của tập thuộc tính X (X+ )
F
Dữ liệu vào : X, F
| Dữ liệu ra : X+ |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- |
F
begin
X+ F  = X;
Repeat
| X' = X+ |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- |
F
For i:=1 to m do  { với m = card(F)}
if VT(fi)  X+  then X+  := X+   VP(fi)  {VT(fi): vế trái của fi, VP: vế phải}
|           | F         | F   | F   |     |     |
| --------- | --------- | --- | --- | --- | --- |
| Until (X+ | F  = X')  |     |     |     |     |
end;
Ví dụ: cho Q(ABCDEGH) và tập phụ thuộc hàm
|             F ={f | :B→A; f | :DA→CE; f | :D→H; f | :GH→C; f | :AC→D}  |
| ----------------- | ------- | --------- | ------- | -------- | ------- |
|                   | 1       | 2         | 3       | 4        | 5       |
a.  Tìm bao đóng của tập thuộc tính {BD}
X+  = BD
F
| Do f :   X+ |  = BDA   |     |     |     |     |
| ----------- | -------- | --- | --- | --- | --- |
| 1           | F        |     |     |     |     |
| Do f :   X+ |  = BDAH  |     |     |     |     |
| 3           | F        |     |     |     |     |
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
| 58  |     |     |     |
| --- | --- | --- | --- |
  BÀI 5: THIẾT KẾ CƠ SỞ DỮ LIỆU

| Do f :   X+  = BDAHCE  |     |     |     |
| ---------------------- | --- | --- | --- |
| 2 F                    |     |     |     |
X+
| Do f 3 :   F  = BDAHCE  |     |     |     |
| ----------------------- | --- | --- | --- |
Vậy X+  = BDAHCE.
F
b.  Tìm bao đóng của tập thuộc tính {BCG}
X+  = BCG
F
| Do f :   X+  = BCGA     |     |     |     |
| ----------------------- | --- | --- | --- |
| 1 F                     |     |     |     |
| Do f :   X+  = BCGAD    |     |     |     |
| 5 F                     |     |     |     |
| Do f :   X+  = BCGADE   |     |     |     |
| 2 F                     |     |     |     |
| Do f :   X+  = BCGADEH  |     |     |     |
| 3 F                     |     |     |     |
Vậy X+  = Q+.
F
Ví dụ: Cho Q(ABCDEH) và
| F = {f : AB→C, f | :AE→D, f | :BC→D, f | :C→E, f :ED→H}  |
| ---------------- | -------- | -------- | --------------- |
| 1                | 2        | 3        | 4 5             |
Kiểm tra AB→EH có thuộc vào F+ hay không?
Cách giải: Kiểm tra EH  {AB} +? Nếu EH nằm trong {AB} + thì kết luật AB → EH
F F
thuộc F+. Ngược lai kết luận là không thuộc F+.
5.2 KHÓA VÀ CÁCH XÁC ĐỊNH
5.2.1 Định nghĩa
Cho lược đồ quan hệ u=(Q,F) với Q là tập thuộc tính và F = { f ,f ,..f }
1 2 n
1.  S  Q+, S là siêu khóa của Q nếu S →Q+  F+
2.  K  Q+, K là khóa chính của Q nếu K là siêu khóa và PTH K→Q+ là PTH nguyên tố.
Nhận xét: Nếu đồ thị biểu diễn của tập PTH F không chứa chu trình thì Q chỉ có duy
nhất một khóa.
5.2.2 Cách xác định khóa của một quan hệ
5.2.2.1 THUẬT TOÁN XÁC ĐỊNH MỘT KHÓA
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
59
BÀI 5: THIẾT KẾ CƠ SỞ DỮ LIỆU
Ý tưởng: Xuất phát từ một siêu khóa K=Q. Duyệt lần lượt các thuộc tính A  K. Nếu
i
bất biến (K-A)+=Q được bảo toàn thì loại A khỏi K. Kết thúc quá trình lặp ta được K là
i i
một khóa chính của LĐQH.
Thuật toán xác định một khóa của LĐQH
Dữ liệu vào: Q, F
Dữ liệu ra: K là một khóa của (Q,F)
Begin
K=Q;
For each attribute A in Q+ do
i
if ((K-A)+ = Q) then
i
K=K-A ;
i
Write (K);
End.
Ví dụ: áp dụng thuật toán trên tìm một khóa của LĐQH u=(Q,F) với Q=ABCDE và
F= {B → C, C → BD, BE → A, A → C}
Giải
K=ABCDE
Vòng lặp thực hiện 5 lần (do Q có 5 thuộc tính)
Với i=1. Xét thuộc tính A
Tính BCDE+ = Q => K=BCDE
Với i=2. Xét thuộc tính B
Tính CDE+ = Q => K=CDE
Với i=3. Xét thuộc tính C
Tính DE+ ≠ Q => K=CDE
Với i=4. Xét thuộc tính D
Tính CE+ = Q => K=CE
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
60
BÀI 5: THIẾT KẾ CƠ SỞ DỮ LIỆU
Với i=5. Xét thuộc tính E
Tính C+ ≠ Q => K=CE
Xuất ra khóa K=CE.
5.2.2.2 THUẬT TOÁN XÁC ĐỊNH KHÓA DỰA VÀO ĐỒ THỊ
Ý tưởng: từ đồ thị của tập PTH (5.1.2.4) thực hiện các bước sau:
Gọi N là tập thuộc tính nguồn, chỉ chứa các nút thuộc tính không có cung đi tới
Gọi M là tập thuộc tính trung gian, chứa các nút thuộc tính vừa có cung đi tới, vừa có
cung đi ra.
Nếu từ N ta có thể lần theo hướng các cung để đến được tất cả các nút còn lại thì N
chính là khóa và là khóa duy nhất.
Ngược lại, ta lần lượt hội N với 1 tập con của M để kiểm tra có là khóa hay không.
Ví dụ: Cho lược đồ quan hệ Giảng dạy:
GiangDay =(MsGV, Hoten, MsMH, TenMH, Phòng, Giờ)
F={f :MsGV → Hoten; f : MsMH →TenMH; f : Phong,Gio → MSMH;
1 2 3
f : MsGV,Giờ → Phòng}
4
Tìm khóa của quan hệ GiangDay?
Vẽ đồ thị của tập PTH. Ta nhận thấy: N = {MsGV, Gio} và M = {MsMH, Phong}. Từ
tập N ta có thể lần theo hướng các cung đến được tất cả các nút. Vậy Khóa K=
{MsGV, Gio} là khóa duy nhất.
5.2.2.3 THUẬT TOÁN TÌM TẤT CẢ CÁC KHÓA
Thuật toán
Dữ liệu vào: <Q,F>
Dữ liệu ra: K {Tập các khóa của quan hệ Q}
Begin
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
61
BÀI 5: THIẾT KẾ CƠ SỞ DỮ LIỆU
b : Tìm tập N, với N là tập các thuộc tính không xuất hiện ở vế phải của các phụ
1
thuộc hàm. Tính N+. Nếu N+ = Q thì K=N là khóa duy nhất (Thoát). Ngược lại sang
bước 2
b : Tìm tập M với M là tập các thuộc tính xuất hiện ở cả 2 vế trong tập PTH F.
2
b : Xây dựng 2m-1 tập con của tập M với m = Card(M)
3
b : Xây dựng tập K chứa các khóa
4
Begin
K ={} ;
For i:=1 to (2m-1) do
begin
K := N  M ;
i i
Nếu K không chứa các khóa đã xác định trước đó và X+ = Q+ thì
i i F
K là 1 khóa của Q: K = K  K.
i i
end
End
End
Ví dụ: Cho lược đồ quan hệ u=(Q,F) với Q=(ABCDEG) và F = { f : AD → B;
1
f : EG → A; f : BC → G}. Xác định các khóa của lược đồ quan hệ u.
2 3
Giải:
N = {CDE}
M = {ABG}
Tập các khóa tìm được K={K =CDEA, K =CDEB, K =CDEG}.
1 2 3
Ví dụ: Cho lược đồ quan hệ u=(Q,F) với Q = (ABCDE) và F = {A → BE, B → E,
C → D, EC → AB }. Xác định các khóa của lược đồ quan hệ u.
Giải:
N = {C};
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
62
BÀI 5: THIẾT KẾ CƠ SỞ DỮ LIỆU
M = {ABE}
Các tập con của M gồm {A,B,E,AB,AE,BE,ABE}.
Lần lượt hội với tập nguồn {C} với các tập con của tập M ta có 3 khóa: K = AC, K =
1 2
BC, K = EC. Các tập khác mặc dù bao đóng bằng Q nhưng vẫn bị loại do chứa 3 khóa
3
đã tìm thấy và chúng được coi là siêu khóa.
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
63
BÀI 5: THIẾT KẾ CƠ SỞ DỮ LIỆU
BÀI TẬP
Bài 1: Cho lược đồ quan hệ r(Q,F) với Q=(A,B,C,D,E,G) ,
F={A→B, CD→A, BC→D, AE→BG}
a. Tìm một khóa của r?
b. Các tập ABCE và ABD có phải là khóa của r không? tại sao?
c. Tìm tập các thuộc tính không tham gia vào khóa nào của r?
Bài 2: Cho lược đồ quan hệ u(Q,F) với Q=( I,J,K,L,M,N,O),
F={L→J, LM→O, N→K, KO→N, M→I, LO→MI}
a. Lược đồ quan hệ u có duy nhất một khóa không? Tại sao?
b. Tìm tất cả Khóa của u?
c. Có thể thêm một phụ thuộc hàm vào F để u có khóa duy nhất khóa không? Tại
sao?
Bài 3: Cho lược đồ quan hệ r(Q,F) với Q=(A,B,C,D,E,G,H),
F={B→AC, HD→AE, AC→BE, E→H, A→D, G→E}
a. Tìm một khóa của r?
b. Các tập BCG và ACB có phải là khóa của r không? tại sao?
c. Tìm tập các thuộc tính không tham gia vào khóa nào của r?
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
64
BÀI 6: DẠNG CHUẨN
BÀI 6: DẠNG CHUẨN
Trong thực tế, một ứng dụng có thể được phân tích và thiết kế thành nhiều lược đồ
CSDL khác nhau. Để đành giá chất lượng giữa các lược đồ CSDL này người ta dựa trên
một số tiêu chuẩn trong đó có tiêu chuẩn về dạng chuẩn của lược đồ CSDL.
Dạng chuẩn được xây dựng nhằm mục đích giảm sự trùng lắp thông tin trong CSDL.
Từ đó tránh các sai sót trong các thao tác cặp nhật trên CSDL. Vì Sự trùng lắp thông
tin sẽ làm tăng không gian lưu trữ, cũng như chi phí kiểm tra RBTV một cách vô ích.
Ngoài ra, các thao tác thêm, xóa, sửa trong CSDL khi có sự trùng lắp thông tin cũng
gặp nhiều khó khăn và dễ dẫn đến sai sót.
Ví dụ: Xét một thể hiện của quan hệ quản lý học tập(QLHT) của sinh viên
QLHT(MsSV, Ten, NS, Phai, ĐC, MsLop, TenLop, MsMH, TenMH, Diem)
F = { f :MsSV → Ten, NS, Phai, ĐC, MsLop; f : MsLop → TenLop; f : MsMH → TenMH;
1 2 3
f : MsSV, MsMH → Diem }
4
Quan hệ QLHT có sự trùng lắp thông tin. Sự trùng lắp thông tin này có thể gây nên
một số vấn đề khi thực hiện các thao tác trên quan hệ:
- Sửa: Giả sử có 1 sinh viên (SV) thay đổi địa chỉ, thì hệ thống cần phải duyệt trên
toàn bộ quan hệ để tìm và sửa địa chỉ ở các bộ liên quan đến SV này. Nếu để sót thì
sẽ dẫn đến tình trạng thông tin không nhất quán.
- Xóa: Giả sử SV có mã số 1108 hiện nay chỉ đăng ký một học môn CSDL. Nếu muốn
xóa kết quả điểm môn này thì dẫn đến mất luôn thông tin của SV.
- Thêm: Vì khóa của quan hệ là {MsSV, MsMH} do đó không thể thêm 1 SV vào quan
hệ nếu SV đó chưa đăng ký học môn nào.
Qua ví dụ trên chúng ta nhận thấy sự trùng lắp thông tin là nguyên nhân làm cho
CSDL có chất lượng kém. Để hạn chế tình trạng trùng lắp dữ liệu, người ta đưa ra các
yêu cầu thiết kế cần thiết cho một quan hệ dựa trên khái niệm phụ thuộc hàm, được
gọi là các dạng chuẩn của một quan hệ.
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
65
BÀI 6: DẠNG CHUẨN
6.1 CÁC DẠNG CHUẨN
6.1.1 Dạng chuẩn 1
Khái niệm thuộc tính đơn: Một thuộc tính được gọi là thuộc tính đơn nếu giá trị của
nó không phải là sự kết hợp bởi nhiều thông tin có ý nghĩa khác nhau và hệ thống
luôn truy xuất trên toàn bộ giá trị của nó. Ngược lại, là thuộc tính kép.
Ví dụ: Xét quan hệ VatTu(MaVT, TenVT, DVT)
Nếu TenVT bao gồm tên của vật tư và cả qui cách của nó. Như vậy TenVT là thuộc
tính kép.
Ví dụ: ChuyenMon(MaGV, MonGD)
Nếu MonGD là một chuỗi các môn học mà giáo viên có thể phụ trách như: ‘CSDL,
CTDL, KTLT, PTTKHĐT’, thì MonGD không phải là thuộc tính đơn.
Định nghĩa (dạng chuẩn 1):
Một lược đồ quan hệ Q đạt dạng chuẩn 1 (1 Normal Form - 1NF) nếu mọi thuộc tính
của Q đều là thuộc tính đơn.
Quy ươc: Đối với thuộc tính lưu trữ ngày dương lịch (bao gồm ngày, tháng, năm) có
thể xem là thuộc tính đơn.
Nhận xét:
- Một quan hệ có 1NF được xem là quan hệ có cấu trúc phẳng.
- Quan hệ đạt dạng chuẩn 1 còn trùng lắp thông tin
Ví dụ: TKBCoiThi(GT, Ngay, Giờ, Phong, Mon, GV)
F = { f : GT → Ngay,Gio,Phong,Mon,GV;
1
f :Mon → GV; f :Ngay,gio,phong → Mon}
2 3
Với qui định Mon → GV (Mỗi môn học chỉ có một giảng viên phụ trách) sẽ dẫn đến sự
trùng lắp thông tin.
Nếu thay đổi giờ thi của 2 môn thi sẽ sai giảng viên
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
66
BÀI 6: DẠNG CHUẨN
6.1.2 Dạng chuẩn 2
6.1.2.1 PHỤ THUỘC HÀM ĐẦY ĐỦ
Cho phụ thuộc hàm X → A. Thuộc tính A được gọi là phụ thuộc đầy đủ vào tập thuộc
tính X nếu:
Không tồn tại X’  X và X’ → A
Ví dụ: phụ thuộc hàm: MsSV, MsMH → TenSV là phụ thuộc hàm không đầy đủ vì chỉ
cần một thuộc tính MsSV là đã xác định được tên sinh viên: MsSV → TenSV
6.1.2.2 ĐỊNH NGHĨA (DẠNG CHUẨN 2)
Quan hệ Q đạt dạng chuẩn 2 nếu:
a. Q ở dạng chuẩn 1,
b. Mọi thuộc tính không khóa đều phụ thuộc đầy đủ vào các khóa của Q.
Ví dụ: Xét quan hệ quản lý học tập(QLHT) sau:
QLHT(MsSV, Ten, NS, Phai, ĐC, MsLop, tenLop, MsMh, TenMh, Diem)
F= { MsSV → Ten, NS, Phai, ĐC, MsLop ;
MsLop → tenLop;
MsMh →TenMh;
MsMh, MsSV → Diem }
Quan hệ QLHT không đạt dạng chuẩn 2 do MsSV → Ten với Ten là thuộc tính không
khóa, không phụ thuộc đầy đủ vào khóa {MsMh, MsSV}.
Có thể thay quan hệ QLHT bằng 3 quan hệ sau để đạt dạng chuẩn 2:
QLHT(MsSV, MsMH, Diem)
F ={ f : MsSV, MsMH → Diem}
QLHT 4
SV(MsSV, Ten, NS, Phai, ĐC, MsLop, TenLop)
F = {f :MsSV → Ten, NS, Phai, ĐC, MsLop; f : MsLop → TenLop}
SV 1 2
MH(MsMH, TenMH)
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
67
BÀI 6: DẠNG CHUẨN
F = { f : MsMH → TenMH}
MH 3
Ví dụ: LopHoc(Lop, Mon, NgayKG, HocPhi)
F = { f : Lop,Mon → NgayKG; f : Mon → HocPhi}
1 2
Xác định khóa và kiểm tra có đạt dạng chuẩn 2 hay không?
Giải: Dựa vào F ta có Khóa là K={Lop, Mon}
Quan hệ LopHoc không ở dạng chuẩn 2 vì thuộc tính không khóa HocPhi không phụ
thuộc đầy đủ vào khóa. Mon → HocPhi
Để khắc phục ta có thể tách quan hệ trên thành 2 quan hệ:
LopHoc(Lop, Mon, NgayKG)
F = { f : Lop,Mon → NgayKG}
LopHoc 1
và MonHoc(Mon,HocPhi)
F = { f : Mon → HocPhi}
MonHoc 2
thì hai quan hệ này đều đạt dạng chuẩn 2 trở lên.
Ví dụ: xét quan hệ đăng ký điện thoại khách hàng:
ĐTKH(MsĐT, TenKH, MSCáp, KinhPhí),
F = { MsĐT → TenKH; MsĐT, MsCáp → Kinhphí}
Quan hệ ĐTKH có đạt dạng chuẩn 2 hay không?
Nhận xét:
- Nếu mỗi khóa của quan hệ Q chỉ có 1 thuộc tính thì Q tối thiểu đạt dạng chuẩn 2.
- Các quan hệ ở dạng chuẩn 2 nhưng vẫn còn trùng lắp thông tin.
6.1.3 Dạng chuẩn 3
6.1.3.1 PHỤ THUỘC BẮC CẦU
Thuộc tính A  Q+ được gọi là phụ thuộc bắc cầu vào một tập thuộc tính X nếu tồn tại
nhóm thuộc tính Y  Q+ thỏa mãn đồng thời 4 điều kiện sau:
i. X → Y  F+
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
68
BÀI 6: DẠNG CHUẨN
ii. Y → A  F+
iii.Y -/-> X
iv.A  {X  Y}
Ví dụ: Xét quan hệ SV(MsSV, Ten, Ngsinh, Phai, MsLop, TenLop)
TenLop phụ thuộc bắc cầu vào MsSV vì: MsSV → MsLop và MsLop → TenLop.
6.1.3.2 ĐỊNH NGHĨA (DẠNG CHUẨN 3)
Quan hệ Q đạt dạng chuẩn 3 nếu :
a. Q ở dạng chuẩn 1,
b. Mọi thuộc tính không khóa của Q đều không phụ thuộc bắc cầu vào một khóa
nào của Q.
Ví dụ: Quan hệ SV trong ví dụ trên không đạt dạng chuẩn 3. Ta có thể quan hệ SV
tách thành 2 quan hệ:
SV(MsSV, Ten, Ngsinh, Phai, MsLop)
Lop(MsLop, TenLop)
Để loại bỏ PTH bắc cầu và đạt dạng chuẩn 3 trở lên.
Ví dụ: Xét LĐCSDL gồm 3 QH sau:
PXN (SP, Ngay, MsKH, TenKH, TrịGiá)
F ={SP → Ngay, MsKH, TrịGia; MsKH → TenKH}
CTP (SP, MsHH, TenHH, SL,ĐG)
F = {SP, MsHH → SL,ĐG; MsHH → TenHH}
Tồn_Kho (MSHH, MSKho, TenKho, SLT)
F={ MSHH, MSKho → SLT; MSKho → TenKho; TenKho → MsKho}
-Xét quan hệ phiếu xuất nhập PXN có 1 khóa {SP}
Đạt dạng chuẩn 2 nhưng không đạt dạng chuẩn 3 vì có phụ thuộc bắc cầu
SP → MsKH; MSKH -/-> SP; MSKH → TenKH
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
69
BÀI 6: DẠNG CHUẨN
- Quan hệ chi tiết phiếu CTP: có 1 khóa là {SP,MsHH}
Không đạt dạng chuẩn 2 vì TenHH không phụ thuộc đầy đủ vào khóa
- Quan hệ Tồn_Kho: có 2 khóa là {MSHH,MSKho} và {MsHH, TenKho}
Đạt dạng chuẩn 3 vì chỉ có 1 thuộc tính không khóa là SLT và thuộc tính này không
phụ thuộc bắc cầu vào bất kỳ khóa nào.
Nhận xét:
Quan hệ Tồn_kho đạt dạng chuẩn 3 nhưng vẫn còn sự trùng lắp thông tin trên các cột
MsKho và TenKho.
6.1.4 Dạng chuẩn BC (Boyce - Codd)
Định nghĩa: Quan hệ Q ở dạng chuẩn BC nếu Q ở dạng chuẩn 1 và mọi phụ thuộc
hàm không hiển nhiên đều có vế trái là một siêu khóa.
X → A  F+ : A  X và X phải chứa khóa của Q (X là một siêu khóa)
Nhận xét: Nếu Q đạt dạng chuẩn BC thì mọi vế trái của tập PTH đều là siêu khóa.
Ví dụ: Quan hệ Tồn_Kho không đạt dạng chuẩn BC vì: MsKho → TenKho
Ta tách thành 2 quan hệ: Tồn_Kho (MSHH, MSKho, SLT) và Kho(MSKho, TenKho) thì
lúc này cả 2 quan hệ này đều đạt BCNF.
6.1.5 Dạng chuẩn của một LĐCSDL
Là dạng chuẩn thấp nhất trong các quan hệ của LĐCSDL.
Ví dụ: Cho lược đồ CSDL gồm hai lược đồ quan hệ sau :
Q (ABC), F ={A → BC, C → B}
1 1
Q (BC), F ={C → B}
2 2
Cho biết LĐCSDL trên ở dạng chuẩn cao nhất nào ?
<Q ,F > ở 2NF do có phụ thuộc bắc cầu vào khóa.
1 1
<Q ,F > ở BCNF.
2 2
Vậy LĐCSDL ở 2NF.
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
| 70  |     |     |     |
| --- | --- | --- | --- |
  BÀI 6: DẠNG CHUẨN

6.2 CHUẨN HÓA MỘT LĐQH BẰNG PHÂN RÃ:
6.2.1 Khái Niệm Chuẩn Hóa
Xuất phát từ tập thuộc tính của lược đồ quan hệ Q, cùng với tập phụ thuộc hàm(PTH)
F Q  xác định trên Q thể hiện các qui tắc quản lý, Q chưa ở dạng chuẩn 3. Ta phân rã Q
thành các quan hệ con {Q} dựa trên tập PTH F  sao cho các quan hệ con đạt dạng
|     |     | i   | Q   |
| --- | --- | --- | --- |
chuẩn cao nhất, tối thiểu là DC3, được gọi là quá trình chuẩn hoá.
Trong quá trình chuẩn hóa cần chú trọng đến 2 tính chất sau:
- Bảo toàn thông tin: Phân rã nhận được phải bảo đảm tính kết không mất thông tin,
nghĩa là:
| Q +  Q | + = Q+,     |           |     |
| ------- | ----------- | --------- | --- |
| 1       | 2           |           |     |
| T : T  |  = T [Q +]  |  T [Q +]  |     |
| Q       | Q Q 1       | Q 2       |     |
- Bảo toàn PTH:
Q+ = Q+
i
| F Qi   = F | Q   |     |     |
| ----------- | --- | --- | --- |
6.2.2 Định lý Delobel
Cho lược đồ quan hệ u=(Q, F) với Q là tập thuộc tính và F là tập phụ thuộc hàm. Nếu
f: X → A  F+ sao cho X  A  Q+ (là con thực sự của Q+) thì phép phân rã Q thành 2
lược đồ quan hệ con:
| <Q (X, A), F  | ={f F : VT(f)  VP(f)  Q |     | +} >  |
| ------------- | -------------------------- | --- | ----- |
| 1             | 1                          |     | 1     |
| <Q (Q+\ A), F | ={f F : VT(f)  VP(f)  Q |     | +} >  |
| 2             | 2                          |     | 2     |
là bảo toàn thông tin
6.2.3 Thuật toán phân rã
Ý tưởng: Dựa vào định lý Delobel, ta phân rã quan hệ Q thành 2 quan hệ Q  và Q
1 2
bằng 1 PTH f thỏa điều kiện của định lý. Lặp lại phân rã trên Q  và Q  cho đến khi các
1 2
Q thu được đều đạt BCNF.
i
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
71
BÀI 6: DẠNG CHUẨN
Procedure PhanRa(Q, F)
Dữ liệu vào: <Q, F>
Dữ liệu ra: C = { Qi }n {tập các lược đồ quan hệ thu được sau phân rã}
i=1
Begin
b . Loại bỏ các PTH có VT  VP = Q+ khỏi F
1
F* = F \ { f  F : VT(f)  VP(f) = Q+ }
b . Nếu F* =  thì C = C  {Q} và kết thúc {Điểm dừng}
2
ngược lại, thực hiện phân rã
b . Chọn f:X → Y  F
2.1
b . Phân rã thành 2 lược đồ con:
2.2
<Q + = {X, A}, F1={f  F : VT(f)  VP(f) Q +} >
1 1
<Q + = Q+ \ A, F2={f  F : VT(f)  VP(f) Q +} >
2 2
b . Phân rã đệ qui Q và Q :
2.3 1 2
PhanRa(Q , F );
1 1
PhanRa(Q , F );
2 2
end;
Ví dụ: Xét Lược đồ quan hệ u=<Q,F> với Q=(MsKH, TP, CTyVC, MsHH, SL)
(MsKH: Mã số Khách hàng. TP: Thành phố của nhà cung cấp. CtyVC: công ty vận
chuyển hàng. MsHH: mã hàng hóa. SL: số lượng) và tập PTH F.
F = {f : MsKH → TP; f : MsKH → CTyVC; f : MsKH, MsHH → SL; f :TP → CtyVC}
1 2 3 4
Khóa là: {MsKH, MsHH}
Đạt dạng chuẩn 1 không đạt dạng chuẩn 2 vì: thuộc tính không khóa CtyVC không
phụ thuộc đầy đủ vào khóa {MsKH, MsHH} (MsKH → CTyVC).
Sử dụng PP phân rã để nâng cấp lược đồ quan hệ Q:
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
| 72  |                   |     |     |     |     |     |
| --- | ----------------- | --- | --- | --- | --- | --- |
|     | BÀI 6: DẠNG CHUẨN |     |     |     |     |     |

Q(MsKH, TP, CTyVC, MsHH, SL)
f
4
|     |     | Q (TP, CtyVC)                      Q |     |     | (MsKH, TP, MsHH, SL)  |     |
| --- | --- | ------------------------------------ | --- | --- | --------------------- | --- |
|     |     | 1                                    |     |     | 2                     |     |
     F 1  = {f 4 }                    F 2  = {f 1 :MsKH→TP; f 2 : MsKH,MsHH→SL}
|       |     |     |     |     |               f |     |
| ----- | --- | --- | --- | --- | --------------- | --- |
1
                Q 21 (MsKH, TP)           Q 22 (MsKH, MsHH, SL)
|                          |     |                     |       | F  = {f | }          F | ={f }  |
| ------------------------ | --- | ------------------- | ----- | ------- | ------------ | ------ |
|                          |     |                     |       | 21      | 1            | 22 3   |
| Kết quả: C = { <Q        |     | (TP, CtyVC), F      |  = {f | }>;     |              |        |
|                          |     | 1                   | 1     | 4       |              |        |
|                  <Q      |     | (MsKH, TP), F       |  = {f | }>;     |              |        |
|                          |     | 21                  | 21    | 1       |              |        |
|                       <Q |     | (MsKH, MsHH, SL), F |       |  = {f   | }> }         |        |
|                          |     | 22                  |       | 22      | 3            |        |
LĐCSDL C trên đạt BCNF, bảo toàn thông tin, bảo toàn phụ thuộc hàm;
Nhận xét:
Thuật toán phân rã luôn luôn bảo toàn thông tin theo đinh lý delobel.
Tất cả các quan hệ kết quả đều đạt dạng chuẩn BC.
Tùy theo thứ tự các PTH được xét trong quá trình phân rã, mà kết quả và số lượng
quan hệ con có thể khác nhau.
Hậu quả:
Thuật toán có thể dẫn đến 1 lược đồ CSDL không bảo toàn phụ thuộc hàm(PTH).
Kết quả thu được có thể chứa một quan hệ con mà ngữ nghĩa của nó không có ích cho
ứng dụng thực tế.
Thông thường PTH được chọn ưu tiên là PTH không chứa khóa, và là PTH gây chất
lượng xấu của lược đồ quan hệ (như PTH không đầy đủ hoặc các PTH bắc cầu vào
khóa).
Ví dụ:  Nếu thứ tự chọn PTH là: f  , f  , f  thì sẽ cho LĐCSDL như sau:
|     |     |     | 3   | 4 1 |     |     |
| --- | --- | --- | --- | --- | --- | --- |
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
  73

BÀI 6: DẠNG CHUẨN

Kết quả: C = {<Q
|                    |     | (MsKH, MsHH, SL), F |  = {f  }>; <Q   | (TP, CtyVC), F |  = {f }>;  |
| ------------------ | --- | ------------------- | --------------- | -------------- | ---------- |
|                    |     | 1                   | 1 3             | 2              | 2 4        |
|   <Q (MsKH, TP), F |     |  = {f }>;  <Q       | (MsKH, MsHH), F |  ={} }         |            |
| 3                  |     | 3 1                 | 4               | 4              |            |
Bài tập :
Bài 1: Cho LĐCSDL có các phụ thuộc hàm F = { f : A→BC; f : C→B} và 2 quan hệ
|       |          |        |     | 1 2 |     |
| ----- | -------- | ------ | --- | --- | --- |
| sau:Q | (ABC), Q | (BC).  |     |     |     |
|       | 1        | 2      |     |     |     |
a.  Xác định tập phụ thuộc hàm trên từng quan hệ.
b.  Xác định dạng chuẩn cao nhất của LĐCSDL.
Giải:
| a.  | F = {f : A → BC; f | : C → B}  |     |     |     |
| --- | ------------------ | --------- | --- | --- | --- |
Q1 1 2
|        F | = {f : C →B}  |     |     |     |     |
| -------- | ------------- | --- | --- | --- | --- |
Q2 2
| b.  | Q 1 (ABC) đạt dạng chuẩn 2 không đạt dạng chuẩn 3 vì:   |     |     |     |     |
| --- | ------------------------------------------------------- | --- | --- | --- | --- |
B phụ thuộc bắc cầu vào khóa A: A → C; C → B; C-/->A
Q (BC) đạt dạng chuẩn BC.
2
Bài 2: Xét lược đồ quan hệ Q(MsKH, TP, CTyVC, MsHH, SL)
MsKH: Mã số Khách hàng. TP: Thành phố của nhà cung cấp. CtyVC: công ty vận
chuyển hàng. MsHH: mã hàng hóa. SL: số lượng.
F = { f : MsKH → TP, CTyVC; f2: MsKH, MsHH → SL; f3: TP → CtyVC}
1
a.  Xác định khóa của quan hệ?
b.  Xác định dạng chuẩn của quan hệ?
c.  Có thể tách quan hệ trên thành các quan hệ nào để lđcsdl đạt dạng chuẩn cao
nhất.
Giải:
a.  Khóa: {MsKH, MsHH}
b.  Đạt dạng chuẩn 1, không đạt dạng chuẩn 2 vì: TP không phụ thuộc đầy đủ vào
khóa (MsKH → TP).
c.  Thay Q thành 2 quan hệ: KH(MsKH, TP, CtyVC);  CTVC(MsKH, MsHH, SL)
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
74
BÀI 6: DẠNG CHUẨN
Lược đồ trên đạt dạng chuẩn 2 nhưng không đạt dạng chuẩn 3 vì quan hệ KH không
đạt dạng chuẩn 3: do thuộc tính không khóa CtyVC phụ thuộc bắc cầu vào khóa
(MsKH → TP, TP → CtyVC).
Nên Tách thành các quan hệ:
KH(MsKH, TP); PC(TP, CtyVC); CTVC(MsKH, MsHH, SL)
Các quan hệ trên đã đạt dạng chuẩn BC.
Bài 3: Xét lược đồ quan hệ TKBCoiThi(GT, Ngay, Giờ, Phong, Mon, GV)
F = { f : GT → Ngay,Gio,Phong,Mon; f :Mon → GV; f :Ngay,gio,phong →Mon}
1 2 3
a. Xác định khóa của quan hệ?
b. Xác định dạng chuẩn của quan hệ?
c. Nếu quan hệ chưa đạt BCNF hãy phân rã để có LĐCSDL đạt BCNF?
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
75
TÀI LIỆU THAM KHẢO
TÀI LIỆU THAM KHẢO
1. Abraham Silberschatz, Henry F. Korth, S. Sudarshan (2011) Database system
concepts (sixth edition).
2. Jeffrey Ullman - dịch giả Trần Đức Quang (2002) Lý thuyết thiết kế cơ sở dữ liệu
NXB Thống Kê, Hà Nội.
3. David Maier (1983). The Theory of Relational Database, Communications of the
ACM, Volume 26, Number 2.
4. Đồng Thị Bích Thủy (2000), Nhập môn cơ sở dữ liệu, ĐH khoa học tự nhiên, ĐH
Quốc Gia TP. Hồ Chí Minh.
5. Nguyễn Bá Tường (1996), Cơ sở dữ liệu – Lý thuyết và thực hành, nhà xuất bản
Thống Kê, Hà Nội.
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)