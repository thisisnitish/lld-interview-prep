class Transaction:
    def __init__(self, from_user, to_user, amount):
        self.from_user = from_user
        self.to_user = to_user
        self.amount = amount

    def get_description(self):
        return f"{self.from_user.get_name()} should pay {self.to_user.get_name()} ${self.amount:.2f}"