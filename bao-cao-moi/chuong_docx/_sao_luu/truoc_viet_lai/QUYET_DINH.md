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

## 10. Thu gọn phạm vi cho chắc và đúng thực tế (30/10/2026)

Theo yêu cầu của Twot: mô tả phải sát thực tế nhất và ít bị hỏi vặn; hệ thống đủ và chắc, không cần lớn. Căn cứ: đánh giá độ chân thật so với GearVN, HACOM, Phong Vũ và bản tra cứu có nguồn ở `05_tai_lieu_cua_hang_thuc_te.md`. **Mục này thay D1, D2 và phần "thêm 7 quan hệ" ở mục 7** (hướng A+ được rút lại một phần).

- **Bỏ 6 quan hệ** (không quan hệ nào khác tham chiếu tới): VAITRO, GIUVAITRO, NHATKYDONHANG, GIOHANG, CHITIETGIOHANG, DIACHIKHACH. Còn **25 quan hệ ban đầu, 26 sau cải tiến** (20 thực thể, 5 mối kết hợp có thuộc tính). Lý do: là dữ liệu tạm (giỏ), dữ liệu sao chép (địa chỉ đã chép vào đơn), hoặc mức kiểm soát quá chặt so với cửa hàng nhỏ (lịch sử giữ vai trò, nhật ký đơn).
- **Thay vai trò bằng cột `NHANVIEN.ChucVu`** (Quản lý, Bán hàng, Thu ngân, Kỹ thuật, Kho, Giao hàng; giả thiết G6). Bỏ chức vụ Quản trị và Chăm sóc khách hàng: người quản lý tạo tài khoản, nhân viên bán hàng tiếp nhận đổi trả. Vẫn truy được trách nhiệm nhờ các cột MaNV trên chứng từ (lập đơn, thu tiền, giao, nhập, nhận lại, duyệt và chi hoàn tiền, bảo hành).
- **Giữ LANNHANLAI** (một hồ sơ có thể nhận lại nhiều lần; gộp vào HOSODOITRA sẽ thêm 6 cột NULL và đổi quy tắc thành "đúng một lần").
- **Sửa mô tả theo nguồn:** bỏ câu "phần mềm phổ thông ít chú ý seri" và "ghi sổ tay hoặc Excel" (không có bằng chứng); bỏ "hủy trong 24 giờ" (Phong Vũ: hủy được trước khi cửa hàng xác nhận), bỏ "bảo hành từ 3 lần thì đổi" (không có nguồn); không thu đủ trong 24 giờ thì hủy → đơn trả trước phải thanh toán trước khi xác nhận (Phong Vũ); không sửa được → đổi tương đương hoặc thu hồi có khấu hao (GearVN, HACOM); 48 giờ, 30 ngày, 7 ngày dẫn nguồn GearVN; mốc đổi ý 7 ngày ghi là giả thiết (HACOM 15 ngày, phí 10–20%). "Bán trùng" được giải thích bằng seri (mỗi chiếc bán một lần); đơn web trừ kho khi xác nhận đơn (giả thiết). Mức đặt cọc chỉ ghi "hai bên thỏa thuận" (`DieuKienCoc`).
- **Số liệu mới** (từ `tools/chay_het.py` trừ `gen_chuong1.py`): đồ thị 25 nút, 41 cung, 9 nút vào, 57 đường truy xuất, 9 truy vấn khai thác (K6 truy trách nhiệm theo đơn và chức vụ, K8 nhân viên theo chức vụ, K9 phiếu bảo hành quá hẹn; K9 giỏ hàng cũ bị thay); mọi truy vấn có kết quả, không còn đường rỗng. ERD 8 hình (1 tổng quát + 7 nhóm), 0 giao cắt; sơ đồ quan hệ dạng bảng 5 hình. 26 quan hệ sau cải tiến đạt BCNF.
- **Đã sửa:** `tools/luoc_do.py`, `erd.py`, `ve_erd3.py`, `ve_bang.py`, `noidung.py`, `sql_gen.py`, `gen_chuong2/3/4.py`, `sql/02_du_lieu_minh_hoa.sql`, `chuong/05_tai_lieu_tham_khao.md`, `chuong_docx/Chuong1..4`, bản ghép. **Chương 1 sửa trực tiếp trong Word** (đúng nguồn chính ở mục 9); `gen_chuong1.py` vẫn chạy được và chỉ sinh Chương 1 cho bản nộp cũ; Chương 1 chính thức là file Word. Bản sao lưu trước khi thu gọn: `chuong_docx/_sao_luu/truoc_thu_gon/`.
- **Use case và lưu đồ đã rà (31/10/2026):** `ve_usecase.py`, `ve_luudo.py` và `_cho_chuong2/UseCase_va_LuuDo.docx` sửa theo mô hình 25 quan hệ: bỏ tác nhân Quản trị và Chăm sóc khách hàng (còn 6 chức vụ, giả thiết G6); bỏ ca "quản lý vai trò", "địa chỉ giao hàng", thống kê giỏ hàng; "Tiếp nhận đổi trả" thuộc Bán hàng; thống kê thêm "phiếu bảo hành quá ngày hẹn trả" (K9) và "nhân viên theo chức vụ" (K8); lưu đồ đơn bỏ nhánh hủy sau 24 giờ và ghi chú nhật ký đơn; lưu đồ bảo hành bỏ mốc "từ 3 lần". 10 hình trong file Word đã thay. Số hình trong file này (1.10–1.19) vẫn là số cũ, đánh lại khi đưa vào Chương 2. `gen_chuong1.py` (sinh `chuong/01_chuong1.md` và Chương 1 của `PowerTech_CSDLNC_Bao_cao_moi.docx`) vẫn mang lời văn cũ (vai trò, giỏ hàng, 24 giờ); chỉ nộp và đọc bản ghép `PowerTech_CSDLNC_Bao_cao_ghep.docx`, vì Chương 1 ở đó lấy từ file Word. Mục lục, danh mục hình/bảng trong bản ghép là trường Word cần cập nhật (còn số cũ đến khi cập nhật). Chưa đọc Điều 38 Luật 19/2023 và Nghị định 55/2024, chưa mở `help.phongvu.vn`.
- **Use case và lưu đồ đã đưa vào Chương 2 (31/10/2026):** thêm mục 2.4 "Phân tích chức năng và quy trình nghiệp vụ" (2.4.1 sáu sơ đồ Use Case, Hình 2.10–2.15; 2.4.2 bốn lưu đồ, Hình 2.16–2.19) ở cuối Chương 2, sau 2.3.9, nên các mục và số hình 2.1–2.9 không đổi. Mục 2.4 do `tools/gen_chuong2.py` (hàm `sec_24`) sinh, nên chạy lại `chay_het.py` không làm mất. `chuong_docx/Chuong2_*.docx` đã thay; `Chuong1/3/4` không đổi. Sao lưu trước bước này ở `chuong_docx/_sao_luu/truoc_ch2_usecase/`. Lý do đặt ở cuối thay vì đầu chương: tránh đánh lại số của gần 100 mục, 49 bảng và chú thích chéo. `_cho_chuong2/UseCase_va_LuuDo.docx` giữ làm bản tham khảo, không còn dùng. Chưa xem bố cục trong Word.

## 11. Quy tắc bảo hành theo luật, thêm mục ngoài phạm vi (31/10/2026)

Căn cứ: `06_nghien_cuu_van_hanh_cua_hang_thuc_te.md` (mục 10–11), câu chữ ở `07_cau_chu_de_xuat_sua_chuong1.md`. Điều 30 Luật 19/2023/QH15 đã đối chiếu với bản PDF Công báo số 865+866; các trang cửa hàng ở mức "đã mở" hay "chỉ thấy trong kết quả tìm kiếm" ghi trong file 06.

**Lưu ý đọc file:** phạm vi hiện hành là mục 10 (25 quan hệ ban đầu, 26 sau cải tiến). D1, D2, mục 4 (câu hỏi "24 quan hệ") và mục 7 là lịch sử, đã bị mục 10 thay thế.

| # | Quyết định | Căn cứ |
|---|---|---|
| Q1 | **Khôi phục** quy tắc "bảo hành từ ba lần trở lên mà lỗi vẫn còn thì đổi sản phẩm mới tương tự hoặc thu hồi và trả lại tiền". **Đính chính mục 10:** lý do bỏ quy tắc này ("không có nguồn") là sai | Luật 19/2023, Điều 30 khoản 2 điểm đ |
| Q2 | Thời gian sản phẩm nằm ở cửa hàng hoặc hãng để bảo hành **không tính vào thời hạn bảo hành**; thay linh kiện hoặc đổi sản phẩm mới thì **tính lại thời hạn** từ lúc thay hoặc lúc đổi. Đây là quy định của luật, không còn là giả thiết nhóm | Điều 30 khoản 2 điểm c |
| Q3 | Khi thu hồi sản phẩm không sửa được, **mức khấu hao là thỏa thuận giữa cửa hàng và khách (giả thiết của nhóm)**, người quản lý quyết định. Luật chỉ nói "trả lại tiền"; GearVN và HACOM có khấu hao nhưng chưa tìm được căn cứ pháp lý. Cần hỏi thầy | Điều 30 điểm đ; GearVN, HACOM (file 05) |
| Q4 | **Thêm vào danh sách ngoài phạm vi (mục 1.3):** đơn đặt hàng nhà cung cấp, trả hàng nhà cung cấp, kiểm kê và chuyển kho, hóa đơn điện tử. Hai giả thiết phạm vi: đơn đặt hàng gửi nhà cung cấp theo dõi ngoài hệ thống; hóa đơn điện tử phát hành bằng phần mềm riêng, hệ thống chỉ lưu số đơn và mã số thuế khách | KiotViet, Sapo, MISA, Odoo có các nghiệp vụ này (file 06 mục 6, 8); nhóm chọn phạm vi hẹp |
| Q5 | Đoạn Phiếu Nhập: "đối chiếu với đơn đặt" đổi thành "đối chiếu với đơn đặt hàng cửa hàng đã gửi (theo dõi ngoài hệ thống)" để khớp Q4 | Nhất quán nội bộ |
| Q6 | **Không đổi lược đồ và không đổi Chương 2–3.** Quy tắc ba lần và cộng ngày gửi là quy tắc nghiệp vụ, không tạo phụ thuộc hàm mới; đếm số lần bảo hành theo số seri và cộng ngày gửi từ ngày nhận, ngày trả thực tế đều tính được từ dữ liệu hiện có | `tools/luoc_do.py` (PHIEUBAOHANH), file 06 mục 11.4 (đọc lược đồ, chưa chạy truy vấn) |
| Q7 | **Chiếc hàng thay thế khi bảo hành "đổi mới" nằm ngoài phạm vi (quyết định 31/10/2026, chọn hướng ghi ngoài phạm vi, không thêm cột).** Cơ sở dữ liệu chỉ ghi kết quả "đổi mới" trên phiếu bảo hành; không nối chiếc mới và không theo dõi thời hạn riêng của nó. Đã ghi ở Chương 1 (đoạn Phiếu Bảo Hành, danh sách ngoài phạm vi 1.3) và Chương 4 (mục 4.3). Giữ nguyên lược đồ 25/26 quan hệ | Khoảng trống ở file 06 mục 11.4; chọn hướng này vì không phải tính lại PTH, khóa, dạng chuẩn và số liệu của cả báo cáo |

**Chưa làm:**

- ~~Dán câu chữ A–D (file 07) vào `chuong_docx/Chuong1_Tong_quan.docx`.~~ **Đã làm 31/10/2026:** dán vào đoạn Phiếu Bảo Hành (A, B, C), câu liệt kê và câu giải thích ở 1.3 (D1, D2) và đoạn Phiếu Nhập (D3), bằng cách sửa trực tiếp `word/document.xml` của `Chuong1_Tong_quan.docx` và `PowerTech_CSDLNC_Bao_cao_ghep.docx` (Chương 1 của bản ghép lấy từ file Word). Chữ mới dán như chữ thường, không in đậm. **Không sửa** `PowerTech_CSDLNC_Bao_cao_moi.docx`: Chương 1 trong file đó là bản cũ sinh tự động, đừng nộp file đó. Bản gốc trước khi dán: `chuong_docx/_sao_luu/truoc_dan_ABCD/`. Chưa mở trong Word để xem trang.
- ~~Sửa `tools/gen_chuong4.py` (mục 4.3 hạn chế) cho khớp Q4, rồi sinh lại Chương 4; kiểm tra bản ghép.~~ **Đã làm 31/10/2026:** sửa mục 4.3 (thêm đơn đặt hàng và trả hàng nhà cung cấp, kiểm kê và chuyển kho, hóa đơn điện tử) và 4.4 trong `gen_chuong4.py`, sinh lại `chuong/04_chuong4.md`. Ba file Word (`chuong_docx/Chuong4_*.docx`, `PowerTech_CSDLNC_Bao_cao_ghep.docx`, `PowerTech_CSDLNC_Bao_cao_moi.docx`) được thay đúng hai câu đó bằng cách sửa trực tiếp `word/document.xml`, vì máy này không có python-docx và Graphviz nên không chạy lại `chay_het.py`; các phần khác của gói không đổi (đã so với bản sao lưu ở `chuong_docx/_sao_luu/truoc_q4_ch4/`). Chưa mở trong Word; trên máy có Python đầy đủ nên chạy lại `chay_het.py` một lần để chắc chắn ba nguồn cùng khớp (lưu ý README: lệnh này không đụng Chương 1 chính thức).
- ~~Chưa quyết (khoảng trống lược đồ): chiếc hàng đổi mới trong bảo hành chưa nối được với phiếu bảo hành.~~ **Đã quyết 31/10/2026: ghi ngoài phạm vi (Q7).** Nếu sau này muốn biểu diễn được thì thêm cột trỏ tới chiếc hàng mới (hoặc ngày bắt đầu bảo hành) vào PHIEUBAOHANH, rồi tính lại PTH, khóa, dạng chuẩn và số liệu liên quan, sinh lại chương và SQL. Bản sao lưu trước khi ghi: `chuong_docx/_sao_luu/truoc_ngoai_pham_vi/`. Chương 4 (bốn file: md, Chuong4 docx, bản ghép, bản moi) và Chương 1 (Chuong1 docx, bản ghép) đã cập nhật; chưa mở trong Word.
- Hai bổ sung tùy chọn E, F (file 06 mục 11.3): câu về Điều 37 trong mục Hồ Sơ Đổi Trả; hàng gửi hãng nước ngoài lâu hơn (nguồn thứ cấp).
- Mục 8 của file 06 so với bản `.md` cũ nên có dòng lỗi thời; mục 11 của file 06 là bản đối chiếu đúng với Word.
- Mở lại các liên kết mức P, T trong file 06 trước khi nộp.
- Chưa commit; commit và push do Twot làm.

## 12. Vẽ lại đồ thị quan hệ bằng đường thẳng (31/10/2026)

- **Lý do:** Hình 3.1, 3.2 cũ do Graphviz `dot` vẽ, nút NHANVIEN nhận 13 cung cong vòng; mẫu của thầy dùng toàn đường thẳng. Mục tiêu của Twot: hình dễ nhìn như mẫu, ưu tiên đồ thị.
- **Công cụ mới:** `tools/ve_dothi.py` (thay phần vẽ trong `gen_chuong3.py`, hàm `draw` chỉ còn gọi nó). Ủ mô phỏng tìm vị trí nút, cung là đường thẳng, vẽ bằng `neato -n`. Bố cục lưu ở `tools/bo_cuc_dothi.json` (`DOTHI_MOI=1` tìm lại từ đầu, `DOTHI_TINH=1` tinh chỉnh tiếp); hai hình dùng chung bố cục nên cùng một đồ thị.
- **Kết quả đã kiểm:** đồ thị **không phẳng** (networkx), nên không thể không có giao điểm. Bố cục hiện tại: **10 chỗ cắt, 0 cung đi xuyên nút, mọi cung đủ dài để thấy mũi tên** (kiểm trên tọa độ thật). 10 là số tìm được, **chưa chứng minh là nhỏ nhất**. Chương 3 đã thêm một đoạn nói rõ điều này (số 10 lấy tự động từ bố cục). Đường truy xuất (57), SQL (57 + 9) không đổi (cùng mã băm).
- **Thử và bỏ:** bố cục lưới nguyên cho 6 giao cắt nhưng có một cung (21 → 12) đi đúng qua tâm nút NHANVIEN, dễ hiểu nhầm; cấm hẳn cung xuyên nút trên lưới nguyên làm giao cắt tăng lên 15. Tọa độ thực cho 10 giao cắt và 0 xuyên nút.
- **Hạn chế:** Hình 3.2 (có tên) rộng 12,9 inch, khi in rộng 16 cm chữ 12 pt còn khoảng **5,9 pt** (dưới mức 7 pt ở mục 6). Hình 3.1 (chỉ số) đọc rõ. Cách khác nếu cần: bỏ Hình 3.2, hoặc giữ tên ở Bảng 3.2.
- **Đã cập nhật:** `hinh/do_thi_quan_he*` (.dot, .png, .svg), `chuong/03_chuong3.md`, `chuong_docx/Chuong3_Ket_qua_thuc_nghiem.docx` và bản ghép (hai ảnh, kích thước ảnh và đoạn giải thích). Bản sao lưu trước đó: `chuong_docx/_sao_luu/truoc_dothi_thang/`. Chưa mở trong Word.
- **Môi trường:** đã cài `python-docx`, `Pillow`, `networkx`, Graphviz 16.1.0 trên máy Windows; sửa `tools/ve_erd.py` chọn phông Arial theo hệ điều hành.

### 12.1 ERD vẽ lại (31/10/2026)

- **Hiện trạng đã đo:** cả 8 hình ERD (1 tổng quát + 7 nhóm) đã có 0 giao cắt, 0 đường xuyên nút, 0 chồng nút/oval từ bản trước; chỉ còn lỗi trình bày: nhãn bản số chồng lên nhau (rõ nhất ở HỒ SƠ ĐỔI TRẢ trong hình tổng quát, và quanh NHÂN VIÊN ở nhóm 7) và một số đoạn quá ngắn.
- **Đã sửa:** (1) `tools/ve_erd3.py` thêm bước **gỡ chồng nhãn bản số** (hai nhãn đè nhau thì đẩy ra theo trục đè ít hơn); (2) bắt buộc "không còn đoạn ngắn" khi tìm bố cục mới (tối đa 8 vòng) nhưng thực tế vẫn còn 1–4 đoạn ngắn ở vài hình; (3) **hình nhóm 7 (trách nhiệm) dùng bố cục mới**: các thực thể tỏa quanh NHÂN VIÊN, gọn hơn (1161×885 thay vì 1147×1121), bản cũ có ba đường dồn xuống một chỗ. Các hình còn lại giữ bố cục cũ vì tìm lại không tốt hơn.
- **Còn lại, chưa sửa:** ở nhóm 7 ba nhãn `(0,n)` xếp dọc ở mép trên NHÂN VIÊN (đọc được nhưng khó biết nhãn nào của đường nào); các hình có mối kết hợp `CHI TIẾT …` nối với mối kết hợp khác (HÀNG CÓ SERI, PHIẾU BẢO HÀNH, CHI TIẾT TRẢ ↔ CHI TIẾT ĐƠN HÀNG) là ký hiệu "mối kết hợp nối mối kết hợp", cùng kiểu mà tôi đã chê ở báo cáo mẫu (08, lỗi E1); giữ nguyên vì thay đổi sẽ kéo theo lược đồ quan hệ; cần chuẩn bị câu trả lời nếu thầy hỏi.
- **Đã cập nhật:** `hinh/erd_*.png`, `tools/bo_cuc_erd3.json`, `chuong_docx/Chuong1_Tong_quan.docx` và `PowerTech_CSDLNC_Bao_cao_ghep.docx` (8 ảnh và kích thước). Sao lưu trước đó: `chuong_docx/_sao_luu/truoc_erd_moi/`. Chưa mở trong Word.

## 13. Rà soát lần cuối, thu gọn mô tả, tài liệu câu hỏi khó (01/11/2026)

- **Không viết lại từ đầu.** Mọi phép tính, 57 đường truy xuất, 57 + 9 câu SQL đã kiểm; viết lại sẽ làm mất kết quả đã kiểm. Chỉ sửa đúng các chỗ còn tồn.
- **Chương 1 (Word):** bỏ câu nói về công cụ ("SQL Server hoặc SQLite, Graphviz"), bỏ đoạn lặp ở 1.3, bỏ hồ sơ nhân viên lặp ở 1.4 (đã có ở đoạn Nhân Viên), bỏ hai câu lặp ở đoạn Đơn Hàng, bớt chi tiết phần trăm phí của HACOM (chưa kiểm nguồn). Mục 1.4 còn khoảng 4.450 từ so với 4.550 trước đó; **mẫu ThamKhao khoảng 4.040 (cùng cách đếm, tách theo khoảng trắng)**. Không cắt thêm vì phần còn lại là quy tắc nghiệp vụ của đổi trả, bảo hành, thanh toán. Số "4.347 và 3.864" ở file 09 đếm theo cách khác, không so được với số này. Bản sao lưu: `chuong_docx/_sao_luu/truoc_thu_gon_ch1/`.
- **SQL 57 đường truy xuất:** đổi `SELECT *` thành danh sách khóa chính của các quan hệ trên đường (cột nối trùng giá trị lấy một lần). Sửa `tools/sql_gen.py`, `tools/gen_chuong3.py`; sinh lại `sql/03` và `chuong/03`; vá 6 khối SQL và đoạn giải thích trong `Chuong3_Ket_qua_thuc_nghiem.docx`. Bản sao lưu: scratchpad `truoc_select`.
- **B3, B5, B7:** đã có câu kết luận ở 3.1 (không tạo nút bản lề; B5 không thực hiện; B7 không có cung vô hướng vì quan hệ n–n đều có thuộc tính riêng), không thêm.
- **Giữ nguyên lược đồ:** PHIEUGIAO 1–1 ĐƠN HÀNG, LANNHANLAI (0,n), GIAODICHKHO, NHANVIEN nối nhiều. Lý do và câu trả lời sẵn ở `10_cau_hoi_de_bi_hoi_kho_va_tra_loi.md`.
- **Số liệu:** `chay_het.py` cho 25 nút, 41 cung (40 cung + 1 khuyên), 9 nút vào, 57 đường; chương 1, 2, 4 sinh ra không đổi so với lần trước (trừ ký tự xuống dòng).
- **Ghép Word:** `PowerTech_CSDLNC_Bao_cao_ghep.docx` đang mở trong Word nên không ghi đè được; đã thay bằng bản mới (Chương 1, 3 cập nhật; 29 hình) sau khi Twot đóng Word; bản cũ lưu ở `chuong_docx/_sao_luu/truoc_ghep_v2/`. `PowerTech_CSDLNC_Bao_cao_moi.docx` bị `chay_het.py` ghi đè (Chương 1 trong đó là bản sinh cũ, chính thức nằm ở `chuong_docx/`). PDF cũ chưa xuất lại.
- **Việc còn lại:** mở Word xem trang và cập nhật trường (F9); xuất lại PDF; Hình 3.2 chữ nhỏ khi in; mở lại nguồn mức P, T trong file 06.

## 14. Sửa ba lỗ hổng lược đồ (01/11/2026)

Theo yêu cầu của Twot sau khi đánh giá lại đề tài. Giữ 25 quan hệ ban đầu, 26 sau cải tiến. Sao lưu trước khi sửa: `chuong_docx/_sao_luu/truoc_sua_3_lo_hong/`.

| # | Lỗ hổng | Cách sửa |
|---|---|---|
| L1 | Khóa (MaHS, SoDongDH) của CHITIETTRA không ghi được việc trả 2 chiếc có seri trên cùng một dòng đơn; PTH `MaHS,SoDongDH → MaSeri` sai về nghiệp vụ | Thêm `SoDongTra`. Khóa mới {MaHS, SoDongTra} và {MaHS, MaSeri} (khóa sau theo G4). CHECK `SoLuongTra = 1` khi có MaSeri |
| L2 | Mô tả nói thời hạn bảo hành không đổi khi đổi chính sách, nhưng `ThoiHanBH` chỉ ở MATHANG | Thêm `CHITIETDONHANG.ThoiHanBHChot`, cùng kiểu với DonGiaChot |
| L3 | Khoản hoàn do bảo hành không nối được với phiếu; không phân biệt được với hoàn do hủy đơn | Thêm khóa ngoại `KHOANHOAN.MaPhieuBH`. Chọn khóa ngoại thay vì cột lý do vì cột lý do không chỉ ra được đúng phiếu. CHECK không cùng có MaHS và MaPhieuBH |

- **Số liệu đổi:** 37 mối kết hợp thường (trước 36); đồ thị 25 nút, **42 cung** (trước 41), **8 nút vào** (trước 9, PHIEUBAOHANH không còn là nút vào), **vẫn 57 đường** (các đường từ PHIEUBAOHANH nay bắt đầu từ KHOANHOAN), 64 cặp giao (trước 63). Dạng chuẩn không đổi: ban đầu 20 BCNF, 1 3NF, 1 2NF, 1 1NF, 2 chưa 1NF; sau cải tiến 26 BCNF.
- **Hình:** ERD tổng quát tìm lại bố cục (0 giao cắt, khung cao hơn trước). ERD nhóm 5 thêm PHIẾU BẢO HÀNH. Đồ thị quan hệ **14 giao cắt, 0 cung xuyên nút** (trước 10); tìm lại từ đầu cho 15 giao cắt và 2 cung xuyên nút nên giữ bản 14; chưa chứng minh là nhỏ nhất.
- **SQL:** `sql_gen.py` sinh `CREATE UNIQUE INDEX ... WHERE ... IS NOT NULL` cho cột cho phép rỗng (CHITIETTRA, và sửa luôn TAIKHOAN vì UNIQUE thường của SQL Server chỉ cho một giá trị NULL). Chưa chạy trên SQL Server. `sql/02`: thêm cột mới, phiếu bảo hành 1 đổi thành đã trả khách với kết quả thu hồi, thêm khoản hoàn 2, chuyển KHOANHOAN xuống sau PHIEUBAOHANH.
- **Đã kiểm:** SQLite có bật khóa ngoại: 57 + 9 câu đều có kết quả; trả chiếc thứ hai cùng dòng đơn được nhận, ghi trùng chiếc bị chặn; đổi `ThoiHanBH` không đổi `ThoiHanBHChot`; khoản hoàn có cả hai nguồn bị chặn. Tính lại độc lập: BCNF 26 quan hệ, 57 đường, 8 nút vào, khớp.
- **Word:** Chương 1 sửa trong `chuong_docx/Chuong1_Tong_quan.docx` (bốn đoạn 1.4, hai dòng 1.6, số ở 1.7.1, thêm một dòng Bảng 1.1, thay 8 hình ERD); Chương 2–4 lấy từ bản sinh lại; bản ghép đã dựng lại. Chưa mở trong Word; mục lục và danh mục vẫn cần cập nhật trường (F9). PDF chưa xuất lại.
- **Chưa xử lý:** bán lại hàng trả về ghi đè `HANGCOSERI.MaDH` nên câu 6.8 của file 10 không đúng cho chiếc đã bán lại; đoạn 1.4 đổi hàng lập đơn mới nhưng hồ sơ chưa nối với đơn mới.

## 15. Thống nhất DC1, quy tắc bán lại, Use Case theo chức vụ (01/11/2026)

Làm việc 1–3 ở `08_cham_diem_bao_cao_mau_ThamKhao.md` mục 6.2. Sao lưu: `chuong_docx/_sao_luu/truoc_viec_1_3/`. Lược đồ không đổi cấu trúc: 25/26 quan hệ, 42 cung, 8 nút vào, 57 đường, dạng chuẩn giữ nguyên.

- **DC1:** tiêu chí "chỉ tách khi cửa hàng phải dùng một phần giá trị" nêu ở 2.3.2 cho `TenNguoiNhan`, `NguoiLienHeNCC`, `DiaChiGiao`, `DiaChiNCC`, `PhuKienDiKem` (giả thiết). Câu "phí giao tính theo khu vực" đổi thành phí do nhân viên bán hàng chốt và ghi trên đơn. `PhuKienDiKem` là ghi chú tự do.
- **Bán lại:** chọn cách nhẹ, không thêm quan hệ. `HANGCOSERI.MaDH, SoDongDH` là **lần bán gần nhất**; chiếc trả về rồi bán lại thì ghi sang lần mới, lần trước tra ở `CHITIETTRA` và `PHIEUBAOHANH`. Người mua của phiếu bảo hành tra theo mạch trực tiếp 25 → 13. Đã đổi mô tả 1.4, tân từ, ràng buộc 2, ngữ nghĩa cung 19 → 13, K4, nhận xét đồ thị, thêm hạn chế ở 4.3. Đã thử trên SQLite: phiếu cho đơn 2, mạch qua seri cho đơn mới, dòng trả vẫn giữ đơn 2.
- **Use Case:** bỏ tác nhân Nhân viên chung; 6 chức vụ nối riêng. Sửa theo 1.4: danh mục cơ bản và nhà cung cấp do người quản lý; bán hàng và giao hàng thêm vào thanh toán; kho thêm vào lấy hàng, bàn giao; người quản lý thêm vào duyệt hàng nhận lại. Đường nối vào đầu oval nên không xuyên oval khác.
- **Chưa làm:** mở Word xem trang và cập nhật trường; xuất lại PDF; việc 4–8 ở file 08 mục 6.2.

## 16. Rút gọn mô tả, SQL Server, soát cuối (01/11/2026)

Làm việc 4–8 ở `08_cham_diem_bao_cao_mau_ThamKhao.md` mục 6.2. Sao lưu: `chuong_docx/_sao_luu/truoc_viec_4_8/` (gồm cả PDF cũ). Số liệu lược đồ và đồ thị không đổi so với mục 14.

- **Mô tả 1.4:** còn 4.036 từ (trước 4.541 theo cùng cách đếm; mẫu khoảng 4.040). Bỏ đoạn tóm quy trình trùng với các đoạn đối tượng, bỏ mã G1–G6 và câu nhắc Chương 2. Giả thiết gom một câu: "Những quy tắc, con số và phân công không ghi nguồn là đề xuất của nhóm". Mã G1–G6 vẫn định nghĩa ở 2.2.1. Thay "mã hóa" bằng "mã hóa một chiều" cho mật khẩu.
- **Đổi hàng:** đơn mới ghi số hồ sơ đổi trả ở ghi chú; nối hai chứng từ bằng khóa ngoại nằm ngoài phạm vi (1.3, 4.3). Không thêm khóa ngoại vì sẽ có cung song song HOSODOITRA tới DONHANG.
- **Chương 3:** thêm câu giải thích B3 và sáu đường có ý nghĩa nghiệp vụ ở cuối 3.2.3.
- **SQL Server:** phát hiện câu "chạy được trên SQL Server" là sai vì 4 CHECK dạng `(A IS NULL) = (B IS NULL)` không hợp lệ trong T-SQL. Đã viết lại dạng chuẩn. Chạy trên instance LocalDB 17.0 tạm (đã xóa), CSDL collation `Vietnamese_100_CI_AS_SC_UTF8`: `01`, `02` không lỗi, 26 bảng, 45 CHECK; `03`, `04` đủ 57 + 9 câu đều có kết quả; thử dòng trả, khoản hoàn hai nguồn, nhân viên nghỉ thiếu ngày đều đúng. Không đụng CSDL đang chạy và `database/`.
- **Word:** cập nhật mục lục và danh mục bằng Word, xuất `PowerTech_CSDLNC_Bao_cao_ghep.pdf` 143 trang. Xóa `PowerTech_CSDLNC_Bao_cao_moi.pdf` cũ ở thư mục gốc. Đã xem mẫu 4 trang (mục lục, Bảng 1.1, Use Case tổng quát, đồ thị); chưa soát từng trang.
- **Lưu ý:** chạy lại `chay_het.py` hoặc `ghep_chuong_docx.py` sẽ ghi đè bản ghép; phải cập nhật trường và xuất PDF lại.
