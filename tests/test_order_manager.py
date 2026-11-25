
import unittest

from orders.order_manager import OrderManager


class TestOrderManager(unittest.TestCase):

    def setUp(self):
        self.manager = OrderManager()

    # Kiểm tra tạo đơn hàng đầu tiên
    def test_create_order(self):
        order = self.manager.create_order("KH001")

        self.assertEqual(order.order_id, "DH001")
        self.assertEqual(order.customer_id, "KH001")

    # Kiểm tra mã đơn hàng tăng dần
    def test_create_multiple_orders(self):
        order1 = self.manager.create_order("KH001")
        order2 = self.manager.create_order("KH002")

        self.assertEqual(order1.order_id, "DH001")
        self.assertEqual(order2.order_id, "DH002")

    # Kiểm tra tìm đơn hàng
    def test_find_order(self):
        order = self.manager.create_order("KH001")

        result = self.manager.find_order("DH001")

        self.assertEqual(result, order)

    # Kiểm tra mã đơn hàng không tồn tại
    def test_find_order_not_found(self):
        result = self.manager.find_order("DH999")

        self.assertIsNone(result)

    # Kiểm tra lấy danh sách đơn hàng
    def test_get_all_orders(self):
        self.manager.create_order("KH001")
        self.manager.create_order("KH002")

        orders = self.manager.get_all_orders()

        self.assertEqual(len(orders), 2)


if __name__ == "__main__":
    unittest.main()
