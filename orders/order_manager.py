
from orders.order import Order


class OrderManager:
    def __init__(self):
        # Danh sách lưu các đơn hàng tạm thời
        self.orders = []
        self.next_order_id = 1

    # Tạo đơn hàng mới
    def create_order(self, customer_id):
        order_id = f"DH{self.next_order_id:03d}"

        order = Order(order_id, customer_id)

        self.orders.append(order)
        self.next_order_id += 1

        return order

    # Tìm đơn hàng theo mã
    def find_order(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                return order

        return None

    # Lấy danh sách đơn hàng
    def get_all_orders(self):
        return self.orders
