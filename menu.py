DRINKS = [
    {
        "id": "TS01",
        "name": "Trà sữa truyền thống",
        "category": "Trà sữa",
        "base_price": 30000,
        "description": "Trà đen đậm vị kết hợp sữa béo thơm.",
    },
    {
        "id": "TD01",
        "name": "Trà đào cam sả",
        "category": "Trà trái cây",
        "base_price": 35000,
        "description": "Trà thanh mát cùng đào miếng và hương sả.",
    },
    {
        "id": "ML01",
        "name": "Matcha latte",
        "category": "Matcha",
        "base_price": 40000,
        "description": "Bột matcha thơm dịu hòa quyện sữa tươi.",
    },
    {
        "id": "ST01",
        "name": "Sữa tươi trân châu đường đen",
        "category": "Sữa tươi",
        "base_price": 40000,
        "description": "Sữa tươi mát lạnh kèm trân châu đường đen dẻo mềm.",
    },
]

SIZE_EXTRA = {"S": 0, "M": 5000, "L": 10000}
SUGAR_OPTIONS = ["0%", "30%", "50%", "70%", "100%"]
ICE_OPTIONS = ["0%", "30%", "50%", "70%", "100%"]
TOPPING_EXTRA = {
    "Trân châu đen": 5000,
    "Trân châu trắng": 7000,
    "Thạch đào": 6000,
    "Kem cheese": 10000,
}


def list_drinks(category=None):
    if not category:
        return DRINKS
    filtered = []
    for item in DRINKS:
        if item["category"].lower() == category.lower():
            filtered.append(item)
    return filtered


def get_drink_detail(drink_id):
    for item in DRINKS:
        if item["id"] == drink_id:
            return item
    return None


def customize_drink(drink_id, size="M", sugar="70%", ice="50%", toppings=None):
    if toppings is None:
        toppings = []

    drink = get_drink_detail(drink_id)
    if drink is None:
        raise ValueError("Không tìm thấy đồ uống")
    if size not in SIZE_EXTRA:
        raise ValueError("Size không hợp lệ")
    if sugar not in SUGAR_OPTIONS or ice not in ICE_OPTIONS:
        raise ValueError("Mức đường hoặc đá không hợp lệ")

    price = drink["base_price"] + SIZE_EXTRA[size]
    chosen_toppings = []
    for topping in toppings:
        if topping not in TOPPING_EXTRA:
            raise ValueError(f"Topping không hợp lệ: {topping}")
        price += TOPPING_EXTRA[topping]
        chosen_toppings.append(topping)

    return {
        "id": drink["id"],
        "name": drink["name"],
        "size": size,
        "sugar": sugar,
        "ice": ice,
        "toppings": chosen_toppings,
        "total_price": price,
    }