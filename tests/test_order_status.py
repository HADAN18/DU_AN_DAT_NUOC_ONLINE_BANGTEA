import unittest
from orders.order_status import OrderStatus


class TestOrderStatus(unittest.TestCase):

    def setUp(self):
        self.order_status = OrderStatus()

    def test_get_status_success(self):
        result = self.order_status.get_status("DH001")
        self.assertEqual(result, "Đang chờ xác nhận")

    def test_get_status_not_found(self):
        result = self.order_status.get_status("DH999")
        self.assertEqual(result, "Không tìm thấy đơn hàng")


if __name__ == "__main__":
    unittest.main()