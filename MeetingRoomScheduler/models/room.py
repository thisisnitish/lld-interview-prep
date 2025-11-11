class Room:
    def __init__(self, id, name, capacity):
        self.id = id
        self.name = name
        self.capacity = capacity
        self.bookings = [] # list of bookings

    def __repr__(self):
        return f"Room({self.name}, cap={self.capacity})"