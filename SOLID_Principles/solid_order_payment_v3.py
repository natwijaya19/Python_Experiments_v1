# A magic command for Jupyter Notebook.
# %%============================================================================
from typing import Any


class Order:
    # noinspection PyCompatibility
    items: list[Any] = []
    # noinspection PyCompatibility
    quantities: list[Any] = []
    # noinspection PyCompatibility
    prices: list[Any] = []
    # noinspection PyCompatibility
    status: str = "Open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


class PaymentProcessor:
    @staticmethod
    def pay_debit(order, security_code):
        print("Processing debit payment type")
        print("Verifying security code: {security_code}".format(security_code=security_code))
        print("Payment successful")
        order.status = "paid"

    @staticmethod
    def pay_credit(order, security_code):
        print("Processing credit payment type")
        print("Verifying security code: {security_code}".format(security_code=security_code))
        print("Payment successful")
        order.status = "paid"


if __name__ == "__main__":
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB Cable", 5, 10)

    print(order.status)
    processor = PaymentProcessor()
    processor.pay_debit(order, 1234)

    print(order.total_price())
    print(order.status)

# %%============================================================================
