# Kế hoạch nâng cấp báo cáo từ bài học báo cáo mẫu (31/10/2026)

Yêu cầu của Twot (5 điều): (1) mô tả không lớn, tốt hơn mẫu; (2) thực tế, không lỗ hổng; (3) sơ đồ dễ nhìn như mẫu; (4) thực thể, PTH, khóa, dạng chuẩn, 4NF, đồ thị, SQL đúng chính xác; (5) ưu tiên đồ thị và đường truy xuất. Căn cứ: `08_cham_diem_bao_cao_mau_ThamKhao.md`. Nhãn **[kiểm]** = đã chạy lại hôm nay.

## A. Hiện trạng đối chiếu (đã kiểm)

| Hạng mục | Mẫu | Báo cáo nhóm | Kết luận |
|---|---|---|---|
| Số đường truy xuất | 69 liệt kê, tính lại ra 70 (thiếu `11 → 10`) | 57 liệt kê, **tính lại độc lập ra 57, khớp 100%** [kiểm] | Nhóm đúng |
| Nút vào | 5, không giải thích | 9 (nút không có cung vào), có giải thích 3.2.1 | Nhóm tốt hơn |
| Bản số (m, A, M) trên cung | Không | Có cho từng cung (Bảng 3.4) | Nhóm tốt hơn |
| SQL cho đường truy xuất | 5/69, một câu lỗi | **57/57 chạy được trên SQLite có bật khóa ngoại, đều có kết quả; 9 truy vấn khai thác cũng chạy được** [kiểm] | Nhóm tốt hơn |
| Dạng chuẩn | Bảng mâu thuẫn kết luận | 26/26 BCNF, phân rã có tableau, F' ≡ F; bộ kiểm tra chạy lại ra đúng 25 ban đầu (20 BCNF, 1 3NF, 1 2NF, 1 1NF, 2 chưa 1NF) và 26 sau cải tiến [kiểm] | Nhóm tốt hơn |
| 4NF | Không làm | Một tình huống có chứng minh MVD | Nhóm tốt hơn |
| B7 (cung vô hướng) | Có một cung | Không có; hiện thực đúng điều kiện trong Bài 10 (không thuộc tính không khóa, đúng 2 cung ra, không cung vào, khóa = hợp hai khóa) | Đúng, nhưng cần câu giải thích vì sao không có |
| Mô tả 1.4 | 3.864 từ, 27 đoạn | 4.347 từ, 35 đoạn (dài hơn 12%) | Cần cắt gọn, không thêm |
| Hình | Bố cục dễ nhìn, nhưng có lỗi ký hiệu | Hình đồ thị: nút NHANVIEN nhận 13 cung cong; ERD có đường chéo dài, nhãn bản số chồng nhau gần HỒ SƠ ĐỔI TRẢ | Cần vẽ lại |

## B. Việc cần làm, theo thứ tự ưu tiên

### B1. Đồ thị và đường truy xuất (ưu tiên 1)

1. **Vẽ lại Hình 3.1, 3.2** theo kiểu mẫu: chỉ đường thẳng, nút xếp hàng, không cung cong vòng. Vấn đề chính là nút 8 (NHANVIEN) nhận 13 cung vai trò. Hướng: đặt NHANVIEN ở giữa hoặc cạnh, cung vai trò có màu và nhãn ngắn; hoặc tách Hình 3.1 (cung khóa chính) và Hình 3.1b (cung vai trò). Cần Graphviz.
2. **Khuyên 1 → 1** (LOAIHANG cha – con): mẫu coi "…→ 3 → 3" là một đường kết thúc; nhóm để ngoài thuật toán (quy ước Q4). Chọn một cách và viết rõ lý do; nếu đưa vào thì thêm các đường kết thúc `… → 1 → 1`.
3. **Mục 3.1:** thêm hai dòng chứng minh vì sao B3, B5, B7 không tạo gì (liệt kê ứng viên và điều kiện bị loại, như bài giảng làm).
4. **SQL:** thay `SELECT *` bằng danh sách cột chính (tránh trùng tên cột); giữ kết quả chạy được. Có thể giữ `SELECT *` ở file `03` và ghi rõ là bản rút gọn.
5. **Ngữ nghĩa:** cắt các câu "Cho biết…" quá dài; giữ ví dụ điển hình ở thân bài, bảng đầy đủ để phụ lục.

### B2. Mô tả (1.1–1.4)

- Mục tiêu: **không dài hơn mẫu** (hiện 4.347 từ, mẫu 3.864) mà cụ thể và thực tế hơn.
- Cắt: câu "kiểm tra bằng SQL Server hoặc SQLite, vẽ bằng Graphviz" ở 1.2 (thuật ngữ kỹ thuật, thầy đã phê loại này); gộp các đoạn Mã Giảm Giá, Phiếu Giao, Lần Giao, Phiếu Nhập; giảm số lần nhắc "giả thiết" (hiện 16 + 6) bằng một đoạn quy ước ở đầu 1.4.
- Giữ: thanh toán và đặt cọc, đổi trả, bảo hành (đúng điều thầy hỏi ở D6), ai làm khâu nào.
- Không thêm tính năng mới (không giỏ hàng, không trả góp, không kiểm kê).

### B3. Thực thể (ba loại): ba điểm có thể bị hỏi

| Điểm | Rủi ro | Hướng |
|---|---|---|
| GIAODICHKHO | Thầy từng phê "TonKho, LichSu… là thống kê, không là thực thể"; bảng này là sổ biến động, tồn tính từ nó; tham chiếu chứng từ đa hình (`LoaiChungTu, MaChungTu`) không có khóa ngoại | Giữ nhưng viết rõ lý do (hàng không seri cần theo nhóm kho), hoặc đổi thành mối kết hợp theo chứng từ nguồn. Cần Twot quyết |
| LANNHANLAI so với LANGIAO | LANGIAO là mối kết hợp (khóa = khóa cha + số lần) còn LANNHANLAI là thực thể có khóa riêng: nhìn như không nhất quán | Chuẩn bị câu trả lời hoặc thống nhất cách xếp |
| PHIEUGIAO | Quan hệ 1–1 với DONHANG | Giải thích: có LANGIAO con (tối đa 3) nên tách |

### B4. Hình khác

- ERD tổng quát và 7 hình nhóm: bố trí lại cho không có đường chéo dài, nhãn bản số không chồng nhau (Hình 1.1 hiện có chồng `(0,n)` và `(1,n)` gần HỒ SƠ ĐỔI TRẢ). So lại với mẫu: tên mối kết hợp là động từ, mỗi nhánh có (min,max).
- Sơ đồ quan hệ dạng bảng, use case, lưu đồ: kiểm lại sau khi cài công cụ.

## C. Công cụ (cập nhật 31/10/2026: đã cài xong)

Đã cài trên máy Windows này: `python-docx` 1.2.0, `Pillow` 13.0.0, `networkx` 3.7 (pip; `numpy` 2.4.6 đi kèm) và **Graphviz 16.1.0** (winget, ở `C:\Program Files\Graphviz\bin`; shell đang mở chưa có trong PATH, cần `export PATH="/c/Program Files/Graphviz/bin:$PATH"` hoặc mở shell mới). Đã sửa `tools/ve_erd.py` để tự chọn phông Arial (macOS hoặc Windows) thay cho đường dẫn macOS cố định.

**Đã kiểm:** chạy `tools/chay_het.py` trên một **bản sao** ở thư mục tạm: chạy hết 10 bước trong 14 giây, ra 39 hình và 61 bảng; `02_chuong2.md`, `03_chuong3.md`, `04_chuong4.md`, `sql/01`, `sql/03`, `sql/04` và `so_lieu_chuong3.json` **giống hệt bản gốc** (trừ ký tự xuống dòng), tức quy trình dựng lại được trên máy này. Ảnh PNG chỉ khác chút về kích thước tệp do phông.

**Cảnh báo khi chạy `chay_het.py` thật:** lệnh này ghi đè `PowerTech_CSDLNC_Bao_cao_moi.docx` bằng Chương 1 bản cũ (xem README); bản nộp là `PowerTech_CSDLNC_Bao_cao_ghep.docx` ghép từ `chuong_docx/`, và `chay_het.py` không đụng tới các file đó.

## D. Chưa kiểm

- Chưa so từng chữ phần PTH của 25 quan hệ với giáo trình; chưa chạy kiểm độc lập phủ tối thiểu/khóa bằng vét cạn hôm nay (báo cáo ghi đã làm ngày 25/10).
- Chưa mở file Word xem số trang và bố cục.
