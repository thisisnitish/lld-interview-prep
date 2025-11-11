import threading

class ParkingSpot:
    def __init__(self, spot_id, vehicle_type):
        self.spot_id = spot_id
        self.vehicle_type = vehicle_type
        self.is_occupied = False
        self.parked_vehicle = None
        self.lock = threading.Lock()

    def get_spot_id(self):
        return self.spot_id
    
    def get_vehicle_type(self):
        return self.vehicle_type
    
    def is_spot_occupied(self):
        return self.is_occupied
    
    def park_vehicle(self, vehicle):
        with self.lock:
            self.park_vehicle = vehicle
            self.is_occupied = True

    def unpark_vehicle(self):
        with self.lock:
            self.parked_vehicle = None
            self.is_occupied = False

    def can_fit_vehicle(self, vehicle):
        if self.is_occupied:
            return False
        return vehicle.get_type() == self.vehicle_type