lOMoARcPSD|56030397
CCOOSS332233--TTHHỰỰCC HHÀÀNNHH CCƠƠ SSỞỞ DDỮỮ LLIIỆỆUU
NNhhậậpp mmôônn ccơơ ssởở ddữữ lliiệệuu ((HHUUTTEECCHH UUnniivveerrssiittyy ooff TTeecchhnnoollooggyy))
SSccaann ttoo ooppeenn oonn SSttuuddooccuu
SSttuuddooccuu iiss nnoott ssppoonnssoorreedd oorr eennddoorrsseedd bbyy aannyy ccoolllleeggee oorr uunniivveerrssiittyy
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
LI U
Biên
Võ Hoàng Khang
www.hutech.edu.vn
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
HÀNH
*1.2020.cos323*
này, xin - :
tailieuhoctap@hutech.edu.vn
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
I
M
...................................................................................................................I
........................................................................................................... II
.......................................................................... 1
..................................................................... 8
..................................................................... 13
................................................................ 16
.......................................................................... 25
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
II

| -  Cài  | t SQL Server phiên b | n 2014, 2016 tr |  v  sau...  |
| ------- | -------------------- | --------------- | ----------- |
-  Ph n cài  t, SV có th  th c hi n   nhà. Trong phòng máy th c hành, SV luy n
t p các thao tác Detach, Attach, Backup, Restore database cho thu n th c, nh m
| h  tr |  t t cho các bu | i th c hành sau.  |     |
| ----- | --------------- | ----------------- | --- |
-  Bu i th c hành  u tiên, SV l y thông tin c a bài  a lý Vi t Nam   th c hi n.
-  Chú  ý:  ch n  Server  name  (ch n  Computer  name)  và  Authentication (ch n
| Windows Authentication)  |     |     | p.  |
| ------------------------ | --- | --- | --- |

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
III
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
  1

  T o DataBase DIALYVN.
Chú ý: Ki u thu c tính và   r ng c a Khóa chính và Khóa ng  ph i gi ng nhau.

| -  Nh | p d  li u:                    |              |     |     |     |
| ----- | ----------------------------- | ------------ | --- | --- | --- |
|       | Nh p tr c ti p t              |  bàn phím    |     |     |     |
|       | Nh p b ng l nh Insert         |              |     |     |     |
|       | Nh p b ng cách copy và paste  |              |     |     |     |
|       | Nh p b ng cách Import t       |  file Excel  |     |     |     |
D n dò:
Sau m i bu i th c hành, SV có c  ch  sao l u   ph c h i d  li u khi c n thi t
| (mang v |  nhà hay làm ti | p vào các bu | i th c hành k |  ti |     |
| ------- | --------------- | ------------ | ------------- | --- | --- |
-  Detach và Attach DB
-  Backup và Restore DB

TINH_TP (MA_T_TP, TEN_T_TP, DT, DS, MIEN)
| Mô  | -   |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
-

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
| 2   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |

Trung, Nam.
BIENGIOI (NUOC, MA_T_TP)
| -   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
LANGGIENG (MA_T_TP, LG)
| M             |                  |                        | -   |     |           |     |     |
| ------------- | ---------------- | ---------------------- | --- | --- | --------- | --- | --- |
| (LANGGIENG).  |                  | LG: chính là MA_T_TP.  |     |     |           |     |     |
| Thu c tính    | Mô t             |                        |     |     | Ki u      |     | c   |
| MA_T_TP       | Mã s             |  t nh, thành ph        |     |     | varchar   | 3   |     |
| TEN_T_TP      | Tên t            | nh, Thành ph           |     |     | nvarchar  | 20  |     |
| DT            | Di n tích (Km2)  |                        |     |     | float     |     |     |
| DS            | Dân s            |                        | i)  |     | bigint    |     |     |
| MIEN          | Mi n (B          | c, Trung, Nam)         |     |     | nvarchar  | 10  |     |
| NUOC          | c có biên gi     |                        | i   |     | nvarchar  | 15  |     |
| LG            | Gi               |                        |     |     |           |     |     |

TINH_TP:
| MA_TTP  | TEN_TTP    |     |     | DT    | DS       |     | MIEN  |
| ------- | ---------- | --- | --- | ----- | -------- | --- | ----- |
| AG      | An Giang   |     |     | 3406  | 2142709  |     | Nam   |
| BR      | Bà R a -   |     |     | 1982  | 996682   |     | Nam   |
| BC      | B c C n    |     |     | 4857  | 293826   |     | B c   |
| BG      | B c Giang  |     |     | 3823  | 1554131  |     | B c   |
| BL      | B c Liêu   |     |     | 2526  | 856518   |     | Nam   |

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
  3

| MA_TTP  | TEN_TTP     |     | DT       | DS       | MIEN   |
| ------- | ----------- | --- | -------- | -------- | ------ |
| BN      | B c Ninh    |     | 808      | 1024472  | B c    |
| BT      | B n Tre     |     | 2322     | 1255946  | Nam    |
| BDI     |             | nh  | 6025     | 1486465  | Trung  |
| BD      |             |     | 2696     | 1481550  | Nam    |
| BP      |             | c   | 6857     | 873598   | Nam    |
| BTH     | Bình Thu    | n   | 7828     | 1167023  | Trung  |
| CM      | Cà Mau      |     | 5202     | 1206938  | Nam    |
| CT      | C           |     | 1390     | 1188435  | Nam    |
| CB      | Cao B       | ng  | 6691     | 507183   | B c    |
| DN      | ng          |     | 1256     | 887435   | Trung  |
| DL      | c L         | c   | 13085    | 1733624  | Trung  |
| DNO     | c Nông      |     | 6515     | 489392   | Trung  |
| DB      | n Biên      |     | 9560     | 490306   | B c    |
| DNA     | ng Nai      |     | 5895     | 2486154  | Nam    |
| DT      | ng Tháp     |     | 3246     | 1666467  | Nam    |
| GL      | Gia Lai     |     | 15495    | 1274412  | Trung  |
| HG      | Hà Giang    |     | 7884     | 724537   | B c    |
| HNA     | Hà Nam      |     | 852      | 784045   | B c    |
| HN      | Hà N i      |     | 3334,47  | 6451909  | B c    |
| HT      | Hà Tây      |     | 2193     | 2047000  | B c    |
| HTI     |             |     | 6055,70  | 1227554  | B c    |
| HD      | H           |     | 1648     | 1705059  | B c    |
| HP      | H i Phòng   |     | 1526     | 1837173  | B c    |
| HAG     | H u Giang   |     | 1608     | 757300   | Nam    |
| HB      | Hòa Bình    |     | 4663     | 785217   | B c    |
| HY      |             |     | 923      | 1127903  | B c    |
| KH      | Khánh Hòa   |     | 5198     | 1157604  | Trung  |
| KG      | Kiên Giang  |     | 6268     | 1688248  | Nam    |
| KT      | Kon Tum     |     | 9615     | 430133   | Trung  |
| LC      | Lai Châu    |     | 9059     | 370502   | B c    |
| LD      |             | ng  | 9765     | 1187574  | Trung  |

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
4

| MA_TTP  | TEN_TTP         |     | DT       | DS       | MIEN   |
| ------- | --------------- | --- | -------- | -------- | ------ |
| LS      | L               |     | 8305     | 732515   | B c    |
| LCA     | Lào Cai         |     | 6357     | 614595   | B c    |
| LA      | Long An         |     | 4491     | 1436066  | Nam    |
| ND      |                 | nh  | 1641     | 1828111  | B c    |
| NA      | Ngh  An         |     | 16487    | 3113055  | Trung  |
| NB      | Ninh Bình       |     | 1384     | 898999   | B c    |
| MA_TTP  | TEN_TTP         |     | DT       | DS       | MIEN   |
| NT      | Ninh Thu        | n   | 3360     | 564993   | Trung  |
| PT      | Phú Th          |     | 3520     | 1316389  | B c    |
| PY      | Phú Yên         |     | 5045     | 862231   | Trung  |
| QB      | Qu ng Bình      |     | 8051,80  | 846924   | Trung  |
| QN      | Qu ng Nam       |     | 10407    | 1422319  | Trung  |
| QNG     | Qu ng Ngãi      |     | 5138     | 1216773  | Trung  |
| QNI     | Qu ng Ninh      |     | 5900     | 1144988  | B c    |
| QT      | Qu ng Tr        |     | 4745,70  | 597985   | B c    |
| ST      |                 |     | 3223     | 1292853  | Nam    |
| SL      |                 |     | 14055    | 1076055  | B c    |
| TN      | Tây Ninh        |     | 4030     | 1066513  | Nam    |
| TB      | Thái Bình       |     | 1545     | 1781842  | B c    |
| TNG     | Thái Nguyên     |     | 3543     | 1123116  | B c    |
| TH      | Thanh Hóa       |     | 11116    | 3400595  | B c    |
| TTH     | Th a Thiên Hu   |     | 5053,99  | 1087579  | Trung  |
| TG      | Ti n Giang      |     | 2367     | 1672271  | Nam    |
| HCM     | TP H  Chí Minh  |     | 2095     | 7162864  | Nam    |
| TV      | Trà Vinh        |     | 2215     | 1003012  | Nam    |
| TQ      | Tuyên Quang     |     | 5868     | 724821   | B c    |
| VL      |                 |     | 1475     | 1024707  | Nam    |
| VP      |                 |     | 1371     | 999786   | B c    |
| YB      | Yên Bái         |     | 6883     | 740387   | B c    |

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
  5

| LANGGIENG:  |      |            |          BIENGIOI:  |         |          |
| ----------- | ---- | ---------- | ------------------- | ------- | -------- |
| MA_T_TP     | LG   |   MA_T_TP  | LG                  |   NUOC  | MA_T_TP  |
| AG          | DT   |   CT       | AG                  |   CPC   | AG       |
| AG          | CT   |   CT       | DT                  |   CPC   | DL       |
| AG          | KG   |   CT       | VL                  |   CPC   | DT       |
| BR          | HCM  |   CT       | KG                  |   CPC   | GL       |
| BR          | BTH  |   CT       | BL                  |   CPC   | KG       |
| BR          | DNA  |   CT       | ST                  |   CPC   | LA       |
| DNA         | BTH  |   DT       | AG                  |   CPC   | BP       |
| DNA         | BR   |   DT       | LA                  |   CPC   | TN       |
| DNA         | HCM  |   DT       | TG                  |   LAO   | GL       |
| BD          | TN   |   HAG      | CT                  |   LAO   | LC       |
| BD          | DNA  |   HAG      | ST                  |   LAO   | NT       |
| BD          | BP   |   HAG      | VL                  |   LAO   | BT       |
| BD          | HCM  |   HAG      | KG                  |   TQ    | CB       |
| BP          | DL   |   HAG      | BL                  |   TQ    | LC       |
| BP          | BD   |   LA       | TN                  |         |          |
| BP          | LD   |   LA       | TG                  |         |          |
| BP          | DNA  |   LA       | DT                  |         |          |
| BL          | KG   |   LA       | HCM                 |         |          |
| BL          | CT   |   HCM      | BD                  |         |          |
| BL          | CM   |   HCM      | TN                  |         |          |
| BL          | ST   |   HCM      | DNA                 |         |          |
| BT          | TG   |   HCM      | BR                  |         |          |
| BT          | VL   |   HCM      | LA                  |         |          |
| BT          | TV   |   HCM      | TG                  |         |          |
| BT          | HCM  |   TG       | LA                  |         |          |
| CM          | KG   |   TG       | DT                  |         |          |
| CM          | BL   |   TG       | BT                  |         |          |
|             |      |   TG       | VL                  |         |          |
|             |      |   TN       | BD                  |         |          |
|             |      |   TN       | BP                  |         |          |
|             |      |   TN       | LA                  |         |          |
|             |      |   TN       | HCM                 |         |          |
|             |      |   BTH      | DNA                 |         |          |

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
| 6   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Câu 1: Xu | t ra tên tnh, TP cùng v |     |     |     | i dân s |     |  c a t nh, TP:  |     |
| --------- | ----------------------- | --- | --- | --- | ------- | --- | --------------- | --- |
| a.  Có di | n tích >= 5000 Km2      |     |     |     |         |     |                 |     |
b.  Có di n tích >= [input] (SV nh p m t s  b t k  t  bàn phím)
| Câu 2: Xu  | t ra tên tnh, TP cùng v |     |     |     | i di | n tích c | a t nh, TP:  |     |
| ---------- | ----------------------- | --- | --- | --- | ---- | -------- | ------------ | --- |
| Câu 3: Thu | c mi                    | n B | c   |     |      |          |              |     |
Câu 4: Thu c mi n [input] (SV nh p m t mi n b t k  t  bàn phím)
Câu 5: Xu t ra các Tên t nh, TP biên gi i thu c mi n [input] (SV cho m t mi n b t
k )
Câu 6: Cho bi t di n tích trung bình c a các t nh, TP (T ng DT/T ng s  t nh_TP).
Câu 7: Cho bi t dân s  cùng v i tên tnh c a các t nh, TP có di n tích > 7000 Km2.
Câu 8: Cho bi t dân s  cùng v i tên tnh c a các t nh mi n  B c.
| Câu 9: Cho bi |     |     |     | c là biên gi |     | i c | a các t nh mi | n  Nam.  |
| ------------- | --- | --- | --- | ------------ | --- | --- | ------------- | -------- |
Câu 10: Cho bi t di n tích trung bình c a các tnh, TP. (S  d ng hàm)
Câu 11: Cho bi t m  dân s  (DS/DT) cùng v i tên tnh, TP c a t t c  các t nh, TP.
Câu 12: Cho bi t tên các t nh, TP láng gi ng c a tnh  Long An .
| Câu 13: Cho bi |     | t s      |   ng các tnh, TP giáp v |                   |     |     | i CPC .       |     |
| -------------- | --- | -------- | ----------------------- | ----------------- | --- | --- | ------------- | --- |
| Câu 14: Cho bi |     | t tên nh |                         | ng t nh, TP có di |     |     | n tích l n nh | t.  |
| Câu 15: Cho bi |     | t t      | nh, TP có m             |                   |     |     | t.            |     |
Câu 16: Cho bi t tên nh ng t nh, TP giáp v c biên gi i khác nhau.
Câu 17: Cho bi t danh sách các mi n cùng v i các t nh, TP trong các mi

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
7
Câu 18: Cho bi t tên nh ng t nh, TP có nhi u láng gi ng nh t.
Câu 19: Cho bi t nh ng t nh, TP có di n tích nh n tích trung bình c a t t c
t nh, TP.
Câu 20: Cho bi t tên nh ng t nh, TP giáp v i các t nh, TP mi n Nam và không ph i
là mi n .
Câu 21: Cho bi t tên nh ng t nh, TP có di n tích l t c các t nh, TP láng
gi ng c a nó.
Câu 22: Cho bi t tên nh ng t nh, TP mà ta có th n b TP.HCM
xuyên qua ba t m xu ng v i
nhau.
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
8
LOP(MaLop, TenLop, SiSo)
MONHOC(MaMH, TenMH, TCLT, TCTH)
SINHVIEN(MSSV, HoTen, NTNS, Phai, MaLop)
i sinh vien (MS
tên (HoTen), ngày sinh (NTNS),
(MaLop).
Ràng
DIEMSV(MSSV, MaMH, Diem)
a DIEMSV.
Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
  9

 2:

| Thu c tính  |     |     | Ki u d        |  li u  |     |     |
| ----------- | --- | --- | ------------- | ------ | --- | --- |
| MaLop       |     |     | char(7)       |        |     |     |
| TenLop      |     |     | nvarchar(50)  |        |     |     |
| SiSo        |     |     | tinyint       |        |     |     |
| MaMH        |     |     | char(6)       |        |     |     |
| TenMH       |     |     | nvarchar(50)  |        |     |     |
| TCLT, TCTH  |     |     | tinyint       |        |     |     |
| MSSV        |     |     | char(6)       |        |     |     |
| HoTen       |     |     | nvarchar(50)  |        |     |     |
| NTNS        |     |     | date          |        |     |     |
| Phai        |     |     | bit           |        |     |     |
| Diem        |     |     | decimal(3,1)  |        |     |     |

LOP:
|          | MaLop  |                 |     | TenLop  |     | SiSo  |
| -------- | ------ | --------------- | --- | ------- | --- | ----- |
| 18DTH01  |        | CNTT Khóa 18, L |     | p 1     |     | 50    |
| 18DTH02  |        | CNTT Khóa 18, L |     | p 2     |     | 45    |
| 19DTH01  |        | CNTT Khóa 19, L |     | p 1     |     | 55    |
| 19DTH02  |        | CNTT Khóa 19, L |     | p 2     |     | 50    |
| 19DTH03  |        | CNTT Khóa 19, L |     | p 3     |     | 40    |
MONHOC:
| MaMH    |     | TenMH          |              |            | TCLT  | TCTH  |
| ------- | --- | -------------- | ------------ | ---------- | ----- | ----- |
| COS201  |     | K  thu         | t l p trình  |            | 2     | 1     |
| COS202  |     | Lý thuy        |  th          |            | 2     | 1     |
| COS203  |     | CSDLvà qu      | n tr CSDL    |            | 3     | 0     |
| COS204  |     | Phân tích thi  | t k          |  h  th ng  | 3     | 0     |
| COS205  |     | CSDL phân tán  |              |            | 3     | 0     |

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
| 10  |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

SINHVIEN:
| MSSV    |     | HoTen       |              |                 |     | NTNS        |     | Phai  |     | MaLop    |
| ------- | --- | ----------- | ------------ | --------------- | --- | ----------- | --- | ----- | --- | -------- |
| 170001  |     | Lê Hoài An  |              |                 |     | 12/10/1999  |     | 1     |     | 18DTH01  |
| 180002  |     | Nguy        |              | n Th  Hòa Bình  |     | 20/11/2000  |     | 1     |     | 18DTH01  |
| 180003  |     | Ph          |              | ng Châu         |     | 07/06/2000  |     | 0     |     | 18DTH02  |
| 180004  |     | Tr          | n Công Danh  |                 |     | 31/01/2000  |     | 0     |     | 19DTH01  |
DIEMSV:
| MSSV          |      |                |      | MaMH          |               |             |            |     | Diem  |          |
| ------------- | ---- | -------------- | ---- | ------------- | ------------- | ----------- | ---------- | --- | ----- | -------- |
| 170001        |      |                |      | COS201        |               |             |            |     | 10    |          |
| 170001        |      |                |      | COS202        |               |             |            |     | 10    |          |
| 170001        |      |                |      | COS203        |               |             |            |     | 10    |          |
| 170001        |      |                |      | COS204        |               |             |            |     | 10    |          |
| 170001        |      |                |      | COS205        |               |             |            |     | 10    |          |
| 180002        |      |                |      | COS201        |               |             |            |     | 3.5   |          |
| 180002        |      |                |      | COS202        |               |             |            |     | 7     |          |
| 180003        |      |                |      | COS201        |               |             |            |     | 8.5   |          |
| 180003        |      |                |      | COS202        |               |             |            |     | 2     |          |
| 180003        |      |                |      | COS203        |               |             |            |     | 6.5   |          |
| 180004        |      |                |      | COS201        |               |             |            |     | 8     |          |
| 180004        |      |                |      | COS204        |               |             |            |     | NULL  |          |
|               |      |                |      |               |               |             | :          |     |       |          |
| Câu 1: Thêm m |      | t dòng m       |      | i vào b       | ng SINHVIEN v |             | i giá tr:  |     |       |          |
| 190001        |      |                |  Tuy | t Hoa         |               | 08/03/2001  |            | 0   |       | 19DTH02  |
| Câu 2:        |      | i tên môn h    |      |               |               |  th         |            | i r |       |          |
| Câu 3: Hi     | n th |  tên các môn h |      | c không có th |               | c hành.     |            |     |       |          |
Câu 4: Hi n th  tên các môn h c v a có lý thuy t, v a có th c hành.
| Câu 5: In ra tên các môn h |     |     |     | c có ký t |     | u c a tên là ch |     |     |     |     |
| -------------------------- | --- | --- | --- | --------- | --- | --------------- | --- | --- | --- | --- |

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
  11

Câu 6: Li t kê thông tin nh ng sinh viên mà h  ch a ch   Th .
Câu 7: In ra 2 l   t (b ng nhi u cách). Hi n th : Mã l p, Tên l
| s . Nh n xét?                 |     |     |     |     |                 |     |     |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
| Câu 8: In danh sách SV theo t |     |     |     |     | ng l p: MSSV, H |     |     |     |     |     |     | ).  |
Câu 9: Cho bi t nh ng sinh viên có tu  20, thông tin g m: H  tên sinh viên, Ngày
| sinh, Tu   | i.                 |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Câu 10: Li | t kê tên các môn h |     |     |     |     |     |     |     |     | m.  |     |     |
Câu 11: Li t kê k t qu  h c t p c a SV có mã s  170001. Hi n th : MSSV, HoTen,
TenMH, Diem.
| Câu 12: Li     | t kê tên sinh viên và mã môn h |                             |          |                     |              |                   |         |           |           |     | i  m     | m.  |
| -------------- | ------------------------------ | --------------------------- | -------- | ------------------- | ------------ | ----------------- | ------- | --------- | --------- | --- | -------- | --- |
| Câu 13: Li     | t tên môn h                    |                             | c cùng s |                     |              |                   |         |           |           | m.  |          |     |
| Câu 14: Li     | t kê tên SV                    |                             |          | m trung bình c      |              |                   |         | .         |           |     |          |     |
| Câu 15: Li     |                                |                             |          |                     | m cao nh     |                   | t c     | a môn h   |           |     |  thu t l |     |
| Câu 16: Li     |                                |                             |          | m trung bình cao nh |              |                   |         | t.        |           |     |          |     |
| Câu 17: Li     |                                |                             |          | h                   | c môn        | oán r             | i r     | c         |           |     |          |     |
| Câu 18: Cho bi |                                | t sinh viên có              |          |                     |  sinh cùng v |                   | i       |           |           |     | .        |     |
| Câu 19: Cho bi |                                | t t ng sinh viên và t       |          |                     |              | ng s  sinh viên n |         |           | .         |     |          |     |
| Câu 20: Cho bi |                                | t danh sách các sinh viên r |          |                     |              |                   | t ít nh | t 1 môn.  |           |     |          |     |
| Câu 21: Cho bi |                                | t MSSV, H                   |          |                     |              |                   |         | m ít nh   | t 3 môn.  |     |          |     |
Câu 22: In danh sách sinh viên có  m môn   thu t l  cao nh t theo t ng
l p.
| Câu 23:  |     |     |     |     |     | m cao nh | t theo t |     | ng môn, t |     | ng l p.  |     |
| -------- | --- | --- | --- | --- | --- | -------- | -------- | --- | --------- | --- | -------- | --- |

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
| 12  |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Câu 24: Cho bi                   |     | t nh ng sinh viên  |     |         |         | m cao nh       | t c a t ng môn.  |             |
| -------------------------------- | --- | ------------------ | --- | ------- | ------- | -------------- | ---------------- | ----------- |
| Câu 25: Cho bi                   |     | t MSSV, H          |     |         |         |                | c môn nào.       |             |
| Câu 26: Danh sách sinh viên có t |     |                    |     | t c     |         |                | u 10.            |             |
| Câu 27:                          | m s |  sinh viên nam, n  |     |  theo t |         | ng l           | p.               |             |
| Câu 28: Cho bi                   |     | t nh               |     |         | c t     | t c            |                  | t môn nào.  |
| Câu 29: Xóa t                    |     | t c  nh            |     |         |         |  thi môn nào.  |                  |             |
| Câu 30: Cho bi                   |     | t nh               |     |         | c t t c |                |                  | c.          |

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
  13

sau:

Doi(MaDoi, TenDoi)
TranDau(MaTD, MaSan, Ngay, Gio)
CT_TranDau(MaTD, MaDoi, SoBanThang).
anThang >= 0.
| Thu c tính  | Ki u d        |  li u  |
| ----------- | ------------- | ------ |
| MaDoi       | char(3)       |        |
| TenDoi      | nvarchar(50)  |        |
| MaTD        | char(2)       |        |
| Ngay        | date          |        |
| Gi          | time          |        |
| DoBanThang  | tinyint       |        |

Doi:
| MaDoi  |     | TenDoi     |
| ------ | --- | ---------- |
| VN     |     | Vi t Nam   |
| LA     |     | Lào        |
| TL     |     | Thái Lan   |
| CPC    |     | Campuchia  |

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
| 14  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

TranDau:
| MaTD  | MaSan  |     | Ngay        |     | Gio    |
| ----- | ------ | --- | ----------- | --- | ------ |
| 01    | MOD    |     | 14/08/2017  |     | 15:00  |
| 02    | NAS    |     | 16/08/2017  |     | 17:00  |
| 03    | MOD    |     | 16/08/2017  |     | 15:00  |
| 04    | IMO    |     | 18/08/2017  |     | 19:00  |
CT_TranDau:
| MaTD  |     | MaDoi  |     | SoBanThang  |     |
| ----- | --- | ------ | --- | ----------- | --- |
| 01    |     | VN     |     | 3           |     |
| 01    |     | TL     |     | 1           |     |
| 02    |     | VN     |     | 5           |     |
| 02    |     | LA     |     | 0           |     |
| 03    |     | TL     |     | 3           |     |
| 03    |     | CPC    |     | 3           |     |
| 04    |     | TL     |     | 2           |     |
| 04    |     | LA     |     | 0           |     |

| Câu 1: In s |  tr      | u mà m   | u. Hi | n th :  MaDoi, TenDoi.  |     |
| ----------- | -------- | -------- | ----- | ----------------------- | --- |
| Câu 2: In k | t qu  tr | u theo t |  s :  |                         |     |
Câu 3:

    01     |      VN-TL     | 3-1
| Câu 4: In k | t qu  m | i tr | m:  |     |     |
| ----------- | ------- | ---- | --- | --- | --- |
MaTran  | Doi  | Diem
01     | VN  |    3

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
  15

01     | TL   |    0
| Câu 5:  |     | i, t ng s |   m:  |     |
| ------- | --- | --------- | ----- | --- |

| Câu 6: S | p x |     |  bi t th |  h ng:  |
| -------- | --- | --- | -------- | ------- |
  MaDoi  |   Ten Doi
    VN     |  Viet Nam  |          6         |             7
| Câu 7: Hi | n th  các tr |     |     |     |
| --------- | ------------ | --- | --- | --- |
| Các tr    |              |     |     |     |
LA - CPC
VN - CPC

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
| 16  |     |     |     |     |
| --- | --- | --- | --- | --- |
  BÀ

CHUYENBAY(MaCB, GaDi, GaDen, DoDai, GioDi, GioDen, ChiPhi, MaMB)
i, ga
|     | ,   | ng  |     | .   |
| --- | --- | --- | --- | --- |
MAYBAY(MaMB, Loai, TamBay)

NHANVIEN(MaNV, Ten, Luong)
| nhân viên c |     |     |     |     |
| ----------- | --- | --- | --- | --- |
CHUNGNHAN(MaNV, MaMB)
Tâ
viên là phi công thì nhân viên
| nào  |     |     | ó   |     |
| ---- | --- | --- | --- | --- |
ó.

| Thu c tính  |     | Mi           | nh  |     |
| ----------- | --- | ------------ | --- | --- |
| MaCB        |     | char(5)      |     |     |
| GaDi        |     | varchar(50)  |     |     |
| GaDen       |     | varchar(50)  |     |     |
| DoDai       |     | int          |     |     |

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
  17

| Thu c tính  |     |     | Mi            | nh  |     |     |     |
| ----------- | --- | --- | ------------- | --- | --- | --- | --- |
| GioDi       |     |     | time          |     |     |     |     |
| GioDen      |     |     | time          |     |     |     |     |
| ChiPhi      |     |     | int           |     |     |     |     |
| MaMB int    |     |     | int           |     |     |     |     |
| Hieu        |     |     | varchar(50)   |     |     |     |     |
| TamBay      |     |     | int           |     |     |     |     |
| MaNV        |     |     | char(9)       |     |     |     |     |
| Ten         |     |     | nvarchar(50)  |     |     |     |     |
| Luong       |     |     | int           |     |     |     |     |

CHUYENBAY
| MaCB   | GaDi  | GaDen  | DoDai  | GioDi  | GioDen  | ChiPhi  | MaMB  |
| ------ | ----- | ------ | ------ | ------ | ------- | ------- | ----- |
| VN431  | SGN   | CAH    | 3693   | 05:55  | 06:55   | 236     | 747   |
| VN320  | SGN   | DAD    | 2798   | 06:00  | 07:10   | 221     | 737   |
| VN464  | SGN   | DLI    | 2002   | 07:20  | 08:05   | 225     | 340   |
| VN216  | SGN   | DIN    | 4170   | 10:30  | 14:20   | 262     | 757   |
| VN280  | SGN   | HPH    | 11979  | 06:00  | 08:00   | 1279    | 777   |
| VN254  | SGN   | HUI    | 8765   | 18:40  | 20:00   | 781     | 767   |
| VN338  | SGN   | BMV    | 4081   | 15:25  | 16:25   | 375     | 320   |
| VN440  | SGN   | BMV    | 4081   | 18:30  | 19:30   | 426     | 319   |
| VN651  | DAD   | SGN    | 2798   | 19:30  | 08:00   | 221     | 727   |
| VN276  | DAD   | CXR    | 1283   | 09:00  | 12:00   | 203     | 154   |
| VN374  | HAN   | VII    | 510    | 11:40  | 13:25   | 120     | 747   |
| VN375  | VII   | CXR    | 752    | 14:15  | 16:00   | 181     | 737   |
| VN269  | HAN   | CXR    | 1262   | 14:10  | 15:50   | 202     | 340   |
| VN315  | HAN   | DAD    | 134    | 11:45  | 13:00   | 112     | 757   |
| VN317  | HAN   | UIH    | 827    | 15:00  | 16:15   | 190     | 777   |
| VN741  | HAN   | PXU    | 395    | 06:30  | 08:30   | 120     | 767   |
| VN474  | PXU   | PQC    | 1586   | 08:40  | 11:20   | 102     | 747   |
| VN476  | UIH   | PQC    | 485    | 09:15  | 11:50   | 117     | 777   |

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
| 18  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |

MAYBAY
| MaMB  | Loai                |     |     |     | TamBay  |
| ----- | ------------------- | --- | --- | --- | ------- |
| 747   | Boeing 747 - 400    |     |     |     | 13488   |
| 737   | Boeing 737 - 800    |     |     |     | 5413    |
| 340   | Airbus A340 - 300   |     |     |     | 11392   |
| 757   | Boeing 757 - 300    |     |     |     | 6416    |
| 777   | Boeing 777 - 300    |     |     |     | 10306   |
| 767   | Boeing 767 - 400ER  |     |     |     | 10360   |
| 320   | Airbus A320         |     |     |     | 4168    |
| 319   | Airbus A319         |     |     |     | 2888    |
| 727   | Boeing 727          |     |     |     | 2406    |
| 154   | Tupolev 154         |     |     |     | 6565    |
NHANVIEN
| MaNV       |     | Ten              |                 |     | Luong   |
| ---------- | --- | ---------------- | --------------- | --- | ------- |
| 242518965  |     | Tr               | n               |     | 120433  |
| 141582651  |     |                  |  Mai            |     | 178345  |
| 011564812  |     |                  | Quý             |     | 153972  |
| 567354612  |     | Quan C           | m Ly            |     | 256481  |
| 552455318  |     | La Qu            |                 |     | 101745  |
| 550156548  |     | Nguy             | n Th  C m       |     | 205187  |
| 390487451  |     |                  | t               |     | 212156  |
| 274878974  |     | Mai Qu           | c Minh          |     | 99890   |
| 254099823  |     | Nguy             | n Th  Qu nh     |     | 24450   |
| 356187925  |     | Nguy             | n Vinh B o      |     | 44740   |
| 355548984  |     | Tr n Th Hoài An  |                 |     | 212156  |
| 310454876  |     | T                | n               |     | 212156  |
| 489456522  |     | Nguy             | n Th  Quý Linh  |     | 127984  |
| 489221823  |     | Bùi Qu           | c Chinh         |     | 23980   |
| 548977562  |     |                  |                 |     | 84476   |
| 310454877  |     | Tr               | o               |     | 33546   |
| 142519864  |     | Nguy             | n Th            | o   | 227489  |

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
  19

| MaNV       | Ten    |              |     | Luong   |
| ---------- | ------ | ------------ | --- | ------- |
| 269734834  |        | ng Tu n Anh  |     | 289950  |
| 287321212  |        | n Minh       |     | 48090   |
| 552455348  | Bùi Th |  Dung        |     | 92013   |
| 248965255  | Tr     | n Th Ba      |     | 43723   |
| 159542516  |        |              |     | 48250   |
| 348121549  | Nguy   | n Thanh      |     | 32899   |
| 574489457  |        | p            |     | 20      |
CHUNGNHAN
| MaNV       | MaMB  |     | MaNV       | MaMB  |
| ---------- | ----- | --- | ---------- | ----- |
| 567354612  | 747   |     | 142519864  | 340   |
| 567354612  | 737   |     | 142519864  | 320   |
| 567354612  | 757   |     | 269734834  | 747   |
| 567354612  | 777   |     | 269734834  | 737   |
| 567354612  | 767   |     | 269734834  | 340   |
| 567354612  | 727   |     | 269734834  | 757   |
| 567354612  | 340   |     | 269734834  | 777   |
| 552455318  | 737   |     | 269734834  | 767   |
| 552455318  | 319   |     | 269734834  | 320   |
| 552455318  | 747   |     | 269734834  | 319   |
| 552455318  | 767   |     | 269734834  | 727   |
| 390487451  | 340   |     | 269734834  | 154   |
| 390487451  | 320   |     | 242518965  | 737   |
| 390487451  | 319   |     | 242518965  | 757   |
| 274878974  | 757   |     | 141582651  | 737   |
| 274878974  | 767   |     | 141582651  | 757   |
| 355548984  | 154   |     | 141582651  | 767   |
| 310454876  | 154   |     | 011564812  | 737   |
| 142519864  | 747   |     | 011564812  | 757   |
| 142519864  | 757   |     | 574489457  | 154   |
| 142519864  | 777   |     |            |       |
| 142519864  | 767   |     |            |       |
| 142519864  | 737   |     |            |       |

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
| 20  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |

| Câu 1: Cho bi    | t các chuy |                | t (DAD).  |           |     |     |
| ---------------- | ---------- | -------------- | --------- | --------- | --- | --- |
| Câu 2: Cho bi    | t các lo   | i máy bay có t | m bay l   |           |     |     |
| Câu 3: Tìm các n |            |                |           |           |     |     |
| Câu 4: Cho bi    | t các chuy | n bay c        |           | ng bay nh |     |     |
8.000km.
| Câu 5: Cho bi            | t các chuy | n bay xu                               | t phát t                  |                  |     | c (BMV).  |
| ------------------------ | ---------- | -------------------------------------- | ------------------------- | ---------------- | --- | --------- |
| Câu 6: Có bao nhiêu chuy |            | n bay xu                               | t phát t                  |  Sài Gòn (SGN).  |     |           |
| Câu 7: Có bao nhiêu lo   |            | i máy báy Boeing.                      |                           |                  |     |           |
| Câu 8: Cho bi            | t t ng s   |                                        | i tr  cho các nhân viên.  |                  |     |           |
| Câu 9: Cho bi            | t mã s     |  c a các phi công lái máy báy Boeing.  |                           |                  |     |           |
Câu 10: Cho bi t các nhân viên có th  lái máy bay có mã s  747.
Câu 11: Cho bi t mã s  c a các lo i máy bay mà nhân viên có h  Nguy n có th  lái.
Câu 12: Cho bi t mã s  c a các phi công v c Boeing v c Airbus.
Câu 13: Cho bi t các lo i máy bay có th  th c hi n chuy n bay VN280.
Câu 14: Cho bi t các chuy n bay có th   c th c hi n b i máy bay Airbus A320.
| Câu 15: Cho bi | t tên c | a các phi công lái máy bay Boeing.  |     |     |     |     |
| -------------- | ------- | ----------------------------------- | --- | --- | --- | --- |
Câu 16: V i m i lo i máy bay có phi công lái cho bi t mã s , lo i máy báy và t ng s
| phi công có th |  lái lo |     |     |     |     |     |
| -------------- | ------- | --- | --- | --- | --- | --- |

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
  21

Câu 17: Gi  s  m t hành khách mu ng t   n ga B r i quay tr  v  ga A.
| Cho bi | ng bay nào có th |     |     | ng yêu c | u này.  |     |
| ------ | ---------------- | --- | --- | -------- | ------- | --- |
Gom nhóm:
Câu 1: V i m i ga có chuy n bay xu t phát t   t có bao nhiêu chuy n bay
| kh i hành t |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- |
Câu 2: V i m i ga có chuy n bay xu t phát t   t t ng chi phí ph i tr  cho
| phi công lái các chuy |     | n bay kh | i hành t |     |     |     |
| --------------------- | --- | -------- | -------- | --- | --- | --- |
Câu 3: V i m m xu t phát cho bi t có bao nhiêu chuy n bay có th  kh i hành
c 12:00.
Câu 4: Cho bi t mã s  c a các phi công ch   c 3 lo i máy bay.
Câu 5: V i m i phi công có th  lái nhi i máy bay, cho bi t mã s  phi công
| và t m bay l | n nh | t c a các lo |     |     |     |  lái.  |
| ------------ | ---- | ------------ | --- | --- | --- | ------ |
Câu 6: V i m i phi công cho bi t mã s  phi công và t ng s  lo i máy bay mà phi công
 lái.
Câu 7: Cho bi t mã s  c a các phi công có th   c nhi u lo i máy bay nh t.
Câu 8: Cho bi t mã s  c a các phi công có th   c ít lo i máy bay nh t.

| Câu 1: Tìm các nhân viên không ph |        |             | i là phi công.  |                     |     |     |
| --------------------------------- | ------ | ----------- | --------------- | ------------------- | --- | --- |
| Câu 2: Cho bi                     | t mã s |  c a các nh |                 |                     |     | t.  |
| Câu 3: Cho bi                     | t t    | ng s        | i tr            |  cho các phi công.  |     |     |
Câu 4: Tìm các chuy n bay có th   c th c hi n b i t t c  các lo i máy bay Boeing.
Câu 5: Cho bi t mã s  c a các máy bay có th   c s  d  th c hi n chuy n bay
| t   |     | n Hu  (HUI).  |     |     |     |     |
| --- | --- | ------------- | --- | --- | --- | --- |

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
| 22  |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Câu 6: Tìm các chuy |        | n bay có th    |         |   c lái b                |         |        |           |         |     |
| ------------------- | ------ | -------------- | ------- | ------------------------ | ------- | ------ | --------- | ------- | --- |
| Câu 7: Cho bi       |        |                |         |                          |         |        | p nh t c  | ng bay  |     |
| t  Sài Gòn (SGN)    |        | n Buôn Mê Thu  |         | c (BMV).                 |         |        |           |         |     |
| Câu 8: Cho bi       | t mã s |  c a các       |         |                          |         | t.     |           |         |     |
| Câu 9: Cho bi       | t mã s |  c a các nhân  |         |                          |         |  nhì.  |           |         |     |
| Câu 10: Cho bi      | t mã s |  c             |         |                          |  cao th |  nh    | t ho c th |  nhì.   |     |
| Câu 11: Cho bi      |        |                |         | a các nhân viên không ph |         |        |           |         |     |
| l n h               |        | nh c           | a t t c |  các phi công.           |         |        |           |         |     |
Câu 12: Cho  bi t  tên  các  phi  công  có  th   lái  các  máy  bay  có  t m  bay  l
ng nh n lái máy bay Boeing.
Câu 13: Cho bi t tên các phi công lái ít nh t 3 lo i máy bay có t
3200km.
:
Câu 1: V i m i nhân viên cho bi t mã s , tên nhân viên và t ng s  lo i máy bay mà
| nhân viên  | ó có th |  lái.  |     |     |     |     |     |     |     |
| ---------- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- |
Câu 2: V i m i nhân viên cho bi t mã s , tên nhân viên và t ng s  lo i máy bay
| Boeing mà nhân viên  |     | ó có th |  lái.  |     |     |     |     |     |     |
| -------------------- | --- | ------- | ------ | --- | --- | --- | --- | --- | --- |
Câu 3: V i m i lo i máy bay cho bi t lo i máy bay và t ng s  phi công có th  lái lo i
.
Câu 4: V i m i lo i máy bay cho bi t lo i máy bay và t ng s  chuy n bay không th
| th c hi n b | i lo i máy bay  |     |     |     |     |     |     |     |     |
| ----------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Câu 5: V i m i lo i máy bay cho bi t lo i máy bay và t ng s   n
|     |     |  lái lo i máy bay  |     |     |     |     |     |     |     |
| --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- |

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
  23

Câu 6: V i m i lo i máy bay có t m bay trên 3200km, cho bi t tên c a lo i máy bay
|     |     | a các phi công có th |     |     |  lái lo i máy bay  |     |
| --- | --- | -------------------- | --- | --- | ------------------ | --- |
Câu 7: V i m i lo i máy bay cho bi t lo i máy bay và t ng s  nhân viên không th  lái
| lo i máy bay  |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- |
Câu 8: V i m i lo i máy bay cho bi t lo i máy bay và t ng s  phi công không th  lái
| lo i máy bay  |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- |
Câu 9: V i m i nhân viên cho bi t mã s , tên nhân viên và t ng s  chuy n bay xu t
| phát t |  Sài Gòn mà nhân viên  |     |     |  lái.  |     |     |
| ------ | ---------------------- | --- | --- | ------ | --- | --- |
Câu 10: V i m i nhân viên cho bi t mã s , tên nhân viên và t ng s  chuy n bay xu t
| phát t |  Sài Gòn mà nhân viên  |     |     | g th |  lái.  |     |
| ------ | ---------------------- | --- | --- | ---- | ------ | --- |
Câu 11: V i m i phi công cho bi t mã s , tên phi công và t ng s  chuy n bay xu t
| phát t |  Sài Gòn mà phi công  |     |     |  lái.  |     |     |
| ------ | --------------------- | --- | --- | ------ | --- | --- |
Câu 12: V i m i phi công cho bi t mã s , tên phi công và t ng s  chuy n bay xu t
| phát t |  Sài Gòn mà phi công  |     |     |     |  lái.  |     |
| ------ | --------------------- | --- | --- | --- | ------ | --- |
Câu 13: V i m i chuy n bay cho bi t mã s  chuy n bay và t ng s  lo i máy bay
| không th |  th c hi | n chuy | n bay  |     |     |     |
| -------- | -------- | ------ | ------ | --- | --- | --- |
Câu 14: V i m i chuy n bay cho bi t mã s  chuy n bay và t ng s  lo i máy bay có
| th  th | c hi n chuy | n bay  |     |     |     |     |
| ------ | ----------- | ------ | --- | --- | --- | --- |
Câu 15: V i m i chuy n bay cho bi t mã s  chuy n bay và t ng s  nhân viên không
| th  lái chuy | n bay  |     |     |     |     |     |
| ------------ | ------ | --- | --- | --- | --- | --- |
Câu 16: V i m i chuy n bay cho bi t mã s  chuy n bay và t ng s  phi công không
| th  lái chuy | n bay  | ó.  |     |     |     |     |
| ------------ | ------ | --- | --- | --- | --- | --- |
:
Câu 1: M t hành khách mu n  i t  Hà N i (HAN)  n Nha Trang (CXR) mà không
ph i  i chuy n bay quá m t l n. Cho bi t mã chuy n bay và th i gian kh i hành t
| Hà N i n | u hành khách mu |     | n   |     | c 16:00.  |     |
| -------- | --------------- | --- | --- | --- | --------- | --- |

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
| 24  |     |     |     |
| --- | --- | --- | --- |

Câu 2: Cho bi t tên các lo i máy bay mà t t c  các phi công có th  lái
| l   |     |     |     |
| --- | --- | --- | --- |
Câu 3: Cho bi t thông tin c a các  ng bay mà t t c  các phi công có th  bay trên
| ng bay  | ó   |     | 0,000.  |
| ------- | --- | --- | ------- |
Câu 4: Cho bi t tên các phi công ch  lái các lo i máy bay có t
Câu 5: Cho bi t tên các phi công ch  lái các lo i máy bay có t m bay xa
| và m t trong s                |   ó là Boeing.  |            |                     |
| ----------------------------- | --------------- | ---------- | ------------------- |
| Câu 6: Tìm các phi công có th |                 |  lái t t c |  các lo i máy bay.  |
Câu 7: Tìm các phi công có th  lái t t c  các lo i máy bay Boeing.

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
  25

NCC(MaNCC, Ten, Heso, ThPho)

VATTU(MaVT, Ten, Mau, TrLuong, ThPho)

DUAN(MaDA, Ten, ThPho)
| tên và  |     |     |     |
| ------- | --- | --- | --- |
CC(MaNCC, MaVT, MaDA, SLuong)

| Thu c tính  |     | Mi n giá tr   |     |
| ----------- | --- | ------------- | --- |
| MaNCC       |     | char(5)       |     |
| Ten         |     | nvarchar(40)  |     |
| Heso        |     | int           |     |
| ThPho       |     | nvarchar(20)  |     |
| MaDA        |     | char(5)       |     |

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
| 26  |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Thu c tính  |     |     |     |     | Mi n giá tr   |     |     |     |
| ----------- | --- | --- | --- | --- | ------------- | --- | --- | --- |
| MaVT        |     |     |     |     | char(5)       |     |     |     |
| Mau         |     |     |     |     | nvarchar(15)  |     |     |     |
| TrLuong     |     |     |     |     | float         |     |     |     |
| SLuong      |     |     |     |     | int           |     |     |     |
|             |     | :   |     |     |               |     |     |     |
NCC
| MaNCC  |     | Ten   |     |     | Heso  |     | ThPho   |        |
| ------ | --- | ----- | --- | --- | ----- | --- | ------- | ------ |
| S1     |     | n     |     |     | 20    |     | TP.HCM  |        |
| S2     |     | Trân  |     |     | 10    |     | Hà N    | i      |
| S3     |     | Bách  |     |     | 30    |     | Hà N    | i      |
| S4     |     | L p   |     |     | 20    |     | TP.HCM  |        |
| S5     |     | Ánh   |     |     | 30    |     |         |  N ng  |
DUAN
| MaDA  |     | Ten         |       |     |     |     | ThPho      |        |
| ----- | --- | ----------- | ----- | --- | --- | --- | ---------- | ------ |
| J1    |     | Máy phân lo |       | i   |     |     | Hà N       | i      |
| J2    |     | Màn hình    |       |     |     |     | Vi         | t Trì  |
| J3    |     | OCR         |       |     |     |     |            | ng     |
| J4    |     | B           | u khi | n   |     |     |            | ng     |
| J5    |     | RAID        |       |     |     |     | TP.HCM     |        |
| J6    |     | EDS         |       |     |     |     | H i Phòng  |        |
| J7    |     | B ng t      |       |     |     |     | TP.HCM     |        |
VATTU
| MaVT  | Ten     |     |     | Mau      |     | TrLuong  |     | ThPho      |
| ----- | ------- | --- | --- | -------- | --- | -------- | --- | ---------- |
| P1    | ai      | c   |     |          |     | 12.0     |     | TP.HCM     |
| P2    | Bù lon  |     |     | Xanh lá  |     | 17.0     |     | Hà N i     |
| P3    |         | t   |     |          | ng  | 17.0     |     | H i Phòng  |
| P4    |         | t   |     |          |     | 14.0     |     | TP.HCM     |
| P5    | Cam     |     |     |          | ng  | 12.0     |     | Hà N i     |
| P6    |         | ng  |     |          |     | 19.0     |     | TP.HCM     |

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
  27

CC
| MaNCC  | MaVT  |     | MaDA  | SLuong  |
| ------ | ----- | --- | ----- | ------- |
| S1     | P1    |     | J1    | 200     |
| S1     | P1    |     | J4    | 700     |
| S2     | P3    |     | J1    | 400     |
| S2     | P3    |     | J2    | 200     |
| S2     | P3    |     | J3    | 200     |
| S2     | P3    |     | J4    | 500     |
| S2     | P3    |     | J5    | 600     |
| S2     | P3    |     | J6    | 400     |
| S2     | P3    |     | J7    | 800     |
| S2     | P5    |     | J2    | 100     |
| S3     | P3    |     | J1    | 200     |
| S3     | P4    |     | J2    | 500     |
| S4     | P6    |     | J3    | 300     |
| S4     | P6    |     | J7    | 300     |
| S5     | P2    |     | J2    | 200     |
| S5     | P2    |     | J4    | 100     |
| S5     | P5    |     | J5    | 500     |
| S5     | P5    |     | J7    | 100     |
| S5     | P6    |     | J2    | 200     |
| S5     | P1    |     | J4    | 100     |
| S5     | P3    |     | J4    | 200     |
| S5     | P4    |     | J4    | 800     |
| S5     | P5    |     | J4    | 400     |
| S5     | P6    |     | J4    | 500     |

Câu 1: T o các quan h  trên v i các ràng bu c khóa chính, khóa ngo i.
| Câu 2: Nh | p d  li u vào các lo | i quan h     |  v a t o.  |     |
| --------- | -------------------- | ------------ | ---------- | --- |
| Câu 3: Th | c hi n các câu l     | nh SQL sau:  |            |     |

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
| 28  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |

1.  Cho bi t quy cách màu và thành ph  c a các v c tr  t i Hà N i có
| tr         | ng l               |     |         |              |     |     |     |
| ---------- | ------------------ | --- | ------- | ------------ | --- | --- | --- |
| 2.  Cho bi | t thông tin chi ti | t c | a t t c |  các d  án.  |     |     |     |
3.  Cho bi t thông tin chi ti t c a t t c  các d  án   TP.HCM.
| 4.  Cho bi | t tên nhà cung c   | p cung c |     | p v |  án J1.  |        |         |
| ---------- | ------------------ | -------- | --- | --- | -------- | ------ | ------- |
| 5.  Cho bi | t tên nhà cung c   | p, tên v |     |     |  án mà s |   ng v | c cung  |
| c p cho d  |  án b i nhà cung c |          | p l |     |          |        |         |
6.  Cho bi t thông tin chi ti t c a các v c cung c p b i các nhà cung c p
TP.HCM.
7.  Cho bi t mã s  các v c cung c p cho các d  án t i TP.HCM b i các nhà
| cung c | p   TP.HCM.  |     |     |     |     |     |     |
| ------ | ------------ | --- | --- | --- | --- | --- | --- |
8.  Li t kê các c p tên thành ph  mà nhà cung c p   thành ph  th  nh t cung c p v t
|     | c tr  t i thành ph |  th |  hai.  |     |     |     |     |
| --- | ------------------ | --- | ------ | --- | --- | --- | --- |
9.  Li t kê các c p tên thành ph  mà nhà cung c p   thành ph  th  nh t cung c p v t
|     |  án t i thành ph |     |  th  hai.  |     |     |     |     |
| --- | ---------------- | --- | ---------- | --- | --- | --- | --- |
10. Li t kê các c p mã s  nhà cung c p   cùng m t thành ph .
11. Cho bi t mã s  và tên các v c cung c p cho d  án cùng thành ph  v i nhà
| cung c | p.  |     |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- |
12. Cho bi t mã s  và tên các d   c cung c p v i ít nh t m t nhà cung
| c p không cùng thành ph |     | .   |     |     |     |     |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- |
13. Cho bi t mã s  nhà cung c p và c p mã s  v c cung c p b i nhà cung c p
này.
| 14. Cho bi | t mã s  các v |     | c cung c | p b i nhi |     | t nhà cung c | p.  |
| ---------- | ------------- | --- | -------- | --------- | --- | ------------ | --- |
15. V i m i v t  t mã s  và t ng s   c cung c p cho các d  án.

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
|     |     |     |     |     |     |     |     |     |     |     |     |   29 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- |

16. Cho bi t t ng s  các d   c cung c p v i nhà cung c p S1.
| 17. Cho bi | t t | ng s |   ng v |     |     | c cung b |     | i nhà cung c |     | p S1.  |     |     |     |
| ---------- | --- | ---- | ------ | --- | --- | -------- | --- | ------------ | --- | ------ | --- | --- | --- |
18. V i m i v c cung c p cho m t d  án, cho bi t mã s , tên v  án
| và t       | ng s        |   ng v      |     |     |          | ng.  |          |              |     |        |     |     |     |
| ---------- | ----------- | ----------- | --- | --- | -------- | ---- | -------- | ------------ | --- | ------ | --- | --- | --- |
| 19. Cho bi | t mã s      | , tên các v |     |     |          |      |  án có s |              |     | ng v   |     |     | g   |
| c p cho d  |             |  án l       |     |     |          |      |          |              |     |        |     |     |     |
| 20. Cho bi | t tên các d |             |     |     | c cung c | p v  |          | i nhà cung c |     | p S1.  |     |     |     |
21. Cho bi t quy cách màu c a các v c cung c p b i nhà cung c p S1.
22. Cho bi t mã s  và tên các v c cung c p cho m t d  án b t k    TP.HCM.
23. Cho bi t mã s  và tên các d  án s  d ng v   c cung c p b i nhà
| cung c     | p S1.  |                    |     |     |     |             |     |     |     |     |     |     |     |
| ---------- | ------ | ------------------ | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| 24. Cho bi | t mã s |  và tên nhà cung c |     |     |     | p có cung c |     | p v |     |     |     | .   |     |
25. Cho bi t tên các nhà cung c p có ch  s  x p h ng nh    s  l n nh t.
| 26. Cho bi | t tên các nhà cung c |                        |     |     | p không cung c |     |     | p v |     |     |          |     |     |
| ---------- | -------------------- | ---------------------- | --- | --- | -------------- | --- | --- | --- | --- | --- | -------- | --- | --- |
| 27. Cho bi | t mã s               |  và tên các nhà cung c |     |     |                |     |     |     |     | p v | c cung c | p b | i   |
| nhà cung c |                      | p có cung c            |     | p v |                | i q |     |     |     | .   |          |     |     |
28. Cho bi t mã s  và tên các nhà cung c p có ch  s  x p h p
S1.
| 29. Cho bi | t mã s |  và tên các d          |        |     |                 | c cung c |          | p v |         | i s      | ng v    |     |      |
| ---------- | ------ | ---------------------- | ------ | --- | --------------- | -------- | -------- | --- | ------- | -------- | ------- | --- | ---- |
| bình l     |        | t c                    |  các s |     |   ng v          |          | c cung c |     | p cho d |  án J1.  |         |     |      |
| 30. Cho bi | t mã s |  và tên các nhà cung c |        |     |                 |          | p cung c |     | p v     |          | t d     |     |      |
| v i s      |        | ng l                   |        |     | ng trung bình c |          |          | a v |         | c cung c | p cho d |     |  án  |
ó.

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)

lOMoARcPSD|56030397
| 30  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |

| 31. Cho bi | t mã s |  và tên các d |     |                 | c cung c | p v |     |
| ---------- | ------ | ------------- | --- | --------------- | -------- | --- | --- |
|            |  b i m | t nhà cung c  | p b | t k    TP.HCM.  |          |     |     |
32. Cho bi t mã s  và tên các d   c cung c p toàn b  v i nhà cung c p
S1.
| 33. Cho bi | t tên các nhà cung c |     | p cung c | p t t c |  các v |     |     |
| ---------- | -------------------- | --- | -------- | ------- | ------ | --- | --- |
34. Cho bi t mã s  và tên các v c cung c p cho t t c  các d  án t i TP.HCM.
35. Cho bi t mã s  và tên các nhà cung c p cung c p cùng m t v t c  các
d  án.
36. Cho bi t mã s  và tên các d   c cung c p t t c  các v   c cung
| c p b | i nhà cung c | p S1.  |     |     |     |     |     |
| ----- | ------------ | ------ | --- | --- | --- | --- | --- |
37. Cho bi t t t c  các thành ph   t m t nhà cung c p, tr  ít nh t
| m t v |     | c có ít nh | t m t d |  án.  |     |     |     |
| ----- | --- | ---------- | ------- | ----- | --- | --- | --- |
38. Cho bi t mã s  các v c cung c p b i m t nhà cung c p   TP.HCM
| ho c cung c |     | p cho m | t d  án t | i TP.HCM.  |     |     |     |
| ----------- | --- | ------- | --------- | ---------- | --- | --- | --- |
39. Li t kê các c p (mã s  nhà cung c p, mã s  v  cung c p không c p
| v   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
40. Li t kê các c p mã s  nhà cung c p có th  cung c p cùng t t c  các lo i v
| 41. Cho bi | t tên các thành ph |     |  tr |  nhi |     |     | .   |
| ---------- | ------------------ | --- | --- | ---- | --- | --- | --- |

Downloaded by 4851_Nguy?n Ng?c Tình (nguyenngoctinh011258@gmail.com)