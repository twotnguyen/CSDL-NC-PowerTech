# bao-cao-moi

Báo cáo mới môn Cơ sở dữ liệu nâng cao, đề tài PowerTech (Nhóm 6, 23DTHD6).

| Đường dẫn | Nội dung |
|---|---|
| `PowerTech_CSDLNC_Bao_cao_ghep.docx` | **Bản nộp**, ghép từ `chuong_docx/` (A4, có mục lục, bảng, hình) |
| `PowerTech_CSDLNC_Bao_cao_moi.docx` | Bản sinh tự động, Chương 1 là bản cũ; chỉ dùng làm nền để ghép, không nộp |
| `PowerTech_CSDLNC_Bao_cao_ghep.pdf` | Bản PDF xuất từ Word từ bản ghép (151 trang A4, gồm phụ lục 61 câu SQL; bản mới nhất đang ở tên `_v2`) để in; xuất lại sau mỗi lần dựng docx |
| `chuong/` | Nội dung từng phần dạng Markdown: `00` phần đầu, `01`–`04` bốn chương, `05` tài liệu tham khảo |
| `chuong_docx/` | 4 file Word, mỗi file một chương, tách từ bản nộp để sửa riêng từng chương (xem "Tách và ghép chương") |
| `chuong_docx/_sao_luu/`, `chuong_docx/_cho_chuong2/` | Bản gốc Chương 1 trước khi viết lại; Use case và lưu đồ cắt khỏi Chương 1; đã đưa vào Chương 2 mục 2.4 (xem `QUYET_DINH.md` mục 9 và cuối file), file này chỉ để tham khảo |
| `sql/` | `01` tạo bảng (26 quan hệ), `02` dữ liệu minh họa, `03` 61 truy vấn theo đường truy xuất, `04` 9 truy vấn khai thác |
| `hinh/` | ERD và đồ thị quan hệ (`.dot` nguồn, `.svg`, `.png`) |
| `tools/` | Mã Python sinh toàn bộ số liệu và nội dung |
| `00`–`03_*.md` | Ghi chú đọc giáo trình, bài giảng, yêu cầu giảng viên, đánh giá báo cáo mẫu |
| `04_doi_chieu_mo_ta_voi_cac_tai_lieu.md` | Đối chiếu mô tả 1.1–1.4 với báo cáo web, bản nộp đầu và báo cáo cũ (đã xử lý bằng hướng A+, xem QUYET_DINH mục 7) |
| `10_cau_hoi_de_bi_hoi_kho_va_tra_loi.md` | Câu hỏi dễ bị hỏi khó khi bảo vệ, kèm trả lời sẵn và các điểm yếu thật |
| `QUYET_DINH.md` | Quyết định, giả thiết, câu hỏi còn mở |

## Dựng lại

Cần Python 3 (`python-docx`, `Pillow`, `networkx`, `numpy`) và Graphviz (`dot`, phải có trong PATH). Trên Windows, Graphviz cài bằng `winget install Graphviz.Graphviz` (ở `C:\Program Files\Graphviz\bin`); phông Arial lấy từ macOS hoặc `C:\Windows\Fonts`.

```bash
python3 tools/chay_het.py
```

Sau thu gọn (30/10/2026, QUYET_DINH mục 10) `chay_het.py` vẫn chạy được, nhưng `gen_chuong1.py` chỉ sinh Chương 1 cho bản nộp `.docx` cũ; **Chương 1 chính thức nằm trong `chuong_docx/Chuong1_Tong_quan.docx`** (sửa trong Word). Sau khi chạy, lấy Chương 2–4 từ bản nộp mới (`tach_chuong_docx.py` ghi đè cả Chương 1, nên tách vào thư mục tạm rồi chỉ chép Chương 2–4).

Lệnh này kiểm tra phân tích (bao đóng, phủ tối thiểu, khóa, dạng chuẩn, bảo toàn), sinh ERD, SQL, chương 1–4, chạy thử SQL trên SQLite rồi ghép docx. Chương 0 và 5 viết tay trong `chuong/`; chương 1–4 là file sinh ra, sửa ở `tools/gen_chuong*.py` chứ không sửa trực tiếp.

## Tách và ghép chương

```bash
python3 tools/tach_chuong_docx.py    # bản nộp .docx -> chuong_docx/ChuongN_*.docx (ghi đè 4 file đó)
python3 tools/ghep_chuong_docx.py    # 4 file chương + bìa, mục lục, lời mở đầu, tài liệu tham khảo của bản nộp -> PowerTech_CSDLNC_Bao_cao_ghep.docx
```

Sửa một chương thì chỉ mở và sửa file chương đó, rồi ghép lại. Tách rồi ghép không sửa gì cho ra gói giống hệt bản nộp gốc. Chương 1–4 của bản nộp vẫn là file sinh ra: `chay_het.py` không đọc `chuong_docx/`, và chạy lại `tach_chuong_docx.py` sẽ ghi đè các file chương đã sửa tay. Chọn một nguồn chính (file Word hoặc `gen_chuong*.py`) và không trộn hai cách.
