import unittest
from customers.menu import Menu
from orders.order import Order


class TestOrder(unittest.TestCase):

    def setUp(self):
        self.menu = Menu()
        self.order = Order("DH001", "KH001")

    def test_create_order(self):
        self.assertEqual(self.order.order_id, "DH001")
        self.assertEqual(self.order.customer_id, "KH001")

    def test_add_item(self):
        drink = self.menu.select_drink(1)
        self.order.add_item(drink, 2)
        self.assertEqual(len(self.order.details), 1)
        self.assertEqual(self.order.total_amount, 50000)

    def test_calculate_total(self):
        drink1 = self.menu.select_drink(1)
        drink2 = self.menu.select_drink(2)
        self.order.add_item(drink1, 2)
        self.order.add_item(drink2, 1)
        self.assertEqual(self.order.calculate_total(), 80000)

    def test_invalid_quantity(self):
        drink = self.menu.select_drink(1)
        with self.assertRaises(ValueError):
            self.order.add_item(drink, 0)

    def test_record_payment_success(self):
        drink = self.menu.select_drink(1)
        self.order.add_item(drink, 2)
        result = self.order.record_payment("Tiền mặt")
        self.assertTrue(result)
        self.assertEqual(self.order.payment_status, "Đã thanh toán")
        self.assertEqual(self.order.payment_method, "Tiền mặt")

    def test_payment_empty_order(self):
        with self.assertRaises(ValueError):
            self.order.record_payment("Tiền mặt")

    def test_payment_twice(self):
        drink = self.menu.select_drink(1)
        self.order.add_item(drink, 1)
        self.order.record_payment("Chuyển khoản")
        with self.assertRaises(ValueError):
            self.order.record_payment("Chuyển khoản")


if __name__ == "__main__":
    unittest.main()
