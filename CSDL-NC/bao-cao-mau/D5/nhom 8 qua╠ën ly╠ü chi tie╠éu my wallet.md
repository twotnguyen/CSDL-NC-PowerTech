Ưng dụng quản lý chi tiêu

1 Mô tả đề tài

Hiện nay, nhiều người gặp khó khăn trong việc quản lý tài chính cá nhân do thói quen ghi chép thủ công, lưu trữ thông tin ở nhiều nơi hoặc quên các khoản thu chi đã phát sinh, dẫn đến tình trạng khó kiểm soát số tiền đã sử dụng và khó đạt được các mục tiêu tiết kiệm. Vì vậy, việc xây dựng một ứng dụng quản lý chi tiêu cá nhân thông minh là cần thiết nhằm giúp người dùng ghi chép, theo dõi và quản lý tài chính thuận tiện, chính xác và an toàn.

Hệ thống cho phép người dùng đăng ký tài khoản với các thông tin gồm mã người dùng, tên đăng nhập, email, họ tên, số điện thoại và đơn vị tiền tệ mặc định, chẳng hạn như VND. Để đảm bảo an toàn và thuận tiện, người dùng có thể đăng nhập bằng email hoặc thông qua tài khoản Google, Apple và Facebook. Hệ thống lưu thông tin xác thực như mã nhà cung cấp, mã tài khoản của nhà cung cấp, thông tin token và ngày liên kết. Một người dùng có thể liên kết nhiều tài khoản khác nhau nhưng chỉ có một phương thức xác thực được chọn làm mặc định. Ngoài ra, ứng dụng hỗ trợ bảo mật bằng mã PIN, vân tay hoặc nhận diện khuôn mặt trên thiết bị. Mỗi lần người dùng đăng nhập trên một thiết bị như Android, iOS hoặc Web, hệ thống sẽ tạo một phiên đăng nhập và lưu các thông tin gồm mã phiên, tên thiết bị, loại thiết bị, địa chỉ IP, refresh token, trạng thái hoạt động, thời gian hết hạn và thời điểm hoạt động gần nhất. Để quản lý tài chính, người dùng có thể tạo và quản lý các danh mục thu nhập, chi tiêu. Mỗi danh mục gồm mã danh mục, mã người dùng, tên danh mục, biểu tượng, màu sắc và loại danh mục là thu nhập hoặc chi tiêu. Hệ thống cung cấp một số danh mục mặc định, đồng thời cho phép người dùng thêm mới, chỉnh sửa hoặc ẩn danh mục theo nhu cầu. Bên cạnh đó, người dùng có thể thiết lập các phương thức thanh toán như tiền mặt, thẻ tín dụng, ví điện tử Momo hoặc tài khoản ngân hàng. Mỗi phương thức thanh toán gồm mã phương thức, mã người dùng, tên phương thức, biểu tượng và trạng thái mặc định, giúp người dùng dễ dàng lựa chọn nguồn tiền khi ghi nhận giao dịch.

Chức năng chính của hệ thống là ghi nhận và quản lý các giao dịch thu nhập, chi tiêu. Mỗi giao dịch gồm mã giao dịch, mã người dùng, mã danh mục, mã phương thức thanh toán, số tiền, loại giao dịch, ghi chú, ngày giờ thực hiện, tên cửa hàng và nguồn tạo giao dịch. Nguồn tạo có thể là nhập thủ công, quét hóa đơn, nhập từ tệp hoặc tự động định kỳ. Mỗi giao dịch phải thuộc một danh mục và có thể liên kết với một phương thức thanh toán. Đối với các hóa đơn mua sắm hoặc ăn uống, ứng dụng tích hợp chức năng quét hình ảnh để nhận diện và đọc thông tin trên hóa đơn. Hệ thống lưu lại nội dung nhận diện ban đầu và độ chính xác của kết quả để người dùng kiểm tra, đối chiếu và chỉnh sửa khi cần thiết. Một giao dịch có thể bao gồm nhiều chi tiết giao dịch, mỗi chi tiết có mã chi tiết, mã giao dịch, tên sản phẩm, số lượng, đơn giá, thành tiền, đơn vị tính và ghi chú. Ngoài ra, người dùng có thể chụp hoặc tải lên các tệp đính kèm như hình ảnh hóa đơn và chứng từ. Mỗi tệp được lưu với mã tệp, mã giao dịch, đường dẫn tệp, loại tệp, dung lượng tệp và ngày tạo. Để kiểm soát chi tiêu, người dùng có thể thiết lập ngân sách theo từng danh mục hoặc áp dụng cho toàn bộ khoản chi. Mỗi ngân sách gồm mã ngân sách, mã người dùng, mã danh mục nếu có, tên ngân sách, hạn mức tiền, chu kỳ áp dụng theo ngày, tuần, tháng hoặc năm, ngày bắt đầu, ngày kết thúc, ngưỡng cảnh báo và trạng thái hoạt động. Khi tổng số tiền chi tiêu trong chu kỳ đạt đến ngưỡng cảnh báo đã thiết lập, chẳng hạn 80% hạn mức, hệ thống sẽ gửi thông báo để nhắc nhở người dùng điều chỉnh việc chi tiêu. Bên cạnh đó, ứng dụng hỗ trợ quản lý các mục tiêu tiết kiệm như mua xe hoặc du lịch. Mỗi mục tiêu gồm mã mục tiêu, mã người dùng, tên mục tiêu, số tiền cần đạt, số tiền hiện có, ngày hết hạn, biểu tượng và trạng thái như đang thực hiện, hoàn thành hoặc đã hủy. Người dùng có thể theo dõi tiến độ tích lũy và chủ động lập kế hoạch tiết kiệm. Hệ thống còn có chức năng nhắc nhở, cho phép người dùng thiết lập mã nhắc nhở, mã người dùng, tiêu đề, nội dung, giờ nhắc, hình thức lặp lại như một lần, hằng ngày, hằng tuần hoặc hằng tháng, các ngày trong tuần, trạng thái hoạt động và thời điểm kích hoạt gần nhất. Qua đó, ứng dụng có thể nhắc người dùng ghi chép thu nhập và chi tiêu đúng thời gian đã cài đặt.

Cuối cùng, hệ thống cung cấp chức năng tìm kiếm giao dịch theo từ khóa, danh mục hoặc khoảng thời gian để người dùng dễ dàng tra cứu các khoản thu chi đã phát sinh. Dữ liệu được tổng hợp và hiển thị dưới dạng biểu đồ tròn, biểu đồ cột và biểu đồ đường, thể hiện tình hình thu nhập, chi tiêu cũng như xu hướng sử dụng tiền theo ngày, tuần và tháng. Các báo cáo này giúp người dùng nắm rõ tình hình tài chính, đánh giá thói quen chi tiêu và đưa ra quyết định sử dụng tiền hợp lý hơn. Về lưu trữ dữ liệu, ứng dụng sử dụng cơ sở dữ liệu trên thiết bị để lưu thông tin người dùng, giao dịch, danh mục và các dữ liệu liên quan. Nhờ đó, người dùng vẫn có thể thực hiện các chức năng ghi chép cơ bản ngay cả khi không có kết nối Internet. Khi thiết bị có mạng trở lại, dữ liệu sẽ được tự động đồng bộ với cơ sở dữ liệu trên máy chủ trực tuyến. Quá trình này giúp dữ liệu giữa thiết bị và máy chủ được cập nhật, hỗ trợ người dùng quản lý tài chính thuận tiện hơn ngay cả khi kết nối mạng không ổn định. Nhìn chung, hệ thống quản lý chi tiêu cá nhân giúp người dùng theo dõi các khoản thu nhập và chi tiêu, kiểm soát ngân sách, quản lý mục tiêu tiết kiệm, lưu trữ chứng từ, nhận thông báo nhắc nhở và xem báo cáo thống kê. Qua đó, ứng dụng góp phần hình thành thói quen ghi chép đầy đủ, sử dụng tiền hợp lý và quản lý tài chính cá nhân một cách khoa học hơn.

2 ĐỐI TƯỢNG THỰC THỂ

Thực thể cơ bản

Thực thể PHƯƠNG THỨC XÁC THỰC

|  |  |  |  |
| --- | --- | --- | --- |
| **Thuộc tính** | **Kiểu dữ liệu** | **Ràng buộc** | **Ý nghĩa** |
| ma\_xac\_thuc | INT | PK, IDENTITY | Mã phương thức xác thực |
| ma\_nguoi\_dung | INT | NOT NULL | Người dùng sở hữu phương thức xác thực |
| nha\_cung\_cap | NVARCHAR(20) | NOT NULL, CHECK | Nhà cung cấp xác thực: EMAIL, GOOGLE, APPLE, FACEBOOK |
| ma\_nha\_cung\_cap | NVARCHAR(255) | — | Mã tài khoản do nhà cung cấp cấp |
| mat\_khau\_ma\_hoa | NVARCHAR(255) | — | Mật khẩu đã mã hóa |
| access\_token | NVARCHAR(MAX) | — | Token truy cập |
| refresh\_token | NVARCHAR(MAX) | — | Token dùng để làm mới phiên |
| thoi\_han\_token | DATETIME2 | — | Thời hạn của token |
| la\_phuong\_thuc\_chinh | BIT | NOT NULL, DEFAULT 0 | Xác định đây có phải phương thức chính không |
| ngay\_lien\_ket | DATETIME2 | NOT NULL, DEFAULT | Thời điểm liên kết |
| su\_dung\_lan\_cuoi | DATETIME2 | — | Thời điểm sử dụng gần nhất |

Thực thể PHIÊN ĐĂNG NHẬP

|  |  |  |  |
| --- | --- | --- | --- |
| **Thuộc tính** | **Kiểu dữ liệu** | **Ràng buộc** | **Ý nghĩa** |
| ma\_phien | INT | PK, IDENTITY | Mã phiên đăng nhập |
| ma\_nguoi\_dung | INT | NOT NULL | Người dùng của phiên |
| ten\_thiet\_bi | NVARCHAR(100) | — | Tên thiết bị đăng nhập |
| loai\_thiet\_bi | NVARCHAR(20) | CHECK | Android, iOS, Web hoặc Other |
| token\_thiet\_bi | NVARCHAR(255) | — | Token của thiết bị |
| refresh\_token | NVARCHAR(255) | NOT NULL, UNIQUE | Token làm mới phiên |
| dia\_chi\_ip | NVARCHAR(45) | — | Địa chỉ IP đăng nhập |
| trang\_thai\_hoat\_dong | BIT | NOT NULL, DEFAULT 1 | Phiên còn hoạt động hay không |
| thoi\_gian\_het\_han | DATETIME2 | NOT NULL | Thời gian phiên hết hạn |
| ngay\_tao | DATETIME2 | NOT NULL, DEFAULT | Thời điểm tạo phiên |
| hoat\_dong\_lan\_cuoi | DATETIME2 | NOT NULL, DEFAULT | Thời điểm hoạt động cuối |

Thực thể DANH MỤC

|  |  |  |  |
| --- | --- | --- | --- |
| **Thuộc tính** | **Kiểu dữ liệu** | **Ràng buộc** | **Ý nghĩa** |
| ma\_danh\_muc | INT | PK, IDENTITY | Mã danh mục |
| ma\_nguoi\_dung | INT | NOT NULL | Người dùng sở hữu danh mục |
| ten\_danh\_muc | NVARCHAR(100) | NOT NULL | Tên danh mục |
| bieu\_tuong | NVARCHAR(50) | — | Biểu tượng đại diện |
| mau\_sac | NVARCHAR(10) | — | Màu hiển thị |
| loai\_danh\_muc | NVARCHAR(10) | NOT NULL, CHECK | THU\_NHAP hoặc CHI\_TIEU |
| la\_mac\_dinh | BIT | NOT NULL, DEFAULT 0 | Danh mục mặc định hay không |
| trang\_thai\_kich\_hoat | BIT | NOT NULL, DEFAULT 1 | Danh mục có đang sử dụng không |
| ngay\_tao | DATETIME2 | NOT NULL, DEFAULT | Ngày tạo |
| ngay\_cap\_nhat | DATETIME2 | NOT NULL, DEFAULT | Ngày cập nhật |

Thực thể PHƯƠNG THỨC THANH TOÁN

|  |  |  |  |
| --- | --- | --- | --- |
| **Thuộc tính** | **Kiểu dữ liệu** | **Ràng buộc** | **Ý nghĩa** |
| ma\_phuong\_thuc | INT | PK, IDENTITY | Mã phương thức |
| ma\_nguoi\_dung | INT | NOT NULL | Người dùng sở hữu |
| ten\_phuong\_thuc | NVARCHAR(50) | NOT NULL | Tên phương thức: tiền mặt, ngân hàng... |
| bieu\_tuong | NVARCHAR(50) | — | Biểu tượng phương thức |
| la\_mac\_dinh | BIT | NOT NULL, DEFAULT 0 | Có phải phương thức mặc định không |
| trang\_thai\_kich\_hoat | BIT | NOT NULL, DEFAULT 1 | Có đang sử dụng không |
| ngay\_tao | DATETIME2 | NOT NULL, DEFAULT | Ngày tạo |

**THỰC THỂ NGHIỆP VỤ**

Thực thể GIAO DỊCH

|  |  |  |  |
| --- | --- | --- | --- |
| **Thuộc tính** | **Kiểu dữ liệu** | **Ràng buộc** | **Ý nghĩa** |
| ma\_giao\_dich | INT | PK, IDENTITY | Mã giao dịch |
| ma\_nguoi\_dung | INT | NOT NULL | Người thực hiện giao dịch |
| ma\_danh\_muc | INT | NOT NULL | Danh mục của giao dịch |
| ma\_phuong\_thuc | INT | FK | Phương thức thanh toán |
| so\_tien | DECIMAL(15,2) | NOT NULL, CHECK >= 0 | Số tiền giao dịch |
| loai\_giao\_dich | NVARCHAR(10) | NOT NULL, CHECK | Thu nhập hoặc chi tiêu |
| ghi\_chu | NVARCHAR(MAX) | — | Nội dung ghi chú |
| ngay\_giao\_dich | DATETIME2 | NOT NULL | Ngày giờ giao dịch |
| ten\_cua\_hang | NVARCHAR(150) | — | Tên cửa hàng/đơn vị phát sinh giao dịch |
| nguon\_tao | NVARCHAR(20) | NOT NULL, DEFAULT, CHECK | Nguồn tạo: thủ công, OCR, nhập file, định kỳ |
| van\_ban\_ocr\_goc | NVARCHAR(MAX) | — | Nội dung OCR ban đầu |
| do\_chinh\_xac\_ocr | DECIMAL(5,2) | — | Độ chính xác nhận dạng OCR |
| da\_xoa | BIT | NOT NULL, DEFAULT 0 | Xác định giao dịch đã xóa hay chưa |
| ngay\_tao | DATETIME2 | NOT NULL, DEFAULT | Thời điểm tạo |
| ngay\_cap\_nhat | DATETIME2 | NOT NULL, DEFAULT | Thời điểm cập nhật |

Thực thể CHI TIẾT GIAO DỊCH

|  |  |  |  |
| --- | --- | --- | --- |
| **Thuộc tính** | **Kiểu dữ liệu** | **Ràng buộc** | **Ý nghĩa** |
| ma\_chi\_tiet | INT | PK, IDENTITY | Mã chi tiết |
| ma\_giao\_dich | INT | NOT NULL | Giao dịch chứa chi tiết |
| ten\_san\_pham | NVARCHAR(200) | NOT NULL | Tên sản phẩm |
| so\_luong | DECIMAL(10,3) | NOT NULL, DEFAULT 1 | Số lượng sản phẩm |
| don\_gia | DECIMAL(15,2) | NOT NULL, DEFAULT 0 | Đơn giá sản phẩm |
| thanh\_tien | DECIMAL(15,2) | NOT NULL, DEFAULT 0 | Thành tiền |
| don\_vi\_tinh | NVARCHAR(20) | — | Đơn vị tính |
| ghi\_chu | NVARCHAR(255) | — | Ghi chú chi tiết |

Thực thể NGÂN SÁCH

|  |  |  |  |
| --- | --- | --- | --- |
| **Thuộc tính** | **Kiểu dữ liệu** | **Ràng buộc** | **Ý nghĩa** |
| ma\_ngan\_sach | INT | PK, IDENTITY | Mã ngân sách |
| ma\_nguoi\_dung | INT | NOT NULL | Người lập ngân sách |
| ma\_danh\_muc | INT |  | Danh mục được áp dụng |
| ten\_ngan\_sach | NVARCHAR(100) | NOT NULL | Tên ngân sách |
| han\_muc\_tien | DECIMAL(15,2) | NOT NULL, CHECK > 0 | Số tiền tối đa |
| chu\_ky | NVARCHAR(10) | NOT NULL, CHECK | Hàng ngày/tuần/tháng/năm |
| ngay\_bat\_dau | DATE | NOT NULL | Ngày bắt đầu |
| ngay\_ket\_thuc | DATE | — | Ngày kết thúc |
| nguong\_canh\_bao | DECIMAL(5,2) | NOT NULL, DEFAULT 80 | Ngưỡng cảnh báo |
| trang\_thai\_kich\_hoat | BIT | NOT NULL, DEFAULT 1 | Ngân sách đang hoạt động hay không |
| ngay\_tao | DATETIME2 | NOT NULL, DEFAULT | Ngày tạo |
| ngay\_cap\_nhat | DATETIME2 | NOT NULL, DEFAULT | Ngày cập nhật |

Thực thể NHẮC NHỞ

|  |  |  |  |
| --- | --- | --- | --- |
| **Thuộc tính** | **Kiểu dữ liệu** | **Ràng buộc** | **Ý nghĩa** |
| ma\_nhac\_nho | INT | PK, IDENTITY | Mã nhắc nhở |
| ma\_nguoi\_dung | INT | NOT NULL | Người tạo nhắc nhở |
| tieu\_de | NVARCHAR(150) | NOT NULL | Tiêu đề nhắc nhở |
| noi\_dung | NVARCHAR(MAX) | — | Nội dung |
| gio\_nhac\_nho | TIME | NOT NULL | Thời gian nhắc |
| loai\_lap\_lai | NVARCHAR(20) | NOT NULL, CHECK | Một lần/ngày/tuần/tháng |
| cac\_ngay\_trong\_tuan | NVARCHAR(20) | — | Các ngày trong tuần cần nhắc |
| trang\_thai\_kich\_hoat | BIT | NOT NULL, DEFAULT 1 | Nhắc nhở có hoạt động không |
| lan\_kich\_hoat\_cuoi | DATETIME2 | — | Lần kích hoạt gần nhất |
| ngay\_tao | DATETIME2 | NOT NULL, DEFAULT | Ngày tạo |

Thực thể MỤC TIÊU TIẾT KIỆM

|  |  |  |  |
| --- | --- | --- | --- |
| **Thuộc tính** | **Kiểu dữ liệu** | **Ràng buộc** | **Ý nghĩa** |
| ma\_muc\_tieu | INT | PK, IDENTITY | Mã mục tiêu |
| ma\_nguoi\_dung | INT | NOT NULL | Người đặt mục tiêu |
| ten\_muc\_tieu | NVARCHAR(150) | NOT NULL | Tên mục tiêu |
| so\_tien\_muc\_tieu | DECIMAL(15,2) | NOT NULL, CHECK > 0 | Số tiền cần đạt |
| so\_tien\_hien\_co | DECIMAL(15,2) | NOT NULL, DEFAULT 0 | Số tiền hiện đã tiết kiệm |
| ngay\_het\_han | DATE | — | Hạn hoàn thành |
| bieu\_tuong | NVARCHAR(50) | — | Biểu tượng mục tiêu |
| trang\_thai | NVARCHAR(20) | NOT NULL, DEFAULT, CHECK | Đang thực hiện/hoàn thành/đã hủy |
| ngay\_tao | DATETIME2 | NOT NULL, DEFAULT | Ngày tạo |
| ngay\_cap\_nhat | DATETIME2 | NOT NULL, DEFAULT | Ngày cập nhật |

Thực thể TỆP ĐÍNH KÈM

|  |  |  |  |
| --- | --- | --- | --- |
| **Thuộc tính** | **Kiểu dữ liệu** | **Ràng buộc** | **Ý nghĩa** |
| ma\_tep | INT | PK, IDENTITY | Mã tệp |
| ma\_giao\_dich | INT | NOT NULL | Giao dịch chứa tệp |
| duong\_dan\_tep | NVARCHAR(255) | NOT NULL | Đường dẫn đến tệp |
| loai\_tep | NVARCHAR(20) | NOT NULL, DEFAULT | Loại tệp |
| dung\_luong\_tep | INT | — | Dung lượng tệp |
| ngay\_tao | DATETIME2 | NOT NULL, DEFAULT | Thời điểm tải tệp |

THỰC THỂ ĐỐI TƯỢNG NGOÀI

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Đối tượng** | **Thuộc tính/Thông tin** | **Kiểu dữ liệu** | **Ràng buộc** | **Ý nghĩa** |
| Google | Mã nhà cung cấp | NVARCHAR(255) | Liên kết với ma\_nha\_cung\_cap | Cho phép đăng nhập bằng Google |
| Apple | Mã nhà cung cấp | NVARCHAR(255) | Liên kết với ma\_nha\_cung\_cap | Cho phép đăng nhập bằng Apple |
| Facebook | Mã nhà cung cấp | NVARCHAR(255) | Liên kết với ma\_nha\_cung\_cap | Cho phép đăng nhập bằng Facebook |
| Email | Tài khoản/email | NVARCHAR | Liên kết với người dùng | Đăng nhập bằng email/mật khẩu |

Thiết bị người dùng

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Đối tượng** | **Thuộc tính/Thông tin** | **Kiểu dữ liệu** | **Ràng buộc** | **Ý nghĩa** |
| Google | Mã nhà cung cấp | NVARCHAR(255) | Liên kết với ma\_nha\_cung\_cap | Cho phép đăng nhập bằng Google |
| Apple | Mã nhà cung cấp | NVARCHAR(255) | Liên kết với ma\_nha\_cung\_cap | Cho phép đăng nhập bằng Apple |
| Facebook | Mã nhà cung cấp | NVARCHAR(255) | Liên kết với ma\_nha\_cung\_cap | Cho phép đăng nhập bằng Facebook |
| Email | Tài khoản/email | NVARCHAR | Liên kết với người dùng | Đăng nhập bằng email/mật khẩu |

Thực thể NGƯỜI DÙNG

|  |  |  |  |
| --- | --- | --- | --- |
| **Thuộc tính** | **Kiểu dữ liệu** | **Ràng buộc** | **Ý nghĩa** |
| ma\_nguoi\_dung | INT | **PK**, IDENTITY(1,1) | Mã định danh duy nhất của người dùng |
| ten\_dang\_nhap | NVARCHAR(50) | UNIQUE | Tên dùng để đăng nhập |
| email | NVARCHAR(100) | UNIQUE | Địa chỉ email của người dùng |
| ho\_ten | NVARCHAR(100) | — | Họ và tên người dùng |
| anh\_dai\_dien | NVARCHAR(255) | — | Đường dẫn ảnh đại diện |
| so\_dien\_thoai | NVARCHAR(20) | — | Số điện thoại |
| don\_vi\_tien\_te | NVARCHAR(10) | NOT NULL, DEFAULT VND | Đơn vị tiền tệ người dùng sử dụng |
| trang\_thai\_kich\_hoat | BIT | NOT NULL, DEFAULT 1 | Xác định tài khoản đang hoạt động hay không |
| lan\_dang\_nhap\_cuoi | DATETIME2 | — | Thời điểm đăng nhập gần nhất |
| ngay\_tao | DATETIME2 | NOT NULL, DEFAULT SYSDATETIME() | Thời điểm tạo tài khoản |
| ngay\_cap\_nhat | DATETIME2 | NOT NULL, DEFAULT SYSDATETIME() | Thời điểm cập nhật thông tin gần nhất |

Tìm khóa và phụ thuộc hàm và phủ tối tiểu và đạt chuẩn

Bảng 1: NGUOI\_DUNG

Khóa chính của quan hệ:

K = {ma\_nguoi\_dung}

Ta có các phụ thuộc hàm:

ma\_nguoi\_dung -> ten\_dang\_nhap

ma\_nguoi\_dung -> email

ma\_nguoi\_dung -> ho\_ten

ma\_nguoi\_dung -> anh\_dai\_dien

ma\_nguoi\_dung -> so\_dien\_thoai

ma\_nguoi\_dung -> don\_vi\_tien\_te

ma\_nguoi\_dung -> trang\_thai\_kich\_hoat

ma\_nguoi\_dung -> lan\_dang\_nhap\_cuoi

ma\_nguoi\_dung -> ngay\_tao

ma\_nguoi\_dung -> ngay\_cap\_nhat