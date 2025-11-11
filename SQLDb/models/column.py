from abc import ABC, abstractmethod

class Column(ABC):
    @abstractmethod
    def validate(self):
        pass
