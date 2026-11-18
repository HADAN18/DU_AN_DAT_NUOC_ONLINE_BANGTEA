import unittest
from order_history import get_order_history, get_order_by_id


class TestOrderHistory(unittest.TestCase):

    def setUp(self):
        self.orders = [
            {"id": 1, "customer_id": 101, "total": 50000},
            {"id": 2, "customer_id": 102, "total": 70000},
            {"id": 3, "customer_id": 101, "total": 90000}
        ]

    def test_get_order_history(self):
        result = get_order_history(self.orders, 101)
        self.assertEqual(len(result), 2)

    def test_customer_without_orders(self):
        result = get_order_history(self.orders, 103)
        self.assertEqual(len(result), 0)

    def test_get_order_by_id(self):
        result = get_order_by_id(self.orders, 2)
        self.assertEqual(result["total"], 70000)

    def test_order_not_found(self):
        result = get_order_by_id(self.orders, 99)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()