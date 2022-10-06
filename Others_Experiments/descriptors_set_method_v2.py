# %%============================================================================
from typing import Callable, Any


class Validation:
    def __init__(self, validation_function: Callable[[Any], bool], error_message: str) -> None:
        self.validation_function = validation_function
        self.error_message = error_message

    def __call__(self, value: Any) -> None:
        if not self.validation_function(value):
            raise ValueError(f"{value!r} {self.error_message}")


class Field:
    def __init__(self, *validations) -> None:
        self._name = None
        self.validations = validations

    def __set_name__(self, owner, name):
        self_name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self._name]

    def validate(self, value: Any) -> None:
        for validation in self.validations:
            validation(value)

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self._name] = value


class ClientClass:
    validation_number = Validation(lambda x: isinstance(x, (int, float)), "is not a number")
    validation_positive = Validation(lambda x: x > 0, "is not positive")
    descriptor = Field(validation_number, validation_positive)


if __name__ == '__main__':
    client = ClientClass()
    client.descriptor = 42
    print(client.descriptor)

    # client.descriptor = -1
    # print(client.descriptor)

    client.descriptor = "hello"
    print(client.descriptor)
