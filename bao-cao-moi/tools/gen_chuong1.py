#!/usr/bin/env python3
"""Sinh chương 1 (chuong/01_chuong1.md): phần văn xuôi viết tay, danh sách thực thể và bảng mối kết hợp sinh từ lược đồ.  Chạy: python3 tools/gen_chuong1.py"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import erd
import luoc_do

REL = luoc_do.REL
OUT = []


def w(s=''):
    OUT.append(s)


MOTA = {
    'LOAIHANG': 'Các loại hàng, phân cấp cha – con (ví dụ "Linh kiện máy tính" gồm "Bộ nhớ RAM", "Ổ cứng SSD").',
    'THUONGHIEU': 'Các thương hiệu của hàng hóa.',
    'MATHANG': 'Các mặt hàng cửa hàng kinh doanh, mỗi mặt hàng có mã nội bộ và mã hàng thương mại (SKU) riêng.',
    'ANHMATHANG': 'Các ảnh minh họa của mặt hàng, có vị trí và ảnh đại diện.',
    'DINHNGHIATHONGSO': 'Các thông số kỹ thuật mà từng loại hàng quy định (dung lượng, tốc độ, công suất…).',
    'KHACHHANG': 'Khách hàng đã để lại thông tin để tra cứu bảo hành, đổi trả và xuất hóa đơn, hoặc đăng ký tài khoản trên trang web.',
    'DIACHIKHACH': 'Các địa chỉ nhận hàng khách lưu trên trang web; một địa chỉ mặc định.',
    'NHANVIEN': 'Nhân viên của cửa hàng: hồ sơ, ngày vào làm và nghỉ việc; một người có thể kiêm nhiều việc.',
    'VAITRO': 'Các vai trò công việc của cửa hàng (quản trị, quản lý, bán hàng, thu ngân, kỹ thuật, kho, giao hàng, chăm sóc khách hàng).',
    'TAIKHOAN': 'Tài khoản đăng nhập của khách trên trang web hoặc của nhân viên trên hệ thống.',
    'NHACUNGCAP': 'Nhà phân phối, đại lý chính hãng giao hàng cho cửa hàng.',
    'MAGIAMGIA': 'Mã giảm giá của từng chương trình khuyến mãi, có thời hạn, số lượt dùng và nhân viên tạo mã.',
    'GIOHANG': 'Giỏ hàng khách đang chọn trên trang web, tạm thời trước khi gửi đơn.',
    'DONHANG': 'Đơn hàng bán tại quầy, qua điện thoại, tin nhắn hoặc trang web; ghi thông tin người nhận, giảm giá, tình trạng đơn.',
    'NHATKYDONHANG': 'Mỗi lần đơn đổi tình trạng: ai làm, lúc nào, vì sao (truy trách nhiệm).',
    'THANHTOAN': 'Mỗi lần thanh toán hoặc đặt cọc cho một đơn hàng.',
    'PHIEUGIAO': 'Phiếu giao hàng lập cho đơn cần giao tận nơi.',
    'LANGIAO': 'Mỗi lần thử giao của một phiếu giao (tối đa 3 lần).',
    'PHIEUNHAP': 'Phiếu nhập ghi một lần nhận hàng thực tế từ nhà cung cấp.',
    'HANGCOSERI': 'Từng chiếc hàng có số seri riêng: nhập về khi nào, lần bán gần nhất theo đơn nào, tình trạng hiện tại.',
    'GIAODICHKHO': 'Mỗi lần hàng vào hoặc ra kho (nhập, bán, nhận lại, chuyển nhóm).',
    'HOSODOITRA': 'Hồ sơ đổi trả của một đơn: trường hợp, lý do, tình trạng, hình thức xử lý.',
    'LANNHANLAI': 'Mỗi lần cửa hàng nhận hàng trả về để kiểm tra.',
    'KHOANHOAN': 'Mỗi khoản hoàn tiền cho khách, gắn với khoản thu gốc.',
    'PHIEUBAOHANH': 'Phiếu tiếp nhận sản phẩm lỗi để bảo hành.',
}
LY_DO = {
    'LOAIHANG': 'Danh mục phân loại ổn định, không có thuộc tính thời gian.',
    'THUONGHIEU': 'Danh mục ổn định, không có thuộc tính thời gian.',
    'MATHANG': 'Tài nguyên kinh doanh có trước khi tin học hóa; giá thay đổi chậm nhưng mặt hàng không gắn với một thời điểm phát sinh.',
    'ANHMATHANG': 'Tư liệu đi kèm mặt hàng, ổn định; có từ hai thể hiện trở lên.',
    'DINHNGHIATHONGSO': 'Danh mục quy định theo loại hàng, ổn định.',
    'KHACHHANG': 'Con người tham gia mua bán; được lưu vì có giá trị khai thác (tra cứu bảo hành, hóa đơn doanh nghiệp, tài khoản web).',
    'DIACHIKHACH': 'Thông tin thành phần của hồ sơ khách, thuộc nhóm đối tượng ngoài; không có thời gian phát sinh.',
    'NHANVIEN': 'Con người thực hiện các nghiệp vụ; được ghi vào chứng từ. NgayVaoLam, NgayNghiViec chỉ là ngày ghi nhận hồ sơ.',
    'VAITRO': 'Danh mục ổn định do cửa hàng quy định, không có thuộc tính thời gian.',
    'TAIKHOAN': 'Không phải con người hay tổ chức; sinh ra khi khách đăng ký hoặc người quản trị cấp, có ThoiDiemTaoTK, số lượng tăng theo thời gian.',
    'NHACUNGCAP': 'Tổ chức giao hàng cho cửa hàng.',
    'MAGIAMGIA': 'Có thời hạn áp dụng (NgayBatDau, NgayKetThuc) và số lượt dùng nên xếp nghiệp vụ dù giống danh mục.',
    'GIOHANG': 'Phát sinh khi khách chọn hàng; có ThoiDiemTaoGio và dữ liệu tạm; số lượng tăng theo thời gian.',
    'DONHANG': 'Phát sinh mỗi lần bán; có ThoiDiemLap; số lượng tăng theo thời gian.',
    'NHATKYDONHANG': 'Phát sinh mỗi lần đổi tình trạng đơn; có ThoiDiemDoi.',
    'THANHTOAN': 'Phát sinh mỗi lần thu tiền; có ThoiDiemTT.',
    'PHIEUGIAO': 'Phát sinh khi xuất hàng đi giao; có ThoiDiemXuat.',
    'LANGIAO': 'Phát sinh mỗi lần thử giao; có ThoiDiemGiao.',
    'PHIEUNHAP': 'Phát sinh mỗi lần nhận hàng; có ThoiDiemNhan.',
    'HANGCOSERI': 'Phát sinh khi chiếc hàng được nhập; có ThoiDiemNhap; số lượng tăng theo thời gian.',
    'GIAODICHKHO': 'Phát sinh mỗi lần hàng vào hoặc ra kho; có ThoiDiemGD.',
    'HOSODOITRA': 'Phát sinh khi khách đề nghị đổi trả; có NgayDeNghi.',
    'LANNHANLAI': 'Phát sinh khi hàng trả về; có ThoiDiemNhanLai.',
    'KHOANHOAN': 'Phát sinh khi duyệt hoàn tiền; có ThoiDiemDuyetHoan.',
    'PHIEUBAOHANH': 'Phát sinh khi tiếp nhận sản phẩm lỗi; có NgayNhan.',
}
MOTA_MKH = {
    'CHITIETDONHANG': 'Đơn hàng – mặt hàng: số lượng, đơn giá, tên hàng và SKU đã chốt tại thời điểm bán; một mặt hàng có thể ở nhiều dòng của một đơn.',
    'CHITIETPHIEUNHAP': 'Phiếu nhập – mặt hàng: số lượng thực nhận và giá nhập.',
    'GIATRITHONGSO': 'Mặt hàng – thông số: giá trị của thông số đó ở mặt hàng.',
    'CHITIETTRA': 'Hồ sơ đổi trả – dòng đơn: số lượng trả và chiếc hàng trả (hàng có seri).',
    'GIUVAITRO': 'Nhân viên – vai trò: giữ từ ngày nào đến ngày nào và do ai phân vai trò.',
    'CHITIETGIOHANG': 'Giỏ hàng – mặt hàng: số lượng khách chọn; mỗi mặt hàng một dòng trong giỏ.',
}


def ents(loai):
    out = []
    for n in luoc_do.ORDER:
        if REL[n]['loai'] == loai:
            fk = {c for cols, p, pc in REL[n]['fks'] for c in cols}
            attrs = [a[0] for a in REL[n]['attrs'] if a[0] in REL[n]['pk'] or a[0] not in fk]
            out.append((n, attrs))
    return out


def main():
    w('# CHƯƠNG 1: TỔNG QUAN')
    w()
    w('## 1.1 KHẢO SÁT THỰC TRẠNG')
    w()
    w('PowerTech là cửa hàng bán lẻ linh kiện máy tính và thiết bị công nghệ: bộ vi xử lý, bo mạch chủ, bộ nhớ RAM, card đồ họa, ổ cứng, nguồn, '
      'vỏ máy, màn hình, bàn phím, chuột, tai nghe, thiết bị mạng, phụ kiện, phần mềm bản quyền, máy tính xách tay và máy tính bộ lắp sẵn. Cửa hàng '
      'bán theo hai cách cùng lúc: khách đến mua trực tiếp tại quầy của cửa hàng (có kho kèm theo), và khách mua trên trang web riêng của cửa hàng, '
      'nơi khách xem hàng, đăng ký tài khoản, chọn hàng vào giỏ rồi đặt hàng; ngoài ra cửa hàng còn nhận đơn qua điện thoại và tin nhắn. Cách vận hành '
      'tham khảo các cửa hàng linh kiện máy tính có cả điểm bán lẫn trang web bán hàng, nơi chính sách bảo hành, đổi trả, giao hàng được công bố công khai '
      '(ví dụ GearVN). Hàng chủ yếu nhập từ các nhà phân phối và đại lý chính hãng; việc bảo hành do hãng hoặc nhà phân phối thực hiện, cửa hàng là nơi bán, '
      'tiếp nhận sản phẩm lỗi, gửi đi bảo hành và trả lại cho khách.')
    w()
    w('Công việc của một cửa hàng như vậy gặp sáu khó khăn đặc thù khi chỉ ghi sổ tay hoặc bảng tính rời rạc:')
    w()
    w('1. **Hàng nhiều thông số, giá trị cao.** Mỗi loại linh kiện có thông số riêng và phải hợp với linh kiện khác (loại chân cắm bộ vi xử lý và bo mạch chủ, '
      'loại RAM, công suất nguồn). Nhiều mặt hàng có số seri riêng từng chiếc để hãng nhận biết khi bảo hành.')
    w('2. **Giá thay đổi thường xuyên.** Giá niêm yết, giá khuyến mãi và giá nhập đổi theo thị trường và từng đợt nhập; cửa hàng cần biết mỗi lần bán hoặc nhập đã dùng mức giá nào.')
    w('3. **Một kho cho nhiều kênh bán.** Hàng trong kho phục vụ khách mua tại quầy và khách đặt trên trang web, qua điện thoại; nếu không ghi nhận đơn đã nhận thì dễ bán trùng một món hàng cho hai người.')
    w('4. **Hàng đã mở hộp không bán lại như hàng mới.** Sản phẩm khách trả hoặc gửi bảo hành phải được kiểm tra trước khi quyết định bán lại, trả nhà cung cấp hay xử lý khác; '
      'ghi chép rời rạc dễ nhầm giữa hàng mới, hàng chờ kiểm tra và hàng lỗi.')
    w('5. **Bảo hành kéo dài và qua nhiều bên.** Thời hạn từ 12 đến 36 tháng với phần lớn mặt hàng, có loại 5 năm và nguồn máy đến 10 năm; sản phẩm gửi hãng mất vài ngày đến khoảng một tháng, '
      'cửa hàng phải biết sản phẩm của từng khách đang ở đâu và hẹn trả khi nào.')
    w('6. **Nhiều người cùng xử lý một chứng từ.** Nhân viên bán hàng, thu ngân, kho, giao hàng, kỹ thuật và quản lý cùng làm việc trên một đơn; khi có sai sót, tranh chấp hay thất thoát, '
      'cửa hàng phải biết ai đã làm, ai đã duyệt và lúc đó người ấy giữ vai trò gì. Ghi chép chung chung không trả lời được câu hỏi này.')
    w()
    w('Vì vậy lĩnh vực cần tin học hóa của đề tài là **quản lý hoạt động kinh doanh bán lẻ linh kiện máy tính và thiết bị công nghệ của PowerTech, gồm cả bán tại quầy lẫn bán trên trang web**: danh mục hàng hóa '
      'và thông số; hồ sơ khách hàng, tài khoản, sổ địa chỉ và giỏ hàng; nhân viên, vai trò và trách nhiệm từng khâu; nhà cung cấp; bán tại quầy và bán từ xa; thanh toán, đặt cọc, hoàn tiền; giao hàng; '
      'nhập hàng và theo dõi hàng trong kho theo tình trạng; đổi trả và bảo hành.')
    w()
    w('## 1.2 TÍNH KHẢ THI CỦA BÀI TOÁN')
    w()
    w('Quy mô một cửa hàng, một kho và số lượng chứng từ vừa phải (mỗi ngày vài chục đơn, vài chục dòng hàng) nên cơ sở dữ liệu quan hệ trên một máy chủ là đủ. '
      'Việc xây cơ sở dữ liệu có cấu trúc tốt giải quyết được các khó khăn nêu ở 1.1:')
    w()
    w('- Tách rõ hàng hóa, thông số, ảnh để thông số được lưu một lần cho mỗi mặt hàng, tìm theo thông số nhanh.')
    w('- Ghi giá tại thời điểm bán vào từng dòng đơn, đổi giá về sau không làm sai đơn cũ; giỏ hàng chỉ giữ lựa chọn tạm, giá chỉ chốt khi cửa hàng xác nhận đơn.')
    w('- Ghi mọi lần hàng vào ra kho theo nhóm (đủ điều kiện bán, chờ kiểm tra, chờ xử lý) để số lượng thực tế luôn tính lại được và hàng trả về không bị bán nhầm.')
    w('- Ghi số seri từng chiếc để truy vết nguồn nhập, người mua và các lần bảo hành, đổi trả.')
    w('- Ghi người thực hiện và người duyệt ở từng khâu, cùng nhật ký đổi tình trạng đơn và lịch sử vai trò của nhân viên, để khi có vấn đề tra được ai chịu trách nhiệm.')
    w('- Bảo đảm nhất quán dữ liệu (không dư thừa, không mâu thuẫn) nhờ chuẩn hóa; đó là trọng tâm của báo cáo này.')
    w()
    w('Về kỹ thuật, các kiến thức cần dùng (phụ thuộc hàm, khóa, dạng chuẩn, phân rã, đồ thị quan hệ) đều trong chương trình môn học; công cụ gồm SQL Server hoặc '
      'SQLite để cài đặt và kiểm tra truy vấn, và Graphviz để vẽ sơ đồ.')
    w()
    w('## 1.3 ĐỐI TƯỢNG SỬ DỤNG VÀ PHẠM VI')
    w()
    w('**Người sử dụng:** khách hàng (xem hàng, đăng ký tài khoản, giỏ hàng, đặt hàng trên trang web, tra cứu đơn); người quản trị (tạo tài khoản và phân vai trò cho nhân viên); '
      'người quản lý (duyệt hoàn tiền, quyết định bán lại hàng trả về); nhân viên tư vấn bán hàng; thu ngân kiêm thủ quỹ; nhân viên kỹ thuật (kiểm tra hàng, tiếp nhận bảo hành); nhân viên kho; '
      'nhân viên giao hàng; nhân viên chăm sóc khách hàng (tiếp nhận yêu cầu đổi trả, bảo hành). Cửa hàng nhỏ nên một người thường kiêm nhiều vai trò.')
    w()
    w('**Phạm vi đề tài** (giảng viên đã nhắc nhiều nhóm phải giới hạn chức năng, nên nhóm chọn nhóm nghiệp vụ cốt lõi và làm sâu):')
    w()
    w('- *Không gian:* một cửa hàng độc lập (một điểm bán kèm một kho); số lượng hàng theo dõi theo mặt hàng và theo nhóm tình trạng, chưa theo vị trí kệ hay nhiều chi nhánh.')
    w('- *Nghiệp vụ có trong mô hình:* danh mục hàng hóa, ảnh, thông số; khách hàng, tài khoản, sổ địa chỉ; nhân viên, vai trò và phân công vai trò; nhà cung cấp; giỏ hàng; bán tại quầy và từ xa (trang web, điện thoại, tin nhắn); '
      'mã giảm giá; nhật ký tình trạng đơn; thanh toán, đặt cọc, hoàn tiền; giao hàng; nhập hàng và số seri; sổ kho; đổi trả; bảo hành; ghi người thực hiện và người duyệt từng khâu.')
    w('- *Ngoài phạm vi:* kiểm kê kho và điều chỉnh tồn; điều chỉnh đơn sau khi chốt; giữ hàng cho đơn; bàn giao tiền thu hộ; trả hàng nhà cung cấp (gửi hãng); kế toán và công nợ; trả góp; bán buôn; khách hàng thân thiết; '
      'đánh giá sản phẩm; hỗ trợ khách bằng phiếu yêu cầu, trò chuyện hay bài hướng dẫn; thu mua thiết bị cũ và bán hàng cũ; ví và số dư tài khoản; thông báo cho khách; thống kê, biểu đồ doanh thu; cảnh báo tồn tối thiểu; '
      'lịch sử thay đổi giá; lắp ráp và cấu hình máy chi tiết; nhiều showroom; **quản lý nhân sự chuyên sâu (chấm công, lương, tuyển dụng)**; phân quyền chi tiết đến từng chức năng (đề tài chỉ dừng ở vai trò).')
    w()
    w('**Liên hệ với website PowerTech.** Đề tài lấy bài toán của website PowerTech (đồ án môn Lập trình web của cùng nhóm): website có các khu vực quản trị, bán hàng, kho, hỗ trợ, giao hàng và khách hàng. '
      'Báo cáo này làm phần cơ sở dữ liệu cho bán hàng (quầy và trang web), kho, đổi trả, bảo hành, tài khoản, vai trò và truy trách nhiệm; các phần phiếu hỗ trợ, đánh giá, thu cũ đổi mới và ví là của website '
      'nhưng nằm ngoài phạm vi báo cáo này. Một số quy tắc (số seri từng chiếc, đặt cọc, hồ sơ đổi trả, phiếu tiếp nhận bảo hành, nhật ký tình trạng đơn, phân công vai trò theo thời gian) '
      'là nghiệp vụ **nhóm đề xuất thêm** theo nhận xét của giảng viên và cách các cửa hàng thực tế vận hành, website hiện tại chưa có.')
    w()
    w('## 1.4 MÔ TẢ NGHIỆP VỤ')
    w()
    w('Phần này kể lại công việc của cửa hàng như người chủ cửa hàng mô tả, bằng lời đời thường, trả lời các câu hỏi thường gặp (thanh toán thế nào, có đặt cọc không, '
      'trả hàng tính phí ra sao, ai kiểm tra, ai duyệt, tối đa mấy lần).')
    w()
    w('### 1.4.1 Hàng hóa, ảnh và thông số kỹ thuật')
    w()
    w('Cửa hàng chia hàng theo loại hàng và thương hiệu. Các loại hàng có thể phân cấp, ví dụ nhóm lớn "Linh kiện máy tính" gồm các nhóm nhỏ "Bộ nhớ RAM", "Ổ cứng SSD"; '
      'mỗi loại chỉ có một loại cha. Hai loại hàng hay hai thương hiệu có thể trùng tên nên phải có mã riêng. Mỗi mặt hàng có một mã nội bộ và một mã hàng thương mại (SKU) không '
      'trùng mặt hàng nào khác, kèm tên, mô tả, giá niêm yết, giá khuyến mãi nếu đang áp dụng, thời hạn bảo hành tính theo tháng và tình trạng đang kinh doanh hay đã ngừng. '
      'Mỗi mặt hàng thuộc đúng một loại và một thương hiệu.')
    w()
    w('Mỗi mặt hàng có nhiều ảnh minh họa; vị trí ảnh trong cùng mặt hàng không trùng nhau và có một ảnh đại diện. Mỗi loại hàng quy định các thông số riêng '
      '(dung lượng, tốc độ, công suất, chuẩn kết nối); mỗi thông số có tên, kiểu giá trị (chữ, số, có/không) và đơn vị nếu có. Mỗi mặt hàng có tối đa một giá trị cho một thông số của loại hàng '
      'mình thuộc về. Thêm hoặc đổi ảnh không làm đổi thông số. Những mặt hàng có số seri riêng từng chiếc (bộ vi xử lý, bo mạch chủ, card đồ họa, ổ cứng, nguồn, màn hình, máy tính xách tay) '
      'được ghi số seri của từng chiếc khi nhập và khi bán; số seri chỉ chắc chắn không trùng trong cùng một mặt hàng. Cáp, tản nhiệt, phụ kiện nhỏ chỉ theo dõi theo dòng hàng.')
    w()
    w('### 1.4.2 Khách hàng, tài khoản và sổ địa chỉ')
    w()
    w('Khách mua tại quầy được đề nghị để lại họ tên và số điện thoại để tra cứu bảo hành khi mất phiếu; khách không để lại vẫn được bán hàng và khi cần bảo hành thì đối chiếu bằng chứng từ mua '
      'và số seri. Khách đặt từ xa và khách là doanh nghiệp cần hóa đơn (cung cấp mã số thuế) luôn có hồ sơ. Họ tên, số điện thoại hay email có thể trùng hoặc đổi nên không dùng để phân biệt hai khách. '
      'Cửa hàng hay tìm khách theo tên gọi nên ghi riêng họ lót và tên.')
    w()
    w('Khách mua trên trang web đăng ký một tài khoản bằng tên đăng nhập và mật khẩu; cửa hàng chỉ giữ mật khẩu đã mã hóa, không giữ mật khẩu gốc. Tên đăng nhập không trùng nhau; mỗi khách có tối đa một tài khoản. '
      'Tài khoản bị khóa khi vi phạm hoặc nghi lộ mật khẩu, khi đó khách không đặt hàng được. Khách đã mua tại quầy rồi mới đăng ký thì hồ sơ cũ chỉ được nối vào tài khoản sau khi khách xác nhận bằng mã gửi về đúng số điện thoại đã để lại; '
      'sau khi nối, khách xem được lịch sử mua và thời hạn bảo hành còn lại.')
    w()
    w('Khách có tài khoản lưu được nhiều địa chỉ nhận hàng; mỗi địa chỉ ghi tên người nhận, số điện thoại và địa chỉ chi tiết, và tại mỗi thời điểm chỉ có tối đa một địa chỉ mặc định. '
      'Khi đặt hàng, khách chọn một địa chỉ đã lưu hoặc nhập địa chỉ mới; địa chỉ được chép vào đơn nên đổi hoặc xóa địa chỉ về sau không sửa đơn cũ.')
    w()
    w('### 1.4.3 Nhân viên, vai trò và trách nhiệm')
    w()
    w('Mỗi nhân viên có hồ sơ gồm họ tên (ghi riêng họ lót và tên), số điện thoại, email nếu có, ngày vào làm và, nếu đã nghỉ, ngày nghỉ việc. Nhân viên nghỉ việc không bị xóa hồ sơ vì cửa hàng còn giữ chứng từ '
      'người đó đã lập hoặc duyệt. Cửa hàng có tám vai trò công việc: quản trị, quản lý, bán hàng, thu ngân, kỹ thuật, kho, giao hàng và chăm sóc khách hàng. Mỗi vai trò có tên chuẩn không trùng và mô tả công việc, quyền hạn. '
      'Cửa hàng nhỏ nên một người thường kiêm nhiều vai trò, và vai trò đổi theo thời gian (ví dụ một nhân viên chuyển từ kho sang bán hàng). Vì vậy cửa hàng ghi từng lần một người giữ một vai trò: từ ngày nào, đến ngày nào '
      '(chưa kết thúc thì để trống) và do người quản trị nào phân vai trò.')
    w()
    w('Nhân viên thao tác trên hệ thống bằng tài khoản riêng do người quản trị tạo; mỗi nhân viên có tối đa một tài khoản và mỗi tài khoản thuộc đúng một nhân viên hoặc đúng một khách. Nhân viên làm được những việc nào '
      'tùy các vai trò người đó đang giữ.')
    w()
    w('**Ai làm, ai duyệt.** Ở mỗi khâu quan trọng cửa hàng ghi lại người thực hiện và người duyệt để khi có sai sót hay tranh chấp thì biết ai đã làm và lúc đó người ấy giữ vai trò gì:')
    w()
    w('- Lập đơn tại quầy hoặc qua điện thoại, tin nhắn: nhân viên bán hàng. Đơn khách tự đặt trên trang web thì chưa có nhân viên cho đến khi nhân viên bán hàng xác nhận.')
    w('- Mỗi lần đơn đổi tình trạng (xác nhận, chuẩn bị, giao, hoàn tất, hủy): ghi ai đổi, lúc nào, lý do (bắt buộc khi hủy). Khách tự hủy đơn chưa xác nhận thì không có nhân viên.')
    w('- Nhận tiền: nhân viên xác nhận đã nhận (thu ngân hoặc bán hàng); với tiền thu khi giao hàng, còn ghi người giao đã thu.')
    w('- Giao hàng: nhân viên giao hàng. Nhập hàng: nhân viên kho lập phiếu và nhân viên kho xác nhận phiếu. Mỗi lần hàng vào ra kho ghi người thực hiện.')
    w('- Mã giảm giá: ghi nhân viên tạo mã (bán hàng hoặc quản lý).')
    w('- Đổi trả: nhân viên chăm sóc khách hàng tiếp nhận hồ sơ; nhân viên kỹ thuật kiểm tra hàng nhận lại; người quản lý duyệt chuyển nhóm hàng. Hoàn tiền: người quản lý duyệt, thu ngân chi tiền.')
    w('- Bảo hành: nhân viên kỹ thuật tiếp nhận và lập phiếu.')
    w()
    w('Chỉ người đang giữ đúng vai trò mới được làm khâu đó (ví dụ chỉ người quản lý duyệt hoàn tiền, chỉ người quản trị phân vai trò). Nhật ký và chứng từ không được sửa hay xóa sau khi ghi.')
    w()
    w('### 1.4.4 Bán hàng tại quầy')
    w()
    w('Khách đến cửa hàng được nhân viên tư vấn chọn linh kiện hoặc cấu hình phù hợp, có kiểm tra sự tương thích giữa các linh kiện. Khi khách đồng ý mua, nhân viên bán hàng lập một đơn ghi '
      'thời điểm bán, nhân viên bán, khách (nếu có) và từng dòng hàng: số thứ tự dòng, mặt hàng, số lượng, đơn giá bán thực tế, tên hàng và SKU lúc bán, kèm số seri với hàng có seri. '
      'Một mặt hàng có thể xuất hiện ở nhiều dòng nếu giá khác nhau (một chiếc bán giá khuyến mãi, một chiếc bán giá thường). Tổng tiền hàng bằng tổng tiền các dòng, trừ khoản giảm giá nếu có; '
      'tiền tính bằng đồng Việt Nam.')
    w()
    w('Khách trả tiền tại quầy thu ngân bằng tiền mặt, chuyển khoản qua mã QR ngân hàng hoặc thẻ ngân hàng. Nhân viên lấy hàng từ kho, kiểm tra ngoại quan và niêm phong trước mặt khách; máy tính xách tay, '
      'màn hình, máy tính bộ được bật chạy thử trước khi giao; linh kiện còn niêm phong chỉ mở hộp khi khách yêu cầu vì hàng đã mở hộp không bán lại như hàng mới. Nhân viên dán tem bảo hành, '
      'giao hàng cùng phiếu bán kiêm phiếu bảo hành. Giao dịch hoàn tất ngay tại quầy và hàng được trừ khỏi kho cùng lúc.')
    w()
    w('### 1.4.5 Bán hàng trên trang web, mã giảm giá và giao hàng')
    w()
    w('Khách xem hàng trên trang web không cần đăng nhập nhưng muốn đặt hàng phải đăng nhập bằng tài khoản. Khách chọn hàng vào giỏ: mỗi mặt hàng chỉ có một dòng trong giỏ, thêm lần nữa thì tăng số lượng; '
      'mỗi tài khoản chỉ có một giỏ đang dùng và có thể bỏ giỏ không đặt. Giỏ chưa chốt giá: giá hiện hành chỉ được chép vào đơn khi cửa hàng xác nhận đơn. Khi đặt hàng, khách chọn địa chỉ nhận hàng, cách thanh toán, '
      'nhập mã giảm giá nếu có; giỏ chuyển sang đã đặt hàng và đơn mới ở tình trạng chờ xác nhận. Khách cũng có thể đặt qua điện thoại hoặc tin nhắn, khi đó nhân viên bán hàng lập đơn thay.')
    w()
    w('Đơn mới ở tình trạng chờ xác nhận; khách tự hủy được khi cửa hàng chưa xác nhận. Nhân viên bán hàng kiểm tra hàng, gọi điện xác nhận hàng, địa chỉ '
      'và cách thanh toán; từ lúc xác nhận, tên hàng, giá và thông tin người nhận được chốt trên đơn, đổi giá hay địa chỉ về sau không sửa đơn cũ. Đơn đi qua các tình trạng: chờ xác nhận, đã xác nhận, đang chuẩn bị, đang giao, '
      'hoàn tất hoặc đã hủy; mỗi lần đổi tình trạng được ghi lại như ở 1.4.3.')
    w()
    w('Mỗi đơn dùng tối đa một mã giảm giá. Mã do một nhân viên tạo, thuộc một chương trình khuyến mãi, giảm theo phần trăm hoặc theo số tiền, có thời gian áp dụng, giá trị đơn tối thiểu, mức giảm tối đa và số lượt dùng tối đa; '
      'chỉ giảm trên tiền hàng, không giảm phí giao.')
    w()
    w('Với đơn cần giao, nhân viên kho lấy hàng, ghi số seri, niêm phong và bàn giao cho nhân viên giao hàng cùng một phiếu giao; mỗi đơn có tối đa một phiếu giao. Phí giao tính theo khu vực và giá trị đơn, '
      'đơn giá trị lớn nội thành thường được miễn phí; đơn nội thành giao trong 1 đến 2 ngày làm việc. Khách kiểm tra bên ngoài, niêm phong và số seri trước khi nhận; hộp rách, móp, ướt hoặc mất '
      'niêm phong thì khách có quyền từ chối nhận. Nếu khách vắng hoặc từ chối, người giao ghi lý do; **mỗi đơn được thử giao tối đa 3 lần**, sau 3 lần không thành công đơn bị hủy và hàng mang về kho. '
      'Khách bỏ đơn từ lần thứ hai trở đi chỉ được bán khi trả trước (đây là cách cửa hàng hạn chế khách đặt rồi bỏ).')
    w()
    w('### 1.4.6 Thanh toán, đặt cọc và hoàn tiền')
    w()
    w('Khách trả trước bằng chuyển khoản, mã QR, ví điện tử hoặc cổng thanh toán, hoặc trả khi nhận hàng. Một đơn có thể có nhiều lần thanh toán, kể cả cọc và phần còn lại; mỗi lần ghi phương thức, số tiền, thời điểm, '
      'kết quả, đơn vị thanh toán và người xác nhận. Chuyển khoản do nhân viên đối chiếu với đơn rồi mới xác nhận đã nhận tiền; lần chuyển không thành công không được tính là đã thu. Tiền thu khi giao hàng do người giao thu '
      'rồi nhân viên bán hàng hoặc người quản lý xác nhận; khoản thu ghi cả người giao đã thu. Đơn trả trước không thu đủ trong 24 giờ kể từ lúc xác nhận thì bị hủy và khoản đã thu được hoàn lại.')
    w()
    w('**Đặt cọc.** Hàng không có sẵn, hàng phải đặt từ nhà cung cấp, máy tính lắp theo yêu cầu riêng và một số mặt hàng giá trị lớn chỉ được giữ khi khách đặt cọc một phần giá trị. Mức cọc do hai bên thỏa thuận và '
      'ghi trên đơn; cửa hàng công bố điều kiện này trước khi nhận cọc. Tiền cọc được trừ vào tổng thanh toán khi nhận hàng. Nếu cửa hàng không có được hàng thì hoàn đủ tiền cọc; nếu khách tự hủy thì xử lý theo điều kiện đã ghi.')
    w()
    w('**Hoàn tiền.** Chỉ người quản lý được duyệt hoàn tiền, thu ngân chi tiền; cửa hàng ghi cả người duyệt, người chi và thời điểm từng bước. Mỗi khoản hoàn gắn với khoản thu gốc và có thể hoàn nhiều lần nhưng tổng không vượt số đã thu. '
      'Số tiền hoàn của một dòng hàng bằng giá đã trả của dòng đó trừ phần giảm giá đã chia cho dòng và trừ phí xử lý nếu có; tiền hoàn theo phương thức khách đã trả.')
    w()
    w('### 1.4.7 Nhập hàng và theo dõi hàng trong kho')
    w()
    w('Nhà cung cấp (nhà phân phối, đại lý chính hãng) có tên công ty, người liên hệ, số điện thoại, địa chỉ, mã số thuế và tình trạng hợp tác; một nhà cung cấp giao nhiều mặt hàng và một mặt hàng có thể nhập từ nhiều nhà cung cấp. '
      'Khi hàng về, nhân viên kho cùng người giao mở kiện, đối chiếu với đơn đặt và hóa đơn của nhà cung cấp, đếm số lượng, kiểm tra ngoại quan và ghi số seri hàng có seri. Nhân viên lập phiếu nhập: '
      'mỗi phiếu là một lần nhận hàng thực tế, có số phiếu không trùng, nhà cung cấp, người lập, thời điểm nhận và các dòng (mặt hàng, số lượng thực nhận, giá nhập). Cùng một mặt hàng có thể ở nhiều dòng nếu '
      'khác giá hoặc khác lô. Sau khi hai bên ký biên bản giao nhận, một nhân viên kho xác nhận phiếu (ghi người và giờ xác nhận) và hàng được ghi tăng vào kho **chỉ một lần**.')
    w()
    w('Cửa hàng chia hàng trong kho thành ba nhóm: *đủ điều kiện bán*, *chờ kiểm tra* và *chờ xử lý (không bán được)*; chỉ nhóm đủ điều kiện bán mới được bán. Mọi lần hàng vào hoặc ra kho (nhập, bán, '
      'nhận lại, chuyển nhóm) được ghi lại với mặt hàng, nhóm, số lượng, thời điểm, người thực hiện và chứng từ gốc; số lượng hiện có tính từ các lần ghi này chứ không ghi thành một con số riêng.')
    w()
    w('### 1.4.8 Đổi trả hàng')
    w()
    w('Cửa hàng áp dụng ba trường hợp: (1) *giao sai, thiếu, hư hỏng bên ngoài*: khách báo trong 48 giờ kể từ khi nhận, cửa hàng đổi lại hoặc hoàn tiền và chịu vận chuyển; (2) *sản phẩm lỗi do nhà sản xuất*: đổi mới '
      'trong 30 ngày kể từ ngày mua với linh kiện và gaming gear, trong 7 ngày với máy tính xách tay và màn hình, sản phẩm còn như mới và đủ phụ kiện; quá hạn thì xử lý theo bảo hành; (3) *khách đổi ý*: chỉ nhận lại trong 7 ngày '
      'nếu còn nguyên niêm phong, chưa mở hộp, đủ phụ kiện; khách chịu vận chuyển và có thể chịu một khoản phí xử lý theo thông báo niêm yết; phần mềm bản quyền đã kích hoạt không đổi trả.')
    w()
    w('Khách mang hóa đơn hoặc phiếu bán gốc đến (hoặc báo qua điện thoại, trang web); nhân viên kỹ thuật kiểm tra sản phẩm. Nếu được chấp nhận, nhân viên tiếp nhận lập hồ sơ đổi trả ghi đơn gốc, ngày, lý do và từng dòng hàng cùng số lượng trả; '
      'một đơn có thể được trả nhiều lần miễn tổng số lượng trả không vượt số đã giao. **Hàng nhận lại không bán ngay:** mọi sản phẩm nhận về vào nhóm chờ kiểm tra; kỹ thuật viên kiểm tra, người quản lý duyệt chuyển '
      'sang nhóm đủ điều kiện bán (còn nguyên niêm phong, không lỗi), hoặc để chờ xử lý (đã mở hộp hoặc lỗi thật); cửa hàng ghi cả người kiểm tra và người duyệt. Khách đổi sang sản phẩm khác thì lập đơn mới và tính chênh lệch; '
      'khách muốn hoàn tiền thì người quản lý duyệt.')
    w()
    w('### 1.4.9 Tiếp nhận và xử lý bảo hành')
    w()
    w('Bảo hành do hãng hoặc nhà phân phối chịu trách nhiệm theo thời hạn ghi trên mặt hàng; cửa hàng là đầu mối tiếp nhận. Thời hạn tính từ ngày mua theo chứng từ gốc và không đổi khi cửa hàng đổi chính sách về sau. '
      'Nhân viên kỹ thuật kiểm tra: còn trong thời hạn, có thông tin mua của cửa hàng, số seri khớp chứng từ, tem còn nguyên, sản phẩm không bị rơi vỡ, vào nước hay tháo sửa. Nếu đủ điều kiện, nhân viên lập phiếu tiếp nhận ghi '
      'sản phẩm và số seri, dòng mua gốc, mô tả lỗi, phụ kiện đi kèm, ngày nhận và ngày hẹn trả (thường 7 đến 30 ngày tùy hãng); nếu không, ghi lý do từ chối và trả lại cho khách. '
      'Mỗi bước (kiểm tra, gửi hãng, có kết quả, trả khách) được ghi vào phiếu. Chi phí sửa chữa và vận chuyển bảo hành do cửa hàng chịu. Nếu quá hạn hẹn mà chưa sửa được, hoặc đã bảo hành từ 3 lần mà lỗi còn, '
      'cửa hàng đổi sản phẩm tương tự hoặc thu hồi và hoàn tiền.')
    w()
    w('## 1.5 MỤC TIÊU NGHIÊN CỨU')
    w()
    w('Áp dụng kiến thức môn Cơ sở dữ liệu nâng cao để thiết kế, chuẩn hóa và đánh giá cơ sở dữ liệu cho PowerTech, theo đề cương bài tập lớn gồm bảy nội dung:')
    w()
    w('1. Mô tả tóm tắt bài toán cần quản lý (mục 1.1 đến 1.4).')
    w('2. Đề nghị cơ sở dữ liệu thích hợp: xác định ba loại thực thể và thuộc tính (mục 1.6, 1.7).')
    w('3. Xác định tập phụ thuộc hàm cho từng lược đồ quan hệ, phủ tối thiểu và khóa của từng lược đồ (mục 2.2).')
    w('4. Xác định dạng chuẩn từng lược đồ; lược đồ vi phạm dạng chuẩn 1, 2 (và 3, BCNF) thì phân rã hoặc tổng hợp để đạt dạng chuẩn cao hơn; kiểm tra bảo toàn thông tin và bảo toàn phụ thuộc hàm (mục 2.2, 2.3).')
    w('5. Tìm phụ thuộc đa trị để phân rã thành đa trị tầm thường, bảo đảm dạng chuẩn 4 (mục 2.3.8).')
    w('6. Xây dựng đồ thị quan hệ; nêu các con đường truy xuất và ngữ nghĩa của từng đường (mục 3.1, 3.2).')
    w('7. Viết các truy vấn SQL cho các truy xuất trên (mục 3.3).')
    w()
    w('Ngoài ra báo cáo đánh giá lược đồ theo ba tiêu chuẩn của giáo trình: nhất quán, dễ khai thác, không trùng lắp.')
    w()
    w('## 1.6 CÁC LOẠI THỰC THỂ')
    w()
    w('Theo giáo trình (13.2.3) và bài giảng, loại thực thể là đối tượng tồn tại độc lập, có giá trị lưu trữ và khai thác, có từ hai thể hiện trở lên, tên là danh từ. Có ba loại: **cơ bản** (nguồn tài nguyên có trước hệ thống, ổn định, '
      'thường không có thuộc tính thời gian), **đối tượng ngoài** (con người hoặc tổ chức) và **nghiệp vụ** (sinh ra khi vận hành, luôn có thuộc tính thời gian). Tên thuộc tính không trùng giữa các thực thể '
      '(HoTenKH và HoTenNV, ThoiDiemLap và ThoiDiemTT); khóa ngoại dùng đúng tên khóa chính của thực thể cha. Danh sách dưới đây ghi thuộc tính của từng thực thể, chưa kể khóa ngoại.')
    w()
    for idx, (title, loai, cap) in enumerate((('1.6.1 Cơ bản', 'co_ban', 'Các thực thể cơ bản'), ('1.6.2 Đối tượng ngoài', 'ngoai', 'Các thực thể đối tượng ngoài'),
                                              ('1.6.3 Nghiệp vụ', 'nghiep_vu', 'Các thực thể nghiệp vụ')), 1):
        w(f'### {title}')
        w()
        w('| Thực thể | Thuộc tính | Ý nghĩa | Lý do xếp loại |')
        w('|---|---|---|---|')
        for n, attrs in ents(loai):
            w(f'| {n} | {", ".join(attrs)} | {MOTA[n]} | {LY_DO[n]} |')
        w()
        w(f'*Bảng 1.{idx}: {cap}*')
        w()
    w('### 1.6.4 Mối kết hợp có thuộc tính')
    w()
    w('Dòng chi tiết là **mối kết hợp** giữa hai thực thể, không phải thực thể (giáo trình 13.2.3, nhận xét của giảng viên):')
    w()
    w('| Mối kết hợp | Thuộc tính riêng | Ý nghĩa |')
    w('|---|---|---|')
    RIENG = {'CHITIETDONHANG': ['SoDongDH', 'SoLuongBan', 'DonGiaChot', 'TenHangChot', 'SKUChot', 'ThoiHanBHChot'],
             'CHITIETPHIEUNHAP': ['SoDongPN', 'SoLuongNhap', 'GiaNhap'], 'GIATRITHONGSO': ['GiaTriTS'],
             'CHITIETTRA': ['SoDongTra', 'SoLuongTra', 'MaSeri'], 'GIUVAITRO': ['NgayBatDauVT', 'NgayKetThucVT', 'MaNVPhanCong'],
             'CHITIETGIOHANG': ['SoLuongGio', 'ThoiDiemThemGio']}
    for n in ('CHITIETDONHANG', 'CHITIETPHIEUNHAP', 'GIATRITHONGSO', 'CHITIETTRA', 'GIUVAITRO', 'CHITIETGIOHANG'):
        w(f'| {n} | {", ".join(RIENG[n])} | {MOTA_MKH[n]} |')
    w()
    w('*Bảng 1.4: Các mối kết hợp có thuộc tính*')
    w()
    w('### 1.6.5 Những điều không xếp thành thực thể')
    w()
    w('- **Tồn kho, tổng tiền đơn, doanh thu** là dữ liệu thống kê hoặc tính toán, không phải thực thể. Số lượng hàng trong kho tính từ GIAODICHKHO; tổng tiền đơn tính từ các dòng, giảm giá và phí giao.')
    w('- **Giới tính, tình trạng, kênh bán, phương thức thanh toán** chỉ là giá trị phân loại nên là thuộc tính có miền giá trị, không thành bảng riêng.')
    w('- **Khách hàng** vẫn là thực thể dù giáo trình nêu ví dụ bán lẻ không cần khách hàng: PowerTech cần tra cứu bảo hành, xuất hóa đơn doanh nghiệp và nhận đơn từ xa; khách vãng lai không có hồ sơ (MaKH rỗng).')
    w('- **Quyền hạn** không có bảng riêng: quyền của một nhân viên là quyền của các vai trò người đó đang giữ (GIUVAITRO); phân quyền đến từng chức năng nằm ngoài phạm vi. '
      '**Vai trò hiện tại** của nhân viên suy ra từ các lần giữ vai trò chưa kết thúc, không lưu thành cột riêng.')
    w('- **Tài khoản** xếp đối tượng ngoài (hồ sơ truy cập của khách và nhân viên) dù có thời điểm tạo, vì đó là ngày ghi nhận hồ sơ chứ không phải một lần giao dịch; **giỏ hàng** xếp nghiệp vụ vì phát sinh '
      'mỗi lần khách chọn hàng, dù là dữ liệu tạm.')
    w('- **Ca tranh luận:** MAGIAMGIA giống danh mục nhưng có thời hạn và số lượt dùng nên xếp nghiệp vụ; HANGCOSERI là từng chiếc hàng, phát sinh khi nhập kho nên xếp nghiệp vụ; ANHMATHANG phụ thuộc mặt hàng '
      'nhưng ổn định và không có thời gian nên xếp cơ bản.')
    w()
    w('## 1.7 MÔ HÌNH ERD (ENTITY – RELATIONSHIP DIAGRAM)')
    w()
    w('### 1.7.1 Phân tích mô hình ERD')
    w()
    w(f'Mô hình có **{len(erd.ENTITIES)} thực thể** (hình chữ nhật), **{len(erd.MKH)} mối kết hợp có thuộc tính** (oval xanh) và **' + str(len(erd.relationships())) + ' mối kết hợp** còn lại (oval cam) đặt tên bằng động từ. '
      'Bản số (min,max) đặt cạnh thực thể: số lần mỗi thể hiện của thực thể tham gia mối kết hợp. Ví dụ DONHANG (0,1) – Đặt – KHACHHANG (0,n): một đơn có tối đa một khách (khách vãng lai thì không), một khách có thể có nhiều đơn.')
    w()
    w('| Mối kết hợp | Thực thể | Bản số | Thực thể | Bản số |')
    w('|---|---|---|---|---|')
    for verb, child, parent, bc, bp, cols in erd.relationships():
        w(f'| {verb} | {erd.SHORT[child]} | {bc} | {erd.SHORT[parent]} | {bp} |')
    mk = erd.mkh_card()
    for n, (verb, ends) in erd.MKH.items():
        (a, ba), (b, bb) = mk[n]
        w(f'| {verb} ({erd.SHORT[n]}) | {erd.SHORT[a]} | {ba} | {erd.SHORT[b]} | {bb} |')
    w()
    w('*Bảng 1.5: Các mối kết hợp và bản số*')
    w()
    w('**Điều ERD không biểu diễn được bằng bản số** (ghi lại ở mục 2.1 và 2.3.6): (1) PHIEUGIAO chỉ lập cho đơn có giao (bản số (0,1) của DONHANG); (2) một đơn có ít nhất một dòng; '
      '(3) tổng hoàn tiền không vượt tiền đã thu; (4) hàng trả về chỉ chuyển nhóm sau khi người quản lý duyệt; (5) mặt hàng của chiếc hàng phải trùng mặt hàng của dòng nhập và dòng bán; '
      '(6) thông số của giá trị phải thuộc loại hàng của mặt hàng; (7) mỗi tài khoản thuộc đúng một khách hoặc đúng một nhân viên và chỉ tài khoản khách có giỏ hàng; '
      '(8) người thực hiện hoặc duyệt một khâu phải đang giữ vai trò phù hợp vào lúc đó (suy ra từ GIUVAITRO).')
    w()
    w('Bốn liên kết có một đầu là mối kết hợp (HANGCOSERI – CHITIETDONHANG, HANGCOSERI – CHITIETPHIEUNHAP, PHIEUBAOHANH – CHITIETDONHANG, CHITIETTRA – CHITIETDONHANG) '
      'là mối kết hợp *tổng hợp*: chiếc hàng, phiếu bảo hành hay dòng trả thuộc về một **dòng** của đơn hoặc phiếu nhập chứ không chỉ về cả đơn. '
      'Nhiều thực thể nối tới NHANVIEN bằng các mối kết hợp vai trò (lập, xác nhận, giao, duyệt, chi…); mỗi mối kết hợp cho biết **ai đã làm khâu đó**, là cơ sở truy trách nhiệm (mục 1.4.3).')
    w()
    w('### 1.7.2 Mô hình ERD')
    w()
    w('![Hình 1.1: Mô hình ERD tổng quát](hinh/erd_tong_quat.png)')
    w()
    w(f'*Hình 1.1: Mô hình ERD tổng quát ({len(erd.ENTITIES)} thực thể; tên mối kết hợp và bản số (min,max) ghi ở các hình theo nhóm bên dưới)*')
    w()
    for k, (ten, _) in erd.GROUPS.items():
        w(f'![Hình 1.{int(k) + 1}: ERD nhóm {ten}](hinh/erd_nhom{k}.png)')
        w()
        w(f'*Hình 1.{int(k) + 1}: ERD nhóm “{ten}”*')
        w()
    def fig(path, title):
        w(f'![{title}](hinh/{path}.png)')
        w()
        w(f'*{title}*')
        w()
    n_fig = len(erd.GROUPS) + 1
    w('## 1.8 PHÂN TÍCH CHỨC NĂNG (USE CASE)')
    w()
    w('Theo báo cáo mẫu, các chức năng được nhóm theo ba loại thực thể (đối tượng ngoài, danh mục cơ bản, nghiệp vụ) cùng hai nhóm chung là tìm kiếm và thống kê. Tác nhân **Nhân viên** là khái quát hóa của tám vai trò công việc '
      '(mục 1.4.3), mỗi vai trò chỉ làm những chức năng thuộc quyền của mình; tác nhân **Khách hàng** dùng trang web. Các chức năng nằm trong phạm vi ở mục 1.3.')
    w()
    for i, (k, ten) in enumerate((('tong_quat', 'Sơ đồ Use Case tổng quát'), ('doi_tuong_ngoai', 'Sơ đồ Use Case quản lý đối tượng ngoài'), ('danh_muc', 'Sơ đồ Use Case quản lý danh mục cơ bản'),
                                  ('nghiep_vu', 'Sơ đồ Use Case quản lý nghiệp vụ'), ('tim_kiem', 'Sơ đồ Use Case tìm kiếm'), ('thong_ke', 'Sơ đồ Use Case thống kê')), 1):
        fig(f'usecase_{k}', f'Hình 1.{n_fig + i}: {ten}')
    n_fig += 6
    w('## 1.9 LƯU ĐỒ CÁC QUY TRÌNH NGHIỆP VỤ')
    w()
    w('Bốn lưu đồ tóm tắt các quy trình có quy tắc dễ nhầm nhất, giúp đối chiếu với mô tả ở mục 1.4 và với các ràng buộc ở chương 2: vòng đời tình trạng đơn hàng, đổi trả, bảo hành và ba nhóm hàng trong kho.')
    w()
    for i, (k, ten) in enumerate((('luudo_don_hang', 'Lưu đồ tình trạng đơn hàng'), ('luudo_doi_tra', 'Lưu đồ đổi trả hàng, hoàn tiền'), ('luudo_bao_hanh', 'Lưu đồ tiếp nhận và xử lý bảo hành'),
                                  ('luudo_kho', 'Lưu đồ ba nhóm hàng trong kho')), 1):
        fig(k, f'Hình 1.{n_fig + i}: {ten}')
    out = os.path.join(HERE, '..', 'chuong', '01_chuong1.md')
    open(out, 'w', encoding='utf-8').write('\n'.join(OUT) + '\n')
    print('đã ghi', os.path.normpath(out))


if __name__ == '__main__':
    main()
