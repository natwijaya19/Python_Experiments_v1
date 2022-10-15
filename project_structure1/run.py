import constants as c
import helpers


def run():
    primes = helpers.calculate_primes(start=c.START, end=c.END)
    print(primes)


if __name__ == "__main__":
    run()

# %%============================================================================


