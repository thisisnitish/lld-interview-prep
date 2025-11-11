from abc import ABC, abstractmethod

class ConflictCheckerStrategy(ABC):
    @abstractmethod
    def has_conflict(self):
        pass


class SimpleConflictCheckerStrategy(ConflictCheckerStrategy):
    def has_conflict(self, new_booking, existing_bookings):
        for booking in existing_bookings:
            if new_booking.overlaps(booking):
                return True
        return False

