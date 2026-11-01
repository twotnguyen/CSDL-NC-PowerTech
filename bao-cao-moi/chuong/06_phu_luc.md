# PHỤ LỤC: TRUY VẤN SQL CHO 61 CON ĐƯỜNG TRUY XUẤT

Phụ lục in lại nội dung file `sql/03_truy_van_cac_duong_truy_xuat.sql`. Số dòng kết quả tính trên dữ liệu minh họa `sql/02_du_lieu_minh_hoa.sql`.

Các đường ghi “lần bán gần nhất” đi từ dòng trả hoặc phiếu bảo hành qua HANGCOSERI tới đơn hàng, nên cho người mua của lần bán gần nhất của chiếc hàng. Khi chiếc hàng đã được bán lại, đó không phải người mua gốc; đơn gốc tra qua HOSODOITRA.MaDH hoặc cặp (MaDH, SoDongDH) của phiếu bảo hành.

**Đường 1:** ANHMATHANG → MATHANG → LOAIHANG (5 dòng)

```sql
SELECT am.MaAnh, mh.MaSP, lh.MaLoai
FROM ANHMATHANG am
JOIN MATHANG mh ON am.MaSP = mh.MaSP
JOIN LOAIHANG lh ON mh.MaLoai = lh.MaLoai;
```

**Đường 2:** ANHMATHANG → MATHANG → THUONGHIEU (5 dòng)

```sql
SELECT am.MaAnh, mh.MaSP, th.MaTH
FROM ANHMATHANG am
JOIN MATHANG mh ON am.MaSP = mh.MaSP
JOIN THUONGHIEU th ON mh.MaTH = th.MaTH;
```

**Đường 3:** GIATRITHONGSO → MATHANG → LOAIHANG (5 dòng)

```sql
SELECT gt.MaSP, gt.MaTS, lh.MaLoai
FROM GIATRITHONGSO gt
JOIN MATHANG mh ON gt.MaSP = mh.MaSP
JOIN LOAIHANG lh ON mh.MaLoai = lh.MaLoai;
```

**Đường 4:** GIATRITHONGSO → MATHANG → THUONGHIEU (5 dòng)

```sql
SELECT gt.MaSP, gt.MaTS, th.MaTH
FROM GIATRITHONGSO gt
JOIN MATHANG mh ON gt.MaSP = mh.MaSP
JOIN THUONGHIEU th ON mh.MaTH = th.MaTH;
```

**Đường 5:** GIATRITHONGSO → DINHNGHIATHONGSO → LOAIHANG (5 dòng)

```sql
SELECT gt.MaSP, gt.MaTS, lh.MaLoai
FROM GIATRITHONGSO gt
JOIN DINHNGHIATHONGSO dn ON gt.MaTS = dn.MaTS
JOIN LOAIHANG lh ON dn.MaLoai = lh.MaLoai;
```

**Đường 6:** TAIKHOAN → KHACHHANG (3 dòng)

```sql
SELECT tk.MaTK, kh.MaKH
FROM TAIKHOAN tk
JOIN KHACHHANG kh ON tk.MaKH = kh.MaKH;
```

**Đường 7:** TAIKHOAN → NHANVIEN (3 dòng)

```sql
SELECT tk.MaTK, nv.MaNV
FROM TAIKHOAN tk
JOIN NHANVIEN nv ON tk.MaNV = nv.MaNV;
```

**Đường 8:** LANGIAO → NHANVIEN (4 dòng)

```sql
SELECT lg.MaGiao, lg.SoLan, nv.MaNV
FROM LANGIAO lg
JOIN NHANVIEN nv ON lg.MaNV = nv.MaNV;
```

**Đường 9:** LANGIAO → PHIEUGIAO → NHANVIEN (4 dòng)

```sql
SELECT lg.MaGiao, lg.SoLan, nv.MaNV
FROM LANGIAO lg
JOIN PHIEUGIAO pg ON lg.MaGiao = pg.MaGiao
JOIN NHANVIEN nv ON pg.MaNV = nv.MaNV;
```

**Đường 10:** LANGIAO → PHIEUGIAO → DONHANG → KHACHHANG (4 dòng)

```sql
SELECT lg.MaGiao, lg.SoLan, dh.MaDH, kh.MaKH
FROM LANGIAO lg
JOIN PHIEUGIAO pg ON lg.MaGiao = pg.MaGiao
JOIN DONHANG dh ON pg.MaDH = dh.MaDH
JOIN KHACHHANG kh ON dh.MaKH = kh.MaKH;
```

**Đường 11:** LANGIAO → PHIEUGIAO → DONHANG → NHANVIEN (1 dòng)

```sql
SELECT lg.MaGiao, lg.SoLan, dh.MaDH, nv.MaNV
FROM LANGIAO lg
JOIN PHIEUGIAO pg ON lg.MaGiao = pg.MaGiao
JOIN DONHANG dh ON pg.MaDH = dh.MaDH
JOIN NHANVIEN nv ON dh.MaNV = nv.MaNV;
```

**Đường 12:** LANGIAO → PHIEUGIAO → DONHANG → MAGIAMGIA → NHANVIEN (1 dòng)

```sql
SELECT lg.MaGiao, lg.SoLan, dh.MaDH, mg.MaMG, nv.MaNV
FROM LANGIAO lg
JOIN PHIEUGIAO pg ON lg.MaGiao = pg.MaGiao
JOIN DONHANG dh ON pg.MaDH = dh.MaDH
JOIN MAGIAMGIA mg ON dh.MaMG = mg.MaMG
JOIN NHANVIEN nv ON mg.MaNV = nv.MaNV;
```

**Đường 13:** GIAODICHKHO → MATHANG → LOAIHANG (6 dòng)

```sql
SELECT gd.MaGDK, mh.MaSP, lh.MaLoai
FROM GIAODICHKHO gd
JOIN MATHANG mh ON gd.MaSP = mh.MaSP
JOIN LOAIHANG lh ON mh.MaLoai = lh.MaLoai;
```

**Đường 14:** GIAODICHKHO → MATHANG → THUONGHIEU (6 dòng)

```sql
SELECT gd.MaGDK, mh.MaSP, th.MaTH
FROM GIAODICHKHO gd
JOIN MATHANG mh ON gd.MaSP = mh.MaSP
JOIN THUONGHIEU th ON mh.MaTH = th.MaTH;
```

**Đường 15:** GIAODICHKHO → NHANVIEN (6 dòng)

```sql
SELECT gd.MaGDK, nv.MaNV
FROM GIAODICHKHO gd
JOIN NHANVIEN nv ON gd.MaNV = nv.MaNV;
```

**Đường 16:** CHITIETTRA → HANGCOSERI → MATHANG → LOAIHANG (1 dòng)

```sql
SELECT cr.MaHS, cr.SoDongTra, hs.MaSeri, mh.MaSP, lh.MaLoai
FROM CHITIETTRA cr
JOIN HANGCOSERI hs ON cr.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN MATHANG mh ON sm.MaSP = mh.MaSP
JOIN LOAIHANG lh ON mh.MaLoai = lh.MaLoai;
```

**Đường 17:** CHITIETTRA → HANGCOSERI → MATHANG → THUONGHIEU (1 dòng)

```sql
SELECT cr.MaHS, cr.SoDongTra, hs.MaSeri, mh.MaSP, th.MaTH
FROM CHITIETTRA cr
JOIN HANGCOSERI hs ON cr.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN MATHANG mh ON sm.MaSP = mh.MaSP
JOIN THUONGHIEU th ON mh.MaTH = th.MaTH;
```

**Đường 18:** CHITIETTRA → HANGCOSERI → CHITIETDONHANG → MATHANG → LOAIHANG (1 dòng)

```sql
SELECT cr.MaHS, cr.SoDongTra, hs.MaSeri, ct.MaDH, ct.SoDongDH, mh.MaSP, lh.MaLoai
FROM CHITIETTRA cr
JOIN HANGCOSERI hs ON cr.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETDONHANG ct ON hs.MaDH = ct.MaDH AND hs.SoDongDH = ct.SoDongDH
JOIN MATHANG mh ON ct.MaSP = mh.MaSP
JOIN LOAIHANG lh ON mh.MaLoai = lh.MaLoai;
```

**Đường 19:** CHITIETTRA → HANGCOSERI → CHITIETDONHANG → MATHANG → THUONGHIEU (1 dòng)

```sql
SELECT cr.MaHS, cr.SoDongTra, hs.MaSeri, ct.MaDH, ct.SoDongDH, mh.MaSP, th.MaTH
FROM CHITIETTRA cr
JOIN HANGCOSERI hs ON cr.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETDONHANG ct ON hs.MaDH = ct.MaDH AND hs.SoDongDH = ct.SoDongDH
JOIN MATHANG mh ON ct.MaSP = mh.MaSP
JOIN THUONGHIEU th ON mh.MaTH = th.MaTH;
```

**Đường 20:** CHITIETTRA → HANGCOSERI → CHITIETDONHANG → DONHANG → KHACHHANG (1 dòng; lần bán gần nhất)

```sql
SELECT cr.MaHS, cr.SoDongTra, hs.MaSeri, ct.MaDH, ct.SoDongDH, kh.MaKH
FROM CHITIETTRA cr
JOIN HANGCOSERI hs ON cr.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETDONHANG ct ON hs.MaDH = ct.MaDH AND hs.SoDongDH = ct.SoDongDH
JOIN DONHANG dh ON ct.MaDH = dh.MaDH
JOIN KHACHHANG kh ON dh.MaKH = kh.MaKH;
```

**Đường 21:** CHITIETTRA → HANGCOSERI → CHITIETDONHANG → DONHANG → NHANVIEN (1 dòng; lần bán gần nhất)

```sql
SELECT cr.MaHS, cr.SoDongTra, hs.MaSeri, ct.MaDH, ct.SoDongDH, nv.MaNV
FROM CHITIETTRA cr
JOIN HANGCOSERI hs ON cr.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETDONHANG ct ON hs.MaDH = ct.MaDH AND hs.SoDongDH = ct.SoDongDH
JOIN DONHANG dh ON ct.MaDH = dh.MaDH
JOIN NHANVIEN nv ON dh.MaNV = nv.MaNV;
```

**Đường 22:** CHITIETTRA → HANGCOSERI → CHITIETDONHANG → DONHANG → MAGIAMGIA → NHANVIEN (1 dòng; lần bán gần nhất)

```sql
SELECT cr.MaHS, cr.SoDongTra, hs.MaSeri, ct.MaDH, ct.SoDongDH, mg.MaMG, nv.MaNV
FROM CHITIETTRA cr
JOIN HANGCOSERI hs ON cr.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETDONHANG ct ON hs.MaDH = ct.MaDH AND hs.SoDongDH = ct.SoDongDH
JOIN DONHANG dh ON ct.MaDH = dh.MaDH
JOIN MAGIAMGIA mg ON dh.MaMG = mg.MaMG
JOIN NHANVIEN nv ON mg.MaNV = nv.MaNV;
```

**Đường 23:** CHITIETTRA → HANGCOSERI → CHITIETPHIEUNHAP → MATHANG → LOAIHANG (1 dòng)

```sql
SELECT cr.MaHS, cr.SoDongTra, hs.MaSeri, cp.MaPN, cp.SoDongPN, mh.MaSP, lh.MaLoai
FROM CHITIETTRA cr
JOIN HANGCOSERI hs ON cr.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETPHIEUNHAP cp ON hs.MaPN = cp.MaPN AND hs.SoDongPN = cp.SoDongPN
JOIN MATHANG mh ON cp.MaSP = mh.MaSP
JOIN LOAIHANG lh ON mh.MaLoai = lh.MaLoai;
```

**Đường 24:** CHITIETTRA → HANGCOSERI → CHITIETPHIEUNHAP → MATHANG → THUONGHIEU (1 dòng)

```sql
SELECT cr.MaHS, cr.SoDongTra, hs.MaSeri, cp.MaPN, cp.SoDongPN, mh.MaSP, th.MaTH
FROM CHITIETTRA cr
JOIN HANGCOSERI hs ON cr.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETPHIEUNHAP cp ON hs.MaPN = cp.MaPN AND hs.SoDongPN = cp.SoDongPN
JOIN MATHANG mh ON cp.MaSP = mh.MaSP
JOIN THUONGHIEU th ON mh.MaTH = th.MaTH;
```

**Đường 25:** CHITIETTRA → HANGCOSERI → CHITIETPHIEUNHAP → PHIEUNHAP → NHANVIEN (1 dòng)

```sql
SELECT cr.MaHS, cr.SoDongTra, hs.MaSeri, cp.MaPN, cp.SoDongPN, nv.MaNV
FROM CHITIETTRA cr
JOIN HANGCOSERI hs ON cr.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETPHIEUNHAP cp ON hs.MaPN = cp.MaPN AND hs.SoDongPN = cp.SoDongPN
JOIN PHIEUNHAP pn ON cp.MaPN = pn.MaPN
JOIN NHANVIEN nv ON pn.MaNV = nv.MaNV;
```

**Đường 26:** CHITIETTRA → HANGCOSERI → CHITIETPHIEUNHAP → PHIEUNHAP → NHACUNGCAP (1 dòng)

```sql
SELECT cr.MaHS, cr.SoDongTra, hs.MaSeri, cp.MaPN, cp.SoDongPN, nc.MaNCC
FROM CHITIETTRA cr
JOIN HANGCOSERI hs ON cr.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETPHIEUNHAP cp ON hs.MaPN = cp.MaPN AND hs.SoDongPN = cp.SoDongPN
JOIN PHIEUNHAP pn ON cp.MaPN = pn.MaPN
JOIN NHACUNGCAP nc ON pn.MaNCC = nc.MaNCC;
```

**Đường 27:** CHITIETTRA → HOSODOITRA → NHANVIEN (1 dòng)

```sql
SELECT cr.MaHS, cr.SoDongTra, nv.MaNV
FROM CHITIETTRA cr
JOIN HOSODOITRA hd ON cr.MaHS = hd.MaHS
JOIN NHANVIEN nv ON hd.MaNV = nv.MaNV;
```

**Đường 28:** CHITIETTRA → HOSODOITRA → DONHANG → KHACHHANG (1 dòng)

```sql
SELECT cr.MaHS, cr.SoDongTra, dh.MaDH, kh.MaKH
FROM CHITIETTRA cr
JOIN HOSODOITRA hd ON cr.MaHS = hd.MaHS
JOIN DONHANG dh ON hd.MaDH = dh.MaDH
JOIN KHACHHANG kh ON dh.MaKH = kh.MaKH;
```

**Đường 29:** CHITIETTRA → HOSODOITRA → DONHANG → NHANVIEN (1 dòng)

```sql
SELECT cr.MaHS, cr.SoDongTra, dh.MaDH, nv.MaNV
FROM CHITIETTRA cr
JOIN HOSODOITRA hd ON cr.MaHS = hd.MaHS
JOIN DONHANG dh ON hd.MaDH = dh.MaDH
JOIN NHANVIEN nv ON dh.MaNV = nv.MaNV;
```

**Đường 30:** CHITIETTRA → HOSODOITRA → DONHANG → MAGIAMGIA → NHANVIEN (1 dòng)

```sql
SELECT cr.MaHS, cr.SoDongTra, dh.MaDH, mg.MaMG, nv.MaNV
FROM CHITIETTRA cr
JOIN HOSODOITRA hd ON cr.MaHS = hd.MaHS
JOIN DONHANG dh ON hd.MaDH = dh.MaDH
JOIN MAGIAMGIA mg ON dh.MaMG = mg.MaMG
JOIN NHANVIEN nv ON mg.MaNV = nv.MaNV;
```

**Đường 31:** LANNHANLAI → NHANVIEN (1 dòng)

```sql
SELECT nl.MaNhanLai, nv.MaNV
FROM LANNHANLAI nl
JOIN NHANVIEN nv ON nl.MaNV = nv.MaNV;
```

**Đường 32:** LANNHANLAI → HOSODOITRA → NHANVIEN (1 dòng)

```sql
SELECT nl.MaNhanLai, hd.MaHS, nv.MaNV
FROM LANNHANLAI nl
JOIN HOSODOITRA hd ON nl.MaHS = hd.MaHS
JOIN NHANVIEN nv ON hd.MaNV = nv.MaNV;
```

**Đường 33:** LANNHANLAI → HOSODOITRA → DONHANG → KHACHHANG (1 dòng)

```sql
SELECT nl.MaNhanLai, hd.MaHS, dh.MaDH, kh.MaKH
FROM LANNHANLAI nl
JOIN HOSODOITRA hd ON nl.MaHS = hd.MaHS
JOIN DONHANG dh ON hd.MaDH = dh.MaDH
JOIN KHACHHANG kh ON dh.MaKH = kh.MaKH;
```

**Đường 34:** LANNHANLAI → HOSODOITRA → DONHANG → NHANVIEN (1 dòng)

```sql
SELECT nl.MaNhanLai, hd.MaHS, dh.MaDH, nv.MaNV
FROM LANNHANLAI nl
JOIN HOSODOITRA hd ON nl.MaHS = hd.MaHS
JOIN DONHANG dh ON hd.MaDH = dh.MaDH
JOIN NHANVIEN nv ON dh.MaNV = nv.MaNV;
```

**Đường 35:** LANNHANLAI → HOSODOITRA → DONHANG → MAGIAMGIA → NHANVIEN (1 dòng)

```sql
SELECT nl.MaNhanLai, hd.MaHS, dh.MaDH, mg.MaMG, nv.MaNV
FROM LANNHANLAI nl
JOIN HOSODOITRA hd ON nl.MaHS = hd.MaHS
JOIN DONHANG dh ON hd.MaDH = dh.MaDH
JOIN MAGIAMGIA mg ON dh.MaMG = mg.MaMG
JOIN NHANVIEN nv ON mg.MaNV = nv.MaNV;
```

**Đường 36:** KHOANHOAN → NHANVIEN (2 dòng)

```sql
SELECT kc.MaHoan, nv.MaNV
FROM KHOANHOAN kc
JOIN NHANVIEN nv ON kc.MaNV = nv.MaNV;
```

**Đường 37:** KHOANHOAN → THANHTOAN → NHANVIEN (2 dòng)

```sql
SELECT kc.MaHoan, tt.MaTT, nv.MaNV
FROM KHOANHOAN kc
JOIN THANHTOAN tt ON kc.MaTT = tt.MaTT
JOIN NHANVIEN nv ON tt.MaNV = nv.MaNV;
```

**Đường 38:** KHOANHOAN → THANHTOAN → DONHANG → KHACHHANG (2 dòng)

```sql
SELECT kc.MaHoan, tt.MaTT, dh.MaDH, kh.MaKH
FROM KHOANHOAN kc
JOIN THANHTOAN tt ON kc.MaTT = tt.MaTT
JOIN DONHANG dh ON tt.MaDH = dh.MaDH
JOIN KHACHHANG kh ON dh.MaKH = kh.MaKH;
```

**Đường 39:** KHOANHOAN → THANHTOAN → DONHANG → NHANVIEN (2 dòng)

```sql
SELECT kc.MaHoan, tt.MaTT, dh.MaDH, nv.MaNV
FROM KHOANHOAN kc
JOIN THANHTOAN tt ON kc.MaTT = tt.MaTT
JOIN DONHANG dh ON tt.MaDH = dh.MaDH
JOIN NHANVIEN nv ON dh.MaNV = nv.MaNV;
```

**Đường 40:** KHOANHOAN → THANHTOAN → DONHANG → MAGIAMGIA → NHANVIEN (2 dòng)

```sql
SELECT kc.MaHoan, tt.MaTT, dh.MaDH, mg.MaMG, nv.MaNV
FROM KHOANHOAN kc
JOIN THANHTOAN tt ON kc.MaTT = tt.MaTT
JOIN DONHANG dh ON tt.MaDH = dh.MaDH
JOIN MAGIAMGIA mg ON dh.MaMG = mg.MaMG
JOIN NHANVIEN nv ON mg.MaNV = nv.MaNV;
```

**Đường 41:** KHOANHOAN → HOSODOITRA → NHANVIEN (1 dòng)

```sql
SELECT kc.MaHoan, hd.MaHS, nv.MaNV
FROM KHOANHOAN kc
JOIN HOSODOITRA hd ON kc.MaHS = hd.MaHS
JOIN NHANVIEN nv ON hd.MaNV = nv.MaNV;
```

**Đường 42:** KHOANHOAN → HOSODOITRA → DONHANG → KHACHHANG (1 dòng)

```sql
SELECT kc.MaHoan, hd.MaHS, dh.MaDH, kh.MaKH
FROM KHOANHOAN kc
JOIN HOSODOITRA hd ON kc.MaHS = hd.MaHS
JOIN DONHANG dh ON hd.MaDH = dh.MaDH
JOIN KHACHHANG kh ON dh.MaKH = kh.MaKH;
```

**Đường 43:** KHOANHOAN → HOSODOITRA → DONHANG → NHANVIEN (1 dòng)

```sql
SELECT kc.MaHoan, hd.MaHS, dh.MaDH, nv.MaNV
FROM KHOANHOAN kc
JOIN HOSODOITRA hd ON kc.MaHS = hd.MaHS
JOIN DONHANG dh ON hd.MaDH = dh.MaDH
JOIN NHANVIEN nv ON dh.MaNV = nv.MaNV;
```

**Đường 44:** KHOANHOAN → HOSODOITRA → DONHANG → MAGIAMGIA → NHANVIEN (1 dòng)

```sql
SELECT kc.MaHoan, hd.MaHS, dh.MaDH, mg.MaMG, nv.MaNV
FROM KHOANHOAN kc
JOIN HOSODOITRA hd ON kc.MaHS = hd.MaHS
JOIN DONHANG dh ON hd.MaDH = dh.MaDH
JOIN MAGIAMGIA mg ON dh.MaMG = mg.MaMG
JOIN NHANVIEN nv ON mg.MaNV = nv.MaNV;
```

**Đường 45:** KHOANHOAN → PHIEUBAOHANH → NHANVIEN (1 dòng)

```sql
SELECT kc.MaHoan, bh.MaPhieuBH, nv.MaNV
FROM KHOANHOAN kc
JOIN PHIEUBAOHANH bh ON kc.MaPhieuBH = bh.MaPhieuBH
JOIN NHANVIEN nv ON bh.MaNV = nv.MaNV;
```

**Đường 46:** KHOANHOAN → PHIEUBAOHANH → CHITIETDONHANG → MATHANG → LOAIHANG (1 dòng)

```sql
SELECT kc.MaHoan, bh.MaPhieuBH, ct.MaDH, ct.SoDongDH, mh.MaSP, lh.MaLoai
FROM KHOANHOAN kc
JOIN PHIEUBAOHANH bh ON kc.MaPhieuBH = bh.MaPhieuBH
JOIN CHITIETDONHANG ct ON bh.MaDH = ct.MaDH AND bh.SoDongDH = ct.SoDongDH
JOIN MATHANG mh ON ct.MaSP = mh.MaSP
JOIN LOAIHANG lh ON mh.MaLoai = lh.MaLoai;
```

**Đường 47:** KHOANHOAN → PHIEUBAOHANH → CHITIETDONHANG → MATHANG → THUONGHIEU (1 dòng)

```sql
SELECT kc.MaHoan, bh.MaPhieuBH, ct.MaDH, ct.SoDongDH, mh.MaSP, th.MaTH
FROM KHOANHOAN kc
JOIN PHIEUBAOHANH bh ON kc.MaPhieuBH = bh.MaPhieuBH
JOIN CHITIETDONHANG ct ON bh.MaDH = ct.MaDH AND bh.SoDongDH = ct.SoDongDH
JOIN MATHANG mh ON ct.MaSP = mh.MaSP
JOIN THUONGHIEU th ON mh.MaTH = th.MaTH;
```

**Đường 48:** KHOANHOAN → PHIEUBAOHANH → CHITIETDONHANG → DONHANG → KHACHHANG (1 dòng)

```sql
SELECT kc.MaHoan, bh.MaPhieuBH, ct.MaDH, ct.SoDongDH, kh.MaKH
FROM KHOANHOAN kc
JOIN PHIEUBAOHANH bh ON kc.MaPhieuBH = bh.MaPhieuBH
JOIN CHITIETDONHANG ct ON bh.MaDH = ct.MaDH AND bh.SoDongDH = ct.SoDongDH
JOIN DONHANG dh ON ct.MaDH = dh.MaDH
JOIN KHACHHANG kh ON dh.MaKH = kh.MaKH;
```

**Đường 49:** KHOANHOAN → PHIEUBAOHANH → CHITIETDONHANG → DONHANG → NHANVIEN (1 dòng)

```sql
SELECT kc.MaHoan, bh.MaPhieuBH, ct.MaDH, ct.SoDongDH, nv.MaNV
FROM KHOANHOAN kc
JOIN PHIEUBAOHANH bh ON kc.MaPhieuBH = bh.MaPhieuBH
JOIN CHITIETDONHANG ct ON bh.MaDH = ct.MaDH AND bh.SoDongDH = ct.SoDongDH
JOIN DONHANG dh ON ct.MaDH = dh.MaDH
JOIN NHANVIEN nv ON dh.MaNV = nv.MaNV;
```

**Đường 50:** KHOANHOAN → PHIEUBAOHANH → CHITIETDONHANG → DONHANG → MAGIAMGIA → NHANVIEN (1 dòng)

```sql
SELECT kc.MaHoan, bh.MaPhieuBH, ct.MaDH, ct.SoDongDH, mg.MaMG, nv.MaNV
FROM KHOANHOAN kc
JOIN PHIEUBAOHANH bh ON kc.MaPhieuBH = bh.MaPhieuBH
JOIN CHITIETDONHANG ct ON bh.MaDH = ct.MaDH AND bh.SoDongDH = ct.SoDongDH
JOIN DONHANG dh ON ct.MaDH = dh.MaDH
JOIN MAGIAMGIA mg ON dh.MaMG = mg.MaMG
JOIN NHANVIEN nv ON mg.MaNV = nv.MaNV;
```

**Đường 51:** KHOANHOAN → PHIEUBAOHANH → HANGCOSERI → MATHANG → LOAIHANG (1 dòng)

```sql
SELECT kc.MaHoan, bh.MaPhieuBH, hs.MaSeri, mh.MaSP, lh.MaLoai
FROM KHOANHOAN kc
JOIN PHIEUBAOHANH bh ON kc.MaPhieuBH = bh.MaPhieuBH
JOIN HANGCOSERI hs ON bh.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN MATHANG mh ON sm.MaSP = mh.MaSP
JOIN LOAIHANG lh ON mh.MaLoai = lh.MaLoai;
```

**Đường 52:** KHOANHOAN → PHIEUBAOHANH → HANGCOSERI → MATHANG → THUONGHIEU (1 dòng)

```sql
SELECT kc.MaHoan, bh.MaPhieuBH, hs.MaSeri, mh.MaSP, th.MaTH
FROM KHOANHOAN kc
JOIN PHIEUBAOHANH bh ON kc.MaPhieuBH = bh.MaPhieuBH
JOIN HANGCOSERI hs ON bh.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN MATHANG mh ON sm.MaSP = mh.MaSP
JOIN THUONGHIEU th ON mh.MaTH = th.MaTH;
```

**Đường 53:** KHOANHOAN → PHIEUBAOHANH → HANGCOSERI → CHITIETDONHANG → MATHANG → LOAIHANG (1 dòng)

```sql
SELECT kc.MaHoan, bh.MaPhieuBH, hs.MaSeri, ct.MaDH, ct.SoDongDH, mh.MaSP, lh.MaLoai
FROM KHOANHOAN kc
JOIN PHIEUBAOHANH bh ON kc.MaPhieuBH = bh.MaPhieuBH
JOIN HANGCOSERI hs ON bh.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETDONHANG ct ON hs.MaDH = ct.MaDH AND hs.SoDongDH = ct.SoDongDH
JOIN MATHANG mh ON ct.MaSP = mh.MaSP
JOIN LOAIHANG lh ON mh.MaLoai = lh.MaLoai;
```

**Đường 54:** KHOANHOAN → PHIEUBAOHANH → HANGCOSERI → CHITIETDONHANG → MATHANG → THUONGHIEU (1 dòng)

```sql
SELECT kc.MaHoan, bh.MaPhieuBH, hs.MaSeri, ct.MaDH, ct.SoDongDH, mh.MaSP, th.MaTH
FROM KHOANHOAN kc
JOIN PHIEUBAOHANH bh ON kc.MaPhieuBH = bh.MaPhieuBH
JOIN HANGCOSERI hs ON bh.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETDONHANG ct ON hs.MaDH = ct.MaDH AND hs.SoDongDH = ct.SoDongDH
JOIN MATHANG mh ON ct.MaSP = mh.MaSP
JOIN THUONGHIEU th ON mh.MaTH = th.MaTH;
```

**Đường 55:** KHOANHOAN → PHIEUBAOHANH → HANGCOSERI → CHITIETDONHANG → DONHANG → KHACHHANG (1 dòng; lần bán gần nhất)

```sql
SELECT kc.MaHoan, bh.MaPhieuBH, hs.MaSeri, ct.MaDH, ct.SoDongDH, kh.MaKH
FROM KHOANHOAN kc
JOIN PHIEUBAOHANH bh ON kc.MaPhieuBH = bh.MaPhieuBH
JOIN HANGCOSERI hs ON bh.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETDONHANG ct ON hs.MaDH = ct.MaDH AND hs.SoDongDH = ct.SoDongDH
JOIN DONHANG dh ON ct.MaDH = dh.MaDH
JOIN KHACHHANG kh ON dh.MaKH = kh.MaKH;
```

**Đường 56:** KHOANHOAN → PHIEUBAOHANH → HANGCOSERI → CHITIETDONHANG → DONHANG → NHANVIEN (1 dòng; lần bán gần nhất)

```sql
SELECT kc.MaHoan, bh.MaPhieuBH, hs.MaSeri, ct.MaDH, ct.SoDongDH, nv.MaNV
FROM KHOANHOAN kc
JOIN PHIEUBAOHANH bh ON kc.MaPhieuBH = bh.MaPhieuBH
JOIN HANGCOSERI hs ON bh.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETDONHANG ct ON hs.MaDH = ct.MaDH AND hs.SoDongDH = ct.SoDongDH
JOIN DONHANG dh ON ct.MaDH = dh.MaDH
JOIN NHANVIEN nv ON dh.MaNV = nv.MaNV;
```

**Đường 57:** KHOANHOAN → PHIEUBAOHANH → HANGCOSERI → CHITIETDONHANG → DONHANG → MAGIAMGIA → NHANVIEN (1 dòng; lần bán gần nhất)

```sql
SELECT kc.MaHoan, bh.MaPhieuBH, hs.MaSeri, ct.MaDH, ct.SoDongDH, mg.MaMG, nv.MaNV
FROM KHOANHOAN kc
JOIN PHIEUBAOHANH bh ON kc.MaPhieuBH = bh.MaPhieuBH
JOIN HANGCOSERI hs ON bh.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETDONHANG ct ON hs.MaDH = ct.MaDH AND hs.SoDongDH = ct.SoDongDH
JOIN DONHANG dh ON ct.MaDH = dh.MaDH
JOIN MAGIAMGIA mg ON dh.MaMG = mg.MaMG
JOIN NHANVIEN nv ON mg.MaNV = nv.MaNV;
```

**Đường 58:** KHOANHOAN → PHIEUBAOHANH → HANGCOSERI → CHITIETPHIEUNHAP → MATHANG → LOAIHANG (1 dòng)

```sql
SELECT kc.MaHoan, bh.MaPhieuBH, hs.MaSeri, cp.MaPN, cp.SoDongPN, mh.MaSP, lh.MaLoai
FROM KHOANHOAN kc
JOIN PHIEUBAOHANH bh ON kc.MaPhieuBH = bh.MaPhieuBH
JOIN HANGCOSERI hs ON bh.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETPHIEUNHAP cp ON hs.MaPN = cp.MaPN AND hs.SoDongPN = cp.SoDongPN
JOIN MATHANG mh ON cp.MaSP = mh.MaSP
JOIN LOAIHANG lh ON mh.MaLoai = lh.MaLoai;
```

**Đường 59:** KHOANHOAN → PHIEUBAOHANH → HANGCOSERI → CHITIETPHIEUNHAP → MATHANG → THUONGHIEU (1 dòng)

```sql
SELECT kc.MaHoan, bh.MaPhieuBH, hs.MaSeri, cp.MaPN, cp.SoDongPN, mh.MaSP, th.MaTH
FROM KHOANHOAN kc
JOIN PHIEUBAOHANH bh ON kc.MaPhieuBH = bh.MaPhieuBH
JOIN HANGCOSERI hs ON bh.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETPHIEUNHAP cp ON hs.MaPN = cp.MaPN AND hs.SoDongPN = cp.SoDongPN
JOIN MATHANG mh ON cp.MaSP = mh.MaSP
JOIN THUONGHIEU th ON mh.MaTH = th.MaTH;
```

**Đường 60:** KHOANHOAN → PHIEUBAOHANH → HANGCOSERI → CHITIETPHIEUNHAP → PHIEUNHAP → NHANVIEN (1 dòng)

```sql
SELECT kc.MaHoan, bh.MaPhieuBH, hs.MaSeri, cp.MaPN, cp.SoDongPN, nv.MaNV
FROM KHOANHOAN kc
JOIN PHIEUBAOHANH bh ON kc.MaPhieuBH = bh.MaPhieuBH
JOIN HANGCOSERI hs ON bh.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETPHIEUNHAP cp ON hs.MaPN = cp.MaPN AND hs.SoDongPN = cp.SoDongPN
JOIN PHIEUNHAP pn ON cp.MaPN = pn.MaPN
JOIN NHANVIEN nv ON pn.MaNV = nv.MaNV;
```

**Đường 61:** KHOANHOAN → PHIEUBAOHANH → HANGCOSERI → CHITIETPHIEUNHAP → PHIEUNHAP → NHACUNGCAP (1 dòng)

```sql
SELECT kc.MaHoan, bh.MaPhieuBH, hs.MaSeri, cp.MaPN, cp.SoDongPN, nc.MaNCC
FROM KHOANHOAN kc
JOIN PHIEUBAOHANH bh ON kc.MaPhieuBH = bh.MaPhieuBH
JOIN HANGCOSERI hs ON bh.MaSeri = hs.MaSeri
JOIN SERIMATHANG sm ON sm.MaSeri = hs.MaSeri
JOIN CHITIETPHIEUNHAP cp ON hs.MaPN = cp.MaPN AND hs.SoDongPN = cp.SoDongPN
JOIN PHIEUNHAP pn ON cp.MaPN = pn.MaPN
JOIN NHACUNGCAP nc ON pn.MaNCC = nc.MaNCC;
```

