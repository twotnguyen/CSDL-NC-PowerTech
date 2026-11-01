Một số khái niệm:

* Q(A1, A2, …, An): Q là tên table, Ai là các thuộc tính.
* Q+: là tập tất cả các thuộc tính của Q.
* ||Q||: Tân từ. Mô tả ngữ nghĩa của bảng Q.
* q: 1 bộ (tube) <=> 1 dòng, 1 mẫu tin, 1 record trong CSDL
* Siêu khóa (super key): là tập các thuộc tính mà khi biết giá trị của nó, có thể suy ra các giá trị còn lại.

VD: SV(HoLot, Ten, NTNS, Phai, DT, DiaChi, Hinh, CCCD)

Siêu khóa là gì? Super Key

SK1: DT

SK2: HoLot, Ten, NTNS, Phai, DT, DiaChi

SK3: Hinh

Một table có thể có nhiều Siêu khóa. Khi cài đặt trong SQL, Mongo, SQLite… ta chọn 1 SK làm khóa chỉ định => Đó chính là Primary Key. Ưu tiên PK có ít thuộc tính nhất, đơn giản nhất.

* Phép chiếu: ΠX(Q) hay Q[X], với Q là tên table.

VD: ΠMSSV(SV) hay SV[MSSV] lấy ra MSSV của toàn bộ table SV. Phép chiếu <=> lệnh gì trong SQL?

select distinct

* Phép chọn: Lọc ra các mẫu tin thỏa điều kiện.

VD: ΠX(Q):(Điều kiện)) hay QĐiều\_kiện[X]

ΠMSSV,HoTen(SV):(Diem>=8) hay QDiem>=8[MSSV, HoTen]

<=> lệnh gì trong SQL? where

HĐH:

Samsung, Xaomi, Oppo… => Android

iOS, Windows Home.

SQL Server, SQLite (MacOS), PostGre, MySQL

Maria, MongoDB

=> Tạo bảng:

**SV**(HoLot, Ten, NTNS, Phai, DT, Email, DiaChi, Hinh…)

=> Tạo bảng, khóa là gì? Ko có khóa dc ko?

Siêu khóa là: HoLot, Ten, NTNS, Phai, DT

Hay: HoLot, Ten, NTNS, Phai, Emai

… => Dài, mất time tìm kiếm => Ưu tiên ngắn gọn, ít tốn bộ nhớ.

=> Đưa và MSSV.

* Phụ thuộc hàm (FD: functional dependency): X -> Y (Y phụ thuộc vào X hay X suy ra Y)

Tìm khóa: Q(A,B,C,D) và F={f1, f2…}

Ta tính qua tất cả các bao đóng (closure):

A, B, C, D; AB, AC, AD, BC, BD; CD; ABC, ABD, ACD; BCD; ABCD; ∅. Có 24 bao đóng. Ta có tất cả các siêu khóa. Trong đó, siêu khóa nào bé nhất => Chọn làm khóa chính.

![](data:image/png;base64...)

Ta có: {AB}+F = {AB C(f1) D(f3) E(f4) F(f5) D(f2)}={ABCDEF}

VD: Cho R(U) với U = {A,B,C,D,E,G,H},

F = {B 🡪 A, DA 🡪 CE, D 🡪 H, GH 🡪 C, AC 🡪 D}. Hãy tìm tất cả các khóa của R.

Giải: N={B,G}, M={A,C,D,H}

|  |  |  |  |
| --- | --- | --- | --- |
| ACDH | Mi | Ki = N ∪ Mi | {Ki}+F |
| 0000 | ∅ | BG | BG A |
| 0001 | H | **BGH** | BGH ACDE = R+ |
| 0010 | D | **BGD** | BGD ACEH = R+ |
| 0011 | DH | BGDH | BGDH ACE = R+ |
| 0100 | C | **BGC** | BGC ADEH = R+ |
| 0101 | CH | BGCH | BGCH ADE = R+ |
| 0110 | CD | BGCD | BGCD AEH = R+ |
| 0111 | CDH | BGCDH | = R+ |
| 1000 | A | BGA | BGA |
| 1001 | AH | BGAH | BGAH CDE = R+ |
| 1010 | AD | BGAD | BGAD CEH = R+ |
| 1011 | ADH | BGADH | = R+ |
| 1100 | AC | BGAC | BGAC DEH = R+ |
| 1101 | ACH | BGACH | = R+ |
| 1110 | ACD | BGACD | BGACD EH = R+ |
| 1111 | ACDH | BGACDH | = R+ |

Về nhà tính xem có bao nhiêu siêu khóa. Chỉ ra khóa chính.

Có 14 siêu khóa. Trong đó {BGH}, {BGD} và {BGC} là 3 siêu khóa bé nhất. Vậy R có 3 khóa. Khi cài đặt, ta chọn 1 trong 3 làm PK.

--Ôn tập: BA/DBA/DA/Tester

1, Có bao nhiêu loại thực thể (trong môn PTTKHT)/loại quan hệ (trong môn CSDL) => Cả 2, khi cài đặt trong hệ quản trị CSDL, nó chính là Table?

- Trả lời: Có 3 loại:

1/ Cơ bản: Là nguồn tài nguyên của hệ thống, có tính ổn định cao. Nó có trước khi hệ thống được tin học hóa. Thường ko có thuộc tính thời gian, nếu có thì là ngày sinh, ngày tạo ra, ngày đưa vào sử dụng. SL thường cố định và ít thay đổi theo thời gian.

Ví dụ:

QL Học tập: Phòng học, Môn học.

Quản lý bán hàng: Sản phẩm/Mặt hàng, Loại hàng

2/ Đối tượng ngoài: Là Con người hay Tổ chức.

Ví dụ:

QL Học tập: SV, GV (con người), Khoa/Viện/Phòng ban (tổ chức)…

Quản lý bán hàng: Khách hàng, NV (con người)… Tổ chức: Phòng ban…

3/ Nghiệp vụ: Được sinh ra khi hệ thống đưa vào vận hành, luôn có thuộc tính thời gian. SL mẫu tin tăng dần theo thời gian.

Ví dụ:

QL Học tập: Phiếu đăng ký MH (có ngày ĐK), Bảng điểm (Ngày in)…

Quản lý bán hàng: Hóa đơn (ngày bán), Phiếu nhập hàng (ngày nhập)…

=> Ví dụ tổng hợp: Hãy xác định 3 loại thực thể của bài Quản lý Thư viện.

+ Loại tt cơ bản: Sách, Thể loại, => CV(MACV, TenCV, PCCV)

+ Loại tt đối tượng ngoài: Độc giả, NV, NXB, Thủ thư (1 CV)…

=> NV(<u>MSNV</u>, HoTen, Phai, NTNS, CV(Thủ thư, QL sách. PGĐ, GĐ…))

+ Loại tt nghiệp vụ: PhieuMS, PhieuTra, PhieuPhat, TheĐG, PhieuNopLP…

Sau khi xác định 3 loại thực thể, ta tiếp tục xác định các thuộc tính của từng loại thực thể. Tiếp theo là xđ các PTH trên từng loại thực thể.

1. Phụ thuộc hàm là gì? Tại sao với mỗi loại thực thể/loại quan hệ, ta cần phải tìm tập Phụ thuộc hàm?

+ PTH (functional dependency): là các quy tắc do hệ thống quy định.

Vd: Biết Họ tên, NTNS, Phái của 1 NV thì ta sẽ biết quê quán, nơi sinh và hình ảnh của NV đó.

1. Khóa là gì? 1 bảng ko có Khóa được ko?

Ta tìm Khóa bằng cách nào? => Dựa vào tập PTH.

--Phủ tối tiểu (minimal cover):

1. VD1: F = (f1, f2)

Với f1={AB->C} và f2={A->C) => f1 thừa B.

2. F = (f1, f2, f3)

f1={A->B}, f2={B->C}, f3={A->C}

Thừa f3 từ f1 và f2, do bắc cầu ta suy ra được f3.

Về nhà:

![](data:image/png;base64...)

![](data:image/png;base64...)

3 bước:

+B1: Vế phải của F chỉ chứa 1 thuộc tính.

F = {AB->C, AB->D, B->C, C->D}

+B2: F chỉ chứa các PTH đầy đủ (Ko thừa vế trái).

AB->C: thừa B vì đã có B->C

AB->D và B->D (bắc cầu): thừa B

Vậy: G = {A->C, A->D, B->C, C->D}

Các PTH có vế trái là 1 thuộc tính => Đầy đủ.

+B3: Loại bỏ các PTH dư thừa.

Bỏ: A->D do bắc cầu => G = {A->C, B->C, C->D}

Vậy G là 1 phủ tối tiểu của F.

VD2: Hãy tìm PTT của F = {AB->C, A->B, B->C, B->A}

--Giải:

+B1: Vế phải chỉ có 1 tt => thỏa.

+B2: Loại PTH ko đầy đủ (thừa vế trái). Chỉ xét các PTH có vế trái chứa từ 2 tt trở lên.

Xét AB->C: thừa B vì đã có B->C.

G={A->C, A->B, B->C, B->A}

+B3: Bỏ các PTH dư thừa.

Thừa A->C vì đã có A->B và B->C.

G1={A->B, B->C, B->A} là 1 PTT của F.

+ Cách khác: G={A->C, A->B, B->C, B->A}

+B3: Bỏ B->C vì đã có B->A và A->C.

G2={A->C, A->B, B->A} là 1 PTT khác của F.

--Dạng chuẩn (Normal Form):

+DC1: Thuộc tính đơn.

Chuyen\_Mon (MaGV, Mon)

![Screen Clipping](data:image/png;base64...)

Viết lệnh SQL in ra mỗi GV có thể dạy được bao nhiêu môn?

select MaGV, count(Mon) as [Số môn]

from Chuyen\_Mon

MaGV | Số môn

GV001 1

GV002 1

GV003 1

select MaGV, count(Mon) as [Số môn]

from Chuyen\_Mon

group by MaGV => In ra kết quả giống như trên

select MaGV, count(disdinct Mon) as [Số môn]

from Chuyen\_Mon => In ra kết quả giống như trên

VD khác:

SV(MSSV, HoTen)

=> Đếm xem có bao nhiêu SV tên là ‘Mỹ’.

select count(\*)

from SV

where HoTen like N‘%Mỹ’

=> Đếm xem có bao nhiêu SV có họ lót là ‘Hoàng’.

select count(\*)

from SV

where HoTen like N‘%Hoàng%’

=> Vi phạm DC1: thuộc tính HoTen là đa trị (bao gồm Họ+Lót+Tên)

Sửa: SV(MSSV, HoLot, Ten) => Các tt là đơn, thỏa DC1.

+DC2: Mọi tt không khóa phải phụ thuộc đầy đủ vào khóa (ko phụ thuộc 1 phần).

VD: KetQua(MSSV, MAMH, TenMH, Diem)

F={f1: MSSV->TenMH, Diem; f2: MAMH->TenMH}

=> Khóa K={MSSV, MAMH}

Đạt DC1, đạt DC2 không? Không. Vì:

TenMH là tt không khóa phụ thuộc vào MAMH (f2) là 1 phần của khóa.

+DC3: Ko tồn tại PTH bắc cầu vào khóa.

VD: KetQua(MSSV, MAMH, TenMH, Diem)

F={f1: MSSV,MAMH->Diem; f2: MSSV, MAMH->TenMH}

=> Khóa K={MSSV, MAMH}. Đạt DC1, DC2. Đạt DC3 vì ko có bắc cầu.

VD khác: R(A, B, C, D) có F={AB->C, C->D}. Đạt DC mấy, tại sao?

Khóa K={AB}

DC1: đạt. DC2: đạt (C->D có C ko nằm trong khóa)

DC3: ko vì AB->D do bắt cầu qua C.

Sửa để đạt DC3:

R1(A, B, C) có F1={AB->C} => Đạt DC3

R2(C,D) có F2={C->D} => Đạt DC3

Vậy cả LĐ đạt DC3.

DC3 là DC tối thiểu của LĐ CSDL.

--Bài tập:

1/ Cho lược đồ quan hệ Q(A,B,C,D) và tập phụ thuộc hàm F={AB→C; B→D; BC→A}. Hỏi Q có đạt chuẩn 2 không?

Có 2 khóa: K1={AB}, K2={BC}.

+Xét K1: Đạt DC1. Ko đạt DC2 do B->D: D là tt ko khóa, phụ thuộc vào B là 1 phần của khóa.

+Xét K2: Đạt DC1. Ko đạt DC2 do B->D: D là tt ko khóa, phụ thuộc vào B là 1 phần của khóa.

Vậy Q chỉ đạt DC1.

2/ Quan hệ sau đạt chuẩn mấy?
Q(G,M,V,N,H,P) F={G→M; G→N; G→H; G→P; M→V; NHP→M}

Khóa K={G}. Đạt DC1, DC2 (khóa chỉ có 1 tt).

DC3: Ko đạt do G->M mà M->V => G->V.

3/ Cho lược đồ quan hệ Q(A,B,C,D) F={AB→C; D→B; C→ABD}. Hỏi Q có đạt chuẩn 3 không?

Khóa là K={C}: đạt DC1, DC2 (khóa có 1 tt).

DC3: đạt (ko có bắc cầu).

DCBC: Ko đạt vì AB→C; D→B là 2 PTH có vế trái ko chứa khóa.

4/ Q(A,B,C,D,E,I) F={ACD→EBI; CE→AD}. Hỏi Q có đạt chuẩn BC không?

Khóa là: có 2 khóa nhưng chọn K1 do bé nhất. K1={CE}.

Xét ACD→EBI: ta có C là 1 phần của khóa (ko chứa khóa) => Ko đạt DCBC.

5/ Cho Q(ABCD) với F={A->B, B->C, C->D}. Đạt DC mấy? DC2.

--Về nhà coi trước DC4.

--Kiểm tra phân rã bảo toàn PTH và bảo toàn thông tin:

![](data:image/png;base64...)

Giải:

1. Q1(AB) với F1={∅}; Q2(ACD) với F2={A->C, C->A, D->C};

Q3(BCD) với F3=(D->C)

b- Kiểm tra tính bảo toàn PTH:

- Đặt F’ = (∪Fi) = (A->C, C->A, D->C)

-![](data:image/png;base64...)

+ Ta cần chứng minh:

1/ ∀f’ ∈ (F’ \ F) thì f’ ∈ F+:

Ta có: F’ \ F = (A->C, C->A, D->C) \ (A->C, C->A, D->C, BD->A) = {∅}

∀f’ ∈ {∅} thì f’ ∈ F+: hiển nhiên => Đúng.

và

2/ ∀f ∈ (F \ F’) thì f ∈ F’+:

Ta có: F = (F \ F’) = (A->C, C->A, D->C, BD->A) \ (A->C, C->A, D->C) = (BD->A)

∀f ∈ (BD->A): f ∈ F’+ với F’+ = (A->C, C->A, D->C)+ = (A->C, C->A, D->C, D->A). f ko thuộc F’+ nên ko thỏa.

Thỏa 1. mà ko thỏa 2. nên phân rã ko bảo toàn PTH.

--BTTT: Phân rã sau có BTTT ko?

![](data:image/png;base64...)

=> Xét BTTT xem sao?

Kẻ bảng có 4 cột chính (do Q có 4 thuộc tính), 4 dòng chính (do có 3 phân ra Q1, Q2, Q3).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| T | A | B | C | D |
| Q1 | a1 | a2 | b1 | b2 |
| Q2 | a1 | b3 | a3 | a4 |
| Q3 | b4 => a1 | a2 | a3 | a4 |

Chọn 2 dòng Q2 và Q3 để biến đổi (vì Q3 chỉ có 1 ô a1 chứa b, ít nhất). Ta cần xđ PTH nào mà có vế phải là Y={A}, vế trái X cần chứa {C} hoặc {D} (vì nó chứa ‘a’).

- Xét PTH: C->A của Q. Xét dòng Q2, ta có C->A với giá trị a3->a1, dòng Q3 có a3->b4 nên biến ‘b4’ thành ‘a1’.

Vậy Q3 có dòng chứa toàn ‘a’ nên phân rã đã cho BTTT.

+ Xét VD khác:

![](data:image/png;base64...)

+ Các PTH chiếu lên từng phân rã Qi:

Q1(CD, MSSV) với F1={∅}; Q2(CD, MSCD) với F2={f1, f2};

Q3(MSSV, HG) với F3={∅}

+ Chọn Q1 để biến đổi:

Tại Q2: chọn f2: CD->MSCD, b1 thành a1.

Chọn Q2: ko có PTH tương thích

Chọn Q3: ko có PTH tương thích

Ko có cặp Qi, Qj nào để biến giá trị b2 của Q1 thành a4.

=> KL: ko bảo toàn thông tin

+ VD khác:

1. Cho Q(ABCD) và F = {B 🡪 C; D 🡪 C; BD 🡪 B}

Xét phân rã Q1(AB); Q2(BCD); Q3(ACD).

a/ Tìm các phụ thuộc hàm được chiếu trên từng quan hệ, suy ra các khóa của các quan hệ con.

b/ Chứng minh lược đồ phân rã trên không bảo toàn thông tin.

Giải:

a/ Q1(AB) với F1={∅}; Q2(BCD} với F2={B 🡪 C; D 🡪 C; BD 🡪 B};

Q3(ACD) với F3={D 🡪 C}.

Khóa: Q1 có khóa K1={AB}: do ko có PTH nên tất cả các thuộc tính đều là Nguồn.

Q2 có khóa K2={BD}: dùng thuật toán tím tất cả các khóa;

Q3 có khóa K3={AD}, ta đưa A vào vì A ko nằm trong tập PTH => Ta xem nó là Nguồn. Nguồn thì phải nằm trong Khóa (do thuật toán tìm Khóa).

b/ Ta kẻ bảng có 5 cột, 4 dòng.

Q1(AB) với F1={∅}; Q2(BCD} với F2={B 🡪 C; D 🡪 C; BD 🡪 B};

Q3(ACD) với F3={D 🡪 C}.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| T | A | B | C | D |
| Q1 | a1 | a2 | b1 | b2 |
| Q2 | b3 | a2 | a3 | a4 |
| Q3 | a1 | b4 | a3 | a4 |

Chọn Q3 để biến đổi (vì dòng này chỉ chứa 1 ô b4). Ko có dòng nào thỏa.

Chọn Q2 để biến đổi.

F = {B 🡪 C; D 🡪 C; BD 🡪 B}

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| T | A | B | C | D |
| Q1 | a1 | a2 | b1 =>a3 | b2 |
| Q2 | b3 | a2 | a3 | a4 |
| Q3 | a1 | b4 | a3 | a4 |

\* Cách 1:

Chọn dòng Q1 để biến đổi (ta muốn biến đổi b1, b2 thành a3 và a4).

Chọn PTH B->C: Xét 2 dòng Q1 và Q2. Tại Q2, có a2->a3 thõa B->C nên ta thay b1 ở Q1 thành a3.

Ko có PTH nào mà vế phải chứa D nên ko thể biến b2 thành a4.

\* Cách 2:

Chọn dòng Q1 để xét: PTH D->C ko thể chọn 2 dòng Q để biến đổi vế phải thành ‘a’. Q2 và Q3 thõa D->C nhưng vế phải C đã là ‘a3’ nên ko xét được.

Phân rã ko BTTT.

\* Cách 3:

Chọn PTH BD->B: ko có dòng nào thỏa để biến đổi.

Phân rã ko BTTT.

=> KL: Phân rã đã cho không BTTT.

--BTVN:

Cho Q(ABCD) có F = {B 🡪A; B 🡪 D; A 🡪C; C 🡪 D}

Gọi C = {Q1(AB); Q2(BD); Q3(AC)}

a) Tìm các PTH chiếu trên các quan hệ con:

Q1(AB) với F1={B 🡪A}; Q2(BD) với F2={B 🡪 D}; Q3(AC) với F3={A 🡪C}

b) C có bảo toàn phụ thuộc hàm hay không?

Giải:

a/ Ta cần chứng minh:

1/ ∀f’ ∈ (F’ \ F) thì f’ ∈ F+:

F’ = (∪Fi) = (B 🡪A, B 🡪D, A 🡪C)

Ta có (F’ \ F) = (B 🡪A, B 🡪D, A 🡪C) \ (B 🡪A; B 🡪 D; A 🡪C; C 🡪 D)

= {∅}

∀f’ ∈ {∅} thì f’ ∈ F+: thỏa.

2/ ∀f ∈ (F \ F’) thì f ∈ F’+:

Ta có: F \ F’ = (B 🡪A; B 🡪 D; A 🡪C; C 🡪 D) \ (B 🡪A, B 🡪D, A 🡪C)

= (C 🡪 D)

∀f ∈ (F \ F’) tức ∈ (C 🡪 D) thì f ∈ F’+: tức f phải ∈ (B 🡪A, B 🡪D, A © => Ko thỏa => Ko bảo toàn PTH.

**--Chuẩn hóa LĐ bằng phương pháp phân rã, tổng hợp và tổng hợp cải tiến.**

Xét ví dụ sau:

Có nhóm SV làm ĐACN liên quan đến Logictis. Nhóm đã tạo ra 1 LĐQH sau:

**Q(MsKH, TP, CTyVC, MsHH, SL)**

+ Mô tả: MsKH: Mã số Khách hàng. TP: Thành phố của nhà cung cấp. CtyVC: Công ty vận chuyển hàng. MsHH: Mã hàng hóa. SL: Số lượng.

Nhóm đã phân tích và xác định được tập phụ thuộc hàm như bên dưới:

F = {f1: MsKH→TP; f2: MsKH→CTyVC;

f3: MsKH, MsHH→SL; f4: TP→CtyVC}

Yêu cầu:

1. Hãy xác định khóa của lđ trên.
2. Từ tập khóa tìm được, cho biết lđ đạt DC mấy? Giải thích.

Bảng Q có nhập liệu được ko? Có vấn đề gì gặp phải? **TP, CTyVC lặp nhiều lần => Mất thời gian nhập.**

1. Nếu lđ chưa đạt DC tối thiểu để cài đặt. Hãy dùng các thuật toán đã học để cải tiến cho lđ đạt DC cao hơn (có thể cài đặt và sử dụng).

Giải:

Khóa là: {MsKH, MsHH}

Đạt dạng chuẩn 1, không đạt dạng chuẩn 2 vì: f1 có vế trái là 1 phần của Khóa.

\* Cách 1: Dùng thuật toán Phân rã:

Giải:

F = {f1: MsKH→TP; f2: MsKH→CTyVC;

f3: MsKH, MsHH→SL; f4: TP→CtyVC}

+B1: Loại bỏ các pth có VT ∪ VP = Q+ khỏi F:

=> Bỏ f3. Vì f3: (MsKH, MsHH ∪ SL)=Q+.

= {MsKH, MsHH, SL}+F = Q+.

F\* = F \ {f3 ∈ F: VT(f) ∪ VP(f) = Q+ = {f1, f2, f4}

+B2: Nếu F\* = ∅ thì C = C ∪ {Q} và kết thúc {Điểm dừng}

F\* = {f1, f2, f4} <> ∅ => thực hiện phân rã:

+ B2.1:Chọn f: X → A ∈ F: Nên chọn PTH gây xấu cho lược đồ.

Chọn f4 (có vế trái ko nằm trong khóa => dê dẫn tới vi phạm DC3 (bắc cầu)).

+ B2.2: Phân rã thành 2 lđ con:

<Q1+ = {X, A}, F1 = {f ∈ F+: VT(f) ∪ VP(f) ⊆ Q1+}>

Q1(TP, CtyVC), F1 = {f4: TP→CtyVC}

<Q2+ = Q+ \ A, F2={f ∈ F+: VT(f) ∪ VP(f) ⊆ Q2+}>

Q2(MsKH, TP, MsHH, SL), F2 = {f1, f3} (bỏ f2: MsKH→CTyVC)

+B2.3: Phân rã đệ qui Q1 và Q2 (lặp lại từ Bước 1):

\*B1: - Xét Q1: Q1 có F1 = {f4: TP→CtyVC}

F\* = F1 \ {f ∈ F: VT(f) ∪ VP(f) = Q1+} = F1 \ {f4} = ∅

Vì F\* = ∅ => Dừng.

- Xét Q2: Q2(MsKH, TP, MsHH, SL), F2 = {f1, f3}

F\* = F2 \ { f ∈ F: VT(f) ∪ VP(f) = Q2+} = F2 \ {f3} = {f1}

F\* = {f1} <> ∅, tiếp tục phân rã:=> Phân rã đệ quy Q2: tức là thực hiện B1, B2 và B3.

+B1: Chọn PTH có VT(f) ∪ VP(f) = Q2+.

+B2.1: Chọn Chọn f: X→A ∈ F2, ta chọn f1 (duy nhất)

+B2.2: Phân rã thành 2 lđ con:

Q21(MsKH,TP) với F21 = {f1: MsKH→TP}

Q22 = Q2 \ {TP} = Q22(MsKH, MsHH, SL)

với F22 = {f3: MsKH, MsHH→SL}

+B2.3: Tiếp tục phân rã đện quy Q22.

\*B1:

- Xét Q21: Chọn f=f1. F\* = F21 \ {f1} = ∅ => Dừng.

- Xét Q22: Chọn f=f3. F\* = F \ {f3} = ∅ => Dừng.

Dừng vì F\* của Q21 và Q22 = ∅ .

Vậy Q ban đầu được phân rã thành:

Q = {Q1(TP, CtyVC) với F1={f4},

Q21(MsKH, TP) với F21 = {f1} và

Q22(MsKH, MsHH, SL) với F22 ={f3}.

Cả Q1, Q21 và Q22 đều đạt DCBC nên Q đạt DCBC.

KL: Ban đầu Q đạt DC1, sau khi phân rã thì Q đạt DCBC.

\* Cách 2: Dùng thuật toán Tổng hợp:

F = {f1: MsKH→TP; f2: MsKH→CTyVC;

f3: MsKH, MsHH→SL; f4: TP→CtyVC}

\*B1. Tìm Phủ tối thiểu của FQ. PTT thực hiện 3 bước:

b1. Phân rã các PTH có vế phải chỉ chứa 1 thuộc tính.

Thỏa.

b2. Thay thế bằng các PTH ko đầy đủ bằng các PTH đầy đủ (ko dư thừa vế trái).

Ta xét các PTH có vế trái từ 2 thuộc tính trở lên => xem nó dư thừa thuộc tính nào?

- Xét f3: f3: MsKH, MsHH→SL. Có dư MsKH hay MsHH ko?

Ko dư.

b3. Loại bỏ các PTH dư thừa.

- Bỏ f2: vì f1 và f4 bắc cầu.

F = {f1: MsKH→TP; ~~f2: MsKH→CTyVC~~;

f3: MsKH, MsHH→SL; f4: TP→CtyVC}

\*B2. Chia PTT thành những nhóm Fi. Mỗi nhóm Fi chứa các pth có cùng vế trái.

Ghi chú: Vế trái của mỗi Fi, được ký hiệu Ki, là siêu khóa của quan hệ con tương lai.

\*B3. Gộp các Fi có vế trái phụ thuộc lẫn nhau lại thành một nhóm.

Ví dụ: Fi chứa các pth có vế trái là Ki;

Fj chứa các pth có vế trái là KJ;

Nếu Ki → Kj và Kj → Ki thì gộp Fi và Fj thành 1 nhóm.

- Ở bài này ko có.

B4. Tạo các quan hệ con Qi từ các nhóm pth Fi đã tạo ở B3.

- Tạo 3 lđ con:

Q1(MsKH, TP) với F1 = {f1: MsKH→TP};

Q2(MsKH, MsHH, SL) với F2 = {f3: MsKH, MsHH→SL};

Q3(TP, CtyVC) với F3 = {f4: TP→CtyVC}.

Q1, Q2, Q3 đạt DCBC nên lđ đạt DCBC.

Nhận xét: PP Phân rã và Tổng hợp cho ra kết quả giống nhau.

\* Cách 2: Dùng thuật toán Tổng hợp cải tiến:

Từ phương pháp tổng hợp, ta thêm vào 2 bước nhằm bảo toàn thông tin:

\*B5. Tìm tập khóa (K) của quan hệ Q ban đầu

\*B6. Nếu không tồn tại Qi chứa khóa của Q ban đầu thì thêm vào CSDL C một quan hệ Q’(Ki) chứa một khóa Ki của Q ban đầu.

--

KQ ban đầu là {MsKH, MsHH}.

\*B5: Xét Q1, Q2, Q3 có chứa khóa K ban đầu ko? Có Q2 với f3.

\*B6: Ko làm.

Ta cần chứng minh thêm nó bảo toàn thông tin, bảo toàn PTH (Về nhà làm)

+ Ch/m bảo toàn PTH:

1/ ∀f’ ∈ (F’ \ F) thì f’ ∈ F+:

F’ = (∪Fi) = {F1, F21, F22} =

{f4: TP→CtyVC; f1: MsKH→TP, f3: MsKH, MsHH→SL}

Ta có (F’ \ F) = {∅}

∀f’ ∈ {∅} thì f’ ∈ F+: thỏa.

2/ ∀f ∈ (F \ F’) thì f ∈ F’+:

F \ F’={f2: MsKH→CTyVC}

∀f’ ∈ {f2: MsKH→CTyVC} thì f’∈ F+ (f1, f2, f3, f4) : ko thõa (chỉ có f2).

KL: Ko bảo toàn PTH.

+ Ch/m bảo toàn thông tin: Về nhà làm.

--

Chuẩn hóa LĐ bằng PP tổng hợp:
Xét quan hệ Q(MSCD, MSSV, CD, HG (Hạng))

Tập phụ thuộc hàm từ tân từ trên như sau:

FQ = {f1: MSCD → CD; f2: CD → MSCD; f3: CD, MSSV → HG;

f4: MSCD,HG → MSSV; f5: CD,HG → MSSV; f6: MSCD,MSSV → HG}

Xác định 1 phân rã theo thuật toán Tổng hợp.

+B1: Tìm PTT của FQ:

PTT = {f1, f2, f3, f4}. Ta bỏ f5 do suy ra từ f2 và f4 (do bắc cầu giả), bỏ f6 do suy ra từ f1 và f3 (do bắc cầu giả).

(Lưu ý: Ta có thể bỏ các PTH khác =. Kết quả ra sẽ khác nhau. Cái nào có DC tốt nhất, bảo toàn PTH và bảo toàn thông tin thì ta chọn)

+B2: Các PTH fi không cùng vế trái => Có 4 nhóm ứng với f1, f2, f3, f4.

|  |  |
| --- | --- |
| F1 | f1: MSCD → CD |
| F2 | f2: CD → MSCD |
| F3 | f3: CD, MSSV → HG |
| F4 | f4: MSCD,HG → MSSV |

+B3: Gom các Fi có vế trái phụ thuộc lẫn nhau.

|  |  |
| --- | --- |
| F12 | f1: MSCD → CD; f2: CD → MSCD (f1 và f2 phụ thuộc lẫn nhau) |
| F3 | f3: CD, MSSV → HG |
| F4 | f4: MSCD,HG → MSSV |

+B4: Tạo các quan hệ con Qi từ các F'i:

**Q12**(MSCD, CD),
F1 = {f1: MSCD → CD; f2: CD → MSCD}

**Q2**(CD, MSSV, HG),
F2 = {f3: CD, MSSV →HG}

**Q3**(MSCD, HG, MSSV)

F4 = {f4MSCD, HG → MSSV}

--

PP tổng hợp phân rã:

Q12, Q2, Q3 có chứa khóa ban đầu ko? Về nhà làm

--Bài tập:

Ví dụ 1: Cho LĐQH u=<Q,F> với Q=(abc), F= {a → b, b → c}

u ở dạng chuẩn mấy? Nếu u chưa BCNF hãy phân rã để được các LĐQH ở BCNF?

Giải: K={a}, đạt DC2 vì vi phạm DC3 (bắc cầu).

+ Thuật toán phân rã:

Giải:

+B1: Loại bỏ các pth có VT ∪ VP = Q+ khỏi F:

=> Bỏ f1.

F\* = F \ {f ∈ F: VT(f) ∪ VP(f) = Q+}

+B2: Nếu F\* = ∅ thì C = C ∪ {Q} và kết thúc {Điểm dừng}

F\* = F \ {f1} = {f2} <> ∅. Với F = {f1, f2}.

thực hiện phân rã:

+ B2.1:Chọn f: X → A ∈ F: Nên chọn PTH gấy xấu cho lược đồ.

Chọn f2.

+ B2.2: Phân rã thành 2 lđ con:

<Q1+ = {X, A}, F1 = {f1 ∈ F+: VT(f) ∪ VP(f) ⊆ Q1+}>

Q1(b, c), F1 = {f2: b→c}

<Q2+ = Q+ \ A, F2={f ∈ F+: VT(f) ∪ VP(f) ⊆ Q2+}>

Q2(a, b), F2 = {f1}

+B2.3: Phân rã đệ qui Q1 và Q2 (lặp lại từ bước 2.1):

- Xét Q1: Vì F\* = ∅ => Dừng.

- Xét Q2: Vì F\* = ∅ => Dừng.

Vậy Q = (Q1, Q2), với Q1(b, c) và Q2(a, b). Cả Q1, Q2 đều đạt DCBC nên Q đạt DCBC.

--Về nhà làm:

Ví dụ 2: Cho LĐQH u=<Q,F> với Q=(abcd), F= {a → b, b → c}

u ở dạng chuẩn mấy? Nếu u chưa BCNF hãy phân rã để được các LĐQH ở BCNF?

--

Ví dụ 3: Chuẩn hóa bằng pp tổng hợp.

Q(ABCD), F= {f1: A → C; f2: C → A;

f3: BC → D; f4: AD → B;

f5: CD → B; f6: AB → D}

Hãy chuẩn hóa bằng pp tổng hợp.

Giải:

B1. Tìm Phủ tối thiểu (PTT) của F.

3 bước:

+b1: vế phải của các PTH chỉ chứa 1 thuộc tính => Thỏa.

+b2: thay thế các PTH ko đầy đủ bằng cách PTH đầy đủ (ko thừa vế trái).

=> Ta chỉ xét các PTH có vế trái từ 2 thuộc tính trở lên.

Cụ thể, ta xét: f3: BC → D; f4: AD → B; f5: CD → B; f6: AB → D.

Xét f3: xem có dư B (tự B suy ra D): hay C (tự C suy ra D) ko? Ko thừa B hay D.

Xét f4: Ko thừa A. Ko thừa D.

Xét f5: Ko thừa C, D.

Xét f6: Ko thừa A, B.

+b3: loại bỏ các PTH dư thừa (do bắc cầu/phân rã…)

Từ f2 và f4, ta suy ra f5 => Dư thừa f5.

Từ f1 và f3, ta suy ra f6 => Dư thừa f6.

Vậy: F= {f1: A → C; f2: C → A; f3: BC → D; f4: AD → B}

B2. Chia PTT thành những nhóm Fi. Mỗi nhóm Fi chứa các pth có cùng vế trái.

Ghi chú: Vế trái của mỗi Fi, được ký hiệu Ki, là siêu khóa của quan hệ con tương lai.

Nhận xét: Có 4 nhóm vì các PTH ko có vế trái giống nhau.

|  |  |
| --- | --- |
| F1 | f1: A→ C |
| F2 | f2: C → A |
| F3 | f3: BC → D |
| F4 | f4: AD → B |

B3. Gộp các Fi có vế trái phụ thuộc lẫn nhau lại thành một nhóm.

Ví dụ: Fi chứa các pth có vế trái là Ki;

Fj chứa các pth có vế trái là Kj;

Nếu Ki → Kj và Kj → Ki thì gộp Fi và Fj thành 1 nhóm.

Vậy ta gom thành 2 nhóm.

F1, F2 có vế trái phụ thuộc lẫn nhau => gom thành 1 nhóm.

F3, F4 có vế trái phụ thuộc lẫn nhau => gom thành 1 nhóm.

|  |  |
| --- | --- |
| F12 | f1: A→ C; f2: C → A |
| F34 | f3: BC → D; f4: AD → B |

B4. Tạo các quan hệ con Qi từ các nhóm pth Fi đã tạo sau B3:

Q12(A,C) với F1 = {f1: A→ C; f2: C → A} => Khóa là {AC}. Đạt DC3?

Q34(A,B,C,D) với F2 = {BC → D; f4: AD → B}

=> Khóa là K1 = {ABC}, K2 = {ACD} => DC1

Cả LĐCSDL đạt DC1.

Kết thúc.

--PP tổng hợp cải tiến:

+ B5. Tìm tập khóa (K) của quan hệ Q ban đầu

+ B6. Nếu không tồn tại Qi chứa khóa của Q ban đầu thì thêm vào CSDL C một quan hệ Q’(Ki) chứa một khóa Ki của Q ban đầu.

Q(ABCD), F= {f1: A → C; f2: C → A;

f3: BC → D; f4: AD → B;

f5: CD → B; f6: AB → D}

Xét bài trên: Khóa K ban đầu là K1={AB}, K2={BC}, K3={AD}, K4={CD}.

Lần lượt xét 4 khóa, vì Q34 chứa thuộc tính các khóa nên ko cần tạo lđ mới chứa khóa.

**BÀI TẬP**

Cho một quan hệ phổ quát liên quan đến ứng dụng quản lý bán hàng của một công ty:

Q(MAKH, TENKH, MAHD, NGAYHD, MAHG, TENHG, SOLG, DG)

Với tập phụ thuộc hàm

FQ = {MAKH 🡪 TENKH; MAHG 🡪 TENHG; TENHG 🡪 MAHG;

MAHD 🡪 MAKH, NGAYHD; MAHD, MAHG 🡪 SOLG, DG}

**Yêu Cầu:**

1. Hãy đánh giá dạng chuẩn của quan hệ Q.

Khóa K = {MAHG, MAHD}

LĐ đạt DC1

1. Xác định một lược đồ CSDL khác đạt dạng chuẩn cao nhất. (dùng cả 3 phương pháp: phân rã, tổng hợp, tổng hợp cải tiến)

**Cách 1: Phân rã**

+B1:

+B1: Loại bỏ các pth có VT ∪ VP = Q+ khỏi F:

Xét MAHD,MAHG → SOLG,DG ta có VT ∪ VP = Q+ => Loại.

F\* = F \ {f ∈ F: VT(f) ∪ VP(f) = Q+} = {MAKH 🡪 TENKH; MAHG 🡪 TENHG; TENHG 🡪 MAHG; MAHD 🡪 MAKH, NGAYHD}

+B2: Nếu F\* = ∅ thì C = C ∪ {Q} và kết thúc {Điểm dừng} => Ko thỏa

Thực hiện phân rã:

+ B2.1: Chọn f: X → A ∈ F: Nên chọn PTH gấy xấu cho lược đồ (vế trái ko chứa khóa). Chọn MAKH 🡪 TENKH.

+ B2.2: Phân rã thành 2 lđ con:

<Q1+ = {X, A}, F1 = {f1 ∈ F+: VT(f) ∪ VP(f) ⊆ Q1+}>

Q1(MAKH, TENKH), F1 = {MAKH 🡪 TENKH}

<Q2+ = Q+ \ A, F2={f ∈ F+: VT(f) ∪ VP(f) ⊆ Q2+}>

Q2(MAKH, MAHD, NGAYHD, MAHG, TENHG, SOLG, DG),

F2 = {MAHG 🡪 TENHG; TENHG 🡪 MAHG; MAHD 🡪 MAKH, NGAYHD}

+b1: Ko có

+b2: F\* = F2 \ {∅} = F2

+b2.1: Chọn TENHG 🡪 MAHG (gây xấu cho lđ)

Q21(TENHG, MAHG) với F21={TENHG->MAHG}=>Dừng

Q22(MAKH, MAHD, NGAYHD, TENHG, SOLG, DG)

Với F22={MAHG->TENHG; MAHD 🡪 MAKH, NGAYHD}

Tiếp tục phân rã Q22:

+b1: Ko có

+b2: F\* = F22 (giữ nguyên)

+b2.1: Chọn PTH gây xấu cho lđ. 2 PTH chứa 1 phần của khóa => Tương đương nhau, chọn cái nào cũng được.

Chọn MAHG->TENHG.

+b2.2:

Q221(MAHG, TENHG), F221={MAHG->TENHG}

Q222(MAKH, MAHD, NGAYHD, SOLG, DG),

F222={MAHD 🡪 MAKH, NGAYHD}

+b2.3: Phân rã đệ uy Q222

+b1: Ko có

+b2: F\* = F222

+b2.1: Chỉ còn 1 PTH mà thôi.

Chọn MAHD 🡪 MAKH, NGAYHD.

+b2.2:

Q2221(MAHD, MAKH, NGAYHD),

F2221={MAHD 🡪 MAKH, NGAYHD}

Q2222(MAHD, SOLG, DG) (lđ vô nghĩa)

F2222={∅}

+b2.3:

Phân rã đệ quy Q2221.

+b1: Chọn f={MAHD 🡪 MAKH, NGAYHD} F\* = {∅} => Dừng

Phân rã đệ quy Q2222.

+b1: Ko còn PTH nào.

F\* = {∅} => Dừng

Kết luận:

Q = (Q1(MAKH, TENKH) với F1 = {MAKH 🡪 TENKH};

Q21(TENHG, MAHG) với F21={TENHG->MAHG};

Q221(MAHG, TENHG) với F221={MAHG->TENHG};

Q2221(MAHD, MAKH, NGAYHD)

với F2221={MAHD 🡪 MAKH, NGAYHD});

Q2222(MAHD, SOLG, DG) với F2222={∅})

**Cách 2: Tổng hợp**

+B1: Tìm PTT của FQ:

FQ = {MAKH 🡪 TENKH; MAHG 🡪 TENHG; TENHG 🡪 MAHG;

MAHD 🡪 MAKH, NGAYHD; MAHD, MAHG 🡪 SOLG, DG}

=> PTT(FQ) = {} làm 3 bước…

+B2: Chia PTT thành những nhóm Fi…

+B3: Gom nhóm

+B4: tạo quan hệ con

**Cách 3: Tổng hợp cải tiến**

+B5:

+B6: