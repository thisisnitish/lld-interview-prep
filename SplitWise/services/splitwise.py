from models.user import User
from models.group import Group
from models.expense import Expense
from models.transaction import Transaction

class Splitwise:
    def __init__(self):
        self.users = {}
        self.groups = {}


    def add_user(self, name):
        user = User(name)
        self.users[user.get_id()] = user
        return user
    
    def add_group(self, name, members):
        group = Group(name, members)
        self.groups[group.get_id()] = group
        return group

    def create_expense(self, description, amount, paid_by, participants, split_strategy):
        expense = Expense(description, amount, paid_by, participants, split_strategy)

        for split in expense.get_splits():
            particpant = split.get_user()
            amount_p = split.get_amount()

            if paid_by != particpant:
                paid_by.get_balance_sheet().adjust_balance(particpant, amount_p)
                particpant.get_balance_sheet().adjust_balance(paid_by, -amount_p)
        
        print(f"Expense '{expense.get_description()}' of amount {expense.get_amount()} created.")


    def settle_up(self, payer_id, payee_id, amount):
        payer = self.users[payer_id]
        payee = self.users[payee_id]

        print(f"{payer.get_name()} is settling up {amount} with {payee.get_name()}")

        # Settlement is like a reverse expense. payer owes less to payee.
        payee.get_balance_sheet().adjust_balance(payer, -amount)
        payer.get_balance_sheet().adjust_balance(payee, amount)


    def show_balance_sheet(self, user_id: str):
        user = self.users[user_id]
        user.get_balance_sheet().show_balances()

    def simplify_group_debts(self, group_id, apply = False):
        group = self.groups[group_id]

        if group is None:
            return "No Group!!"
        
        net_balances= {}

        for member in group.get_members():
            balance = 0
            for other_user, amount in member.get_balance_sheet().get_balances().items():
                # Consider only balances with other group members
                if other_user in group.get_members():
                    balance += amount

            net_balances[member] = balance


        # Separate into creditors and debtors
        creditors = [(user, balance) for user, balance in net_balances.items() if balance > 0]
        debitors = [(user, balance) for user, balance in net_balances.items() if balance < 0]
        
        creditors.sort(key=lambda x: x[1], reverse=True)
        debitors.sort(key=lambda x: x[1])
        
        transactions = []
        i = j = 0

        while i < len(creditors) and j < len(debitors):
            creditor_user, creditor_amount = creditors[i]
            debitor_user, debitor_amount = debitors[j]
            
            amount_to_settle = min(creditor_amount, -debitor_amount)
            transactions.append(Transaction(debitor_user, creditor_user, amount_to_settle))
            
            creditors[i] = (creditor_user, creditor_amount - amount_to_settle)
            debitors[j] = (debitor_user, debitor_amount + amount_to_settle)
            
            if abs(creditors[i][1]) < 0.01:
                i += 1
            if abs(debitors[j][1]) < 0.01:
                j += 1

        for transaction in transactions:
            if apply:
                payer = transaction.from_user
                payee = transaction.to_user
                amount = transaction.amount
                payee.get_balance_sheet().adjust_balance(payer, -amount)
                payer.get_balance_sheet().adjust_balance(payee, amount)

        
        return transactions
                

    
    