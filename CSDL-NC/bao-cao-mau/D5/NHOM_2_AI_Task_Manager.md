**Thành Viên Nhóm:**

1. Võ Hồng Sơn MSSV: 238060192 Lớp: 23DTHD5
2. Huỳnh Văn Nhật Hoàng MSSV: 2380600713 Lớp: 23DTHD5
3. Lê Hồng Sơn MSSV: 2380601916 Lớp: 23DTHD5
4. **Mô tả đề tài:**

Đề tài “Hệ thống quản lý công việc thông minh (AI Task Manager)” là một hệ thống hỗ trợ người dùng quản lý công việc cá nhân và công việc theo dự án trên nền tảng web. Hệ thống được xây dựng nhằm giúp người dùng theo dõi các công việc cần thực hiện, quản lý tiến độ, tổ chức công việc theo dự án và phối hợp với những thành viên khác trong quá trình làm việc. Bên cạnh các chức năng quản lý công việc truyền thống, hệ thống còn tích hợp các chức năng AI nhằm hỗ trợ người dùng trong việc phân tích và quản lý công việc một cách thông minh hơn.

Mỗi người dùng có một tài khoản riêng để đăng nhập và sử dụng hệ thống. Sau khi đăng nhập, người dùng có thể quản lý thông tin cá nhân của mình, đồng thời tạo và theo dõi các công việc cần thực hiện. Mỗi công việc có các thông tin cơ bản như tiêu đề, mô tả, trạng thái, mức độ ưu tiên, thời hạn hoàn thành và thời gian tạo. Người dùng có thể cập nhật trạng thái công việc, đánh dấu công việc đã hoàn thành và theo dõi những công việc đang thực hiện hoặc đã quá hạn. Các công việc cá nhân cũng có thể được gắn với một dự án cụ thể nếu người dùng muốn quản lý chúng trong phạm vi của một dự án.

Ngoài việc quản lý công việc cá nhân, hệ thống cho phép người dùng tạo và quản lý các dự án. Người tạo dự án được xác định là chủ sở hữu của dự án và có các quyền quản lý dự án theo chức năng của hệ thống. Một dự án có thể có nhiều thành viên tham gia và một người dùng cũng có thể tham gia nhiều dự án khác nhau. Do đó, hệ thống quản lý thông tin thành viên dự án thông qua bảng thành viên, qua đó xác định người dùng nào đang tham gia dự án nào.

Trong mỗi dự án, chủ dự án có quyền khởi tạo các hạng mục công việc trong phạm vi dự án phụ trách. Các thành viên tham gia có thể đăng ký thực hiện từng công việc cụ thể. Thông tin về thời gian nhận, trạng thái xử lý và thời gian hoàn thành đều được hệ thống ghi nhận, giúp các thành viên nắm bắt tiến độ chung của dự án.

Để hỗ trợ việc hình thành nhóm làm việc, hệ thống cung cấp chức năng mời người dùng tham gia dự án. Chủ một dự án có thể gửi lời mời đến một người dùng khác để họ tham gia dự án của mình. Lời mời được lưu trữ cùng với thông tin về dự án, người gửi và trạng thái của lời mời. Người được mời có thể thực hiện các thao tác như xác nhận hoặc từ chối lời mời.

Trong mỗi dự án, các thành viên cũng có thể trao đổi thông tin với nhau thông qua chức năng nhắn tin. Tin nhắn được gắn với người gửi và dự án tương ứng, hỗ trợ việc trao đổi về công việc, tiến độ và những vấn đề liên quan đến dự án.

Bên cạnh đó, hệ thống cũng ghi nhận lịch sử hoạt động trong quá trình sử dụng. Đối với dự án, lịch sử phản ánh các hoạt động của thành viên và những thay đổi liên quan; đối với công việc cá nhân, hệ thống cũng lưu lại quá trình xử lý và các hoạt động liên quan.

Một điểm đặc trưng của hệ thống là khả năng hỗ trợ quản lý công việc bằng AI. Dựa trên dữ liệu công việc và các thông tin liên quan, hệ thống có thể sử dụng các thành phần AI để phân tích nội dung công việc, hỗ trợ xác định mức độ ưu tiên, nhận diện ý định hoặc đưa ra những hỗ trợ phù hợp cho người dùng trong quá trình quản lý công việc. AI đóng vai trò là thành phần hỗ trợ, giúp người dùng có thêm thông tin để tổ chức và xử lý công việc hiệu quả hơn, thay vì thay thế hoàn toàn việc ra quyết định của người dùng.

Nhìn tổng thể, hệ thống bao gồm các nhóm nghiệp vụ chính: quản lý người dùng, quản lý công việc, quản lý dự án, quản lý thành viên dự án, quản lý công việc trong dự án, quản lý lời mời tham gia dự án, trao đổi thông tin trong dự án và theo dõi hoạt động của hệ thống. Các nhóm nghiệp vụ này được liên kết với nhau thông qua các quan hệ giữa người dùng, công việc và dự án, tạo thành cơ sở dữ liệu phục vụ cho toàn bộ hệ thống AI Task Manager.

1. **Xác định 3 loại thực thể:**
2. ***Thực thể Cơ Bản:***

**-AspNetUser:**

|  |  |  |  |
| --- | --- | --- | --- |
| Thuộc tính | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
| Id | nvarchar(450) | PK | Mã người dùng |
| FullName | nvarchar(max) | NULL | Họ và tên |
| UserName | nvarchar(256) | NULL | Tên đăng nhập |
| Email | nvarchar(256) | NULL | Địa chỉ email |
| PhoneNumber | nvarchar(max) | NULL | Số điện thoại |

**-TaskItems:**

|  |  |  |  |
| --- | --- | --- | --- |
| Thuộc tính | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
| Id | int | PK | Mã công việc |
| Title | nvarchar(200) | NOT NULL | Tiêu đề công việc |
| Description | nvarchar(1000) | NULL | Mô tả công việc |
| Status | int | NOT NULL | Trạng thái công việc |
| Priority | int | NOT NULL | Mức độ ưu tiên |
| Deadline | datetime2 | NULL | Thời hạn hoàn thành |
| CreatedAt | datetime2 | NOT NULL | Thời điểm tạo công việc |
| UpdatedAt | datetime2 | NULL | Thời điểm cập nhật |
| CompletedAt | datetime2 | NULL | Thời điểm hoàn thành |
| UserId | nvarchar(450) | NULL, FK | Người sở hữu công việc |
| ProjectId | int | NULL, FK | Dự án liên quan |
| AiReason | nvarchar(500) | NULL | Lý do AI đề xuất mức ưu tiên |
| PriorityScore | float | NULL | Điểm ưu tiên do AI tính toán |

**-Project:**

|  |  |  |  |
| --- | --- | --- | --- |
| Thuộc tính | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
| Id | int | PK | Mã dự án |
| Name | nvarchar(200) | NOT NULL | Tên dự án |
| Description | nvarchar(1000) | NULL | Mô tả dự án |
| OwnerId | nvarchar(450) | NOT NULL, FK | Người sở hữu dự án |
| CreatedAt | datetime2 | NOT NULL | Thời điểm tạo dự án |
| EndDate | datetime2 | NULL | Ngày kết thúc dự án |
| Goal | nvarchar(max) | NULL | Mục tiêu của dự án |
| ProjectType | nvarchar(max) | NOT NULL | Loại dự án |
| StartDate | datetime2 | NULL | Ngày bắt đầu dự án |
| Status | int | NOT NULL | Trạng thái dự án |
| AISummary | nvarchar(max) | NULL | Nội dung tóm tắt do AI hỗ trợ |

1. ***Thực thể Nghiệp Vụ:***

**-ProjectMember:**

|  |  |  |  |
| --- | --- | --- | --- |
| Thuộc tính | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
| Id | int | PK | Mã bản ghi thành viên |
| ProjectId | int | NOT NULL, FK | Dự án |
| UserId | nvarchar(450) | NOT NULL, FK | Người dùng |
| Role | int | NOT NULL | Vai trò của người dùng trong dự án |

**-ProjectTask:**

|  |  |  |  |
| --- | --- | --- | --- |
| Thuộc tính | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
| Id | int | PK | Mã công việc |
| Title | nvarchar(max) | NOT NULL | Tiêu đề công việc |
| Description | nvarchar(max) | NULL | Mô tả công việc |
| Status | int | NOT NULL | Trạng thái công việc |
| Priority | int | NOT NULL | Mức độ ưu tiên |
| Deadline | datetime2 | NULL | Thời hạn hoàn thành |
| CreatedAt | datetime2 | NOT NULL | Thời điểm tạo |
| UpdatedAt | datetime2 | NULL | Thời điểm cập nhật |
| ProjectId | int | NOT NULL, FK | Dự án chứa công việc |
| AssignedToUserId | nvarchar(450) | NULL, FK | Người đăng ký thực hiện công việc |
| AIReason | nvarchar(max) | NULL | Lý do AI đề xuất |
| AIScore | float | NULL | Điểm đánh giá do AI tính toán |
| DependsOnTaskId | int | NULL | Mã công việc mà công việc này phụ thuộc |

**-ActivityLogs:**

|  |  |  |  |
| --- | --- | --- | --- |
| Thuộc tính | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
| Id | int | PK | Mã lịch sử hoạt động |
| ProjectId | int | NULL, FK | Dự án liên quan |
| UserId | nvarchar(450) | NOT NULL, FK | Người thực hiện hoạt động |
| Action | nvarchar(max) | NOT NULL | Nội dung hành động |
| TaskTitle | nvarchar(max) | NULL | Tên công việc liên quan |
| CreatedAt | datetime2 | NOT NULL | Thời điểm hoạt động xảy ra |

**-ProjectInvitations:**

|  |  |  |  |
| --- | --- | --- | --- |
| Thuộc tính | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
| Id | int | PK | Mã lời mời |
| ProjectId | int | NOT NULL, FK | Dự án được mời tham gia |
| InvitedUserId | nvarchar(450) | NOT NULL, FK | Người được mời |
| InvitedByUserId | nvarchar(450) | NOT NULL, FK | Người gửi lời mời |
| CreatedAt | datetime2 | NOT NULL | Thời điểm gửi lời mời |
| IsAccepted | bit | NOT NULL | Trạng thái đã chấp nhận |
| IsRejected | bit | NOT NULL | Trạng thái đã từ chối |

**-ProjectMessages:**

|  |  |  |  |
| --- | --- | --- | --- |
| Thuộc tính | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
| Id | int | PK | Mã tin nhắn |
| ProjectId | int | NOT NULL | Dự án chứa tin nhắn |
| UserId | nvarchar(450) | NOT NULL, FK | Người gửi tin nhắn |
| Message | nvarchar(max) | NOT NULL | Nội dung tin nhắn |
| CreatedAt | datetime2 | NOT NULL | Thời điểm gửi tin nhắn |

1. ***Thực thể Ngoài:***

**-AiLearningRecords:**

|  |  |  |  |
| --- | --- | --- | --- |
| Thuộc tính | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
| Id | int | PK | Mã bản ghi học AI |
| Text | nvarchar(max) | NOT NULL | Nội dung dữ liệu được AI xử lý |
| Score | float | NULL | Điểm đánh giá của AI |
| Priority | nvarchar(max) | NOT NULL | Mức độ ưu tiên do AI xác định |
| Reason | nvarchar(max) | NULL | Lý do AI đưa ra kết quả |
| Corrected | bit | NOT NULL | Cho biết kết quả AI đã được điều chỉnh hay chưa |
| CreatedAt | datetime2 | NOT NULL | Thời điểm tạo bản ghi |

**- AiTrainingData:**

|  |  |  |  |
| --- | --- | --- | --- |
| Thuộc tính | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
| Id | int | PK | Mã dữ liệu huấn luyện |
| InputText | nvarchar(max) | NULL | Dữ liệu đầu vào dùng để huấn luyện AI |
| Intent | nvarchar(100) | NULL | Ý định được xác định từ dữ liệu đầu vào |

**III. Tìm Khóa, Dạng Chuẩn, Phủ Tối Thiểu**

**-Bảng 1: AspNetUser**

|  |  |  |  |
| --- | --- | --- | --- |
| Thuộc tính | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
| Id | nvarchar(450) | PK | Mã người dùng |
| FullName | nvarchar(max) | NULL | Họ và tên |
| UserName | nvarchar(256) | NULL | Tên đăng nhập |
| Email | nvarchar(256) | NULL | Địa chỉ email |
| PhoneNumber | nvarchar(max) | NULL | Số điện thoại |

***1. Xác định khóa***

Khóa ứng viên: K = {Id}

Vì: Id+ = {Id, FullName, UserName, Email, PhoneNumber, ProfilePicture}

=>Do đó Id là khóa của quan hệ.

1. ***Xác định dạng chuẩn***

Khóa của quan hệ là: K = {Id}

Các thuộc tính không khóa: FullName, UserName, Email, PhoneNumber, ProfilePicture

**1NF**: Đạt 1NF vì các thuộc tính đều chứa giá trị đơn, không có thuộc tính đa trị hay nhóm lặp.

**2NF**: Đạt 2NF vì khóa Id chỉ gồm một thuộc tính nên không thể xảy ra phụ thuộc bộ phận. (Khóa chỉ có 1 tt nên luôn đạt DC2)

**3NF**: Đạt 3NF vì với mọi phụ thuộc hàm Id -> A, vế trái Id là siêu khóa.

**BCNF**: Đạt BCNF vì với mọi phụ thuộc hàm không tầm thường X -> Y, X là siêu khóa. Ở đây các phụ thuộc hàm đều có vế trái là Id, mà Id là khóa.

Kết luận:

**AspNetUsers đạt BCNF.**

***3. Tìm Phủ Tối Thiểu***

F = {

Id -> FullName,

Id -> UserName,

Id -> Email,

Id -> PhoneNumber,

Id -> ProfilePicture

}

**Bước 1**: Phân rã vế phải

Vế trái của các phụ thuộc hàm chỉ chứa 1 thuộc tính đơn nên không cần phân rã vế trái.

**Bước 2**: Loại bỏ thuộc tính dư thừa ở vế trái

Vế trái của tất cả các phụ thuộc hàm chỉ chứa 1 thuộc tính, nên không có thuộc tính dư thừa ở vế trái để loại bỏ.

**Bước 3**: Loại bỏ phụ thuộc hàm dư thừa

Lần lượt che từng phụ thuộc hàm và kiểm tra xem có thể suy ra phụ thuộc hàm đó từ các phụ thuộc hàm còn lại hay không.

***(=>Vì mỗi Vế Trái thuộc tính chỉ xuất hiện một lần nên chắc chắn sẽ ko dư thừa)***

**+Xét Id -> FullName: (Loại Id -> FullName ra khỏi F)**

Tính bao đóng:

Id+ = {Id, UserName, Email, PhoneNumber, ProfilePicture}

Không suy ra được FullName.

→ Id -> FullName không dư thừa.

**+Xét Id -> UserName: (Loại Id -> UserName ra khỏi F)**

Tính bao đóng:

Id+ = {Id, FullName, Email, PhoneNumber, ProfilePicture}

Không suy ra được UserName.

→ Id -> UserName không dư thừa.

**+Xét Id -> Email: (Loại Id -> Email ra khỏi F)**

Tính bao đóng:

Id+ = {Id, FullName, UserName, PhoneNumber, ProfilePicture}

Không suy ra được Email.

→ Id -> Email không dư thừa.

**+Xét Id -> PhoneNumber: (Loại Id -> PhoneNumber ra khỏi F)**

Tính bao đóng:

Id+ = {Id, FullName, UserName, Email, ProfilePicture}

Không suy ra được PhoneNumber.

→ Id -> PhoneNumber không dư thừa.

**Xét Id -> ProfilePicture: (Loại Id -> ProfilePicture ra khỏi F)**

Tính bao đóng:

Id+ = {Id, FullName, UserName, Email, PhoneNumber}

Không suy ra được ProfilePicture.

→ Id -> ProfilePicture không dư thừa.

Kết luận phủ tối thiểu:

Không có phụ thuộc hàm nào dư thừa.

Fmin = {

Id -> FullName

Id -> UserName

Id -> Email

Id -> PhoneNumber

Id -> ProfilePicture

}

**-Bảng 2: TaskItems**

|  |  |  |  |
| --- | --- | --- | --- |
| Thuộc tính | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
| Id | int | PK | Mã công việc |
| Title | nvarchar(200) | NOT NULL | Tiêu đề công việc |
| Description | nvarchar(1000) | NULL | Mô tả công việc |
| Status | int | NOT NULL | Trạng thái công việc |
| Priority | int | NOT NULL | Mức độ ưu tiên |
| Deadline | datetime2 | NULL | Thời hạn hoàn thành |
| CreatedAt | datetime2 | NOT NULL | Thời điểm tạo công việc |
| UpdatedAt | datetime2 | NULL | Thời điểm cập nhật |
| CompletedAt | datetime2 | NULL | Thời điểm hoàn thành |
| UserId | nvarchar(450) | NULL, FK | Người sở hữu công việc |
| ProjectId | int | NULL, FK | Dự án liên quan |
| AiReason | nvarchar(500) | NULL | Lý do AI đề xuất mức ưu tiên |
| PriorityScore | float | NULL | Điểm ưu tiên do AI tính toán |

***1. Xác định khóa***

Khóa ứng viên: K = {Id}

Vì: Id+ = {Id, Title, Description, Status, Priority, Deadline, CreatedAt, UpdatedAt, CompletedAt, UserId, ProjectId, AiReason, PriorityScore}

→ Do đó Id là khóa của quan hệ.

**=>Các thuộc tính UserId, ProjectId không phải khóa vì**:

Một UserId có thể sở hữu nhiều công việc.

Một ProjectId có thể liên quan đến nhiều công việc.

***2. Xác định dạng chuẩn***

Khóa của quan hệ là: K = {Id}

Các thuộc tính không khóa:

Title, Description, Status, Priority, Deadline, CreatedAt, UpdatedAt, CompletedAt, UserId, ProjectId, AiReason, PriorityScore

**1NF**: Đạt 1NF vì các thuộc tính đều chứa giá trị đơn, không có thuộc tính đa trị hay nhóm lặp.

**2NF**: Đạt 2NF vì khóa Id chỉ gồm một thuộc tính nên không thể xảy ra phụ thuộc bộ phận. (Khóa chỉ có 1 thuộc tính nên luôn đạt DC2)

**3NF**: Đạt 3NF vì với mọi phụ thuộc hàm Id -> A, vế trái Id là siêu khóa.

**BCNF**: Đạt BCNF vì với mọi phụ thuộc hàm không tầm thường X -> Y, X là siêu khóa. Ở đây các phụ thuộc hàm đều có vế trái là Id, mà Id là khóa.

Kết luận:

**TaskItems đạt BCNF**.

***3. Tìm Phủ Tối Thiểu***

**Bước 1**: Phân rã vế phải

Vế trái của các phụ thuộc hàm chỉ chứa 1 thuộc tính đơn nên không cần phân rã vế trái.

**Bước 2**: Loại bỏ thuộc tính dư thừa ở vế trái

Vế trái của tất cả các phụ thuộc hàm chỉ chứa 1 thuộc tính, nên không có thuộc tính dư thừa ở vế trái để loại bỏ.

**Bước 3**: Loại bỏ phụ thuộc hàm dư thừa

Lần lượt che từng phụ thuộc hàm và kiểm tra xem có thể suy ra phụ thuộc hàm đó từ các phụ thuộc hàm còn lại hay không.

***(=>Vì mỗi Vế Trái thuộc tính chỉ xuất hiện một lần nên chắc chắn sẽ ko dư thừa)***

**+ Xét Id -> Title: (Loại Id -> Title ra khỏi F)**

Tính bao đóng:

Id+ = {Id, Description, Status, Priority, Deadline, CreatedAt, UpdatedAt, CompletedAt, UserId, ProjectId, AiReason, PriorityScore}

Không suy ra được Title.

→ Id -> Title không dư thừa.

**+ Xét Id -> Description: (Loại Id -> Description ra khỏi F)**

Tính bao đóng:

Id+ = {Id, Title, Status, Priority, Deadline, CreatedAt, UpdatedAt, CompletedAt, UserId, ProjectId, AiReason, PriorityScore}

Không suy ra được Description.

→ Id -> Description không dư thừa.

**+ Xét Id -> Status: (Loại Id -> Status ra khỏi F)**

Tính bao đóng:

Id+ = {Id, Title, Description, Priority, Deadline, CreatedAt, UpdatedAt, CompletedAt, UserId, ProjectId, AiReason, PriorityScore}

Không suy ra được Status.

→ Id -> Status không dư thừa.

**+ Xét Id -> Priority: (Loại Id -> Priority ra khỏi F)**

Tính bao đóng:

Id+ = {Id, Title, Description, Status, Deadline, CreatedAt, UpdatedAt, CompletedAt, UserId, ProjectId, AiReason, PriorityScore}

Không suy ra được Priority.

→ Id -> Priority không dư thừa.

**+ Xét Id -> Deadline: (Loại Id -> Deadline ra khỏi F)**

Tính bao đóng:

Id+ = {Id, Title, Description, Status, Priority, CreatedAt, UpdatedAt, CompletedAt, UserId, ProjectId, AiReason, PriorityScore}

Không suy ra được Deadline.

→ Id -> Deadline không dư thừa.

**+ Xét Id -> CreatedAt: (Loại Id -> CreatedAt ra khỏi F)**

Tính bao đóng:

Id+ = {Id, Title, Description, Status, Priority, Deadline, UpdatedAt, CompletedAt, UserId, ProjectId, AiReason, PriorityScore}

Không suy ra được CreatedAt.

→ Id -> CreatedAt không dư thừa.

**+ Xét Id -> UpdatedAt: (Loại Id -> UpdatedAt ra khỏi F)**

Tính bao đóng:

Id+ = {Id, Title, Description, Status, Priority, Deadline, CreatedAt, CompletedAt, UserId, ProjectId, AiReason, PriorityScore}

Không suy ra được UpdatedAt.

→ Id -> UpdatedAt không dư thừa.

**+ Xét Id -> CompletedAt: (Loại Id -> CompletedAt ra khỏi F)**

Tính bao đóng:

Id+ = {Id, Title, Description, Status, Priority, Deadline, CreatedAt, UpdatedAt, UserId, ProjectId, AiReason, PriorityScore}

Không suy ra được CompletedAt.

→ Id -> CompletedAt không dư thừa.

**+ Xét Id -> UserId: (Loại Id -> UserId ra khỏi F)**

Tính bao đóng:

Id+ = {Id, Title, Description, Status, Priority, Deadline, CreatedAt, UpdatedAt, CompletedAt, ProjectId, AiReason, PriorityScore}

Không suy ra được UserId.

→ Id -> UserId không dư thừa.

**+ Xét Id -> ProjectId: (Loại Id -> ProjectId ra khỏi F)**

Tính bao đóng:

Id+ = {Id, Title, Description, Status, Priority, Deadline, CreatedAt, UpdatedAt, CompletedAt, UserId, AiReason, PriorityScore}

Không suy ra được ProjectId.

→ Id -> ProjectId không dư thừa.

**+ Xét Id -> AiReason: (Loại Id -> AiReason ra khỏi F)**

Tính bao đóng:

Id+ = {Id, Title, Description, Status, Priority, Deadline, CreatedAt, UpdatedAt, CompletedAt, UserId, ProjectId, PriorityScore}

Không suy ra được AiReason.

→ Id -> AiReason không dư thừa.

**+ Xét Id -> PriorityScore: (Loại Id -> PriorityScore ra khỏi F)**

Tính bao đóng:

Id+ = {Id, Title, Description, Status, Priority, Deadline, CreatedAt, UpdatedAt, CompletedAt, UserId, ProjectId, AiReason}

Không suy ra được PriorityScore.

→ Id -> PriorityScore không dư thừa.

Kết luận phủ tối thiểu:

Không có phụ thuộc hàm nào dư thừa.

Fmin = {

Id -> Title

Id -> Description

Id -> Status

Id -> Priority

Id -> Deadline

Id -> CreatedAt

Id -> UpdatedAt

Id -> CompletedAt

Id -> UserId

Id -> ProjectId

Id -> AiReason

Id -> PriorityScore

}

**-Bảng 3: Project**

|  |  |  |  |
| --- | --- | --- | --- |
| Thuộc tính | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
| Id | int | PK | Mã dự án |
| Name | nvarchar(200) | NOT NULL | Tên dự án |
| Description | nvarchar(1000) | NULL | Mô tả dự án |
| OwnerId | nvarchar(450) | NOT NULL, FK | Người sở hữu dự án |
| CreatedAt | datetime2 | NOT NULL | Thời điểm tạo dự án |
| EndDate | datetime2 | NULL | Ngày kết thúc dự án |
| Goal | nvarchar(max) | NULL | Mục tiêu của dự án |
| ProjectType | nvarchar(max) | NOT NULL | Loại dự án |
| StartDate | datetime2 | NULL | Ngày bắt đầu dự án |
| Status | int | NOT NULL | Trạng thái dự án |
| AISummary | nvarchar(max) | NULL | Nội dung tóm tắt do AI hỗ trợ |

***1. Xác định khóa***

Khóa ứng viên: K = {Id}

Vì: Id+ = {Id, ProjectId, UserId, Role}

→ Do đó Id là khóa của quan hệ.

**=>Các thuộc tính UserId, ProjectId không phải khóa vì**:

ProjectId không phải khóa vì một dự án có nhiều thành viên.

UserId không phải khóa vì một người có thể tham gia nhiều dự án.

***2. Xác định dạng chuẩn***

Khóa của quan hệ là: K = {Id}

Các thuộc tính không khóa: ProjectId, UserId, Role

**1NF**: Đạt 1NF vì các thuộc tính đều chứa giá trị đơn, không có thuộc tính đa trị hay nhóm lặp.

**2NF**: Đạt 2NF vì khóa Id chỉ gồm một thuộc tính nên không thể xảy ra phụ thuộc bộ phận. (Khóa chỉ có 1 thuộc tính nên luôn đạt DC2)

**3NF**: Đạt 3NF vì với mọi phụ thuộc hàm Id -> A, vế trái Id là siêu khóa.

**BCNF**: Đạt BCNF vì với mọi phụ thuộc hàm không tầm thường X -> Y, X là siêu khóa. Ở đây các phụ thuộc hàm đều có vế trái là Id, mà Id là khóa.

Kết luận:

**ProjectMembers đạt BCNF.**

***3. Tìm Phủ Tối Thiểu***

**Bước 1**: Phân rã vế phải

Vế trái của các phụ thuộc hàm chỉ chứa 1 thuộc tính đơn nên không cần phân rã vế trái.

**Bước 2**: Loại bỏ thuộc tính dư thừa ở vế trái

Vế trái của tất cả các phụ thuộc hàm chỉ chứa 1 thuộc tính, nên không có thuộc tính dư thừa ở vế trái để loại bỏ.

**Bước 3**: Loại bỏ phụ thuộc hàm dư thừa

Lần lượt che từng phụ thuộc hàm và kiểm tra xem có thể suy ra phụ thuộc hàm đó từ các phụ thuộc hàm còn lại hay không.

***(=>Vì mỗi Vế Trái thuộc tính chỉ xuất hiện một lần nên chắc chắn sẽ ko dư thừa)***

**+ Xét Id -> ProjectId: (Loại Id -> ProjectId ra khỏi F)**

Tính bao đóng:

Id+ = {Id, UserId, Role}

Không suy ra được ProjectId.

→ Id -> ProjectId không dư thừa.

**+ Xét Id -> UserId: (Loại Id -> UserId ra khỏi F)**

Tính bao đóng:

Id+ = {Id, ProjectId, Role}

Không suy ra được UserId.

→ Id -> UserId không dư thừa.

**+ Xét Id -> Role: (Loại Id -> Role ra khỏi F)**

Tính bao đóng:

Id+ = {Id, ProjectId, UserId}

Không suy ra được Role.

→ Id -> Role không dư thừa.

Kết luận phủ tối thiểu:

Không có phụ thuộc hàm nào dư thừa.

Fmin = {

Id -> ProjectId

Id -> UserId

Id -> Role

}

**-Bảng 4: ProjectMember**

|  |  |  |  |
| --- | --- | --- | --- |
| Thuộc tính | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
| Id | int | PK | Mã bản ghi thành viên |
| ProjectId | int | NOT NULL, FK | Dự án |
| UserId | nvarchar(450) | NOT NULL, FK | Người dùng |
| Role | int | NOT NULL | Vai trò của người dùng trong dự án |

***1. Xác định khóa***

Khóa ứng viên: K = {Id}

Vì: Id+ = {Id, ProjectId, UserId, Role}

→ Do đó Id là khóa của quan hệ.

**=> Các thuộc tính UserId, ProjectId không phải khóa vì:**

ProjectId không phải khóa vì một dự án có nhiều thành viên.

UserId không phải khóa vì một người có thể tham gia nhiều dự án.

***2. Xác định dạng chuẩn***

Khóa của quan hệ là: K = {Id}

Các thuộc tính không khóa: ProjectId, UserId, Role

**1NF**: Đạt 1NF vì các thuộc tính đều chứa giá trị đơn, không có thuộc tính đa trị hay nhóm lặp.

**2NF**: Đạt 2NF vì khóa Id chỉ gồm một thuộc tính nên không thể xảy ra phụ thuộc bộ phận. (Khóa chỉ có 1 thuộc tính nên luôn đạt DC2)

**3NF**: Đạt 3NF vì với mọi phụ thuộc hàm Id -> A, vế trái Id là siêu khóa.

**BCNF**: Đạt BCNF vì với mọi phụ thuộc hàm không tầm thường X -> Y, X là siêu khóa. Ở đây các phụ thuộc hàm đều có vế trái là Id, mà Id là khóa.

Kết luận:

**ProjectMembers đạt BCNF.**

1. **Tìm Phủ Tối Thiểu**

**Bước 1**: Phân rã vế phải

Vế trái của các phụ thuộc hàm chỉ chứa 1 thuộc tính đơn nên không cần phân rã vế trái.

**Bước 2**: Loại bỏ thuộc tính dư thừa ở vế trái

Vế trái của tất cả các phụ thuộc hàm chỉ chứa 1 thuộc tính, nên không có thuộc tính dư thừa ở vế trái để loại bỏ.

**Bước 3**: Loại bỏ phụ thuộc hàm dư thừa

Lần lượt che từng phụ thuộc hàm và kiểm tra xem có thể suy ra phụ thuộc hàm đó từ các phụ thuộc hàm còn lại hay không.

**(=> Vì mỗi Vế Trái thuộc tính chỉ xuất hiện một lần nên chắc chắn sẽ không dư thừa)**

**+ Xét Id -> ProjectId: (Loại Id -> ProjectId ra khỏi F)**

Tính bao đóng:

Id+ = {Id, UserId, Role}

Không suy ra được ProjectId.

→ Id -> ProjectId không dư thừa.

**+ Xét Id -> UserId: (Loại Id -> UserId ra khỏi F)**

Tính bao đóng:

Id+ = {Id, ProjectId, Role}

Không suy ra được UserId.

→ Id -> UserId không dư thừa.

**+ Xét Id -> Role: (Loại Id -> Role ra khỏi F)**

Tính bao đóng:

Id+ = {Id, ProjectId, UserId}

Không suy ra được Role.

→ Id -> Role không dư thừa.

Kết luận phủ tối thiểu:

Không có phụ thuộc hàm nào dư thừa.

Fmin = {

Id -> ProjectId

Id -> UserId

Id -> Role

}

**-Bảng 5: ProjectTask**

|  |  |  |  |
| --- | --- | --- | --- |
| Thuộc tính | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
| Id | int | PK | Mã công việc |
| Title | nvarchar(max) | NOT NULL | Tiêu đề công việc |
| Description | nvarchar(max) | NULL | Mô tả công việc |
| Status | int | NOT NULL | Trạng thái công việc |
| Priority | int | NOT NULL | Mức độ ưu tiên |
| Deadline | datetime2 | NULL | Thời hạn hoàn thành |
| CreatedAt | datetime2 | NOT NULL | Thời điểm tạo |
| UpdatedAt | datetime2 | NULL | Thời điểm cập nhật |
| ProjectId | int | NOT NULL, FK | Dự án chứa công việc |
| AssignedToUserId | nvarchar(450) | NULL, FK | Người đăng ký thực hiện công việc |
| AIReason | nvarchar(max) | NULL | Lý do AI đề xuất |
| AIScore | float | NULL | Điểm đánh giá do AI tính toán |

***1. Xác định khóa***

Khóa ứng viên: K = {Id}

Vì: Id+ = {Id, Title, Description, Status, Priority, Deadline, CreatedAt, UpdatedAt, ProjectId, AssignedToUserId, AIReason, AIScore}

→ Do đó Id là khóa của quan hệ.

**=> Các thuộc tính ProjectId, AssignedToUserId, không phải khóa vì:**

ProjectId không phải khóa vì một dự án có nhiều công việc.

AssignedToUserId không phải khóa vì một người có thể đăng ký thực hiện nhiều công việc.

***2. Xác định dạng chuẩn***

Khóa của quan hệ là: K = {Id}

Các thuộc tính không khóa: Title, Description, Status, Priority, Deadline, CreatedAt, UpdatedAt, ProjectId, AssignedToUserId, AIReason, AIScore

**1NF**: Đạt 1NF vì các thuộc tính đều chứa giá trị đơn, không có thuộc tính đa trị hay nhóm lặp.

**2NF**: Đạt 2NF vì khóa Id chỉ gồm một thuộc tính nên không thể xảy ra phụ thuộc bộ phận. (Khóa chỉ có 1 thuộc tính nên luôn đạt DC2)

**3NF**: Đạt 3NF vì với mọi phụ thuộc hàm Id -> A, vế trái Id là siêu khóa.

**BCNF**: Đạt BCNF vì với mọi phụ thuộc hàm không tầm thường X -> Y, X là siêu khóa. Ở đây các phụ thuộc hàm đều có vế trái là Id, mà Id là khóa.

Kết luận:

**ProjectTasks đạt BCNF.**

***3. Tìm Phủ Tối Thiểu***

**Bước 1**: Phân rã vế phải

Vế trái của các phụ thuộc hàm chỉ chứa 1 thuộc tính đơn nên không cần phân rã vế trái.

**Bước 2**: Loại bỏ thuộc tính dư thừa ở vế trái

Vế trái của tất cả các phụ thuộc hàm chỉ chứa 1 thuộc tính, nên không có thuộc tính dư thừa ở vế trái để loại bỏ.

**Bước 3**: Loại bỏ phụ thuộc hàm dư thừa

Lần lượt che từng phụ thuộc hàm và kiểm tra xem có thể suy ra phụ thuộc hàm đó từ các phụ thuộc hàm còn lại hay không.

***(=> Vì mỗi Vế Trái thuộc tính chỉ xuất hiện một lần nên chắc chắn sẽ không dư thừa)***

**+ Xét Id -> Title: (Loại Id -> Title ra khỏi F)**

Tính bao đóng:

Id+ = {Id, Description, Status, Priority, Deadline, CreatedAt, UpdatedAt, ProjectId, AssignedToUserId, AIReason, AIScore}

Không suy ra được Title.

→ Id -> Title không dư thừa.

**+ Xét Id -> Description: (Loại Id -> Description ra khỏi F)**

Tính bao đóng:

Id+ = {Id, Title, Status, Priority, Deadline, CreatedAt, UpdatedAt, ProjectId, AssignedToUserId, AIReason, AIScore}

Không suy ra được Description.

→ Id -> Description không dư thừa.

**+ Xét Id -> Status: (Loại Id -> Status ra khỏi F)**

Tính bao đóng:

Id+ = {Id, Title, Description, Priority, Deadline, CreatedAt, UpdatedAt, ProjectId, AssignedToUserId, AIReason, AIScore}

Không suy ra được Status.

→ Id -> Status không dư thừa.

**+ Xét Id -> Priority: (Loại Id -> Priority ra khỏi F)**

Tính bao đóng:

Id+ = {Id, Title, Description, Status, Deadline, CreatedAt, UpdatedAt, ProjectId, AssignedToUserId, AIReason, AIScore}

Không suy ra được Priority.

→ Id -> Priority không dư thừa.

**+ Xét Id -> Deadline: (Loại Id -> Deadline ra khỏi F)**

Tính bao đóng:

Id+ = {Id, Title, Description, Status, Priority, CreatedAt, UpdatedAt, ProjectId, AssignedToUserId, AIReason, AIScore}

Không suy ra được Deadline.

→ Id -> Deadline không dư thừa.

**+ Xét Id -> CreatedAt: (Loại Id -> CreatedAt ra khỏi F)**

Tính bao đóng:

Id+ = {Id, Title, Description, Status, Priority, Deadline, UpdatedAt, ProjectId, AssignedToUserId, AIReason, AIScore}

Không suy ra được CreatedAt.

→ Id -> CreatedAt không dư thừa.

**+ Xét Id -> UpdatedAt: (Loại Id -> UpdatedAt ra khỏi F)**

Tính bao đóng:

Id+ = {Id, Title, Description, Status, Priority, Deadline, CreatedAt, ProjectId, AssignedToUserId, AIReason, AIScore}

Không suy ra được UpdatedAt.

→ Id -> UpdatedAt không dư thừa.

**+ Xét Id -> ProjectId: (Loại Id -> ProjectId ra khỏi F)**

Tính bao đóng:

Id+ = {Id, Title, Description, Status, Priority, Deadline, CreatedAt, UpdatedAt, AssignedToUserId, AIReason, AIScore}

Không suy ra được ProjectId.

→ Id -> ProjectId không dư thừa.

**+ Xét Id -> AssignedToUserId: (Loại Id -> AssignedToUserId ra khỏi F)**

Tính bao đóng:

Id+ = {Id, Title, Description, Status, Priority, Deadline, CreatedAt, UpdatedAt, ProjectId, AIReason, AIScore}

Không suy ra được AssignedToUserId.

→ Id -> AssignedToUserId không dư thừa.

**+ Xét Id -> AIReason: (Loại Id -> AIReason ra khỏi F)**

Tính bao đóng:

Id+ = {Id, Title, Description, Status, Priority, Deadline, CreatedAt, UpdatedAt, ProjectId, AssignedToUserId, AIScore}

Không suy ra được AIReason.

→ Id -> AIReason không dư thừa.

**+ Xét Id -> AIScore: (Loại Id -> AIScore ra khỏi F)**

Tính bao đóng:

Id+ = {Id, Title, Description, Status, Priority, Deadline, CreatedAt, UpdatedAt, ProjectId, AssignedToUserId, AIReason}

Không suy ra được AIScore.

→ Id -> AIScore không dư thừa.

Kết luận phủ tối thiểu:

Không có phụ thuộc hàm nào dư thừa.

Fmin = {

Id -> Title

Id -> Description

Id -> Status

Id -> Priority

Id -> Deadline

Id -> CreatedAt

Id -> UpdatedAt

Id -> ProjectId

Id -> AssignedToUserId

Id -> AIReason

Id -> AIScore

Id -> DependsOnTaskId

}

**-Bảng 6: ActivityLogs**

|  |  |  |  |
| --- | --- | --- | --- |
| Thuộc tính | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
| Id | int | PK | Mã lịch sử hoạt động |
| ProjectId | int | NULL, FK | Dự án liên quan |
| UserId | nvarchar(450) | NOT NULL, FK | Người thực hiện hoạt động |
| Action | nvarchar(max) | NOT NULL | Nội dung hành động |
| TaskTitle | nvarchar(max) | NULL | Tên công việc liên quan |
| CreatedAt | datetime2 | NOT NULL | Thời điểm hoạt động xảy ra |

***1. Xác định khóa***

Khóa ứng viên: K = {Id}

Vì: Id+ = {Id, ProjectId, UserId, Action, TaskTitle, CreatedAt}

→ Do đó Id là khóa của quan hệ.

**=> Các thuộc tính ProjectId, UserId, TaskTitle không phải khóa vì:**

ProjectId không phải khóa vì một dự án có thể có nhiều lịch sử hoạt động.

UserId không phải khóa vì một người có thể thực hiện nhiều hoạt động.

TaskTitle không phải khóa vì một công việc có thể xuất hiện trong nhiều hoạt động khác nhau.

***2. Xác định dạng chuẩn***

Khóa của quan hệ là: K = {Id}

Các thuộc tính không khóa: ProjectId, UserId, Action, TaskTitle, CreatedAt

**1NF**: Đạt 1NF vì các thuộc tính đều chứa giá trị đơn, không có thuộc tính đa trị hay nhóm lặp.

**2NF**: Đạt 2NF vì khóa Id chỉ gồm một thuộc tính nên không thể xảy ra phụ thuộc bộ phận.(Khóa chỉ có 1 thuộc tính nên luôn đạt DC2)

**3NF**: Đạt 3NF vì với mọi phụ thuộc hàm Id -> A, vế trái Id là siêu khóa.

**BCNF**: Đạt BCNF vì với mọi phụ thuộc hàm không tầm thường X -> Y, X là siêu khóa. Ở đây các phụ thuộc hàm đều có vế trái là Id, mà Id là khóa.

Kết luận:

**ActivityLogs đạt BCNF.**

1. ***Tìm Phủ Tối Thiểu***

**Bước 1**: Phân rã vế phải

Vế trái của các phụ thuộc hàm chỉ chứa 1 thuộc tính đơn nên không cần phân rã vế trái.

**Bước 2**: Loại bỏ thuộc tính dư thừa ở vế trái

Vế trái của tất cả các phụ thuộc hàm chỉ chứa 1 thuộc tính, nên không có thuộc tính dư thừa ở vế trái để loại bỏ.

**Bước 3**: Loại bỏ phụ thuộc hàm dư thừa

Lần lượt che từng phụ thuộc hàm và kiểm tra xem có thể suy ra phụ thuộc hàm đó từ các phụ thuộc hàm còn lại hay không.

***(=> Vì mỗi Vế Trái thuộc tính chỉ xuất hiện một lần nên chắc chắn sẽ không dư thừa)***

**+ Xét Id -> ProjectId: (Loại Id -> ProjectId ra khỏi F)**

Tính bao đóng:

Id+ = {Id, UserId, Action, TaskTitle, CreatedAt}

Không suy ra được ProjectId.

→ Id -> ProjectId không dư thừa.

**+ Xét Id -> UserId: (Loại Id -> UserId ra khỏi F)**

Tính bao đóng:

Id+ = {Id, ProjectId, Action, TaskTitle, CreatedAt}

Không suy ra được UserId.

→ Id -> UserId không dư thừa.

**+ Xét Id -> Action: (Loại Id -> Action ra khỏi F)**

Tính bao đóng:

Id+ = {Id, ProjectId, UserId, TaskTitle, CreatedAt}

Không suy ra được Action.

→ Id -> Action không dư thừa.

**+ Xét Id -> TaskTitle: (Loại Id -> TaskTitle ra khỏi F)**

Tính bao đóng:

Id+ = {Id, ProjectId, UserId, Action, CreatedAt}

Không suy ra được TaskTitle.

→ Id -> TaskTitle không dư thừa.

**+ Xét Id -> CreatedAt: (Loại Id -> CreatedAt ra khỏi F)**

Tính bao đóng:

Id+ = {Id, ProjectId, UserId, Action, TaskTitle}

Không suy ra được CreatedAt.

→ Id -> CreatedAt không dư thừa.

Kết luận phủ tối thiểu:

Không có phụ thuộc hàm nào dư thừa.

Fmin = {

Id -> ProjectId

Id -> UserId

Id -> Action

Id -> TaskTitle

Id -> CreatedAt

}

**-Bảng 7:ProjectInvitations**

|  |  |  |  |
| --- | --- | --- | --- |
| Thuộc tính | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
| Id | int | PK | Mã lời mời |
| ProjectId | int | NOT NULL, FK | Dự án được mời tham gia |
| InvitedUserId | nvarchar(450) | NOT NULL, FK | Người được mời |
| InvitedByUserId | nvarchar(450) | NOT NULL, FK | Người gửi lời mời |
| CreatedAt | datetime2 | NOT NULL | Thời điểm gửi lời mời |
| IsAccepted | bit | NOT NULL | Trạng thái đã chấp nhận |
| IsRejected | bit | NOT NULL | Trạng thái đã từ chối |

***1. Xác định khóa***

Khóa ứng viên: K = {Id}

Vì: Id+ = {Id, ProjectId, InvitedUserId, InvitedByUserId, CreatedAt, IsAccepted, IsRejected}

→ Do đó Id là khóa của quan hệ.

**=> Các thuộc tính ProjectId, InvitedUserId, InvitedByUserId không phải khóa vì:**

ProjectId không phải khóa vì một dự án có thể có nhiều lời mời tham gia.

InvitedUserId không phải khóa vì một người có thể nhận nhiều lời mời tham gia các dự án khác nhau.

InvitedByUserId không phải khóa vì một người có thể gửi nhiều lời mời cho nhiều người khác nhau.

***2. Xác định dạng chuẩn***

Khóa của quan hệ là: K = {Id}

Các thuộc tính không khóa: ProjectId, InvitedUserId, InvitedByUserId, CreatedAt, IsAccepted, IsRejected

**1NF**: Đạt 1NF vì các thuộc tính đều chứa giá trị đơn, không có thuộc tính đa trị hay nhóm lặp.

**2NF**: Đạt 2NF vì khóa Id chỉ gồm một thuộc tính nên không thể xảy ra phụ thuộc bộ phận. (Khóa chỉ có 1 thuộc tính nên luôn đạt DC2)

**3NF**: Đạt 3NF vì với mọi phụ thuộc hàm Id -> A, vế trái Id là siêu khóa.

**BCNF**: Đạt BCNF vì với mọi phụ thuộc hàm không tầm thường X -> Y, X là siêu khóa. Ở đây các phụ thuộc hàm đều có vế trái là Id, mà Id là khóa.

Kết luận:

**ProjectInvitations đạt BCNF.**

1. ***Tìm Phủ Tối Thiểu***

**Bước 1**: Phân rã vế phải

Vế trái của các phụ thuộc hàm chỉ chứa 1 thuộc tính đơn nên không cần phân rã vế trái.

**Bước 2:** Loại bỏ thuộc tính dư thừa ở vế trái

Vế trái của tất cả các phụ thuộc hàm chỉ chứa 1 thuộc tính, nên không có thuộc tính dư thừa ở vế trái để loại bỏ.

**Bước 3**: Loại bỏ phụ thuộc hàm dư thừa

Lần lượt che từng phụ thuộc hàm và kiểm tra xem có thể suy ra phụ thuộc hàm đó từ các phụ thuộc hàm còn lại hay không.

***(=> Vì mỗi Vế Trái thuộc tính chỉ xuất hiện một lần nên chắc chắn sẽ không dư thừa)***

**+ Xét Id -> ProjectId: (Loại Id -> ProjectId ra khỏi F)**

Tính bao đóng:

Id+ = {Id, InvitedUserId, InvitedByUserId, CreatedAt, IsAccepted, IsRejected}

Không suy ra được ProjectId.

→ Id -> ProjectId không dư thừa.

**+ Xét Id -> InvitedUserId: (Loại Id -> InvitedUserId ra khỏi F)**

Tính bao đóng:

Id+ = {Id, ProjectId, InvitedByUserId, CreatedAt, IsAccepted, IsRejected}

Không suy ra được InvitedUserId.

→ Id -> InvitedUserId không dư thừa.

**+ Xét Id -> InvitedByUserId: (Loại Id -> InvitedByUserId ra khỏi F)**

Tính bao đóng:

Id+ = {Id, ProjectId, InvitedUserId, CreatedAt, IsAccepted, IsRejected}

Không suy ra được InvitedByUserId.

→ Id -> InvitedByUserId không dư thừa.

**+ Xét Id -> CreatedAt: (Loại Id -> CreatedAt ra khỏi F)**

Tính bao đóng:

Id+ = {Id, ProjectId, InvitedUserId, InvitedByUserId, IsAccepted, IsRejected}

Không suy ra được CreatedAt.

→ Id -> CreatedAt không dư thừa.

**+ Xét Id -> IsAccepted: (Loại Id -> IsAccepted ra khỏi F)**

Tính bao đóng:

Id+ = {Id, ProjectId, InvitedUserId, InvitedByUserId, CreatedAt, IsRejected}

Không suy ra được IsAccepted.

→ Id -> IsAccepted không dư thừa.

**+ Xét Id -> IsRejected: (Loại Id -> IsRejected ra khỏi F)**

Tính bao đóng:

Id+ = {Id, ProjectId, InvitedUserId, InvitedByUserId, CreatedAt, IsAccepted}

Không suy ra được IsRejected.

→ Id -> IsRejected không dư thừa.

Kết luận phủ tối thiểu:

Không có phụ thuộc hàm nào dư thừa.

Fmin = {

Id -> ProjectId

Id -> InvitedUserId

Id -> InvitedByUserId

Id -> CreatedAt

Id -> IsAccepted

Id -> IsRejected

}

**-Bảng 8: ProjectMessages**

|  |  |  |  |
| --- | --- | --- | --- |
| Thuộc tính | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
| Id | int | PK | Mã tin nhắn |
| ProjectId | int | NOT NULL | Dự án chứa tin nhắn |
| UserId | nvarchar(450) | NOT NULL, FK | Người gửi tin nhắn |
| Message | nvarchar(max) | NOT NULL | Nội dung tin nhắn |
| CreatedAt | datetime2 | NOT NULL | Thời điểm gửi tin nhắn |

***1. Xác định khóa***

Khóa ứng viên: K = {Id}

Vì: Id+ = {Id, ProjectId, UserId, Message, CreatedAt}

→ Do đó Id là khóa của quan hệ.

**=> Các thuộc tính ProjectId, UserId không phải khóa vì:**

ProjectId không phải khóa vì một dự án có thể có nhiều tin nhắn.

UserId không phải khóa vì một người có thể gửi nhiều tin nhắn trong dự án.

***2. Xác định dạng chuẩn***

Khóa của quan hệ là: K = {Id}

Các thuộc tính không khóa: ProjectId, UserId, Message, CreatedAt

**1NF**: Đạt 1NF vì các thuộc tính đều chứa giá trị đơn, không có thuộc tính đa trị hay nhóm lặp.

**2NF**: Đạt 2NF vì khóa Id chỉ gồm một thuộc tính nên không thể xảy ra phụ thuộc bộ phận.(Khóa chỉ có 1 thuộc tính nên luôn đạt DC2)

**3NF**: Đạt 3NF vì với mọi phụ thuộc hàm Id -> A, vế trái Id là siêu khóa.

BCNF: Đạt BCNF vì với mọi phụ thuộc hàm không tầm thường X -> Y, X là siêu khóa. Ở đây các phụ thuộc hàm đều có vế trái là Id, mà Id là khóa.

Kết luận:

**ProjectMessages đạt BCNF.**

***3. Tìm Phủ Tối Thiểu***

**Bước 1**: Phân rã vế phải

Vế trái của các phụ thuộc hàm chỉ chứa 1 thuộc tính đơn nên không cần phân rã vế trái.

**Bước 2**: Loại bỏ thuộc tính dư thừa ở vế trái

Vế trái của tất cả các phụ thuộc hàm chỉ chứa 1 thuộc tính, nên không có thuộc tính dư thừa ở vế trái để loại bỏ.

**Bước 3**: Loại bỏ phụ thuộc hàm dư thừa

Lần lượt che từng phụ thuộc hàm và kiểm tra xem có thể suy ra phụ thuộc hàm đó từ các phụ thuộc hàm còn lại hay không.

**(=> Vì mỗi Vế Trái thuộc tính chỉ xuất hiện một lần nên chắc chắn sẽ không dư thừa)**

**+ Xét Id -> ProjectId: (Loại Id -> ProjectId ra khỏi F)**

Tính bao đóng:

Id+ = {Id, UserId, Message, CreatedAt}

Không suy ra được ProjectId.

→ Id -> ProjectId không dư thừa.

**+ Xét Id -> UserId: (Loại Id -> UserId ra khỏi F)**

Tính bao đóng:

Id+ = {Id, ProjectId, Message, CreatedAt}

Không suy ra được UserId.

→ Id -> UserId không dư thừa.

**+ Xét Id -> Message: (Loại Id -> Message ra khỏi F)**

Tính bao đóng:

Id+ = {Id, ProjectId, UserId, CreatedAt}

Không suy ra được Message.

→ Id -> Message không dư thừa.

**+ Xét Id -> CreatedAt: (Loại Id -> CreatedAt ra khỏi F)**

Tính bao đóng:

Id+ = {Id, ProjectId, UserId, Message}

Không suy ra được CreatedAt.

→ Id -> CreatedAt không dư thừa.

Kết luận phủ tối thiểu:

Không có phụ thuộc hàm nào dư thừa.

Fmin = {

Id -> ProjectId

Id -> UserId

Id -> Message

Id -> CreatedAt

}

**-Bảng 9: AiLearningRecords**

|  |  |  |  |
| --- | --- | --- | --- |
| Thuộc tính | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
| Id | int | PK | Mã bản ghi học AI |
| Text | nvarchar(max) | NOT NULL | Nội dung dữ liệu được AI xử lý |
| Score | float | NULL | Điểm đánh giá của AI |
| Priority | nvarchar(max) | NOT NULL | Mức độ ưu tiên do AI xác định |
| Reason | nvarchar(max) | NULL | Lý do AI đưa ra kết quả |
| Corrected | bit | NOT NULL | Cho biết kết quả AI đã được điều chỉnh hay chưa |
| CreatedAt | datetime2 | NOT NULL | Thời điểm tạo bản ghi |

***1. Xác định khóa***

Khóa ứng viên: K = {Id}

Vì:Id+ = {Id, Text, Score, Priority, Reason, Corrected, CreatedAt}

→ Do đó Id là khóa của quan hệ.

**=> Các thuộc tính Text, Score, Priority, Reason, Corrected, CreatedAt không phải khóa vì:**

Text không phải khóa vì một nội dung có thể xuất hiện trong nhiều bản ghi học AI.

Score không phải khóa vì nhiều bản ghi có thể có cùng điểm đánh giá.

Priority không phải khóa vì nhiều bản ghi có thể có cùng mức độ ưu tiên.

Reason không phải khóa vì nhiều bản ghi có thể có cùng lý do.

Corrected không phải khóa vì nhiều bản ghi có thể có cùng trạng thái điều chỉnh.

CreatedAt không phải khóa vì nhiều bản ghi có thể được tạo tại các thời điểm giống nhau.

***2. Xác định dạng chuẩn***

Khóa của quan hệ là: K = {Id}

Các thuộc tính không khóa: Text, Score, Priority, Reason, Corrected, CreatedAt

**1NF**: Đạt 1NF vì các thuộc tính đều chứa giá trị đơn, không có thuộc tính đa trị hay nhóm lặp.

**2NF**: Đạt 2NF vì khóa Id chỉ gồm một thuộc tính nên không thể xảy ra phụ thuộc bộ phận. (Khóa chỉ có 1 thuộc tính nên luôn đạt DC2)

**3NF**: Đạt 3NF vì với mọi phụ thuộc hàm Id -> A, vế trái Id là siêu khóa.

**BCNF:** Đạt BCNF vì với mọi phụ thuộc hàm không tầm thường X -> Y, X là siêu khóa. Ở đây các phụ thuộc hàm đều có vế trái là Id, mà Id là khóa.

Kết luận:

**AiLearningRecords đạt BCNF.**

***3. Tìm Phủ Tối Thiểu***

**Bước 1**: Phân rã vế phải

Vế trái của các phụ thuộc hàm chỉ chứa 1 thuộc tính đơn nên không cần phân rã vế trái.

**Bước 2:** Loại bỏ thuộc tính dư thừa ở vế trái

Vế trái của tất cả các phụ thuộc hàm chỉ chứa 1 thuộc tính, nên không có thuộc tính dư thừa ở vế trái để loại bỏ.

**Bước 3**: Loại bỏ phụ thuộc hàm dư thừa

Lần lượt che từng phụ thuộc hàm và kiểm tra xem có thể suy ra phụ thuộc hàm đó từ các phụ thuộc hàm còn lại hay không.

**(=> Vì mỗi Vế Trái thuộc tính chỉ xuất hiện một lần nên chắc chắn sẽ không dư thừa)**

**+ Xét Id -> Text: (Loại Id -> Text ra khỏi F)**

Tính bao đóng:

Id+ = {Id, Score, Priority, Reason, Corrected, CreatedAt}

Không suy ra được Text.

→ Id -> Text không dư thừa.

**+ Xét Id -> Score: (Loại Id -> Score ra khỏi F)**

Tính bao đóng:

Id+ = {Id, Text, Priority, Reason, Corrected, CreatedAt}

Không suy ra được Score.

→ Id -> Score không dư thừa.

**+ Xét Id -> Priority: (Loại Id -> Priority ra khỏi F)**

Tính bao đóng:

Id+ = {Id, Text, Score, Reason, Corrected, CreatedAt}

Không suy ra được Priority.

→ Id -> Priority không dư thừa.

**+ Xét Id -> Reason: (Loại Id -> Reason ra khỏi F)**

Tính bao đóng:

Id+ = {Id, Text, Score, Priority, Corrected, CreatedAt}

Không suy ra được Reason.

→ Id -> Reason không dư thừa.

**+ Xét Id -> Corrected: (Loại Id -> Corrected ra khỏi F)**

Tính bao đóng:

Id+ = {Id, Text, Score, Priority, Reason, CreatedAt}

Không suy ra được Corrected.

→ Id -> Corrected không dư thừa.

**+ Xét Id -> CreatedAt: (Loại Id -> CreatedAt ra khỏi F)**

Tính bao đóng:

Id+ = {Id, Text, Score, Priority, Reason, Corrected}

Không suy ra được CreatedAt.

→ Id -> CreatedAt không dư thừa.

Kết luận phủ tối thiểu:

Không có phụ thuộc hàm nào dư thừa.

Fmin = {

Id -> Text

Id -> Score

Id -> Priority

Id -> Reason

Id -> Corrected

Id -> CreatedAt

}

**-Bảng 10: AiTrainingData**

|  |  |  |  |
| --- | --- | --- | --- |
| Thuộc tính | Kiểu dữ liệu | Ràng buộc | Ý nghĩa |
| Id | int | PK | Mã dữ liệu huấn luyện |
| InputText | nvarchar(max) | NULL | Dữ liệu đầu vào dùng để huấn luyện AI |
| Intent | nvarchar(100) | NULL | Ý định được xác định từ dữ liệu đầu vào |

***1. Xác định khóa***

Khóa ứng viên: K = {Id}

Vì:Id+ = {Id, InputText, Intent}

→ Do đó Id là khóa của quan hệ.

**=> Các thuộc tính InputText, Intent không phải khóa vì:**

InputText không phải khóa vì nhiều dữ liệu huấn luyện có thể có nội dung đầu vào giống hoặc tương tự nhau.

Intent không phải khóa vì nhiều dữ liệu huấn luyện có thể cùng thuộc một ý định.

***2. Xác định dạng chuẩn***

Khóa của quan hệ là: K = {Id}

Thuộc tính không khóa: InputText, Intent

**1NF**: Đạt 1NF vì các thuộc tính đều chứa giá trị đơn, không có thuộc tính đa trị hay nhóm lặp.

**2NF:** Đạt 2NF vì khóa Id chỉ gồm một thuộc tính nên không thể xảy ra phụ thuộc bộ phận. (Khóa chỉ có 1 thuộc tính nên luôn đạt DC2)

**3NF:** Đạt 3NF vì với mọi phụ thuộc hàm Id -> A, vế trái Id là siêu khóa.

**BCNF:** Đạt BCNF vì với mọi phụ thuộc hàm không tầm thường X -> Y, X là siêu khóa. Ở đây các phụ thuộc hàm đều có vế trái là Id, mà Id là khóa.

Kết luận:

**AiTrainingData đạt BCNF.**

***3. Tìm Phủ Tối Thiểu***

**Bước 1**: Phân rã vế phải

Vế trái của các phụ thuộc hàm chỉ chứa 1 thuộc tính đơn nên không cần phân rã vế trái.

**Bước 2**: Loại bỏ thuộc tính dư thừa ở vế trái

Vế trái của tất cả các phụ thuộc hàm chỉ chứa 1 thuộc tính, nên không có thuộc tính dư thừa ở vế trái để loại bỏ.

**Bước 3:** Loại bỏ phụ thuộc hàm dư thừa

Lần lượt che từng phụ thuộc hàm và kiểm tra xem có thể suy ra phụ thuộc hàm đó từ các phụ thuộc hàm còn lại hay không.

**(=> Vì mỗi Vế Trái thuộc tính chỉ xuất hiện một lần nên chắc chắn sẽ không dư thừa)**

**+ Xét Id -> InputText: (Loại Id -> InputText ra khỏi F)**

Tính bao đóng:

Id+ = {Id, Intent}

Không suy ra được InputText.

→ Id -> InputText không dư thừa.

**+ Xét Id -> Intent: (Loại Id -> Intent ra khỏi F)**

Tính bao đóng:

Id+ = {Id, InputText}

Không suy ra được Intent.

→ Id -> Intent không dư thừa.

Kết luận phủ tối thiểu:

Không có phụ thuộc hàm nào dư thừa.

Fmin = {

Id -> InputText

Id -> Intent

}

Qua quá trình phân tích 10 quan hệ của hệ thống, nhận thấy tất cả các quan hệ đều đạt dạng chuẩn BCNF.

=>Do đó, lược đồ quan hệ của toàn bộ hệ thống đạt dạng chuẩn BCNF (Boyce-Codd Normal Form).

***=> Dạng chuẩn cao nhất của toàn bộ lược đồ: BCNF.***