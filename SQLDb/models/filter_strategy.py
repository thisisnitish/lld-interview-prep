from abc import ABC, abstractmethod

class FilterStrategy(ABC):
    @abstractmethod
    def apply_filter(self):
        pass

class EqualFilterStrategy(FilterStrategy):
    def apply_filter(self, records, column, value):
        filtered_records = []
        for record in records:
            if record[column] == value:
                filtered_records.append(record)

        return filtered_records