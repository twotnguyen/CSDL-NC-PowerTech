# Ghi chú Bài học và Kiến thức: `Do_thi_va_CDTX.docx` & `Do thi quan he.pptx` (Cập nhật 27/10/2026)

Tài liệu mới nhất do Thầy cung cấp bổ sung các bài tập thực chiến, bài giải mẫu và ảnh chụp trực tiếp từ bài giảng trên lớp về Đồ thị quan hệ, Con đường truy xuất và Mô hình ERD.

---

## 1. Bản chất & Động cơ của Đồ thị quan hệ (Bài 9, 10, 11 Giáo trình 2015)
- Thao tác tốn kém nhất trong CSDL quan hệ là phép kết (`JOIN`). Hệ quản trị CSDL dựa vào chỉ mục (`Index`) để tăng tốc phép kết.
- Tạo quá ít index $\to$ quét toàn bảng (Table Scan, rất chậm). Tạo quá nhiều index $\to$ tốn dung lượng và chi phí bảo trì khi thêm/sửa/xóa.
- **Mục tiêu của Đồ thị:** Làm nổi bật các thuộc tính chung (nơi diễn ra phép kết), từ đó xác định số lượng chỉ mục tối thiểu nhưng đủ dùng, và chỉ ra các con đường truy xuất tối ưu (`Join Paths`) cho các câu hỏi nghiệp vụ.

---

## 2. Các bài tập mẫu và bài học kỹ thuật rút ra

### 2.1. Bài tập 1: Đánh giá trùng lắp thông tin & Khử cung thừa bắc cầu
- Lược đồ: $Q_1(\underline{A}, D)$, $Q_2(\underline{B}, E, G)$, $Q_3(\underline{A}, \underline{B}, G, H)$, $Q_4(\underline{C}, M)$, $Q_5(\underline{B}, \underline{C}, N, A)$.
- **Trùng lắp thông tin:** Xảy ra tại thuộc tính $G$ của $Q_2$ và $Q_3$.
  - Trong $Q_2$: $B$ là khóa $\implies B \to G$ (đã lưu trọn vẹn quan hệ giữa $B$ và $G$).
  - Trong $Q_3$: Khóa là $\{A, B\}$, $G$ phụ thuộc vào một phần của khóa là $B$ ($B \to G$) $\implies Q_3$ chỉ đạt 1NF (vi phạm 2NF), khiến giá trị $G$ bị lặp đi lặp lại nhiều lần theo từng dòng $B$ kết hợp với các $A$ khác nhau.
- **Khử cung thừa bắc cầu tại $Q_5$:**
  - $Q_5$ chứa thuộc tính của cả 4 quan hệ $\{1, 2, 3, 4\}$.
  - Nút 1 và nút 2 bị thừa trong $PTH(N_5)$ vì đã đi bắc cầu qua nút trung gian 3 ($5 \to 3 \to 1$ và $5 \to 3 \to 2$).
  - Nút 2 vẫn được giữ lại làm cung chính thức nhờ quan hệ lồng khóa $LK(N_5) = \{2, 4\}$ (vì khóa $\{B, C\}$ chứa khóa $\{B\}$).
  - Kết quả tạo cung: $\text{Cung}(N_5) = \{2, 3, 4\}$.

### 2.2. Bài tập 3 (10 quan hệ): Kỹ thuật tạo Nút bản lề (Hinge Nodes - Bước 3)
- Khi giao thuộc tính giữa hai quan hệ $Q_i \cap Q_j$ sinh ra một tập thuộc tính khóa mà **chưa có bất kỳ quan hệ nào trong CSDL nhận làm khóa chính**, thuật toán bắt buộc phải **tạo một nút bản lề mới**:
  - $Q_1 \cap Q_4 = \{B\} \implies$ Tạo nút bản lề $Q_{14}(B)$.
  - $Q_3 \cap Q_5 = \{C\} \implies$ Tạo nút bản lề $Q_{35}(C)$.
  - $Q_4 \cap Q_5 = \{E\} \implies$ Tạo nút bản lề $Q_{45}(E)$.
  - $Q_5 \cap Q_9 = \{G\} \implies$ Tạo nút bản lề $Q_{59}(G)$.
- Các nút bản lề này chỉ bị hủy ở Bước 5 nếu chúng chỉ có đúng 1 cung đi vào; nếu có từ 2 cung đi vào trở lên thì bắt buộc phải giữ lại.

### 2.3. Bài tập 4: Bài toán Giải bóng đá 7 quan hệ
- Minh họa hoàn chỉnh chu trình: Lập bảng ma trận tạo cung 6 cột $\to$ khử các cung bắc cầu thừa $\to$ xác định ngõ vào (Nút 3 và 4) $\to$ phân tích con đường truy xuất $\to$ viết câu lệnh SQL minh họa.

---

## 3. Kiến thức từ 3 hình ảnh gốc đính kèm

1. **Ảnh bảng phấn (`img_2.png`): Mô hình ERD quan niệm Merise chuẩn:**
   - 4 thực thể: `Thẻ`, `KH` (Khách hàng), `Hóa đơn`, `MH` (Mặt hàng).
   - Mối kết hợp: `Của`, `Có`, và `CTHD` (Chi tiết hóa đơn mang thuộc tính *Số lượng, Đơn giá, Thành tiền*).
   - Bản số $(\min, \max)$ rõ ràng: $(1, 1), (0, 1), (1, n)$.
   $\implies$ **Mẫu chuẩn để vẽ ERD ở Chương 1 (Mục 1.6 / Mục 6).**

2. **Ảnh Case Studio / IDEF1X (`img_1.png`): Chuyển ERD sang quan hệ logic:**
   - Phân biệt rõ ràng giữa **Khóa chính (PK)**, **Khóa ngoại (FK)**, và **Khóa kết hợp vừa là PK vừa là FK (PFK)** trong các bảng trung gian như `CTHD(SOHD (PFK), MAMH (PFK), SL, Gia, ThanhTien)`.

3. **Ảnh giải tay (`img_0.png`): Thuật toán tối giản đồ thị có hướng:**
   - Các bước kiểm tra giao khóa ở B3 và bảng lọc cung B4 để đảm bảo đồ thị tối giản, không bị rối bởi các cung thừa bắc cầu.

---

## 4. Áp dụng trực tiếp vào Đồ án PowerTech

- **Mục 6 (ERD):** Vẽ đầy đủ thực thể (hình chữ nhật), mối kết hợp (hình thoi động từ), thuộc tính và bản số $(\min, \max)$ theo chuẩn Merise như ảnh bảng phấn của Thầy. Các bảng chi tiết (`ChiTietDonHang`, `ChiTietPhieuNhap`) được thể hiện đúng là Mối kết hợp mang thuộc tính.
- **Mục 7 (Chuyển quan hệ):** Đúng quy ước: <u>Khóa chính gạch liền</u>, <span style="text-decoration: underline dashed">Khóa ngoại gạch đứt</span>.
- **Mục 8 & 9 (Dạng chuẩn & Chuẩn hóa):** Nắm rõ cơ chế vi phạm 2NF do phụ thuộc bộ phận (như $B \to G$) để đưa ra phương án phân rã đạt BCNF và chứng minh bằng bảng Tableau.
- **Mục 10 (Đồ thị quan hệ & Con đường truy xuất):** Lập Bảng ma trận tạo cung 6 cột chuẩn mực; xác định các nút ngõ vào ( ) và viết các câu lệnh SQL minh họa tương ứng.
