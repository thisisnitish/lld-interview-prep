from abc import ABC, abstractmethod
from models.split import Split

class SplitStrategy(ABC):
    @abstractmethod
    def calculate_splits(self):
        pass


class EqualSplitStrategy(SplitStrategy):
    def calculate_splits(self, total_amount, participants):
        splits = []
        amount_per_person = total_amount / len(participants)
        for particpant in participants:
            splits.append(Split(particpant, amount_per_person))
        return splits