import threading

class ParkingFloor:
    def __init__(self, floor_number):
        self.floor_number = floor_number
        self.parking_spots = {}
        self.lock = threading.Lock()

    def add_parking_spot(self, parking_spot):
        self.parking_spots[parking_spot.get_spot_id()] = parking_spot

    def find_available_spot(self, vehicle):
        with self.lock:
            for spot in self.parking_spots.values():
                if spot.can_fit_vehicle(vehicle):
                    return spot
            
            return None
    
    def display_avaliability(self):
        print(f"Parking Floor {self.floor_number} Availability:")
        available_spots = {}
        for spot in self.parking_spots.values():
            if not spot.is_spot_occupied():
                available_spots[spot.get_vehicle_type()] = available_spots.get(spot.get_vehicle_type(), 0) + 1

        for vehicle_type, count in available_spots.items():
            print(f"  {vehicle_type.name}: {count} spots available")
