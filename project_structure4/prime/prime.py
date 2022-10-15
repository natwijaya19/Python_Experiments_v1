# from helpers import is_prime


class Prime:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def calculate_prime(self) -> list:
        primes = []
        for n in range(self.start, self.end):
            if is_prime(n):
                primes.append(n)
        return primes

    def prettify(self) -> str:
        body = ""
        for result in self.calculate_prime():
            body += f"This is a prime number: {result} \n"

        return body


def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for number in range(2, num):
        if num % number == 0:
            return False
    return True
