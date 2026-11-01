# QUYẾT ĐỊNH & NGUYÊN TẮC THIẾT KẾ BÁO CÁO CSDL-NC (NHÓM 6)

> Áp dụng cho toàn bộ quá trình viết báo cáo môn **Cơ sở dữ liệu nâng cao** của **Nhóm 6 (Lớp 23DTHD6)** — Đề tài: **PowerTech Cửa Hàng Máy Tính**.
> Thành viên: Nguyễn Ngọc Tình (Trưởng nhóm), Đỗ Thanh Hoàng Đức Nhả, Võ Thành Đông.

---

## 1. KHUNG 8 MỤC BẮT BUỘC THEO YÊU CẦU ĐỀ BÀI CỦA GIẢNG VIÊN

1. **Mục 1 — Mô tả:** Mô tả nghiệp vụ đời sống tự nhiên 100%, không lạm dụng CNTT, không đưa tên bảng/FK/khóa/giao diện; nêu bật khó khăn thực tế và **lĩnh vực cần tin học hóa**; tích hợp đầy đủ bán trực tiếp tại quầy, quy trình bảo hành, quy trình đổi trả hàng (theo đúng lời phê của Thầy).
2. **Mục 2 — Xác định 3 loại thực thể, thuộc tính:** Phân loại chuẩn xác thành 3 nhóm (Cơ bản, Đối tượng ngoài, Nghiệp vụ — có cột thuộc tính thời gian). Liệt kê đầy đủ thuộc tính, kiểu dữ liệu, miền giá trị. *Lưu ý: `ChiTiet...` là mối kết hợp, không phải thực thể; `TonKho` là thống kê, không phải thực thể.*
3. **Mục 3 — Xác định tập phụ thuộc hàm từng loại thực thể:** Viết rõ tân từ $\Vert Q \Vert$ cho từng quan hệ, giải thích quy tắc nghiệp vụ cho từng phụ thuộc hàm $X \to Y$.
4. **Mục 4 — Tìm phủ tối thiểu (PTT):** Thực hiện đầy đủ giải thuật 3 bước (B1: Tách vế phải $\to$ B2: Loại thuộc tính thừa vế trái bằng bao đóng $\to$ B3: Loại PTH dư thừa).
5. **Mục 5 — Tìm khóa:** Áp dụng thuật toán chia tập thuộc tính thành Nguồn ($N$), Trung gian ($M$), Đích ($D$), lập bảng tổ hợp các khóa ứng viên, xác định khóa tối tiểu và chọn Primary Key.
6. **Mục 6 — Vẽ ERD:** Mô hình thực thể – kết hợp hoàn chỉnh với đầy đủ các mối kết hợp (động từ), thuộc tính và **bản số $(\min, \max)$** ở cả 2 đầu liên kết.
7. **Mục 7 — Chuyển ERD sang mô hình quan hệ:** Áp dụng quy tắc chuyển đổi chuẩn, tuân thủ nghiêm ngặt quy ước trình bày của Thầy:
   - **<u>Gạch chân liền dưới khóa chính (Primary Key)</u>**
   - **<span style="text-decoration: underline dashed">Gạch nét đứt dưới khóa ngoại (Foreign Key)</span>**
   - *(Trong Microsoft Word: PK dùng Single Underline; FK dùng Dash Underline)*.
8. **Mục 8 — Xác định dạng chuẩn từng bảng $\to$ Dạng chuẩn chung của cả Lược đồ:** Xét tuần tự 1NF $\to$ 2NF $\to$ 3NF $\to$ BCNF cho từng bảng. Dạng chuẩn của cả hệ thống bằng $\min$ các bảng.

### Các nội dung nâng cao & điểm cộng (theo Hướng dẫn viết báo cáo của GV):
9. **Mục 9 — Cải tiến để đạt dạng chuẩn cao hơn & Điểm cộng 4NF:**
   - Dùng thuật toán phân rã (Delobel) hoặc tổng hợp (Bernstein).
   - **Chứng minh Bảo toàn phụ thuộc hàm** ($F' \equiv F$).
   - **Chứng minh Bảo toàn thông tin** (Bảng Tableau ma trận).
   - **Phát hiện và khử Phụ thuộc đa trị (MVD) để đạt Dạng chuẩn 4 (4NF) — Lấy trọn điểm cộng**: Áp dụng cho quan hệ Sản phẩm – Ảnh – Thông số kỹ thuật độc lập.
10. **Mục 10 — Đồ thị quan hệ & Con đường truy xuất:** Theo đúng Bài 9–11 Giáo trình CSDL-NC 2015. Xây dựng đồ thị quan hệ (nút bản lề $N_{bl}$), đồ thị con đường truy xuất thô (nút ngõ vào  , cung đơn $\to (1,1,1)$, cung kép $\twoheadrightarrow (1,-,n)$), và phân tích các chuỗi kết (Join paths) phục vụ các câu hỏi truy xuất thực tế.

---

## 2. NGUYÊN TẮC BẤT DI BẤT DỊCH CHO MỤC 1 (MÔ TẢ ĐỀ TÀI)

1. **Văn phong thuần túy nghiệp vụ đời sống 100%:**
   - Đóng vai chủ cửa hàng bán lẻ máy tính PowerTech mô tả cách vận hành hoạt động kinh doanh.
   - **TUYỆT ĐỐI CẤM:** Không xuất hiện các từ kỹ thuật CNTT/CSDL: `"bảng"`, `"table"`, `"FK"`, `"khóa"`, `"khóa ngoại"`, `"khóa ghép"`, `"màn hình"`, `"giao diện"`, `"nút bấm"`.
2. **Khắc phục triệt để lời phê của Giảng viên:**
   - Bắt buộc mô tả rõ nét **kênh bán lẻ trực tiếp tại quầy (mua tại cửa hàng)** song song với kênh bán trực tuyến.
   - Bắt buộc có quy trình **Tiếp nhận & Trả bảo hành** (căn cứ số seri, tem bảo hành, thời hạn chốt tại đơn mua gốc).
   - Bắt buộc có quy trình **Đổi trả hàng & Hoàn tiền** (hàng nhận lại phải đưa vào khu vực *"Chờ kiểm tra"*, tuyệt đối không tự động cộng vào tồn hàng mới).
3. **Mô tả đầy đủ các luồng dòng tiền và dòng hàng:**
   - Đặt cọc, giữ hàng (giữ hàng chưa xuất kho vật lý), thanh toán đa hình thức (tiền mặt, QR chuyển khoản, COD, ví).
   - Xử lý khi khách boom hàng, giao hàng thất bại (tối đa 3 lần).
   - Nhập hàng từ nhà cung cấp, kiểm đếm chênh lệch, đề nghị điều chỉnh kho.

---

## 3. NGUYÊN TẮC CHO MỤC 2 (3 LOẠI THỰC THỂ)

1. **Phân loại chuẩn 3 nhóm theo bài giảng:**
   - **Thực thể Cơ bản:** Tài nguyên nền tảng, có trước hệ thống, ổn định, *không có thuộc tính thời gian* (`LoaiSanPham`, `ThuongHieu`, `SanPham`, `DinhNghiaThongSo`, `VaiTro`).
   - **Thực thể Đối tượng ngoài:** Con người hoặc tổ chức (`NguoiDung`, `NhaCungCap`, `SoDiaChi`).
   - **Thực thể Nghiệp vụ:** Hồ sơ, chứng từ, sự kiện phát sinh khi vận hành, **bắt buộc luôn có thuộc tính thời gian** (`DonHang`, `PhieuNhap`, `ThanhToan`, `GiaoDichKho`, `YeuCauBaoHanh`, `YeuCauDoiTra`, `DanhGia`).
2. **CÁC ĐIỀU CẤM KỴ (TRÁNH BỊ TRỪ ĐIỂM):**
   - **`ChiTiet...` KHÔNG PHẢI LÀ THỰC THỂ:** `ChiTietDonHang`, `ChiTietPhieuNhap` là **Mối kết hợp (MKH)** mang thuộc tính giữa Đơn hàng/Phiếu nhập và Sản phẩm trong ERD. Tuyệt đối không xếp vào danh sách thực thể độc lập ở Chương 2.
   - **`TonKho`, `LichSu...` KHÔNG PHẢI LÀ THỰC THỂ:** Đây là dữ liệu thống kê/suy diễn, không được tạo thực thể. Quản lý kho thông qua thực thể nghiệp vụ `GiaoDichKho`.
   - Thuộc tính không được biến thành bảng (`GioiTinh`, `DiemDanhGia`).

---

## 4. QUYẾT ĐỊNH TỪ MỤC 8 ĐẾN MỤC 10

- **Mục 8:** giữ `HoTen` là một thuộc tính (phương án 1, không tách họ và tên); dạng chuẩn chung của lược đồ hiện trạng là 1NF (CHITIETTRA).
- **Mục 9:** chọn **phương án C** cho HANGCOSERI (tách thêm SERIMATHANG, BCNF và bảo toàn thông tin, bảo toàn PTH), giữ quy tắc "seri duy nhất theo mặt hàng" **[GT]**; bỏ cột MaDH khỏi CHITIETTRA và MaSP khỏi PHIEUBAOHANH; tình huống 4NF là ảnh – thông số của mặt hàng. Lược đồ sau cải tiến: 39 quan hệ, dạng chuẩn chung BCNF.
- **Mục 10:** áp dụng B1–B7 với sáu quy ước Q1–Q6 (khóa ưu tiên = khóa chính; cùng thuộc tính khi nối bằng khóa ngoại; khóa ngoại tới NHANVIEN và MaKH của HOSODOITRA, PHIEUBAOHANH là vai trò riêng; không gộp một–một tùy chọn; cung thừa chỉ xét qua đường bắt buộc; khuyên ngoài thuật toán). Điều kiện hình thức ở 9.5 của giáo trình bị lỗi định dạng nên dựa vào ví dụ. Quy ước dấu của sổ kho (GIAODICHKHO.SoLuong luôn dương) **chưa chốt**. Ngõ vào đề xuất ở 10.5.3 là giả thiết chờ xác nhận.

---

## 5. YÊU CẦU MỚI CỦA GIẢNG VIÊN (ghi 24/10/2026)

Nguồn: `CSDL-NC/yeu-cau-giang-vien/Cau truc bao cao mon CSDL Nang cao.md` (+ `.pptx`, file ngày 21/10) và báo cáo mẫu `BaoCaoCSDLNC_ThamKhao.docx` (file ngày 24/10). Theo thứ tự ưu tiên của AGENTS.md, đề cương này đứng trên khung 10 mục ở phần 1.

**Đề cương 7 mục:** (1) mô tả tóm tắt bài toán; (2) 3 loại thực thể và thuộc tính; (3) tập PTH cho từng lược đồ và khóa; (4) dạng chuẩn từng lược đồ, phân rã/tổng hợp để đạt BCNF (ít nhất 3NF), kiểm tra bảo toàn thông tin và PTH; (5) phụ thuộc đa trị → 4NF (không có thì bỏ qua); (6) đồ thị quan hệ, các con đường truy xuất **và ngữ nghĩa từng con đường**; (7) truy vấn SQL **cho các truy xuất đó**. Nhóm 1–3 SV (nhóm 6 có 3 SV, không bị nâng yêu cầu).

**Đối chiếu với bản nộp (mục 1–10):**

| Đề cương | Đã có ở | Ghi chú |
|---|---|---|
| 1, 2, 3, 4, 5 | Mục 1, 2, 3–5, 8–9, 9 | Đủ. ERD (mục 6–7) không bắt buộc nhưng báo cáo mẫu có ERD nên giữ. |
| 6 | 10.4, 10.5.2 | Đủ. |
| 7 | 10.6 (K1–K7) | **Cần kiểm tra:** đề cương đòi SQL cho *các con đường truy xuất* ở mục 6; K1–K7 là 7 yêu cầu khai thác, chưa chắc phủ hết các đường trong 10.5.2. |

**Báo cáo mẫu có mà bản nộp chưa có:** Lời mở đầu, Lời cảm ơn, Lời cam đoan; khảo sát thực trạng, tính khả thi, đối tượng sử dụng, mục tiêu nghiên cứu; Chương Kết luận và kiến nghị (ưu/nhược điểm, tính năng đã/chưa làm, hướng phát triển); Tài liệu tham khảo. Mẫu chia 4 chương (Tổng quan, Cơ sở lý thuyết, Kết quả thực nghiệm, Kết luận); chưa có quyết định đổi cách đánh số mục 1–10 sang chương.

