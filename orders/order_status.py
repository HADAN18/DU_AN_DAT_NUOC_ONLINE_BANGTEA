class OrderStatus:
    def __init__(self):
        self.orders = {
            "DH001": "Đang chờ xác nhận",
            "DH002": "Đang chuẩn bị",
            "DH003": "Đang giao hàng",
            "DH004": "Đã hoàn thành"
        }

    def get_status(self, order_id):
        return self.orders.get(order_id, "Không tìm thấy đơn hàng")