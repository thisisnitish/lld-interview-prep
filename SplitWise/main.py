from models.user import User
from models.group import Group
from models.expense import Expense
from models.transaction import Transaction
from services.splitwise import Splitwise
from strategies.split_strategies import EqualSplitStrategy

def run():
    split_wise = Splitwise()
    u1 = split_wise.add_user("Alice")
    u2 = split_wise.add_user("Bob")
    u3 = split_wise.add_user("Charlie")

    g1 = split_wise.add_group("Trip1", [u1, u2, u3])

    split_wise.create_expense("Dinner", 370, u1, [u1, u2, u3], EqualSplitStrategy())

    split_wise.show_balance_sheet(u1.get_id())
    split_wise.show_balance_sheet(u2.get_id())
    split_wise.show_balance_sheet(u3.get_id())

    print("Simplify debts---")
    simplified_debts = split_wise.simplify_group_debts(g1.get_id(), apply=True)
    if not simplified_debts:
        print("All debts are settled within the group!")
    else:
        for debt in simplified_debts:
            print(debt.get_description())
    print()

    # split_wise.show_balance_sheet(u1.get_id())
    split_wise.show_balance_sheet(u2.get_id())
    print()
    split_wise.show_balance_sheet(u3.get_id())


if __name__ == "__main__":
    run()