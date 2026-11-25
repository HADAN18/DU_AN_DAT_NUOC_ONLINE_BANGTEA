
import unittest

from customers.menu import Menu
from orders.order import Order


class TestPayment(unittest.TestCase):

    def setUp(self):
        self.menu = Menu()
        self.order = Order("DH001", "KH001")

    # Kiểm tra phương thức thanh toán không hợp lệ
    def test_invalid_payment_method(self):
        drink = self.menu.select_drink(1)
        self.order.add_item(drink, 2)

        with self.assertRaises(ValueError):
            self.order.record_payment("Thẻ ngân hàng")

    # Kiểm tra tổng tiền khi đơn hàng trống
    def test_empty_order_total(self):
        self.assertEqual(self.order.calculate_total(), 0)

    # Kiểm tra tổng tiền sau khi thêm nhiều món
    def test_total_after_adding_multiple_items(self):
        drink1 = self.menu.select_drink(1)
        drink2 = self.menu.select_drink(2)

        self.order.add_item(drink1, 2)
        self.order.add_item(drink2, 1)

        self.assertEqual(self.order.calculate_total(), 80000)


if __name__ == "__main__":
    unittest.main()
