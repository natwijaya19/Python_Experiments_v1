from project_structure_fix_ImportModuleNotFoundError.email.email import Email
from project_structure_fix_ImportModuleNotFoundError.prime import constants as c
from project_structure_fix_ImportModuleNotFoundError.prime import prime


def run():
    p = prime.Prime(start=c.START, end=c.END)
    prettier = p.prettify()
    print(prettier)

    new_email = Email()
    new_email.to = "johndoe@example.com"
    new_email.subject = f"Prime Numbers execution from {c.START} to {c.END}"
    new_email.body = prettier
    new_email.send()


if __name__ == "__main__":
    run()

# %%====================================================

# if __name__ == "__main__":
#     from prime.helpers import is_prime
#     result = is_prime(35)
#     print(result)
