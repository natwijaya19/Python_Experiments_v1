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

    def pay(self, payment_type, security_code):
        if payment_type == "debit":
            # pay with debit card
            print("Processing debit payment type")
            print("Verifying security code: {security_code}".format(security_code=security_code))
            print("Payment successful")
            self.status = "paid"
        elif payment_type == "credit":
            # pay with credit card
            print("Processing credit payment type")
            print("Verifying security code: {security_code}".format(security_code=security_code))
            print("Payment successful")
            self.status = "paid"
        else:
            raise Exception("unknown payment type: {payment_type}".format(payment_type=payment_type))


if __name__ == "__main__":
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB Cable", 5, 10)

    print(order.status)
    order.pay("debit", 1234)

    print(order.total_price())
    print(order.status)

# %%
