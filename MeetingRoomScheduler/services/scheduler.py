import threading
from models.room import Room
from models.booking import Booking

class Scheduler:
    def __init__(self, conflict_checker):
        self.rooms = {}
        self.bookings = {}
        self.conflict_checker = conflict_checker
        self.lock = threading.Lock()
        self.subscribers = [] # observers to notify

    def add_room(self, id, name, capacity):
        room = Room(id, name, capacity)
        self.rooms[id] = room

    def subscribe(self, fn):
        self.subscribers.append(fn)

    def notify(self, message):
        for subscriber in self.subscribers:
            subscriber(message)

    def book_room(self, room_id, user_id, start, end):
        with self.lock:
            room = self.rooms[room_id]
            if not room:
                print("Room not found")
                return
            
            new_booking = Booking(len(self.bookings)+1, room_id, user_id, start, end)
            if self.conflict_checker.has_conflict(new_booking, room.bookings):
                print(f"[{user_id}] Booking conflict for {room.name}")
                return

            self.bookings[new_booking.id] = new_booking
            room.bookings.append(new_booking)
            self.notify(f"Booking confirmed for {room.name} by {user_id}")
            return new_booking

    def cancel_booking(self, booking_id):
        with self.lock:
            booking = self.bookings[booking_id]
            if not booking:
                print("No booking found")
                return
            
            room = self.rooms[booking.room_id]
            update_bookings = []
            for booking in room.bookings:
                if booking.id != booking_id:
                    update_bookings.append(booking)

            room.bookings = update_bookings
            self.notify(f"Booking {booking_id} cancelled")

    def show_schedule(self, room_id):
        room = self.rooms[room_id]
        if not room:
            print("No room found!!")
            return
        
        print(f"Schedule for Room {room_id}")
        for b in room.bookings:
            print(f"  {b.start.time()} - {b.end.time()} by {b.user_id}")