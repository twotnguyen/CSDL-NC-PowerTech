**Dạng chuẩn 4 (Fourth Normal Form - 4NF)**

**Định nghĩa:**

Một quan hệ RRR được xem là ở **Dạng chuẩn 4 (4NF)** nếu:

1. Quan hệ đã đạt **BCNF (Boyce-Codd Normal Form)**.
2. Không tồn tại **phụ thuộc đa trị không tầm thường (non-trivial multivalued dependency - MVD)** dạng:

X↠Y

mà X không phải là siêu khóa (super key).

Nói cách khác, **4NF được dùng để loại bỏ tình trạng một thuộc tính độc lập xác định nhiều tập giá trị khác nhau**, gây dư thừa dữ liệu.

**Phụ thuộc đa trị là gì?**

Phụ thuộc đa trị xảy ra khi một thực thể có thể liên kết với **nhiều giá trị độc lập** của hai hay nhiều thuộc tính.

Ví dụ:

* Một giảng viên có thể dạy nhiều môn học.
* Một giảng viên có thể sử dụng nhiều ngôn ngữ lập trình.

Hai tập thông tin này độc lập với nhau.

Ký hiệu:

GiangVien↠MonHoc

GiangVien↠NgonNgu

**Ví dụ 1: Quan hệ chưa đạt 4NF**

Quan hệ:

**GIANGVIEN(MaGV, MonHoc, NgonNgu)**

Dữ liệu:

|  |  |  |
| --- | --- | --- |
| **MaGV** | **MonHoc** | **NgonNgu** |
| GV01 | CSDL | Python |
| GV01 | CSDL | Java |
| GV01 | AI | Python |
| GV01 | AI | Java |

Giả sử:

* GV01 dạy: {CSDL, AI}
* GV01 biết: {Python, Java}

Do hai thông tin độc lập nên hệ thống phải lưu tích Descartes (cross product):

2×2=4 dòng

Ta có:

MaGV↠MonHoc

MaGV↠NgonNgu

Quan hệ này **vi phạm 4NF**.

**Tách về 4NF**

Tách thành:

**GIANGVIEN\_MONHOC**

|  |  |
| --- | --- |
| **MaGV** | **MonHoc** |
| GV01 | CSDL |
| GV01 | AI |

**GIANGVIEN\_NGONNGU**

|  |  |
| --- | --- |
| **MaGV** | **NgonNgu** |
| GV01 | Python |
| GV01 | Java |

Lúc này không còn dư thừa dữ liệu.

Quan hệ đạt **4NF**.

**Ví dụ 2: Sinh viên - Sở thích - Kỹ năng**

Quan hệ:

**SINHVIEN(MSSV, SoThich, KyNang)**

Dữ liệu:

|  |  |  |
| --- | --- | --- |
| **MSSV** | **SoThich** | **KyNang** |
| SV01 | Bóng đá | Java |
| SV01 | Bóng đá | Python |
| SV01 | Âm nhạc | Java |
| SV01 | Âm nhạc | Python |

Ta có:

MSSV↠SoThichMSSV \twoheadrightarrow SoThichMSSV↠SoThich MSSV↠KyNangMSSV \twoheadrightarrow KyNangMSSV↠KyNang

Hai tập giá trị độc lập nên quan hệ vi phạm 4NF.

Tách thành:

**SV\_SOTHICH(MSSV, SoThich)**

|  |  |
| --- | --- |
| **MSSV** | **SoThich** |
| SV01 | Bóng đá |
| SV01 | Âm nhạc |

**SV\_KYNANG(MSSV, KyNang)**

|  |  |
| --- | --- |
| **MSSV** | **KyNang** |
| SV01 | Java |
| SV01 | Python |

Đạt 4NF.

**Ví dụ 3: Phim - Diễn viên - Thể loại**

Quan hệ:

**PHIM(TenPhim, DienVien, TheLoai)**

|  |  |  |
| --- | --- | --- |
| **TenPhim** | **DienVien** | **TheLoai** |
| Avengers | Robert Downey Jr. | Action |
| Avengers | Robert Downey Jr. | Sci-Fi |
| Avengers | Chris Evans | Action |
| Avengers | Chris Evans | Sci-Fi |

Ta có:

TenPhim↠DienVienTenPhim \twoheadrightarrow DienVienTenPhim↠DienVien TenPhim↠TheLoaiTenPhim \twoheadrightarrow TheLoaiTenPhim↠TheLoai

Quan hệ vi phạm 4NF vì danh sách diễn viên và thể loại là hai tập độc lập.

Tách thành:

**PHIM\_DIENVIEN(TenPhim, DienVien)**

**PHIM\_THELOAI(TenPhim, TheLoai)**

**So sánh nhanh BCNF và 4NF**

|  |  |
| --- | --- |
| **Dạng chuẩn** | **Xử lý** |
| 1NF | Loại bỏ thuộc tính lặp |
| 2NF | Loại bỏ phụ thuộc bộ phận |
| 3NF | Loại bỏ phụ thuộc bắc cầu |
| BCNF | Mọi determinant phải là siêu khóa |
| **4NF** | Loại bỏ phụ thuộc đa trị (MVD) |
| 5NF | Loại bỏ phụ thuộc nối (Join Dependency) |

**Ghi nhớ**

* **3NF/BCNF** xử lý **phụ thuộc hàm (FD)**.
* **4NF** xử lý **phụ thuộc đa trị (MVD)**.
* Khi một thực thể có **nhiều tập giá trị độc lập** (nhiều môn học, nhiều kỹ năng, nhiều sở thích...), hãy kiểm tra khả năng vi phạm **4NF**.
* Quy tắc dễ nhớ: **"Một thực thể không nên lưu đồng thời hai quan hệ 1-N độc lập trong cùng một bảng."** Đây chính là tình huống điển hình dẫn đến vi phạm 4NF.