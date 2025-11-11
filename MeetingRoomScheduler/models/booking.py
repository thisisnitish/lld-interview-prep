class Booking:
    def __init__(self, id, room_id, user_id, start, end):
        self.id = id
        self.room_id = room_id
        self.user_id = user_id
        self.start = start
        self.end = end

    def overlaps(self, other):
        return self.start < other.end and other.start < self.end
    
    def __repr__(self):
        return f"Booking({self.booking_id}, room={self.room_id}, {self.start.time()} - {self.end.time()})"