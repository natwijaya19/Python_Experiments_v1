def calculate_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
