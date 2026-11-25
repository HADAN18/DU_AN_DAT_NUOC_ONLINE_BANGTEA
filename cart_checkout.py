
from customers.menu import Menu
from orders.order import Order


class CartCheckout:
    def __init__(self):
        self.menu = Menu()
        self.order = Order("DH001", "KH001")

    # Hiển thị menu
    def show_menu(self):
        self.menu.view_menu()

    # Thêm món vào giỏ hàng
    def add_to_cart(self):
        self.show_menu()

        try:
            drink_id = int(input("\nNhập mã món muốn chọn: "))
            drink = self.menu.select_drink(drink_id)

            if drink is None:
                print("Không tìm thấy món!")
                return

            quantity = int(input("Nhập số lượng: "))

            self.order.add_item(drink, quantity)
            print(f"Đã thêm {drink['name']} vào giỏ hàng!")

        except ValueError as error:
            print("Dữ liệu không hợp lệ:", error)

    # Hiển thị giỏ hàng
    def show_cart(self):
        print("\n========== GIỎ HÀNG ==========")

        if not self.order.details:
            print("Giỏ hàng đang trống!")
            return

        for index, detail in enumerate(self.order.details, 1):
            print(
                f"{index}. {detail.drink_name} | "
                f"Số lượng: {detail.quantity} | "
                f"Đơn giá: {detail.unit_price:,} VND | "
                f"Thành tiền: {detail.calculate_subtotal():,} VND"
            )

        print("------------------------------")
        print(f"TỔNG TIỀN: {self.order.calculate_total():,} VND")

    # Thanh toán
    def checkout(self):
        self.show_cart()

        if not self.order.details:
            return

        print("\n===== THANH TOÁN =====")
        print("1. Tiền mặt")
        print("2. Chuyển khoản")
        print("3. Ví điện tử")

        methods = {
            "1": "Tiền mặt",
            "2": "Chuyển khoản",
            "3": "Ví điện tử"
        }

        choice = input("Chọn phương thức thanh toán: ")

        payment_method = methods.get(choice)

        if payment_method is None:
            print("Phương thức thanh toán không hợp lệ!")
            return

        try:
            self.order.record_payment(payment_method)

            print("\n===== ĐẶT HÀNG THÀNH CÔNG =====")
            print("Mã đơn hàng:", self.order.order_id)
            print("Tổng tiền:", f"{self.order.total_amount:,} VND")
            print("Phương thức:", self.order.payment_method)
            print("Trạng thái:", self.order.payment_status)

        except ValueError as error:
            print("Không thể thanh toán:", error)

    # Giao diện chính
    def run(self):
        while True:
            print("\n========== BĂNG TEA ==========")
            print("1. Xem menu")
            print("2. Thêm món vào giỏ hàng")
            print("3. Xem giỏ hàng")
            print("4. Thanh toán")
            print("0. Thoát")

            choice = input("Nhập lựa chọn: ")

            if choice == "1":
                self.show_menu()
            elif choice == "2":
                self.add_to_cart()
            elif choice == "3":
                self.show_cart()
            elif choice == "4":
                self.checkout()
            elif choice == "0":
                print("Cảm ơn bạn đã sử dụng Băng Tea!")
                break
            else:
                print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    app = CartCheckout()
    app.run()
