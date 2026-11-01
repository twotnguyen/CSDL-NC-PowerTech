# 10. Những câu dễ bị hỏi khó khi bảo vệ, và câu trả lời sẵn

Tài liệu cho Twot ôn vấn đáp. Mỗi câu có: **câu hỏi thầy có thể hỏi**, **trả lời ngắn** (nói được trong 20–30 giây), **căn cứ** (mục trong báo cáo để mở ra chỉ). Nguyên tắc: nếu thầy chỉ ra một điểm đúng là yếu thì nhận, nói rõ đã chọn gì và vì sao, không chối. Phần cuối (mục 8) liệt kê thẳng những điểm yếu thật còn lại.

Số liệu hiện hành (đã khớp `tools/chay_het.py`): **20 thực thể** (5 cơ bản, 3 đối tượng ngoài, 12 nghiệp vụ); **5 mối kết hợp có thuộc tính** và **37 mối kết hợp thường**; **25 quan hệ** ban đầu, **26** sau cải tiến; đồ thị **25 nút, 42 cung** (41 cung giữa hai nút khác nhau và 1 khuyên của LOAIHANG), **8 nút vào**, **57 đường truy xuất**; 9 truy vấn khai thác.

---

## 1. Phạm vi và tính thực tế

**1.1. Đề tài có quá lớn không? Một sinh viên làm nổi không?**
Cỡ trung bình: 20 thực thể, hơn báo cáo mẫu ThamKhao 3 thực thể (17), cùng 5 mối kết hợp có thuộc tính. Nhóm đã bỏ 6 quan hệ (giỏ hàng, địa chỉ, nhật ký đơn, vai trò…) vì là dữ liệu tạm hoặc sao chép (QUYET_DINH mục 10), và liệt kê rõ phần ngoài phạm vi ở 1.3. Bù lại làm sâu: đổi trả, bảo hành, số seri, truy trách nhiệm. *Căn cứ: 1.3; Chương 4 mục 4.3.*

**1.2. Vì sao có đặt cọc, đổi trả, bảo hành? Có thật trong cửa hàng không?**
Có. Thời hạn đổi trả 48 giờ / 30 ngày / 7 ngày lấy theo chính sách công khai của GearVN; bảo hành theo Điều 30 Luật 19/2023/QH15 (ngày gửi bảo hành không tính vào thời hạn; thay linh kiện hoặc đổi mới thì tính lại; hết hạn hẹn không sửa được hoặc bảo hành từ ba lần mà lỗi còn thì đổi mới hoặc trả tiền). Chỗ nào chỉ là đề xuất nhóm thì báo cáo ghi "giả thiết của nhóm" (ví dụ mốc 7 ngày khi khách đổi ý, mức khấu hao khi thu hồi). *Căn cứ: 1.4 các đoạn Hồ Sơ Đổi Trả, Phiếu Bảo Hành; file 06 mục 10–11.*

**1.3. Mô tả có vẻ dài, sao không gọn hơn?**
Mục 1.4 dài hơn mẫu khoảng 10%, vì mẫu chỉ có bài tập, lớp học còn nhóm có thêm đổi trả và bảo hành là hai nghiệp vụ nhiều quy tắc nhất của cửa hàng linh kiện. Mỗi đoạn theo cùng một khuôn: định danh, thuộc tính, quan hệ với đối tượng khác, ai quản lý. Không đoạn nào nói về giao diện hay công cụ.

**1.4. Bảo hành "đổi mới" thì chiếc hàng mới ghi ở đâu?**
Nằm ngoài phạm vi, quyết định Q7. Cơ sở dữ liệu chỉ ghi kết quả "đổi mới" trên phiếu bảo hành, không nối chiếc mới và không theo dõi thời hạn riêng của nó. Nếu muốn biểu diễn thì thêm một cột trỏ tới chiếc hàng mới vào PHIEUBAOHANH rồi tính lại phụ thuộc hàm, khóa, dạng chuẩn. Đã nêu ở 1.3 và 4.3.

**1.5. Khấu hao khi thu hồi sản phẩm lấy ở đâu?**
Luật chỉ nói "trả lại tiền". GearVN và HACOM có khấu hao nhưng nhóm chưa tìm được căn cứ pháp lý, nên mức khấu hao là thỏa thuận giữa cửa hàng và khách do người quản lý quyết định (giả thiết, Q3). Đây là điểm nên hỏi lại thầy nếu có dịp.

---

## 2. Ba loại thực thể

**2.1. NHÂN VIÊN nối với 16 mối kết hợp, có quá nhiều không?**
Không sai. Mỗi chứng từ ghi người làm là mẫu truy trách nhiệm quen thuộc; mỗi mối nối trả lời một câu hỏi kiểm soát: ai lập đơn, ai thu tiền, ai giao, ai nhập, ai kiểm, ai duyệt, ai chi hoàn. Hai khâu tiền và kho có thêm người duyệt khác người lập (hoàn tiền: quản lý duyệt, thu ngân chi; nhập kho: kho lập, rồi xác nhận). Về chuẩn hóa không phát sinh phụ thuộc hàm mới vì mỗi cột `MaNV…` chỉ phụ thuộc vào khóa của quan hệ chứa nó. Hình tổng quát gom bớt, hình nhóm 7 (Hình 1.8) vẽ đủ. Tôi cũng thừa nhận đây là nút nhiều cung nhất (12 trên 41 cung giữa hai nút).

**2.2. Vì sao PHIEUGIAO không gộp vào ĐƠN HÀNG? Hai bên 1–1 mà.**
Bản số là (1,1) phía phiếu giao và (0,1) phía đơn: đơn mua tại quầy không có phiếu giao, gộp thì các cột `ThoiDiemXuat`, `TinhTrangGiao`, người giao thành NULL hàng loạt ở đơn tại quầy. Phiếu giao còn là một chứng từ thật (kho bàn giao cho người giao) và có LANGIAO (tối đa 3 lần) gắn vào. Nhận: nếu gộp thì phương án vẫn đúng, chỉ khác ở độ NULL.

**2.3. LANNHANLAI có phải chỉ là thuộc tính của HOSODOITRA?**
Chỉ khi mỗi hồ sơ nhận lại đúng một lần. Nhóm giả thiết một hồ sơ có thể nhận lại nhiều lần (nhận thiếu phụ kiện rồi nhận bổ sung), nên là (1,1)–(0,n). Gộp vào hồ sơ thì thêm 6 cột NULL và đổi quy tắc thành "đúng một lần" (QUYET_DINH mục 10). Đây là giả thiết nghiệp vụ của nhóm.

**2.4. GIAODICHKHO có giống "lịch sử thống kê" thầy từng phê không?**
Nó là sổ kho: mỗi lần hàng vào ra là một sự kiện có thời điểm, và còn ghi **nhóm kho** (đủ điều kiện bán, chờ kiểm tra, chờ xử lý) mà chứng từ gốc không ghi. Số tồn kho tính từ sổ này nên không lưu thành cột (tránh dư thừa). Điểm yếu thật: `LoaiChungTu, MaChungTu` là tham chiếu đa hình, không có khóa ngoại. Chương 4 chưa nêu thẳng điểm này, nên tự biết trước.

**2.5. Dòng chi tiết đơn hàng sao không phải thực thể?**
Giáo trình (13.2.3) và nhận xét của giảng viên: dòng chi tiết là **mối kết hợp** giữa đơn và mặt hàng, có thuộc tính (số lượng, đơn giá chốt). Vẽ oval xanh. Khi lập lược đồ nó vẫn thành một quan hệ riêng (CHITIETDONHANG) với khóa (MaDH, SoDongDH).

**2.6. Mối kết hợp nối với mối kết hợp (HÀNG CÓ SERI – CHI TIẾT ĐƠN HÀNG…) có sai ký hiệu không?**
Đây là mối kết hợp *tổng hợp*: chiếc hàng, phiếu bảo hành, dòng trả thuộc về một **dòng** của đơn chứ không chỉ về cả đơn. Nhóm giữ vì tách ra phải thêm thực thể không có thật. Nếu thầy muốn đúng chuẩn Chen, có thể đổi thành mối kết hợp ba nhánh (đơn, mặt hàng, chiếc hàng), nhưng khi đó lược đồ không đổi.

**2.7. THUONGHIEU chỉ có tên và mô tả, sao không là thuộc tính của MẶT HÀNG?**
Nếu để tên hãng trong MATHANG thì `MaTH → TenTH, MoTaTH` là phụ thuộc giữa các thuộc tính không khóa (vi phạm 3NF), tên hãng lặp ở mọi mặt hàng và sửa phải sửa nhiều chỗ.

**2.8. ANHMATHANG là thuộc tính đa trị, sao thành thực thể?**
Thuộc tính đa trị không đặt được trong một quan hệ đạt 1NF, phải tách; ảnh còn có thuộc tính riêng (vị trí, đường dẫn, là ảnh chính) nên thành thực thể cơ bản. Đây cũng là tình huống 4NF của báo cáo.

**2.9. TAIKHOAN vì sao riêng? Gộp vào KHACHHANG, NHANVIEN được không?**
Gộp thì phải lặp bốn cột đăng nhập ở hai bảng, và khách mua tại quầy không có tài khoản. Tài khoản là đối tượng sinh ra khi đăng ký hoặc được cấp, có `ThoiDiemTaoTK`, nên xếp nghiệp vụ.

**2.10. Tổng tiền, tồn kho, doanh thu để đâu?**
Không lưu: là dữ liệu tính toán. Tổng tiền đơn = tổng dòng hàng − giảm giá + phí giao; tồn kho tính từ GIAODICHKHO. Lưu sẵn sẽ tạo phụ thuộc hàm thừa và dị thường cập nhật.

**2.11. Khoản hoàn lấy nguồn từ đâu?**
Mọi khoản hoàn gắn với khoản thu gốc. Do đổi trả thì có `MaHS`, do bảo hành thu hồi sản phẩm thì có `MaPhieuBH`, không có cả hai là hoàn do hủy đơn. Một khoản không được có cả `MaHS` lẫn `MaPhieuBH` (CHECK). *Căn cứ: 2.2.25, ràng buộc 4 ở 2.3.6.*

---

## 3. Phụ thuộc hàm và khóa

**3.1. Phụ thuộc hàm lấy từ đâu? Từ dữ liệu mẫu à?**
Từ tân từ và quy tắc nghiệp vụ, **không** từ dữ liệu mẫu (dữ liệu chỉ bác bỏ được một PTH, không chứng minh được). Mỗi PTH ghi căn cứ; những chỗ nhóm tự đặt là giả thiết G1–G6 (2.2.1).

**3.2. Mọi bảng có khóa `Id` thì mặc nhiên BCNF, đúng không?**
Không. Phải xét **mọi khóa ứng viên**. Kết quả của nhóm: ban đầu 20 quan hệ BCNF, 1 ở 3NF (HANGCOSERI), 1 ở 2NF (PHIEUBAOHANH), 1 ở 1NF (CHITIETTRA), 2 chưa đạt 1NF (KHACHHANG, NHANVIEN: họ tên). Hai quan hệ sau (CHITIETTRA, PHIEUBAOHANH) vi phạm vì cột nhắc lại thông tin đã suy ra được (MaDH, MaSP).

**3.3. Giá trên đơn có phải phụ thuộc vào mặt hàng không (MaSP → DonGiaChot)?**
Không. `DonGiaChot` là giá chốt lúc bán (snapshot), một mặt hàng có thể có nhiều dòng giá khác nhau (giá khuyến mãi, giá thường), nên báo cáo không đặt phụ thuộc đó; khóa của CHITIETDONHANG là (MaDH, SoDongDH).

**3.4. TAIKHOAN có bốn khóa, nhưng MaKH, MaNV có thể NULL — có là khóa không?**
Chỉ là khóa trên những tài khoản mà cột đó khác rỗng. Báo cáo nói rõ ở giả thiết G4: PTH có vế trái chứa cột cho phép rỗng chỉ xét trên những bộ cột đó khác rỗng. Cài đặt: UNIQUE có điều kiện và ràng buộc "đúng một trong MaKH, MaNV".

**3.5. Phủ tối thiểu có duy nhất không?**
Không; thứ tự xét cho ra các phủ khác nhau nhưng tương đương. Báo cáo trình bày một phủ, nêu thứ tự (xét từ PTH cuối lên đầu để giữ các PTH của khóa chính) và kiểm tra G ≡ F bằng bao đóng.

**3.6. Vì sao số seri chỉ duy nhất theo mặt hàng, không duy nhất toàn cửa hàng (G1)?**
Số seri do từng hãng tự đánh, hai hãng có thể trùng. Chọn "duy nhất theo mặt hàng" là phương án an toàn hơn; hệ quả là (SoSeri, MaSP) mới là khóa. Nếu cửa hàng xác nhận "duy nhất toàn cửa hàng" thì phụ thuộc đổi và phải tính lại (đã nêu ở 4.4).

**3.7. Vì sao CHITIETTRA có khóa (MaHS, SoDongTra) mà không phải (MaHS, SoDongDH)?**
Một dòng đơn có thể gồm hai chiếc có seri. Nếu khóa là (MaHS, SoDongDH) thì PTH `MaHS,SoDongDH → MaSeri` sai về nghiệp vụ, vì khách trả cả hai chiếc thì chỉ ghi được một. Nên mỗi chiếc một dòng trả, có số thứ tự riêng. Khóa thứ hai (MaHS, MaSeri) chỉ xét trên dòng có seri (giả thiết G4). *Căn cứ: 2.2.23, 2.3.3.*

**3.8. Sao đã có ThoiHanBH ở MATHANG còn thêm ThoiHanBHChot ở dòng đơn?**
Cùng lý do với DonGiaChot: `ThoiHanBH` là chính sách hiện tại của mặt hàng, `ThoiHanBHChot` là thời hạn đã cam kết với khách lúc bán. Đổi chính sách về sau không được làm đổi thời hạn của đơn cũ. Không có `MaSP → ThoiHanBHChot`. *Căn cứ: 2.2.14, đoạn Phiếu Bảo Hành ở 1.4.*

---

## 4. Dạng chuẩn, phân rã, bảo toàn

**4.1. Vì sao dùng thuật toán phân rã (Delobel) mà không phải tổng hợp (Bernstein)?**
Ba quan hệ cần sửa đều có một PTH "gây xấu" rõ (vế trái không chứa khóa), tách theo đó cho kết quả BCNF, bảo toàn thông tin. Báo cáo trình bày cả hai cách ở từng quan hệ (Cách 1 phân rã, Cách 2 tổng hợp) rồi mới chọn lược đồ cuối. Phân rã có thể mất PTH nên phải chứng minh F' ≡ F; việc này đã làm ở 2.3.3–2.3.5.

**4.2. HANGCOSERI đang 3NF mà không BCNF là sao?**
Khóa gồm {MaSeri}, {SoSeri, MaSP}… nên `MaSP` là thuộc tính khóa, đủ để qua 3NF. Nhưng (MaPN, SoDongPN) → MaSP và (MaDH, SoDongDH) → MaSP có vế trái không chứa khóa nên không đạt BCNF. Cách sửa của nhóm là phương án C: thêm quan hệ SERIMATHANG(MaSeri, SoSeri, MaSP) giữ ràng buộc "seri duy nhất trong cùng mặt hàng", và bỏ SoSeri, MaSP khỏi HANGCOSERI (2.3.5, 2.3.6).

**4.3. Chứng minh bảo toàn thông tin thế nào?**
Bảng a/b (tableau): cột là thuộc tính của Q, dòng là các Qᵢ, áp các PTH để đồng nhất ký hiệu; có một dòng toàn a là bảo toàn. Với phép tách hai thành phần có thể dùng thêm định lý Rissanen: (Q₁ ∩ Q₂) → (Q₁ \ Q₂) hoặc (Q₁ ∩ Q₂) → (Q₂ \ Q₁). Lưu ý: slide 3 của Bài 7 Bổ sung viết `R₂ ∪ R₁ → R₂ \ R₁`, đó là chỗ in sai; dạng đúng là giao, không phải hợp. Báo cáo dùng bảng a/b chứ không dựa vào slide này.

**4.4. Tách họ tên có đúng là vi phạm 1NF không? Tên Việt đâu có chuẩn.**
Theo phép thử của bài giảng: nếu phải dùng một **phần** của giá trị (`LIKE '%Mỹ'`) thì thuộc tính chưa nguyên tố. Cửa hàng tìm khách theo tên (G3) nên tách thành HoLot và Ten. Giới hạn: tên có nhiều từ phụ thuộc quy ước nhập, không kiểm bằng phụ thuộc hàm (đã nêu ở 4.3).

---

## 5. Phụ thuộc đa trị và 4NF

**5.1. Vì sao ảnh và thông số độc lập?**
Theo nghiệp vụ: thêm hoặc đổi ảnh không làm đổi thông số, và ngược lại. Nên quan hệ lưu chung phải chứa mọi cặp (ảnh, thông số) của mặt hàng, tức MaSP ↠ DuongDanAnh. Nhiều dòng trong dữ liệu **không phải** bằng chứng; bằng chứng là tính độc lập theo nghiệp vụ.

**5.2. Có phải cố tạo 4NF cho có không?**
R₂(MaSP, DuongDanAnh, MaTS) toàn khóa nên BCNF, nhưng vi phạm 4NF. Số liệu seed: 3.256 dòng nếu lưu chung so với 1.538 dòng nếu tách (gấp khoảng 2,1 lần), và thêm một ảnh thì buộc thêm 3 dòng thay vì 1. Kết luận 4NF cho các quan hệ còn lại dựa trên mô tả nghiệp vụ, **chưa chứng minh tổng quát** (4.3).

---

## 6. Đồ thị quan hệ và đường truy xuất (phần thầy xem trước)

**6.1. Nút vào là gì? Vì sao chọn 9 nút này?**
Nút vào là nút mà người dùng cung cấp khóa để truy xuất. Để liệt kê nhiều đường nhất, báo cáo chọn nút **không có cung vào** (ANHMATHANG, GIATRITHONGSO, TAIKHOAN, LANGIAO, GIAODICHKHO, CHITIETTRA, LANNHANLAI, KHOANHOAN). PHIEUBAOHANH không còn là nút vào vì KHOANHOAN trỏ tới nó. Từ nút khác chỉ đến các nút này bằng cách đi ngược cung (cho nhiều bộ).

**6.2. Nút bản lề có không?**
Không. Có 64 cặp quan hệ có giao khác rỗng; với mỗi cặp, khóa của giao đều trùng khóa của một quan hệ sẵn có (bảng 3.1) nên không tạo nút bản lề, B5 (hủy nút bản lề thừa) không thực hiện.

**6.3. Cung vô hướng (B7) có không?**
Không. B7 chỉ áp dụng cho quan hệ chỉ gồm thuộc tính khóa, có đúng hai cung ra và không có cung vào. Các quan hệ nối n–n của lược đồ đều có thuộc tính riêng (GIATRITHONGSO có GiaTriTS; CHITIET… có số lượng, giá).

**6.4. Vì sao đồ thị giữ nhiều cung tới NHÂN VIÊN? Thuật toán bảo bỏ cung thừa mà.**
Quy ước Q2 của mục 3.1: các cột `MaNV` ở các quan hệ là vai trò khác nhau của cùng một người (lập đơn, thu tiền, giao, nhập…), nên mỗi cung vai trò được giữ riêng chứ không coi là thừa theo Q3. Cột phụ như `MaNVThu`, `MaNVXacNhan`, `MaNVDuyet`, `MaNVChi` ghi thêm một vai trò của nhân viên trên cùng quan hệ. Đây là một quy ước, giáo trình cho phép nhiều đồ thị cho cùng một lược đồ (mục 10.4); các cung này vẽ màu xám trên Hình 3.1.

**6.5. Khuyên của LOAIHANG thì sao?**
Khuyên LOAIHANG → LOAIHANG (loại cha – con) nằm ngoài thuật toán (Q4); vì vậy 42 cung gồm 41 cung giữa hai nút và 1 khuyên. Đây là chỗ nhóm có thể được hỏi "có đưa vào đường truy xuất không"; câu trả lời: không, vì thuật toán không có khuyên và truy hồi cây loại hàng là truy vấn đệ quy khác.

**6.6. Đồ thị có giao cắt, sao không vẽ phẳng?**
Đồ thị **không phẳng** (đã kiểm bằng thuật toán kiểm tra tính phẳng) nên khi mọi cung là đường thẳng vẫn có chỗ hai cung cắt nhau. Nhóm xếp nút để còn 14 chỗ cắt, không cung nào xuyên qua nút. 14 là số tìm được, **chưa chứng minh là nhỏ nhất**. Chỗ cắt của hai cung không phải là nút.

**6.7. 57 đường truy xuất được liệt kê thế nào? Có kiểm không?**
Từ mỗi nút vào đi theo chiều cung đến khi hết cung; đã tính lại bằng chương trình độc lập, khớp 57 đường. Mỗi đường có một câu SQL, đã chạy trên dữ liệu minh họa: mọi đường đều trả về ít nhất một dòng.

**6.8. Hai mạch tới cùng một nút (PHIEUBAOHANH → CHITIETDONHANG) nghĩa là gì?**
Là ràng buộc nhất quán: chiếc hàng đem bảo hành phải thuộc đúng dòng đơn đã mua; tương tự KHOANHOAN → DONHANG qua THANHTOAN, qua HOSODOITRA và qua PHIEUBAOHANH phải cùng một đơn. Đây là ràng buộc 2 và 4 ở 2.3.6, cài bằng khóa ngoại ghép hoặc trigger.

---

## 7. SQL

**7.1. Sao truy vấn chỉ chọn khóa chính, không chọn đầy đủ cột?**
Truy vấn của đường truy xuất chỉ cần chỉ ra **bộ chứng từ** nào nối với nhau (khóa chính của từng quan hệ trên đường). Muốn xem thông tin thì thêm cột; 9 truy vấn khai thác (K1–K9) chọn cột cụ thể và có tổng hợp, truy trách nhiệm theo nhân viên và chức vụ.

**7.2. Có đo hiệu năng chưa?**
Chưa. Dữ liệu minh họa chỉ vài chục dòng, đủ để kiểm truy vấn chạy đúng, không đủ để đánh giá hiệu năng. Mục 3.4 mới nêu chỉ mục đề xuất (cột khóa ngoại và các ngõ vào tra cứu).

**7.3. Dữ liệu minh họa có đại diện không?**
Không đại diện. Đó là dữ liệu tự tạo (`sql/02`), dùng để kiểm truy vấn và ràng buộc khóa ngoại. Số liệu 4NF (3.256 và 1.538 dòng) lấy từ seed của PowerTech đã ẩn thông tin cá nhân.

---

## 8. Điểm yếu thật còn lại (nên tự biết trước)

1. **Nhiều phụ thuộc hàm là giả thiết nhóm** (G1–G6), chưa kiểm với một cửa hàng thật.
2. **GIAODICHKHO** dùng tham chiếu đa hình không có khóa ngoại; số tồn kho phụ thuộc quy ước dấu chưa chốt.
3. **LANNHANLAI (0,n)** và **PHIEUGIAO 1–1 với ĐƠN HÀNG** là hai chỗ nhóm chọn có chủ ý; thầy có thể bảo gộp.
4. **Mối kết hợp nối mối kết hợp** trong ERD: không có trong ký hiệu Chen chuẩn.
5. **Đồ thị có 14 giao cắt**; Hình 3.2 (có tên nút) khi in còn chữ khoảng 5,9 pt, nhỏ hơn mức 7 pt; nên dùng Hình 3.1 và Bảng 3.2 khi trình bày.
6. **Chưa đo hiệu năng**, và chưa mở bản Word để xem từng trang.
7. Báo cáo chưa kèm mô hình quyền hạn chi tiết; quy tắc "đúng chức vụ mới được làm khâu đó" chỉ cưỡng chế được khi ghi dữ liệu.
