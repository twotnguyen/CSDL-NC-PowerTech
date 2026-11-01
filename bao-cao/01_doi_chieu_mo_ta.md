# Đối chiếu ba bản mô tả đề tài và kiểm tra tính thực tế

Ngày làm: 18/10/2026. Các bản được so sánh (mục 1 đến 6 so A, B, v2; mục 7 đến 9 nói về v3):

| Ký hiệu | File | Ghi chú |
|---|---|---|
| **A** | phần "Mô tả" trong [PowerTech-CSDL-NC.md](PowerTech-CSDL-NC.md) | Bản đầu đã nộp. File `.docx` trong `bao-cao/` và `Documents/` giống hệt, văn bản trùng với `.md` |
| **B** | [01_Mo_ta_de_tai.md](01_Mo_ta_de_tai.md) | Bản viết lại sau nhận xét của giảng viên |
| **C** (v2) | [01_Mo_ta_de_tai_v2.md](01_Mo_ta_de_tai_v2.md) | Bản sửa B cho sát thực tế (đã làm trước) |
| **D** (v3) | [01_Mo_ta_de_tai_v3.md](01_Mo_ta_de_tai_v3.md) (+ `.docx`) | **Bản chính thức hiện tại.** Tổng hợp A, B, v2, dữ liệu thực của website và nguồn thực tế. Các bản khác giữ làm tham chiếu |

Nhãn trong file này: **[Nguồn]** có nguồn đã đọc ở mục 5; **[Quy ước]** do PowerTech tự đặt hợp lý, chưa có nguồn xác minh, cần nhóm xác nhận; **[Nhận định]** suy luận của người ghi chép.

## 1. A so với B: giữ, thêm, bỏ, đổi

| Chủ đề | A (bản đầu) | B (01_Mo_ta) | Thay đổi |
|---|---|---|---|
| Phạm vi | Một cửa hàng; chưa xét chi nhánh, **lắp ráp máy**, kế toán đầy đủ | Một cửa hàng; chưa xét chi nhánh, kế toán chuyên sâu, thuật toán gợi ý | Đổi: bỏ "lắp ráp máy" và thêm "AI gợi ý" khỏi danh sách loại trừ |
| Hàng bán | Linh kiện, máy bộ, thiết bị công nghệ | Thêm máy tính xách tay | Thêm |
| Khó khăn và lĩnh vực tin học hóa | Không có | Mục 1.1 mới: bốn khó khăn, lĩnh vực cần tin học hóa | Thêm (giảng viên yêu cầu) |
| Nhân viên, tài khoản, vai trò | Tài khoản riêng, nhiều vai trò, quản trị phân quyền; vai trò: bán hàng, kho, hỗ trợ, giao hàng, quản trị | Chỉ còn mã, họ tên, SĐT, trạng thái; vai trò: tư vấn bán hàng, kỹ thuật kho, giao hàng, chăm sóc khách hàng, quản lý | Bỏ tài khoản và phân quyền; đổi tên vai trò |
| Người quản lý duyệt | Duyệt điều chỉnh kho **và hoàn tiền** | Chỉ duyệt kiểm kê và chuyển nhóm kho | Bỏ phần duyệt hoàn tiền |
| Khách hàng | Có thể chưa có tài khoản; mỗi tài khoản tối đa một khách; khách vãng lai không bắt buộc hồ sơ | **Bắt buộc** thu họ tên và SĐT khi mua tại quầy; tự nối hồ sơ khi đăng ký cùng SĐT | Đổi |
| Hạng thành viên, điểm thưởng | Không có | Bạc, Vàng, Kim Cương, điểm thưởng | Thêm |
| Địa chỉ nhận hàng | Nhiều địa chỉ, tối đa một mặc định | Giữ | Giữ |
| Loại hàng, thương hiệu | Loại phân cấp, một loại cha, không tạo vòng; tên có thể trùng | Giữ phân cấp; bỏ "không tạo vòng" và ghi chú tên trùng | Giữ, bỏ ràng buộc phụ |
| Giá | Giá niêm yết, **giá ưu đãi**, tình trạng kinh doanh | Chỉ giá niêm yết hiện tại | Bỏ giá ưu đãi |
| Ảnh và thông số | Một ảnh chính; đủ thông số bắt buộc; tối đa một giá trị mỗi thông số, đúng kiểu và loại | Một ảnh đại diện chính; mỗi mặt hàng có một giá trị cho thông số | Giữ ý chính, bỏ "đúng kiểu", "tối đa" |
| Nhà cung cấp | Nhiều sản phẩm ↔ nhiều nhà cung cấp; không có mã số thuế | Thêm mã số thuế; bỏ quan hệ nhiều–nhiều | Đổi |
| Phiếu nhập | Số dòng; cùng mặt hàng nhiều dòng; ít nhất một dòng; ghi tăng kho một lần; chi phí bổ sung riêng | Kiểm đếm cùng người giao, biên bản giao nhận (thêm); bỏ ba ràng buộc đầu | Thêm kiểm đếm; bỏ ràng buộc |
| Nhóm hàng trong kho | Đủ điều kiện bán / chờ kiểm tra / không đủ điều kiện bán chờ xử lý | Đủ điều kiện bán / chờ kiểm tra kỹ thuật / hàng lỗi chờ đổi trả nhà cung cấp | Đổi tên nhóm ba |
| Sổ kho | Tồn đầu có căn cứ; mỗi lần phát sinh có mã, người thực hiện, chứng từ nguồn | Không nhắc tồn đầu và chứng từ nguồn | Bỏ |
| Kiểm kê | Có chênh lệch thì đề nghị điều chỉnh, quản lý duyệt | Chi tiết hơn: định kỳ, theo vị trí lưu trữ, biên bản | Thêm chi tiết; **thêm "vị trí lưu trữ"** |
| Giỏ hàng | Giỏ tạm không cần tài khoản; gửi đơn phải đăng nhập; một giỏ đang dùng | Phải đăng nhập mới có giỏ | Đổi |
| Đơn và dòng đơn | Số đơn duy nhất, kênh bán, số dòng, cùng mặt hàng nhiều dòng | Giữ mã, người nhận, địa chỉ, giá chốt; bỏ kênh bán và số dòng | Giữ, bỏ chi tiết |
| Mã giảm giá | Hiệu lực, đơn tối thiểu, trần giảm, giới hạn lượt; chỉ giảm tiền hàng | Chỉ "tối đa một mã" | Bỏ chi tiết |
| Tổng tiền | Tiền hàng + phí giao − giảm; làm tròn một đồng | Không nhắc phí giao và công thức | Bỏ |
| Giữ hàng | Nhân viên bán hàng kiểm tra, xác nhận, giữ; sửa đơn cần khách đồng ý, lưu trước–sau; giao toàn bộ một đợt | Hệ thống tự giữ khi khách gửi đơn | Đổi (người thành tự động); bỏ phần sửa đơn |
| Thanh toán | Tiền mặt, CK, ví, COD; nhiều lần thử, lần thất bại không tính; hạn thu đủ thì hủy | Quầy: tiền mặt, QR; mạng: CK, ví điện tử, COD | Bỏ nhiều lần thử và hạn thanh toán |
| Hoàn tiền | Gắn khoản thu gốc; nhiều lần, tổng không vượt | Hoàn theo giá trừ giảm giá; tiền mặt, CK hoặc số dư nội bộ | Đổi; bỏ ràng buộc tổng |
| Giao hàng | Lịch sử phân công; tối đa 3 lần thất bại; người giao ghi, bán hàng hoặc quản lý xác nhận COD | Giữ 3 lần; COD nộp **thủ quỹ**; bỏ lịch sử phân công | Đổi, bỏ |
| Hủy đơn | Hủy trước xuất giải phóng giữ và mã; hủy sau xuất không tự tăng kho | Chỉ có trường hợp giao thất bại 3 lần | Bỏ |
| Trả hàng | Nhiều lần, tổng ≤ đã giao; khách vãng lai bằng chứng từ; hàng về chờ kiểm tra | Điều kiện 7 ngày; hồ sơ đổi trả; hàng về chờ kiểm tra bắt buộc | Thêm điều kiện 7 ngày; bỏ nhiều lần |
| Bảo hành | Chỉ đối chiếu căn cứ mua; **sửa chữa kỹ thuật ngoài phạm vi** | Quy trình sáu bước: seri, tem, phiếu tiếp nhận, sửa/đổi linh kiện/gửi hãng, biên bản trả | Thêm mạnh; ngược với A ở chỗ sửa chữa |
| Đánh giá, hỗ trợ khách | Đánh giá sản phẩm; hồ sơ hỗ trợ (người phụ trách, phản hồi) | Không có | Bỏ |
| Thu mua thiết bị cũ | Đề nghị, thẩm định, báo giá, chứng từ | Không có | Bỏ |
| Ví | Mỗi tài khoản tối đa một ví, không âm | Chỉ "số dư tài khoản nội bộ" | Bỏ gần hết |
| Bài hướng dẫn, thông báo, thống kê, lưu lịch sử | Có | Không có | Bỏ |
| Bán tại quầy | Một câu: lập đơn, giao trực tiếp, cấp chứng từ | Năm bước, có thu ngân, dán tem, chạy thử | Thêm mạnh (theo nhận xét giảng viên) |
| Đặt cọc | Không có | Không có | Cả hai đều thiếu |
| Phí đổi trả, hóa đơn | Không có | Không có | Cả hai đều thiếu |

**Nhận xét [Nhận định].** B bổ sung đúng ba điểm giảng viên hỏi (quầy, bảo hành, đổi trả) nhưng đồng thời **bỏ nhiều quy tắc về tiền và chứng từ** mà A có (nhiều lần thanh toán, hoàn nhiều lần, hạn thanh toán, phân công giao hàng) và **thêm các nội dung ngoài cơ sở dữ liệu hiện có** (hạng thành viên, điểm thưởng, vị trí lưu trữ, số seri, phiếu bảo hành, hồ sơ đổi trả). Danh sách thực thể trong `PowerTech-CSDL-NC.md` còn bám vào A.

## 2. Kiểm tra tính thực tế của B và cách C sửa

| # | Điểm trong B | Vấn đề so với thực tế | Căn cứ | Sửa trong C |
|---|---|---|---|---|
| 1 | Cửa hàng tự bảo hành: dán tem, tự sửa, đổi linh kiện kho, rồi gửi hãng | Cửa hàng linh kiện thường bán hàng nhà phân phối; bảo hành thật do hãng hoặc nhà phân phối. Cửa hàng là đầu mối tiếp nhận và gửi hãng | [Nguồn] GearVN: gửi nhà sản xuất hoặc đơn vị ủy quyền, bảo hành theo chính sách của hãng, không chịu trách nhiệm nếu hãng từ chối | Mục 1.1 và 1.2.5: PowerTech là đầu mối; sửa tại cửa hàng chỉ khi hãng cho phép |
| 2 | Thời gian hẹn "ghi trên phiếu" nhưng không nêu cỡ | Thời gian bảo hành hãng thường từ vài ngày đến khoảng 30 ngày | [Nguồn] GearVN: 7–30 ngày laptop, màn hình, bàn phím, bo mạch chủ; CPU 7–14 ngày; cam kết trong 30 ngày | 1.2.5 bước 3: "thường từ 7 đến 30 ngày tùy hãng và loại hàng" |
| 3 | Chỉ có "đủ điều kiện hoặc không" | Thực tế còn trường hợp kiểm tra không thấy lỗi thì trả lại khách | [Nguồn] GearVN: không phát sinh lỗi thì hoàn trả sau 3 ngày | 1.2.5 bước 4 |
| 4 | Bảo hành xong thì trả; chưa nói khi không sửa được | Luật quy định đổi sản phẩm mới tương tự hoặc thu hồi và trả tiền nếu hết thời hạn hẹn mà không sửa được, hoặc đã bảo hành từ 3 lần mà lỗi còn | [Nguồn] Luật 19/2023/QH15, Điều 30 khoản 2 điểm đ (qua trang caselaw.vn) | 1.2.5 bước 5 |
| 5 | Phiếu tiếp nhận không ghi "thời gian thực hiện" rõ | Luật yêu cầu cấp văn bản tiếp nhận bảo hành ghi thời gian thực hiện | [Nguồn] Điều 30 khoản 2 điểm c | 1.2.5 bước 3 có ngày hẹn trả |
| 6 | Dán tem cửa hàng "lên linh kiện" | Tem của cửa hàng không được che tem niêm phong của hãng, vì tem hãng rách là lý do từ chối bảo hành | [Nguồn] GearVN và Hoàng Hà PC đều từ chối khi tem hãng rách hoặc tẩy xóa; [Nhận định] suy ra tem cửa hàng không nên đè lên | 1.2.3 bước 5: dán lên hộp hoặc vị trí không che tem hãng |
| 7 | Mọi sản phẩm đều có seri duy nhất | Nhiều phụ kiện, cáp, tản nhiệt không có seri riêng | [Nhận định] | 1.2.1: chỉ hàng thường có seri mới ghi seri từng chiếc |
| 8 | Bán tại quầy: "mở hộp kiểm tra và bật máy chạy thử" mọi sản phẩm | Linh kiện mở hộp thì không bán lại như hàng mới; chính các cửa hàng cũng yêu cầu hộp nguyên vẹn khi đổi | [Nguồn] GearVN: đổi mới khi còn như mới, hộp không hư hại | 1.2.3 bước 4: kiểm tra niêm phong, chỉ chạy thử máy bộ, laptop, màn hình; mở hộp linh kiện khi khách yêu cầu |
| 9 | Đổi trả 7 ngày chung cho mọi hàng | Cửa hàng linh kiện thường tách thời hạn theo loại hàng; GearVN đổi mới linh kiện trong 30 ngày, laptop và màn hình trong 7 ngày | [Nguồn] GearVN | 1.2.6: 30 ngày linh kiện, 7 ngày laptop và màn hình |
| 10 | Không phân biệt lỗi nhà sản xuất với khách đổi ý | Hai trường hợp khác nhau về điều kiện và chi phí | [Quy ước] khách đổi ý chỉ khi còn nguyên niêm phong trong 7 ngày, có thể thu phí xử lý | 1.2.6: hai trường hợp riêng |
| 11 | Hàng trả chỉ có hai đường: bán lại hoặc trả nhà cung cấp | Hàng đã mở hộp nhưng không lỗi thường bán lại dạng hàng đã mở hộp giảm giá | [Quy ước]; [Nhận định] | 1.2.6 bước 4 |
| 12 | Không có đặt cọc | Hàng đặt từ nhà cung cấp và máy tính lắp theo cấu hình riêng thường cần cọc; giảng viên hỏi "đặt cọc không?" ở nhiều nhóm | [Quy ước]; giảng viên hỏi ở D5/g12, D6/g11, g13 | 1.2.4 bước 5; mức cọc "do hai bên thỏa thuận" |
| 13 | Không có hóa đơn, không có khách doanh nghiệp | Luật yêu cầu bên kinh doanh cung cấp hóa đơn, chứng từ theo quy định hoặc theo yêu cầu khách; khách công ty thường cần hóa đơn có mã số thuế | [Nguồn] Luật 19/2023, Điều 29 khoản 1 | 1.2.3 bước 5 |
| 14 | Không nêu hóa đơn điện tử từ máy tính tiền | Từ 1/6/2025, hộ kinh doanh bán lẻ thuộc diện phải dùng hóa đơn điện tử khởi tạo từ máy tính tiền | [Nguồn thứ cấp, chưa đối chiếu văn bản gốc] Nghị định 70/2025/NĐ-CP qua MISA, Sapo | C chỉ ghi "cấp hóa đơn theo quy định"; không đi vào kế toán |
| 15 | Bán tại quầy chỉ tiền mặt hoặc QR | Quầy bán lẻ thường nhận cả quẹt thẻ; trả góp qua công ty tài chính rất phổ biến | [Nguồn] Phong Vũ có chương trình trả góp; thẻ quầy là [Nhận định] | 1.2.3 bước 3: thêm quẹt thẻ; trả góp loại trừ |
| 16 | Hệ thống tự liên kết hồ sơ quầy với tài khoản khi trùng SĐT | Nối chỉ bằng số điện thoại không an toàn: người khác có thể đăng ký bằng số của khách | [Nhận định] | 1.2.2: chỉ nối sau khi khách xác nhận bằng mã gửi về số điện thoại |
| 17 | Bắt buộc thu SĐT mọi khách quầy | Thực tế khách có thể từ chối; cửa hàng vẫn phải bán | [Nhận định]; GearVN từ chối bảo hành khi không có thông tin mua | 1.2.2: đề nghị, không bắt buộc; bảo hành đối chiếu chứng từ và seri |
| 18 | Hạng thành viên Bạc, Vàng, Kim Cương và điểm thưởng | Không có trong dữ liệu hiện có; làm rộng phạm vi trong khi giảng viên nhắc giới hạn chức năng | Giảng viên: D5/g3, D6/g8, g15 | Chuyển sang loại trừ trong 1.3 |
| 19 | "Hệ thống tự giữ hàng" ngay khi khách gửi đơn, trả trước thì chờ thu tiền | Thực tế nhân viên gọi xác nhận đơn, nhất là đơn giá trị cao hoặc COD; A đã có "nhân viên bán hàng xác nhận" | [Nhận định]; A | 1.2.4 bước 2: nhân viên gọi xác nhận rồi giữ hàng |
| 20 | Giao thất bại 3 lần: hủy; không nói chế tài khi bỏ đơn | Giảng viên hỏi chế tài boom hàng | D5/g5 | 1.2.4 bước 9: bỏ đơn từ lần thứ hai chỉ bán khi trả trước [Quy ước] |
| 21 | Không nhắc khách kiểm hàng khi nhận COD | Thực tế khách kiểm niêm phong, thường quay video mở hộp để làm bằng chứng | [Nhận định] | 1.2.4 bước 8 |
| 22 | Kiểm kê "theo từng vị trí lưu trữ" | Cơ sở dữ liệu hiện có không theo dõi vị trí; tồn lưu tổng theo sản phẩm | `README.md` mục 2 | 1.3: theo mặt hàng và tình trạng, chưa theo vị trí |
| 23 | Bỏ nhiều nhà cung cấp cho một mặt hàng và quy trình trả hàng nhà cung cấp | Hàng lỗi nhập về hoặc khách gửi bảo hành đều phải qua nhà cung cấp hoặc hãng | [Nhận định]; GearVN | 1.2.7 bước 1 và 5 |
| 24 | "Thủ quỹ" nhận tiền COD nhưng không có trong danh sách nhân viên | Thiếu nhất quán nội bộ của B | B | 1.2.2 có thu ngân; 1.2.4 bước 8: nộp về thủ quỹ, quản lý hoặc bán hàng xác nhận |
| 25 | Dùng từ "hệ thống", "nền tảng web", "nhấn gửi đơn", "đăng nhập" nhiều lần | `QUYET_DINH.md` yêu cầu văn phong đời sống, tránh từ kỹ thuật và thao tác giao diện | `QUYET_DINH.md` mục 2 | C không dùng từ "hệ thống"; chỉ nhắc "tin học hóa" ở 1.1, còn lại viết như chủ cửa hàng kể |

## 3. Những quy ước C tự đặt (cần nhóm xác nhận)

Các con số và chính sách sau **không có nguồn xác minh**; nếu giảng viên hỏi, nói rõ đây là chính sách giả định của cửa hàng PowerTech:

1. Khách đổi ý chỉ đổi trả trong **7 ngày**, khi còn nguyên niêm phong; có thể thu phí xử lý (không đặt mức).
2. Đơn trả trước không thu đủ trong **24 giờ** thì hủy.
3. Khách **bỏ đơn từ lần thứ hai** chỉ bán khi trả trước.
4. Đặt cọc cho hàng đặt trước và máy lắp theo yêu cầu; mức cọc do hai bên thỏa thuận, không nêu tỷ lệ.
5. Hàng đã mở hộp, không lỗi, có thể bán lại giảm giá, do người quản lý quyết định.
6. Hạn đổi mới **30 ngày** (linh kiện) và **7 ngày** (laptop, màn hình) lấy theo GearVN; Hoàng Hà PC lại đổi mới 3 năm với CPU, 1 năm với RAM, nguồn, tản nhiệt, SSD, 6 tháng với bo mạch chủ, VGA, HDD. Chính sách mỗi cửa hàng khác nhau, nên chọn con số nào cũng là lựa chọn của PowerTech.

## 4. Chênh lệch giữa C và dữ liệu hiện có

`database/data.sql` có 36 bảng nhưng **không có** bảng riêng cho số seri từng chiếc, phiếu tiếp nhận bảo hành, hồ sơ đổi trả, đặt cọc và phân công giao hàng (chỉ có `Orders.DeliveryFailCount` và `OrderHistory`). Vì thế C mô tả nghiệp vụ rộng hơn CSDL hiện tại. Theo `README.md`, thiết kế đề xuất không bị giới hạn bởi cấu trúc cũ, nhưng cần ghi rõ phần nào là bổ sung.

Cần cập nhật theo C: danh sách thực thể trong `PowerTech-CSDL-NC.md` (đang bám A). Nếu giữ thu mua thiết bị cũ, đánh giá, hỗ trợ, ví như A thì phải đưa lại vào mô tả hoặc bỏ khỏi danh sách thực thể.

## 5. Nguồn đã đọc

- [GearVN – Chính sách bảo hành](https://gearvn.com/pages/chinh-sach-bao-hanh): điều kiện, từ chối bảo hành, thời gian xử lý, đổi mới 7 và 30 ngày, bảo hành tại hãng hoặc cửa hàng. Đọc ngày 18/10/2026.
- [Hoàng Hà PC – Chính sách hậu mãi](https://hoanghapc.vn/chinh-sach-bao-hanh): thời hạn đổi mới theo loại linh kiện, điều kiện và từ chối bảo hành, thời gian xử lý. Đọc ngày 18/10/2026.
- [Luật Bảo vệ quyền lợi người tiêu dùng 19/2023/QH15 (caselaw.vn)](https://caselaw.vn/van-ban-phap-luat/411464-luat-bao-ve-quyen-loi-nguoi-tieu-dung-so-19-2023-qh15-ngay-20-06-2023-cua-quoc-hoi): Điều 29, 30, 37, 38. Hiệu lực từ 1/7/2024. Chỉ đọc đến khoảng 100.000 ký tự đầu; đây là trang tổng hợp, không phải bản gốc của cơ quan nhà nước.
- [Phong Vũ – Chính sách mua linh kiện khi build PC](https://phongvu.vn/cong-nghe/chinh-sach-mua-linh-kien-khi-build-pc-tai-phong-vu/): một số linh kiện (RAM, SSD, CPU Intel) chỉ bán kèm dịch vụ build PC; không nêu đặt cọc, bảo hành.
- Kết quả tìm kiếm về Nghị định 70/2025/NĐ-CP (MISA, Sapo): hóa đơn điện tử từ máy tính tiền từ 1/6/2025. **Chưa đối chiếu văn bản gốc.**

**Chưa tìm được nguồn cho:** chính sách đặt cọc của cửa hàng linh kiện Việt Nam (tìm kiếm không trả về trang chính sách nào); chính sách đổi trả hàng không lỗi của Phong Vũ và GearVN cho linh kiện mới; chính sách trả hàng khi mua qua mạng của từng cửa hàng.

## 6. Việc cần quyết định

1. Giữ hay khôi phục các phần A có mà B và C bỏ: **đánh giá sản phẩm, hồ sơ hỗ trợ, thu mua thiết bị cũ, ví, thông báo**. C đặt vào loại trừ; nếu giữ thì cần viết lại mục 1.2.
2. Có nhận **lắp ráp theo cấu hình** là một hoạt động không? C ghi đặt cọc cho máy lắp theo yêu cầu nhưng loại trừ quy trình lắp ráp.
3. Có hỏi giảng viên về chính sách giả định ở mục 3 trước khi chốt các con số không.
4. Có cần xuất C sang `.docx`? Tôi chưa làm.


## 7. Các bản mô tả đã có và vai trò

| Nguồn | Nội dung | Dùng để |
|---|---|---|
| `PowerTech-CSDL-NC.docx` (bản nộp, đã chấm) | Phần "Mô tả" 15 đoạn viết theo quy tắc ràng buộc | Mốc **A**: cái giảng viên đã đọc |
| `Documents/Mo_ta_chi_tiet_de_tai_PowerTech.md` | Trùng văn bản với A (đã so từng đoạn: không đoạn nào khác), chỉ thêm tiêu đề và chú thích cuối | Không có thông tin mới |
| `Documents/Mo_ta_de_tai_PowerTech.md` | Bản thảo hướng cơ sở dữ liệu (26 quan hệ, định hướng cải tiến) | Chỉ tham khảo; không phải mô tả nghiệp vụ |
| `Documents/bao_cao_mo_ta_chi_tiet_cap_nhat.pdf` | Mô tả website cho môn Lập trình Web: chức năng theo vai trò, danh mục hàng, trạng thái đơn | Đối chiếu vai trò, danh mục, luồng đơn của website thật |
| [01_Mo_ta_de_tai.md](01_Mo_ta_de_tai.md) (**B**) | Bản viết lại sau nhận xét | Nguồn cho phần quầy, bảo hành, đổi trả |
| [01_Mo_ta_de_tai_v2.md](01_Mo_ta_de_tai_v2.md) (v2) | Sửa B cho thực tế | Nền cho v3 |
| [01_Mo_ta_de_tai_v3.md](01_Mo_ta_de_tai_v3.md) (**D**) | Bản chính thức | Dùng cho báo cáo |

## 8. Nhận xét của giảng viên được xử lý ở đâu trong v3

| Nhận xét | Mục trong v3 |
|---|---|
| **[GV, nhóm 6]** "Bổ sung hình thức mua trực tiếp tại cửa hàng" | 1.2.3 (6 bước, có kiểm tra tại chỗ, tem, hóa đơn); 1.2.2 (khách mua tại quầy); 1.1 |
| **[GV, nhóm 6]** "Cơ chế bảo hành... ra sao?" | 1.2.7 (8 bước: tiếp nhận, kiểm tra điều kiện, phiếu, gửi hãng, trả, tính lại hạn, đổi hoặc hoàn tiền) |
| **[GV, nhóm 6]** "Đổi hàng... ra sao?" | 1.2.8 (ba trường hợp, hồ sơ đổi trả, ba nhóm kho, hoàn tiền và đổi hàng) |
| Thanh toán bằng cách nào? (nhiều nhóm) | 1.2.3 bước 3, 1.2.5 |
| Có đặt cọc không? | 1.2.5 mục 3 |
| Trả, đổi, hủy, phí? | 1.2.6 mục 2 và 6, 1.2.8 |
| Ai kiểm tra, ai duyệt? | 1.2.2 (quản lý duyệt hoàn tiền, kiểm kê, bán lại hàng trả), 1.2.8 bước 4 và 5 |
| Chế tài khi bỏ đơn | 1.2.6 mục 5 |
| Con số giới hạn | 1.2.6 mục 5 (3 lần giao), 1.2.8 (48 giờ, 30 ngày, 7 ngày), 1.2.5 mục 2 (24 giờ) |
| Không đưa thuật ngữ CNTT, khóa, FK vào mô tả | Đã quét: không còn các từ "bảng", "khóa", "hệ thống", "giao diện", "nhấn", "đăng nhập", "cơ sở dữ liệu" |
| Giới hạn phạm vi | 1.3 |
| Kiểm tra thực tế Việt Nam | Hóa đơn, thời hạn bảo hành theo luật, quyền từ chối nhận hàng |
| Chưa làm ở mục này | Ba loại thực thể, ERD (mục 2, 6 của báo cáo) |

## 9. v3 sửa gì so với v2

| # | Điểm | v2 | v3 | Căn cứ |
|---|---|---|---|---|
| 1 | Chi phí bảo hành | Chỉ nói gửi qua đơn vị vận chuyển | Cửa hàng chịu chi phí sửa chữa và vận chuyển bảo hành | **[Nguồn]** Luật 19/2023, Điều 30 khoản 2 điểm e |
| 2 | Thời hạn bảo hành sau khi sửa | Không có | Thời gian ở bảo hành không tính vào hạn; thay linh kiện hoặc đổi mới thì tính lại | **[Nguồn]** Điều 30 khoản 2 điểm c |
| 3 | Trong lúc chờ bảo hành | Không có | Có thể cho mượn sản phẩm tương tự | **[Nguồn]** Điều 30 khoản 2 điểm d (cung cấp sản phẩm tạm hoặc cách giải quyết phù hợp) |
| 4 | Công bố chính sách | Không có | Chính sách bảo hành niêm yết tại quầy và trên trang web | **[Nguồn]** Điều 30 khoản 2 điểm a |
| 5 | Kênh đặt hàng | Quầy và trang web | Thêm điện thoại, tin nhắn (nhân viên lập đơn) | **[Nhận định]** thực tế cửa hàng linh kiện nhận đơn qua điện thoại; website thật chưa có |
| 6 | Hủy đơn của khách | Chỉ hủy do giao thất bại | Khách tự hủy khi chưa xác nhận | Mô tả website: "Hủy đơn hàng khi chưa xử lý" |
| 7 | Tình trạng đơn | Không liệt kê | Chờ xác nhận, đã xác nhận, đang chuẩn bị, đang giao, hoàn tất, đã hủy | Mô tả website, mục vai trò bán hàng |
| 8 | Tách mục | Thanh toán, giao hàng gộp trong 1.2.4 | Tách thành 1.2.4 (đặt hàng), 1.2.5 (thanh toán và cọc), 1.2.6 (giao hàng) | Dễ đọc, mỗi mục trả lời một nhóm câu hỏi |
| 9 | Đặt cọc | Hàng không có sẵn, máy lắp riêng | Thêm "một số mặt hàng giá trị lớn", cửa hàng công bố điều kiện cọc trước khi nhận | **[Nguồn]** GearVN: một số sản phẩm phải đặt cọc theo quy định |
| 10 | Cách trả tiền từ xa | Chuyển khoản, QR, ví điện tử, COD | Thêm cổng thanh toán trực tuyến; chuyển khoản do nhân viên đối chiếu | **[Nguồn]** GearVN liệt kê chuyển khoản, COD, MoMo, ZaloPay; dữ liệu thật có VNPay |
| 11 | COD tại quầy | Không nói | Ghi rõ COD không áp dụng tại quầy | **[Nhận định]**; dữ liệu thật có 3 đơn quầy ghi COD (xem mục 10) |
| 12 | Phí và thời gian giao | Biểu phí theo khu vực, giá trị đơn | Thêm đơn lớn nội thành thường miễn phí, giao nội thành 1–2 ngày làm việc | **[Nguồn]** GearVN: đơn từ 5 triệu miễn phí ở HCM, HN; 1–2 ngày nội thành |
| 13 | Nhận hàng | Khách kiểm tra, quay video | Thêm quyền từ chối nhận khi hộp rách, móp, ướt, mất niêm phong; đơn hoàn về kho và hủy | **[Nguồn]** GearVN, chính sách vận chuyển |
| 14 | Ba trường hợp đổi trả | Hai trường hợp (lỗi nhà sản xuất, khách đổi ý) | Thêm giao sai, thiếu, hư bên ngoài: báo trong 48 giờ | **[Nguồn]** GearVN: thông báo trong 48 giờ với thiếu phụ kiện, bể vỡ |
| 15 | Phần mềm bản quyền | Không nói | Đã kích hoạt thì không đổi trả; không có bảo hành phần cứng | **[Nhận định]**; dữ liệu thật có mặt hàng phần mềm với bảo hành 0 tháng |
| 16 | Thời hạn bảo hành | "12 đến 36 tháng, có dòng dài hơn" | 12–36 tháng phần lớn; RAM, ổ cứng 5 năm; nguồn đến 10 năm | Dữ liệu thật: 12, 18, 24, 36, 60, 120 tháng |
| 17 | Danh mục hàng | Liệt kê chung | Liệt kê đủ nhóm hàng của website: thêm loa, phần mềm bản quyền, phụ kiện | Dữ liệu thật có 17 loại hàng |
| 18 | Lắp ráp | Loại trừ cả quy trình | Cửa hàng hỗ trợ lắp ráp và chạy thử theo cấu hình khách chọn; bảo hành theo từng linh kiện; quy trình chi tiết vẫn loại trừ | **[Nguồn]** Phong Vũ bán một số linh kiện chỉ kèm dịch vụ build; việc không tính phí riêng là **[Nhận định]**, nên v3 không nêu |
| 19 | Số lượng ban đầu | Không nói | Kiểm kê đầu kỳ có biên bản | A có "tồn đầu có căn cứ kiểm kê"; dữ liệu thật có tồn đầu 100 không có trong sổ kho (báo cáo toàn vẹn) |
| 20 | Nhân viên kiêm nhiệm | Không nói | Một nhân viên thường kiêm nhiều việc | Mô tả website: mô hình nhiều vai trò, phù hợp cửa hàng nhỏ |
| 21 | Phạm vi loại trừ | Gồm "thu mua thiết bị cũ" | Thêm bán buôn, đánh giá sản phẩm và hỗ trợ ngoài bảo hành, đổi trả | Giữ phạm vi gọn theo nhận xét "giới hạn chức năng" |

## 10. Đối chiếu với dữ liệu thật của website (`database/data.seed.sql`)

Số liệu tổng hợp từ bản seed, không dùng thông tin cá nhân.

| Dữ liệu thật | v3 | Nhận xét |
|---|---|---|
| Phương thức thanh toán: chuyển khoản ngân hàng 12 đơn, COD 23, VNPay 1 | Tiền mặt, chuyển khoản, QR, thẻ ở quầy; chuyển khoản, ví, cổng thanh toán, COD từ xa | Khớp |
| 29 đơn trên web, 7 đơn quầy | Quầy và web (thêm điện thoại, tin nhắn) | Điện thoại, tin nhắn là bổ sung theo thực tế, dữ liệu chưa có |
| Phí giao bằng 0 ở cả 36 đơn | Biểu phí theo khu vực và giá trị; miễn phí nội thành đơn lớn | Dữ liệu không minh họa phí giao |
| **3 đơn quầy ghi COD** | COD không áp dụng tại quầy | **Trái thực tế.** Nên nêu trong báo cáo là sai lệch dữ liệu (ví dụ cho mục "dữ liệu không nhất quán") |
| Vai trò: Admin, Customer, SalesStaff, WarehouseStaff, SupportStaff, Shipper | Tư vấn bán hàng, thu ngân kiêm thủ quỹ, kỹ thuật, kho, giao hàng, chăm sóc khách hàng, quản lý | v3 thêm kỹ thuật và thu ngân kiêm thủ quỹ theo thực tế cửa hàng; hai vai trò này chưa có trong website |
| Loại hàng: 17 loại, không có loại cha | Loại hàng "có thể phân cấp" | Dữ liệu thật hiện không phân cấp; giữ vì cấu trúc cho phép |
| Mã giảm giá: một theo phần trăm, một theo số tiền; có đơn tối thiểu, giới hạn lượt | Mô tả đủ ba yếu tố | Khớp |
| Tình trạng đơn trong lịch sử: Pending, Processing, Shipping, Completed, Cancelled | Chờ xác nhận, đã xác nhận, đang chuẩn bị, đang giao, hoàn tất, đã hủy | Website mô tả sáu tình trạng, dữ liệu có năm giá trị; chưa đối chiếu từng chữ |

## 11. Nguồn thêm đã đọc trong lượt này

- [GearVN – Chính sách đổi trả](https://gearvn.com/pages/chinh-sach-doi-tra): báo trong 48 giờ khi thiếu phụ kiện hoặc bể vỡ; gửi trả trong 14 ngày; kiểm hàng khi nhận.
- [GearVN – Chính sách vận chuyển](https://gearvn.com/pages/chinh-sach-van-chuyen): phí giao, thời gian giao, quay video khui hàng, quyền từ chối khi hộp hư, liên lạc thêm ít nhất 2 lần khi giao thất bại.
- [GearVN – Hướng dẫn thanh toán](https://gearvn.com/pages/huong-dan-thanh-toan) (qua kết quả tìm kiếm, chưa mở toàn trang): chuyển khoản, trực tiếp, khi nhận hàng, MoMo, ZaloPay, quẹt thẻ tại showroom.
- [GearVN – Hướng dẫn trả góp](https://gearvn.com/pages/huong-dan-tra-gop) (qua kết quả tìm kiếm): một số sản phẩm phải đặt cọc theo quy định.
- Luật 19/2023/QH15, Điều 29 và 30 (qua caselaw.vn), đọc lại đoạn nói về chi phí vận chuyển bảo hành và tính lại thời hạn.

**Quy ước mới trong v3 chưa có nguồn xác minh:** quyền mượn sản phẩm trong lúc chờ bảo hành "nếu còn hàng"; đơn giá trị lớn nội thành "thường" miễn phí giao (GearVN chỉ là một ví dụ về mức 5 triệu); thông báo hư hỏng trong 48 giờ (mượn từ GearVN); kênh điện thoại, tin nhắn. Các quy ước cũ ở mục 3 vẫn áp dụng.
