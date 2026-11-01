BỘ GIÁO DỤC VÀ ĐÀO TẠO
THỰC HÀNH
QUẢN TRỊ CƠ SỞ DỮ LIỆU
Biên soạn: ThS. Võ Hoàng Khang
Tài Liệu Lưu Hành Tại HUTECH www.hutech.edu.vn

THỰC HÀNH QUẢN TRỊ CƠ SỞ DỮ LIỆU
Ấn bản 6/2019

I
MỤC LỤC
MỤC LỤC
MỤC LỤC ...................................................................................................................I
HƯỚNG DẪN ........................................................................................................... II
BÀI 1: HƯỚNG DẪN ..................................................................................................... 1
1.1 Đăng nhập SQL Server ....................................................................................... 1
1.2 Tạo Database bằng công cụ ............................................................................... 2
1.3 Attach Database ................................................................................................ 3
1.4 gán quyền sở hữu DATABASE ............................................................................. 6
1.5 DEtach Database ................................................................................................ 8
1.6 Backup Database ............................................................................................... 8
1.7 Restore database ............................................................................................. 10
BÀI 2: QUẢN LÝ BÁN HÀNG ....................................................................................... 11
2.1 Tạo DB, cÁc Table vÀ cài đặt ràng buộc toàn vẹn ............................................. 11
2.2 Nhập dữ liệu cho các table ............................................................................... 12
2.3 Thực hiện các câu hỏi ....................................................................................... 14
Tạo các view sau: .................................................................................................. 14
Tạo các procedure sau: .......................................................................................... 16
Tạo các function sau: ............................................................................................. 17
Tạo các trigger để thực hiện các ràng buộc sau: ........................................................ 17
BÀI 3: QUẢN LÝ SẢN XUẤT ........................................................................................ 19
3.1 Tạo database, các table và cài đặt ràng buộc toàn vẹn .................................... 19
3.2 Nhập dữ liệu cho các table ............................................................................... 19
3.3 Thực hiện các câu hỏi ....................................................................................... 21
Tạo các view sau: .................................................................................................. 21
Tạo các Function sau: ............................................................................................ 22
Tạo các Procedure sau: .......................................................................................... 22
Viết các trigger để thực hiện các ràng buộc sau: ........................................................ 23
BÀI 4: QUẢN LÝ SẢN PHẨM ....................................................................................... 24
4.1 Tạo database, các table và cài đặt ràng buộc toàn vẹn .................................... 24
4.2 Nhập dữ liệu cho các table ............................................................................... 25
4.3 Thực hiện các câu truy vấn .............................................................................. 29
Tạo các view sau: .................................................................................................. 29
Viết các Stored Procedure sau ................................................................................. 29
Tạo các Trigger sau: .............................................................................................. 30
Cussor: ................................................................................................................ 30
Bảo mật phân quyền: ............................................................................................ 30

II
HƯỚNG DẪN
HƯỚNG DẪN
MÔ TẢ MÔN HỌC
- Bài tập thực hành bao gồm 3 bài cụ thể, mỗi bài chứa các nội dung gắn liền với
bài học lý thuyết, có độ khó tăng dần. Học viên lần lượt làm tuần tự các bài tập trong
các buổi thực hành tại phòng máy với sự hướng dẫn của giảng viên giảng dạy thực
hành.
- Cuối mỗi buổi thực hành, cần sao lưu dữ liệu (Detach/Backup) để về nhà làm tiếp
hay có thể thực hành vào các buổi tiếp theo (Attach/Restore).
NỘI DUNG MÔN HỌC
- BÀI 1 - QUẢN LÝ BÁN HÀNG
- BÀI 2 - QUẢN LÝ SẢN XUẤT
- BÀI 3 - QUẢN LÝ SẢN PHẨM

1
HƯỚNG DẪN
BÀI 1: HƯỚNG DẪN
1.1 ĐĂNG NHẬP SQL SERVER
Khởi động SQL Server, tại Server name, chọn <Browse for more…>
Chọn tên máy và click OK.

2
HƯỚNG DẪN
1.2 TẠO DATABASE BẰNG CÔNG CỤ
Tại cửa sổ Object Explorer, Right Click vào Databases, chọn New Database…
Nhập vào các mục:
Database name: Tên DB cần tạo (Ví dụ: QLBANHANG)
Owner: Chọn như hình bên dưới.

3
HƯỚNG DẪN
Nhấn OK để tạo mới Database.
1.3 ATTACH DATABASE
Tại cửa sổ Object Explorer, Right Click vào Databases, chọn Attach…

4
HƯỚNG DẪN
Click vào nút Add…

5
HƯỚNG DẪN
Chỉ ra tập tin .MDF, SQL Server sẽ tự tìm tập tin .LDF ở cùng đường dẫn, nếu
không tìm thấy thì sẽ tạo mới:
Nhấn OK để attach.

6
HƯỚNG DẪN
1.4 GÁN QUYỀN SỞ HỮU DATABASE
Right Click vào Database, chọn Properties…

7
HƯỚNG DẪN
Chỉ định user là “NT AUTHORITY\SYSTEM” tại mục Owner:

8
HƯỚNG DẪN
1.5 DETACH DATABASE
Right Click vào tên Database, chọn Tasks => Detach…
1.6 BACKUP DATABASE
Right Click vào tên Database, chọn Tasks => Back Up…

9
HƯỚNG DẪN
Chú ý các lựa chọn:
• Backup type: Full (backup toàn bộ dữ liệu đang có)
Differential (backup những gì thay đổi so với lần Full
Backup gần nhất)
• Nút Add… Chỉ ra đường dẫn lưu tập tin .BAK
Chọn OK để hoàn tất Backup.

10
HƯỚNG DẪN
1.7 RESTORE DATABASE
Tại cửa sổ Object Explorer, Right Click vào Database, chọn Restore Database…
Tại Source: Chỉ ra tập tin .BAK tại mục Device.
Tại Destination: Chỉ ra tên DB cần Restore.
Cuối cùng, chọn OK để hoàn tất.

11
QUẢN LÝ BÁN HÀNG

BÀI 2:  QUẢN LÝ BÁN HÀNG
2.1 TẠO DB, CÁC TABLE VÀ CÀI ĐẶT RÀNG BUỘC
TOÀN VẸN
Tạo Database QLBANHANG. Tạo các Table có cấu trúc như sau:
(Lưu ý: các thuộc tính có gạch chân là field khóa chính, gạch nét đứt là khóa
ngoại)
Table: KHACHHANG
|   Name    | Type      | Size  |
| --------- | --------- | ----- |
|   MAKH    | varchar   | 5     |
|   TENKH   | nvarchar  | 30    |
|   DIACHI  | nvarchar  | 50    |
|   DT      | varchar   | 11    |
|   EMAIL   | varchar   | 30    |
Ràng buộc: TENKH not null, DT có thể có từ 8 chữ số đến 11 chữ số.
Table: VATTU
|   Name    | Type      | Size  |
| --------- | --------- | ----- |
|   MAVT    | varchar   | 5     |
|   TENVT   | Nvarchar  | 30    |
|   DVT     | Nvarchar  | 20    |
|   GIAMUA  | Money     |       |
|   SLTON   | Int       |       |
Ràng buộc: TENVT not null, GIAMUA > 0, SLTON >= 0.

12
QUẢN LÝ BÁN HÀNG

Table: HOADON
|   Name    |     | Type     |     | Size  |     |
| --------- | --- | -------- | --- | ----- | --- |
|   MAHD    |     | varchar  |     | 10    |     |
|   NGAY    |     | date     |     |       |     |
|   MAKH    |     | varchar  |     | 5     |     |
|   TONGTG  |     | float    |     |       |     |
Ràng buộc: Giá trị nhập vào cho field NGAY phải trước ngày hiện hành.
Table: CTHD
|   Name       |     | Type     |     | Size  |     |
| ------------ | --- | -------- | --- | ----- | --- |
|   MAHD       |     | varchar  |     | 10    |     |
|   MAVT       |     | varchar  |     | 5     |     |
|   SL         |     | int      |     |       |     |
|   KHUYENMAI  |     | float    |     |       |     |
|   GIABAN     |     | float    |     |       |     |
Ràng buộc: Giá trị nhập vào cho field SL phải lớn hơn 0.
2.2 NHẬP DỮ LIỆU CHO CÁC TABLE
Table VATTU:
|     | MAVT  | TENVT    | DVT   | GIAMUA  | SLTON   |
| --- | ----- | -------- | ----- | ------- | ------- |
|     | VT01  | Xi măng  | Bao   | 50000   | 5000    |
|     | VT02  | Cát      | Khối  | 45000   | 50000   |
|     | VT03  | Gạch     | Viên  | 120     | 800000  |
ống
|     | VT04  | Gạch  | Viên  | 110  | 800000  |
| --- | ----- | ----- | ----- | ---- | ------- |
thẻ
|     | VT05  | Đá lớn  | Khối  | 25000  | 100000  |
| --- | ----- | ------- | ----- | ------ | ------- |
|     | VT06  | Đá nhỏ  | Khối  | 33000  | 100000  |

13
QUẢN LÝ BÁN HÀNG

|     |     | VT07  |     | Lam gió  |     | Cái  |     | 15000  |     | 50000  |     |
| --- | --- | ----- | --- | -------- | --- | ---- | --- | ------ | --- | ------ | --- |
Table KHACHHANG:
| MAKH  |     | TENKH          |     |     | DIACHI    |     | DT        |     | EMAIL          |     |     |
| ----- | --- | -------------- | --- | --- | --------- | --- | --------- | --- | -------------- | --- | --- |
| KH01  |     | Nguyễn Thị Bé  |     |     | Tân Bình  |     | 38457895  |     | bnt@yahoo.com  |     |     |
KH02  Lê Hoàng Nam  Bình Chánh 39878987  namlehoang@gmail.com
| KH03  |     | Trần Thị Chiêu   |     |     | Tân Bình         |     | 38457895  |     | NULL               |     |     |
| ----- | --- | ---------------- | --- | --- | ---------------- | --- | --------- | --- | ------------------ | --- | --- |
| KH04  |     | Mai Thị Quế Anh  |     |     | Bình Chánh NULL  |     |           |     | NULL               |     |     |
| KH05  |     | Lê Văn Sáng      |     |     | Quận 10          |     | NULL      |     | sanglv@hcm.vnn.vn  |     |     |
| KH06  |     | Trần Hoàng       |     |     | Tân Bình         |     | 38457897  |     | NULL               |     |     |
Table HOADON:
|     |     | MAHD   |     |     | NGAY        |     |     | MAKH  | TONGTG  |     |     |
| --- | --- | ------ | --- | --- | ----------- | --- | --- | ----- | ------- | --- | --- |
|     |     | HD001  |     |     | 12/05/2010  |     |     | KH01  | NULL    |     |     |
|     |     | HD002  |     |     | 25/05/2010  |     |     | KH02  | NULL    |     |     |
|     |     | HD003  |     |     | 25/05/2010  |     |     | KH01  | NULL    |     |     |
|     |     | HD004  |     |     | 25/05/2010  |     |     | KH04  | NULL    |     |     |
|     |     | HD005  |     |     | 26/05/2010  |     |     | KH04  | NULL    |     |     |
|     |     | HD006  |     |     | 02/06/2010  |     |     | KH03  | NULL    |     |     |
|     |     | HD007  |     |     | 22/06/2010  |     |     | KH04  | NULL    |     |     |
|     |     | HD008  |     |     | 25/06/2010  |     |     | KH03  | NULL    |     |     |
|     |     | HD009  |     |     | 15/08/2010  |     |     | KH04  | NULL    |     |     |
|     |     | HD010  |     |     | 30/09/2010  |     |     | KH01  | NULL    |     |     |
Table CTHD:
|     | MAHD   |     | MAVT  |     |     | SL  | KHUYENMAI  |       |     | GIABAN  |        |
| --- | ------ | --- | ----- | --- | --- | --- | ---------- | ----- | --- | ------- | ------ |
|     | HD001  |     | VT01  |     |     |     | 5          | NULL  |     |         | 52000  |
|     | HD001  |     | VT05  |     |     | 10  |            | NULL  |     |         | 30000  |

14
QUẢN LÝ BÁN HÀNG

| HD002  | VT03  | 10000  | NULL  | 150    |
| ------ | ----- | ------ | ----- | ------ |
| HD003  | VT02  | 20     | NULL  | 55000  |
| HD004  | VT03  | 50000  | NULL  | 150    |
| HD004  | VT04  | 20000  | NULL  | 120    |
| HD005  | VT05  | 10     | NULL  | 30000  |
| HD005  | VT06  | 15     | NULL  | 35000  |
| HD005  | VT07  | 20     | NULL  | 17000  |
| HD006  | VT04  | 10000  | NULL  | 120    |
| HD007  | VT04  | 20000  | NULL  | 125    |
| HD008  | VT01  | 100    | NULL  | 55000  |
| HD008  | VT02  | 20     | NULL  | 47000  |
| HD009  | VT02  | 25     | NULL  | 48000  |
| HD010  | VT01  | 25     | NULL  | 57000  |
2.3 THỰC HIỆN CÁC CÂU HỎI
Tạo các view sau:
1.  Hiển thị danh sách các khách hàng có địa chỉ là “Tân Bình” gồm mã khách
hàng, tên khách hàng, địa chỉ, điện thoại, và địa chỉ E-mail.
2.  Hiển thị danh sách các khách hàng gồm các thông tin mã khách hàng, tên
khách hàng, địa chỉ và địa chỉ E-mail của những khách hàng chưa có số điện
thoại.
3.  Hiển thị danh sách các khách hàng chưa có số điện thoại và cũng chưa có địa
chỉ Email gồm mã khách hàng, tên khách hàng, địa chỉ.
4.  Hiển thị danh sách các khách hàng đã có số điện thoại và địa chỉ E-mail gồm
mã khách hàng, tên khách hàng, địa chỉ, điện thoại, và địa chỉ E-mail.
5.  Hiển thị danh sách các vật tư có đơn vị tính là “Cái” gồm mã vật tư, tên vật tư
và giá mua.
6.  Hiển thị danh sách các vật tư gồm mã vật tư, tên vật tư, đơn vị tính và giá
mua mà có giá mua trên 25000.

15
QUẢN LÝ BÁN HÀNG
7. Hiển thị danh sách các vật tư là “Gạch” (bao gồm các loại gạch) gồm mã vật
tư, tên vật tư, đơn vị tính và giá mua.
8. Hiển thị danh sách các vật tư gồm mã vật tư, tên vật tư, đơn vị tính và giá
mua mà có giá mua nằm trong khoảng từ 20000 đến 40000.
9. Lấy ra các thông tin gồm Mã hóa đơn, ngày lập hóa đơn, tên khách hàng, địa
chỉ khách hàng và số điện thoại.
10. Lấy ra các thông tin gồm Mã hóa đơn, tên khách hàng, địa chỉ khách hàng và
số điện thoại của ngày 25/5/2010.
11. Lấy ra các thông tin gồm Mã hóa đơn, ngày lập hóa đơn, tên khách hàng, địa
chỉ khách hàng và số điện thoại của những hóa đơn trong tháng 6/2010.
12. Lấy ra danh sách những khách hàng (tên khách hàng, địa chỉ, số điện thoại)
đã mua hàng trong tháng 6/2010.
13. Lấy ra danh sách những khách hàng không mua hàng trong tháng 6/2010
gồm các thông tin tên khách hàng, địa chỉ, số điện thoại.
14. Lấy ra các chi tiết hóa đơn gồm các thông tin mã hóa đơn, mã vật tư, tên vật
tư, đơn vị tính, giá bán, giá mua, số lượng, trị giá mua (giá mua * số lượng),
trị giá bán (giá bán * số lượng).
15. Lấy ra các chi tiết hóa đơn gồm các thông tin mã hóa đơn, mã vật tư, tên vật
tư, đơn vị tính, giá bán, giá mua, số lượng, trị giá mua (giá mua * số lượng),
trị giá bán (giá bán * số lượng) mà có giá bán lớn hơn hoặc bằng giá mua.
16. Lấy ra các thông tin gồm mã hóa đơn, mã vật tư, tên vật tư, đơn vị tính, giá
bán, giá mua, số lượng, trị giá mua (giá mua * số lượng), trị giá bán (giá bán
* số lượng) và cột khuyến mãi với khuyến mãi 10% cho những mặt hàng bán
trong một hóa đơn lớn hơn 100.
17. Tìm ra những mặt hàng chưa bán được.
18. Tạo bảng tổng hợp gồm các thông tin: mã hóa đơn, ngày hóa đơn, tên khách
hàng, địa chỉ, số điện thoại, tên vật tư, đơn vị tính, giá mua, giá bán, số
lượng, trị giá mua, trị giá bán.
19. Tạo bảng tổng hợp tháng 5/2010 gồm các thông tin: mã hóa đơn, ngày hóa
đơn, tên khách hàng, địa chỉ, số điện thoại, tên vật tư, đơn vị tính, giá mua,
giá bán, số lượng, trị giá mua, trị giá bán.

16
QUẢN LÝ BÁN HÀNG
20. Tạo bảng tổng hợp quý 1 – 2010 gồm các thông tin: mã hóa đơn, ngày hóa
đơn, tên khách hàng, địa chỉ, số điện thoại, tên vật tư, đơn vị tính, giá mua,
giá bán, số lượng, trị giá mua, trị giá bán.
21. Lấy ra danh sách các hóa đơn gồm các thông tin: Số hóa đơn, ngày, tên khách
hàng, địa chỉ khách hàng, tổng trị giá của hóa đơn.
22. Lấy ra hóa đơn có tổng trị giá lớn nhất gồm các thông tin: Số hóa đơn, ngày,
tên khách hàng, địa chỉ khách hàng, tổng trị giá của hóa đơn.
23. Lấy ra hóa đơn có tổng trị giá lớn nhất trong tháng 5/2010 gồm các thông tin:
Số hóa đơn, ngày, tên khách hàng, địa chỉ khách hàng, tổng trị giá của hóa
đơn.
24. Đếm xem mỗi khách hàng có bao nhiêu hóa đơn.
25. Đếm xem mỗi khách hàng, mỗi tháng có bao nhiêu hóa đơn.
26. Lấy ra các thông tin của khách hàng có số lượng hóa đơn mua hàng nhiều
nhất.
27. Lấy ra các thông tin của khách hàng có số lượng hàng mua nhiều nhất.
28. Lấy ra các thông tin về các mặt hàng mà được bán trong nhiều hóa đơn nhất.
29. Lấy ra các thông tin về các mặt hàng mà được bán nhiều nhất.
30. Lấy ra danh sách tất cả các khách hàng gồm Mã khách hàng, tên khách hàng,
địa chỉ, số lượng hóa đơn đã mua (nếu khách hàng đó chưa mua hàng thì cột
số lượng hóa đơn để trống)
Tạo các procedure sau:
1. Lấy ra danh các khách hàng đã mua hàng trong ngày X, với X là tham số
truyền vào.
2. Lấy ra danh sách khách hàng có tổng trị giá các đơn hàng lớn hơn X (X là
tham số).
3. Lấy ra danh sách X khách hàng có tổng trị giá các đơn hàng lớn nhất (X là
tham số).
4. Lấy ra danh sách X mặt hàng có số lượng bán lớn nhất (X là tham số).
5. Lấy ra danh sách X mặt hàng bán ra có lãi ít nhất (X là tham số).
6. Lấy ra danh sách X đơn hàng có tổng trị giá lớn nhất (X là tham số).

17
QUẢN LÝ BÁN HÀNG
7. Tính giá trị cho cột khuyến mãi như sau: Khuyến mãi 5% nếu SL > 100, 10%
nếu SL > 500.
8. Tính lại số lượng tồn cho tất cả các mặt hàng (SLTON = SLTON – tổng SL bán
được).
9. Tính trị giá cho mỗi hóa đơn.
10. Tạo ra table KH_VIP có cấu trúc giống với cấu trúc table KHACHHANG. Lưu các
khách hàng có tổng trị giá của tất cả các đơn hàng >=10,000,000 vào table
KH_VIP.
Tạo các function sau:
1. Viết hàm tính doanh thu của năm, với năm là tham số truyền vào.
2. Viết hàm tính doanh thu của tháng, năm, với tháng và năm là 2 tham số truyền
vào.
3. Viết hàm tính doanh thu của khách hàng với mã khách hàng là tham số truyền
vào.
4. Viết hàm tính tổng số lượng bán được cho từng mặt hàng theo tháng, năm nào
đó. Với mã hàng, tháng và năm là các tham số truyền vào, nếu tháng không
nhập vào tức là tính tất cả các tháng.
5. Viết hàm tính lãi (giá bán – giá mua) * số lượng bán được cho từng mặt hàng,
với mã mặt hàng là tham số truyền vào. Nếu mã mặt hàng không truyền vào
thì tính cho tất cả các mặt hàng.
Tạo các trigger để thực hiện các ràng buộc sau:
1. Thực hiện việc kiểm tra các ràng buộc khóa ngoại.
2. Không cho phép CASCADE DELETE trong các ràng buộc khóa ngoại. Ví dụ không
cho phép xóa các HOADON nào có SOHD còn trong table CTHD.
3. Không cho phép user nhập vào hai vật tư có cùng tên.
4. Khi user đặt hàng thì KHUYENMAI là 5% nếu SL > 100, 10% nếu SL > 500.
5. Chỉ cho phép mua các mặt hàng có số lượng tồn lớn hơn hoặc bằng số lượng
cần mua và tính lại số lượng tồn mỗi khi có đơn hàng.
6. Không cho phép user xóa một lúc nhiều hơn một vật tư.
7. Mỗi hóa đơn cho phép bán tối đa 5 mặt hàng.

18
QUẢN LÝ BÁN HÀNG
8. Mỗi hóa đơn có tổng trị giá tối đa 50000000.
9. Không được phép bán hàng lỗ quá 50%.
10. Chỉ bán mặt hàng Gạch (các loại gạch) với số lượng là bội số của 100.

19
QUẢN LÝ SẢN XUẤT
BÀI 3: QUẢN LÝ SẢN XUẤT
3.1 TẠO DATABASE, CÁC TABLE VÀ CÀI ĐẶT
RÀNG BUỘC TOÀN VẸN
Tạo lược đồ cơ sở dữ liệu như sau:
(Sinh viên tự chọn kiểu dữ liệu và thuộc tính sao cho phù hợp)
Loai(MaLoai, TenLoai)
SanPham(MaSP, TenSP, MaLoai)
NhanVien(MaNV, HoTen, NgaySinh, Phai)
PhieuXuat(MaPX, NgayLap, MaNV)
CTPX(MaPX, MaSP, SoLuong)
Các ràng buộc:
• Tên sản phẩm là duy nhất nhưng không là khóa chính.
• Mã phiếu xuất là số nguyên tự động tăng.
• Các mã số của các bảng còn lại là phải nhập vào và có kiểu là char(5).
• Số lượng xuất kho là số nguyên dương.
• Phái của nhân viên có giá trị là 1 (nếu là nam) hoặc 0 (nếu là nữ), mặc định
là 0.
Giá trị cho ngày sinh của nhân viên là >=18 tuổi và <=55 tuổi.
3.2 NHẬP DỮ LIỆU CHO CÁC TABLE
Bảng LOAI:
Mã loại Tên loại

20
QUẢN LÝ SẢN XUẤT

1  Vật liệu xây dựng
2  Hàng tiêu dùng
3  Ngũ cốc
Bảng SANPHAM:
|     | Mã SP  | Tên SP          | Mã loại  |     |
| --- | ------ | --------------- | -------- | --- |
|     | 1      | Xi măng         | 1        |     |
|     | 2      | Gạch            | 1        |     |
|     | 3      | Gạo nàng hương  | 3        |     |
|     | 4      | Bột mì          | 3        |     |
|     | 5      | Kệ chén         | 2        |     |
|     | 6      | Đậu xanh        | 3        |     |
Bảng NHANVIEN:
| Mã NV  | Họ tên           |     | Ngày sinh  | Phái  |
| ------ | ---------------- | --- | ---------- | ----- |
| NV01   | Nguyễn Mai Thi   |     | 15/5/82    | 0     |
| NV02   | Trần Đình Chiến  |     | 2/12/80    | 1     |
| NV03   | Lê Thị Chi       |     | 23/1/79    | 0     |

21
QUẢN LÝ SẢN XUẤT

Bảng PHIEUXUAT:
| Mã phiếu xuất  | Ngày lập   | Mã NV  |
| -------------- | ---------- | ------ |
| 1              | 12/3/2010  | NV01   |
| 2              | 3/2/2010   | NV02   |
| 3              | 1/6/2010   | NV03   |
| 4              | 16/6/2010  | NV01   |
Bảng CTPX:
| MAPX  | MASP  | Số lượng  |
| ----- | ----- | --------- |
| 1     | 1     | 10        |
| 1     | 2     | 15        |
| 1     | 3     | 5         |
| 2     | 2     | 20        |
| 3     | 1     | 20        |
| 3     | 3     | 25        |
| 4     | 5     | 12        |
3.3 THỰC HIỆN CÁC CÂU HỎI
Tạo các view sau:
1.  Cho biết mã sản phẩm, tên sản phẩm, tổng số lượng xuất của từng sản phẩm
trong năm 2010. Lấy dữ liệu từ View này sắp xếp tăng dần theo tên sản
phẩm.

22
QUẢN LÝ SẢN XUẤT
2. Cho biết mã sản phẩm, tên sản phẩm, tên loại sản phẩm mà đã được bán từ
ngày 1/1/2010 đến 30/6/2010.
3. Cho biết số lượng sản phẩm trong từng loại sản phẩm gồm các thông tin: mã
loại sản phẩm, tên loại sản phẩm, số lượng các sản phẩm.
4. Cho biết tổng số lượng phiếu xuất trong tháng 6 năm 2010.
5. Cho biết thông tin về các phiếu xuất mà nhân viên có mã NV01 đã xuất.
6. Cho biết danh sách nhân viên nam có tuổi trên 25 nhưng dưới 30.
7. Thống kê số lượng phiếu xuất theo từng nhân viên.
8. Thống kê số lượng sản phẩm đã xuất theo từng sản phẩm.
9. Lấy ra tên của nhân viên có số lượng phiếu xuất lớn nhất.
10. Lấy ra tên sản phẩm được xuất nhiều nhất trong năm 2010.
Tạo các Function sau:
1. Function F1 có 2 tham số vào là: tên sản phẩm, năm. Function cho biết: số
lượng xuất kho của tên sản phẩm đó trong năm này. (Chú ý: Nếu tên sản phẩm
đó không tồn tại thì phải trả về 0)
2. Function F2 có 1 tham số nhận vào là mã nhân viên. Function trả về số lượng
phiếu xuất của nhân viên truyền vào. Nếu nhân viên này không tồn tại thì trả
về 0.
3. Function F3 có 1 tham số vào là năm, trả về danh sách các sản phẩm được xuất
trong năm truyền vào.
4. Function F4 có một tham số vào là mã nhân viên để trả về danh sách các phiếu
xuất của nhân viên đó. Nếu mã nhân viên không truyền vào thì trả về tất cả
các phiếu xuất.
5. Function F5 để cho biết tên nhân viên của một phiếu xuất có mã phiếu xuất là
tham số truyền vào.
6. Function F6 để cho biết danh sách các phiếu xuất từ ngày T1 đến ngày T2. (T1,
T2 là tham số truyền vào). Chú ý: T1 <= T2.
7. Function F7 để cho biết ngày xuất của một phiếu xuất với mã phiếu xuất là
tham số truyền vào.
Tạo các Procedure sau:
1. Procedure tên là P1 cho có 2 tham số sau:

23
QUẢN LÝ SẢN XUẤT
• 1 tham số nhận vào là: tên sản phẩm.
• 1 tham số trả về cho biết: tổng số lượng xuất kho của tên sản phẩm này
trong năm 2010 (Không viết lại truy vấn, hãy sử dụng Function F1 ở câu
4 để thực hiện)
2. Procedure tên là P2 có 2 tham số sau:
• 1 tham số nhận vào là: tên sản phẩm.
• 1 tham số trả về cho biết: tổng số lượng xuất kho của tên sản phẩm này
trong khoảng thời gian từ đầu tháng 4/2010 đến hết tháng 6/2010 (Chú
ý: Nếu tên sản phẩm này không tồn tại thì trả về 0)
3. Procedure tên là P3 chỉ có duy nhất 1 tham số nhận vào là tên sản phẩm. Trong
Procedure này có khai báo 1 biến cục bộ được gán giá trị là: số lượng xuất kho
của tên sản phẩm này trong khoảng thời gian từ đầu tháng 4/2010 đến hết
tháng 6/2010. Việc gán trị này chỉ được thực hiện bằng cách gọi Procedure P2.
4. Procedure P4 để INSERT một record vào trong table LOAI. Giá trị các field là
tham số truyền vào.
5. Procedure P5 để DELETE một record trong Table NhânViên theo mã nhân viên.
Mã NV là tham số truyền vào.
Viết các trigger để thực hiện các ràng buộc sau:
1. Chỉ cho phép một phiếu xuất có tối đa 5 chi tiết phiếu xuất.
2. Chỉ cho phép một nhân viên lập tối đa 10 phiếu xuất trong một ngày.
3. Khi người dùng viết 1 câu truy vấn nhập 1 dòng cho bảng chi tiết phiếu xuất thì
CSDL kiểm tra, nếu mã phiếu xuất mới đó chưa tồn tại trong bảng phiếu xuất
thì CSDL sẽ không cho phép nhập và thông báo lỗi “Phiếu xuất này không tồn
tại”. Hãy viết 1 trigger đảm bảo điều này.

24
QUẢN LÝ SẢN PHẨM
BÀI 4: QUẢN LÝ SẢN PHẨM
4.1 TẠO DATABASE, CÁC TABLE VÀ CÀI ĐẶT
RÀNG BUỘC TOÀN VẸN
Tạo lược đồ CSDL sau: (Sinh viên tự chọn kiểu dữ liệu và thuộc tính sao cho phù
hợp)
LOAISP (MaLoai, TenLoai)
SANPHAM (MASP, TenSP, Mota, Gia, Maloai)
KHACHHANG (MAKH, TenKH, DC, DT)
DONDH (SoDDH, NgayDat, MAKH)
CTDDH (SoDDH, MASP, SoLuong)
NGUYENLIEU (MaNL, TenNL, DVT, Gia)
LAM (MaNL, MASP, SoLuong)
Giải thích:
▪ LOAISP: Mỗi loại sản phẩm có mã loại và tên loại.
▪ SANPHAM: Mỗi sản phẩm có mã số duy nhất, có tên sản phẩm, mô tả sản
phẩm và giá của sản phẩm. Mỗi sản phẩm chỉ thuộc 1 loại.
▪ KHACHHANG: Mỗi khách hàng có mã số, tên, địa chỉ và điện thoại.
▪ DONDH: Mỗi đơn đặt hàng có số đơn duy nhất, có ngày đặt và do 1 khách
hàng nào đó đặt.
▪ CTDDH: Mỗi đơn đặt hàng có thể đặt nhiều sản phẩm với số lượng khác
nhau cho từng sản phẩm.
▪ NGUYENLIEU: Mỗi nguyên liệu có mã số, tên nguyên liệu, đơn vị tính và giá.
▪ LAM: Mỗi sản phẩm được làm từ nhiều nguyên liệu với số lượng tương ứng.

25
QUẢN LÝ SẢN PHẨM

Yêu cầu:
Câu 1: Tạo CSDL QLSANPHAM – Tạo các bảng.
Câu 2: Tạo các ràng buộc khóa chính, khóa ngoại.
Câu 3: Xác định và tạo các ràng buộc dữ liệu khác: UNIQUE, CHECK, DEFAULT, RULE.
Câu 4: Xác định và tạo các chỉ mục cần thiết cho CSDL.
4.2 NHẬP DỮ LIỆU CHO CÁC TABLE
LOAISP
|     |     | MALOAI  | TENLOAI  |     |     |
| --- | --- | ------- | -------- | --- | --- |
|     |     | L01     | Tủ       |     |     |
|     |     | L02     | Bàn      |     |     |
|     |     | L03     | Giường   |     |     |
SANPHAM
| MASP  | TENSP            | MOTA                 |              | GIA      | MALOAI  |
| ----- | ---------------- | -------------------- | ------------ | -------- | ------- |
| SP01  | Tủ trang điểm    | Cao 1.4m, rộng 2.2m  |              | 1000000  | L01     |
| SP02  | Giường đơn Cali  | Rộng 1.4m            |              | 1500000  | L03     |
| SP03  | Tủ DDA           | Cao  1.6m,           | rộng  2.0m,  | 800000   | L01     |
cửa kiếng
| SP04  | Bàn ăn         | 1m x 1.5m   |     | 650000   | L02  |
| ----- | -------------- | ----------- | --- | -------- | ---- |
| SP05  | Bàn uống trà   | Tròn, 1.8m  |     | 1100000  | L02  |

26
QUẢN LÝ SẢN PHẨM

KHACHHANG
| MAKH   | TENKH     |                          | DC  |             | DT  |
| ------ | --------- | ------------------------ | --- | ----------- | --- |
| KH001  | Trần Hải  | 731 Trần Hưng Đạo, Q.1,  |     | 08-9776655  |     |
Cường  TP.HCM
| KH002  | Nguyễn Thị Bé  | 638 Nguyễn Văn Cừ, Q.5,  |     | 0913-666123  |     |
| ------ | -------------- | ------------------------ | --- | ------------ | --- |
TP.HCM
KH003  Trần Thị Minh  543 Mai Thị Lựu, Ba Đình, Hà  04-9238777
Hòa  Nội
KH004  Phạm Đình  975 Lê Lai, P.3, TP. Vũng Tàu   064-543678
Tuân
| KH005  | Lê Xuân  | 450 Trưng Vương, TP. Mỹ Tho,  |     | 073-987123  |     |
| ------ | -------- | ----------------------------- | --- | ----------- | --- |
Nguyện  Tiền Giang
| KH006  | Văn Hùng  | 291 Hồ Văn Huê, Q. PN, TP.HCM  |     | 08-8222111  |     |
| ------ | --------- | ------------------------------ | --- | ----------- | --- |
Dũng
KH012  Lê Thị Hương  980 Lê Hồng Phong, TP. Vũng  064-452100
Hoa  Tàu
KH016  Hà Minh Trí  332 Nguyễn Thái Học, TP. Quy  056-565656
Nhơn
DONDH
|     |     | SODDH  | NGAYDAT     | MAKH   |     |
| --- | --- | ------ | ----------- | ------ | --- |
|     |     | DH001  | 15/03/2010  | KH001  |     |
|     |     | DH002  | 15/03/2010  | KH016  |     |
|     |     | DH003  | 16/03/2010  | KH003  |     |

27
QUẢN LÝ SẢN PHẨM

|     | DH004  |     | 16/03/2010  |     | KH012  |     |
| --- | ------ | --- | ----------- | --- | ------ | --- |
|     | DH005  |     | 17/03/2010  |     | KH001  |     |
|     | DH006  |     | 01/04/2010  |     | KH002  |     |
CTDDH
|     | SODDH  |     | MASP  | SOLUONG  |     |     |
| --- | ------ | --- | ----- | -------- | --- | --- |
|     | DH001  |     | SP01  |          | 5   |     |
|     | DH001  |     | SP03  |          | 1   |     |
|     | DH002  |     | SP02  |          | 2   |     |
|     | DH003  |     | SP01  |          | 2   |     |
|     | DH003  |     | SP04  |          | 10  |     |
|     | DH003  |     | SP05  |          | 5   |     |
|     | DH004  |     | SP02  |          | 2   |     |
|     | DH004  |     | SP05  |          | 2   |     |
|     | DH005  |     | SP03  |          | 3   |     |
|     | DH006  |     | SP02  |          | 4   |     |
|     | DH006  |     | SP04  |          | 3   |     |
|     | DH006  |     | SP05  |          | 6   |     |
NGUYENLIEU
| MANL  |     | TENNL  |     | DVT  |     | GIA  |
| ----- | --- | ------ | --- | ---- | --- | ---- |
m3
| NL01  |     | Gỗ Lim XP  |     |     |     | 1200000  |
| ----- | --- | ---------- | --- | --- | --- | -------- |

28
QUẢN LÝ SẢN PHẨM

| NL02  | Gỗ Sao NT    |     | m3  | 1000000  |
| ----- | ------------ | --- | --- | -------- |
| NL03  | Gỗ tạp nham  |     | m3  | 500000   |
| NL04  | Đinh lớn     |     | kg  | 40000    |
| NL05  | Đinh nhỏ     |     | kg  | 30000    |
| NL06  | Kiếng        |     | m2  | 350000   |
LAM
| MANL  |     | MASP  | SOLUONG  |     |
| ----- | --- | ----- | -------- | --- |
| NL01  |     | SP01  | 1.2      |     |
| NL03  |     | SP01  | 0.3      |     |
| NL06  |     | SP01  | 2.5      |     |
| NL02  |     | SP02  | 1.1      |     |
| NL04  |     | SP02  | 2.2      |     |
| NL02  |     | SP03  | 0.9      |     |
| NL05  |     | SP03  | 2.1      |     |
| NL02  |     | SP04  | 1.3      |     |
| NL04  |     | SP04  | 1.7      |     |
| NL03  |     | SP05  | 0.8      |     |
| NL05  |     | SP05  | 0.5      |     |
| NL06  |     | SP05  | 2.4      |     |

29
QUẢN LÝ SẢN PHẨM
4.3 THỰC HIỆN CÁC CÂU TRUY VẤN
Tạo các view sau:
1. Danh sách các loại sản phẩm có nhiều sản phẩm nhất (Tên loại SP, số sản
phẩm).
2. Danh sách khách hàng không đặt hàng trong tháng 3/2010 (Tên KH, địa chỉ).
3. DS khách hàng đặt nhiều đơn đặt hàng nhất trong tháng 3/2010 (Tên KH, địa
chỉ).
4. Danh sách các sản phẩm không được đặt trong tháng 3/2010 (Tên SP, mô tả).
5. Danh sách khách hàng có đặt trên 10 cái tủ DDA (Tên KH, địa chỉ, tổng số
lượng).
6. DS các sản phẩm được làm từ nhiều loại nguyên liệu nhất (Tên SP, Giá, Số
loại).
7. Danh sách các sản phẩm có giá thành SX hơn 1 triệu (Tên SP, Giá thành SX).
8. DS các sản phẩm có lãi trên 20% (Tên SP, Giá thành SX, Giá bán, phần trăm
lãi).
9. Danh sách đơn đặt hàng có tổng số tiền lớn hơn 100 triệu (Số DDH, Ngày đặt,
Tổng tiền).
10. Danh sách các loại nguyên liệu dùng để làm tất cả các sản phẩm (TênNL, Giá).
11. Danh sách khách hàng có đặt tất cả các sản phẩm (Tên KH, DC).
12. Danh sách các sản phẩm tất cả các khách hàng đều đặt (Tên SP, Mô tả).
13. Danh sách khách hàng lâu nhất chưa đặt hàng (Tên KH, địa chỉ).
Viết các Stored Procedure sau
1. Liệt kê DS khách hàng (TênKH, DC) có đặt hàng vào Ngày tháng năm X.
2. Liệt kê DS khách hàng (TênKH, DC) có đặt hàng sản phẩm có mã số X.
3. Liệt kê DS khách hàng (TênKH, DC) có đặt hàng với tổng số tiền trên X (1 đơn).
4. Liệt kê DS khách hàng (TênKH, DC) có đặt hàng với tổng số tiền trên X (tất cả).
5. Liệt kê DS sản phẩm (TênSP, Giá thành SX, Giá) bán lãi trên X.
6. Liệt kê DS khách hàng (TênKH, DC) đã trên X ngày rồi chưa đặt hàng.
7. Liệt kê DS sản phẩm (TênSP, Số đơn) có tổng số đơn đặt hàng trên X.
8. Liệt kê DS sản phẩm (TênSP, Tổng SL) có tổng số lượng đặt hàng trên X.

30
QUẢN LÝ SẢN PHẨM
9. Liệt kê DS sản phẩm (TênSP, Tổng số tiền) có tổng số tiền đặt hàng trên X.
Tạo các Trigger sau:
1. Mỗi ngày mỗi khách hàng chỉ đặt tối đa 2 đơn hàng.
2. Mỗi đơn đặt hàng có tổng số lượng sản phẩm không quá 100.
3. Đảm bảo rằng mỗi sản phẩm không bị lỗ hơn 50%.
Cussor:
1. Viết thủ tục liệt kê (theo thứ tự giảm dần của giá) X sản phẩm đầu tiên của sản
phẩm có mã loại là Y (X, Y nhập khi gọi thủ tục) theo dạng sau:
• Tên loại: Tủ
• Sản phẩm 1: Tủ Trang điểm – Mô tả: Cao 1.4m, rộng 2.2m – Giá:
1000000
• Sản phẩm 2: Tủ DDA – Mô tả: Cao 1.6m, rộng 2.0m, cửa kiếng – Giá:
800000
…
2. Viết thủ tục cập nhật giá cho bảng sản phẩm như sau:
• Những sản phẩm có lãi trên 30% thì giảm giá 10%
• Những sản phẩm bị lỗ thì cập nhật giá bằng giá thành SX
• Những sản phẩm khác thì tăng 5%
3. Viết thủ tục in ra thống kê đặt hàng trong tháng X (nhập khi gọi thủ tục) có
dạng như sau:
Ngày 15/3/2004
1-DH001: KH001, Tổng tiền: 15000000
2-DH002: KH016, Tổng tiền: 27500000
Ngày 16/3/2004
1-DH003: KH003, Tổng tiền: 8000000
2-DH004: KH012, Tổng tiền: 1100000
Bảo mật phân quyền:
Tạo 3 user: Giám đốc, Kế toán và Nhân viên. Thực hiện phân quyền như sau:
• Giám đốc: Toàn quyền trên toàn bộ CSDL

31
QUẢN LÝ SẢN PHẨM
• Kế toán: Chỉ được xem trên bảng SANPHAM, LOAISP. Các bảng khác toàn
quyền.
• Nhân viên: Không được truy cập bảng NGUYENLIEU, LAM. Các bảng khác
được quyền xem, không được cập nhật.