from abc import ABC, abstractmethod

class ParkingStrategy(ABC):
    @abstractmethod
    def find_parking_spot(self):
        pass

class NearestFirstParkingStrategy(ParkingStrategy):
    def find_parking_spot(self, floors, vehicle):
        for floor in floors:
            spot = floor.find_available_spot(vehicle)
            if spot is not None:
                return spot
        
        return None
    

class FarthestFirstParkingStrateg(ParkingStrategy):
    def find_parking_spot(self, floors, vehicle):
        reversed_floors = list(reversed(floors))
        for floor in reversed_floors:
            spot = floor.find_available_spot(vehicle)
            if spot is not None:
                return spot
            
        return None