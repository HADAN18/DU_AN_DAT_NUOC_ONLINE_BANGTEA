
class Menu:
    def __init__(self):
        self.drinks = [
            {"id": 1, "name": "Trà sữa truyền thống", "price": 25000},
            {"id": 2, "name": "Trà sữa matcha", "price": 30000},
            {"id": 3, "name": "Trà sữa socola", "price": 30000},
            {"id": 4, "name": "Trà đào cam sả", "price": 35000},
            {"id": 5, "name": "Trà vải", "price": 30000}
        ]

    def view_menu(self):
        print("\n===== MENU BĂNG TEA =====")
        for drink in self.drinks:
            print(f"{drink['id']}. {drink['name']} - {drink['price']:,} VND")

    def select_drink(self, drink_id):
        for drink in self.drinks:
            if drink["id"] == drink_id:
                return drink
        return None
