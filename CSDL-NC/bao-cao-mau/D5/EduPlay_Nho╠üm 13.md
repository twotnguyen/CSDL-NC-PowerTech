Đề tài: EduPlay

# Mô tả đề tài

# EduPlay là một ứng dụng web hỗ trợ chuyển bộ câu hỏi trắc nghiệm thành các trò chơi tương tác. Người tạo trò chơi, thường là giáo viên, có thể thiết kế nội dung, lựa chọn hình thức chơi, lưu và quản lý các bài đã tạo. Khi muốn giao bài, giáo viên tạo phòng chơi và gửi mã cho người học. Người học nhập mã để mở trò chơi, tham gia bằng tên cá nhân hoặc tên đội tùy chế độ. Sau khi chơi, hệ thống lưu kết quả để giáo viên tra cứu trong lịch sử bài đã giao.

# Đề tài tập trung vào quy trình tạo nội dung trò chơi, chia sẻ quyền truy cập bằng mã phòng và lưu kết quả. Các trò chơi có thể chạy trực tiếp từ danh sách bài của người tạo hoặc được truy cập thông qua phòng đã giao. Hệ thống có giao diện riêng cho việc quản lý và thiết lập trò chơi, giao diện tham gia phòng và giao diện gameplay cho từng chế độ.

# Người dùng chính là người tạo trò chơi. Người này đăng ký hoặc đăng nhập, sau đó có thể tạo và quản lý các bài chơi gắn với tài khoản của mình. Các bài được phân loại theo chế độ, có thể mở lại để chỉnh sửa, chơi thử, giao cho người học hoặc xóa.

# Người tham gia thường là học sinh. Khi tham gia bài đã giao, học sinh nhập mã phòng và có thể nhập tên hiển thị trước khi bắt đầu. Tùy trò chơi, người tham gia có thể cần khai báo tên của từng người chơi hoặc tên hai đội. Luồng vào chơi bằng mã không yêu cầu học sinh đăng ký tài khoản.

# Giao diện đăng nhập có các lựa chọn đăng nhập bằng email và mật khẩu, Google hoặc Facebook. Phần dữ liệu tài khoản do hệ thống backend quản lý gồm mã người dùng, họ tên, email, thông tin mật khẩu với tài khoản thường và loại đăng nhập. Thông tin người dùng đăng nhập được lưu phía trình duyệt để duy trì trạng thái giao diện.

# Người tạo có thể tạo bài chơi mới, xem danh sách bài đã lưu, chỉnh sửa cấu hình hoặc bộ câu hỏi, và xóa bài không còn sử dụng. Danh sách bài hiển thị thông tin phù hợp với từng trò chơi, chẳng hạn số câu hỏi, thời lượng, tốc độ, kích thước lưới hoặc ảnh minh họa.

# Bộ câu hỏi trắc nghiệm được xây dựng quanh nội dung câu hỏi, các phương án trả lời và vị trí của đáp án đúng. Người tạo có thể nhập câu hỏi thủ công thông qua màn hình quản lý câu hỏi, thêm nhiều câu vào một bài và xem phần xem trước trước khi lưu. Các màn hình tạo bài có kiểm tra những dữ liệu cần thiết, ví dụ tiêu đề, nội dung câu hỏi, phương án trả lời hoặc số lượng câu tương ứng với cấu hình của trò chơi.

# Ngoài nhập thủ công, project có giao diện tạo câu hỏi bằng AI. Người tạo cung cấp môn học, khối lớp, số lượng câu, mức độ tư duy và nội dung tham khảo; hệ thống gửi yêu cầu tạo câu hỏi trắc nghiệm bốn phương án, sau đó đưa kết quả vào bộ câu hỏi để người tạo xem lại. Câu hỏi do AI tạo có thể tiếp tục được chỉnh sửa như câu hỏi thông thường trước khi lưu bài. Giao diện có lựa chọn nhập nội dung văn bản hoặc chọn tệp.

# Một số loại trò chơi cho phép thiết lập nhạc nền. Game theo lượt có danh sách nhạc có sẵn; game đua thuyền rồng có danh sách nhạc và giao diện tải nhạc riêng. Dữ liệu nhạc tải lên trong màn hình tạo game đua thuyền được lưu phía trình duyệt bằng IndexedDB để có thể sử dụng lại trên trình duyệt đó.

# Các chế độ trò chơi

# 1. Game theo lượt

# Người tạo đặt tiêu đề, chọn từ hai đến bốn người chơi, nhập tên người chơi, thiết lập số chướng ngại vật và chọn nhạc nền. Bộ câu hỏi được nhập thủ công hoặc tạo bằng AI. Trước khi lưu, hệ thống kiểm tra bài có tiêu đề, có ít nhất một câu hỏi và mỗi câu có đủ nội dung cùng các phương án trả lời.

# Trong gameplay, các nhân vật di chuyển lần lượt trên một đường chơi dạng bản đồ. Người chơi tung xúc xắc để xác định số bước di chuyển; khi gặp ô thử thách hoặc chướng ngại vật, người chơi trả lời câu hỏi để tiếp tục. Giao diện có bảng thông tin người chơi, trạng thái lượt hiện tại, xúc xắc, nhạc nền, điều khiển âm thanh và chế độ toàn màn hình. Khi có người về đích, hệ thống hiển thị kết quả và lưu kết quả của những người chơi trong lượt, gồm trạng thái thắng/thua.

# 2. Chém hoa quả

# Người tạo nhập tiêu đề bài, thiết lập thời gian cho mỗi câu và chọn tốc độ trò chơi gồm nhanh, trung bình hoặc chậm. Bộ câu hỏi có thể được nhập thủ công hoặc hỗ trợ tạo bằng AI. Khi lưu, hệ thống kiểm tra tiêu đề, số lượng câu hỏi và nội dung/đáp án của từng câu; điểm số được phân bổ theo tổng số câu để tổng điểm quy đổi về thang điểm 10.

# Trong lúc chơi, câu hỏi được hiển thị cùng các trái cây tương ứng với phương án trả lời. Người chơi thao tác chém trái cây để lựa chọn đáp án trước khi hết thời gian. Trò chơi có bộ đếm giờ, hoạt ảnh trái cây, hiệu ứng chém, âm thanh đúng/sai và màn hình tổng kết. Kết quả gồm số câu đúng, tổng số câu và điểm quy đổi; nếu chơi thông qua phòng, kết quả được lưu gắn với phòng để người tạo có thể xem lại.

# 3. Lật mảnh ghép

# Người tạo đặt tiêu đề, nhập đáp án cần đoán, chọn ảnh từ tệp trên thiết bị hoặc sử dụng đường dẫn ảnh. Có thể cấu hình kích thước lưới từ 2×2 đến 6×6, thời gian trả lời câu hỏi, thời gian đoán ảnh và màu sắc hoặc kiểu hiển thị các mảnh. Mỗi ô cần có câu hỏi tương ứng, vì vậy số câu hỏi phải đáp ứng số ô của lưới đã chọn.

# Trong trò chơi, người chơi chọn một ô, trả lời câu hỏi trắc nghiệm để mở mảnh ảnh và theo dõi phần trăm tiến độ được cập nhật. Sau khi mở các mảnh, người chơi nhập đáp án đoán hình. Giao diện có bước xác nhận trước khi chốt đáp án và chỉ cho một lần đoán cuối; trò chơi hiển thị kết quả thắng hoặc thua, đáp án và lựa chọn chơi lại hoặc quay về. Kết quả hoàn thành được lưu theo phòng với tên người chơi và thông tin trạng thái kết quả.

# 4. Đua thuyền rồng

# Người tạo đặt tiêu đề và cấu hình thời gian đua, điểm cần đạt để thắng, thời gian đóng băng đội, tên hai đội và nhạc nền. Trò chơi có hai cách tổ chức câu hỏi: hai đội dùng chung một bộ câu hỏi hoặc mỗi đội sử dụng bộ câu hỏi riêng. Câu hỏi có thể được nhập thủ công hoặc tạo bằng AI; ở chế độ riêng, nội dung được gắn với đội tương ứng. Màn hình cấu hình cũng có lựa chọn cách điều khiển qua giao diện hoặc bàn phím.

# Trong gameplay, màn hình trình bày đường đua, vị trí thuyền, bộ câu hỏi và điểm của hai đội. Đội trả lời đúng sẽ tiến về phía đích; trò chơi có bộ đếm thời gian và có thể áp dụng hiệu ứng đóng băng cho đội theo thiết lập. Trò chơi xác định đội thắng khi đạt điều kiện chiến thắng hoặc kết thúc thời gian, đồng thời hiển thị kết quả thắng, thua hoặc hòa. Kết quả của hai đội được lưu riêng nhưng cùng gắn với một mã lượt chơi.

# Giao bài và tham gia bằng mã phòng

# Từ bài đã lưu, người tạo mở chức năng giao bài, nhập tên gợi nhớ và chọn thời hạn mã phòng. Các lựa chọn thời hạn hiện có là một, ba hoặc bảy ngày. Khi tạo thành công, hệ thống sinh mã phòng sáu chữ số và cung cấp đường dẫn tham gia để sao chép hoặc chia sẻ.

# Mỗi phòng gắn với bài chơi, người tạo, loại trò chơi, tên gợi nhớ, mã phòng, thời điểm tạo và thời hạn. Người học có thể mở trang tham gia, nhập mã bằng các ô ký tự hoặc dán toàn bộ mã. Hệ thống tra cứu phòng, kiểm tra phòng có tồn tại và còn hạn hay không, rồi chuyển người học đến đúng giao diện gameplay theo loại trò chơi.

# Phòng là cơ chế để tìm đúng bài được giao và liên kết lượt chơi với bài đó. Từng người hoặc đội có thể bắt đầu trò chơi trên giao diện của mình; trong mã nguồn hiện tại không thấy cơ chế đồng bộ một phiên chơi trực tiếp giữa nhiều thiết bị theo thời gian thực.

# Lịch sử giao bài và kết quả

# Người tạo có trang lịch sử bài đã giao, hiển thị tên gợi nhớ, tên bài, mã phòng, trạng thái thời hạn, số lượt nộp và thao tác xem chi tiết hoặc xóa phòng. Trạng thái phòng được xác định dựa trên thời điểm tạo và số ngày hiệu lực. Khi bài gốc đã bị xóa, lịch sử phòng vẫn có thể thể hiện tình trạng bài không còn tồn tại.

# Kết quả được lưu theo phòng và có thể bao gồm mã lượt chơi, tên người chơi, tên đội, loại trò chơi, nội dung kết quả, điểm số, dữ liệu bổ sung và thời điểm nộp. Trang chi tiết nhóm các bản ghi theo lượt để giáo viên có thể xem kết quả những người chơi cùng ván. Cách hiển thị phụ thuộc chế độ: game theo lượt thể hiện người thắng/thua; Chém hoa quả thể hiện số câu đúng và điểm; Lật mảnh ghép thể hiện trạng thái hoàn thành; Đua thuyền rồng thể hiện kết quả của từng đội.

# MÔ TẢ THỰC THỂ

## 1. Thực thể cơ bản / danh mục giá trị

|  |  |  |  |
| --- | --- | --- | --- |
| **STT** | **Danh mục** | **Giá trị / ý nghĩa** | **Nơi sử dụng** |
| 1 | Loại trò chơi | turnbased – Game theo lượt; quizfruit – Chém hoa quả; memory – Lật mảnh ghép; dragonboat – Đua thuyền rồng | games.game\_type, rooms.game\_type, results.game\_type |
| 2 | Hình thức đăng nhập | normal – tài khoản thường; google – đăng nhập Google; facebook – đăng nhập Facebook | users.login\_type |
| 3 | Kết quả trò chơi | WIN, LOSE, DRAW, HOAN\_THANH; riêng Chém hoa quả còn lưu kết quả dạng số câu đúng/tổng số câu, ví dụ x/y | results.result\_text |
| 4 | Dữ liệu kết quả bổ sung | Dữ liệu dạng JSON tùy loại trò chơi, ví dụ người thắng và danh sách người chơi, số câu đúng/tổng số câu hoặc trạng thái hoàn thành | results.extra\_data |
| 5 | Thời hạn phòng | Số ngày hiệu lực của mã phòng; giao diện cho chọn 1, 3 hoặc 7 ngày | rooms.expire\_day |
| 6 | Cấu hình trò chơi | Dữ liệu JSON gồm các thiết lập tùy loại game như bộ câu hỏi, đáp án, người chơi, ảnh, lưới, thời gian, tốc độ, nhạc hoặc cấu hình đội | games.game\_data |

## 2. Đối tượng sử dụng / chủ thể tương tác

|  |  |  |  |
| --- | --- | --- | --- |
| **STT** | **Chủ thể** | **Thuộc tính nhận diện tiêu biểu** | **Vai trò** |
| 1 | Người tạo trò chơi / giáo viên | Tài khoản người dùng; mã người dùng, họ tên, email và loại đăng nhập | Tạo, lưu, sửa, xóa trò chơi; tạo phòng giao bài; theo dõi các phòng và xem kết quả |
| 2 | Người tham gia cá nhân / học sinh | Tên người chơi được lưu tại results.player\_name | Nhập mã phòng, tham gia trò chơi và ghi nhận kết quả. |
| 3 | Nhóm / đội tham gia | Tên đội được lưu tại results.team\_name | Tham gia chế độ Đua thuyền rồng hoặc chơi theo đội; kết quả của đội được ghi trong bảng results. |

## 3. Thực thể nghiệp vụ

## 3.1. Người dùng

|  |  |  |  |
| --- | --- | --- | --- |
| **STT** | **Bảng / thực thể** | **Kiểu/Ràng buộc trong SQL** | **Ý nghĩa** |
| 1 | id | int, khóa chính, tự tăng, NOT NULL | Mã người dùng |
| 2 | full\_name | nvarchar(255), NULL | Họ tên hiển thị |
| 3 | email | nvarchar(255), NOT NULL, UNIQUE | Email tài khoản; không trùng |
| 4 | password | nvarchar(255), NULL | Mật khẩu tài khoản thường; có thể NULL với tài khoản đăng nhập ngoài |
| 5 | avatar | nvarchar(max), NULL | Đường dẫn hoặc dữ liệu ảnh đại diện |
| 6 | login\_type | nvarchar(50), NOT NULL | Hình thức đăng nhập, ví dụ tài khoản thường hoặc Google |

**Vai trò và quan hệ:**người dùng là chủ thể tạo trò chơi. Một người dùng có thể tạo nhiều trò chơi và nhiều phòng. Mã người dùng được tham chiếu theo logic ứng dụng qua games.user\_id và rooms.teacher\_id.

**3.2. Trò chơi**

|  |  |  |  |
| --- | --- | --- | --- |
| **STT** | **Bảng / thực thể** | **Kiểu/Ràng buộc trong SQL** | **Ý nghĩa** |
| 1 | id | int, khóa chính, tự tăng, NOT NULL | Mã trò chơi |
| 2 | user\_id | int, NULL | Mã người dùng tạo trò chơi |
| 3 | game\_type | nvarchar(50), NULL | Loại trò chơi |
| 4 | title | nvarchar(255), NULL | Tiêu đề bài chơi |
| 5 | subject | nvarchar(255), NULL | Môn học hoặc thông tin phân loại chủ đề |
| 6 | music | nvarchar(max), NULL | Nhạc nền hoặc thông tin nguồn nhạc |
| 7 | game\_data | nvarchar(max), NULL | Cấu hình trò chơi và bộ câu hỏi được lưu dưới dạng JSON |
| 8 | created\_at | datetime, NULL, mặc định getdate() | Thời điểm tạo trò chơi |

**Vai trò và quan hệ:** trò chơi là nội dung được tạo và lưu để chơi trực tiếp hoặc dùng khi giao bài. Một trò chơi có thể được tham chiếu bởi nhiều phòng qua rooms.game\_id. game\_data chứa dữ liệu khác nhau theo chế độ, chẳng hạn cấu hình số người chơi, câu hỏi/đáp án, ảnh đố và lưới, hoặc thiết lập cuộc đua.

**3.3. Phòng / Bài tập được giao**

|  |  |  |  |
| --- | --- | --- | --- |
| **STT** | **Bảng / thực thể** | **Kiểu/Ràng buộc trong SQL** | **Ý nghĩa** |
| 1 | id | int, khóa chính, tự tăng, NOT NULL | Mã phòng nội bộ |
| 2 | game\_id | int, NULL | Mã trò chơi được giao |
| 3 | teacher\_id | int, NOT NULL | Mã người dùng tạo phòng |
| 4 | game\_type | nvarchar(50), NOT NULL | Loại trò chơi trong phòng |
| 5 | assign\_name | nvarchar(255), NULL | Tên gợi nhớ của bài được giao |
| 6 | room\_code | nvarchar(20), NOT NULL, UNIQUE | Mã dùng để tìm và tham gia phòng |
| 7 | expire\_day | int, NOT NULL | Số ngày phòng có hiệu lực |
| 8 | created\_at | datetime, NOT NULL | Thời điểm tạo phòng |

**Vai trò và quan hệ:** phòng liên kết trò chơi với người tạo và cung cấp mã để người tham gia vào đúng bài. Một phòng có thể có nhiều kết quả thông qua results.room\_id. game\_id cho phép NULL, nên cấu trúc hỗ trợ giữ phòng khi trò chơi bị xóa hoặc không còn gắn với bài gốc.

**3.4.  Kết quả tham gia trò chơi**

|  |  |  |  |
| --- | --- | --- | --- |
| **STT** | **Bảng / thực thể** | **Kiểu/Ràng buộc trong SQL** | **Ý nghĩa** |
| 1 | id | int, khóa chính, tự tăng, NOT NULL | Mã bản ghi kết quả |
| 2 | room\_id | int, NOT NULL | Mã phòng mà kết quả thuộc về |
| 3 | game\_type | nvarchar(50), NOT NULL | Loại trò chơi đã tham gia |
| 4 | player\_name | nvarchar(255), NULL | Tên người chơi tham gia |
| 5 | team\_name | nvarchar(255), NULL | Tên đội chơi nếu chơi chế độ đội |
| 6 | score | float, NULL | Điểm số dành cho game Chém Hoa Quả |
| 7 | result\_text | nvarchar(255), NULL | Kết quả trò chơi |
| 8 | extra\_data | nvarchar(max), NULL | Thông tin JSON bổ sung tùy chế độ |
| 9 | match\_id | bigint, NULL | Mã dùng để nhóm các kết quả thuộc cùng 1 lượt chơi |
| 10 | submitted\_at | datetime, NULL, mặc định getdate() | Thời điểm ghi nhận kết quả |

# Vai trò và quan hệ: bảng ghi nhận lượt chơi cá nhân hoặc đội. Một phòng có thể có nhiều kết quả; match\_id được sử dụng để gom các kết quả phát sinh trong cùng một ván, ví dụ kết quả nhiều người trong game theo lượt hoặc hai đội trong cuộc đua.

# PHẦN PHỤ THUỘC HÀM

|  |  |  |  |
| --- | --- | --- | --- |
| **STT** | **Bảng** | **Khóa xác định** | **Phụ thuộc hàm** |
| 1 | users | id | id → full\_name, email, password, avatar, login\_type |
| 2 | users | email (duy nhất) | email → id, full\_name, password, avatar, login\_type |
| 3 | games | id | id → user\_id, game\_type, title, subject, music, game\_data, created\_at |
| 4 | rooms | id | id → game\_id, teacher\_id, game\_type, assign\_name, room\_code, expire\_day, created\_at |
| 5 | rooms | room\_cod (duy nhất) | room\_code → id, game\_id, teacher\_id, game\_type, assign\_name, expire\_day, created\_at |
| 6 | result | id | id → room\_id, game\_type, player\_name, team\_name, score, result\_text, extra\_data, match\_id, submitted\_at |

# Tìm phủ tối thiểu

Tập phụ thuộc hàm (F) được xác định dựa trên khóa chính và các ràng buộc UNIQUE trong cơ sở dữ liệu EduPlay. Hệ thống hiện có 4 bảng: users, games, rooms, results.

### **Bước 1: Phân rã vế phải thành các thuộc tính đơn lẻ**

Áp dụng luật phân rã (X→YZ⟹X→Y,X→Z), ta chuyển tất cả vế phải thành thuộc tính đơn:

**users:**id → full\_name
id → email
id → password
id → avatar
id → login\_type
email → id
email → full\_name
email → password
email → avatar
email → login\_type
**games:**id → user\_id
id → game\_type
id → title
id → subject
id → music
id → game\_data
id → created\_at
**rooms:**id → game\_id
id → teacher\_id
id → game\_type
id → assign\_name
id → room\_code
id → expire\_day
id → created\_at
room\_code → id
room\_code → game\_id
room\_code → teacher\_id
room\_code → game\_type
room\_code → assign\_name
room\_code → expire\_day
room\_code → created\_at
**results:**id → room\_id
id → game\_type
id → player\_name
id → team\_name
id → score
id → result\_text
id → extra\_data
id → match\_id
id → submitted\_at

### **Bước 2: Loại bỏ thuộc tính dư thừa ở vế trái**

Xét các phụ thuộc hàm trong (F), mỗi vế trái chỉ gồm một thuộc tính: id, email hoặc room\_code.

Do vế trái không có từ hai thuộc tính trở lên nên không có thuộc tính nào dư thừa ở vế trái.

### **Bước 3: Loại bỏ phụ thuộc hàm dư thừa**

### **Bảng users**

Trong bảng users có các phụ thuộc hàm:

id → email
email → id

Do có email duy nhất, email xác định được id. Mặt khác, id xác định các thuộc tính còn lại. Vì vậy, các phụ thuộc hàm sau là dư thừa:

email → full\_name
email → password
email → avatar
email → login\_type

Các phụ thuộc này có thể suy ra qua email → id và id → thuộc tính tương ứng.

Giữ lại:

email → id

Các phụ thuộc hàm có vế trái là id vẫn được giữ lại.

### **Bảng rooms**

Trong bảng rooms có các phụ thuộc hàm:

id → room\_code
room\_code → id

Do room\_code có ràng buộc duy nhất, room\_code xác định được id. Vì id xác định các thuộc tính còn lại, các phụ thuộc hàm sau là dư thừa:

room\_code → game\_id
room\_code → teacher\_id
room\_code → game\_type
room\_code → assign\_name
room\_code → expire\_day
room\_code → created\_at

Các phụ thuộc này có thể suy ra qua room\_code → id và id → thuộc tính tương ứng.

Giữ lại:

room\_code → id

Các phụ thuộc hàm có vế trái là id vẫn được giữ lại.

### **Bảng games và results**

Hai bảng games và results chỉ có khóa chính id được khai báo trong schema. Không có khóa thay thế hoặc khóa ghép nào khác được khai báo là duy nhất, nên không có phụ thuộc hàm dư thừa cần loại bỏ.

### **Kết luận tập phủ tối thiểu Fmin​**

Tập Fmin​ hoàn chỉnh gồm các phụ thuộc hàm sau:

**users:**id → full\_name
id → email
id → password
id → avatar
id → login\_type
email → id
**games:**id → user\_id
id → game\_type
id → title
id → subject
id → music
id → game\_data
id → created\_at
**rooms:**id → game\_id
id → teacher\_id
id → game\_type
id → assign\_name
id → room\_code
id → expire\_day
id → created\_at
room\_code → id
**results:**id → room\_id
id → game\_type
id → player\_name
id → team\_name
id → score
id → result\_text
id → extra\_data
id → match\_id
id → submitted\_at

# Xác định Khóa và Dạng chuẩn từng quan hệ

**Định nghĩa dạng chuẩn Boyce-Codd (BCNF):** Một lược đồ quan hệ R đạt chuẩn BCNF khi và chỉ khi với mọi phụ thuộc hàm không tầm thường X→Y đúng trên R, X bắt buộc phải là một **siêu khóa (superkey)** của R.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| STT | Tên bảng / Quan hệ | Tập khóa ứng viên (Candidate Keys) | Phân tích điều kiện chuẩn hóa | Dạng chuẩn |
| 1 | users | {id}, {email} | id là khóa chính; email có ràng buộc duy nhất và không NULL. Các vế trái của phụ thuộc hàm từ các khóa này đều là siêu khóa. | BCNF |
| 2 | games | {id} | id là khóa chính. Vế trái của mọi phụ thuộc hàm không tầm thường là siêu khóa. | BCNF |
| 3 | rooms | {id}, {room\_code} | id là khóa chính; room\_code có ràng buộc duy nhất và không NULL. Cả hai đều xác định các thuộc tính còn lại. | BCNF |
| 4 | results | {id} | id là khóa chính. Vế trái của mọi phụ thuộc hàm không tầm thường là siêu khóa. | BCNF |

# Suy ra Dạng chuẩn của cả Lược đồ Cơ sở dữ liệu

Dựa vào các phụ thuộc hàm đã xác định, các vế trái của những phụ thuộc hàm không tầm thường đều là khóa của quan hệ tương ứng. Cụ thể, users có khóa id và email; rooms có khóa id và room\_code; games và results có khóa id. Do đó, các quan hệ đều thỏa mãn dạng chuẩn Boyce–Codd (BCNF).

Vì toàn bộ các quan hệ thành phần đều đạt BCNF nên lược đồ cơ sở dữ liệu EduPlay cũng đạt BCNF. Suy ra, lược đồ đồng thời thỏa mãn các dạng chuẩn thấp hơn là 3NF, 2NF và 1NF.