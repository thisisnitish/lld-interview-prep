from abc import ABC, abstractmethod

class FeeStrategy(ABC):
    @abstractmethod
    def calculate_fee(self):
        pass


class FlatRateFeeStrategy(FeeStrategy):
    def __init__(self, rate):
        self.rate = rate

    def calculate_fee(self, parking_ticket):
        duration = parking_ticket.get_exit_time() - parking_ticket.get_entry_time()
        hours = (duration // (1000 * 60 * 60)) + 1 # Round up to the next hour
        return hours * self.rate
