BỘ GIÁO DỤC VÀ ĐÀO TẠO

ĐẠI HỌC CÔNG NGHỆ TP.HCM

THỰC HÀNH

PHÂN TÍCH THIẾT KẾ HỆ THỐNG

Biên soạn:  ThS. Võ Hoàng Khang

Website: http://www.hutech.edu.vn

THỰC HÀNH PHÂN TÍCH THIẾT KẾ HỆ THỐNG

Ấn bản 2022

MỤC LỤC

MỤC LỤC

I

MỤC LỤC ................................................................................................................... 1

HƯỚNG DẪN ............................................................................................................. 2

BÀI 1: HỆ THỐNG QUẢN LÝ THƯ VIỆN ................................................................... 18

1.1 MÔ TẢ ............................................................................................................... 18

1.2 CÂU HỎI ............................................................................................................ 19

BÀI 2: HỆ THỐNG QUẢN LÝ CỬA HÀNG NƯỚC GIẢI KHÁT ...................................... 20

2.1 MÔ TẢ ............................................................................................................... 20

2.2 CÂU HỎI ............................................................................................................ 21

BÀI 3: HỆ THỐNG QUẢN LÝ KHÁCH SẠN ................................................................ 22

3.1 MÔ TẢ ............................................................................................................... 22

3.2 CÂU HỎI ............................................................................................................ 23

BÀI 4: QUẢN LÝ CHO THUÊ VĂN PHÒNG Ở CAO ỐC ................................................ 24

4.1 MÔ TẢ ............................................................................................................... 24

4.2 CÂU HỎI ............................................................................................................ 25

BÀI 5: QUẢN LÝ HỒ SƠ BỆNH ÁN CỦA BỆNH NHÂN ............................................... 26

5.1 MÔ TẢ ............................................................................................................... 26

5.2 CÂU HỎI ............................................................................................................ 27

BÀI 6: QUẢN LÝ CÔNG TY DU LỊCH ........................................................................ 28

6.1 MÔ TẢ ............................................................................................................... 28

6.2 CÂU HỎI ............................................................................................................ 29

BÀI 7: QUẢN LÝ NHÂN SỰ ..................................................................................... 30

7.1 MÔ TẢ ............................................................................................................... 30

7.2 CÂU HỎI ............................................................................................................ 31

BÀI 8: QUẢN LÝ CUỘC ĐUA XE ĐẠP CÚP TRUYỀN HÌNH TP.HCM ............................ 32

8.1 MÔ TẢ ............................................................................................................... 32

8.2 CÂU HỎI ............................................................................................................ 33

TÀI LIỆU THAM KHẢO ............................................................................................ 34

II

HƯỚNG DẪN

HƯỚNG DẪN

MÔ TẢ MÔN HỌC

Phân tích thiết kế hệ thống là một giai đoạn quan trọng để xây dựng thành công

một hệ thống. Xây dựng một hệ thống được gọi là thành công nếu hệ thống này đáp

ứng được các yêu cầu của tổ chức đặt ra, có chu kỳ sống chấp nhận được, và hơn thế

nữa có thể phát triển khi hệ thống yêu cầu. Trong thực tế nhiều hệ thống chỉ tồn tại

trong  một  thời  gian  ngắn  và  sau  đó  không  còn  đáp  ứng  được  nhu  cầu  của  người  sử

dụng. Một trong những lý do là chưa quan tâm đến giai đoạn phân tích và thiết kế một

cách đầy đủ và sâu sắc, để rồi khi tổ chức phát triển thì hệ thống không còn khả năng

đáp ứng. Một lý do khác không kém phần quan trọng, là các nhà xây dựng hệ thống

không được trang bị một cách đầy đủ các kiến thức và phương pháp cơ bản để có thể

tiến hành việc xây dựng một hệ thống. Nếu phần phân tích thiết kế không hoàn chỉnh

và đúng đắn thì sẽ dẫn đến việc cài đặt thất bại.

Phân tích thiết kế hệ thống là một môn học chính cho các sinh viên chuyên ngành

công nghệ thông tin trong các trường đại học và cao đẳng. Đây cũng là một tài liệu

tham khảo cần thiết cho những ai quan tâm đến việc phân tích thiết kế hệ thống.

Giáo trình được chia làm 8 bài, ở mỗi nội dung chúng tôi có đưa các ví dụ thực tiễn

ở các lĩnh vực trong cuộc sống, những sai lầm có thể xảy ra trong quá trình phân tích

thiết kế để phân tích viên khỏi mắc sai sót khi làm việc, giúp cho người đọc thấy được

bức tranh toàn cục của hệ thống qua các bước thiết kế.

NỘI DUNG MÔN HỌC

  Bài 1. HỆ THỐNG QUẢN LÝ THƯ VIỆN

  Bài 2. HỆ THỐNG QUẢN LÝ CỬA HÀNG NƯỚC GIẢI KHÁT

  Bài 3. HỆ THỐNG QUẢN LÝ KHÁCH SẠN

  Bài 4. QUẢN LÝ CHO THUÊ VĂN PHÒNG Ở CAO ỐC

  Bài 5. QUẢN LÝ HỒ SƠ BỆNH ÁN CỦA BỆNH NHÂN

  Bài 6. QUẢN LÝ CÔNG TY DU LỊCH

  Bài 7. QUẢN LÝ NHÂN SỰ

  Bài 8. QUẢN LÝ CUỘC ĐUA XE ĐẠP CÚP TRUYỀN HÌNH

HƯỚNG DẪN  III

IV

HƯỚNG DẪN

KIẾN THỨC TIỀN ĐỀ

Môn Thực hành phân tích thiết kế hệ thống yêu cầu sinh viên có kiến thức về cơ sở

dữ liệu quan hệ và quản trị cơ sở dữ liệu.

YÊU CẦU MÔN HỌC

Người học vận dụng được lý thuyết phân tích thiết kế để xây dựng được mô hình

dữ diệu quan niệm hay còn gọi là mô hình thực thể kết hợp. Sử dụng công cụ thiết kế

cơ sở dữ liệu để vẽ mô hình quan hệ (Case Studio, Toad Data Modeler…), sinh ra câu

lệnh SQL, từ đó tạo được database hoàn chỉnh. Trên cơ sở đó, đội ngũ lập trình viên sẽ

xây dựng các chương trình quản lý ứng dụng trong cuộc sống.

CÁCH TIẾP NHẬN NỘI DUNG MÔN HỌC

Để học tốt môn này, người học cần đọc trước các nội dung được học trên lớp, tham

gia đều đặn và tích cực các buổi thực hành, hiểu các khái niệm, tính chất và ví dụ tại

lớp học. Sau khi học xong, cần ôn lại bài đã học và làm các bài tập tình huống. Tìm đọc

thêm các tài liệu khác liên quan đến bài học và các kiến thức cần thiết trong việc quản

lý một hệ thống thông tin.

PHƯƠNG PHÁP ĐÁNH GIÁ MÔN HỌC

Môn học được đánh giá gồm ba thành phần:

  Phần chuyên cần: chiếm 15%. SV đi học đầy đủ các buổi thực hành, làm các bài

thực hành theo sự hướng dẫn của GV. Đóng góp ý kiến xây dựng bài thực hành.

  Kiểm tra giữa kỳ: chiếm 35%. Hình thức và nội dung đánh giá: SV thực hiện các bài

tập trong các buổi thực hành và làm bài kiểm tra giữa kỳ tại phòng thực hành do GV

dạy thực hành quy định. GV chấm điểm, giải thích các thắc mắc và công bố  công

khai sau khi chấm điểm.

  Kiểm tra cuối kỳ: chiếm 50%. Hình thức và nội dung đánh giá: SV thực hiện bài tập

kiểm tra cuối kỳ tại phòng thực hành do GV dạy thực hành quy định. GV chấm điểm,

giải thích các thắc mắc, sau đó sẽ tổng hợp thành một cột điểm kết thúc môn học

và công bố công khai sau khi hoàn thành.

HƯỚNG DẪN  V

VI

HƯỚNG DẪN

HƯỚNG DẪN SỬ DỤNG CASE STUDIO 2.25

SV có thể download phiên bản sau của Case Studio là Toad Data Modeler đễ

hỗ  trợ  tốt  cho  các  phiên  bản  mới  nhất  của  các  database  như: SQL Server,

Oracle, DB2, PostgreeSQL...

Với các phần mềm tương tự khác, GV giảng dạy sẽ giới thiệu trong giờ học lý

thuyết.

I)  Giới thiệu:

  Case Studio là phần mềm hỗ trợ việc phân tích và thiết kế hệ thống

thông tin.

  Nhà sản xuất: Quest Software.

  Cài đặt: Xem trong file hướng dẫn.

HƯỚNG DẪN  7

II)  Sử dụng:

1) Tạo mới mô hình ERD:

  Vào menu File, chọn New Model (Ctrl + N), hoặc click vào biểu tượng

 trên thanh công cụ File.

  Chọn Database tương ứng của mô hình:

  Click vào nút OK. Giao diện chính của mô hình:

VIII

HƯỚNG DẪN

  Một số thành phần:

Loại mối kết hợp n-n (mối kết

Loại mối kết hợp phản thân (mối

hợp nhiều-nhiều – many to

kết hợp đệ quy – seft relationship)

many relationship)

Loại mối kết hợp 1-n (mối kết

hợp cha con – non-identifying

relationship)

Entity: Loại thực thể

Loại mối kết hợp 1-1 (mối kết hợp

định danh – identifying relationship)

  Tạo mới loại thực thể và các thuộc tính tương ứng:

- Click vào loại thực thể và thả vào vùng thiết kế như hình bên dưới:

HƯỚNG DẪN  9

- Double click vào loại thực thể vừa tạo:

Tên loại thực thể

Tên thuộc tính

Thêm mới thuộc tính

X

HƯỚNG DẪN

Double click vào để khai báo các tính chất của

thuộc tính

Độ rộng

Kiểu dữ liệu

Khai báo các constraint

(ràng buộc) nếu có

HƯỚNG DẪN  11

Double click vào để thiết lập khóa chính, nhấn Ctrl để chọn

nhiều thuộc tính (khi khóa chính gồm nhiều thuộc tính)

XII

HƯỚNG DẪN

  Giả sử ta có mô hình ERD như sau:

(0,n)

(1,1)

KHÁCH HÀNG

Mua

HÓA ĐƠN

(0,1)

Có

(1,1)

SL

Đơn giá

(1,n)

CTHD

(0,n)

THẺ VIP

MẶT HÀNG

- Biểu diễn trong Case Studio:

Chọn loại

MKH 1-n kéo

từ

KHACHHANG

và thả qua

THE_VIP.

Sửa

Cardinality

thành 1.

Double click

vào loại

MKH, đổi tên

(Name)

thành Có.

Chọn loại MKH

n-n kéo từ

HOADON và thả

qua MATHANG

hoặc ngược lại.

Double click

vào loại MKH,

thêm vào 2

thuộc tính SL

và DONGIA.

Chọn loại MKH 1-n kéo từ KHACHHANG

và thả qua HOADON.

- Sinh code SQL trong Case Studio: Vào menu Model -> Generate script (F9).

Chọn các chức năng cần sinh code SQL -> Nhấn vào nút Generate và View, sau

đó ta có thể lưu lại tập tin script này.

Chú ý: Nhớ bỏ chọn tại mục Check Script.

HƯỚNG DẪN  13

XIV

HƯỚNG DẪN

- Biểu diễn mô hình trên bằng phần mềm Toad Data Modeler:

- Tạo bảng KHACHHANG:

HƯỚNG DẪN  15

Tại thẻ SQL Preview cho phép chúng ta xem code SQL được sinh ra.

XVI

HƯỚNG DẪN

Tương tự cho việc tạo các bảng còn lại.

Sau khi tạo các bảng cùng mối kết hợp (giống cách làm trong Case Studio), phần

mềm  cũng  cho  phép  chúng  ta  sinh  code  SQL  cho  toàn  bộ  database,  bằng  cách  vào

menu Model -> Generate DDL Script -> Run… (F9).

HƯỚNG DẪN  17

Học viên lần lượt thực hiện các bài tập bên dưới trong giờ thực hành với sự hướng

dẫn của GV phụ trách môn học.

XVIII

HƯỚNG DẪN

BÀI 1:  HỆ THỐNG QUẢN LÝ THƯ VIỆN

1.1 MÔ TẢ

Một thư viện cần tin học hóa khâu quản lý thông tin sách và việc mượn trả sách

như sau:

Thư  viện  có  nhiều  nhân  viên  làm  việc  như  thủ  thư,  nhân  viên  quản  lý  sách…

Thông tin của một nhân viên phân biệt bằng mã nhân viên, họ, tên, phái, ngày sinh,

chức vụ, số điện thoại...

Thư viện có rất nhiều đầu sách, mỗi đầu sách có những thông tin lưu trữ và phân

biệt bằng mã đầu sách, tên sách, năm xuất bản, số lượng hiện có... và được phân

chia thành nhiều thể loại sách khác nhau (tiểu thuyết, truyện ngắn, tin học, anh

văn…). Một thể loại sách bao gồm nhiều đầu sách khác nhau nhưng một đầu sách

chỉ thuộc một thể loại duy nhất. Một cuốn sách được xuất bản bởi một nhà xuất bản

nào đó. Thông tin nhà xuất bản cũng được lưu trữ và phân biệt bằng mã xuất bản,

địa chỉ và số điện thoại của nhà xuất bản đó.

Đọc giả là đối tượng đọc và mượn sách của thư viện và được cấp một thẻ đọc giả

gồm các thông tin lưu trữ và quản lý như: mã độc giả, họ, tên, địa chỉ, email... Trên

thẻ ghi rõ ngày cấp và hạn sử dụng của thẻ đó. Tại một thời điểm đọc giả chỉ có

một thẻ có giá trị sử dụng duy nhất và sẽ được gia hạn hoặc cấp thẻ mới khi hết

hạn sử dụng. Đọc giả sẽ đóng lệ phí theo năm, nếu thẻ quá hạn hoặc chưa đóng lệ

phí thì không có giá trị.

Khi mượn sách đọc giả tự tra cứu thông tin sách mượn, thủ thư sẽ kiểm tra sách

mượn và số lượng mượn theo quy định. Nếu hợp lệ, thủ thư sẽ lập một phiếu mượn

sách ghi rõ ngày mượn, ngày trả cụ thể. Một độc giả được quyền mượn tối đa về

nhà 3 cuốn sách khác nhau, tuy nhiên nếu đọc giả đó vẫn còn sách quá hạn chưa

trả thì sẽ không được mượn thêm. Trong một phiếu mượn đọc giả không được mượn

2 sách cùng 1 đầu sách. Độc giả phải đóng lệ phí theo năm, hết năm thì phải đóng

phí, nếu không đóng phí thì sẽ không được mượn sách nữa.

HƯỚNG DẪN  19

Khi trả sách, thủ thư sẽ kiểm tra tình trạng và ngày trả quy định, nếu trễ hạn

hoặc mất, rách sách thủ thư sẽ lập phiếu phạt ghi rõ nội dung và phí phạt cụ thể

cho từng cuốn sách của phiếu mượn.

Quy  định  khi  trả  sách:  Sách  phải  nguyên  vẹn  như  cũ,  không  rách,  không  mất

trang sách, không được viết lên sách… nếu vi phạm dựa vào tỷ lệ hư tổn của sách

so với lúc đầu và giá trị của sách mà có mức phạt khác nhau như 1%--50% giá trị

của sách.

Hàng tháng thủ thư sẽ thống kê sách mượn, sách mất, sách hư hỏng, sách mượn

quá hạn… để lên kế hoạch nhập sách và phân bổ sách cho hiệu quả.

1.2 CÂU HỎI

1)  Xác định các loại thực thể cùng thuộc tính tương ứng. Chọn kiểu dữ liệu và độ

rộng thích hợp cho từng thuộc tính, gạch chân dưới khóa chính. Giải thích tại sao

lại chọn kiểu dữ liệu và độ rộng như vậy?

2)  Xây dựng mô hình quan niệm dữ liệu (mô hình thực thể kết hợp) với đầy đủ mối

kết hợp cùng bản số tương ứng cho hệ thống quản lý trên.

3)  Dùng phần mềm biểu diễn mô hình thực thể kết hợp ở trên. Lưu lại file với tên

phù hợp.

4)  Hãy thử đổi tên và sửa độ rộng của 1 khóa ngoại bất kỳ, nhận xét?

XX

HƯỚNG DẪN

BÀI 2:  HỆ THỐNG QUẢN LÝ CỬA

HÀNG NƯỚC GIẢI KHÁT

2.1 MÔ TẢ

Một cửa hàng kinh doanh nước giải khát cần tin học hóa việc mua bán nước giải

khát của cửa hàng. Dưới đây là mô tả về nghiệp vụ.

Cửa hàng buôn bán nhiều loại nước giải khát (NGK) của nhiều nhãn hiệu khác

nhau (chẳng hạn như Pepsi, Coca Cola, Bia Sài Gòn...). Một nhãn hiệu được phân

biệt bằng mã loại, tên loại riêng và có nhiều nước giải khát cùng loại. Nước giải khát

được lưu trữ và phân biệt bằng mã, tên, đơn vị tính…

Để đáp ứng nhu cầu mua hàng của khách không bị thiếu hụt, cửa hàng nhập các

loại nước giải khát từ các nhà cung  ứng. Mỗi loại chỉ được nhập từ một nhà cung

ứng, thông tin nhà cung ứng được liên hệ và lưu trữ trong hệ thống bằng tên, địa

chỉ và số điện thoại. Nhân viên cửa hàng sẽ liên hệ, lập và gởi đơn đặt hàng (ĐĐH)

đến các nhà cung ứng trong đó ghi rõ ngày đặt hàng, ngày nhận hàng và số lượng

đặt cụ thể trên từng đơn hàng. Mỗi ĐĐH có thể giao tối đa 3 đợt. Mỗi đợt giao hàng

nhà  cung  ứng  sẽ  gởi  kèm  theo  phiếu  giao  hàng  trên  đó  ghi  cụ  thể  ngày  giao,  số

lượng  chi tiết  các  mặt hàng được  và  số tiền  phải  trả  cho số lượng  mặt  hàng  trên

phiếu giao và số đơn hàng được giao.

Khi khách đến mua hàng, cửa hàng sẽ kiểm tra trong kho số lượng các mặt hàng

NGK khách yêu cầu. Nếu số lượng có đủ trong kho thì khách được giao hàng ngay

cùng với hóa đơn tính tiền cần thanh toán. Nếu không đủ thì đối với các khách quen

cửa hàng sẽ hẹn giao hàng nhiều đợt vào các ngày khác bằng các phiếu hẹn theo

hóa đơn đó. Thông tin hóa đơn, phiếu hẹn giao hàng sẽ được lưu trữ cập nhật vào

hệ thống để phục vụ cho việc tra cứu và thống kê.

Đối với khách vãng lai thì hóa đơn sẽ được thanh toán và giao hàng ngay tại cửa

hàng, còn đối với các khách quen cửa hàng cho phép trả chậm bằng cách lập các

phiếu ghi nợ và sẽ ghi nhận lại ngày, số tiền khách trả tiền cho các phiếu ghi nợ đó.

Hệ thống ghi nhận và lưu trữ toàn bộ thông tin trên để quản lý một cách chặt

HƯỚNG DẪN  21

chẽ và hiệu quả.

2.2 CÂU HỎI

1) Xác định các loại thực thể cùng thuộc tính tương ứng, xác định kiểu dữ liệu và độ

rộng phù hợp, gạch chân dưới khóa chính.

2) Xây dựng mô hình quan niệm dữ liệu (mô hình thực thể kết hợp) với đầy đủ mối

kết hợp cùng bản số tương ứng cho hệ thống quản lý trên.

3) Dùng phần mềm vẽ mô hình thực thể kết hợp ở trên, lưu lại với tên file phù hợp.

4) Hãy sinh code SQL của mô hình, lưu lại file script.

5) Mở SQL Server, tạo mới database với tên NGK. Mở file script ở Câu 4, thực thi

file để tạo các bảng. Nhận xét thứ tự tạo các bảng?

XXII

HƯỚNG DẪN

BÀI 3:  HỆ THỐNG QUẢN LÝ KHÁCH

SẠN

3.1 MÔ TẢ

Một khách sạn cần tin học hóa khâu quản lý tài sản và việc thuê phòng trong

khách sạn. Dưới đây là thông tin mô tả.

Khách sạn có nhiều khu vực, mỗi khu vực có nhiều phòng, mỗi phòng được phân

biệt bằng số phòng, số người ở tối đa và đơn giá thuê phòng tính theo ngày. Trong

mỗi phòng đều có trang bị một số loại tiện nghi như: ti vi, tủ lạnh, điện thoại... Mỗi

tiện nghi thuộc cùng một loại đều có một số thứ tự phân biệt với các tiện nghi khác

trong cùng loại. Một tiện nghi có thể được sắp xếp trang bị cho nhiều phòng khác

nhau được quản lý và theo dõi tình trạng thông qua các phiếu lắp đặt. Nhân viên

khách sạn khi muốn luân chuyển hoặc trang bị tiện nghi cho phòng phải lập một

phiếu lắp đặt trong đó ghi rõ ngày cụ thể và tình trạng của tiện nghi đó, trong một

ngày một thiết bị chỉ trang bị cho một phòng duy nhất.

Khách muốn thuê phòng có thể liên hệ nhân viên tiếp tân bằng điện thoại, website

của khách sạn hoặc đặt trực tiếp tại khách sạn. Nhân viên quản lý sẽ kiểm tra thông

tin khách đặt phòng, thông tin phòng đặt và số người ở để tư vấn và chọn phòng

thích  hợp.  Đồng  thời  ghi nhận  họ  tên,  số  CMND,  quốc  tịch  của  những người  thuê

phòng… Hệ thống sẽ lập một phiếu đặt phòng ghi rõ thông tin các phòng đặt, ngày

nhận phòng, ngày trả dự kiến và tiền cọc (nếu không nhận phòng sau thời gian lập

phiếu, khách sẽ bị mất cọc). Hệ thống sẽ lưu trữ thông tin đặt phòng và cập nhật

tình trạng phòng đặt vào hệ thống và xuất phiếu đặt phòng cho khách.

Khách thuê phòng có thể sử dụng thêm các dịch vụ (thuê xe, tắm hơi, ăn sáng,

karaoke...). Thông tin dịch vụ được phân biệt bằng mã dịch vụ, tên dịch vụ, đơn vị

tính và đơn giá riêng. Mỗi lần một khách hàng sử dụng dịch vụ, đều được hệ thống

ghi nhận bằng phiếu sử dụng có ghi nhận cụ thể ngày sử dụng và số lượng sử dụng

HƯỚNG DẪN  23

cụ thể. Nếu trong một ngày khách thuê phòng sử dụng một dịch vụ nhiều lần thì

tiền dịch vụ được cộng dồn thành một lần và lưu thành một bộ.

Khi khách trả phòng, nhân viên phục vụ phòng sẽ kiểm tra tiện nghi và tình trạng

để báo lại cho nhân viên thanh toán, nếu xảy ra tình trạng hư hỏng và mất mát thì

sẽ lập phiếu đền bù. Khi trả phòng và thanh toán nhân viên sẽ lập hóa đơn bao gồm

tiền thuê phòng và tiền sử dụng dịch vụ của phòng đó.

Quy định hư hỏng được khách sạn quy định khách đề bù theo từng tiện nghi và

mức độ thiệt hại nhất định.

3.2 CÂU HỎI

1) Xác định các loại thực thể cùng thuộc tính tương ứng, xác định kiểu dữ liệu và độ

rộng phù hợp, gạch chân dưới khóa chính.

2) Xây dựng mô hình quan niệm dữ liệu (mô hình thực thể kết hợp) với đầy đủ mối

kết hợp cùng bản số tương ứng cho hệ thống quản lý trên.

3) Dùng phần mềm vẽ mô hình thực thể kết hợp ở trên, lưu lại với tên file phù hợp.

4) Hãy thử xóa 1 thuộc tính khóa ngoại trong 1 loại thực thể bất kỳ, nhận xét?

5) Nếu có yêu cầu “Tên tiện nghi là duy nhất”, ta sẽ chỉ định trong phần mềm Case

Studio như thế nào?

XXIV

HƯỚNG DẪN

BÀI 4:  QUẢN LÝ CHO THUÊ VĂN

PHÒNG Ở CAO ỐC

4.1 MÔ TẢ

Để quản lý việc thuê văn phòng ở một cao ốc, cần có các thông tin và các quy tắc

quản lý sau:

Mỗi tầng có nhiều phòng, mỗi phòng có thể có các diện tích sử dụng khác nhau. Có

mã phòng dùng để phân biệt.

Khách hàng muốn thuê phòng thì phải đến tòa nhà để tham khảo vị trí, diện tích

phòng và giá cả. Giá cả phòng được ấn định tùy theo độ cao, diện tích sử dụng…

Khách hàng đồng ý thuê thì sẽ làm hợp đồng với bộ phận quản lý cao ốc, khách có

thể làm hợp đồng thuê cùng lúc nhiều phòng. Thời gian của đợt thuê ít nhất 6 tháng và

sau đó có thể gia hạn thêm. Khách phải trả trước tiền thuê của 6 tháng đầu tiên, từ

tháng thứ 7 nếu có thì phải trả vào đầu mỗi tháng. Giá thuê phòng không kể chi phí

điện và các chi phí cho các dịch vụ khác nếu có. Tất cả các vấn đề trên đều được nêu

trong nội dung hợp đồng…

Ngoài ra, để đảm bảo an toàn, bộ phận quản lý nhà cũng phải biết thông tin về các

nhân  viên làm  việc ở  các  văn phòng  trong tòa nhà. Mỗi  nhân  viên  có  một  mã  số  để

phân biệt, có hình ảnh nhân viên, thuộc một công ty nào, chức vụ, ở phòng mấy, tầng

mấy… Khi một công ty có tuyển nhân viên mới thì phải báo cáo thông tin về nhân viên

đó cho bộ phận quản lý tòa nhà.

Các nhân viên làm việc tại các văn phòng của cao ốc sẻ được cấp một thẻ giữ xe do

cao ốc cấp để quản lý tránh việc mất xe, trên thẻ có ghi: mã thẻ, thông tin của nhân

viên làm việc tại các văn phòng cao ốc.

Cách 1 năm cao ốc sẽ tiến hành kiểm tra tình trạng các phòng của cao ốc để có kế

hoạch tu sửa kip thời.

Nếu các phòng tự ý thay đổi, chỉnh sửa kết cấu của văn phòng thì sẽ bị phạt theo

HƯỚNG DẪN  25

quy định của cao ốc.

4.2 CÂU HỎI

1) Xác định các loại thực thể cùng thuộc tính tương ứng, xác định kiểu dữ liệu và độ

rộng phù hợp, gạch chân dưới khóa chính.

2) Xây dựng mô hình quan niệm dữ liệu (mô hình thực thể kết hợp) với đầy đủ mối

kết hợp cùng bản số tương ứng cho hệ thống quản lý trên.

3) Dùng phần mềm vẽ mô hình thực thể kết hợp ở trên, lưu lại với tên file phù hợp.

Chú ý cách vẽ mối kết hợp bậc 2.

4) Nếu  ta  cần  bổ  sung  ràng  buộc  “Giá  thuê  phòng  phải  lớn  hơn  0”  và  “Ngày  lập

phiếu thuê phòng phải nhỏ hơn hoặc bằng ngày hiện hành” thì ta phải chỉ định

trong phần mềm cách thực hiện như thế nào?

5) Hãy sinh code SQL cho mô hình trên. Xem kỹ cấu trúc các câu lệnh và so sánh

với môn học Cơ sở dữ liệu và Quản trị cơ sở dữ liệu đã học trước đó?

XXVI

HƯỚNG DẪN

BÀI 5:  QUẢN LÝ HỒ SƠ BỆNH ÁN CỦA

BỆNH NHÂN

5.1 MÔ TẢ

Để tin học hóa việc quản lý bệnh án của các bệnh nhân tại một bệnh viện quốc tế

cần các thông tin quản lý sau:

Một bệnh nhân lần đầu tiên khám bệnh tại bệnh viện được phát phiếu đăng ký khám

bệnh và theo dõi sức khỏe thường xuyên của bệnh viện. Bệnh nhân cần đóng một lệ

phí hằng năm cho việc quản lý và khám định kỳ hằng năm.

Thông tin phiếu đăng ký bao gồm: Họ tên, địa chỉ, ngày sinh, điện thoại liên lạc và

một ảnh chụp… Nhờ thông tin của phiếu đăng ký này và lệ phí đóng một năm, bệnh

nhân được phát hồ sơ bệnh án. Thông tin hồ sơ bệnh án bao gồm: Trang bìa ghi Mã hồ

sơ để phân biệt các bệnh nhân khác nhau và các thông tin từ phiếu đăng ký. Các trang

sau ghi nhận phiếu khám bệnh, thông tin ghi nhận bao gồm: Ngày giờ khám, bác sĩ

khám, khoa điều trị, triệu chứng (Nhức đầu, thân nhiệt, huyết áp…), toa thuốc  điều trị

cho  triệu  chứng trên  và  các  xét  nghiệm cần  thiết.  Tất  cả thông  tin  trên được  phòng

chăm sóc và theo dõi khách hàng ghi nhận lại trên máy vi tính sau khi bệnh nhận làm

thủ tục xuất viện và thanh toán viện phí. Thông tin này tiện cho việc theo dõi diễn biến

của bệnh, phản ứng phụ do thuốc gây ra cũng như hiệu quả của việc điều trị và trách

nhiệm của bác sĩ trong các đợt điều trị.

Mỗi khi bệnh nhân khám bệnh lần sau có thể mang hồ sơ bệnh án theo hoặc chỉ cần

báo mã hồ sơ (hoặc các thông tin tìm kiếm khác để lấy ra hồ sơ trong máy vi tính). Các

bác sĩ điều trị lần này có thể biết được lý lịch bệnh án và sức khỏe của bệnh nhân để

đưa ra cách điều trị thích hợp nhất.

Các bệnh nhân có hồ sơ bệnh án ngoài việc điều trị bệnh còn có quyền lợi khám sức

khoẻ định kỳ theo quý mà không phải đóng tiền. Bệnh nhân có thể gọi đến phòng chăm

sóc khách hàng để có cuộc hẹn chính xác ngày giờ khám phù hợp với thời gian rãnh rỗi

của khách hàng. Thông tin các đợt khám sức khỏe cũng được ghi nhận như một lần

điều trị nhưng không có bệnh hoặc phát hiện mầm bệnh sớm nhất để phục vụ khách

HƯỚNG DẪN  27

hàng hiệu quả nhất.

5.2 CÂU HỎI

1)  Xác định các loại thực thể cùng thuộc tính tương ứng, xác định kiểu dữ liệu và

độ rộng phù hợp, gạch chân dưới khóa chính.

2)  Xây dựng mô hình quan niệm dữ liệu (mô hình thực thể kết hợp) với đầy đủ mối

kết hợp cùng bản số tương ứng cho hệ thống quản lý trên.

3)  Dùng phần mềm vẽ mô hình thực thể kết hợp ở trên, lưu lại với tên file phù hợp.

4)  Thử đặt tên 2 loại mối kết hợp giống nhau (tên vai trò), sau đó sinh code SQL

và thực thi trong SQL Server, rút ra nhận xét gì?

XXVIII  HƯỚNG DẪN

BÀI 6:  QUẢN LÝ CÔNG TY DU LỊCH

6.1 MÔ TẢ

Cty Du lịch Văn Hóa Việt TP.HCM muốn tin học hóa việc quản lý tình hình đăng ký

các tour DL của khách và thông tin các tour cho khách.

Mục đích của chương trình tin học hoá là cung cấp thông tin các tour DL để quản cáo

trên website của công ty. Quản lý tình hình đăng ký du lịch ở các tour để tiện việc sắp

xếp lịch thực hiện các tour cho nhân viên hướng dẫn du lịch. Mọi tour được xem như

xuất phát từ TP.HCM.

Thông tin tour bao gồm: Mã tour dùng để phân biệt, tên tour, số ngày thực hiện,

đơn giá cho một khách. Khách đăng ký du lịch có hai loại khách: Khách đi trên 12 người

xem như khách theo đoàn và điền vào phiếu đăng ký theo đoàn, khách đi theo đoàn

được chọn ngày đi bất kỳ cho tour mình chọn, và có ghi nhận: Tên cơ quan (Hoặc ghi

tên đại diện gia đình), địa chỉ cơ quan, điện thoại cơ quan, người đại diện, số người đi,

nếu có mua bảo hiểm phải kèm theo danh sách những người được đi. Công ty cho xe

đến đón tại địa điểm do đoàn yêu cầu. Thông tin của khách theo đoàn được lưu trữ trên

máy tính để tiện cho việc chiêu mãi hay liên lạc sau này. “Khách lẻ” là khách đăng ký

dưới 12 người, đi cá nhân hay bạn bè, khi đi du lịch theo tour phải đăng ký theo chuyến.

Mỗi chuyến có ngày đi theo lịch của công ty. Khách lẽ có thể đăng ký tại các điểm bán

vé lẻ khác nhau gần nơi mình ở, và đến điạ điểm đón theo quy định của công ty để

cùng đi theo một tour duy nhất.

Nhân viên hướng dẫn du lịch được phân công theo đoàn của một tour nhất định hoặc

phân công theo chuyến đi theo khách lẻ sao cho không chồng chéo lịch phân công. Mỗi

chuyến khách lẻ được phân công một nhân viên cụ thể, khách theo đoàn có thể nhiều

nhân viên  nếu đoàn  đi  đông.  Lương  của  nhân viên  được  tính  theo  lương  căn bản  và

lương theo từng tour mà nhân viên thực hiện trong tháng.

Một tour du lịch có thể có nhiều nơi dừng chân, chính là nơi đến quan trọng của tour,

cũng chính là nơi đi tiếp theo của tour, kết thúc tour là TP.HCM. Mỗi nơi dừng chân xác

HƯỚNG DẪN  29

định có đổi phương tiện hay không, có hay không nơi ăn, có hay không khách sạn ở lại,

loại  khách  sạn  (2,3,4  hoặc  5  sao),  như  vậy  với  một  tour  du  lịch  có  thể  dùng  nhiều

phương tiện khách nhau, ví dụ như: Đi máy bay tới nơi A, tiếp theo đi xe đò tới nơi B,

và tàu hỏa tới nơi C, từ C về TP.HCM bằng máy bay. Ngoài ra tour du lịch còn ghi nhận

điểm tham quan (các di tích lịch sử, danh lam thắng cảnh…), mỗi điểm tham quan ghi

nhận mã số để phân biệt, tên điểm tham quan, địa điểm tham quan, nội dung, ý nghĩa).

Có sự việc xảy ra, nhân viên phải thông báo cho công ty để lập phiếu xử lý tour cho

tour đó, để công ty đưa ra hướng giải quyết kịp thời theo quy định của công ty.

Sau khi kết thúc tour, công ty sẽ gửi phiếu khảo sát cho khách hàng, ghi nhận lại

các góp ý nhằm mục đích phục vụ khách hàng tốt hơn.

6.2 CÂU HỎI

1)  Xác định các loại thực thể cùng thuộc tính tương ứng, xác định kiểu dữ liệu và

độ rộng phù hợp, gạch chân dưới khóa chính.

2)  Xây dựng mô hình quan niệm dữ liệu (mô hình thực thể kết hợp) với đầy đủ mối

kết hợp cùng bản số tương ứng cho hệ thống quản lý trên.

3)  Dùng phần mềm vẽ mô hình thực thể kết hợp ở trên, lưu lại với tên file phù hợp.

XXX

HƯỚNG DẪN

BÀI 7:  QUẢN LÝ NHÂN SỰ

7.1 MÔ TẢ

Để tin học hoá việc quản lý nhân sự tại công ty sơn Đông Á, cần quản lý một số

quyết định và các  thông tin sau:

Nhân viên sau khi được tuyển dụng phải có quyết định tuyển dụng, quyết định tuyển

dụng phải ghi rõ thời gian thử việc tại một phòng ban có nhu cầu tuyển dụng (ví dụ

phòng tài chính kế toán, phòng kỹ thuật, phòng sản xuất...), thông tin về mức lương

thử việc, nội dung của quyết định ghi rõ điều khoản của hai bên (nhà tuyển dụng và

người được tuyển dụng). Hết thời gian thử việc nhân viên sẽ được chính thức ký hợp

đồng và nhận một số quyết định liên quan như: Quyết định chức vụ và phụ cấp chức

vụ (nếu có). Quyết định lương ghi rõ mức lương cơ bản, phụ cấp lương hay phụ cấp độc

hại (nếu có). Quá trình tăng lương hay bổ nhiệm chức vụ cũng được ghi nhận qua các

quyết định trên. Hợp đồng tuyển dụng có hai loại, hợp đồng dài hạn và hợp đồng ngắn

hạn. Đối với hợp đồng dài hạn công ty phải làm hồ sơ Bảo hiểm y tế và Bảo hiểm xã

hội cho nhân viên và được trích trừ trong bảng lương theo mức đóng.

Lương nhân viên được tính hằng tháng dưạ vào quyết định lương, quyết định chức

vụ, bảng chấm công và phiếu ghi nhận giờ phụ trội trong tháng. Phiếu ghi nhận giờ phụ

trội và phiếu chấm công do ban chấm công thực hiện. Phiếu ghi nhận phụ trội  gồm các

thông tin: Số phiếu, ngày phụ trội, số giờ phụ trội, hình thức phụ trội (tăng ca, ngày

lễ, ngày nghỉ), giờ phụ trội được tính 1.5 lần giờ lao động bình thường. Chi tiết phiếu

phụ trội ghi rõ cho từng nhân viên tham gia phụ trội đó. Hằng tuần các trưởng phòng,

ban, phân xưởng lập kế hoạch phân công cho từng nhân viên theo các ca làm việc và

lên  kế  hoạch  phụ  trội  nếu  có  và  đưa  cho  ban  chấm  công  theo  dõi  việc  thực  hiện  và

chấm công. Bảng chấm công sẽ đưa vào máy tính để thực hiện bảng lương hằng tháng.

  Hệ thống còn phải quản lý các quyết định khen thưởng, quyết định kỷ luật đối  với

cá nhân hay tập thể phòng ban. Mỗi quyết định khen thưởng tương ứng với số tiền khen

thưởng qua phiếu chi khen thưởng, hay quyết định xử phạt tương ứng với số tiền nộp

phạt thể hiện qua phiếu thu nộp phạt được phát hay trừ lương trong bảng lương. Việc

chi cho ngày lễ, thưởng cuối năm, lương tháng 13 cũng thực hiện theo quyết định khen

HƯỚNG DẪN  31

thưởng như trên do giám đốc ký.

7.2 CÂU HỎI

1)   Xác định các loại thực thể cùng thuộc tính tương ứng, xác định kiểu dữ liệu và

độ rộng phù hợp, gạch chân dưới khóa chính.

2)  Xây dựng mô hình quan niệm dữ liệu (mô hình thực thể kết hợp) với đầy đủ mối

kết hợp cùng bản số tương ứng cho hệ thống quản lý trên.

3)  Dùng phần mềm vẽ mô hình thực thể kết hợp ở trên, lưu lại với tên file phù hợp.

XXXII  HƯỚNG DẪN

BÀI 8:  QUẢN LÝ CUỘC ĐUA XE ĐẠP

CÚP TRUYỀN HÌNH TP.HCM

8.1 MÔ TẢ

Hằng năm, cuộc đua xe đạp Cúp truyền hình TP.HCM được tổ chức bởi HTV và được

nhiều đội đăng ký tham gia. Ban tổ chức dự tính tin học hóa để quản lý các thông tin

liên quan đến cuộc đua, tính toán kết quả chính xác và nhanh chóng.

Mỗi đơn vị dự thi sẽ đăng ký số kíp tham gia dự thi. Mỗi đơn vị được đăng ký từ 1

đến 2 êkíp (bao gồm đội chính và đội trẻ).

Mỗi năm, cuộc đua sẽ có các đơn vị bảo trợ khác nhau. Các đơn vị bảo trợ sẽ hỗ trợ

chi phí tổ chức cuộc đua và cho các giải thưởng cho vận động viên. Các đơn vị bảo trợ

sẽ được ưu tiên quảng cáo trong suốt thời gian cuộc đua tiến hành.

Mỗi cuộc đua, vận động viên sẽ tham dự một và chỉ một êkíp. Mỗi vận động viên

đăng ký sẽ cung cấp cho Ban tổ chức biết họ, tên, ngày tháng năm sinh và quốc tịch.

Một êkíp gồm 4 vận động viên trong đó có một là trưởng êkíp. Ngoài ra, mỗi một êkíp

còn có một huấn luyện viên, một bác sĩ chăm sóc sức khỏe cho vận động viên và một

tài xế lái xe. Mỗi êkíp sẽ được trang bị một xe để phục vụ cho việc tiếp tế và di chuyển

cùng một điện thoại di động để liên lạc với Ban tổ chức.

Cuộc đua tổ chức thành nhiều chặng, mỗi chặng có thể đua nước rút hay đua tính

giờ.

Mỗi chặng đua tính giờ sẽ quy định thời gian tối đa để vận động viên đến đích. Vận

động viên nào không đến đích trước thời gian đó sẽ bị phạt bằng cách cộng thêm thời

gian vào bảng tính thời gian của vận động viên đó. Thời gian phạt sẽ bằng hai lần hiệu

số thời gian đến đích trừ thời gian tối đa quy định. Các vận động viên bị chấn thương

hay vì lý do nào đó mà không hoàn tất chặng sẽ bị phạt thời gian bằng thời gian phạt

của người về đích cuối cùng cộng thêm 10 phút.

HƯỚNG DẪN  33

Mỗi chặng đua nước rút sẽ quy định thời gian thưởng cho ba vận động viên về đầu.

Vận động viên nào đạt thời gian thưởng sẽ được trừ thời gian trong bảng tính thời gian

của vận động viên đó.

Thông tin về mỗi chặng bao gồm: chặng đua trước (nếu có), chặng đua sau (nếu

có), tên chặng, địa điểm xuất phát, địa điểm đích, số km, hình thức đua (nước rút hay

tính giờ), thời gian tối đa quy định (đối với đua tính giờ), thời gian thưởng (đối với đua

nước rút) và địa điểm tiếp tế (nếu có).

Các thông số kỹ thuật cần quan tâm đối với mỗi chặng: danh sách các vận động

viên, ê kíp dẫn đầu, tốc độ trung bình, tỷ lệ vận động viên về trước thời gian quy định.

Vận động viên nào về đích trước tiên trong một chặng sẽ được mặc áo xanh thắng

chặng đó do Ban tổ chức cấp. Tùy theo địa phương ở địa điểm đích, các vận động viên

về đích thứ tự từ một đến mười và các ê kíp có tổng thời gian trong chặng ít nhất theo

thứ tự nhất, nhì, ba có thể được giải thưởng của địa phương đó hay không.

Cuối  cuộc  đua,  vận  động  viên  có  bảng  tính  thời  gian  ngắn  nhất  sẽ  mặc  áo  vàng

chung  cuộc  cho  toàn  bộ  cuộc  đua.  Các  vận  động  viên  xếp  thứ  nhất  (áo  vàng  chung

cuộc), hai và ba sẽ được nhận giải thưởng của Ban tổ chức. Sau đó, tổng thời gian của

mỗi êkíp sẽ được tính và xếp hạng cho các êkíp. Các êkíp xếp thứ nhất, nhì và ba sẽ

được giải thưởng của Ban tổ chức.

Thông tin về giải thưởng gồm có tên giải thưởng, đối tượng được thưởng (cá nhân

thay ê kíp), loại giải thưởng (cho chặng hay toàn cuộc), nguồn cấp giải thưởng (Ban tổ

chức, địa phương, nhà tài trợ...), loại giải thưởng (tiền hay hiện vật), trị giá giải thưởng,

mô tả giải thưởng (nếu là hiện vật).

8.2 CÂU HỎI

1)   Xác định các loại thực thể cùng thuộc tính tương ứng, xác định kiểu dữ liệu và

độ rộng phù hợp, gạch chân dưới khóa chính.

2)  Xây dựng mô hình quan niệm dữ liệu (mô hình thực thể kết hợp) với đầy đủ mối

kết hợp cùng bản số tương ứng cho hệ thống quản lý trên.

3)  Dùng phần mềm vẽ mô hình thực thể kết hợp ở trên, lưu lại với tên file phù hợp.

XXXIV  HƯỚNG DẪN

TÀI LIỆU THAM KHẢO

[1].  Văn  Như  Bích  B,  Võ  Hoàng  Khang  (2018).  Phân  tích  thiết  kế  hệ  thống.  Khoa

CNTT, ĐH Công Nghệ TP.HCM.

[2].  Đồng thị Bích Thủy (2013), Giáo trình phân tích thiết kế hệ thống thông tin. Khoa

CNTT, ĐH Khoa học Tự nhiên, ĐH Quốc Gia TP.HCM.

[3].  D.Maier (2012), The theory of relational databases. Computer Science Press.

[4].  Jeffrey  D.  Ullman  (2012),  Nguyên  lý  các  hệ  cơ  sở  dữ  liệu  và  cơ  sở  tri  thức

(Principles of data base and knowledge base Systems). NXB Thống kê.

[5].  Các website HTTT kinh tế (2012). Tài liệu trực tuyến. Giáo dục.

[6].  Nhóm tác giả thuộc Viện Tin Học (2010). Phân tích, thiết kế, cài đặt hệ thống

thông tin quản lý. Viện Tin Học, Hà Nội.

[7].  James  A. Senn (2010).  Analysis  and  Design  of  Information  Systems.  Mc  Graw

Hill, New York.

[8].  James Martin (2010). Structured Analysis and System Specification. Yourdon Inc,

New York.

