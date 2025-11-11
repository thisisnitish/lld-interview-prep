import uuid
from datetime import datetime

class Expense:
    def __init__(self, description, amount, paid_by, participants, split_strategy):
        self.id = str(uuid.uuid4())
        self.description = description
        self.amount = amount
        self.paid_by = paid_by
        self.participants = participants
        self.timestamp = datetime.now()
        self.splits = split_strategy.calculate_splits(amount, participants)

    def get_splits(self):
        return self.splits
    
    def get_description(self):
        return self.description
    
    def get_amount(self):
        return self.amount