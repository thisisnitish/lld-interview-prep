import threading

from strategies.fee_strategy import FlatRateFeeStrategy
from strategies.parking_strategy import NearestFirstParkingStrategy
from models.parking_ticket import ParkingTicket

def singleton(cls):
    instances = {}
    lock = threading.Lock()

    def get_instance(*args, **kwargs):
        with lock:
            if cls not in instances:
                instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

@singleton
class ParkingLot:
    def __init__(self):
        self.floors = [] # List of ParkingFloor objects
        self.active_tickets = {} # ticket_id -> ParkingTicket
        self.fee_strategy = FlatRateFeeStrategy(rate=10)
        self.parking_strategy = NearestFirstParkingStrategy()
        self.lock = threading.Lock()

    def add_floor(self, parking_floor):
        self.floors.append(parking_floor)

    def set_fee_strategy(self, fee_strategy):
        self.fee_strategy = fee_strategy

    def park_vehicle(self, vehicle):
        with self.lock:
            spot = self.parking_strategy.find_parking_spot(self.floors, vehicle)
            if spot:
                spot.park_vehicle(vehicle)
                ticket = ParkingTicket(vehicle, spot)
                self.active_tickets[vehicle.get_license_number()] = ticket
                print(f"Vehicle parked {vehicle.get_license_number()}. Ticket ID: {ticket.get_ticket_id()}")
                return ticket
            else:
                print("No available parking spot.")
                return None
        
    def unpark_vehicle(self, license_number):
        with self.lock:
            ticket = self.active_tickets.pop(license_number, None)
            if ticket is None:
                print("Invalid ticket or vehicle not found.")
                return None
            
            ticket.get_spot().unpark_vehicle()
            ticket.set_exit_time()
            fee = self.fee_strategy.calculate_fee(ticket)
            print(f"Vehicle unparked {license_number}. Parking fee: {fee}")
            return fee

