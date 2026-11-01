Cho cơ sở dữ liệu (CSDL) sau: Q1(A,D), Q2(B,E,G), Q3(A,B,G,H), Q4(C,M), Q5(B,C,N,A)

a) CSDL trên có trùng lắp thông tin không? giải thích?

b) Hãy vẽ đồ thị quan hệ của CSDL đã cho?

Giải:

a) Trùng lắp thông tin tại thuộc tính G của Q2 và Q3.

b)

+B1: C là phân rã đồng nhất.

+B2: Tạo nút và quan hệ nút: Có 5 nút.

+B3: Tạo nút bản lề và quan hệ (nút) bản lề:

Q1 với Q2: Ko có.

Q1 ∩ Q3 = {A} (Chỉ tính Khóa). Vì đã có Q1 chứa A => Ko tạo nút bản lề.

Q2 ∩ Q3 = {B}. Vì đã có Q2 chứa B => Ko tạo nút bản lề.

Q2 ∩ Q5 = {B}. Vì đã có Q2 chứa B => Ko tạo nút bản lề.

Q3 ∩ Q5 = {B}. Vì đã có Q2 chứa B => Ko tạo nút bản lề.

Q4 ∩ Q5 = {C}. Vì đã có Q4 chứa C => Ko tạo nút bản lề.

Vậy, ko tạo nút bản lề nào cả.

+B4: Tạo cung và quan hệ cung:

PTH\_Thừa(Ni) = {Nj ∈ PTH(Ni): ∃Nh ∈ PTH(Ni) với Qh sao cho KQh+ ⊃ KQj+}

Q1(A,D), Q2(B,E,G), Q3(A,B,G,H), Q4(C,M), Q5(B,C,N,A)

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | PTH(Ni) | | PTH\_Thừa(Ni) | LK(Ni) | LK\_Thừa(Ni) | Cung(Ni) |
| Q1(A,D) | | ∅ | - | - | - | ∅ |
| Q2(B,E,G) | | ∅ | - | - | - | ∅ |
| Q3(A,B,G,H) | | 1, 2 | ∅ | 1, 2 | ∅ | 1, 2 |
| Q4(C,M) | | ∅ | ∅ | ∅ | - | ∅ |
| Q5(B,C,N,A) | | 1,2, 3, 4 | 1, 2  j=1 (vì nút h=3, j là cha của h)  j=2 (vì nút h=3, j là cha của h) | 2, 4 | ∅ | 2, 3, 4 |

+B5: Hủy những nút bản lề thừa: Ko có.

Q1

Q1

Q1

+B6: Mịn hóa các quan hệ nút

+B7: Tạo cung vô hướng: Ko tạo.

Q2

Q1

Q5

Q3

Q4

Con đường truy xuất:

+ Q5 -> Q3 -> Q1

+ Q5 -> Q3 -> Q2

+ Q5 -> Q2

+ Q5 -> Q4

Cho CSDL sau:

Q1(A,M,B)

Q2(B,N,H)

Q3(A,B,E)

Q4(C,A,G)

Q5(C,B,D,A,M)

a) CSDL trên có trùng lắp thông tin không? giải thích?

b) Hãy vẽ đồ thị quan hệ của CSDL đã cho.

--

**Cho phân rã sau:**

**Q1(ABX1) Q6(CEX6)**

**Q2(AX2) Q7(EHX7)**

**Q3(ABCX3DEG) Q8(HX8)**

**Q4(BDEX4) Q9(HG)**

**Q5(CEGX5) Q10(ABCH)**

**1) Hãy biến đổi sang đồ thị quan hệ.**

**2) Hãy chỉ ra các con đường truy xuất.**

+B1: C là 1 phân rã đồng nhất

+B2: Tạo nút và quan hệ nút: có 10 nút.

+B3: Tạo nút bản lề và quan hệ nút bản lề

Q1 ∩ Q4 = {B}, chưa có Q nào chứa khóa B => Tạo Q14(B)

Q3 ∩ Q4 = {B}, có Q14 rồi nên ko tạo

Q3 ∩ Q5 = {C}, chưa có Q nào chứa khóa C => Tạo Q35(C)

Q4 ∩ Q5 = {E}, chưa có Q nào chứa khóa E => Tạo Q45(E)

Q5 ∩ Q9 = {G}, chưa có Q nào chứa khóa G => Tạo Q59(G)

Vậy cần tạo 4 nút bản lề.

+B4: Tạo cung và quan hệ cung

Lồng\_khóa(Ni) = {Nj với Qj sao cho KQi+ ⊃ KQj+}

Lồng\_khóa\_thừa(Ni)={Nj∈lồng\_khóa(Ni): ∃Nh ∈ lồng\_khóa(Ni) với Qh sao cho KQh+ ⊃ KQj+}

Cung(ni) = (pth(ni) - pth\_thừa(ni) ) ∪ (lồng\_khóa(ni) - lồng\_khóa\_thừa(ni))

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | PTH(Ni) | PTH\_Thừa(Ni) | LK(Ni) | LK\_Thừa(Ni) | Cung(Ni) |
| **Q1(ABX1)** | Q2 | ∅ | Q2 | ∅ | Q2 |
| **Q2(AX2)** | ∅ | ∅ | ∅ | ∅ | ∅ |
| **Q3(ABCX3DEG)** | Q1,Q2 | Q2 | Q1,Q2 | Q2 | Q1 |
| **Q4(BDEX4)** | ∅ | ∅ | ∅ | ∅ | ∅ |
| **Q5(CEGX5)** | Q6 | ∅ | Q6 | ∅ | Q6 |
| **Q6(CEX6)** | ∅ | ∅ | ∅ | ∅ | ∅ |
| **Q7(EHX7)** | Q8 | ∅ | Q8 | ∅ | Q8 |
| **Q8(HX8)** | ∅ | ∅ | ∅ | ∅ | ∅ |
| **Q9(HG)** | Q8 | ∅ | Q8 | ∅ | Q8 |
| **Q10(ABCH)** | Q1,Q2,Q3,Q8 | Q1 (vì Q3 chứa)  Q2 (vì Q3 chứa | Q1,Q2,Q3,Q8 | Q1, Q2 | Q3,Q8 |

+B5: Hủy nút bản lề thừa

Q14(B): ko bỏ được vì có 2 cung đến từ Q1 và Q4

Q35(C), Q45(E), Q59(G): tương tự như trên

+B6: Mịn hóa: Xóa thuộc tính Kj nằm trong Qi mà ko là khóa của Qi nhưng là khóa của Qj. Ko bỏ dc nút nào cả.

+B7: Tạo cung vô hướng.

Q2

Q1

Q1

Q1

Q59

Q6

Q9

Q7

Q8

Q45

Q35

Q14

Q4

Q10

Q5

Q3

Q4, Q9 và Q10 là các nút cần xóa và tạo các cung vô hướng:

Q2

Q1

Q59

Q6

Q7

Q8

Q45

Q35

Q14

Q5

Q3

Con đường truy xuất:

Xét ERD sau:

![A chalkboard with a diagram drawn on it  Description automatically generated](data:image/png;base64...)

Hãy vẽ bằng Case Studio:

![A diagram of a diagram  Description automatically generated with medium confidence](data:image/png;base64...)

Cần nắm:

1/ Con đường truy xuất

2/ Con đường truy xuất thô

3/ Đồ thị quan hệ

1. DOI(MADOI, TENDOI, HLVIEN)

2.TRANDAU(MATRAN, NGAY\_T\_DAU, GIO, VONGDAU)

3. BANG\_TDAU(MADOI, BANG)

4. CAUTHU(MACAUTHU,TENVIETTAT, TENCAUTHU, VITRI, MADOI, SOAO)

5. BANTHANG\_CAUTHU(MATRAN, PHUT\_THU, MACAUTHU)

6. CTIET\_TRANDAU(MATRAN, MADOI, SOBANTHANG)

7. DUDOAN\_KQTD(STT, MATRAN, MADOI, KETQUA, SONGUOI\_DUDOAN, DIENTHOAI)

1) Hãy vẽ ĐT quan hệ và con đường truy xuất (CĐTX).

2) Cho biết ý nghĩa cùa CĐTX. Viết câu lệnh SQL để minh họa.

![](data:image/png;base64...)

1) Hãy vẽ ĐT quan hệ và con đường truy xuất (CĐTX).

+B1: Biến C thành phân rã đồng nhất: Có 7 loại quan hệ: Q1…Q7

+B2: Tạo nút và qh nút. Có 7 nút.

+B3: Tạo nút bản lề và qh nút bản lề. Ta lần lượt xét tuần tự quan hệ giữa các nút xem có tt chung ko, ko có thì bỏ qua, có thì tạo quan hệ mới và nếu qh mới này đã có thì Ko tạo.

- Q1 và Q3 => Q13(MADOI), vì đã có Q1 nên ko tạo. Tương tự cho Q14, Q16, Q17.

- Q25, Q26, Q27 cũng ko tạo vì đã có Q2.

- Q34, Q37, Q37; Q45, Q56, Q57, Q67 cũng ko tạo.

+B4: Tạo cung và các qh cung.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | PTH(Ni) | PTH\_Thua(Ni) | Lồng\_Khóa(Ni) | LK\_PTHThua(Ni) | Cung(Ni) |
| Q1: DOI | ∅ | ∅ | ∅ | ∅ |  |
| Q2: TRANDAU | ∅ | ∅ | ∅ | ∅ |  |
| Q3: BANG\_TD | 1 | ∅ | ∅ | ∅ | 1 |
| Q4: CAUTHU | 1 | ∅ | ∅ | ∅ | 1 |
| Q5: BANTHANG | 2,4 | ∅ | ∅ | ∅ | 2,4 |
| Q6: CTTD | 1,2 | ∅ | ∅ | ∅ | 1,2 |
| Q7: DUDOAN | 1,2 | ∅ | ∅ | ∅ | 1,2 |

Xem và sửa bài giải của lớp 19DTJB1.

+B5: Hủy nút bản lề thừa.

Vì ko có nút bản lề => bỏ qua.

+B6: Mịn hóa các nút và qh nút

+B7:

**6**

**1**

**2**

**7**

**5**

**3**

**4**

Nếu có Qi mà có 2 đầu ra, ko có đầu vào => tạo cung vô hướng

+B7:

**1**

**2**

**3**

**4**

Nếu có Qi mà có 2 đầu ra, ko có đầu vào => tạo cung vô hướng

2) Cho biết ý nghĩa cùa CĐTX. Viết câu lệnh SQL để minh họa.

Có 2 nút vào: 3 và 4.

CDTX:

1. >1->2

4->1->2