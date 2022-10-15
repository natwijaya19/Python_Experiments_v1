# from helpers import is_prime


class Prime(object):
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def calculate_primes(self) -> list:
        primes = []
        for num in range(self.start, self.end + 1):
            if self.is_prime(num):
                primes.append(num)
        return primes

    def prettify(self) -> str:
        body = ""
        for prime in self.calculate_primes():
            body += f"{prime} is prime"
        return body

    @staticmethod
    def is_prime(num: int) -> bool:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


# %%============================================================================
