from services.parking_lot import ParkingLot
from models.vehicle import Vehicle
from models.parking_floor import ParkingFloor
from models.parking_spot import ParkingSpot
from models.vehicle_types import VehicleType


def run():
    parking_lot = ParkingLot()

    # initialize parking floors and spots
    floor1 = ParkingFloor(floor_number=1)
    floor1.add_parking_spot(ParkingSpot("1A", VehicleType.CAR))
    floor1.add_parking_spot(ParkingSpot("1B", VehicleType.MOTORCYCLE))

    floor2 = ParkingFloor(floor_number=2)
    floor2.add_parking_spot(ParkingSpot("2A", VehicleType.TRUCK))
    floor2.add_parking_spot(ParkingSpot("2B", VehicleType.BUS))

    parking_lot.add_floor(floor1)
    parking_lot.add_floor(floor2)  

    print("Entries")
    floor1.display_avaliability()
    floor2.display_avaliability()

    vehicle1 = Vehicle("ABC123", VehicleType.CAR)
    vehicle2 = Vehicle("XYZ789", VehicleType.MOTORCYCLE)
    vehicle3 = Vehicle("TRK456", VehicleType.TRUCK)

    vehicle1_ticket = parking_lot.park_vehicle(vehicle1)
    vehicle2_ticket = parking_lot.park_vehicle(vehicle2)
    vehicle3_ticket = parking_lot.park_vehicle(vehicle3)

    print("\nAfter Parking")
    floor1.display_avaliability()
    floor2.display_avaliability()

    print("\nUpark Vehicles")
    if vehicle1_ticket:
        parking_lot.unpark_vehicle(vehicle1.get_license_number())
    if vehicle2_ticket:
        parking_lot.unpark_vehicle(vehicle2.get_license_number())

    print("\nAfter Unparking")
    floor1.display_avaliability()
    floor2.display_avaliability()



if __name__ == '__main__':
    run()