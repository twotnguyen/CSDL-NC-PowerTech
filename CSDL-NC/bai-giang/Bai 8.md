# Bài 8 — Bài tập phương pháp chuẩn hóa

> Bản chuyển lại từ `Bai 8.ppt` (8 slide) thay cho `Bai 8.md`. Ký hiệu Wingdings/Symbol đã đổi về Unicode; chỉ số dưới/trên suy từ ngữ cảnh. `⟨?XX⟩` = ký hiệu chưa đọc được. `[BẢNG]` = ô bảng chép theo thứ tự trong file, cần xếp lại theo slide gốc.

---

## Slide 1

**BÀI 8**

- BÀI TẬP PP CHUẨN HÓA:
  - PHÂN RÃ, TỔNG HỢP
- (yêu cầu SV làm ở nhà và  thay nhau sửa trên lớp)

## Slide 2

- Bài tập 1:
- Cho Q(ABCD) và F = {A → C; D → C; BD → A}
- Xét phân rã Q₁(AB); Q₂(ACD); Q₃(BCD).
- a) Tìm các khóa và dạng chuẩn của Q
- b) Tìm các phụ thuộc hàm được chiếu trên từng quan hệ, suy ra các khóa của các quan hệ con.
- c) Lược đồ CSDL sau khi phân rã ở dạng chuẩn mấy?
- d) Lược đồ phân rã trên có bảo toàn thông tin không?
- e) Lược đồ phân rã trên có bảo toàn PTH không?

## Slide 3

- Bài tập 2
- Cho một quan hệ quản lý bán hàng của một công ty:
- Q(MAKH,TENKH,MAHD,NGAYHD,MAHG,TENHG,SOLG,DG)
- Với tập phụ thuộc hàm
- FQ ={MAKH → TENKH; MAHG → TENHG; TENHG → MAHG;
      - MAHD → MAKH, NGAYHD; MAHD, MAHG → SOLG, DG}
- Yêu Cầu:
      - a) Hãy đánh giá dạng chuẩn của quan hệ Q.
      - b) Xác định một lược đồ CSDL khác đạt dạng chuẩn BCNF.

## Slide 4

- Bài tập 3
- Xét LĐQH Q(MsKH, TP, CTyVC, MsHH, SL)
- MsKH: Mã số Khách hàng. TP: Thành phố của nhà cung cấp. CtyVC: công ty vận chuyển hàng. MsHH: mã hàng hóa. SL: số lượng.
- F = {f1: MsKH → TP, CTyVC; f2: MsKH, MsHH → SL; f3: TP → CtyVC}
- Xác định khóa của quan hệ.
- Xác định dạng chuẩn của quan hệ.
- Có thể tách quan hệ trên thành các quan hệ nào để lđcsdl đạt dạng chuẩn BCNF.

## Slide 5

- Bài tập 4
- Cho LĐQH Q=(CV, VP, CĐ, SL, CP, L). và
- FQ = {f1:CP → L; f2: CĐ → CV; f3: CĐ,CP → SL; f4: CV → VP}
- a) Xác định khóa của quan hệ.
- b) Xác định phân rã đạt dạng chuẩn BC, bảo toàn thông tin và PTH.
- c) Xét phân rã: C₁ = {⟨Q₁(CĐ, CP, SL, L), F₁={f1; f3}⟩,
      - ⟨Q₂(CĐ, CV, VP), F₂={f2; f4}⟩}
      - c1) Chỉ ra những trùng lắp thông tin của phân rã trên
      - c2) Chỉ ra những bất tiện trong quá trình khai thác CSDL trên.
- d) Xét phân rã: C₂ = {⟨Q₁(CP, CĐ, VP), F₁= ∅⟩,
      - ⟨Q₂(CP, CĐ, SL), F₂= {f3}⟩, ⟨Q₃(CĐ, CV), F₃={f2}⟩,
      - ⟨Q₄(CP, L), F₄= {f1}⟩}
      - C₂ có bảo toàn thông tin và bảo toàn phụ thuộc hàm không?

## Slide 6

- Bài tập 5
- Cho Q(Tàu, LoạiTàu, VậnChuyển, LôHàng, Cảng, Ngày)
- FQ = {T → L; VC → T, LH; T, N → C, VC}
- a) Xác định phân rã C bảo đảm 3 điều kiện BT PTH, BTTT và đạt dạng chuẩn 3.
- b) Cho C₁ = {Q₁(T, N, C, VC); Q₂(VC, LH); Q₃(T, L)}.
      - C₁ đạt những tiêu chuẩn gì (BTTT? BTPTH? DC mấy)
- Bài tập 6
- Cho Quan hệ Thoi_khoa_bieu_LT(MLOP, MGV, MAMON, PHONG, STC_LT, THU, CA, NGAY_BD, NGAY_KT)
- a) Xác định các phụ thuộc hàm theo quy tắc quản lý thời khóa biểu dạy lý thuyết.
- b) Lược đồ quan hệ trên đạt dạng chuẩn mấy? Nếu không đạt dạng chuẩn 3 hãy đề xuất CSDL đạt dạng chuẩn 3 trở lên và bảo toàn quy tắc quản lý theo như phân tích ban đầu.

## Slide 7

(slide trống hoặc chỉ có hình)


## Slide 8

- Kiểm tra giữa kỳ
- nộp bài lên classroom lúc 9h00
- (Các bạn nộp bài trễ sẽ bị trừ điểm)

