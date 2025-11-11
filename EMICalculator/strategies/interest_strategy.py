from abc import ABC, abstractmethod

class InterestStrategy(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass