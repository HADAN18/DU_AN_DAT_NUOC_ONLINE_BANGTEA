
from orders.order_detail import OrderDetail


class Order:
    def __init__(self, order_id, customer_id):
        self.order_id = order_id
        self.customer_id = customer_id
        self.details = []
        self.total_amount = 0
        self.order_status = "Đang chờ xác nhận"
        self.payment_status = "Chưa thanh toán"
        self.payment_method = None

    # Thêm món vào đơn hàng
    def add_item(self, drink, quantity):
        detail = OrderDetail(drink, quantity)
        self.details.append(detail)
        self.calculate_total()

    # Tính tổng tiền
    def calculate_total(self):
        self.total_amount = sum(
            detail.calculate_subtotal()
            for detail in self.details
        )
        return self.total_amount

    # Ghi nhận thanh toán
    def record_payment(self, payment_method):
        allowed_methods = [
            "Tiền mặt",
            "Chuyển khoản",
            "Ví điện tử"
        ]

        if not self.details:
            raise ValueError("Đơn hàng chưa có món!")

        if payment_method not in allowed_methods:
            raise ValueError("Phương thức thanh toán không hợp lệ!")

        if self.payment_status == "Đã thanh toán":
            raise ValueError("Đơn hàng đã được thanh toán!")

        self.payment_method = payment_method
        self.payment_status = "Đã thanh toán"

        return True

    # Chuyển thông tin đơn hàng thành dictionary
    def to_dict(self):
        return {
            "order_id": self.order_id,
            "customer_id": self.customer_id,
            "details": [
                detail.to_dict() for detail in self.details
            ],
            "total_amount": self.total_amount,
            "order_status": self.order_status,
            "payment_status": self.payment_status,
            "payment_method": self.payment_method
        }



