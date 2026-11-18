
import unittest
from customers.menu import Menu


class TestMenu(unittest.TestCase):

    def setUp(self):
        self.menu = Menu()

    def test_view_menu(self):
        self.assertEqual(len(self.menu.drinks), 5)

    def test_select_drink_success(self):
        drink = self.menu.select_drink(1)
        self.assertIsNotNone(drink)
        self.assertEqual(drink["name"], "Trà sữa truyền thống")

    def test_select_drink_not_found(self):
        drink = self.menu.select_drink(99)
        self.assertIsNone(drink)


if __name__ == "__main__":
    unittest.main()
