import unittest
from menu import list_drinks, get_drink_detail, customize_drink


class TestTV4Menu(unittest.TestCase):
    def test_list_all_drinks(self):
        self.assertEqual(len(list_drinks()), 4)

    def test_filter_drinks_by_category(self):
        drinks = list_drinks("Trà sữa")
        self.assertEqual(len(drinks), 1)
        self.assertEqual(drinks[0]["id"], "TS01")

    def test_get_drink_detail(self):
        drink = get_drink_detail("TD01")
        self.assertIsNotNone(drink)
        self.assertEqual(drink["name"], "Trà đào cam sả")

    def test_customize_drink_calculation(self):
        customized = customize_drink(
            drink_id="TS01",
            size="L",
            sugar="70%",
            ice="50%",
            toppings=["Trân châu đen"],
        )
        self.assertEqual(customized["total_price"], 45000)


if __name__ == "__main__":
    unittest.main()