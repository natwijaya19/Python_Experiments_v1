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


from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order_input):
        pass


class PaymentProcessorSMS(PaymentProcessor):
    @abstractmethod
    def auth_SMS(self, code):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: int):
        self.security_code = security_code
        self.verified = False

        def auth_SMS(self, SMS_Code: int):
            print("verifying SMS code: {SMS_Code}".format(SMS_Code=SMS_Code))
            if self.security_code == SMS_Code:
                self.verified = True
            else:
                self.verified = False

    def pay(self, order_input: Order):
        print("Processing debit payment type")
        print("Verifying security code: {security_code}".format(security_code=self.security_code))
        print("Payment successful")
        order_input.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: int):
        self.security_code = security_code

    def pay(self, order_input: Order):
        print("Processing credit payment type")
        print("Verifying security code: {security_code}".format(security_code=self.security_code))
        print("Payment successful")
        order_input.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_address: str):
        self.email_address = email_address
        self.verified = False

        def auth_SMS(self, SMS_Code: int):
            print("verifying SMS code: {SMS_Code}".format(SMS_Code=SMS_Code))
            if self.security_code == SMS_Code:
                self.verified = True
            else:
                self.verified = False

    def pay(self, order_input: Order):
        print("Processing paypal payment type")
        print("Verifying security code: {email_address}".format(email_address=self.email_address))
        print("Payment successful")
        order_input.status = "paid"


if __name__ == "__main__":
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB Cable", 5, 10)

    print(order.status)
    processor = PaypalPaymentProcessor("kiki.mulyadi@psn.co.id")
    processor.pay(order)

    print(order.total_price())
    print(order.status)
