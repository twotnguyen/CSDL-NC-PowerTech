# QUYẾT ĐỊNH CỦA BÁO CÁO MỚI (bao-cao-moi)

Ghi ngày 24/10/2026. Báo cáo cũ ở `../bao-cao/` giữ nguyên làm tham khảo.

## 1. Căn cứ

- Yêu cầu mới nhất của thầy Khang: `CSDL-NC/yeu-cau-giang-vien/Cau truc bao cao mon CSDL Nang cao.md` (7 nội dung).
- Cấu trúc trình bày theo `CSDL-NC/bao-cao-mau/BaoCaoCSDLNC_ThamKhao.md`: 4 chương (Tổng quan và mô tả; Thiết kế và chuẩn hóa; Kết quả thực nghiệm; Kết luận), có khảo sát, tính khả thi, mục tiêu, mô tả nghiệp vụ, ERD, quan hệ, PTH, khóa, dạng chuẩn, đồ thị, SQL.
- Ký hiệu, thuật toán: giáo trình CSDL-NC-2015 và bài giảng 18/10/2026 (đã kiểm tra lại các chỗ bài giảng sai, xem `01_ghi_chu_bai_giang_18_10.md`).
- **Phạm vi nguồn tài liệu:** Chỉ truy xuất trong thư mục dự án `PowerTech/CSDL-NC/`; bỏ qua hoàn toàn và không quét thư mục ngoài `~/Documents/CSDL-NC/`.

## 2. Các quyết định đã chọn (mặc định, Twot có thể đổi)

| # | Quyết định | Lý do |
|---|---|---|
| D1 | Phạm vi 31 quan hệ ban đầu (32 sau cải tiến), thay cho 38–39 bảng của bản cũ (cập nhật 25/10/2026: từ 24 lên 31 khi thêm kênh online và nhân sự, hướng A+) | Đủ để làm tay từng bước (phủ tối thiểu, khóa N/TG/D, chuẩn hóa) mà vẫn bao phủ bán tại quầy và trên trang web, thanh toán, giao hàng, nhập kho, đổi trả, bảo hành, nhân sự và truy trách nhiệm |
| D2 | Ngoài phạm vi (nêu ở 1.3): kiểm kê và điều chỉnh tồn, giữ hàng, đánh giá, phiếu hỗ trợ/chat/FAQ, thu cũ đổi mới, ví, thông báo, thống kê, cảnh báo tồn tối thiểu, trả góp, nhiều showroom, chấm công/lương/tuyển dụng. **Đã đưa vào** (25/10/2026): tài khoản, giỏ hàng, sổ địa chỉ, vai trò, giữ vai trò, nhật ký đơn | Giữ hẹp nhưng đủ kênh online như GearVN; theo yêu cầu của Twot |
| D3 | Lược đồ ban đầu **cố ý giữ** vài cột tra cứu dư (MaSP ở HANGCOSERI, PHIEUBAOHANH; MaDH ở CHITIETTRA) và họ tên gộp một cột | Để các mức 1NF–3NF và phân rã/tổng hợp được thể hiện bằng ví dụ thật; ghi rõ là hiện trạng cần cải tiến |
| D4 | Tách HoTen thành HoLot + Ten khi cải tiến (giả thiết G3) | Theo bài giảng: họ tên là thuộc tính kép, vi phạm DC1 |
| D5 | Phương án cải tiến chọn: tách bốn thành phần cho HANGCOSERI (giữ cả bảo toàn thông tin lẫn PTH); phương án Delobel đơn giản bị loại vì mất PTH | Đã chứng minh bằng bảng a/b và kiểm tra F' ≡ F |
| D6 | Khách hàng là thực thể đối tượng ngoài; thuộc tính đặt hậu tố (HoTenKH, HoTenNV…) để không trùng tên giữa các quan hệ | Tránh lỗi trùng thuộc tính khi tính bao đóng |
| D7 | Khóa chính làm khóa ưu tiên khi vẽ đồ thị (Q1); khóa ngoại tới NHANVIEN ngoài khóa chính giữ làm cung vai trò (Q2) | Giáo trình 10.4 cho phép nhiều đồ thị |
| D8 | Viết SQL cho **tất cả** 65 con đường truy xuất + 9 truy vấn khai thác (K6–K9 mới: truy trách nhiệm, giỏ hàng), chạy thử trên SQLite có bật khóa ngoại; 1 đường rỗng đúng quy tắc (giỏ → tài khoản → nhân viên) | Yêu cầu 7 của đề cương |
| D9 | Mô tả nghiệp vụ 1.4 viết thuần đời sống, không có tên bảng/khóa | AGENTS.md mục 5.1 và nhận xét D5/D6 |

## 3. Giả thiết nghiệp vụ (ghi "giả thiết" trong báo cáo)

- G1: số seri duy nhất trong cùng một mặt hàng.
- G2: mỗi dòng đơn và mỗi dòng phiếu nhập chỉ một mặt hàng.
- G3: họ tên gồm họ lót và tên (quy ước nhập liệu).
- G4: PTH có vế trái có thể NULL chỉ xét trên các bộ khác NULL (HANGCOSERI, PHIEUBAOHANH, TAIKHOAN).
- G5: SKU, SoDH, SoPhieu, CodeMG, TenDangNhap, TenVT duy nhất; mỗi đơn tối đa một phiếu giao.
- G6: mỗi tài khoản thuộc đúng một khách hoặc một nhân viên; mỗi khách và mỗi nhân viên tối đa một tài khoản; quyền của nhân viên là quyền của các vai trò đang giữ. Mọi quy tắc "đúng vai trò mới được làm khâu đó" là giả thiết của nhóm.

## 4. Cần Twot xác nhận / hỏi thầy

1. Có chấp nhận phạm vi 24 quan hệ không, hay muốn mở rộng thêm (giỏ hàng, đánh giá)?
2. Tên giảng viên hướng dẫn ở trang bìa ("ThS. Võ Hoàng Khang") và thông tin thành viên nhóm cần đối chiếu lại.
3. Hỏi thầy: lược đồ ban đầu có được cố ý thiết kế chưa đạt chuẩn để minh họa không; 4NF cần chứng minh tổng quát hay một tình huống là đủ.
4. Dữ liệu minh họa là dữ liệu tự tạo (không phải dữ liệu seed thật), riêng số dòng ảnh – thông số ở mục 2.3.8 lấy từ seed.

## 5. Chưa làm / chưa kiểm chứng

- Bản in A4: đã xuất PDF bằng Word trên máy này và xem lại các trang chính (bìa, mục lục, ERD, bảng, SQL). Chưa xem từng trang trong số 105 trang; trước khi in nên cuộn qua một lượt.
- Lời cam đoan ở phần đầu là văn mẫu: Twot phải đọc và tự chịu trách nhiệm.
- Chưa commit gì; commit/push do Twot làm.

## 6. Cấu hình in A4 (ghi 25/10/2026)

- Khổ A4 dọc, lề trái 3 cm, các lề còn lại 2 cm; chữ Times New Roman 13 pt; bảng 9–10 pt; mã SQL 9 pt.
- Mọi hình nằm gọn trong một trang A4 dọc (tối đa 16 × 21 cm, kèm chú thích); không còn trang ngang. Để chữ vẫn ≥ 7 pt khi in: ERD tổng quát chỉ còn thực thể và đường nối (tên mối kết hợp và bản số nằm ở các hình nhóm); ERD chia thành 5 hình nhóm (nhóm "Đổi trả, hoàn tiền và bảo hành" tách làm "Đổi trả và hoàn tiền" và "Bảo hành"); đồ thị quan hệ dùng nút hình chữ nhật bo góc.
- Ô bảng ngắn (≤ 12 ký tự) không xuống dòng ("11 → 10", "siêu khóa").
- Mục lục, danh mục hình/bảng là trường Word: mở docx, chọn "Yes" khi Word hỏi cập nhật trường để số trang khớp.

## 7. Cập nhật 25/10/2026: kênh online, nhân sự và truy trách nhiệm (hướng A+)

Theo yêu cầu của Twot (làm đề tài như một cửa hàng linh kiện thật có cả quầy và trang web, ví dụ GearVN; có quản lý nhân sự và biết ai làm/duyệt từng khâu). Đối chiếu nguồn: `04_doi_chieu_mo_ta_voi_cac_tai_lieu.md`.

- **Thêm 7 quan hệ:** TAIKHOAN, DIACHIKHACH, VAITRO, GIUVAITRO, GIOHANG, CHITIETGIOHANG, NHATKYDONHANG (31 quan hệ ban đầu; 32 sau cải tiến).
- **Thêm cột truy trách nhiệm:** MAGIAMGIA.MaNV (người tạo mã); THANHTOAN.MaNVThu; PHIEUNHAP.MaNVXacNhan, ThoiDiemXacNhan; LANNHANLAI.MaNVDuyet; KHOANHOAN.MaNVChi; NHANVIEN thêm EmailNV, NgayVaoLam, NgayNghiViec. DONHANG.MaNV cho phép rỗng (đơn khách tự đặt trên web).
- **Sửa hai chỗ mâu thuẫn của bản trước:** bỏ "cộng số dư" ở hoàn tiền (không có ví) và bỏ "điều chỉnh" khỏi biến động kho và nhiệm vụ người quản lý (kiểm kê nằm ngoài phạm vi).
- **Mô tả 1.4 đánh số lại:** 1.4.2 khách – tài khoản – địa chỉ; 1.4.3 nhân viên – vai trò – trách nhiệm (mới); 1.4.4 quầy; 1.4.5 trang web; 1.4.6 thanh toán; 1.4.7 nhập hàng; 1.4.8 đổi trả; 1.4.9 bảo hành.
- **Vai trò (8):** Quản trị, Quản lý, Bán hàng, Thu ngân, Kỹ thuật, Kho, Giao hàng, Chăm sóc khách hàng. Tương ứng web: Admin, SalesStaff, WarehouseStaff, SupportStaff, Shipper.
- **TAIKHOAN xếp "đối tượng ngoài"** (hồ sơ truy cập), GIOHANG xếp "nghiệp vụ"; ghi lý do ở 1.6.5.
- **Đồ thị:** khóa ngoại phụ tới NHANVIEN (tên khác MaNV) không vẽ thành cung riêng; truy xuất bằng truy vấn K7. Kết quả: 31 nút, 48 cung, 12 nút vào, 65 đường.
- **Kiểm tra độc lập (bằng vét cạn, không dùng fd.py):** khóa và BCNF của 32 quan hệ khớp; khóa ngoại trỏ đúng khóa của quan hệ cha; dữ liệu minh họa không vi phạm PTH đã khai báo.
- **ERD:** 9 hình (1 tổng quát chỉ còn thực thể và đường nối, 8 hình nhóm). Hình tổng quát chữ khoảng 6,5 pt khi in A4, nhỏ nhất trong các hình.
- **Chương 4 sinh tự động** từ lược đồ (`tools/gen_chuong4.py`) để số liệu không lệch.
- **Hạn chế mới:** quy tắc vai trò – khâu chỉ cưỡng chế được khi ghi dữ liệu; DONHANG.TinhTrangDH là bản sao của dòng nhật ký mới nhất.

## 8. Hình vẽ (cập nhật 25/10/2026)

- Danh mục hình tăng từ 10 lên **32** (theo `BaoCaoCSDLNC_ThamKhao.docx`, vốn có ERD, sơ đồ quan hệ dạng bảng, use case, đồ thị): ERD tổng quát + 8 hình nhóm (1.1–1.9); 6 use case (1.10–1.15); 4 lưu đồ nghiệp vụ (1.16–1.19); 7 sơ đồ quan hệ dạng bảng (2.1–2.7); 4 sơ đồ phân rã (2.8–2.11); đồ thị quan hệ dạng số nút và dạng có tên (3.1–3.2).
- Không vẽ sơ đồ lớp (Class Diagram) của báo cáo mẫu: đề tài chỉ xét cơ sở dữ liệu, sơ đồ quan hệ dạng bảng thay vai trò đó.
- ERD vẽ bằng `tools/ve_erd.py` với bố cục đặt tay ở `tools/bo_cuc_erd.py` (đổi vị trí ở đó); mỗi hình nằm gọn một trang A4 dọc. Chữ nhỏ nhất ≈ 5–7 pt ở ERD tổng quát và Hình 1.3; các hình còn lại ≥ 7 pt.
- Chạy `python3 tools/chay_het.py` vẽ lại tất cả hình, sinh chương rồi ghép docx.

## 9. Viết lại Chương 1 theo báo cáo mẫu (30/10/2026)

- **Nguồn chính của Chương 1 là `chuong_docx/Chuong1_Tong_quan.docx`** (Twot chọn sửa trong Word). `tools/gen_chuong1.py` và `chuong/01_chuong1.md` là bản cũ; chạy `chay_het.py` hoặc `tach_chuong_docx.py` sẽ ghi đè bản viết lại. Bản gốc trước khi sửa: `chuong_docx/_sao_luu/Chuong1_Tong_quan.goc.docx`.
- Lấy hình thức của `BaoCaoCSDLNC_ThamKhao`: 1.1 bốn đoạn văn xuôi; 1.2 câu dẫn + 5 mục "Về mặt…" + đoạn kết; 1.3 ba danh sách tổ chức; 1.4 không chia tiểu mục, mỗi thực thể một đoạn "Đối với việc quản lý X…"; 1.5 danh sách 7 nội dung; 1.6 danh sách `TENBANG(khóa, thuộc tính…)` theo ba loại; 1.7 giữ bảng bản số và 9 hình ERD (chú thích hình giữ kiểu Caption có trường SEQ để mục lục hình hoạt động). Định dạng thân văn bản: thụt đầu dòng 1 cm, giãn dòng 1,5, sau đoạn 0.
- **Use case và lưu đồ (1.8, 1.9 cũ) chuyển sang `chuong_docx/_cho_chuong2/UseCase_va_LuuDo.docx`** để đưa vào Chương 2 khi viết lại chương đó (như mẫu). Số hình đánh lại lúc đó (hiện Chương 1 còn Hình 1.1–1.9, Bảng 1.1).
- **Con số chính sách** (hủy đơn 24 giờ, đặt cọc, phí xử lý, đổi trả 48 giờ / 30 ngày / 7 ngày, quy tắc bảo hành 3 lần, hẹn trả 7–30 ngày) ghi là "do nhóm đề xuất"; chỉ "giao tối đa 3 lần" khớp website PowerTech. Chưa đối chiếu GearVN. Các con số bảo hành 12–36 tháng, 5 năm, 10 năm bị bỏ khỏi 1.1.
- **Họ tên** khách và nhân viên vẫn là một thuộc tính (HoTenKH, HoTenNV) ở Chương 1; tách ở Chương 2 (D4, G3).
- **Chưa làm:** định dạng theo mẫu cho Chương 2–4; lề dưới 2,5 cm (lề nằm ở file nền khi ghép, không ở file chương); đối chiếu thuộc tính ở 1.6 với Chương 2; mở file ghép trong Word để xem trang.

### 9.1 Chuyển NHATKYDONHANG và LANGIAO thành mối kết hợp (30/10/2026)

- **Lý do:** thầy nhận xét `LichSu…` là thống kê hoặc mối kết hợp, không phải thực thể (D5/g9, D6/g1); giáo trình 13.2.3 yêu cầu thực thể tồn tại độc lập, thuộc tính không chứa khóa của thực thể khác. Hai bảng này có khóa dạng *khóa cha + số đếm* (MaDH, SoLanDoi; MaGiao, SoLan), cùng cấu trúc với dòng chi tiết đã xếp là mối kết hợp.
- **NHATKYDONHANG:** mối kết hợp DONHANG (1,n) – NHANVIEN (0,n); giữ nguyên cột.
- **LANGIAO:** thêm cột `MaNV` (NOT NULL, nhân viên giao hàng thực hiện lần đó) để có hai đầu: PHIEUGIAO (0,3) – NHANVIEN (0,n). PHIEUGIAO.MaNV là người phụ trách phiếu, có thể khác người đi giao một lần cụ thể.
- **Kết quả:** 23 thực thể (6 cơ bản, 5 đối tượng ngoài, 12 nghiệp vụ), 8 mối kết hợp có thuộc tính, 39 mối kết hợp khóa ngoại; vẫn 31 quan hệ. Đồ thị quan hệ 31 nút, 49 cung (trước 48), 66 đường (trước 65), SQL 03 có 66 truy vấn.
- **Đã sinh lại:** hình ERD, SQL 01 và 03, Chương 2–4 (`chuong_docx/Chuong2–4`, chưa sửa tay trước đó; bản cũ ở `chuong_docx/_sao_luu/truoc_MKH/`), Bảng 1.1 và 9 hình ERD trong Chương 1 (Word). Dữ liệu minh họa `sql/02` thêm giá trị MaNV = 3 cho 4 dòng LANGIAO.
- **Đã làm tiếp (30/10/2026):** (1) TAIKHOAN chuyển sang *nghiệp vụ* (không phải con người hay tổ chức; sinh ra khi vận hành, có thời điểm tạo, số lượng tăng dần); mô hình còn 6 cơ bản, 4 đối tượng ngoài, 13 nghiệp vụ, 8 mối kết hợp có thuộc tính. (2) Đổi tên thuộc tính trùng: `LANNHANLAI.ThoiDiemNhan` thành `ThoiDiemNhanLai`, `KHOANHOAN.ThoiDiemDuyet` thành `ThoiDiemDuyetHoan` (giáo trình 13.2.3 mục 5); đã kiểm tra không còn thuộc tính không-khóa-ngoại nào trùng tên. (3) Lý do giữ DIACHIKHACH và ANHMATHANG là thực thể (thuộc tính đa trị, dạng chuẩn 1) viết ở cuối 1.6.

### 9.2 Vẽ lại ERD tự động, đường thẳng không cắt nhau (30/10/2026)

- **Yêu cầu của Twot:** ERD giống cách vẽ của báo cáo mẫu, mọi đường nối là đường thẳng, không cong, không chồng lấn nhau.
- **Công cụ mới:** `tools/ve_erd2.py` (thay `ve_erd.py` trong `chay_het.py`; `ve_erd.py` vẫn giữ làm thư viện vẽ). Dựng đồ thị từ `erd.py`, kiểm tra tính phẳng (cả 9 hình đều phẳng), rồi tìm bố cục bằng ủ mô phỏng: không giao cắt, không đường xuyên nút, góc tối thiểu giữa hai đường cùng nút, đủ chỗ cho bản số. Hình tổng quát (70 nút) bắt đầu từ bố cục phẳng (Chrobak–Payne) và chỉ nhận bước dịch chuyển không làm phát sinh giao cắt.
- **Kết quả:** 9 hình đều 0 giao cắt, 0 đường xuyên nút. Hình tổng quát còn 2 nhãn bản số sát nhau (quanh ĐƠN HÀNG). Hình tổng quát nay có đủ tên mối kết hợp và bản số.
- **Bộ nhớ vị trí:** `tools/bo_cuc_erd2.json` (chỉ ghi khi bố cục sạch) giúp chạy lại nhanh và ra cùng hình. Đổi mô hình hoặc kích thước nút thì đặt `ERD_MOI=1` để vẽ lại từ đầu. Bố cục tay cũ `tools/bo_cuc_erd.py` không còn dùng cho ERD.
- **Chưa làm:** Use case, lưu đồ, sơ đồ quan hệ dạng bảng, đồ thị quan hệ vẫn vẽ theo cách cũ.

### 9.3 Vẽ lại ERD theo bố cục lưới của báo cáo mẫu (30/10/2026)

- **Lý do:** bản ve_erd2 (bố cục tự do) vẫn rối và không đẹp như hình mẫu. Hình mẫu: nút xếp theo cột và hàng đều, mỗi mối kết hợp là oval nằm đúng giữa đoạn thẳng nối hai thực thể, đường ngang hoặc dọc càng nhiều càng tốt, bản số nằm trên đường sát thực thể.
- **Công cụ:** `tools/ve_erd3.py` (thay `ve_erd2.py` trong `chay_het.py`; `ve_erd2.py` giữ lại). Nút (thực thể, mối kết hợp có thuộc tính) đặt vào ô lưới, oval mối kết hợp khóa ngoại là điểm giữa cạnh; bố cục ban đầu là bản vẽ phẳng trên lưới nguyên, ủ mô phỏng với bước dịch từng nút và bước nén theo khối, chỉ nhận bước không làm phát sinh giao cắt. Các quan hệ song song giữa cùng một cặp (ví dụ PHIẾU NHẬP – NHÂN VIÊN) vẽ thành hai đường song song, quan hệ tự thân (LOẠI HÀNG) vẽ thành hai đường song song tới một oval. Vị trí lưu ở `tools/bo_cuc_erd3.json`; `ERD_MOI=1` để vẽ lại từ đầu.
- **Hình tổng quát chỉ giữ các mối kết hợp chính với NHÂN VIÊN** (giữ vai trò, tài khoản, nhật ký đơn, lần giao, người lập đơn, người phụ trách giao); các mối kết hợp "ai làm, ai duyệt" còn lại vẽ đủ ở hình nhóm 8 (Hình 1.9). Nhóm 3 thêm NHÂN VIÊN để NHẬT KÝ ĐƠN HÀNG và LẦN GIAO đủ hai đầu.
- **Kết quả:** 9 hình đều 0 giao cắt, 0 đường xuyên nút, 0 chồng nút và oval.
