def get_order_history(orders, customer_id):
    history = []

    for order in orders:
        if order["customer_id"] == customer_id:
            history.append(order)

    return history


def get_order_by_id(orders, order_id):
    for order in orders:
        if order["id"] == order_id:
            return order

    return None