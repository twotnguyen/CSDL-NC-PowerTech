# Chấm điểm báo cáo mẫu `BaoCaoCSDLNC_ThamKhao` theo đề cương 7 nội dung (31/10/2026, chấm lại 01/11/2026)

Vai: người chấm. Đối tượng: `CSDL-NC/bao-cao-mau/BaoCaoCSDLNC_ThamKhao.md` và `.docx` (hai bản cùng nội dung; `.md` cắt hình nên hình xem từ `.docx`). Đối chiếu: `Cau truc bao cao mon CSDL Nang cao.md` (7 nội dung) và `Huong_dan_cach_viet_bao_cao_CSDLNC.md`. Bổ sung cho `03_danh_gia_bao_cao_mau_va_bai_hoc.md` (24/10); mục này kiểm lại bằng script và xem từng hình. Điểm dưới đây là bản chấm lại ngày 01/11/2026.

**Giới hạn.** Thang điểm và trọng số bên dưới là của tôi, không phải của thầy; cột điểm trong `23DTHD6.xlsx` chưa rõ nghĩa. Đã đọc toàn bộ Chương 1, 2.1.1–2.1.2, 2.3.23, Chương 3–4, đọc kỹ một số trong 22 mục phân tích quan hệ (các mục còn lại lặp cùng một khuôn) và liệt kê tập F của cả 22; xem đủ 11 hình nội dung (ERD, Toad, Class, 6 Use Case, hai đồ thị). Chưa chạy SQL của mẫu vì báo cáo không kèm dữ liệu; lỗi đường 38 và 45 suy từ lược đồ. Nhãn: **[kiểm]** đã kiểm bằng script hoặc đối chiếu hai chỗ trong báo cáo; **[nhận định]** suy luận của tôi.

## 1. Điểm theo từng yêu cầu (thang 10)

| # | Yêu cầu | Điểm | Căn cứ chính |
|---|---|---|---|
| 1 | Mô tả tóm tắt bài toán | **7,0** | Rất chi tiết, có quy tắc đo được (mã sinh viên 10 chữ số, lớp tối đa gần 60 sinh viên, mật khẩu tối thiểu 8 ký tự). Nhưng không "tóm tắt" (khoảng 25 đoạn), lẫn thuật ngữ kỹ thuật (UUID 36 ký tự, API, Website/Mobile, Google Drive, "hệ thống Scan") |
| 2 | Ba loại thực thể và thuộc tính | **7,0** | Đủ ba loại, mỗi thực thể ghi thuộc tính và ý nghĩa; thuộc tính có hậu tố phân biệt; `CHITIET…` và `KETQUASINHVIEN` vẽ là mối kết hợp. Thiếu lý do xếp loại; mục 1.7.1 chỉ có hình, không phân tích; `LOAIDIEM` xếp "nghiệp vụ" chỉ vì có thời gian tạo |
| 3 | Phụ thuộc hàm và khóa từng lược đồ | **4,5** | **[kiểm]** Cả 22 tập F đều dạng `khóa → mọi thuộc tính`, **không có khóa ngoại nào nằm trong F**. Khóa ứng viên duy nhất là khóa chính; email, số điện thoại, mã nhân viên có quy tắc đặt mã không được xét. Phủ tối thiểu sai ở bước 2 của KETQUASINHVIEN |
| 4 | Dạng chuẩn, phân rã/tổng hợp, bảo toàn | **3,0** | **[kiểm]** Bảng 2.3.23 ghi 4 quan hệ `CHITIET…` là **3NF** nhưng kết luận ngay dưới "Min(Qᵢ) = BCK". Hai câu này mâu thuẫn nhau. Theo phép thử của thầy, nhiều cột chưa đạt DC1 (F13) nên kết luận BCK không vững. Không có phân rã, tableau hay kiểm tra F' ≡ F, dù mục 1.5 hứa "xây dựng phép kết bảo toàn thông tin" |
| 5 | Phụ thuộc đa trị, dạng chuẩn 4 | **3,0** | Đề cương cho phép bỏ qua nếu không có, nhưng báo cáo hứa ở 1.5 mục 7 rồi không nói gì: không nêu "không có vì sao", trong khi các cột `CacDuongDan…` là ứng viên đa trị |
| 6 | Đồ thị quan hệ, đường truy xuất, ngữ nghĩa | **7,5** | **[kiểm]** Làm đủ B1–B7; 31 quan hệ cung khớp 31 cung trong Hình 3.1; Hình 3.2 có cung vô hướng 5—19; mỗi đường một câu "Cho biết…". Nhưng B3 thiếu 16 trên 73 cặp (F14) và ngữ nghĩa đường 65–69 sai (F15). Thiếu: lý do chọn nút vào, (m, A, M), tên quan hệ cạnh số nút |
| 7 | Truy vấn SQL cho các truy xuất | **4,0** | Câu nói "mỗi đường một câu lệnh" nhưng chỉ có **5 trên 69**; còn lại ghi "tương tự". Một câu không chạy được, một câu gõ sai tên bảng. Không có truy vấn thống kê/khai thác dù 1.5 mục 10 hứa |

**Điểm trung bình đều các mục: 5,1** (bản 31/10: 5,4). Nếu chấm nặng mô tả và ERD như cách thầy đã nhận xét lớp D6 (các nhóm đó nhận 6–7) thì báo cáo này ước **6,5**. Nếu chấm nặng phần kỹ thuật thì **5,0–5,5**. **Ước lượng chung: 6,0, loại trung bình khá.** Vì đây là báo cáo thầy gửi làm mẫu, điểm thực tế có thể cao hơn. Rất chi tiết về hình thức nhưng độ chắc thấp. Điểm cao do phần mô tả, ERD và đồ thị; điểm thấp do phần phụ thuộc hàm, dạng chuẩn và SQL.

## 2. Quy mô của đề tài

**[nhận định]** Quy mô **trung bình về số bảng, cơ bản về độ sâu.**

- 22 quan hệ (17 thực thể + 5 mối kết hợp), 31 cung, 69 đường. Không nhỏ, nhưng cùng một khuôn nên dễ làm.
- Phụ thuộc hàm đều đơn giản (khóa → thuộc tính), không có khóa kép thú vị, không có phụ thuộc bắc cầu, không có phụ thuộc đa trị. Vì vậy phần chuẩn hóa rất nhẹ: "mọi bảng đạt BCK" là kết luận gần như hiển nhiên.
- Độ rộng nghiệp vụ lớn: quản lý lớp học kiểu Google Classroom gồm bài tập, nhóm, dự án, nhiệm vụ, bài đăng, bình luận, thêm "hệ thống Scan điểm". Thầy từng phê "Quá LIỀU" (gara, vì thêm giao tác và khóa) và "làm không nổi" (siêu thị). Với mẫu này, nguy cơ "rộng nhưng nông".
- Rất dễ bị hỏi khó ở **tính nhất quán** (mô tả với ERD, ERD với F, bảng với kết luận) hơn là ở lý thuyết.

## 3. Sơ đồ: lỗi và điểm yếu

### 3.1 Hình 1.1 (ERD tổng quát)

| # | Lỗi hoặc điểm yếu | Mức |
|---|---|---|
| E1 | `KẾT QUẢ SINH VIÊN` và `CHI TIẾT NHÓM` (mối kết hợp, hình oval xanh) bị nối thêm một oval khác ("Thuộc" tới LOẠI ĐIỂM; "Cấp bậc" tới VAI TRÒ NHÓM): **mối kết hợp nối với mối kết hợp** không có trong ERD chuẩn. Đúng ra là một mối kết hợp ba nhánh | **[kiểm]** sai ký hiệu |
| E2 | `CHI TIẾT NHIỆM VỤ`: phía NHIỆM VỤ ghi **(0,n)**, nhưng 1.4 viết nhiệm vụ "được giao cho một hoặc nhiều thành viên" → phải (1,n). Trong khi CHI TIẾT BÀI TẬP ghi (1,n) cho đúng ý đó | **[kiểm]** mâu thuẫn mô tả–hình |
| E3 | NHÂN VIÊN–KHOA và NHÂN VIÊN–CHỨC VỤ đều **(1,1)**, nhưng 1.4 viết giảng viên "kiêm nhiệm nhiều chức vụ, làm việc tại nhiều khoa" | **[kiểm]** mâu thuẫn mô tả–hình |
| E4 | KHOA và CHỨC VỤ có min = 1 phía nhân viên: không tạo được khoa hoặc chức vụ mới khi chưa có nhân viên | **[nhận định]** nên (0,n) |
| E5 | Tên mối kết hợp: "Cấp bậc" là danh từ và dùng hai lần cho hai ý khác nhau; "Chứa" 7 lần, "Tổ chức" 3 lần | **[kiểm]** vi phạm "đặt tên bằng động từ" |
| E6 | BÀI ĐĂNG và CÂU NHẬN XÉT: hai nhánh tới SINH VIÊN và NHÂN VIÊN đều (0,1); "đúng một trong hai" chỉ ghi ở chữ, hình không thể hiện | **[kiểm]** |
| E7 | CHI TIẾT NHÓM: SINH VIÊN ghi (0,n), mô tả viết "một sinh viên chỉ thuộc một nhóm" (trong một phòng học); khóa (SV, Nhóm) không bảo đảm điều này | **[nhận định]** |
| E8 | LỚP HỌC không nối với NGÀNH hay KHOA dù tên lớp mã hóa ngành; SINH VIÊN lại nối thẳng KHOA | **[nhận định]** xem F3 |
| E9 | Nhiều đường chéo dài, giao nhau (nhất là các đường từ SINH VIÊN, NHÂN VIÊN–BÀI ĐĂNG) | **[kiểm]** khó đọc, không phải lỗi logic |
| E10 | KẾT QUẢ SINH VIÊN và CÂU TRẢ LỜI nối thẳng tới SINH VIÊN, PHÒNG HỌC, BÀI TẬP (cả Hình 1.2), không qua `CHITIETPHONGHOC`, `CHITIETBAITAP`, trong khi đồ thị đi 11→9 và 14→13. Khóa ngoại không ngăn được điểm của sinh viên không học phòng đó | **[kiểm]** lệch giữa ERD và đồ thị |

### 3.2 Các hình khác

| Hình | Lỗi hoặc điểm yếu |
|---|---|
| 1.2 (Toad) | Hợp lệ về khóa/khóa ngoại, nhưng không có bản số; không giải thích khác gì Hình 1.1. Xem E10 |
| 2.1 (Class) | **[kiểm]** Khóa của NHIEMVU và CHITIETNHIEMVU ghi `MaNV: Guid`, trùng tên với `MaNV: string` của NHANVIEN. Tên thuộc tính khác với mô hình quan hệ (`MaCV`/`MaChucVu`, `MaLH`/`MaLopHoc`, `MaBT`/`MaBaiTap`, `MaCTL`, `MaVTN`, `MaNVQL`). Mọi lớp có phương thức giả `+PhuongThuc()`; giới tính là enum nhưng Toad và bảng 2.1.3 ghi Integer. Môn này không yêu cầu sơ đồ lớp, và nó chưa khớp lược đồ |
| 2.2 (Use case tổng quát) | **[nhận định]** Quản trị viên vẽ là một dạng của Nhân viên, trong khi 1.4 viết quản trị viên "không có quyền truy cập dữ liệu nội bộ". Mũi tên từ Sinh viên vào use case "Quản lý đối tượng ngoài" không theo ký hiệu UML |
| 2.3–2.7 (Use Case chi tiết) | **[kiểm]** Dùng `<<extend>>` cho các chức năng cốt lõi (extend vốn là tùy chọn). Mọi loại nhân viên cùng một quyền, trái phân quyền ở 1.4. **[kiểm]** Hình 2.5 không nối Sinh viên dù sinh viên nộp bài, đăng bài, nhận xét; cũng không có chức năng cập nhật kết quả sinh viên |
| 3.1 | **[kiểm]** 31 cung khớp với danh sách quan hệ cung. Hình chỉ có số nút, không có tên quan hệ, không có (m, A, M) |
| 3.2 | **[kiểm]** Cung vô hướng 5—19 (đỏ) đúng với việc thay nút 20 theo B7. Số "5 nút vào" khớp hình, nhưng không giải thích vì sao chọn |

## 4. Lỗi nội dung đã kiểm

| # | Lỗi | Căn cứ |
|---|---|---|
| F1 | **Bảng 2.3.23 mâu thuẫn kết luận:** 4 quan hệ `CHITIET…` ghi 3NF, kết luận Min(Qᵢ) = BCK | Bảng 2.3.23 và câu dưới nó. Kết luận đúng theo định nghĩa phải là BCNF cho quan hệ chỉ có khóa; vấn đề là hai câu không thể cùng đúng |
| F2 | **Phủ tối thiểu sai** (KETQUASINHVIEN): F = {SV, PH, LĐ → Điểm}; bước 2 tách thành {SV → Điểm; PH → Điểm; LĐ → Điểm}. Không thuộc tính nào ở vế trái là thừa; ba PTH mới sai về nghiệp vụ. Và 2.3.11 vẫn viết "đạt 2NF" ngay sau đó | 2.3.11 dòng 1278–1286 |
| F3 | **F không chứa khóa ngoại.** Ví dụ NHANVIEN có 10 thuộc tính nhưng F chỉ có 7; PHONGHOC bỏ `MaHocPhan, MaLopHoc, MaNhanVien`; CAUTRALOI bỏ `MaBaiTap, MaSoSinhVien`. Phân tích dạng chuẩn thực chất làm trên quan hệ khác với lược đồ. **[nhận định]** Có một PTH ẩn rất có thể đúng: lớp thuộc một ngành/khoa nên `MaLopHoc → MaKhoa`; khi đó SINHVIEN (có `MaLopHoc` và `MaKhoa`) không đạt 3NF | 2.3 so với 2.1.2 |
| F4 | **Quy tắc đặt mã nhân viên không bảo đảm duy nhất:** chữ cái đầu họ-tên lót-tên cộng ngày, tháng, hai chữ số năm sinh; hai người cùng chữ viết tắt và cùng ngày sinh sẽ trùng. Mã còn chứa sẵn ngày sinh (thông tin dư) | 1.4 và 2.1.1 |
| F5 | **SQL đường 38** (`19 ⭢ 5 ⭢ 1`): `NHIEMVU NV JOIN SINHVIEN SV ON NV.MaSoSinhVien = …` nhưng NHIEMVU không có cột `MaSoSinhVien` (sinh viên–nhiệm vụ nằm ở CHITIETNHIEMVU, chính là quan hệ của cung vô hướng). Không chạy được. Đường 45 viết tên bảng `CAUNHATXET` | 3.3 |
| F6 | **Thiếu một đường truy xuất:** tính lại bằng script từ Hình 3.2, các đường cực đại từ 5 nút vào là **70**, báo cáo liệt kê **69**. Thiếu `11 ⭢ 10` (kết quả sinh viên – loại điểm). 69 đường còn lại khớp đúng | script (đồ thị đọc từ hình, khuyên 3→3 coi là bước kết thúc) |
| F7 | **Mô tả không "tóm tắt" và có thuật ngữ kỹ thuật** (UUID, API, Google Drive, "hệ thống Scan") — đúng loại lỗi thầy đã phê ở D5 ("chưa lạm dụng CNTT khi mô tả") | 1.2, 1.4, 2.1.1 |
| F8 | Số bảng không nhất quán: 2.1.1 ghi "21 bảng", liệt kê 22; "FNHANVIEN" dán nhầm vào mục KHOA; câu "Q₈ ⋂ Q₁₂" lặp ở 3.1 bước 3 | 2.1.1, 2.3.1, 3.1 |
| F9 | **Chương 4 là của đồ án phần mềm,** không phải của môn CSDL: "tính năng đã/chưa phát triển được", "triển khai lên AWS, Azure" | Chương 4 |
| F10 | **Đính chính 01/11: không phải lỗi, rút lại.** Bản 31/10 cho rằng coi `22 ⭢ 5` không thừa trong khi `21 ⭢ 5` thừa là chưa nhất quán. Theo quy tắc `PTH_Thừa` của chính báo cáo (dòng 2018), `21 ⭢ 5` thừa vì khóa của nút 9 chứa `MaSoSinhVien`, còn nút 22 không có nút nào như vậy, nên hai kết luận nhất quán | 3.1 dòng 2018 và bảng bước 4 |
| F11 | **Lý do "không đạt BCK" sai ở 4 quan hệ `CHITIET…`** (PHONGHOC, BAITAP, NHOM, NHIEMVU): báo cáo viết không đạt BCK "do … không có phụ thuộc hàm". Đây là nguồn của mâu thuẫn F1. BCK đòi mọi PTH không hiển nhiên có vế trái là siêu khóa; F rỗng thì không có PTH nào vi phạm, nên điều kiện đúng hiển nhiên và quan hệ đạt BCK | `BaoCaoCSDLNC_ThamKhao.md` dòng 1210, 1376, 1542, 1663 |
| F12 | **Quan hệ cung Q14.13 thiếu `MaBaiTap`:** công thức của chính báo cáo là Qij = Qi[KQi⁺ ∪ KQj⁺], khóa của Q13 là (MaSoSinhVien, MaBaiTap), nên phải là Q14.13(MaCauTraLoi, MaSoSinhVien, MaBaiTap), nhưng báo cáo ghi (MaCauTraLoi, MaSoSinhVien). Nối theo `MaSoSinhVien` một mình thì câu trả lời khớp với mọi bài tập của sinh viên đó | 3.1, dòng 2053 và 2091 |
| F13 | **Chưa đạt DC1 theo phép thử của thầy, dù mọi mục ghi "thuộc tính đơn":** `CacDuongDanBT`, `CacDuongDanCTL`, `CacDuongDanBD` chứa danh sách đường dẫn (tối đa 2000 ký tự); `LuongTietHoc` gộp tiết bắt đầu và kết thúc; `SoPhongHoc` gộp khu, tầng, phòng | 2.1.1 dòng 419, 439, 449, 484; 2.3.12 |
| F14 | **B3 chưa xét đủ:** script tính ra 73 cặp có giao, báo cáo thiếu 16 cặp (3-5, 3-6, 5-6, 5-8, 8-11, 8-22, 9-20, 9-22, 11-20, 11-22, 12-15, 12-21, 14-21, 14-22, 15-21, 17-18). Có dòng vô nghĩa `Q3 ⋂ Q3`, `Q11 ⋂ Q11`, một dòng lặp Q8 ⋂ Q12, và hai giao ghi thiếu thuộc tính (Q8 ⋂ Q21, Q21 ⋂ Q22). Kết luận không tạo nút bản lề có thể vẫn đúng, nhưng phép chứng minh chưa đủ | 3.1 dòng 1847–1965; script |
| F15 | **Ngữ nghĩa sai ở đường 65–69:** mạch đi 9 ⭢ 8 nhưng câu diễn giải nói về nhiệm vụ, dự án, nhóm, các nút không có trên đường (chép từ đường 60–64) | 3.2 dòng 2203–2207 |
| F16 | **Điểm bị xóa theo phòng học:** 1.3 nói giữ bảng điểm 5 năm sau tốt nghiệp, 1.4 nói phòng học bị xóa sau học kỳ, nhưng `KETQUASINHVIEN` có khóa chứa `MaPhongHoc` và không có quan hệ nào lưu điểm sau khi xóa | 1.3 dòng 260; 1.4 dòng 285, 295, 313 |
| F17 | **Thông tin mô tả nhưng không có nơi lưu:** mật khẩu tài khoản sinh viên, nhân viên; mã, email, mật khẩu của quản trị viên | 1.4 dòng 272, 283 so với 2.1.2 |
| F18 | **Mô tả tự mâu thuẫn:** lớp "ít nhất 60 người" và "tối đa gần 60 sinh viên"; mã ngành là chuỗi theo Bộ Giáo dục nhưng ở quan hệ là số tự tăng; giới tính "Nam/Nữ/Khác" nhưng kiểu Integer | Dòng 227 và 293; 289 và 410; 395 và 544 |
| F19 | **Bố cục:** Chương 2 tên "Cơ sở lý thuyết" nhưng không có lý thuyết; `ThoiGianCapNhapLD` viết khác `ThoiGianCapNhatLD` | Chương 2; dòng 427, 429 |

Điều **không** tính là lỗi của nhóm: "Boyee-Codd-Kent" xuất hiện y nguyên trong `Bai 4.md` của bài giảng.

## 5. Câu hỏi vấn đáp dễ bị hỏi

1. "SINH VIÊN vừa có lớp vừa có khoa: khoa có suy ra được từ lớp không? Nếu có, bảng này đạt dạng chuẩn nào?" (E8, F3)
2. "Bảng 2.3.23 ghi 3NF mà kết luận BCK. Em giải thích thế nào?" (F1, F11)
3. "Vì sao F không có `MaHocPhan`, `MaLopHoc` của PHONGHOC? Quan hệ em phân tích có phải quan hệ trong lược đồ không?" (F3)
4. "Làm lại bước 2 của phủ tối thiểu cho KETQUASINHVIEN bằng bao đóng." (F2)
5. "Hai nhân viên cùng chữ viết tắt, cùng ngày sinh thì mã ra sao?" (F4)
6. "Có phụ thuộc đa trị không? Nếu không, giải thích vì sao." (nội dung 5)
7. "Mô tả nói giảng viên làm nhiều khoa nhưng bảng chỉ có một `MaKhoa`." (E3)
8. "Chạy giúp thầy câu SQL của đường 38." (F5)
9. "NHIỆM VỤ có thể không có thành viên nào được giao không?" (E2)
10. "`CacDuongDanBT` chứa nhiều đường dẫn, sao gọi là thuộc tính đơn?" (F13)
11. "Xóa phòng học thì điểm lưu ở đâu, khi phải giữ 5 năm?" (F16)

## 6. Điều rút ra cho báo cáo của nhóm

Kiểm ngày 01/11/2026 trên `PowerTech_CSDLNC_Bao_cao_ghep.docx` (sau khi sửa ba lỗ hổng, `QUYET_DINH.md` mục 14). Nhãn: **[kiểm]** đã chạy script hoặc đối chiếu trực tiếp; **[nhận định]** suy luận của tôi.

**Kết luận.** Nhóm đã tránh được các lỗi tính toán nặng của mẫu. Rủi ro còn lại giống mẫu ở **tiêu chí DC1 chưa nhất quán, mô tả còn dài, sơ đồ Use Case phân quyền chưa khớp mô tả, và ngữ nghĩa đường truy xuất ghép máy móc**. Mẫu nên học về bố cục, không học về cách phân tích.

### 6.1 Đối chiếu từng lỗi của mẫu

| Lỗi của mẫu | Báo cáo nhóm | Kết quả |
|---|---|---|
| F không chứa khóa ngoại (F3) | F tính trên đủ thuộc tính của quan hệ | **Đã tránh** [kiểm] |
| Chỉ xét khóa chính | Xét mọi khóa ứng viên, ví dụ HANGCOSERI có 4 khóa, CHITIETTRA có 2 khóa | **Đã tránh** [kiểm] |
| Phủ tối thiểu sai, bảng mâu thuẫn kết luận (F1, F2, F11) | 2.2.27 và kiểm tra độc lập khớp nhau: ban đầu 20 BCNF, 1 3NF, 1 2NF, 1 1NF, 2 chưa 1NF; sau cải tiến 26 BCNF | **Đã tránh** [kiểm] |
| Không phân rã, không kiểm tra bảo toàn | Có phân rã, tổng hợp, bảng a/b và F' ≡ F | **Đã tránh** [kiểm] |
| Bỏ qua phụ thuộc đa trị | Có tình huống 4NF, nhưng là quan hệ giả định, lược đồ thật không chứa R₂ | **Tốt hơn mẫu, vẫn có thể bị hỏi** |
| B3 thiếu cặp (F14) | Bảng 3.1 đủ 64 cặp theo quy ước Q2; 3 cặp có hai dòng vì giao tách thành hai khóa. Đếm theo tên cột thì là 125 cặp, vì các cột `MaNV` vai trò không tính là cùng thuộc tính | **Đúng, thiếu câu giải thích** [kiểm] |
| Thiếu đường, ngữ nghĩa chép sai (F6, F15) | 57 đường, tính lại độc lập khớp. Ngữ nghĩa sinh từ đúng các cung của đường nên không lệch như đường 65–69 của mẫu | **Đã tránh** [kiểm], nhưng câu dài và máy móc |
| SQL thiếu và lỗi (F5) | 57 + 9 câu chạy trên SQLite có bật khóa ngoại, đều có kết quả | **Đã tránh** [kiểm]; chưa chạy trên SQL Server |
| Quan hệ cung thiếu thuộc tính (F12) | Bảng quan hệ cung sinh từ khóa bằng chương trình | **Đã tránh** [nhận định], chưa soát từng dòng |
| Số liệu lệch giữa các chương (F8) | Không còn 41 cung, 9 nút vào, 36 mối kết hợp, 63 cặp trong bản ghép; Bảng 1.1 có đủ 42 dòng | **Đã tránh** [kiểm]; mục lục còn cũ đến khi cập nhật trường |
| Chương 2 sai tên, Chương 4 của đồ án phần mềm (F9, F19) | Chương 2 "Thiết kế và chuẩn hóa"; Chương 4 đối chiếu 7 nội dung | **Đã tránh** [kiểm] |
| Thông tin không có nơi lưu (F17) | Đã vá ba chỗ: chiếc seri trả, thời hạn chốt, nguồn hoàn. Còn thiếu liên kết hồ sơ đổi hàng với đơn mới | **Còn một chỗ** [kiểm] |
| Xóa dữ liệu làm mất lịch sử (F16) | Không xóa nhưng tương tự: bán lại hàng trả về ghi đè `HANGCOSERI.MaDH` | **Còn rủi ro** [kiểm] |
| Lược đồ chưa đạt DC1 thật (F13) | Tách họ tên, nhưng còn các cột dưới đây | **Còn rủi ro** [kiểm] |
| Mối kết hợp nối mối kết hợp (E1) | Vẫn có ở HÀNG CÓ SERI, PHIẾU BẢO HÀNH, CHI TIẾT TRẢ với CHI TIẾT ĐƠN HÀNG | **Cùng lỗi** [kiểm], đã có câu trả lời ở file 10 |
| Use Case cho mọi nhân viên cùng quyền | Không dùng `<<extend>>`, nhưng 6 chức vụ đều kế thừa Nhân viên và cùng nối 5 nhóm chức năng ở Hình tổng quát. Đường tới "Thống kê" đi xuyên oval "Tìm kiếm" | **Cùng lỗi** [kiểm] |
| Mô tả không tóm tắt (F7) | Mục 1.4 khoảng 4.450 từ, dài hơn mẫu 4.040; còn 17 lần chữ "giả thiết", mã G1–G6, nhắc "Chương 2", "lược đồ" | **Cùng lỗi, nặng hơn về độ dài** [kiểm] |

### 6.2 Việc nên làm, theo thứ tự

1. **Thống nhất tiêu chí DC1.** Báo cáo tách họ tên vì phải dùng một phần giá trị, nên phải trả lời được cho các cột sau:
   - `PhuKienDiKem`: là danh sách, thuộc loại lỗi F13 của mẫu. Nên đổi thành mô tả tự do hoặc nêu rõ không tra cứu từng phụ kiện.
   - `DiaChiGiao`: mô tả nói phí giao tính theo khu vực, tức phải dùng một phần địa chỉ. Nên tách khu vực hoặc bỏ câu đó.
   - `TenNguoiNhan`, `NguoiLienHeNCC`: nêu lý do không tách, vì cửa hàng không tìm theo tên gọi ở hai cột này.
2. **Xử lý bán lại hàng trả về.** Cách nhẹ: nói rõ `HANGCOSERI.MaDH` là lần bán gần nhất, lịch sử xem ở `CHITIETTRA` và `PHIEUBAOHANH`, đường đúng từ phiếu tới người mua là 25 → 13, rồi sửa câu 6.8 của file 10. Cách đầy đủ: tách quan hệ chiếc hàng – dòng đơn, nhưng phải tính lại đồ thị.
3. **Sửa Use Case theo chức vụ.** Mỗi chức vụ chỉ nối với chức năng của mình, khớp danh sách ở 1.4 và ràng buộc 6 ở 2.3.6.
4. **Rút gọn 1.4.** Bỏ mã G1–G6 và câu nhắc Chương 2 khỏi mô tả, gom giả thiết về một đoạn. Mục tiêu không dài hơn mẫu.
5. **Thêm một câu ở B3 mục 3.1**, giải thích 64 cặp theo quy ước Q2 và 3 cặp có hai dòng, để không bị hỏi vì sao thiếu Q8 ∩ Q12.
6. **Thêm cột hoặc khóa ngoại nối hồ sơ đổi hàng với đơn mới**, hoặc ghi rõ nằm ngoài phạm vi.
7. **Chọn lọc ngữ nghĩa khi trình bày.** Giữ bảng 57 đường, nhưng chuẩn bị 5–7 đường có ý nghĩa nghiệp vụ thật. Các đường như phiếu bảo hành tới người tạo mã giảm giá chỉ có giá trị về hình thức.
8. **Soát cuối:** cập nhật trường trong Word, xuất lại PDF, sửa tài liệu tham khảo số 10 cho có Điều 30, chạy SQL trên SQL Server nếu có điều kiện.

### 6.3 Cần hỏi thầy

- Lược đồ ban đầu có được cố ý giữ cột dư để minh họa chuẩn hóa không (D3)?
- 4NF giả định từ quan hệ lưu chung có được chấp nhận không, hay nên ghi "không có phụ thuộc đa trị" đúng theo đề cương?
- Mối kết hợp nối mối kết hợp có được chấp nhận trong ERD của môn không?
