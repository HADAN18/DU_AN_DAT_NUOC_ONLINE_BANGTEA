

class OrderDetail:

    def __init__(self, drink, quantity):
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise ValueError("Số lượng phải là số nguyên!")

        if quantity <= 0:
            raise ValueError("Số lượng phải lớn hơn 0!")

        self.drink_id = drink["id"]
        self.drink_name = drink["name"]
        self.unit_price = drink["price"]
        self.quantity = quantity

    def calculate_subtotal(self):
        return self.unit_price * self.quantity

    def to_dict(self):
        return {
            "drink_id": self.drink_id,
            "drink_name": self.drink_name,
            "unit_price": self.unit_price,
            "quantity": self.quantity,
            "subtotal": self.calculate_subtotal()
        }

