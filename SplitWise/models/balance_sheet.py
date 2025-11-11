class BalanceSheet:
    def __init__(self, owner):
        self.owner = owner
        self.balances = {} # {user: amount}

    def get_balances(self):
        return self.balances
    
    def adjust_balance(self, other_user, amount):
        if self.owner == other_user:
            return
        
        if other_user in self.balances:
            self.balances[other_user] += amount
        else:
            self.balances[other_user] = amount
        

    def show_balances(self):
        if not self.balances:
            print("All settled up!!")
            return
        
        total_owed_to_me = 0
        total_i_owe = 0

        for other_user, amount in self.balances.items():
            if amount > 0.01:
                print(f"{other_user.get_name()} owes {self.owner.get_name()} ${amount:.2f}")
                total_owed_to_me += amount
            elif amount < -0.01:
                print(f"{self.owner.get_name()} owes {other_user.get_name()} ${-amount:.2f}")
                total_i_owe += (-amount)

        print(f"Total Owed to {self.owner.get_name()}: ${total_owed_to_me:.2f}")
        print(f"Total {self.owner.get_name()} Owes: ${total_i_owe:.2f}")