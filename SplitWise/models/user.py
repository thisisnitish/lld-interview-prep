import uuid
from models.balance_sheet import BalanceSheet

class User:
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
        self.balance_sheet = BalanceSheet(self)

    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id
    
    def get_balance_sheet(self):
        return self.balance_sheet