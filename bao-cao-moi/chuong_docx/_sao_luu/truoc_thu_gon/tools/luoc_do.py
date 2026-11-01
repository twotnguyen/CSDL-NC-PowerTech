"""Nguồn dữ liệu duy nhất của báo cáo: lược đồ ban đầu (31 quan hệ) và các thay đổi khi cải tiến (thêm SERIMATHANG, 32 quan hệ).

Mọi file sinh ra (chương 2, chương 3, hình, SQL) đều đọc từ đây để các con số khớp nhau.
Quy ước đặt tên: thuộc tính không khóa có hậu tố phân biệt giữa các quan hệ (HoTenKH, HoTenNV...),
khóa ngoại dùng cùng tên với khóa chính của quan hệ cha (MaKH, MaSP...).
Mỗi thuộc tính: (tên, kiểu, ghi chú, ý nghĩa); ghi chú 'NN' = NOT NULL, 'NULL' = cho phép rỗng.
"""

LOAI = {'co_ban': 'Cơ bản', 'ngoai': 'Đối tượng ngoài', 'nghiep_vu': 'Nghiệp vụ', 'mkh': 'Mối kết hợp'}

# ----------------------------------------------------------------------------------------------
# Lược đồ ban đầu (kết quả chuyển ERD sang mô hình quan hệ, chưa tối ưu)
# ----------------------------------------------------------------------------------------------
REL = {}


def rel(name, loai, ten, attrs, pk, F, tantu, rangbuoc, fks=(), uniques=()):
    REL[name] = dict(loai=loai, ten=ten, attrs=attrs, pk=list(pk), F=list(F), tantu=tantu, rangbuoc=rangbuoc,
                     fks=[(tuple(c), p, tuple(pc)) for c, p, pc in fks], uniques=[tuple(u) for u in uniques])


rel('LOAIHANG', 'co_ban', 'Loại hàng',
    [('MaLoai', 'INT', 'NN', 'Mã loại hàng'), ('TenLoai', 'NVARCHAR(100)', 'NN', 'Tên loại hàng'),
     ('MoTaLoai', 'NVARCHAR(500)', 'NULL', 'Mô tả loại hàng'), ('MaLoaiCha', 'INT', 'NULL', 'Mã loại hàng cha')],
    ['MaLoai'], ['MaLoai -> TenLoai,MoTaLoai,MaLoaiCha'],
    'Mỗi loại hàng được phân biệt bằng mã loại hàng (MaLoai), có tên (TenLoai) và mô tả (MoTaLoai). Các loại hàng '
    'phân cấp: một loại có tối đa một loại cha (MaLoaiCha), ví dụ nhóm "Linh kiện máy tính" gồm "Bộ nhớ RAM". '
    'Tên không dùng để phân biệt vì hai loại hàng có thể trùng tên.',
    'MaLoai là số tự nhiên tăng dần. TenLoai không rỗng, tối đa 100 ký tự. MaLoaiCha rỗng với loại hàng ở cấp cao nhất '
    'và khác MaLoai của chính nó.',
    fks=[(['MaLoaiCha'], 'LOAIHANG', ['MaLoai'])])

rel('THUONGHIEU', 'co_ban', 'Thương hiệu',
    [('MaTH', 'INT', 'NN', 'Mã thương hiệu'), ('TenTH', 'NVARCHAR(100)', 'NN', 'Tên thương hiệu'),
     ('MoTaTH', 'NVARCHAR(500)', 'NULL', 'Mô tả thương hiệu')],
    ['MaTH'], ['MaTH -> TenTH,MoTaTH'],
    'Mỗi thương hiệu được phân biệt bằng mã thương hiệu (MaTH), có tên (TenTH) và mô tả (MoTaTH). Hai thương hiệu có '
    'thể trùng tên nên tên không dùng để phân biệt.',
    'MaTH là số tự nhiên tăng dần. TenTH không rỗng, tối đa 100 ký tự.')

rel('MATHANG', 'co_ban', 'Mặt hàng',
    [('MaSP', 'INT', 'NN', 'Mã mặt hàng (nội bộ)'), ('SKU', 'VARCHAR(50)', 'NN', 'Mã hàng thương mại'),
     ('TenSP', 'NVARCHAR(200)', 'NN', 'Tên mặt hàng'), ('MoTaSP', 'NVARCHAR(2000)', 'NULL', 'Mô tả'),
     ('GiaNiemYet', 'DECIMAL(15,0)', 'NN', 'Giá niêm yết (đồng)'),
     ('GiaKhuyenMai', 'DECIMAL(15,0)', 'NULL', 'Giá khuyến mãi đang áp dụng'),
     ('ThoiHanBH', 'INT', 'NN', 'Thời hạn bảo hành (tháng, 0 nếu không bảo hành)'),
     ('TinhTrangKD', 'NVARCHAR(20)', 'NN', 'Đang kinh doanh hoặc đã ngừng'),
     ('CoSeri', 'BIT', 'NN', 'Có theo dõi số seri từng chiếc'),
     ('MaLoai', 'INT', 'NN', 'Loại hàng'), ('MaTH', 'INT', 'NN', 'Thương hiệu')],
    ['MaSP'], ['MaSP -> SKU,TenSP,MoTaSP,GiaNiemYet,GiaKhuyenMai,ThoiHanBH,TinhTrangKD,CoSeri,MaLoai,MaTH',
               'SKU -> MaSP,TenSP,MoTaSP,GiaNiemYet,GiaKhuyenMai,ThoiHanBH,TinhTrangKD,CoSeri,MaLoai,MaTH'],
    'Mỗi mặt hàng có mã nội bộ (MaSP) và mã hàng thương mại (SKU) đều không trùng với mặt hàng nào khác. Thông tin '
    'gồm tên, mô tả, giá niêm yết, giá khuyến mãi (nếu có), thời hạn bảo hành theo tháng, tình trạng kinh doanh và '
    'cờ CoSeri cho biết mặt hàng có ghi số seri từng chiếc hay không. Mỗi mặt hàng thuộc đúng một loại (MaLoai) và một '
    'thương hiệu (MaTH).',
    'MaSP là số tự nhiên tăng dần. SKU không rỗng, không trùng. GiaNiemYet lớn hơn 0; GiaKhuyenMai nếu có phải nhỏ hơn '
    'hoặc bằng GiaNiemYet. ThoiHanBH từ 0 đến 120. TinhTrangKD chỉ nhận "Đang kinh doanh" hoặc "Ngừng kinh doanh".',
    fks=[(['MaLoai'], 'LOAIHANG', ['MaLoai']), (['MaTH'], 'THUONGHIEU', ['MaTH'])], uniques=[('SKU',)])

rel('ANHMATHANG', 'co_ban', 'Ảnh mặt hàng',
    [('MaAnh', 'INT', 'NN', 'Mã ảnh'), ('MaSP', 'INT', 'NN', 'Mặt hàng'),
     ('ViTriAnh', 'INT', 'NN', 'Vị trí ảnh trong mặt hàng'), ('DuongDanAnh', 'VARCHAR(500)', 'NN', 'Đường dẫn tệp ảnh'),
     ('LaAnhChinh', 'BIT', 'NN', 'Là ảnh đại diện')],
    ['MaAnh'], ['MaAnh -> MaSP,ViTriAnh,DuongDanAnh,LaAnhChinh',
                'MaSP,ViTriAnh -> MaAnh,DuongDanAnh,LaAnhChinh'],
    'Mỗi mặt hàng có nhiều ảnh minh họa. Mỗi ảnh có mã (MaAnh), thuộc một mặt hàng (MaSP), có vị trí (ViTriAnh) trong '
    'mặt hàng đó, đường dẫn tệp (DuongDanAnh) và cờ ảnh đại diện (LaAnhChinh). Vị trí ảnh trong cùng một mặt hàng '
    'không trùng nhau.',
    'MaAnh là số tự nhiên tăng dần. ViTriAnh bắt đầu từ 1. (MaSP, ViTriAnh) không trùng. Mỗi mặt hàng có tối đa một ảnh '
    'có LaAnhChinh = 1.',
    fks=[(['MaSP'], 'MATHANG', ['MaSP'])], uniques=[('MaSP', 'ViTriAnh')])

rel('DINHNGHIATHONGSO', 'co_ban', 'Định nghĩa thông số',
    [('MaTS', 'INT', 'NN', 'Mã thông số'), ('MaLoai', 'INT', 'NN', 'Loại hàng quy định thông số này'),
     ('TenTS', 'NVARCHAR(100)', 'NN', 'Tên thông số'), ('KieuGiaTri', 'NVARCHAR(10)', 'NN', 'Chữ, số hoặc có/không'),
     ('DonViTS', 'NVARCHAR(20)', 'NULL', 'Đơn vị (GB, MHz, W...)'), ('BatBuoc', 'BIT', 'NN', 'Thông số bắt buộc nhập')],
    ['MaTS'], ['MaTS -> MaLoai,TenTS,KieuGiaTri,DonViTS,BatBuoc'],
    'Mỗi loại hàng quy định các thông số riêng của mình. Mỗi thông số có mã (MaTS), thuộc một loại hàng (MaLoai), có '
    'tên (TenTS), kiểu giá trị (KieuGiaTri), đơn vị (DonViTS) nếu có và cho biết có bắt buộc nhập hay không.',
    'MaTS là số tự nhiên tăng dần. KieuGiaTri chỉ nhận "Chữ", "Số" hoặc "Có/Không". TenTS không rỗng.',
    fks=[(['MaLoai'], 'LOAIHANG', ['MaLoai'])])

rel('GIATRITHONGSO', 'mkh', 'Giá trị thông số của mặt hàng',
    [('MaSP', 'INT', 'NN', 'Mặt hàng'), ('MaTS', 'INT', 'NN', 'Thông số'),
     ('GiaTriTS', 'NVARCHAR(200)', 'NN', 'Giá trị của thông số')],
    ['MaSP', 'MaTS'], ['MaSP,MaTS -> GiaTriTS'],
    'Giá trị thông số cho biết mặt hàng (MaSP) có giá trị (GiaTriTS) nào ở thông số (MaTS). Mỗi mặt hàng có tối đa một '
    'giá trị cho một thông số.',
    'GiaTriTS không rỗng. Thông số (MaTS) phải thuộc loại hàng của mặt hàng (MaSP); đây là ràng buộc liên quan hệ '
    'không biểu diễn được bằng PTH.',
    fks=[(['MaSP'], 'MATHANG', ['MaSP']), (['MaTS'], 'DINHNGHIATHONGSO', ['MaTS'])])

rel('KHACHHANG', 'ngoai', 'Khách hàng',
    [('MaKH', 'INT', 'NN', 'Mã khách hàng'), ('HoTenKH', 'NVARCHAR(100)', 'NN', 'Họ và tên khách hàng'),
     ('SDTKH', 'VARCHAR(15)', 'NN', 'Số điện thoại'), ('EmailKH', 'VARCHAR(100)', 'NULL', 'Địa chỉ email'),
     ('MaSoThueKH', 'VARCHAR(14)', 'NULL', 'Mã số thuế (khách là doanh nghiệp)')],
    ['MaKH'], ['MaKH -> HoTenKH,SDTKH,EmailKH,MaSoThueKH'],
    'Mỗi khách hàng được phân biệt bằng mã khách hàng (MaKH), có họ tên (HoTenKH), số điện thoại (SDTKH), email '
    '(EmailKH) nếu có và mã số thuế (MaSoThueKH) nếu là doanh nghiệp cần hóa đơn. Họ tên, số điện thoại hay email có thể '
    'trùng hoặc thay đổi nên không dùng để phân biệt hai khách.',
    'MaKH là số tự nhiên tăng dần. HoTenKH không rỗng, tối đa 100 ký tự. SDTKH gồm 10 chữ số. EmailKH nếu có phải có ký tự '
    '"@". Khách mua tại quầy không để lại thông tin thì không có hồ sơ khách hàng.')

rel('DIACHIKHACH', 'ngoai', 'Địa chỉ giao hàng của khách',
    [('MaDC', 'INT', 'NN', 'Mã địa chỉ'), ('MaKH', 'INT', 'NN', 'Khách hàng'),
     ('TenNguoiNhanDC', 'NVARCHAR(100)', 'NN', 'Tên người nhận'), ('SDTNhanDC', 'VARCHAR(15)', 'NN', 'Số điện thoại người nhận'),
     ('DiaChiChiTiet', 'NVARCHAR(300)', 'NN', 'Địa chỉ chi tiết'), ('LaMacDinh', 'BIT', 'NN', 'Là địa chỉ mặc định')],
    ['MaDC'], ['MaDC -> MaKH,TenNguoiNhanDC,SDTNhanDC,DiaChiChiTiet,LaMacDinh'],
    'Khách có tài khoản lưu được nhiều địa chỉ nhận hàng. Mỗi địa chỉ có mã (MaDC), thuộc một khách hàng (MaKH), ghi tên '
    'người nhận, số điện thoại người nhận, địa chỉ chi tiết và cho biết có phải địa chỉ mặc định hay không (LaMacDinh).',
    'MaDC là số tự nhiên tăng dần. Mỗi khách có tối đa một địa chỉ có LaMacDinh = 1 (ràng buộc có điều kiện, không phải '
    'khóa). Đơn hàng chép địa chỉ vào đơn lúc chốt nên đổi hoặc xóa địa chỉ không sửa đơn cũ.',
    fks=[(['MaKH'], 'KHACHHANG', ['MaKH'])])

rel('NHANVIEN', 'ngoai', 'Nhân viên',
    [('MaNV', 'INT', 'NN', 'Mã nhân viên'), ('HoTenNV', 'NVARCHAR(100)', 'NN', 'Họ và tên nhân viên'),
     ('SDTNV', 'VARCHAR(15)', 'NN', 'Số điện thoại'), ('EmailNV', 'VARCHAR(100)', 'NULL', 'Địa chỉ email'),
     ('NgayVaoLam', 'DATE', 'NN', 'Ngày vào làm'), ('NgayNghiViec', 'DATE', 'NULL', 'Ngày nghỉ việc (rỗng nếu còn làm)'),
     ('TinhTrangNV', 'NVARCHAR(20)', 'NN', 'Đang làm hoặc đã nghỉ')],
    ['MaNV'], ['MaNV -> HoTenNV,SDTNV,EmailNV,NgayVaoLam,NgayNghiViec,TinhTrangNV'],
    'Mỗi nhân viên được phân biệt bằng mã nhân viên (MaNV), có họ tên (HoTenNV), số điện thoại (SDTNV), email (EmailNV) nếu '
    'có, ngày vào làm (NgayVaoLam), ngày nghỉ việc (NgayNghiViec) nếu đã nghỉ và tình trạng làm việc (TinhTrangNV). Nhân viên '
    'nghỉ việc vẫn giữ hồ sơ để tra cứu các chứng từ người đó đã lập hoặc duyệt. Cửa hàng nhỏ nên một nhân viên thường kiêm '
    'nhiều việc, vì vậy quan hệ không ghi chức vụ cố định; vai trò ghi ở GIUVAITRO.',
    'MaNV là số tự nhiên tăng dần. HoTenNV không rỗng. TinhTrangNV chỉ nhận "Đang làm" hoặc "Đã nghỉ". NgayNghiViec không '
    'trước NgayVaoLam và chỉ có giá trị khi TinhTrangNV là "Đã nghỉ". Không xóa hồ sơ nhân viên đã có chứng từ.')

rel('VAITRO', 'co_ban', 'Vai trò công việc',
    [('MaVT', 'INT', 'NN', 'Mã vai trò'), ('TenVT', 'NVARCHAR(50)', 'NN', 'Tên vai trò'),
     ('MoTaVT', 'NVARCHAR(300)', 'NULL', 'Mô tả công việc và quyền hạn')],
    ['MaVT'], ['MaVT -> TenVT,MoTaVT', 'TenVT -> MaVT,MoTaVT'],
    'Mỗi vai trò công việc có mã (MaVT), tên (TenVT) và mô tả công việc, quyền hạn (MoTaVT). Tên vai trò là tên chuẩn của '
    'cửa hàng nên không trùng nhau (giả thiết G5). Cửa hàng có các vai trò: Quản trị, Quản lý, Bán hàng, Thu ngân, Kỹ thuật, '
    'Kho, Giao hàng, Chăm sóc khách hàng.',
    'MaVT là số tự nhiên tăng dần. TenVT không rỗng, không trùng.', uniques=[('TenVT',)])

rel('GIUVAITRO', 'mkh', 'Nhân viên giữ vai trò',
    [('MaNV', 'INT', 'NN', 'Nhân viên'), ('MaVT', 'INT', 'NN', 'Vai trò'),
     ('NgayBatDauVT', 'DATE', 'NN', 'Ngày bắt đầu giữ vai trò'),
     ('NgayKetThucVT', 'DATE', 'NULL', 'Ngày thôi giữ vai trò (rỗng nếu còn giữ)'),
     ('MaNVPhanCong', 'INT', 'NN', 'Người quản trị đã phân vai trò')],
    ['MaNV', 'MaVT', 'NgayBatDauVT'], ['MaNV,MaVT,NgayBatDauVT -> NgayKetThucVT,MaNVPhanCong'],
    'Mỗi lần một nhân viên (MaNV) giữ một vai trò (MaVT) được phân biệt bằng nhân viên, vai trò và ngày bắt đầu '
    '(NgayBatDauVT), ghi ngày thôi giữ (NgayKetThucVT, rỗng nếu còn giữ) và người quản trị đã phân vai trò (MaNVPhanCong). Một '
    'nhân viên có thể giữ nhiều vai trò cùng lúc và có thể giữ lại một vai trò vào lúc khác, vì vậy ngày bắt đầu nằm trong khóa.',
    'NgayKetThucVT nếu có không trước NgayBatDauVT. Hai khoảng thời gian của cùng một cặp (MaNV, MaVT) không chồng nhau. '
    'MaNVPhanCong phải là nhân viên đang giữ vai trò Quản trị vào NgayBatDauVT; hai ràng buộc này liên bộ, không biểu diễn được bằng PTH.',
    fks=[(['MaNV'], 'NHANVIEN', ['MaNV']), (['MaVT'], 'VAITRO', ['MaVT']), (['MaNVPhanCong'], 'NHANVIEN', ['MaNV'])])

rel('TAIKHOAN', 'nghiep_vu', 'Tài khoản đăng nhập',
    [('MaTK', 'INT', 'NN', 'Mã tài khoản'), ('TenDangNhap', 'VARCHAR(50)', 'NN', 'Tên đăng nhập'),
     ('MatKhauBam', 'VARCHAR(255)', 'NN', 'Mật khẩu đã băm (không lưu mật khẩu gốc)'),
     ('TinhTrangTK', 'NVARCHAR(20)', 'NN', 'Hoạt động hoặc bị khóa'),
     ('ThoiDiemTaoTK', 'DATETIME', 'NN', 'Thời điểm tạo tài khoản'),
     ('MaKH', 'INT', 'NULL', 'Khách hàng sở hữu tài khoản (rỗng nếu là tài khoản nhân viên)'),
     ('MaNV', 'INT', 'NULL', 'Nhân viên sở hữu tài khoản (rỗng nếu là tài khoản khách)')],
    ['MaTK'], ['MaTK -> TenDangNhap,MatKhauBam,TinhTrangTK,ThoiDiemTaoTK,MaKH,MaNV',
               'TenDangNhap -> MaTK,MatKhauBam,TinhTrangTK,ThoiDiemTaoTK,MaKH,MaNV',
               'MaKH -> MaTK,TenDangNhap,MatKhauBam,TinhTrangTK,ThoiDiemTaoTK,MaNV',
               'MaNV -> MaTK,TenDangNhap,MatKhauBam,TinhTrangTK,ThoiDiemTaoTK,MaKH'],
    'Khách đặt hàng trên trang web và nhân viên thao tác trên hệ thống đều có tài khoản. Mỗi tài khoản có mã (MaTK) và tên đăng '
    'nhập (TenDangNhap) không trùng, lưu mật khẩu đã băm, tình trạng (khóa khi vi phạm hoặc nghi lộ mật khẩu) và thời điểm tạo. '
    'Tài khoản thuộc đúng một khách hàng (MaKH) hoặc đúng một nhân viên (MaNV); mỗi khách và mỗi nhân viên có tối đa một tài khoản. '
    'Nhân viên không có vai trò riêng ở đây: quyền hạn lấy từ các vai trò nhân viên đang giữ ở GIUVAITRO.',
    'MaTK là số tự nhiên tăng dần. TenDangNhap không rỗng, không trùng. TinhTrangTK chỉ nhận "Hoạt động" hoặc "Bị khóa". '
    'Đúng một trong hai cột MaKH, MaNV có giá trị. Các PTH có vế trái MaKH hoặc MaNV chỉ xét trên những tài khoản có giá trị đó '
    '(giả thiết G4). Chỉ tài khoản khách mới có giỏ hàng.',
    fks=[(['MaKH'], 'KHACHHANG', ['MaKH']), (['MaNV'], 'NHANVIEN', ['MaNV'])],
    uniques=[('TenDangNhap',), ('MaKH',), ('MaNV',)])

rel('NHACUNGCAP', 'ngoai', 'Nhà cung cấp',
    [('MaNCC', 'INT', 'NN', 'Mã nhà cung cấp'), ('TenNCC', 'NVARCHAR(200)', 'NN', 'Tên công ty'),
     ('NguoiLienHeNCC', 'NVARCHAR(100)', 'NULL', 'Người liên hệ'), ('SDTNCC', 'VARCHAR(15)', 'NULL', 'Số điện thoại'),
     ('DiaChiNCC', 'NVARCHAR(300)', 'NULL', 'Địa chỉ'), ('MaSoThueNCC', 'VARCHAR(14)', 'NULL', 'Mã số thuế'),
     ('TinhTrangHT', 'NVARCHAR(20)', 'NN', 'Tình trạng hợp tác')],
    ['MaNCC'], ['MaNCC -> TenNCC,NguoiLienHeNCC,SDTNCC,DiaChiNCC,MaSoThueNCC,TinhTrangHT'],
    'Mỗi nhà cung cấp (nhà phân phối, đại lý chính hãng) được phân biệt bằng mã nhà cung cấp (MaNCC), có tên công ty, '
    'người liên hệ, số điện thoại, địa chỉ, mã số thuế và tình trạng hợp tác. Tên công ty và thông tin liên hệ có thể '
    'trùng nên không dùng để phân biệt.',
    'MaNCC là số tự nhiên tăng dần. TenNCC không rỗng. TinhTrangHT chỉ nhận "Đang hợp tác" hoặc "Ngừng hợp tác".')

rel('GIOHANG', 'nghiep_vu', 'Giỏ hàng',
    [('MaGio', 'INT', 'NN', 'Mã giỏ hàng'), ('MaTK', 'INT', 'NN', 'Tài khoản khách sở hữu giỏ'),
     ('ThoiDiemTaoGio', 'DATETIME', 'NN', 'Thời điểm tạo giỏ'),
     ('ThoiDiemCapNhatGio', 'DATETIME', 'NULL', 'Lần cập nhật gần nhất'),
     ('TinhTrangGio', 'NVARCHAR(15)', 'NN', 'Đang dùng, đã đặt hàng hoặc bỏ')],
    ['MaGio'], ['MaGio -> MaTK,ThoiDiemTaoGio,ThoiDiemCapNhatGio,TinhTrangGio'],
    'Khách đăng nhập trên trang web chọn hàng vào giỏ trước khi gửi đơn. Mỗi giỏ có mã (MaGio), thuộc một tài khoản khách (MaTK), '
    'ghi thời điểm tạo, lần cập nhật gần nhất và tình trạng (đang dùng, đã đặt hàng hoặc bỏ). Khách có thể có nhiều giỏ theo thời gian '
    'nhưng mỗi tài khoản có tối đa một giỏ đang dùng.',
    'TinhTrangGio chỉ nhận "Đang dùng", "Đã đặt hàng" hoặc "Bỏ". Mỗi tài khoản có tối đa một giỏ "Đang dùng" (ràng buộc có điều '
    'kiện, không phải khóa). Chỉ tài khoản khách (MaKH có giá trị) mới có giỏ.',
    fks=[(['MaTK'], 'TAIKHOAN', ['MaTK'])])

rel('CHITIETGIOHANG', 'mkh', 'Chi tiết giỏ hàng',
    [('MaGio', 'INT', 'NN', 'Giỏ hàng'), ('MaSP', 'INT', 'NN', 'Mặt hàng trong giỏ'),
     ('SoLuongGio', 'INT', 'NN', 'Số lượng khách chọn'), ('ThoiDiemThemGio', 'DATETIME', 'NN', 'Thời điểm thêm vào giỏ')],
    ['MaGio', 'MaSP'], ['MaGio,MaSP -> SoLuongGio,ThoiDiemThemGio'],
    'Mỗi dòng của giỏ hàng cho biết mặt hàng (MaSP) khách đã chọn và số lượng (SoLuongGio), thời điểm thêm. Một mặt hàng chỉ có '
    'một dòng trong giỏ nên (MaGio, MaSP) là khóa; thêm lần nữa thì tăng số lượng. Giỏ chưa chốt giá: giá hiện hành của mặt hàng '
    'mới được chép vào dòng đơn khi cửa hàng xác nhận đơn.',
    'SoLuongGio lớn hơn 0.',
    fks=[(['MaGio'], 'GIOHANG', ['MaGio']), (['MaSP'], 'MATHANG', ['MaSP'])])

rel('MAGIAMGIA', 'nghiep_vu', 'Mã giảm giá',
    [('MaMG', 'INT', 'NN', 'Mã nội bộ'), ('CodeMG', 'VARCHAR(30)', 'NN', 'Mã khách nhập'),
     ('TenChuongTrinh', 'NVARCHAR(200)', 'NN', 'Tên chương trình'),
     ('LoaiGiam', 'NVARCHAR(10)', 'NN', 'Theo phần trăm hoặc theo số tiền'),
     ('MucGiam', 'DECIMAL(15,2)', 'NN', 'Mức giảm'), ('DonToiThieu', 'DECIMAL(15,0)', 'NULL', 'Giá trị đơn tối thiểu'),
     ('GiamToiDa', 'DECIMAL(15,0)', 'NULL', 'Mức giảm tối đa'), ('NgayBatDau', 'DATE', 'NULL', 'Ngày bắt đầu áp dụng'),
     ('NgayKetThuc', 'DATE', 'NULL', 'Ngày hết hạn'), ('GioiHanLuot', 'INT', 'NULL', 'Số lượt dùng tối đa'),
     ('MaNV', 'INT', 'NN', 'Nhân viên tạo mã')],
    ['MaMG'], ['MaMG -> CodeMG,TenChuongTrinh,LoaiGiam,MucGiam,DonToiThieu,GiamToiDa,NgayBatDau,NgayKetThuc,GioiHanLuot,MaNV',
               'CodeMG -> MaMG,TenChuongTrinh,LoaiGiam,MucGiam,DonToiThieu,GiamToiDa,NgayBatDau,NgayKetThuc,GioiHanLuot,MaNV'],
    'Mỗi mã giảm giá có mã nội bộ (MaMG) và mã khách nhập (CodeMG), cả hai không trùng. Mã thuộc một chương trình '
    '(TenChuongTrinh), giảm theo phần trăm hoặc theo số tiền (LoaiGiam, MucGiam), áp dụng cho đơn từ giá trị tối thiểu '
    '(DonToiThieu), giảm tối đa (GiamToiDa), trong thời gian từ NgayBatDau đến NgayKetThuc và dùng tối đa GioiHanLuot lượt. Mỗi mã ghi nhân viên tạo (MaNV) để biết ai '
    'chịu trách nhiệm về chương trình.',
    'CodeMG không rỗng, không trùng. LoaiGiam chỉ nhận "Phần trăm" hoặc "Số tiền". MucGiam lớn hơn 0; nếu theo phần '
    'trăm thì không quá 100. NgayKetThuc nếu có phải sau hoặc bằng NgayBatDau.', fks=[(['MaNV'], 'NHANVIEN', ['MaNV'])],
    uniques=[('CodeMG',)])

rel('DONHANG', 'nghiep_vu', 'Đơn hàng',
    [('MaDH', 'INT', 'NN', 'Mã đơn hàng'), ('SoDH', 'VARCHAR(20)', 'NN', 'Số đơn hàng in trên phiếu'),
     ('ThoiDiemLap', 'DATETIME', 'NN', 'Ngày giờ lập đơn'),
     ('KenhBan', 'NVARCHAR(20)', 'NN', 'Quầy, trang web, điện thoại hoặc tin nhắn'),
     ('MaKH', 'INT', 'NULL', 'Khách hàng (rỗng nếu khách vãng lai)'), ('MaNV', 'INT', 'NULL', 'Nhân viên lập đơn (rỗng nếu khách tự đặt trên trang web)'),
     ('TenNguoiNhan', 'NVARCHAR(100)', 'NULL', 'Tên người nhận hàng'), ('SDTNhan', 'VARCHAR(15)', 'NULL', 'Số điện thoại người nhận'),
     ('DiaChiGiao', 'NVARCHAR(300)', 'NULL', 'Địa chỉ giao hàng'), ('PhiGiao', 'DECIMAL(15,0)', 'NN', 'Phí giao hàng'),
     ('GiamGia', 'DECIMAL(15,0)', 'NN', 'Số tiền giảm trên tiền hàng'), ('MaMG', 'INT', 'NULL', 'Mã giảm giá đã dùng'),
     ('TinhTrangDH', 'NVARCHAR(20)', 'NN', 'Tình trạng đơn'), ('DieuKienCoc', 'NVARCHAR(300)', 'NULL', 'Điều kiện đặt cọc đã thỏa thuận'),
     ('GhiChuDH', 'NVARCHAR(500)', 'NULL', 'Ghi chú')],
    ['MaDH'], ['MaDH -> SoDH,ThoiDiemLap,KenhBan,MaKH,MaNV,TenNguoiNhan,SDTNhan,DiaChiGiao,PhiGiao,GiamGia,MaMG,TinhTrangDH,DieuKienCoc,GhiChuDH',
               'SoDH -> MaDH,ThoiDiemLap,KenhBan,MaKH,MaNV,TenNguoiNhan,SDTNhan,DiaChiGiao,PhiGiao,GiamGia,MaMG,TinhTrangDH,DieuKienCoc,GhiChuDH'],
    'Mỗi đơn hàng có mã (MaDH) và số đơn (SoDH) không trùng, ghi ngày giờ lập (ThoiDiemLap), kênh bán (KenhBan), nhân viên '
    'lập (MaNV, rỗng khi khách tự đặt trên trang web) và khách hàng (MaKH) nếu có. Với đơn cần giao, đơn ghi tên, số điện thoại, địa chỉ người nhận, phí giao, '
    'khoản giảm giá và mã giảm giá đã dùng (MaMG), được chốt khi cửa hàng xác nhận đơn. Đơn có tình trạng (TinhTrangDH) '
    'và, với đơn đặt cọc, ghi điều kiện cọc đã thỏa thuận (DieuKienCoc).',
    'SoDH không trùng. KenhBan chỉ nhận "Quầy", "Trang web", "Điện thoại" hoặc "Tin nhắn". TinhTrangDH chỉ nhận "Chờ xác '
    'nhận", "Đã xác nhận", "Đang chuẩn bị", "Đang giao", "Hoàn tất" hoặc "Đã hủy". PhiGiao và GiamGia không âm. Mỗi đơn '
    'dùng tối đa một mã giảm giá. Đơn bán tại quầy không có người nhận hàng nên TenNguoiNhan, SDTNhan, DiaChiGiao rỗng. Đơn có KenhBan khác "Trang '
    'web" phải có MaNV. Mỗi lần đổi tình trạng đơn được ghi ở NHATKYDONHANG.',
    fks=[(['MaKH'], 'KHACHHANG', ['MaKH']), (['MaNV'], 'NHANVIEN', ['MaNV']), (['MaMG'], 'MAGIAMGIA', ['MaMG'])],
    uniques=[('SoDH',)])

rel('CHITIETDONHANG', 'mkh', 'Chi tiết đơn hàng',
    [('MaDH', 'INT', 'NN', 'Đơn hàng'), ('SoDongDH', 'INT', 'NN', 'Số thứ tự dòng trong đơn'),
     ('MaSP', 'INT', 'NN', 'Mặt hàng bán'), ('SoLuongBan', 'INT', 'NN', 'Số lượng'),
     ('DonGiaChot', 'DECIMAL(15,0)', 'NN', 'Đơn giá bán đã chốt'), ('TenHangChot', 'NVARCHAR(200)', 'NN', 'Tên hàng đã chốt'),
     ('SKUChot', 'VARCHAR(50)', 'NN', 'SKU đã chốt')],
    ['MaDH', 'SoDongDH'], ['MaDH,SoDongDH -> MaSP,SoLuongBan,DonGiaChot,TenHangChot,SKUChot'],
    'Mỗi dòng của đơn hàng được phân biệt bằng đơn (MaDH) và số thứ tự dòng (SoDongDH), cho biết mặt hàng (MaSP), số '
    'lượng (SoLuongBan) và đơn giá, tên hàng, SKU đã chốt tại thời điểm bán (DonGiaChot, TenHangChot, SKUChot). Một mặt hàng '
    'có thể ở nhiều dòng của cùng đơn nếu giá hoặc điều kiện bán khác nhau, vì vậy (MaDH, MaSP) không là khóa. Giá và '
    'tên chốt không đổi khi mặt hàng đổi giá hoặc đổi tên về sau.',
    'SoLuongBan lớn hơn 0. DonGiaChot không âm. Mỗi đơn có ít nhất một dòng. Tổng tiền hàng của đơn bằng tổng '
    'SoLuongBan x DonGiaChot của các dòng; đây là dữ liệu tính toán, không lưu.',
    fks=[(['MaDH'], 'DONHANG', ['MaDH']), (['MaSP'], 'MATHANG', ['MaSP'])])

rel('NHATKYDONHANG', 'mkh', 'Nhật ký tình trạng đơn hàng',
    [('MaDH', 'INT', 'NN', 'Đơn hàng'), ('SoLanDoi', 'INT', 'NN', 'Lần đổi tình trạng thứ mấy của đơn'),
     ('TinhTrangMoi', 'NVARCHAR(20)', 'NN', 'Tình trạng đơn sau lần đổi'), ('ThoiDiemDoi', 'DATETIME', 'NN', 'Thời điểm đổi'),
     ('MaNV', 'INT', 'NULL', 'Nhân viên thực hiện (rỗng nếu khách tự thao tác)'),
     ('LyDoDoi', 'NVARCHAR(300)', 'NULL', 'Lý do (bắt buộc khi hủy)')],
    ['MaDH', 'SoLanDoi'], ['MaDH,SoLanDoi -> TinhTrangMoi,ThoiDiemDoi,MaNV,LyDoDoi'],
    'Mỗi lần đơn hàng đổi tình trạng (xác nhận, chuẩn bị, giao, hoàn tất, hủy) được ghi một dòng nhật ký, phân biệt bằng đơn (MaDH) '
    'và số lần đổi (SoLanDoi), ghi tình trạng mới, thời điểm, nhân viên thực hiện (MaNV) và lý do. Nhờ đó cửa hàng biết ai đã xác nhận, '
    'giao hoặc hủy đơn khi có tranh chấp; khách tự hủy đơn chưa xác nhận thì MaNV rỗng.',
    'SoLanDoi bắt đầu từ 1 và tăng dần theo từng đơn. TinhTrangMoi nhận các giá trị tình trạng của đơn. LyDoDoi không rỗng khi '
    'TinhTrangMoi là "Đã hủy". Các lần đổi sang "Đã xác nhận", "Đang chuẩn bị", "Đang giao" và "Hoàn tất" phải có MaNV. '
    'Dòng nhật ký không sửa, không xóa.',
    fks=[(['MaDH'], 'DONHANG', ['MaDH']), (['MaNV'], 'NHANVIEN', ['MaNV'])])

rel('THANHTOAN', 'nghiep_vu', 'Thanh toán',
    [('MaTT', 'INT', 'NN', 'Mã lần thanh toán'), ('MaDH', 'INT', 'NN', 'Đơn hàng'),
     ('LoaiKhoan', 'NVARCHAR(15)', 'NN', 'Thanh toán hoặc đặt cọc'), ('PhuongThuc', 'NVARCHAR(20)', 'NN', 'Phương thức'),
     ('SoTien', 'DECIMAL(15,0)', 'NN', 'Số tiền'), ('ThoiDiemTT', 'DATETIME', 'NN', 'Thời điểm'),
     ('KetQuaTT', 'NVARCHAR(15)', 'NN', 'Thành công, thất bại hoặc chờ'),
     ('MaGiaoDichNgoai', 'VARCHAR(50)', 'NULL', 'Mã giao dịch của ngân hàng hoặc cổng thanh toán'),
     ('DonViThanhToan', 'NVARCHAR(50)', 'NULL', 'Ngân hàng, ví hoặc cổng thanh toán'),
     ('MaNV', 'INT', 'NULL', 'Nhân viên xác nhận đã nhận tiền'),
     ('MaNVThu', 'INT', 'NULL', 'Nhân viên giao hàng thu tiền (khoản thu khi giao)')],
    ['MaTT'], ['MaTT -> MaDH,LoaiKhoan,PhuongThuc,SoTien,ThoiDiemTT,KetQuaTT,MaGiaoDichNgoai,DonViThanhToan,MaNV,MaNVThu'],
    'Mỗi lần thanh toán có mã (MaTT), thuộc một đơn hàng (MaDH), ghi loại khoản (LoaiKhoan: thanh toán hoặc đặt cọc), '
    'phương thức (PhuongThuc), số tiền, thời điểm, kết quả và, với giao dịch qua ngân hàng hoặc cổng thanh toán, mã giao dịch '
    'ngoài cùng đơn vị thanh toán. Một đơn có thể có nhiều lần thanh toán, kể cả cọc và phần còn lại. Nhân viên (MaNV) '
    'xác nhận đã nhận tiền sau khi đối chiếu; với khoản thu khi giao hàng, người giao (MaNVThu) là người đã thu tiền của khách.',
    'PhuongThuc chỉ nhận "Tiền mặt", "Chuyển khoản", "Mã QR", "Thẻ ngân hàng", "Ví điện tử", "Cổng thanh toán" hoặc '
    '"Thu khi giao". SoTien lớn hơn 0. Chỉ lần thanh toán có KetQuaTT là "Thành công" mới được tính là đã thu. Cặp '
    '(DonViThanhToan, MaGiaoDichNgoai) không trùng khi cả hai có giá trị. MaNVThu chỉ có khi PhuongThuc là "Thu khi giao".',
    fks=[(['MaDH'], 'DONHANG', ['MaDH']), (['MaNV'], 'NHANVIEN', ['MaNV']), (['MaNVThu'], 'NHANVIEN', ['MaNV'])])

rel('PHIEUGIAO', 'nghiep_vu', 'Phiếu giao hàng',
    [('MaGiao', 'INT', 'NN', 'Mã phiếu giao'), ('MaDH', 'INT', 'NN', 'Đơn hàng được giao'),
     ('MaNV', 'INT', 'NN', 'Nhân viên giao hàng'), ('ThoiDiemXuat', 'DATETIME', 'NN', 'Thời điểm xuất kho giao đi'),
     ('TinhTrangGiao', 'NVARCHAR(20)', 'NN', 'Tình trạng giao')],
    ['MaGiao'], ['MaGiao -> MaDH,MaNV,ThoiDiemXuat,TinhTrangGiao',
                 'MaDH -> MaGiao,MaNV,ThoiDiemXuat,TinhTrangGiao'],
    'Mỗi phiếu giao có mã (MaGiao), lập cho đúng một đơn cần giao (MaDH) và mỗi đơn chỉ có tối đa một phiếu giao. Phiếu '
    'ghi nhân viên giao hàng (MaNV), thời điểm xuất kho (ThoiDiemXuat) và tình trạng giao (TinhTrangGiao).',
    'MaDH không trùng. TinhTrangGiao chỉ nhận "Đang giao", "Đã giao" hoặc "Không thành công". Chỉ đơn có người nhận và '
    'địa chỉ giao mới có phiếu giao.',
    fks=[(['MaDH'], 'DONHANG', ['MaDH']), (['MaNV'], 'NHANVIEN', ['MaNV'])], uniques=[('MaDH',)])

rel('LANGIAO', 'mkh', 'Lần giao hàng',
    [('MaGiao', 'INT', 'NN', 'Phiếu giao'), ('SoLan', 'INT', 'NN', 'Lần giao thứ mấy (1 đến 3)'),
     ('ThoiDiemGiao', 'DATETIME', 'NN', 'Thời điểm thử giao'), ('KetQuaGiao', 'NVARCHAR(20)', 'NN', 'Thành công hoặc thất bại'),
     ('LyDoThatBai', 'NVARCHAR(300)', 'NULL', 'Lý do khách vắng hoặc từ chối nhận'),
     ('MaNV', 'INT', 'NN', 'Nhân viên giao hàng thực hiện lần này')],
    ['MaGiao', 'SoLan'], ['MaGiao,SoLan -> ThoiDiemGiao,KetQuaGiao,LyDoThatBai,MaNV'],
    'Mỗi lần thử giao của một phiếu giao được phân biệt bằng phiếu (MaGiao) và số lần (SoLan), ghi thời điểm, kết quả '
    '(KetQuaGiao), lý do nếu không thành công (LyDoThatBai) và nhân viên giao hàng thực hiện lần đó (MaNV). Mỗi đơn được thử giao tối đa 3 lần. '
    'Đây là mối kết hợp giữa phiếu giao và nhân viên; nhân viên phụ trách phiếu (PHIEUGIAO.MaNV) có thể khác người đi giao một lần cụ thể.',
    'SoLan từ 1 đến 3. LyDoThatBai không rỗng khi KetQuaGiao là "Thất bại". MaNV là nhân viên đang giữ vai trò giao hàng.',
    fks=[(['MaGiao'], 'PHIEUGIAO', ['MaGiao']), (['MaNV'], 'NHANVIEN', ['MaNV'])])

rel('PHIEUNHAP', 'nghiep_vu', 'Phiếu nhập',
    [('MaPN', 'INT', 'NN', 'Mã phiếu nhập'), ('SoPhieu', 'VARCHAR(20)', 'NN', 'Số phiếu nhập'),
     ('MaNCC', 'INT', 'NN', 'Nhà cung cấp'), ('MaNV', 'INT', 'NN', 'Nhân viên kho lập phiếu'),
     ('ThoiDiemNhan', 'DATETIME', 'NN', 'Thời điểm nhận hàng'), ('TinhTrangPN', 'NVARCHAR(20)', 'NN', 'Tình trạng phiếu'),
     ('MaNVXacNhan', 'INT', 'NULL', 'Nhân viên xác nhận phiếu'), ('ThoiDiemXacNhan', 'DATETIME', 'NULL', 'Thời điểm xác nhận'),
     ('SoHoaDonNCC', 'VARCHAR(30)', 'NULL', 'Số hóa đơn của nhà cung cấp'), ('GhiChuPN', 'NVARCHAR(500)', 'NULL', 'Ghi chú')],
    ['MaPN'], ['MaPN -> SoPhieu,MaNCC,MaNV,ThoiDiemNhan,TinhTrangPN,MaNVXacNhan,ThoiDiemXacNhan,SoHoaDonNCC,GhiChuPN',
               'SoPhieu -> MaPN,MaNCC,MaNV,ThoiDiemNhan,TinhTrangPN,MaNVXacNhan,ThoiDiemXacNhan,SoHoaDonNCC,GhiChuPN'],
    'Mỗi phiếu nhập là một lần nhận hàng thực tế, có mã (MaPN) và số phiếu (SoPhieu) không trùng, ghi nhà cung cấp '
    '(MaNCC), nhân viên lập (MaNV), thời điểm nhận, tình trạng phiếu, nhân viên và thời điểm xác nhận phiếu, số hóa đơn của '
    'nhà cung cấp và ghi chú.',
    'SoPhieu không trùng. TinhTrangPN chỉ nhận "Nháp", "Đã xác nhận" hoặc "Đã hủy". Phiếu có ít nhất một dòng; hàng '
    'chỉ được ghi tăng vào kho một lần khi phiếu chuyển sang "Đã xác nhận". Phiếu "Đã xác nhận" phải có MaNVXacNhan và '
    'ThoiDiemXacNhan; hai cột này cùng rỗng hoặc cùng có giá trị.',
    fks=[(['MaNCC'], 'NHACUNGCAP', ['MaNCC']), (['MaNV'], 'NHANVIEN', ['MaNV']), (['MaNVXacNhan'], 'NHANVIEN', ['MaNV'])], uniques=[('SoPhieu',)])

rel('CHITIETPHIEUNHAP', 'mkh', 'Chi tiết phiếu nhập',
    [('MaPN', 'INT', 'NN', 'Phiếu nhập'), ('SoDongPN', 'INT', 'NN', 'Số thứ tự dòng trong phiếu'),
     ('MaSP', 'INT', 'NN', 'Mặt hàng nhập'), ('SoLuongNhap', 'INT', 'NN', 'Số lượng thực nhận'),
     ('GiaNhap', 'DECIMAL(15,0)', 'NN', 'Giá nhập một đơn vị')],
    ['MaPN', 'SoDongPN'], ['MaPN,SoDongPN -> MaSP,SoLuongNhap,GiaNhap'],
    'Mỗi dòng của phiếu nhập được phân biệt bằng phiếu (MaPN) và số thứ tự dòng (SoDongPN), cho biết mặt hàng (MaSP), '
    'số lượng thực nhận (SoLuongNhap) và giá nhập (GiaNhap). Cùng một mặt hàng có thể ở nhiều dòng nếu khác giá hoặc '
    'khác lô.',
    'SoLuongNhap lớn hơn 0. GiaNhap không âm.',
    fks=[(['MaPN'], 'PHIEUNHAP', ['MaPN']), (['MaSP'], 'MATHANG', ['MaSP'])])

rel('HANGCOSERI', 'nghiep_vu', 'Chiếc hàng có số seri',
    [('MaSeri', 'INT', 'NN', 'Mã nội bộ của chiếc hàng'), ('SoSeri', 'VARCHAR(60)', 'NN', 'Số seri in trên sản phẩm'),
     ('MaSP', 'INT', 'NN', 'Mặt hàng của chiếc này'), ('MaPN', 'INT', 'NN', 'Phiếu nhập chiếc này về'),
     ('SoDongPN', 'INT', 'NN', 'Dòng của phiếu nhập'), ('MaDH', 'INT', 'NULL', 'Đơn đã bán chiếc này'),
     ('SoDongDH', 'INT', 'NULL', 'Dòng của đơn đã bán'), ('TinhTrangSeri', 'NVARCHAR(20)', 'NN', 'Trong kho, đã bán, chờ kiểm tra...'),
     ('ThoiDiemNhap', 'DATETIME', 'NN', 'Thời điểm nhập kho')],
    ['MaSeri'], ['MaSeri -> SoSeri,MaSP,MaPN,SoDongPN,MaDH,SoDongDH,TinhTrangSeri,ThoiDiemNhap',
                 'MaSP,SoSeri -> MaSeri',
                 'MaPN,SoDongPN -> MaSP',
                 'MaDH,SoDongDH -> MaSP'],
    'Mỗi chiếc hàng có số seri được phân biệt bằng mã nội bộ (MaSeri). Chiếc hàng ghi số seri (SoSeri), thuộc một mặt '
    'hàng (MaSP), nhập về theo một dòng của phiếu nhập (MaPN, SoDongPN) và, khi đã bán, thuộc một dòng của đơn hàng '
    '(MaDH, SoDongDH). Số seri là duy nhất trong cùng mặt hàng; hai mặt hàng khác nhau có thể có cùng số seri. Mỗi dòng '
    'nhập hay dòng đơn chỉ chứa một mặt hàng.',
    'MaSeri là số tự nhiên tăng dần. Cặp (MaSP, SoSeri) không trùng. MaSP của chiếc phải bằng MaSP của dòng nhập và '
    'của dòng đơn nếu có. Mặt hàng phải có CoSeri = 1. MaDH và SoDongDH cùng rỗng hoặc cùng có giá trị. Các PTH có vế trái '
    'chứa cột cho phép rỗng (MaDH, SoDongDH) chỉ xét trên những chiếc đã bán.',
    fks=[(['MaSP'], 'MATHANG', ['MaSP']), (['MaPN', 'SoDongPN'], 'CHITIETPHIEUNHAP', ['MaPN', 'SoDongPN']),
         (['MaDH', 'SoDongDH'], 'CHITIETDONHANG', ['MaDH', 'SoDongDH'])], uniques=[('MaSP', 'SoSeri')])

rel('GIAODICHKHO', 'nghiep_vu', 'Giao dịch kho',
    [('MaGDK', 'INT', 'NN', 'Mã giao dịch kho'), ('MaSP', 'INT', 'NN', 'Mặt hàng'),
     ('NhomKho', 'NVARCHAR(20)', 'NN', 'Đủ điều kiện bán, chờ kiểm tra hoặc chờ xử lý'),
     ('LoaiBienDong', 'NVARCHAR(20)', 'NN', 'Nhập, xuất bán, nhận lại hoặc chuyển nhóm'),
     ('SoLuongGD', 'INT', 'NN', 'Số lượng thay đổi (luôn dương)'), ('ThoiDiemGD', 'DATETIME', 'NN', 'Thời điểm'),
     ('MaNV', 'INT', 'NULL', 'Nhân viên thực hiện'), ('LoaiChungTu', 'NVARCHAR(20)', 'NULL', 'Loại chứng từ gốc'),
     ('MaChungTu', 'INT', 'NULL', 'Mã chứng từ gốc'), ('GhiChuGD', 'NVARCHAR(500)', 'NULL', 'Ghi chú')],
    ['MaGDK'], ['MaGDK -> MaSP,NhomKho,LoaiBienDong,SoLuongGD,ThoiDiemGD,MaNV,LoaiChungTu,MaChungTu,GhiChuGD'],
    'Mỗi lần hàng vào hoặc ra kho (nhập, bán, nhận lại, chuyển nhóm) là một giao dịch kho có mã (MaGDK), '
    'ghi mặt hàng, nhóm kho bị ảnh hưởng, loại biến động, số lượng, thời điểm, nhân viên thực hiện và chứng từ gốc. '
    'Số lượng hàng trong kho được tính từ các giao dịch này, không lưu thành một cột riêng.',
    'SoLuongGD lớn hơn 0; hướng tăng hoặc giảm do LoaiBienDong quy định. NhomKho chỉ nhận "Đủ điều kiện bán", "Chờ '
    'kiểm tra" hoặc "Chờ xử lý". (LoaiChungTu, MaChungTu) trỏ tới nhiều loại chứng từ nên không khai báo được khóa ngoại.',
    fks=[(['MaSP'], 'MATHANG', ['MaSP']), (['MaNV'], 'NHANVIEN', ['MaNV'])])

rel('HOSODOITRA', 'nghiep_vu', 'Hồ sơ đổi trả',
    [('MaHS', 'INT', 'NN', 'Mã hồ sơ đổi trả'), ('MaDH', 'INT', 'NN', 'Đơn gốc'),
     ('MaNV', 'INT', 'NN', 'Nhân viên tiếp nhận'),
     ('NgayDeNghi', 'DATE', 'NN', 'Ngày đề nghị'), ('LoaiTruongHop', 'NVARCHAR(30)', 'NN', 'Giao sai/hư hỏng, lỗi nhà sản xuất, khách đổi ý'),
     ('LyDoDoiTra', 'NVARCHAR(500)', 'NN', 'Lý do'), ('TinhTrangHS', 'NVARCHAR(20)', 'NN', 'Tình trạng hồ sơ'),
     ('HinhThucXuLy', 'NVARCHAR(20)', 'NULL', 'Đổi hàng hoặc hoàn tiền')],
    ['MaHS'], ['MaHS -> MaDH,MaNV,NgayDeNghi,LoaiTruongHop,LyDoDoiTra,TinhTrangHS,HinhThucXuLy'],
    'Mỗi hồ sơ đổi trả có mã (MaHS), lập cho một đơn gốc (MaDH), nhân viên tiếp nhận '
    '(MaNV), ngày đề nghị, trường hợp (LoaiTruongHop), lý do, tình trạng và hình thức xử lý (đổi hàng hoặc hoàn tiền). '
    'Một đơn có thể có nhiều hồ sơ, miễn tổng số lượng trả không vượt số đã giao.',
    'LoaiTruongHop chỉ nhận "Giao sai, thiếu hoặc hư hỏng", "Lỗi nhà sản xuất" hoặc "Khách đổi ý". HinhThucXuLy chỉ '
    'nhận "Đổi hàng" hoặc "Hoàn tiền". Hồ sơ chỉ được lập trong thời hạn quy định theo từng trường hợp (48 giờ, 7 hoặc '
    '30 ngày kể từ khi nhận hàng).',
    fks=[(['MaDH'], 'DONHANG', ['MaDH']), (['MaNV'], 'NHANVIEN', ['MaNV'])])

rel('CHITIETTRA', 'mkh', 'Chi tiết trả hàng',
    [('MaHS', 'INT', 'NN', 'Hồ sơ đổi trả'), ('SoDongDH', 'INT', 'NN', 'Dòng của đơn gốc được trả'),
     ('MaDH', 'INT', 'NN', 'Đơn gốc (lưu thêm để khai báo khóa ngoại tới dòng đơn)'),
     ('SoLuongTra', 'INT', 'NN', 'Số lượng trả'), ('MaSeri', 'INT', 'NULL', 'Chiếc hàng trả (hàng có seri)')],
    ['MaHS', 'SoDongDH'], ['MaHS,SoDongDH -> MaDH,SoLuongTra,MaSeri', 'MaHS -> MaDH'],
    'Mỗi dòng của hồ sơ đổi trả được phân biệt bằng hồ sơ (MaHS) và dòng của đơn gốc được trả (SoDongDH), ghi số lượng trả '
    '(SoLuongTra) và, với hàng có seri, chiếc hàng trả (MaSeri). Để khai báo khóa ngoại tới dòng đơn (MaDH, SoDongDH), '
    'dòng trả ghi thêm mã đơn gốc (MaDH), chính là đơn của hồ sơ.',
    'SoLuongTra lớn hơn 0 và không vượt số lượng dòng đơn đã giao trừ số đã trả ở các hồ sơ khác. MaDH phải bằng MaDH '
    'của hồ sơ (ràng buộc liên quan hệ).',
    fks=[(['MaHS'], 'HOSODOITRA', ['MaHS']), (['MaDH', 'SoDongDH'], 'CHITIETDONHANG', ['MaDH', 'SoDongDH']),
         (['MaSeri'], 'HANGCOSERI', ['MaSeri'])])

rel('LANNHANLAI', 'nghiep_vu', 'Lần nhận lại hàng',
    [('MaNhanLai', 'INT', 'NN', 'Mã lần nhận lại'), ('MaHS', 'INT', 'NN', 'Hồ sơ đổi trả'),
     ('ThoiDiemNhanLai', 'DATETIME', 'NN', 'Thời điểm nhận hàng về'), ('MaNV', 'INT', 'NULL', 'Nhân viên kiểm tra'),
     ('KetLuan', 'NVARCHAR(200)', 'NULL', 'Kết luận kiểm tra'), ('NhomSauKiemTra', 'NVARCHAR(20)', 'NULL', 'Nhóm kho sau kiểm tra'),
     ('ThoiDiemDuyet', 'DATETIME', 'NULL', 'Thời điểm người quản lý duyệt'),
     ('MaNVDuyet', 'INT', 'NULL', 'Người quản lý duyệt chuyển nhóm')],
    ['MaNhanLai'], ['MaNhanLai -> MaHS,ThoiDiemNhanLai,MaNV,KetLuan,NhomSauKiemTra,ThoiDiemDuyet,MaNVDuyet'],
    'Mỗi lần cửa hàng nhận hàng trả về có mã (MaNhanLai), thuộc một hồ sơ đổi trả (MaHS), ghi thời điểm nhận. Mọi hàng '
    'nhận về vào nhóm chờ kiểm tra; nhân viên kỹ thuật (MaNV) kiểm tra, ghi kết luận và nhóm kho sau kiểm tra, người quản '
    'lý (MaNVDuyet) duyệt ở ThoiDiemDuyet.',
    'NhomSauKiemTra chỉ nhận "Đủ điều kiện bán", "Chờ xử lý" hoặc "Không bán được". Hàng chỉ chuyển nhóm sau khi có '
    'ThoiDiemDuyet. ThoiDiemDuyet và MaNVDuyet cùng rỗng hoặc cùng có giá trị. Việc chuyển nhóm không làm tăng tổng số hàng '
    'thực tế trong kho.',
    fks=[(['MaHS'], 'HOSODOITRA', ['MaHS']), (['MaNV'], 'NHANVIEN', ['MaNV']), (['MaNVDuyet'], 'NHANVIEN', ['MaNV'])])

rel('KHOANHOAN', 'nghiep_vu', 'Khoản hoàn tiền',
    [('MaHoan', 'INT', 'NN', 'Mã khoản hoàn'), ('MaTT', 'INT', 'NN', 'Khoản thu gốc được hoàn'),
     ('MaHS', 'INT', 'NULL', 'Hồ sơ đổi trả liên quan'), ('MaNV', 'INT', 'NN', 'Người quản lý duyệt hoàn'),
     ('SoTienHoan', 'DECIMAL(15,0)', 'NN', 'Số tiền hoàn'), ('PhuongThucHoan', 'NVARCHAR(30)', 'NN', 'Phương thức hoàn'),
     ('ThoiDiemDuyetHoan', 'DATETIME', 'NN', 'Thời điểm duyệt'), ('ThoiDiemChi', 'DATETIME', 'NULL', 'Thời điểm chi tiền'),
     ('MaNVChi', 'INT', 'NULL', 'Nhân viên chi tiền hoàn')],
    ['MaHoan'], ['MaHoan -> MaTT,MaHS,MaNV,SoTienHoan,PhuongThucHoan,ThoiDiemDuyetHoan,ThoiDiemChi,MaNVChi'],
    'Mỗi khoản hoàn tiền có mã (MaHoan), gắn với một khoản thu gốc (MaTT) và, nếu do đổi trả, với hồ sơ (MaHS). Người '
    'quản lý (MaNV) duyệt; khoản hoàn ghi số tiền, phương thức hoàn, thời điểm duyệt, thời điểm chi và nhân viên chi tiền (MaNVChi). Có thể hoàn '
    'nhiều lần nhưng tổng không vượt số tiền đã thu của khoản gốc.',
    'SoTienHoan lớn hơn 0. Tổng SoTienHoan của một MaTT không vượt SoTien của khoản thu đó. PhuongThucHoan là phương '
    'thức khách đã trả. ThoiDiemChi và MaNVChi cùng rỗng hoặc cùng có giá trị. Chỉ nhân viên giữ vai trò Quản lý được duyệt (MaNV).',
    fks=[(['MaTT'], 'THANHTOAN', ['MaTT']), (['MaHS'], 'HOSODOITRA', ['MaHS']), (['MaNV'], 'NHANVIEN', ['MaNV']),
         (['MaNVChi'], 'NHANVIEN', ['MaNV'])])

rel('PHIEUBAOHANH', 'nghiep_vu', 'Phiếu tiếp nhận bảo hành',
    [('MaPhieuBH', 'INT', 'NN', 'Mã phiếu bảo hành'),
     ('MaSeri', 'INT', 'NULL', 'Chiếc hàng bảo hành (hàng có seri)'), ('MaSP', 'INT', 'NN', 'Mặt hàng bảo hành'),
     ('MaDH', 'INT', 'NN', 'Đơn mua gốc'), ('SoDongDH', 'INT', 'NN', 'Dòng mua gốc'),
     ('MoTaLoi', 'NVARCHAR(500)', 'NN', 'Mô tả lỗi'), ('PhuKienDiKem', 'NVARCHAR(300)', 'NULL', 'Phụ kiện đi kèm'),
     ('NgayNhan', 'DATE', 'NN', 'Ngày nhận'), ('NgayHenTra', 'DATE', 'NN', 'Ngày hẹn trả'),
     ('NgayTraThucTe', 'DATE', 'NULL', 'Ngày trả thực tế'), ('TinhTrangBH', 'NVARCHAR(20)', 'NN', 'Tình trạng phiếu'),
     ('KetQuaBH', 'NVARCHAR(30)', 'NULL', 'Kết quả (sửa xong, đổi mới, hoàn tiền...)'),
     ('LyDoTuChoi', 'NVARCHAR(300)', 'NULL', 'Lý do từ chối bảo hành'), ('MaNV', 'INT', 'NN', 'Nhân viên tiếp nhận')],
    ['MaPhieuBH'], ['MaPhieuBH -> MaSeri,MaSP,MaDH,SoDongDH,MoTaLoi,PhuKienDiKem,NgayNhan,NgayHenTra,NgayTraThucTe,TinhTrangBH,KetQuaBH,LyDoTuChoi,MaNV',
                    'MaDH,SoDongDH -> MaSP',
                    'MaSeri -> MaSP'],
    'Mỗi phiếu tiếp nhận bảo hành có mã (MaPhieuBH), ghi chiếc hàng (MaSeri) nếu có seri, mặt hàng '
    '(MaSP), dòng mua gốc (MaDH, SoDongDH), mô tả lỗi, phụ kiện đi kèm, ngày nhận, ngày hẹn trả, ngày trả thực tế, tình '
    'trạng, kết quả, lý do từ chối nếu có và nhân viên tiếp nhận (MaNV). Mặt hàng được ghi sẵn trên phiếu để tra cứu nhanh. '
    'Mỗi dòng mua và mỗi chiếc hàng chỉ thuộc một mặt hàng.',
    'NgayHenTra không trước NgayNhan. TinhTrangBH chỉ nhận "Đã tiếp nhận", "Đang kiểm tra", "Đang gửi hãng", "Đã có kết '
    'quả", "Đã trả khách" hoặc "Từ chối". LyDoTuChoi không rỗng khi TinhTrangBH là "Từ chối". MaSP phải trùng MaSP của '
    'dòng mua gốc và của chiếc hàng. Các PTH có vế trái là MaSeri chỉ xét trên phiếu có MaSeri.',
    fks=[(['MaSeri'], 'HANGCOSERI', ['MaSeri']), (['MaDH', 'SoDongDH'], 'CHITIETDONHANG', ['MaDH', 'SoDongDH']),
         (['MaSP'], 'MATHANG', ['MaSP']), (['MaNV'], 'NHANVIEN', ['MaNV'])])

ORDER = list(REL)


# ----------------------------------------------------------------------------------------------
# Lược đồ sau cải tiến: thay đổi so với lược đồ ban đầu (xem chương 2, mục 2.4)
# ----------------------------------------------------------------------------------------------
def improved():
    """Trả về bản sao lược đồ đã cải tiến: tách HoTen, bỏ MaDH khỏi CHITIETTRA, bỏ MaSP khỏi PHIEUBAOHANH, tách SERIMATHANG."""
    import copy
    R = copy.deepcopy(REL)


    # DC1: tách họ tên
    for name, ho, ten, hoten, mean in (('KHACHHANG', 'HoLotKH', 'TenKH', 'HoTenKH', 'khách hàng'),
                                        ('NHANVIEN', 'HoLotNV', 'TenNV', 'HoTenNV', 'nhân viên')):
        r = R[name]
        i = [a[0] for a in r['attrs']].index(hoten)
        r['attrs'][i:i + 1] = [(ho, 'NVARCHAR(80)', 'NN', f'Họ và tên lót {mean}'), (ten, 'NVARCHAR(30)', 'NN', f'Tên {mean}')]
    for name in ('KHACHHANG', 'NHANVIEN'):
        R[name]['F'] = [f.replace('HoTenKH', 'HoLotKH,TenKH').replace('HoTenNV', 'HoLotNV,TenNV') for f in R[name]['F']]
    # CHITIETTRA: bỏ MaDH
    ct = R['CHITIETTRA']
    ct['attrs'] = [a for a in ct['attrs'] if a[0] != 'MaDH']
    ct['F'] = ['MaHS,SoDongDH -> SoLuongTra,MaSeri']
    ct['fks'] = [(('MaHS',), 'HOSODOITRA', ('MaHS',)), (('MaSeri',), 'HANGCOSERI', ('MaSeri',))]
    ct['tantu'] = ('Mỗi dòng của hồ sơ đổi trả được phân biệt bằng hồ sơ (MaHS) và số thứ tự dòng của đơn gốc được trả '
                   '(SoDongDH), ghi số lượng trả (SoLuongTra) và, với hàng có seri, chiếc hàng trả (MaSeri). Đơn gốc '
                   'của dòng trả là đơn của hồ sơ (HOSODOITRA.MaDH).')
    ct['rangbuoc'] = ('SoLuongTra lớn hơn 0 và không vượt số lượng dòng đơn đã giao trừ số đã trả ở các hồ sơ khác. '
                      'Dòng (MaDH của hồ sơ, SoDongDH) phải có trong CHITIETDONHANG; ràng buộc liên quan hệ cưỡng chế '
                      'bằng khóa ngoại ghép khi cài đặt hoặc bằng kiểm tra khi ghi.')
    # PHIEUBAOHANH: bỏ MaSP
    bh = R['PHIEUBAOHANH']
    bh['attrs'] = [a for a in bh['attrs'] if a[0] != 'MaSP']
    bh['F'] = ['MaPhieuBH -> MaSeri,MaDH,SoDongDH,MoTaLoi,PhuKienDiKem,NgayNhan,NgayHenTra,NgayTraThucTe,TinhTrangBH,KetQuaBH,LyDoTuChoi,MaNV']
    bh['fks'] = [f for f in bh['fks'] if f[1] != 'MATHANG']
    bh['tantu'] = bh['tantu'].replace('mặt hàng (MaSP), ', '').replace(
        'Mặt hàng được ghi sẵn trên phiếu để tra cứu nhanh. Mỗi dòng mua và mỗi chiếc hàng chỉ thuộc một mặt hàng.',
        'Mặt hàng bảo hành suy ra từ dòng mua gốc (hoặc từ chiếc hàng).')
    bh['rangbuoc'] = ('NgayHenTra không trước NgayNhan. TinhTrangBH chỉ nhận "Đã tiếp nhận", "Đang kiểm tra", "Đang gửi '
                      'hãng", "Đã có kết quả", "Đã trả khách" hoặc "Từ chối". LyDoTuChoi không rỗng khi TinhTrangBH là '
                      '"Từ chối". Nếu có MaSeri thì mặt hàng của chiếc hàng phải trùng mặt hàng của dòng mua gốc.')
    # HANGCOSERI: tách SERIMATHANG (SoSeri, MaSP) khỏi HANGCOSERI
    hs = R['HANGCOSERI']
    hs['attrs'] = [a for a in hs['attrs'] if a[0] not in ('SoSeri', 'MaSP')]
    hs['F'] = ['MaSeri -> MaPN,SoDongPN,MaDH,SoDongDH,TinhTrangSeri,ThoiDiemNhap']
    hs['fks'] = [(('MaSeri',), 'SERIMATHANG', ('MaSeri',)),
                 (('MaPN', 'SoDongPN'), 'CHITIETPHIEUNHAP', ('MaPN', 'SoDongPN')),
                 (('MaDH', 'SoDongDH'), 'CHITIETDONHANG', ('MaDH', 'SoDongDH'))]
    hs['uniques'] = []
    hs['ten'] = 'Chiếc hàng có số seri (thông tin nhập và bán)'
    hs['tantu'] = ('Mỗi chiếc hàng có số seri được phân biệt bằng mã nội bộ (MaSeri) và có hồ sơ nhận diện ở SERIMATHANG. '
                   'Quan hệ này ghi chiếc hàng nhập về theo dòng nào của phiếu nhập (MaPN, SoDongPN), khi đã bán thì '
                   'thuộc dòng nào của đơn hàng (MaDH, SoDongDH), tình trạng hiện tại và thời điểm nhập kho.')
    hs['rangbuoc'] = ('Mặt hàng của chiếc (SERIMATHANG.MaSP) phải bằng MaSP của dòng nhập và của dòng đơn nếu có. MaDH và '
                      'SoDongDH cùng rỗng hoặc cùng có giá trị.')
    R['SERIMATHANG'] = dict(
        loai='nghiep_vu', ten='Nhận diện chiếc hàng (số seri theo mặt hàng)',
        attrs=[('MaSeri', 'INT', 'NN', 'Mã nội bộ của chiếc hàng'), ('SoSeri', 'VARCHAR(60)', 'NN', 'Số seri in trên sản phẩm'),
               ('MaSP', 'INT', 'NN', 'Mặt hàng của chiếc này')],
        pk=['MaSeri'], F=['MaSeri -> SoSeri,MaSP', 'MaSP,SoSeri -> MaSeri'],
        tantu=('Mỗi chiếc hàng có số seri được phân biệt bằng mã nội bộ (MaSeri), ghi số seri (SoSeri) và mặt hàng (MaSP). '
               'Số seri là duy nhất trong cùng mặt hàng nên (MaSP, SoSeri) cũng xác định chiếc hàng.'),
        rangbuoc='Cặp (MaSP, SoSeri) không trùng. Mặt hàng phải có CoSeri = 1.',
        fks=[(('MaSP',), 'MATHANG', ('MaSP',))], uniques=[('MaSP', 'SoSeri')])
    # CHITIETTRA, HANGCOSERI... các khóa ngoại tới SERIMATHANG giữ nguyên tên MaSeri
    return R


# Quan hệ chiếu / thứ tự trình bày sau cải tiến
ORDER_IMPROVED = ORDER[:ORDER.index('HANGCOSERI') + 1] + ['SERIMATHANG'] + ORDER[ORDER.index('HANGCOSERI') + 1:]
