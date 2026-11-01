# PowerTech — Đề tài học phần Cơ sở dữ liệu nâng cao

PowerTech là đề tài báo cáo học phần **Cơ sở dữ liệu nâng cao** của **Nhóm 6, lớp 23DTHD6** (Nguyễn Ngọc Tình – trưởng nhóm, Đỗ Thanh Hoàng Đức Nhả, Võ Thành Đông). Bối cảnh là cửa hàng bán lẻ thiết bị công nghệ, gồm bán tại quầy, bán trực tuyến, nhập kho, giao hàng, bảo hành, đổi trả, hỗ trợ khách và thu cũ đổi mới.

Mục tiêu là **áp dụng kiến thức môn học để phân tích, chuẩn hóa và cải tiến thiết kế CSDL của đề tài**, theo bài giảng, giáo trình và yêu cầu viết báo cáo của giảng viên. CSDL PowerTech hiện tại là điểm xuất phát và nguồn dữ liệu thực tế; thiết kế đề xuất có thể kế thừa, điều chỉnh hoặc thiết kế lại khi có căn cứ nghiệp vụ và lý thuyết.

Trọng tâm là **dữ liệu, mô hình, thiết kế và cấu trúc CSDL**. Mã ứng dụng, giao diện và việc chạy website chỉ được khảo sát khi một yêu cầu cụ thể cần đến.

Đọc file này để nắm các thư mục và nguồn tài liệu. Đọc [AGENTS.md](AGENTS.md) để biết cách làm việc trong từng phiên.

## 1. Bản đồ thư mục

```
PowerTech/
├── README.md, AGENTS.md
├── bao-cao/                  Tài liệu báo cáo của nhóm tôi
├── CSDL-NC/                  Tài liệu môn học
│   ├── yeu-cau-giang-vien/   Cách viết báo cáo, nhận xét của giảng viên, kinh nghiệm rút ra
│   ├── bai-giang/            Bài giảng của giảng viên (đổi theo từng buổi học)
│   ├── giao-trinh/           Giáo trình và tài liệu bổ sung, nơi tra cứu khái niệm
│   └── bao-cao-mau/          Báo cáo của nhóm khác hoặc khóa trước, để tham khảo
├── database/                 Cấu trúc và dữ liệu CSDL PowerTech (tham khảo)
├── Documents/                Báo cáo mô tả và phân tích PowerTech đã có
└── PowerTech/, PowerTech.slnx  Mã ứng dụng web (ngoài trọng tâm)
```

### `bao-cao/` — báo cáo của nhóm

Mọi tài liệu của báo cáo nhóm nằm ở đây: bản nháp từng mục, sơ đồ, SQL đề xuất, các quyết định.

| File | Nội dung |
|---|---|
| [01_Mo_ta_de_tai.md](bao-cao/01_Mo_ta_de_tai.md) (+ `.docx`) | Mục 1: mô tả đề tài bằng văn xuôi nghiệp vụ, đã bổ sung bán tại quầy, bảo hành, đổi trả. |
| [PowerTech-CSDL-NC.md](bao-cao/PowerTech-CSDL-NC.md) | Phân loại ba nhóm thực thể (mục 2), đã cập nhật theo v2. Phần "Mô tả" trong file là bản nộp đầu. Bản nộp đầu nguyên văn: `PowerTech-CSDL-NC_ban_nop.md`; `.docx` cùng tên vẫn là bản nộp đầu, chưa cập nhật. |
| [01_Mo_ta_de_tai_v3.md](bao-cao/01_Mo_ta_de_tai_v3.md) (+ `.docx`) | **Mục 1 chính thức (v3)**, sát thực tế một cửa hàng linh kiện. `01_Mo_ta_de_tai.md` và `_v2` giữ làm tham chiếu. |
| [02_Xac_dinh_thuc_the.md](bao-cao/02_Xac_dinh_thuc_the.md) | **Mục 2 chính thức:** 30 thực thể (6 cơ bản, 4 đối tượng ngoài, 20 nghiệp vụ) và 8 mối kết hợp, thuộc tính chi tiết, đối chiếu với DDL. Thay phần thực thể trong `PowerTech-CSDL-NC.md`. |
| [03_Phu_thuoc_ham.md](bao-cao/03_Phu_thuoc_ham.md) | **Mục 3:** tân từ và tập phụ thuộc hàm của 5 quan hệ cơ bản, 4 đối tượng ngoài, 8 nghiệp vụ phân tích sâu; F ngắn gọn cho phần còn lại; các PTH bị loại và vì sao; PTH sinh từ cột dẫn xuất. |
| [04_Phu_toi_thieu.md](bao-cao/04_Phu_toi_thieu.md) | **Mục 4:** phủ tối thiểu 3 bước cho 11 quan hệ có F nhiều hơn một PTH (2 quan hệ có PTH dư thừa: HANGCOSERI, PHIEUBAOHANH) và tóm tắt 26 quan hệ còn lại. Đối chiếu bằng `bao-cao/tools/mincover.py`. |
| [05_Tim_khoa.md](bao-cao/05_Tim_khoa.md) | **Mục 5:** tìm khóa bằng thuật toán N, M, D với bảng tổ hợp (HANGCOSERI 4 khóa, ANHMATHANG 3, 8 quan hệ 2 khóa), chọn khóa chính; hệ quả cho dạng chuẩn. Đối chiếu bằng `bao-cao/tools/timkhoa.py`. |
| [06_ERD.md](bao-cao/06_ERD.md) | **Mục 6:** ERD với bản số (min,max): 53 mối kết hợp, 8 MKH có thuộc tính, mã Mermaid (toàn cảnh và 5 sơ đồ nhóm, đã kiểm tra dựng được), ràng buộc không vẽ được bằng bản số, đối chiếu khóa ngoại trong DDL. |
| [07_Mo_hinh_quan_he.md](bao-cao/07_Mo_hinh_quan_he.md) | **Mục 7:** chuyển ERD sang 38 quan hệ (PK gạch liền, FK gạch đứt), 71 khóa ngoại, bảng mô tả thuộc tính, UNIQUE, CHECK, thuộc tính dư thừa cần cải tiến. |
| [08_Dang_chuan.md](bao-cao/08_Dang_chuan.md) | **Mục 8:** dạng chuẩn 38 quan hệ theo mọi khóa ứng viên (35 BCNF; HANGCOSERI 3NF, PHIEUBAOHANH 2NF, CHITIETTRA 1NF); dạng chuẩn chung = 1NF; kịch bản khi giả thiết đổi. Đối chiếu bằng `bao-cao/tools/dangchuan.py`. |
| [09_Cai_tien.md](bao-cao/09_Cai_tien.md) | **Mục 9:** cải tiến ba quan hệ (CHITIETTRA, PHIEUBAOHANH, HANGCOSERI) bằng phân rã/tổng hợp; tableau bảo toàn thông tin và kiểm tra bảo toàn PTH; lược đồ 39 quan hệ đạt BCNF (thêm SERIMATHANG); tình huống 4NF ảnh – thông số (3.256 so với 1.538 dòng). Đối chiếu bằng `bao-cao/tools/phanra.py`. |
| [10_Do_thi_truy_xuat.md](bao-cao/10_Do_thi_truy_xuat.md) | **Mục 10:** đồ thị quan hệ (thuật toán B1–B7 Bài 10: 38 nút, 65 cung, 1 nút bản lề BL(MaHS, MaSeri), 1 cung vô hướng), đồ thị con đường truy xuất với (m, A, M), 7 yêu cầu khai thác K1–K7 kèm SQL, 8 ràng buộc từ mạch đi kép, chỉ mục đề xuất. Tính bằng `bao-cao/tools/dothi.py` (dữ liệu `luoc_do_39.py`); SQL ở `bao-cao/sql/10_truy_van_va_chi_muc.sql`. |
| [PowerTech_CSDLNC_Bao_cao.docx](bao-cao/PowerTech_CSDLNC_Bao_cao.docx) | **Bản nộp:** ghép mục 1–10 (bìa, mục lục, danh mục hình và bảng, 172 bảng, 13 sơ đồ; khóa chính gạch liền, khóa ngoại gạch đứt). Sinh bằng `bao-cao/tools/ghep_docx.py`; ảnh sơ đồ ở `bao-cao/hinh/`. Mở trong Word và cập nhật trường (F9) để có số trang mục lục. Bỏ các phần ôn tập "Câu hỏi giảng viên có thể hỏi". |
| [01_doi_chieu_mo_ta.md](bao-cao/01_doi_chieu_mo_ta.md) | So sánh bản nộp đầu, `01_Mo_ta_de_tai.md`, v2 và v3; nhận xét giảng viên nằm ở đâu; căn cứ thực tế và các quy ước tự đặt. |
| [QUYET_DINH.md](bao-cao/QUYET_DINH.md) | Khung các mục báo cáo, nguyên tắc viết và các điều cần tránh. Cập nhật khi có quyết định mới. |

### `CSDL-NC/yeu-cau-giang-vien/` — cách viết và nhận xét của giảng viên

| File | Dùng để |
|---|---|
| [Cau truc bao cao mon CSDL Nang cao.md](<CSDL-NC/yeu-cau-giang-vien/Cau truc bao cao mon CSDL Nang cao.md>) (+ `.pptx`) | Đề cương bài tập lớn, 7 nội dung báo cáo phải có. Đây là yêu cầu chính, mới nhất, ưu tiên cao nhất. |
| [Huong_dan_cach_viet_bao_cao_CSDLNC.md](CSDL-NC/yeu-cau-giang-vien/Huong_dan_cach_viet_bao_cao_CSDLNC.md) (+ `.docx`) | Hướng dẫn cách viết báo cáo, bổ sung cho đề cương; khi khác nhau thì theo đề cương. |
| [23DTHD5.xlsx - Sheet1.md](<CSDL-NC/yeu-cau-giang-vien/23DTHD5.xlsx - Sheet1.md>) (+ `.csv`) | Danh sách nhóm, điểm và nhận xét của giảng viên cho lớp D5. |
| [23DTHD6.xlsx - Sheet1.md](<CSDL-NC/yeu-cau-giang-vien/23DTHD6.xlsx - Sheet1.md>) (+ `.csv`) | Như trên cho lớp D6, trong đó có nhận xét cho nhóm 6 (PowerTech). |
| [00_kinh_nghiem_viet_mo_ta_tu_D5_D6.md](CSDL-NC/yeu-cau-giang-vien/00_kinh_nghiem_viet_mo_ta_tu_D5_D6.md) | Kinh nghiệm viết rút ra từ các nhận xét trên và từ các báo cáo mẫu. Không phải quy định chính thức. |

Đọc các file nhận xét để học từ lỗi của các nhóm khác (nhầm thực thể với mối kết hợp, mô tả lẫn thuật ngữ CNTT, phạm vi quá rộng...) trước khi viết mục mới.

### `CSDL-NC/bai-giang/` — bài giảng

Bài giảng của giảng viên, gồm `.docx` và bản `.md` chuyển bằng markitdown. **Thay file mới sau mỗi buổi học** (tên có ngày, ví dụ `Bai giang CSDLNC-18-10`). Bản có ngày mới nhất là bản hiện hành. Đây là nguồn chuẩn về nội dung, thuật ngữ và cách trình bày.

### `CSDL-NC/giao-trinh/` — giáo trình và tài liệu bổ sung

Nơi tra cứu khi cần làm rõ một khái niệm hoặc chưa chắc một phần lý thuyết.

| Tài liệu | Dùng khi |
|---|---|
| [CSDL-NC-2015.md](CSDL-NC/giao-trinh/CSDL-NC-2015.md) | Lý thuyết quan hệ, phụ thuộc hàm, chuẩn hóa, phân rã, thuật toán tổng hợp, đồ thị quan hệ và con đường truy xuất (Bài 9–11). File lớn, tìm theo từ khóa. |
| [TH_PTTKHT_2022.md](CSDL-NC/giao-trinh/TH_PTTKHT_2022.md) | Phân tích hệ thống, mô hình quan niệm, ERD, bản số, chuyển ERD sang quan hệ. |
| [Dạng chuẩn 4.md](<CSDL-NC/giao-trinh/Dạng chuẩn 4.md>) | Phụ thuộc đa trị và 4NF. |
| `cos135-…`, `cos323-…`, `Thuc Hanh Quan Tri Co So Du Lieu` (`.md` và `.pdf`) | SQL, ràng buộc toàn vẹn, chỉ mục, quản trị CSDL. |

### `CSDL-NC/bao-cao-mau/` — báo cáo mẫu

- `BaoCaoCSDLNC_ThamKhao` (`.md`, `.docx`): báo cáo hoàn chỉnh thầy gửi làm mẫu, đề tài HUTECH Classroom, khung 4 chương. Bản `.docx` trùng với bản trong `yeu-cau-giang-vien/`.
- `D5/` và `D6/`: báo cáo ban đầu của các nhóm hai lớp (8 của D5, 3 của D6), mức điểm ở file nhận xét là 6–7.

Chỉ tham khảo bố cục, mức chi tiết và cách trình bày. Kết luận trong các báo cáo này có thể sai, và không được chép câu chữ.

### `database/` — cấu trúc CSDL của dự án (tham khảo)

| Nguồn | Vai trò |
|---|---|
| [data.sql](database/data.sql) | Bản xuất SQL Server gốc: DDL, dữ liệu, khóa, chỉ mục, ràng buộc, view, thủ tục. Tên database bên trong là `TechZoneStoreDb`. Nguồn sự thật về cấu trúc triển khai. |
| [data.seed.sql](database/data.seed.sql) | Cùng cấu trúc, đã thay một phần thông tin cá nhân. Dùng khi lấy ví dụ dữ liệu cho báo cáo. |
| [erd.md](database/erd.md) | ERD Mermaid sinh từ DDL: toàn cảnh và năm nhóm bảng. |
| [data-integrity-report.md](database/data-integrity-report.md) | Kết quả đối soát dữ liệu có sẵn; tái kiểm tra trước khi trích dẫn. |
| [fixes/001_fix_data_issues.sql](database/fixes/001_fix_data_issues.sql) | Bản vá tham khảo. Mặc định `@Commit = 0`, cuối script hoàn tác. |
| `tools/` | Script phân tích INSERT, đối soát, tạo seed, sinh ERD. Một số script ghi file; đọc trước khi chạy. Hướng dẫn ở [database/README.md](database/README.md). |

### `Documents/` — tài liệu mô tả PowerTech

Các báo cáo mô tả, phân tích thiết kế dữ liệu và bản nháp thực thể/phụ thuộc hàm đã làm trước. Dùng để hiểu ngữ nghĩa và ý định thiết kế; các phiên bản khác nhau về phạm vi nên cần chỉ rõ đang dựa trên bản nào. Khi mâu thuẫn với SQL, SQL là hiện trạng triển khai.

## 2. Hiểu biết đã xác minh về CSDL

Mốc đối chiếu **05/10/2026**; kiểm tra lại khi SQL thay đổi.

- DDL có **36 bảng, 44 FK, 35 CHECK, 59 DEFAULT, 18 view, 15 thủ tục báo cáo**; không có trigger hoặc function. Hai bản SQL cùng DDL.
- 61 chỉ mục nonclustered, 22 unique (bảy unique có điều kiện lọc).
- 2.757 bản ghi: 134 sản phẩm, 36 đơn hàng, 51 dòng đơn, 7 phiếu nhập, 273 giao dịch kho.
- `__EFMigrationsHistory` và các bảng Identity phụ là bảng kỹ thuật, tách khỏi mô hình nghiệp vụ.
- Seed thay 134 dòng thuộc bảy bảng, giữ nguyên cấu trúc và các sai lệch nghiệp vụ.

| Nhóm | Quan hệ tiêu biểu |
|---|---|
| Tài khoản và phân quyền | `AspNetUsers`, `AspNetRoles`, `AspNetUserRoles`, `UserAddresses` |
| Sản phẩm và thông số | `Categories`, `Brands`, `Products`, `ProductImages`, `SpecificationDefinitions`, `ProductSpecifications` |
| Bán hàng và thanh toán | `Carts`, `CartItems`, `Orders`, `OrderItems`, `Payments`, `OrderHistory`, `Coupons` |
| Nhập hàng và tồn | `Suppliers`, `PurchaseReceipts`, `PurchaseReceiptItems`, `StockTransactions` |
| Đánh giá, hỗ trợ, thu cũ | `Reviews`, `ReviewImages`, `SupportTickets`, `TicketResponses`, các bảng FAQ, `TradeInRequests` |

Người dùng có thể có nhiều vai trò nhưng mẫu chưa có người đa vai trò. Tồn lưu tổng theo sản phẩm, chưa theo kho. Chứng từ có các cột lưu giá trị tại thời điểm giao dịch, cần phân biệt với thông tin hiện tại.

## 3. Sai lệch dữ liệu làm căn cứ nghiên cứu

| Phát hiện | Ý nghĩa phân tích |
|---|---|
| 134/134 sản phẩm có tồn khác tổng nhập−xuất; 132/134 khác số dư cuối sổ kho; bốn chỗ đứt chuỗi | Cần xác định tồn đầu, nguồn số dư và quy tắc ghi giao dịch kho. |
| Tổng `SoldQuantity` là 163, đơn Completed bán 158; năm sản phẩm bị ảnh hưởng bởi đơn hủy | Phải thống nhất định nghĩa lượng đã bán và quan hệ với tồn kho. |
| Một phiếu nhập lệch tổng chi tiết 3.518.000 đồng | Ví dụ ràng buộc tổng hợp giữa đầu phiếu và dòng. |
| 34 đơn ghi Paid nhưng `Payments` rỗng | Trạng thái thanh toán và chứng từ thanh toán chưa nhất quán. |
| 11 đơn thiếu lịch sử, một đơn có trạng thái cuối không khớp | Phân biệt trạng thái hiện tại, lịch sử thật và lịch sử suy dựng. |
| `vw_AdminDashboard_TopCategories` và `TopBrands` cộng tồn sau nối với nhiều dòng đơn | Tồn bị cộng lặp: CPU cho 1.587 thay vì 1.032. |

Bản vá hiện có chưa giải quyết hết các điểm trên: nó tính lượng đã bán theo đơn khác Cancelled/Returned, không sửa tồn tương ứng, và lịch sử bổ sung là dữ liệu suy dựng.

## 4. Phạm vi phân tích sâu (đề xuất)

**Sản phẩm–thông số–ảnh**, **đơn hàng–chi tiết–thanh toán** và **phiếu nhập–chi tiết–sổ kho**. Đây là định hướng nghiên cứu, giảng viên chưa phê duyệt phạm vi.
