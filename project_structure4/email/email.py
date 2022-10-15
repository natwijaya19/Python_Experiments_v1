class Email:
    def __init__(self) -> None:
        self.to = None
        self.subject = None
        self.body = None

    def send(self) -> None:
        print(f"Sending email to {self.to}")
        print(f"Subject: {self.subject}")
        print(f"Body: {self.body}")
        print("Email sent!")
