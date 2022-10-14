# %% SOLID principles - Order Payment: Interface segregation principle
import typing


# define a class for Order
class Order:
    items: list[typing.Any] = []
    quantities: list[typing.Any] = []
    prices: list[typing.Any] = []
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


class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self):
        pass


class SMSAuth(Authorizer):
    def __init__(self):
        self.authorized = False

    def verify_code(self, SMS_code):
        print("SMS authorization")
        print(f"Verifying SMS code: {SMS_code}")
        self.authorized = True

    def is_authorized(self):
        return self.authorized


class NotARobotAuth(Authorizer):
    def __init__(self):
        self.authorized = False

    def verify_code(self, captcha_code):
        print("not a robot authorization")
        print(f"Verifying captcha code: {captcha_code}")
        self.authorized = True

    def is_authorized(self):
        return self.authorized


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: int, authorizer: Authorizer):
        self.authorizer = authorizer
        self.security_code = security_code

    def pay(self, order_input: Order):
        if not self.authorizer.is_authorized():
            raise Exception("Payment not authorized")
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
    def __init__(self, email_address: str, authorizer: Authorizer):
        self.authorizer = authorizer
        self.email_address = email_address

    def pay(self, order_input: Order):
        if not self.authorizer.is_authorized():
            raise Exception("Payment not authorized")
        print("Processing paypal payment type")
        print(f"Verifying email address: {self.email_address}")
        print("Payment successful")
        order_input.status = "paid"


if __name__ == "__main__":
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB Cable", 5, 10)

    print(order.status)
    payment_authorizer = SMSAuth()
    processor = DebitPaymentProcessor(1234, payment_authorizer)
    payment_authorizer.verify_code(1234)
    processor.pay(order)

    print(order.total_price())
    print(order.status)

# other order example
    order = Order()
    order.add_item("Keyboard", 2, 50)
    order.add_item("SSD", 2, 150)
    order.add_item("USB Cable", 2, 10)

    print(order.status)
    payment_authorizer = NotARobotAuth()
    processor = PaypalPaymentProcessor(email_address="kiki@gmail.com", authorizer=payment_authorizer)
    payment_authorizer.verify_code(1234)
    processor.pay(order)

    print(order.total_price())
    print(order.status)
