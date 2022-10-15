import prime.constants as c
import prime.prime as p
from email.email import Email


def run() -> None:
    primes = p.Prime(c.START, c.END)
    prettier = primes.prettify()
    print(prettier)
    new_email = Email()
    new_email.to = "JohnDoe@email.com"
    new_email.subject = f"Prime numbers execution between {c.START} and {c.END}"
    new_email.body = prettier
    new_email.send()


if __name__ == "__main__":
    run()


# %%============================================================================
