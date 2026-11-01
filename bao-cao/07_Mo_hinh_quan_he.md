# MỤC 7. CHUYỂN ERD SANG MÔ HÌNH QUAN HỆ

Căn cứ: ERD và bản số ở [06_ERD.md](06_ERD.md), thuộc tính ở [02_Xac_dinh_thuc_the.md](02_Xac_dinh_thuc_the.md), khóa ở [05_Tim_khoa.md](05_Tim_khoa.md). Kết quả: **38 quan hệ** (30 từ thực thể, 8 từ mối kết hợp có thuộc tính) và **71 khóa ngoại**. Đây là bản chuyển **trực tiếp** từ ERD, chưa chuẩn hóa: những thuộc tính dư thừa còn nguyên và được đánh dấu ở 7.7 để xử lý ở mục 8 và 9.

## 7.1. Quy tắc chuyển và quy ước trình bày

**Quy tắc chuyển ERD sang quan hệ:**

| ERD | Quan hệ |
|---|---|
| Mỗi thực thể | Một quan hệ cùng tên, thuộc tính giữ nguyên; khóa chính là khóa đã chọn ở mục 5 |
| Mối kết hợp 1–n | Thêm **khóa ngoại** vào quan hệ phía "n" (phía có bản số tối đa 1 với đối tác), tham chiếu khóa chính phía "1" |
| Mối kết hợp 1–1 | Khóa ngoại ở một phía kèm ràng buộc **UNIQUE** |
| Mối kết hợp n–n (MKH có thuộc tính) | Quan hệ riêng gồm khóa ngoại tới hai thực thể và thuộc tính của MKH; khóa chính theo mục 5 |
| Thực thể yếu | Khóa chính có thành phần là khóa ngoại tới thực thể chủ (LANGIAO: MaGiao, SoLan) |
| Mối kết hợp đệ quy (LOAIHANG) | Khóa ngoại tới chính quan hệ, cho phép rỗng |

**Ký hiệu** (theo hướng dẫn của giảng viên):

- <u>Khóa chính</u>: gạch chân liền.
- <span style="text-decoration: underline dashed">Khóa ngoại</span>: gạch chân nét đứt.
- Thuộc tính vừa là khóa chính vừa là khóa ngoại: gạch chân liền kèm <sup>FK</sup>.
- Nếu công cụ xem không hiển thị gạch đứt, đọc cột "Khóa" ở các bảng 7.4 và bảng 7.5, ghi đầy đủ PK và FK bằng chữ.

**Chính sách xóa.** Mặc định **RESTRICT** (không cho xóa bản ghi cha đang được tham chiếu), vì các chứng từ và sự kiện là dữ liệu lịch sử, không xóa; mặt hàng, khách, nhân viên ngừng dùng thì đổi tình trạng. **CASCADE** chỉ dùng cho thành phần phụ thuộc hoàn toàn vào bản ghi cha: ảnh mặt hàng, giá trị thông số, dòng giỏ hàng, địa chỉ nhận hàng, vai trò của nhân viên.

## 7.2. Chuyển từng mối kết hợp

### 7.2.1. Mối kết hợp thường (53)

| STT | Mối kết hợp | Bản số | Loại | Kết quả chuyển |
|---|---|---|---|---|
| R1 | LOAIHANG – là loại cha của – LOAIHANG | LOAIHANG (0,n); LOAIHANG (0,1) | 1–n | Thêm MaLoaiCha vào LOAIHANG → LOAIHANG (đệ quy, cho rỗng) |
| R2 | LOAIHANG – phân loại – MATHANG | LOAIHANG (0,n); MATHANG (1,1) | 1–n | Thêm MaLoai vào MATHANG → LOAIHANG |
| R3 | THUONGHIEU – mang thương hiệu – MATHANG | THUONGHIEU (0,n); MATHANG (1,1) | 1–n | Thêm MaTH vào MATHANG → THUONGHIEU |
| R4 | MATHANG – có ảnh – ANHMATHANG | MATHANG (0,n); ANHMATHANG (1,1) | 1–n | Thêm MaSP vào ANHMATHANG → MATHANG |
| R5 | LOAIHANG – quy định thông số – DINHNGHIATHONGSO | LOAIHANG (0,n); DINHNGHIATHONGSO (1,1) | 1–n | Thêm MaLoai vào DINHNGHIATHONGSO → LOAIHANG |
| R6 | KHACHHANG – có địa chỉ nhận hàng – DIACHINHANHANG | KHACHHANG (0,n); DIACHINHANHANG (1,1) | 1–n | Thêm MaKH vào DIACHINHANHANG → KHACHHANG |
| R7 | KHACHHANG – đăng ký – TAIKHOAN | KHACHHANG (0,1); TAIKHOAN (0,1) | 1–1 | Thêm MaKH vào TAIKHOAN → KHACHHANG, UNIQUE |
| R8 | TAIKHOAN – sở hữu – GIOHANG | TAIKHOAN (0,n); GIOHANG (1,1) | 1–n | Thêm MaTK vào GIOHANG → TAIKHOAN |
| R9 | KHACHHANG – đặt mua – DONHANG | KHACHHANG (0,n); DONHANG (0,1) | 1–n | Thêm MaKH vào DONHANG → KHACHHANG |
| R10 | NHANVIEN – lập đơn – DONHANG | NHANVIEN (0,n); DONHANG (1,1) | 1–n | Thêm MaNVBan vào DONHANG → NHANVIEN |
| R11 | MAGIAMGIA – áp dụng cho – DONHANG | MAGIAMGIA (0,n); DONHANG (0,1) | 1–n | Thêm MaMG vào DONHANG → MAGIAMGIA |
| R12 | DONHANG – được điều chỉnh – DIEUCHINHDON | DONHANG (0,n); DIEUCHINHDON (1,1) | 1–n | Thêm MaDH vào DIEUCHINHDON → DONHANG |
| R13 | NHANVIEN – ghi nhận điều chỉnh – DIEUCHINHDON | NHANVIEN (0,n); DIEUCHINHDON (1,1) | 1–n | Thêm MaNV vào DIEUCHINHDON → NHANVIEN |
| R14 | CHITIETDONHANG – được giữ hàng – GIUHANG | CHITIETDONHANG (0,n); GIUHANG (1,1) | 1–n | Thêm MaDH, SoDong vào GIUHANG → CHITIETDONHANG (khóa ngoại ghép) |
| R15 | DONHANG – được thanh toán – THANHTOAN | DONHANG (0,n); THANHTOAN (1,1) | 1–n | Thêm MaDH vào THANHTOAN → DONHANG |
| R16 | NHANVIEN – xác nhận thanh toán – THANHTOAN | NHANVIEN (0,n); THANHTOAN (0,1) | 1–n | Thêm MaNVXacNhan vào THANHTOAN → NHANVIEN |
| R17 | THANHTOAN – được hoàn – KHOANHOAN | THANHTOAN (0,n); KHOANHOAN (1,1) | 1–n | Thêm MaTT vào KHOANHOAN → THANHTOAN |
| R18 | NHANVIEN – duyệt hoàn – KHOANHOAN | NHANVIEN (0,n); KHOANHOAN (1,1) | 1–n | Thêm MaNVDuyet vào KHOANHOAN → NHANVIEN |
| R19 | HOSODOITRA – phát sinh khoản hoàn – KHOANHOAN | HOSODOITRA (0,n); KHOANHOAN (0,1) | 1–n | Thêm MaHS vào KHOANHOAN → HOSODOITRA |
| R20 | TAIKHOAN – có biến động số dư – BIENDONGSODU | TAIKHOAN (0,n); BIENDONGSODU (1,1) | 1–n | Thêm MaTK vào BIENDONGSODU → TAIKHOAN |
| R21 | KHOANHOAN – ghi tăng số dư – BIENDONGSODU | KHOANHOAN (0,1); BIENDONGSODU (0,1) | 1–1 | Thêm MaHoan vào BIENDONGSODU → KHOANHOAN, UNIQUE |
| R22 | DONHANG – giao bằng – PHIEUGIAO | DONHANG (0,1); PHIEUGIAO (1,1) | 1–1 | Thêm MaDH vào PHIEUGIAO → DONHANG, UNIQUE |
| R23 | NHANVIEN – giao hàng – PHIEUGIAO | NHANVIEN (0,n); PHIEUGIAO (1,1) | 1–n | Thêm MaNVGiao vào PHIEUGIAO → NHANVIEN |
| R24 | PHIEUGIAO – gồm các lần giao – LANGIAO | PHIEUGIAO (0,3); LANGIAO (1,1) | 1–n | Thêm MaGiao vào LANGIAO → PHIEUGIAO (kèm CHECK SoLan từ 1 đến 3) |
| R25 | PHIEUGIAO – nộp tiền thu hộ – BANGIAOCOD | PHIEUGIAO (0,n); BANGIAOCOD (1,1) | 1–n | Thêm MaGiao vào BANGIAOCOD → PHIEUGIAO |
| R26 | THANHTOAN – được nộp – BANGIAOCOD | THANHTOAN (0,1); BANGIAOCOD (1,1) | 1–1 | Thêm MaTT vào BANGIAOCOD → THANHTOAN, UNIQUE |
| R27 | NHANVIEN – nộp tiền – BANGIAOCOD | NHANVIEN (0,n); BANGIAOCOD (1,1) | 1–n | Thêm MaNVGiao vào BANGIAOCOD → NHANVIEN |
| R28 | NHANVIEN – nhận tiền – BANGIAOCOD | NHANVIEN (0,n); BANGIAOCOD (1,1) | 1–n | Thêm MaNVNhan vào BANGIAOCOD → NHANVIEN |
| R29 | DONHANG – bị đề nghị đổi trả – HOSODOITRA | DONHANG (0,n); HOSODOITRA (1,1) | 1–n | Thêm MaDH vào HOSODOITRA → DONHANG |
| R30 | KHACHHANG – đề nghị – HOSODOITRA | KHACHHANG (0,n); HOSODOITRA (0,1) | 1–n | Thêm MaKH vào HOSODOITRA → KHACHHANG |
| R31 | NHANVIEN – tiếp nhận đổi trả – HOSODOITRA | NHANVIEN (0,n); HOSODOITRA (1,1) | 1–n | Thêm MaNVTiepNhan vào HOSODOITRA → NHANVIEN |
| R32 | HOSODOITRA – có lần nhận lại – LANNHANLAI | HOSODOITRA (0,n); LANNHANLAI (1,1) | 1–n | Thêm MaHS vào LANNHANLAI → HOSODOITRA |
| R33 | NHANVIEN – kiểm tra hàng nhận lại – LANNHANLAI | NHANVIEN (0,n); LANNHANLAI (0,1) | 1–n | Thêm MaNVKiemTra vào LANNHANLAI → NHANVIEN |
| R34 | NHANVIEN – duyệt chuyển nhóm – LANNHANLAI | NHANVIEN (0,n); LANNHANLAI (0,1) | 1–n | Thêm MaNVDuyet vào LANNHANLAI → NHANVIEN |
| R35 | KHACHHANG – đề nghị bảo hành – PHIEUBAOHANH | KHACHHANG (0,n); PHIEUBAOHANH (0,1) | 1–n | Thêm MaKH vào PHIEUBAOHANH → KHACHHANG |
| R36 | CHITIETDONHANG – là dòng mua gốc của – PHIEUBAOHANH | CHITIETDONHANG (0,n); PHIEUBAOHANH (1,1) | 1–n | Thêm MaDH, SoDong vào PHIEUBAOHANH → CHITIETDONHANG (khóa ngoại ghép) |
| R37 | HANGCOSERI – được bảo hành – PHIEUBAOHANH | HANGCOSERI (0,n); PHIEUBAOHANH (0,1) | 1–n | Thêm MaSeri vào PHIEUBAOHANH → HANGCOSERI |
| R38 | MATHANG – bảo hành mặt hàng – PHIEUBAOHANH | MATHANG (0,n); PHIEUBAOHANH (1,1) | 1–n | Thêm MaSP vào PHIEUBAOHANH → MATHANG (dư thừa, xem 7.7) |
| R39 | NHANVIEN – tiếp nhận bảo hành – PHIEUBAOHANH | NHANVIEN (0,n); PHIEUBAOHANH (1,1) | 1–n | Thêm MaNVTiepNhan vào PHIEUBAOHANH → NHANVIEN |
| R40 | NHACUNGCAP – giao hàng nhập – PHIEUNHAP | NHACUNGCAP (0,n); PHIEUNHAP (1,1) | 1–n | Thêm MaNCC vào PHIEUNHAP → NHACUNGCAP |
| R41 | NHANVIEN – lập phiếu nhập – PHIEUNHAP | NHANVIEN (0,n); PHIEUNHAP (1,1) | 1–n | Thêm MaNV vào PHIEUNHAP → NHANVIEN |
| R42 | MATHANG – gồm từng chiếc – HANGCOSERI | MATHANG (0,n); HANGCOSERI (1,1) | 1–n | Thêm MaSP vào HANGCOSERI → MATHANG (dư thừa, xem 7.7) |
| R43 | CHITIETPHIEUNHAP – nhập từng chiếc – HANGCOSERI | CHITIETPHIEUNHAP (0,n); HANGCOSERI (1,1) | 1–n | Thêm MaPN, SoDongNhap vào HANGCOSERI → CHITIETPHIEUNHAP (khóa ngoại ghép) |
| R44 | CHITIETDONHANG – bán từng chiếc – HANGCOSERI | CHITIETDONHANG (0,n); HANGCOSERI (0,1) | 1–n | Thêm MaDH, SoDongDon vào HANGCOSERI → CHITIETDONHANG (khóa ngoại ghép) |
| R45 | MATHANG – có biến động kho – GIAODICHKHO | MATHANG (0,n); GIAODICHKHO (1,1) | 1–n | Thêm MaSP vào GIAODICHKHO → MATHANG |
| R46 | NHANVIEN – thực hiện biến động – GIAODICHKHO | NHANVIEN (0,n); GIAODICHKHO (0,1) | 1–n | Thêm MaNV vào GIAODICHKHO → NHANVIEN |
| R47 | NHANVIEN – lập biên bản kiểm kê – DOTKIEMKE | NHANVIEN (0,n); DOTKIEMKE (1,1) | 1–n | Thêm MaNVLap vào DOTKIEMKE → NHANVIEN |
| R48 | NHANVIEN – duyệt kiểm kê – DOTKIEMKE | NHANVIEN (0,n); DOTKIEMKE (0,1) | 1–n | Thêm MaNVDuyet vào DOTKIEMKE → NHANVIEN |
| R49 | NHACUNGCAP – nhận hàng gửi – PHIEUGUIHANG | NHACUNGCAP (0,n); PHIEUGUIHANG (1,1) | 1–n | Thêm MaNCC vào PHIEUGUIHANG → NHACUNGCAP |
| R50 | NHANVIEN – gửi hàng – PHIEUGUIHANG | NHANVIEN (0,n); PHIEUGUIHANG (1,1) | 1–n | Thêm MaNVGui vào PHIEUGUIHANG → NHANVIEN |
| R51 | PHIEUBAOHANH – là nguồn bảo hành – CHITIETGUIHANG | PHIEUBAOHANH (0,n); CHITIETGUIHANG (0,1) | 1–n | Thêm MaPhieuBH vào CHITIETGUIHANG → PHIEUBAOHANH |
| R52 | HOSODOITRA – là nguồn trả hàng lỗi – CHITIETGUIHANG | HOSODOITRA (0,n); CHITIETGUIHANG (0,1) | 1–n | Thêm MaHS vào CHITIETGUIHANG → HOSODOITRA |
| R53 | HANGCOSERI – được gửi – CHITIETGUIHANG | HANGCOSERI (0,n); CHITIETGUIHANG (0,1) | 1–n | Thêm MaSeri vào CHITIETGUIHANG → HANGCOSERI |

### 7.2.2. Mối kết hợp có thuộc tính (8)

| MKH | Giữa | Loại | Quan hệ tạo ra | Khóa chính | Khóa ngoại |
|---|---|---|---|---|---|
| CHITIETDONHANG | DONHANG – MATHANG | n–n | CHITIETDONHANG | MaDH, SoDong | MaDH → DONHANG; MaSP → MATHANG |
| CHITIETPHIEUNHAP | PHIEUNHAP – MATHANG | n–n | CHITIETPHIEUNHAP | MaPN, SoDong | MaPN → PHIEUNHAP; MaSP → MATHANG |
| CHITIETGIOHANG | GIOHANG – MATHANG | n–n | CHITIETGIOHANG | MaGio, MaSP | MaGio → GIOHANG; MaSP → MATHANG |
| GIATRITHONGSO | MATHANG – DINHNGHIATHONGSO | n–n | GIATRITHONGSO | MaSP, MaTS | MaSP → MATHANG; MaTS → DINHNGHIATHONGSO |
| NHANVIEN_VAITRO | NHANVIEN – VAITRO | n–n | NHANVIEN_VAITRO | MaNV, MaVT | MaNV → NHANVIEN; MaVT → VAITRO |
| CHITIETKIEMKE | DOTKIEMKE – MATHANG | n–n | CHITIETKIEMKE | MaDot, MaSP | MaDot → DOTKIEMKE; MaSP → MATHANG |
| CHITIETTRA | HOSODOITRA – CHITIETDONHANG | n–n | CHITIETTRA | MaHS, SoDong | MaHS → HOSODOITRA; (MaDH, SoDong) → CHITIETDONHANG; (MaHS, MaDH) → HOSODOITRA; MaSeri → HANGCOSERI |
| CHITIETGUIHANG | PHIEUGUIHANG – MATHANG | n–n | CHITIETGUIHANG | MaGui, SoDong | MaPhieuBH → PHIEUBAOHANH; MaHS → HOSODOITRA; MaSeri → HANGCOSERI; MaGui → PHIEUGUIHANG; MaSP → MATHANG |

## 7.3. Lược đồ quan hệ

Mỗi dòng là một quan hệ, thuộc tính đứng đầu là khóa chính. Quan hệ được chia theo ba loại thực thể và nhóm MKH.

### 7.3.1. Quan hệ từ thực thể cơ bản

- **LOAIHANG**(<u>MaLoai</u>, TenLoai, MoTa, <span style="text-decoration: underline dashed">MaLoaiCha</span>)
- **THUONGHIEU**(<u>MaTH</u>, TenTH, MoTa)
- **MATHANG**(<u>MaSP</u>, SKU, TenSP, MoTa, GiaNiemYet, GiaKhuyenMai, ThoiHanBaoHanh, TinhTrangKinhDoanh, CoSeri, <span style="text-decoration: underline dashed">MaLoai</span>, <span style="text-decoration: underline dashed">MaTH</span>)
- **ANHMATHANG**(<u>MaAnh</u>, <span style="text-decoration: underline dashed">MaSP</span>, ViTri, DuongDan, LaAnhChinh, MoTaAnh)
- **DINHNGHIATHONGSO**(<u>MaTS</u>, <span style="text-decoration: underline dashed">MaLoai</span>, TenTS, KieuGiaTri, DonVi, BatBuoc)
- **VAITRO**(<u>MaVT</u>, TenVT)

### 7.3.2. Quan hệ từ thực thể đối tượng ngoài

- **KHACHHANG**(<u>MaKH</u>, HoTen, SDT, Email, MaSoThue)
- **DIACHINHANHANG**(<u>MaDC</u>, <span style="text-decoration: underline dashed">MaKH</span>, TenNguoiNhan, SDT, TinhThanh, PhuongXa, DiaChiCuThe, LaMacDinh)
- **NHANVIEN**(<u>MaNV</u>, HoTen, SDT, TinhTrangLamViec)
- **NHACUNGCAP**(<u>MaNCC</u>, TenNCC, NguoiLienHe, SDT, DiaChi, MaSoThue, TinhTrangHopTac)

### 7.3.3. Quan hệ từ thực thể nghiệp vụ

- **TAIKHOAN**(<u>MaTK</u>, DinhDanhDangNhap, <span style="text-decoration: underline dashed">MaKH</span>, TinhTrang, NgayDangKy, ThoiDiemNoiHoSo)
- **PHIEUNHAP**(<u>MaPN</u>, SoPhieu, <span style="text-decoration: underline dashed">MaNCC</span>, <span style="text-decoration: underline dashed">MaNV</span>, ThoiDiemNhan, TinhTrang, SoHoaDonNCC, GhiChu)
- **HANGCOSERI**(<u>MaSeri</u>, SoSeri, <span style="text-decoration: underline dashed">MaSP</span>, <span style="text-decoration: underline dashed">MaPN</span>, <span style="text-decoration: underline dashed">SoDongNhap</span>, <span style="text-decoration: underline dashed">MaDH</span>, <span style="text-decoration: underline dashed">SoDongDon</span>, TinhTrang, ThoiDiemNhap)
- **GIAODICHKHO**(<u>MaGDK</u>, <span style="text-decoration: underline dashed">MaSP</span>, NhomKho, LoaiBienDong, SoLuong, ThoiDiem, <span style="text-decoration: underline dashed">MaNV</span>, LoaiChungTu, MaChungTu, GhiChu)
- **DOTKIEMKE**(<u>MaDot</u>, LoaiKiemKe, ThoiDiem, <span style="text-decoration: underline dashed">MaNVLap</span>, <span style="text-decoration: underline dashed">MaNVDuyet</span>, ThoiDiemDuyet, TinhTrang)
- **GIOHANG**(<u>MaGio</u>, <span style="text-decoration: underline dashed">MaTK</span>, TinhTrang, ThoiDiemTao)
- **DONHANG**(<u>MaDH</u>, SoDH, ThoiDiemLap, KenhBan, LoaiDon, <span style="text-decoration: underline dashed">MaKH</span>, <span style="text-decoration: underline dashed">MaNVBan</span>, TenNguoiNhan, SDTNhan, DiaChiGiao, PhiGiao, GiamGia, <span style="text-decoration: underline dashed">MaMG</span>, TinhTrang, DieuKienCoc, GhiChu)
- **DIEUCHINHDON**(<u>MaDieuChinh</u>, <span style="text-decoration: underline dashed">MaDH</span>, ThoiDiem, <span style="text-decoration: underline dashed">MaNV</span>, NoiDungTruoc, NoiDungSau, KhachDongY)
- **MAGIAMGIA**(<u>MaMG</u>, Code, TenChuongTrinh, LoaiGiam, MucGiam, DonToiThieu, GiamToiDa, NgayBatDau, NgayKetThuc, GioiHanLuot)
- **GIUHANG**(<u>MaGiu</u>, <span style="text-decoration: underline dashed">MaDH</span>, <span style="text-decoration: underline dashed">SoDong</span>, SoLuong, ThoiDiemGiu, ThoiDiemKetThuc, LyDoKetThuc)
- **THANHTOAN**(<u>MaTT</u>, <span style="text-decoration: underline dashed">MaDH</span>, LoaiKhoan, PhuongThuc, SoTien, ThoiDiem, KetQua, MaGiaoDichNgoai, DonViThanhToan, <span style="text-decoration: underline dashed">MaNVXacNhan</span>)
- **KHOANHOAN**(<u>MaHoan</u>, <span style="text-decoration: underline dashed">MaTT</span>, <span style="text-decoration: underline dashed">MaHS</span>, SoTien, PhuongThucHoan, <span style="text-decoration: underline dashed">MaNVDuyet</span>, ThoiDiemDuyet, ThoiDiemChi)
- **PHIEUGIAO**(<u>MaGiao</u>, <span style="text-decoration: underline dashed">MaDH</span>, <span style="text-decoration: underline dashed">MaNVGiao</span>, ThoiDiemXuat, TinhTrang)
- **LANGIAO**(<u>MaGiao</u><sup>FK</sup>, <u>SoLan</u>, ThoiDiem, KetQua, LyDoThatBai)
- **BANGIAOCOD**(<u>MaBG</u>, <span style="text-decoration: underline dashed">MaGiao</span>, <span style="text-decoration: underline dashed">MaTT</span>, <span style="text-decoration: underline dashed">MaNVGiao</span>, <span style="text-decoration: underline dashed">MaNVNhan</span>, SoTien, ThoiDiem)
- **HOSODOITRA**(<u>MaHS</u>, <span style="text-decoration: underline dashed">MaDH</span>, <span style="text-decoration: underline dashed">MaKH</span>, NgayDeNghi, LoaiTruongHop, LyDo, TinhTrang, HinhThucXuLy, <span style="text-decoration: underline dashed">MaNVTiepNhan</span>)
- **LANNHANLAI**(<u>MaNhanLai</u>, <span style="text-decoration: underline dashed">MaHS</span>, ThoiDiemNhan, <span style="text-decoration: underline dashed">MaNVKiemTra</span>, KetLuan, NhomSauKiemTra, <span style="text-decoration: underline dashed">MaNVDuyet</span>, ThoiDiemDuyet)
- **PHIEUBAOHANH**(<u>MaPhieuBH</u>, <span style="text-decoration: underline dashed">MaKH</span>, <span style="text-decoration: underline dashed">MaSP</span>, <span style="text-decoration: underline dashed">MaSeri</span>, <span style="text-decoration: underline dashed">MaDH</span>, <span style="text-decoration: underline dashed">SoDong</span>, MoTaLoi, PhuKienDiKem, NgayNhan, NgayHenTra, NgayTraThucTe, TinhTrang, KetQua, LyDoTuChoi, <span style="text-decoration: underline dashed">MaNVTiepNhan</span>)
- **PHIEUGUIHANG**(<u>MaGui</u>, <span style="text-decoration: underline dashed">MaNCC</span>, LyDo, NgayGui, NgayNhanKetQua, KetQua, <span style="text-decoration: underline dashed">MaNVGui</span>)
- **BIENDONGSODU**(<u>MaBD</u>, <span style="text-decoration: underline dashed">MaTK</span>, SoTien, LoaiBienDong, <span style="text-decoration: underline dashed">MaHoan</span>, ThoiDiem)

### 7.3.4. Quan hệ từ mối kết hợp có thuộc tính

- **CHITIETDONHANG**(<u>MaDH</u><sup>FK</sup>, <u>SoDong</u>, <span style="text-decoration: underline dashed">MaSP</span>, SoLuong, DonGiaChot, TenHangChot, SKUChot)
- **CHITIETPHIEUNHAP**(<u>MaPN</u><sup>FK</sup>, <u>SoDong</u>, <span style="text-decoration: underline dashed">MaSP</span>, SoLuong, GiaNhap)
- **CHITIETGIOHANG**(<u>MaGio</u><sup>FK</sup>, <u>MaSP</u><sup>FK</sup>, SoLuong)
- **GIATRITHONGSO**(<u>MaSP</u><sup>FK</sup>, <u>MaTS</u><sup>FK</sup>, GiaTri)
- **NHANVIEN_VAITRO**(<u>MaNV</u><sup>FK</sup>, <u>MaVT</u><sup>FK</sup>)
- **CHITIETKIEMKE**(<u>MaDot</u><sup>FK</sup>, <u>MaSP</u><sup>FK</sup>, SoLuongSo, SoLuongDem, LyDoChenhLech)
- **CHITIETTRA**(<u>MaHS</u><sup>FK</sup>, <u>SoDong</u><sup>FK</sup>, <span style="text-decoration: underline dashed">MaDH</span>, SoLuongTra, <span style="text-decoration: underline dashed">MaSeri</span>)
- **CHITIETGUIHANG**(<u>MaGui</u><sup>FK</sup>, <u>SoDong</u>, <span style="text-decoration: underline dashed">MaSP</span>, <span style="text-decoration: underline dashed">MaSeri</span>, SoLuong, <span style="text-decoration: underline dashed">MaPhieuBH</span>, <span style="text-decoration: underline dashed">MaHS</span>)

**Đọc ví dụ.** `CHITIETDONHANG(MaDH, SoDong, ...)` có khóa chính ghép (MaDH, SoDong), trong đó MaDH vừa là khóa chính vừa là khóa ngoại tới DONHANG (gạch liền kèm FK); MaSP là khóa ngoại tới MATHANG (gạch đứt). `HANGCOSERI` có hai khóa ngoại ghép tới dòng nhập và dòng đơn: (MaPN, SoDongNhap) và (MaDH, SoDongDon).

## 7.4. Bảng mô tả thuộc tính

Thuộc tính liệt kê khóa chính trước. Cột "Khóa": PK là khóa chính, FK là khóa ngoại (kèm bảng được tham chiếu), UQ là khóa thay thế duy nhất; các khóa duy nhất ghép và có điều kiện ở 7.6.

### 7.4.1. Quan hệ từ thực thể cơ bản

**LOAIHANG**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaLoai | Mã loại hàng | INT | không | PK | Định danh |
| TenLoai | Tên loại | NVARCHAR(150) | không |  | Không giả định duy nhất (1.2.1) |
| MoTa | Mô tả | NVARCHAR(500) | có |  |  |
| MaLoaiCha | Loại cha | INT | có | FK → LOAIHANG(MaLoai) | Tối đa một loại cha, không tạo vòng |

**THUONGHIEU**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaTH | Mã thương hiệu | INT | không | PK | Định danh |
| TenTH | Tên thương hiệu | NVARCHAR(150) | không |  | Không giả định duy nhất |
| MoTa | Mô tả | NVARCHAR(500) | có |  |  |

**MATHANG**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaSP | Mã nội bộ | INT | không | PK | Định danh |
| SKU | Mã hàng thương mại | NVARCHAR(100) | không | UQ | Không trùng giữa các mặt hàng |
| TenSP | Tên hàng | NVARCHAR(250) | không |  |  |
| MoTa | Mô tả | NVARCHAR(MAX) | có |  |  |
| GiaNiemYet | Giá niêm yết hiện tại | DECIMAL(18,2) | không |  | ≥ 0 |
| GiaKhuyenMai | Giá khuyến mãi đang áp dụng | DECIMAL(18,2) | có |  | ≤ GiaNiemYet |
| ThoiHanBaoHanh | Thời hạn bảo hành, tính theo tháng | INT | không |  | ≥ 0 (0: không bảo hành phần cứng, ví dụ phần mềm) |
| TinhTrangKinhDoanh | Đang kinh doanh hay đã ngừng | BIT | không |  |  |
| CoSeri | Có ghi số seri từng chiếc không | BIT | không |  |  |
| MaLoai | Loại hàng | INT | không | FK → LOAIHANG(MaLoai) | Mỗi mặt hàng đúng một loại |
| MaTH | Thương hiệu | INT | không | FK → THUONGHIEU(MaTH) | Mỗi mặt hàng đúng một thương hiệu |

**ANHMATHANG**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaAnh | Mã ảnh | INT | không | PK | Định danh |
| MaSP | Mặt hàng có ảnh | INT | không | FK → MATHANG(MaSP) |  |
| ViTri | Thứ tự sắp xếp ảnh | INT | không |  | Không trùng trong cùng mặt hàng |
| DuongDan | Đường dẫn ảnh | NVARCHAR(1000) | không |  |  |
| LaAnhChinh | Ảnh đại diện chính | BIT | không |  | Mặt hàng đang bán có một ảnh chính |
| MoTaAnh | Chú thích ảnh | NVARCHAR(250) | có |  |  |

**DINHNGHIATHONGSO**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaTS | Mã thông số | INT | không | PK | Định danh |
| MaLoai | Loại hàng áp dụng | INT | không | FK → LOAIHANG(MaLoai) |  |
| TenTS | Tên thông số | NVARCHAR(150) | không |  | Phân biệt trong cùng loại hàng |
| KieuGiaTri | Kiểu giá trị | NVARCHAR(20) | không |  | Chữ, số hoặc có/không |
| DonVi | Đơn vị | NVARCHAR(50) | có |  |  |
| BatBuoc | Mặt hàng bán ra phải có thông số này | BIT | không |  |  |

**VAITRO**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaVT | Mã vai trò | INT | không | PK | Định danh |
| TenVT | Tên công việc | NVARCHAR(100) | không |  | Tư vấn bán hàng, thu ngân kiêm thủ quỹ, kỹ thuật, kho, giao hàng, chăm sóc khách hàng, quản lý |

### 7.4.2. Quan hệ từ thực thể đối tượng ngoài

**KHACHHANG**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaKH | Mã khách hàng | INT | không | PK | Định danh |
| HoTen | Họ tên | NVARCHAR(150) | không |  | Không đủ để phân biệt hai khách |
| SDT | Số điện thoại | NVARCHAR(20) | không |  | Không đủ để phân biệt; khách không để lại số thì không có hồ sơ |
| Email | Thư điện tử | NVARCHAR(256) | có |  |  |
| MaSoThue | Mã số thuế của khách doanh nghiệp | NVARCHAR(50) | có |  | Chỉ có khi khách cần hóa đơn giá trị gia tăng |

**DIACHINHANHANG**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaDC | Mã địa chỉ | INT | không | PK | Định danh |
| MaKH | Khách sở hữu | INT | không | FK → KHACHHANG(MaKH) |  |
| TenNguoiNhan | Người nhận | NVARCHAR(150) | không |  |  |
| SDT | Số điện thoại người nhận | NVARCHAR(20) | không |  |  |
| TinhThanh | Tỉnh hoặc thành phố | NVARCHAR(100) | không |  |  |
| PhuongXa | Phường hoặc xã | NVARCHAR(100) | không |  |  |
| DiaChiCuThe | Số nhà, đường | NVARCHAR(255) | không |  |  |
| LaMacDinh | Địa chỉ mặc định | BIT | không |  | Tối đa một địa chỉ mặc định cho mỗi khách |

**NHANVIEN**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaNV | Mã nhân viên | INT | không | PK | Định danh |
| HoTen | Họ tên | NVARCHAR(150) | không |  |  |
| SDT | Số điện thoại | NVARCHAR(20) | không |  |  |
| TinhTrangLamViec | Còn làm hay đã nghỉ | BIT | không |  |  |

**NHACUNGCAP**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaNCC | Mã nhà cung cấp | INT | không | PK | Định danh |
| TenNCC | Tên công ty | NVARCHAR(150) | không |  | Không giả định duy nhất |
| NguoiLienHe | Người liên hệ | NVARCHAR(150) | có |  |  |
| SDT | Số điện thoại | NVARCHAR(20) | có |  |  |
| DiaChi | Địa chỉ | NVARCHAR(500) | có |  |  |
| MaSoThue | Mã số thuế | NVARCHAR(50) | có |  | Chưa coi là khóa khi chưa có quy tắc bắt buộc và duy nhất |
| TinhTrangHopTac | Còn hợp tác không | BIT | không |  |  |

### 7.4.3. Quan hệ từ thực thể nghiệp vụ

**TAIKHOAN**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaTK | Mã tài khoản | INT | không | PK | Định danh |
| DinhDanhDangNhap | Số điện thoại hoặc email dùng đăng ký | NVARCHAR(256) | không | UQ | Không trùng |
| MaKH | Khách gắn với tài khoản | INT | có | FK → KHACHHANG(MaKH); UQ | Mỗi tài khoản gắn tối đa một khách |
| TinhTrang | Hoạt động hoặc bị khóa | NVARCHAR(20) | không |  |  |
| NgayDangKy | Thời điểm đăng ký | DATETIME2 | không |  |  |
| ThoiDiemNoiHoSo | Thời điểm hồ sơ quầy được nối vào tài khoản | DATETIME2 | có |  | Chỉ sau khi khách xác nhận bằng mã gửi về số điện thoại |

**PHIEUNHAP**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaPN | Mã phiếu | INT | không | PK | Định danh |
| SoPhieu | Số phiếu | NVARCHAR(50) | không | UQ | Không trùng |
| MaNCC | Nhà cung cấp | INT | không | FK → NHACUNGCAP(MaNCC) |  |
| MaNV | Người lập | INT | không | FK → NHANVIEN(MaNV) |  |
| ThoiDiemNhan | Thời điểm nhận hàng | DATETIME2 | không |  |  |
| TinhTrang | Chờ xác nhận hoặc đã xác nhận | NVARCHAR(30) | không |  | Phải có ít nhất một dòng khi xác nhận; chỉ ghi tăng kho một lần |
| SoHoaDonNCC | Số hóa đơn của nhà cung cấp | NVARCHAR(50) | có |  |  |
| GhiChu | Ghi chú | NVARCHAR(1000) | có |  |  |

**HANGCOSERI**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaSeri | Mã nội bộ của chiếc hàng | INT | không | PK | Định danh |
| SoSeri | Số seri của hãng | NVARCHAR(100) | không |  | Giả thiết: không trùng trong cùng mặt hàng (chưa kiểm chứng) |
| MaSP | Mặt hàng | INT | không | FK → MATHANG(MaSP) | Mặt hàng có CoSeri = đúng |
| MaPN | Phiếu nhập mà chiếc này đến từ | INT | không | FK (MaPN, SoDongNhap) → CHITIETPHIEUNHAP(MaPN, SoDong) |  |
| SoDongNhap | Dòng của phiếu nhập | INT | không | FK (MaPN, SoDongNhap) → CHITIETPHIEUNHAP(MaPN, SoDong) |  |
| MaDH | Dòng đơn đã bán chiếc này | INT | có | FK (MaDH, SoDongDon) → CHITIETDONHANG(MaDH, SoDong) | Rỗng nếu chưa bán |
| SoDongDon | Dòng đơn đã bán chiếc này | INT | có | FK (MaDH, SoDongDon) → CHITIETDONHANG(MaDH, SoDong) | Rỗng nếu chưa bán |
| TinhTrang | Trong kho, đã bán, đang bảo hành, đã gửi hãng, đã trả nhà cung cấp | NVARCHAR(30) | không |  |  |
| ThoiDiemNhap | Thời điểm nhập | DATETIME2 | không |  |  |

**GIAODICHKHO**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaGDK | Mã giao dịch | INT | không | PK | Định danh |
| MaSP | Mặt hàng | INT | không | FK → MATHANG(MaSP) |  |
| NhomKho | Nhóm tình trạng của hàng | NVARCHAR(30) | không |  | Đủ điều kiện bán, chờ kiểm tra, không bán được chờ xử lý |
| LoaiBienDong | Loại | NVARCHAR(20) | không |  | Kiểm kê đầu kỳ, nhập, bán, giao, trả, chuyển nhóm, điều chỉnh |
| SoLuong | Số lượng thay đổi | INT | không |  | > 0; chiều tăng hoặc giảm do loại biến động quyết định (DDL cũng lưu số dương); chuyển nhóm tạo hai dòng đối ứng |
| ThoiDiem | Thời điểm | DATETIME2 | không |  |  |
| MaNV | Người thực hiện | INT | có | FK → NHANVIEN(MaNV) |  |
| LoaiChungTu | Chứng từ gốc (phiếu nhập, đơn, hồ sơ đổi trả...) | NVARCHAR(50) | có |  | Liên kết đa hình, không có khóa ngoại trong DDL hiện tại |
| MaChungTu | Chứng từ gốc (phiếu nhập, đơn, hồ sơ đổi trả...) | INT | có |  | Liên kết đa hình, không có khóa ngoại trong DDL hiện tại |
| GhiChu | Ghi chú | NVARCHAR(500) | có |  |  |

**DOTKIEMKE**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaDot | Mã đợt | INT | không | PK | Định danh |
| LoaiKiemKe | Đầu kỳ, định kỳ hoặc đột xuất | NVARCHAR(20) | không |  |  |
| ThoiDiem | Thời điểm kiểm kê | DATETIME2 | không |  |  |
| MaNVLap | Người lập biên bản | INT | không | FK → NHANVIEN(MaNV) |  |
| MaNVDuyet | Người quản lý duyệt | INT | có | FK → NHANVIEN(MaNV) | Số lượng chỉ được điều chỉnh sau khi duyệt |
| ThoiDiemDuyet | Thời điểm duyệt | DATETIME2 | có |  |  |
| TinhTrang | Chờ duyệt, đã duyệt, từ chối | NVARCHAR(20) | không |  |  |

**GIOHANG**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaGio | Mã giỏ | INT | không | PK | Định danh |
| MaTK | Tài khoản | INT | không | FK → TAIKHOAN(MaTK) | Mỗi tài khoản tối đa một giỏ đang dùng |
| TinhTrang | Đang dùng hoặc đã gửi đơn | NVARCHAR(20) | không |  |  |
| ThoiDiemTao | Thời điểm tạo | DATETIME2 | không |  |  |

**DONHANG**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaDH | Mã đơn | INT | không | PK | Định danh |
| SoDH | Số đơn | NVARCHAR(50) | không | UQ | Không trùng |
| ThoiDiemLap | Thời điểm lập | DATETIME2 | không |  |  |
| KenhBan | Kênh bán | NVARCHAR(20) | không |  | Quầy, trang web, điện thoại hoặc tin nhắn |
| LoaiDon | Loại đơn | NVARCHAR(20) | không |  | Có sẵn, đặt trước, lắp theo yêu cầu |
| MaKH | Khách | INT | có | FK → KHACHHANG(MaKH) | Rỗng nếu khách quầy không để lại thông tin |
| MaNVBan | Nhân viên bán hoặc lập đơn | INT | không | FK → NHANVIEN(MaNV) |  |
| TenNguoiNhan | Người nhận | NVARCHAR(150) | không |  | Chốt khi xác nhận đơn |
| SDTNhan | Số điện thoại nhận | NVARCHAR(20) | không |  | Chốt khi xác nhận đơn |
| DiaChiGiao | Địa chỉ giao | NVARCHAR(500) | có |  | Rỗng nếu giao trực tiếp tại quầy; chốt khi xác nhận đơn |
| PhiGiao | Phí giao hàng | DECIMAL(18,2) | không |  | ≥ 0 |
| GiamGia | Số tiền giảm đã chốt | DECIMAL(18,2) | không |  | ≥ 0; chỉ giảm tiền hàng |
| MaMG | Mã giảm giá đã dùng | INT | có | FK → MAGIAMGIA(MaMG) | Tối đa một mã mỗi đơn |
| TinhTrang | Tình trạng đơn | NVARCHAR(30) | không |  | Chờ xác nhận, đã xác nhận, đang chuẩn bị, đang giao, hoàn tất, đã hủy |
| DieuKienCoc | Điều kiện đặt cọc ghi trên phiếu đặt hàng | NVARCHAR(500) | có |  | Chỉ có với đơn đặt trước hoặc lắp theo yêu cầu |
| GhiChu | Ghi chú | NVARCHAR(1000) | có |  |  |

**DIEUCHINHDON**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaDieuChinh | Mã lần sửa | INT | không | PK | Định danh |
| MaDH | Đơn bị sửa | INT | không | FK → DONHANG(MaDH) | Chỉ sửa trước khi giao |
| ThoiDiem | Thời điểm | DATETIME2 | không |  |  |
| MaNV | Người ghi nhận | INT | không | FK → NHANVIEN(MaNV) |  |
| NoiDungTruoc | Nội dung trước khi sửa | NVARCHAR(MAX) | không |  |  |
| NoiDungSau | Nội dung sau khi sửa | NVARCHAR(MAX) | không |  |  |
| KhachDongY | Khách đã đồng ý | BIT | không |  | Phải đúng |

**MAGIAMGIA**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaMG | Mã nội bộ | INT | không | PK | Định danh |
| Code | Mã khách nhập | NVARCHAR(50) | không | UQ | Không trùng |
| TenChuongTrinh | Tên chương trình | NVARCHAR(150) | không |  |  |
| LoaiGiam | Theo phần trăm hoặc theo số tiền | INT | không |  |  |
| MucGiam | Mức giảm | DECIMAL(18,2) | không |  | > 0 |
| DonToiThieu | Giá trị đơn tối thiểu | DECIMAL(18,2) | có |  |  |
| GiamToiDa | Mức giảm tối đa | DECIMAL(18,2) | có |  |  |
| NgayBatDau | Bắt đầu áp dụng | DATETIME2 | có |  |  |
| NgayKetThuc | Hết hạn | DATETIME2 | có |  | ≥ NgayBatDau |
| GioiHanLuot | Số lượt dùng tối đa | INT | có |  | Số lượt đã dùng là dữ liệu tính từ các đơn |

**GIUHANG**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaGiu | Mã lần giữ | INT | không | PK | Định danh |
| MaDH | Dòng đơn được giữ hàng | INT | không | FK (MaDH, SoDong) → CHITIETDONHANG(MaDH, SoDong) |  |
| SoDong | Dòng đơn được giữ hàng | INT | không | FK (MaDH, SoDong) → CHITIETDONHANG(MaDH, SoDong) |  |
| SoLuong | Số lượng giữ | INT | không |  | > 0 |
| ThoiDiemGiu | Thời điểm giữ | DATETIME2 | không |  | Sau khi nhân viên xác nhận đơn |
| ThoiDiemKetThuc | Thời điểm kết thúc giữ | DATETIME2 | có |  |  |
| LyDoKetThuc | Lý do | NVARCHAR(30) | có |  | Xuất hàng, hủy đơn, giao thất bại, hết hạn trả trước |

**THANHTOAN**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaTT | Mã lần thanh toán | INT | không | PK | Định danh |
| MaDH | Đơn | INT | không | FK → DONHANG(MaDH) | Một đơn có nhiều lần thanh toán |
| LoaiKhoan | Cọc, thanh toán, thu khi giao | NVARCHAR(20) | không |  |  |
| PhuongThuc | Phương thức | NVARCHAR(30) | không |  | Tiền mặt, chuyển khoản hoặc QR, thẻ, ví điện tử hoặc cổng thanh toán, COD (COD không áp dụng tại quầy) |
| SoTien | Số tiền | DECIMAL(18,2) | không |  | > 0 |
| ThoiDiem | Thời điểm | DATETIME2 | không |  |  |
| KetQua | Thành công, thất bại, chờ xác nhận | NVARCHAR(20) | không |  | Lần thất bại không được tính là đã thu |
| MaGiaoDichNgoai | Mã giao dịch bên ngoài | NVARCHAR(100) | có |  | Phân biệt trong phạm vi đơn vị thanh toán |
| DonViThanhToan | Ngân hàng, ví hoặc cổng thanh toán | NVARCHAR(100) | có |  |  |
| MaNVXacNhan | Người xác nhận | INT | có | FK → NHANVIEN(MaNV) |  |

**KHOANHOAN**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaHoan | Mã khoản hoàn | INT | không | PK | Định danh |
| MaTT | Khoản thu gốc | INT | không | FK → THANHTOAN(MaTT) | Tổng các khoản hoàn không vượt số tiền đã thu |
| MaHS | Hồ sơ đổi trả hoặc hủy phát sinh khoản hoàn | INT | có | FK → HOSODOITRA(MaHS) |  |
| SoTien | Số tiền hoàn | DECIMAL(18,2) | không |  | > 0 |
| PhuongThucHoan | Theo phương thức đã trả, chuyển khoản, tiền mặt, số dư tài khoản | NVARCHAR(30) | không |  |  |
| MaNVDuyet | Người quản lý duyệt | INT | không | FK → NHANVIEN(MaNV) |  |
| ThoiDiemDuyet | Thời điểm duyệt | DATETIME2 | không |  |  |
| ThoiDiemChi | Thời điểm chi | DATETIME2 | có |  |  |

**PHIEUGIAO**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaGiao | Mã phiếu giao | INT | không | PK | Định danh |
| MaDH | Đơn giao | INT | không | FK → DONHANG(MaDH); UQ | Mỗi đơn giao trọn trong một đợt |
| MaNVGiao | Người giao | INT | không | FK → NHANVIEN(MaNV) |  |
| ThoiDiemXuat | Thời điểm xuất hàng | DATETIME2 | không |  | Việc giữ hàng kết thúc, số lượng trừ khỏi kho |
| TinhTrang | Đang giao, hoàn tất, thất bại | NVARCHAR(20) | không |  |  |

**LANGIAO**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaGiao | Phiếu giao | INT | không | PK; FK → PHIEUGIAO(MaGiao) |  |
| SoLan | Lần giao thứ mấy | INT | không | PK | 1 đến 3 |
| ThoiDiem | Thời điểm | DATETIME2 | không |  |  |
| KetQua | Thành công hoặc thất bại | NVARCHAR(20) | không |  |  |
| LyDoThatBai | Lý do | NVARCHAR(250) | có |  | Có khi thất bại |

**BANGIAOCOD**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaBG | Mã bàn giao | INT | không | PK | Định danh |
| MaGiao | Phiếu giao | INT | không | FK → PHIEUGIAO(MaGiao) |  |
| MaTT | Khoản thu COD | INT | không | FK → THANHTOAN(MaTT); UQ |  |
| MaNVGiao | Người nộp | INT | không | FK → NHANVIEN(MaNV) |  |
| MaNVNhan | Thủ quỹ nhận | INT | không | FK → NHANVIEN(MaNV) |  |
| SoTien | Số tiền nộp | DECIMAL(18,2) | không |  | > 0 |
| ThoiDiem | Thời điểm nộp | DATETIME2 | không |  |  |

**HOSODOITRA**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaHS | Mã hồ sơ | INT | không | PK | Định danh |
| MaDH | Đơn gốc | INT | không | FK → DONHANG(MaDH) | Một đơn có thể được trả nhiều lần |
| MaKH | Người đề nghị | INT | có | FK → KHACHHANG(MaKH) | Rỗng nếu khách quầy không có hồ sơ; khi đó xử lý bằng chứng từ mua |
| NgayDeNghi | Ngày đề nghị | DATETIME2 | không |  |  |
| LoaiTruongHop | Giao sai thiếu hư ngoài, lỗi nhà sản xuất, khách đổi ý | NVARCHAR(30) | không |  | Quyết định thời hạn (48 giờ, 30 hoặc 7 ngày, 7 ngày) |
| LyDo | Lý do | NVARCHAR(500) | không |  |  |
| TinhTrang | Chờ kiểm tra, chấp nhận, từ chối, hoàn tất | NVARCHAR(20) | không |  |  |
| HinhThucXuLy | Đổi cùng loại, đổi sản phẩm khác, hoàn tiền | NVARCHAR(20) | có |  |  |
| MaNVTiepNhan | Người tiếp nhận | INT | không | FK → NHANVIEN(MaNV) |  |

**LANNHANLAI**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaNhanLai | Mã lần nhận | INT | không | PK | Định danh |
| MaHS | Hồ sơ | INT | không | FK → HOSODOITRA(MaHS) | Tổng số lượng nhận lại không vượt số đã giao |
| ThoiDiemNhan | Thời điểm nhận hàng | DATETIME2 | không |  | Hàng luôn vào nhóm chờ kiểm tra |
| MaNVKiemTra | Kỹ thuật viên | INT | có | FK → NHANVIEN(MaNV) |  |
| KetLuan | Nguyên niêm phong không lỗi, đã mở hộp không lỗi, lỗi thật | NVARCHAR(30) | có |  |  |
| NhomSauKiemTra | Nhóm kho sau kiểm tra | NVARCHAR(30) | có |  | Chuyển nhóm tạo giao dịch kho đối ứng |
| MaNVDuyet | Người quản lý duyệt | INT | có | FK → NHANVIEN(MaNV) |  |
| ThoiDiemDuyet | Thời điểm duyệt | DATETIME2 | có |  |  |

**PHIEUBAOHANH**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaPhieuBH | Mã phiếu | INT | không | PK | Định danh |
| MaKH | Khách | INT | có | FK → KHACHHANG(MaKH) | Rỗng nếu đối chiếu bằng chứng từ mua |
| MaSP | Mặt hàng bảo hành | INT | không | FK → MATHANG(MaSP) |  |
| MaSeri | Chiếc hàng có seri | INT | có | FK → HANGCOSERI(MaSeri) | Rỗng với hàng không có seri |
| MaDH | Dòng mua gốc | INT | không | FK (MaDH, SoDong) → CHITIETDONHANG(MaDH, SoDong) | Căn cứ thời hạn bảo hành đã chốt |
| SoDong | Dòng mua gốc | INT | không | FK (MaDH, SoDong) → CHITIETDONHANG(MaDH, SoDong) | Căn cứ thời hạn bảo hành đã chốt |
| MoTaLoi | Mô tả lỗi | NVARCHAR(500) | không |  |  |
| PhuKienDiKem | Phụ kiện đi kèm | NVARCHAR(250) | có |  |  |
| NgayNhan | Ngày tiếp nhận | DATETIME2 | không |  |  |
| NgayHenTra | Ngày hẹn trả ghi trên phiếu | DATE | không |  | Thường 7 đến 30 ngày tùy hãng |
| NgayTraThucTe | Ngày trả khách | DATETIME2 | có |  |  |
| TinhTrang | Đã tiếp nhận, đang xử lý, đã gửi hãng, đã xong, từ chối | NVARCHAR(20) | không |  |  |
| KetQua | Sửa xong, đổi mới, hoàn tiền, không thấy lỗi, từ chối | NVARCHAR(20) | có |  |  |
| LyDoTuChoi | Lý do từ chối | NVARCHAR(250) | có |  | Có khi từ chối |
| MaNVTiepNhan | Người tiếp nhận | INT | không | FK → NHANVIEN(MaNV) |  |

**PHIEUGUIHANG**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaGui | Mã phiếu gửi | INT | không | PK | Định danh |
| MaNCC | Nhà cung cấp hoặc hãng nhận | INT | không | FK → NHACUNGCAP(MaNCC) |  |
| LyDo | Bảo hành hoặc trả hàng lỗi | NVARCHAR(20) | không |  |  |
| NgayGui | Ngày gửi | DATETIME2 | không |  |  |
| NgayNhanKetQua | Ngày nhận kết quả | DATETIME2 | có |  |  |
| KetQua | Đổi hàng mới, đã sửa, ghi giảm tiền | NVARCHAR(20) | có |  | Hàng đổi về nhập theo phiếu nhập |
| MaNVGui | Người gửi | INT | không | FK → NHANVIEN(MaNV) |  |

**BIENDONGSODU**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaBD | Mã biến động | INT | không | PK | Định danh |
| MaTK | Tài khoản | INT | không | FK → TAIKHOAN(MaTK) |  |
| SoTien | Số tiền tăng (dương) hoặc giảm (âm) | DECIMAL(18,2) | không |  | Số dư tính ra không âm |
| LoaiBienDong | Hoàn tiền hoặc dùng để thanh toán | NVARCHAR(20) | không |  |  |
| MaHoan | Nguồn tăng | INT | có | FK → KHOANHOAN(MaHoan); UQ | Một nguồn không tạo biến động hai lần |
| ThoiDiem | Thời điểm | DATETIME2 | không |  |  |

### 7.4.4. Quan hệ từ mối kết hợp có thuộc tính

**CHITIETDONHANG**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaDH | Đơn chứa dòng | INT | không | PK; FK → DONHANG(MaDH) |  |
| SoDong | Số thứ tự dòng trong đơn | INT | không | PK | Không trùng trong đơn |
| MaSP | Mặt hàng của dòng | INT | không | FK → MATHANG(MaSP) |  |
| SoLuong | Số lượng | INT | không |  | > 0 |
| DonGiaChot | Đơn giá đã chốt khi xác nhận đơn | DECIMAL(18,2) | không |  | ≥ 0; không suy ra từ giá hiện tại |
| TenHangChot | Tên hàng đã chốt | NVARCHAR(250) | không |  |  |
| SKUChot | SKU đã chốt | NVARCHAR(100) | có |  |  |

**CHITIETPHIEUNHAP**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaPN | Phiếu nhập chứa dòng | INT | không | PK; FK → PHIEUNHAP(MaPN) |  |
| SoDong | Số thứ tự dòng trong phiếu | INT | không | PK | Không trùng trong phiếu |
| MaSP | Mặt hàng nhập | INT | không | FK → MATHANG(MaSP) |  |
| SoLuong | Số lượng thực nhận | INT | không |  | > 0 |
| GiaNhap | Giá nhập của dòng | DECIMAL(18,2) | không |  | ≥ 0 |

**CHITIETGIOHANG**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaGio | Giỏ chứa dòng | INT | không | PK; FK → GIOHANG(MaGio) |  |
| MaSP | Mặt hàng trong giỏ | INT | không | PK; FK → MATHANG(MaSP) |  |
| SoLuong | Số lượng | INT | không |  | > 0; mỗi mặt hàng một dòng trong giỏ |

**GIATRITHONGSO**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaSP | Mặt hàng | INT | không | PK; FK → MATHANG(MaSP) |  |
| MaTS | Thông số | INT | không | PK; FK → DINHNGHIATHONGSO(MaTS) | Phải thuộc loại hàng của mặt hàng |
| GiaTri | Giá trị thông số | NVARCHAR(500) | không |  | Đúng kiểu KieuGiaTri; DDL tách thành ba cột chữ, số, có/không |

**NHANVIEN_VAITRO**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaNV | Nhân viên | INT | không | PK; FK → NHANVIEN(MaNV) |  |
| MaVT | Vai trò (công việc) | INT | không | PK; FK → VAITRO(MaVT) |  |

**CHITIETKIEMKE**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaDot | Đợt kiểm kê | INT | không | PK; FK → DOTKIEMKE(MaDot) |  |
| MaSP | Mặt hàng được đếm | INT | không | PK; FK → MATHANG(MaSP) |  |
| SoLuongSo | Số lượng theo sổ | INT | không |  | ≥ 0 |
| SoLuongDem | Số lượng đếm thực tế | INT | không |  | ≥ 0 |
| LyDoChenhLech | Lý do chênh lệch | NVARCHAR(250) | có |  | Chênh lệch là dữ liệu tính |

**CHITIETTRA**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaHS | Hồ sơ đổi trả | INT | không | PK; FK → HOSODOITRA(MaHS); FK (MaHS, MaDH) → HOSODOITRA(MaHS, MaDH) |  |
| SoDong | Số dòng của dòng đơn được trả | INT | không | PK; FK (MaDH, SoDong) → CHITIETDONHANG(MaDH, SoDong) | Mỗi dòng đơn xuất hiện tối đa một lần trong một hồ sơ |
| MaDH | Đơn gốc của dòng | INT | không | FK (MaDH, SoDong) → CHITIETDONHANG(MaDH, SoDong); FK (MaHS, MaDH) → HOSODOITRA(MaHS, MaDH) | Phải trùng đơn của hồ sơ (MaHS → MaDH) |
| SoLuongTra | Số lượng trả | INT | không |  | > 0; tổng không vượt số đã giao |
| MaSeri | Chiếc hàng có seri được trả | INT | có | FK → HANGCOSERI(MaSeri) |  |

**CHITIETGUIHANG**

| Thuộc tính | Ý nghĩa | Kiểu | NULL | Khóa | Ràng buộc |
|---|---|---|---|---|---|
| MaGui | Phiếu gửi chứa dòng | INT | không | PK; FK → PHIEUGUIHANG(MaGui) |  |
| SoDong | Số thứ tự dòng trong phiếu | INT | không | PK |  |
| MaSP | Mặt hàng gửi | INT | không | FK → MATHANG(MaSP) |  |
| MaSeri | Chiếc hàng có seri gửi đi | INT | có | FK → HANGCOSERI(MaSeri) |  |
| SoLuong | Số lượng | INT | không |  | > 0 |
| MaPhieuBH | Phiếu bảo hành là nguồn | INT | có | FK → PHIEUBAOHANH(MaPhieuBH) | Đúng một trong MaPhieuBH, MaHS khác rỗng |
| MaHS | Hồ sơ đổi trả là nguồn | INT | có | FK → HOSODOITRA(MaHS) | Đúng một trong MaPhieuBH, MaHS khác rỗng |

## 7.5. Tổng hợp khóa ngoại

| Quan hệ | Cột khóa ngoại | Tham chiếu | NULL | Khi xóa bản ghi cha |
|---|---|---|---|---|
| LOAIHANG | MaLoaiCha | LOAIHANG(MaLoai) | có | RESTRICT |
| MATHANG | MaLoai | LOAIHANG(MaLoai) | không | RESTRICT |
| MATHANG | MaTH | THUONGHIEU(MaTH) | không | RESTRICT |
| ANHMATHANG | MaSP | MATHANG(MaSP) | không | CASCADE |
| DINHNGHIATHONGSO | MaLoai | LOAIHANG(MaLoai) | không | RESTRICT |
| DIACHINHANHANG | MaKH | KHACHHANG(MaKH) | không | CASCADE |
| TAIKHOAN | MaKH | KHACHHANG(MaKH) | có | RESTRICT |
| GIOHANG | MaTK | TAIKHOAN(MaTK) | không | RESTRICT |
| DONHANG | MaKH | KHACHHANG(MaKH) | có | RESTRICT |
| DONHANG | MaNVBan | NHANVIEN(MaNV) | không | RESTRICT |
| DONHANG | MaMG | MAGIAMGIA(MaMG) | có | RESTRICT |
| DIEUCHINHDON | MaDH | DONHANG(MaDH) | không | RESTRICT |
| DIEUCHINHDON | MaNV | NHANVIEN(MaNV) | không | RESTRICT |
| GIUHANG | MaDH, SoDong | CHITIETDONHANG(MaDH, SoDong) | không | RESTRICT |
| THANHTOAN | MaDH | DONHANG(MaDH) | không | RESTRICT |
| THANHTOAN | MaNVXacNhan | NHANVIEN(MaNV) | có | RESTRICT |
| KHOANHOAN | MaTT | THANHTOAN(MaTT) | không | RESTRICT |
| KHOANHOAN | MaNVDuyet | NHANVIEN(MaNV) | không | RESTRICT |
| KHOANHOAN | MaHS | HOSODOITRA(MaHS) | có | RESTRICT |
| BIENDONGSODU | MaTK | TAIKHOAN(MaTK) | không | RESTRICT |
| BIENDONGSODU | MaHoan | KHOANHOAN(MaHoan) | có | RESTRICT |
| PHIEUGIAO | MaDH | DONHANG(MaDH) | không | RESTRICT |
| PHIEUGIAO | MaNVGiao | NHANVIEN(MaNV) | không | RESTRICT |
| LANGIAO | MaGiao | PHIEUGIAO(MaGiao) | không | RESTRICT |
| BANGIAOCOD | MaGiao | PHIEUGIAO(MaGiao) | không | RESTRICT |
| BANGIAOCOD | MaTT | THANHTOAN(MaTT) | không | RESTRICT |
| BANGIAOCOD | MaNVGiao | NHANVIEN(MaNV) | không | RESTRICT |
| BANGIAOCOD | MaNVNhan | NHANVIEN(MaNV) | không | RESTRICT |
| HOSODOITRA | MaDH | DONHANG(MaDH) | không | RESTRICT |
| HOSODOITRA | MaKH | KHACHHANG(MaKH) | có | RESTRICT |
| HOSODOITRA | MaNVTiepNhan | NHANVIEN(MaNV) | không | RESTRICT |
| LANNHANLAI | MaHS | HOSODOITRA(MaHS) | không | RESTRICT |
| LANNHANLAI | MaNVKiemTra | NHANVIEN(MaNV) | có | RESTRICT |
| LANNHANLAI | MaNVDuyet | NHANVIEN(MaNV) | có | RESTRICT |
| PHIEUBAOHANH | MaKH | KHACHHANG(MaKH) | có | RESTRICT |
| PHIEUBAOHANH | MaDH, SoDong | CHITIETDONHANG(MaDH, SoDong) | không | RESTRICT |
| PHIEUBAOHANH | MaSeri | HANGCOSERI(MaSeri) | có | RESTRICT |
| PHIEUBAOHANH | MaSP | MATHANG(MaSP) | không | RESTRICT |
| PHIEUBAOHANH | MaNVTiepNhan | NHANVIEN(MaNV) | không | RESTRICT |
| PHIEUNHAP | MaNCC | NHACUNGCAP(MaNCC) | không | RESTRICT |
| PHIEUNHAP | MaNV | NHANVIEN(MaNV) | không | RESTRICT |
| HANGCOSERI | MaSP | MATHANG(MaSP) | không | RESTRICT |
| HANGCOSERI | MaPN, SoDongNhap | CHITIETPHIEUNHAP(MaPN, SoDong) | không | RESTRICT |
| HANGCOSERI | MaDH, SoDongDon | CHITIETDONHANG(MaDH, SoDong) | có | RESTRICT |
| GIAODICHKHO | MaSP | MATHANG(MaSP) | không | RESTRICT |
| GIAODICHKHO | MaNV | NHANVIEN(MaNV) | có | RESTRICT |
| DOTKIEMKE | MaNVLap | NHANVIEN(MaNV) | không | RESTRICT |
| DOTKIEMKE | MaNVDuyet | NHANVIEN(MaNV) | có | RESTRICT |
| PHIEUGUIHANG | MaNCC | NHACUNGCAP(MaNCC) | không | RESTRICT |
| PHIEUGUIHANG | MaNVGui | NHANVIEN(MaNV) | không | RESTRICT |
| CHITIETGUIHANG | MaPhieuBH | PHIEUBAOHANH(MaPhieuBH) | có | RESTRICT |
| CHITIETGUIHANG | MaHS | HOSODOITRA(MaHS) | có | RESTRICT |
| CHITIETGUIHANG | MaSeri | HANGCOSERI(MaSeri) | có | RESTRICT |
| CHITIETDONHANG | MaDH | DONHANG(MaDH) | không | RESTRICT |
| CHITIETDONHANG | MaSP | MATHANG(MaSP) | không | RESTRICT |
| CHITIETPHIEUNHAP | MaPN | PHIEUNHAP(MaPN) | không | RESTRICT |
| CHITIETPHIEUNHAP | MaSP | MATHANG(MaSP) | không | RESTRICT |
| CHITIETGIOHANG | MaGio | GIOHANG(MaGio) | không | CASCADE |
| CHITIETGIOHANG | MaSP | MATHANG(MaSP) | không | RESTRICT |
| GIATRITHONGSO | MaSP | MATHANG(MaSP) | không | CASCADE |
| GIATRITHONGSO | MaTS | DINHNGHIATHONGSO(MaTS) | không | RESTRICT |
| NHANVIEN_VAITRO | MaNV | NHANVIEN(MaNV) | không | CASCADE |
| NHANVIEN_VAITRO | MaVT | VAITRO(MaVT) | không | RESTRICT |
| CHITIETKIEMKE | MaDot | DOTKIEMKE(MaDot) | không | RESTRICT |
| CHITIETKIEMKE | MaSP | MATHANG(MaSP) | không | RESTRICT |
| CHITIETTRA | MaHS | HOSODOITRA(MaHS) | không | RESTRICT |
| CHITIETTRA | MaDH, SoDong | CHITIETDONHANG(MaDH, SoDong) | không | RESTRICT |
| CHITIETTRA | MaHS, MaDH | HOSODOITRA(MaHS, MaDH) | không | RESTRICT |
| CHITIETTRA | MaSeri | HANGCOSERI(MaSeri) | có | RESTRICT |
| CHITIETGUIHANG | MaGui | PHIEUGUIHANG(MaGui) | không | RESTRICT |
| CHITIETGUIHANG | MaSP | MATHANG(MaSP) | không | RESTRICT |

## 7.6. Ràng buộc duy nhất và ràng buộc kiểm tra

### 7.6.1. UNIQUE

| Quan hệ | Cột | Loại | Ghi chú |
|---|---|---|---|
| MATHANG | SKU | UNIQUE | Khóa thay thế (mục 5) |
| DONHANG | SoDH | UNIQUE | Khóa thay thế |
| PHIEUNHAP | SoPhieu | UNIQUE | Khóa thay thế |
| MAGIAMGIA | Code | UNIQUE | Khóa thay thế |
| TAIKHOAN | DinhDanhDangNhap | UNIQUE | Khóa thay thế |
| TAIKHOAN | MaKH | UNIQUE (cho phép rỗng) | Mối kết hợp 1–1 với khách |
| BIENDONGSODU | MaHoan | UNIQUE (cho phép rỗng) | Một nguồn không tạo biến động hai lần |
| BANGIAOCOD | MaTT | UNIQUE | Mỗi khoản thu khi giao nộp một lần |
| PHIEUGIAO | MaDH | UNIQUE **[GT]** | Mỗi đơn giao trọn một đợt |
| DINHNGHIATHONGSO | MaLoai, TenTS | UNIQUE | Khóa thay thế ghép |
| ANHMATHANG | MaSP, ViTri | UNIQUE | DDL hiện chưa có |
| ANHMATHANG | MaSP, DuongDan | UNIQUE | DDL đã có |
| HANGCOSERI | MaSP, SoSeri | UNIQUE **[GT]** | Seri duy nhất trong cùng mặt hàng |
| THANHTOAN | DonViThanhToan, MaGiaoDichNgoai | UNIQUE có điều kiện (cả hai khác rỗng) | Chống ghi nhận lặp |
| HOSODOITRA | MaHS, MaDH | UNIQUE | Làm đích cho khóa ngoại ghép (MaHS, MaDH) của CHITIETTRA |
| GIOHANG | MaTK | UNIQUE có điều kiện (TinhTrang = đang dùng) | Mỗi tài khoản tối đa một giỏ đang dùng |
| DIACHINHANHANG | MaKH | UNIQUE có điều kiện (LaMacDinh = đúng) | Tối đa một địa chỉ mặc định |
| ANHMATHANG | MaSP | UNIQUE có điều kiện (LaAnhChinh = đúng) | Tối đa một ảnh chính |

### 7.6.2. CHECK

| Quan hệ | Ràng buộc |
|---|---|
| MATHANG | GiaNiemYet ≥ 0; GiaKhuyenMai rỗng hoặc ≤ GiaNiemYet; ThoiHanBaoHanh ≥ 0 |
| CHITIETDONHANG, CHITIETPHIEUNHAP, CHITIETGIOHANG, GIUHANG, CHITIETGUIHANG | SoLuong > 0 |
| CHITIETDONHANG | DonGiaChot ≥ 0 |
| CHITIETPHIEUNHAP | GiaNhap ≥ 0 |
| THANHTOAN, KHOANHOAN, BANGIAOCOD, BIENDONGSODU (số tiền) | SoTien > 0 (BIENDONGSODU: khác 0) |
| LANGIAO | SoLan từ 1 đến 3 |
| MAGIAMGIA | MucGiam > 0; NgayKetThuc ≥ NgayBatDau |
| DIEUCHINHDON | KhachDongY = đúng |
| GIAODICHKHO | SoLuong > 0 |
| CHITIETGUIHANG | Đúng một trong MaPhieuBH, MaHS khác rỗng |
| Các cột phân loại (KenhBan, LoaiDon, PhuongThuc, TinhTrang...) | Giá trị nằm trong miền ở mục 2 |

## 7.7. Điều phát hiện khi chuyển sang mô hình quan hệ

**1. Thuộc tính dư thừa qua khóa ngoại (xử lý ở mục 8 và 9).**

| Quan hệ | Cột dư thừa | Vì sao dư thừa |
|---|---|---|
| HANGCOSERI | MaSP | Suy ra từ dòng nhập (MaPN, SoDongNhap) hoặc dòng đơn (MaDH, SoDongDon); đã có trong F (mục 3, 4) |
| PHIEUBAOHANH | MaSP | Suy ra từ dòng mua gốc (MaDH, SoDong) hoặc số seri; đã có trong F |
| CHITIETTRA | MaDH | Hồ sơ đổi trả đã xác định đơn gốc (MaHS → MaDH); đã bổ sung vào F ở mục 3 và 4; khóa là (MaHS, SoDong). MaDH vẫn cần để tạo khóa ngoại tới dòng đơn |
| CHITIETGUIHANG | MaSP, MaSeri | Nếu dòng gửi có nguồn là một phiếu bảo hành thì mặt hàng và seri đã có ở phiếu. PTH này chỉ đúng khi có ràng buộc nhất quán, chưa đưa vào F; mục 8 quyết định |

**2. Khóa ngoại ghép.** HANGCOSERI, GIUHANG, PHIEUBAOHANH, CHITIETTRA tham chiếu một dòng của CHITIETDONHANG hoặc CHITIETPHIEUNHAP bằng hai cột. Vì thế các dòng chi tiết phải dùng khóa tự nhiên ghép (MaDH, SoDong) và (MaPN, SoDong); nếu dùng cột `Id` riêng như DDL hiện tại thì khóa ngoại chỉ cần một cột nhưng mất ràng buộc "số dòng không trùng trong đơn" nếu không thêm UNIQUE.

**3. Hai mối kết hợp dư thừa vẽ nét đứt ở ERD (R38, R42)** vẫn được chuyển thành khóa ngoại MaSP trong PHIEUBAOHANH và HANGCOSERI để mô hình khớp với F của mục 3; chúng sẽ bị loại ở mục 9.

**4. Khóa ngoại cho phép rỗng** thể hiện bản số tối thiểu 0: DONHANG.MaKH, DONHANG.MaMG, THANHTOAN.MaNVXacNhan, HANGCOSERI (MaDH, SoDongDon), PHIEUBAOHANH.MaKH, MaSeri, HOSODOITRA.MaKH, KHOANHOAN.MaHS, LANNHANLAI.MaNVKiemTra, MaNVDuyet, DOTKIEMKE.MaNVDuyet, TAIKHOAN.MaKH, CHITIETGUIHANG.MaSeri, MaPhieuBH, MaHS.

## 7.8. Đối chiếu với `database/data.sql`

| Nội dung | Mô hình này | DDL hiện tại |
|---|---|---|
| Khóa chính các quan hệ dòng chi tiết | Khóa ghép tự nhiên (MaDH, SoDong), (MaPN, SoDong) | Cột `Id` riêng, không UNIQUE cặp (đơn, mặt hàng) và không có số dòng |
| Khách, nhân viên, tài khoản | Ba quan hệ KHACHHANG, NHANVIEN, TAIKHOAN | Một bảng `AspNetUsers` |
| Địa chỉ | Tỉnh, phường hoặc xã, địa chỉ cụ thể | Thêm `District` |
| Phương thức thanh toán | Thuộc tính của THANHTOAN, không có thực thể riêng | Cột `PaymentMethod` ở cả `Orders` và `Payments` (hai nơi) |
| Tổng tiền | Không lưu (dữ liệu tính) | `Subtotal`, `TotalAmount`, `LineTotal` lưu sẵn |
| Tồn kho | Tính từ GIAODICHKHO | `StockQuantity`, `SoldQuantity` lưu sẵn |
| Quan hệ mới (seri, giữ hàng, giao hàng, đổi trả, bảo hành, kiểm kê...) | Có (16 quan hệ chưa có trong DDL) | Không có |
| Bảng ngoài phạm vi v3 | Không có | Đánh giá, hỗ trợ, thu cũ, thông báo, bảng định danh phụ |

## 7.9. Câu hỏi giảng viên có thể hỏi

- *Vì sao MKH CHITIETDONHANG có khóa (MaDH, SoDong) mà không phải (MaDH, MaSP)?* Vì v3 cho phép một mặt hàng ở nhiều dòng của một đơn; nếu khóa là (MaDH, MaSP) thì không biểu diễn được trường hợp này.
- *Khóa ngoại ghép dùng để làm gì?* Để một bản ghi (giữ hàng, phiếu bảo hành, chiếc có seri, dòng trả) trỏ đúng một dòng cụ thể của đơn hoặc phiếu nhập.
- *Vì sao quan hệ 1–1 vẫn cần UNIQUE?* Khóa ngoại một mình chỉ bảo đảm "tối đa một cha", không bảo đảm "tối đa một con"; UNIQUE trên khóa ngoại làm cho phía kia cũng chỉ có tối đa một.
- *Vì sao cho phép khóa ngoại rỗng?* Bản số tối thiểu 0: khách quầy không để lại thông tin nên đơn không có khách; đơn không dùng mã giảm giá không có MaMG.
- *Mô hình này đã đạt dạng chuẩn nào?* Chưa kết luận ở mục này; mục 8 xét từng quan hệ, các thuộc tính dư thừa ở 7.7 là chỗ cần cải tiến.
