#!/usr/bin/env python3
"""Sinh chương 4 (chuong/04_chuong4.md) từ lược đồ và số liệu chương 3, để các con số luôn khớp.  Chạy sau gen_chuong3.py."""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import luoc_do

REL = luoc_do.REL
S3 = json.load(open(os.path.join(HERE, 'so_lieu_chuong3.json')))
OUT = []


def w(s=''):
    OUT.append(s)


def main():
    cnt = {k: sum(1 for r in REL.values() if r['loai'] == k) for k in ('co_ban', 'ngoai', 'nghiep_vu', 'mkh')}
    n_ent = cnt['co_ban'] + cnt['ngoai'] + cnt['nghiep_vu']
    n0, n1 = len(REL), len(luoc_do.ORDER_IMPROVED)
    w('# CHƯƠNG 4: KẾT LUẬN VÀ KIẾN NGHỊ')
    w()
    w('## 4.1 KẾT QUẢ ĐẠT ĐƯỢC')
    w()
    w('Đối chiếu với bảy nội dung của đề cương bài tập lớn:')
    w()
    w('| Nội dung đề cương | Kết quả | Mục |')
    w('|---|---|---|')
    w('| 1. Mô tả tóm tắt bài toán | Khảo sát, tính khả thi, đối tượng, phạm vi và mô tả nghiệp vụ bằng lời đời thường cho cả bán tại quầy lẫn bán trên trang web: tài khoản, nhân viên – chức vụ – trách nhiệm, thanh toán, đặt cọc, đổi trả, bảo hành | 1.1 – 1.4 |')
    w(f'| 2. Ba loại thực thể và thuộc tính | {n_ent} thực thể ({cnt["co_ban"]} cơ bản, {cnt["ngoai"]} đối tượng ngoài, {cnt["nghiep_vu"]} nghiệp vụ), {cnt["mkh"]} mối kết hợp có thuộc tính, ERD có bản số (min,max) | 1.6, 1.7 |')
    w(f'| 3. Phụ thuộc hàm và khóa từng lược đồ | {n0} quan hệ ban đầu, mỗi quan hệ có F, phủ tối thiểu 3 bước, khóa (N, TG, D), mọi khóa ứng viên | 2.2 |')
    w(f'| 4. Dạng chuẩn, phân rã/tổng hợp, bảo toàn | Lược đồ ban đầu chưa đạt 1NF; cải tiến 5 quan hệ, chứng minh bảo toàn thông tin (bảng a/b) và bảo toàn PTH; {n1} quan hệ đạt BCNF | 2.3 |')
    w('| 5. Phụ thuộc đa trị, dạng chuẩn 4 | Tình huống ảnh – thông số mặt hàng: R₂ đạt BCNF nhưng không đạt 4NF, tách thành ANHMATHANG và GIATRITHONGSO; 1.538 dòng so với 3.256 dòng trên dữ liệu seed | 2.3.8 |')
    w(f'| 6. Đồ thị quan hệ, con đường truy xuất, ngữ nghĩa | {S3["nodes"]} nút, {S3["arcs"]} cung, {S3["entry"]} nút vào, {S3["paths"]} con đường truy xuất dài và bảng ngữ nghĩa các đường cơ bản | 3.1, 3.2 |')
    w(f'| 7. Truy vấn SQL cho các truy xuất | {S3["paths"]} câu truy vấn cho {S3["paths"]} đường và {S3["k"]} truy vấn khai thác (có truy trách nhiệm theo nhân viên và chức vụ), đã chạy thử trên dữ liệu minh họa | 3.3 |')
    w()
    w('*Bảng 4.1: Đối chiếu kết quả với đề cương bài tập lớn*')
    w()
    w('## 4.2 ƯU ĐIỂM')
    w()
    w(f'- Lược đồ cuối đạt BCNF ở cả {n1} quan hệ, giữ nguyên quy tắc nghiệp vụ “số seri duy nhất trong cùng mặt hàng” nhờ phương án tách bốn thành phần bảo toàn cả thông tin lẫn phụ thuộc hàm.')
    w('- Một mô hình phục vụ cả hai kênh: khách mua tại quầy và khách mua trên trang web (tài khoản, đơn) dùng chung đơn hàng, thanh toán, kho, đổi trả và bảo hành.')
    w('- **Truy được trách nhiệm:** mỗi khâu quan trọng ghi người thực hiện hoặc duyệt (lập đơn, thu tiền, giao hàng, nhập kho, nhận lại hàng, hoàn tiền, bảo hành), kèm chức vụ của người đó (truy vấn K6–K8).')
    w('- Mọi phép tính (bao đóng, phủ tối thiểu, khóa, dạng chuẩn, bảo toàn, đồ thị) được trình bày từng bước và đối chiếu bằng chương trình; số liệu trong báo cáo sinh từ cùng một nguồn nên không mâu thuẫn.')
    w('- Giữ giá và tên hàng tại thời điểm bán trong từng dòng đơn, không lưu tồn kho thành cột, nên các dị thường cập nhật phổ biến của bán lẻ được loại bỏ.')
    w('- Truy vết được một chiếc hàng từ nhà cung cấp, phiếu nhập, đơn bán, đổi trả đến bảo hành bằng các con đường truy xuất đã xác định.')
    w()
    w('## 4.3 HẠN CHẾ')
    w()
    w('- Nhiều phụ thuộc hàm là giả thiết nghiệp vụ nhóm tự đặt (G1–G6) vì chưa có số liệu vận hành thật của cửa hàng; dữ liệu mẫu không chứng minh được phụ thuộc hàm.')
    w('- Kết luận 4NF cho các quan hệ ngoài tình huống ảnh – thông số dựa trên mô tả nghiệp vụ, chưa chứng minh tổng quát.')
    w('- Quy tắc đặt tên của thuộc tính kép (họ lót và tên) là quy ước nhập liệu, không kiểm tra được bằng phụ thuộc hàm.')
    w('- Quy tắc “đúng chức vụ mới được làm khâu đó” (duyệt hoàn tiền, chi tiền, xác nhận phiếu nhập…) là giả thiết nghiệp vụ của nhóm và chỉ cưỡng chế được khi ghi dữ liệu, không bằng khóa hay phụ thuộc hàm.')
    w('- Một số ràng buộc nhất quán liên quan hệ (mục 2.3.6) cần cài đặt bằng khóa ngoại ghép, kiểm tra khi ghi hoặc trigger; quy ước dấu của sổ kho chưa chốt với cửa hàng.')
    w('- Dữ liệu minh họa chỉ có vài chục dòng, đủ để kiểm tra truy vấn chạy đúng chứ không đủ để đánh giá hiệu năng; báo cáo chưa đo hiệu năng và các chỉ mục ở mục 3.4 mới là đề xuất.')
    w('- Phạm vi giới hạn (mục 1.3): một cửa hàng, một kho; chưa có đơn đặt hàng và trả hàng nhà cung cấp, kiểm kê và chuyển kho, hóa đơn điện tử, theo dõi chiếc hàng thay thế khi bảo hành đổi mới, giữ hàng, công nợ, trả góp, giỏ hàng, sổ địa chỉ, nhật ký tình trạng đơn, hỗ trợ khách bằng phiếu yêu cầu, đánh giá, thu cũ đổi mới, ví, thống kê; quản lý nhân sự chỉ dừng ở hồ sơ, chức vụ và truy trách nhiệm trên chứng từ, chưa có lịch sử giữ vai trò, chấm công, lương, tuyển dụng.')
    w()
    w('## 4.4 HƯỚNG PHÁT TRIỂN')
    w()
    w(f'- Cài đặt lược đồ {n1} quan hệ trên SQL Server, bổ sung ràng buộc toàn vẹn (kể cả ràng buộc chức vụ – khâu) và bảng tầm ảnh hưởng, thủ tục và khung nhìn báo cáo (doanh thu, tồn kho theo kỳ, trách nhiệm theo nhân viên).')
    w('- Mở rộng phạm vi theo website PowerTech: phiếu yêu cầu hỗ trợ, đánh giá sản phẩm, thu cũ đổi mới, ví; thêm đơn đặt hàng nhà cung cấp, kiểm kê định kỳ, chuyển kho, nhiều kho hoặc showroom, công nợ nhà cung cấp, trả hàng nhà cung cấp, kết nối hóa đơn điện tử, trả góp.')
    w('- Mở rộng quản lý nhân sự: chấm công, ca làm, lương theo doanh số; phân quyền đến từng chức năng.')
    w('- Đo hiệu năng các truy vấn theo con đường truy xuất trên dữ liệu thật và điều chỉnh chỉ mục.')
    w('- Xác nhận các giả thiết G1–G6 với cửa hàng thực tế và cập nhật phụ thuộc hàm nếu quy tắc thay đổi (ví dụ chuyển sang “seri duy nhất toàn cửa hàng”).')
    out = os.path.join(HERE, '..', 'chuong', '04_chuong4.md')
    open(out, 'w', encoding='utf-8').write('\n'.join(OUT) + '\n')
    print('đã ghi', os.path.normpath(out))


if __name__ == '__main__':
    main()
