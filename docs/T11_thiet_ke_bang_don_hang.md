# T11 - THIET KE BANG DON HANG VA CHI TIET DON HANG

## 1. Bang ORDERS - Don hang

| Truong | Kieu du lieu du kien | Rang buoc | Mo ta |
|---|---|---|---|
| order_id | VARCHAR | PRIMARY KEY | Ma don hang |
| customer_id | VARCHAR | NOT NULL | Ma khach hang |
| total_amount | DECIMAL(12,2) | NOT NULL | Tong tien don hang |
| order_status | VARCHAR(50) | NOT NULL | Trang thai don hang |
| payment_status | VARCHAR(50) | NOT NULL | Trang thai thanh toan |
| payment_method | VARCHAR(50) | NULL | Phuong thuc thanh toan |
| created_at | DATETIME | NOT NULL | Thoi gian tao don |

## 2. Bang ORDER_DETAILS - Chi tiet don hang

| Truong | Kieu du lieu du kien | Rang buoc | Mo ta |
|---|---|---|---|
| detail_id | INT | PRIMARY KEY | Ma chi tiet don hang |
| order_id | VARCHAR | FOREIGN KEY, NOT NULL | Ma don hang |
| drink_id | INT | NOT NULL | Ma do uong |
| drink_name | VARCHAR(255) | NOT NULL | Ten do uong tai thoi diem dat |
| unit_price | DECIMAL(12,2) | NOT NULL | Don gia |
| quantity | INT | NOT NULL | So luong |
| subtotal | DECIMAL(12,2) | NOT NULL | Thanh tien |

## 3. Moi quan he

- ORDERS va ORDER_DETAILS co quan he mot - nhieu (1-N).
- order_id la khoa chinh cua ORDERS.
- order_id trong ORDER_DETAILS la khoa ngoai tham chieu den ORDERS.
- Mot don hang co the co nhieu dong chi tiet.
- Moi dong chi tiet chi thuoc mot don hang.

## 4. Quy tac nghiep vu

- Ma don hang khong duoc trung lap.
- Moi don hang phai co khach hang.
- So luong moi mon phai lon hon 0.
- Don gia khong duoc am.
- Thanh tien = Don gia x So luong.
- Tong tien don hang = Tong thanh tien cua cac dong chi tiet.
- Khong cho phep ghi nhan thanh toan hai lan cho cung mot don hang.
- Luu don gia va ten mon tai thoi diem dat de bao toan lich su don hang.

## 5. Vi du

Don hang DH001 cua khach hang KH001:

| Mon | So luong | Don gia | Thanh tien |
|---|---:|---:|---:|
| Tra sua truyen thong | 2 | 25000 | 50000 |
| Tra sua matcha | 1 | 30000 | 30000 |

Tong tien: 80000 VND.

## 6. Ghi chu

Day la thiet ke logic ban dau. Kieu du lieu va cu phap tao bang
se duoc dieu chinh theo he quan tri co so du lieu ma nhom thong nhat.

Chua khai bao khoa ngoai den bang KHACH_HANG hoac DO_UONG
vi chua xac nhan cau truc co so du lieu chung cua cac bang nay.
