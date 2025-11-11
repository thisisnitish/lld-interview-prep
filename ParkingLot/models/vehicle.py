class Vehicle:
    def __init__(self, license_number, vehicle_type):
        self.license_number = license_number
        self.vehicle_type = vehicle_type

    def get_license_number(self):
        return self.license_number
    
    def get_type(self):
        return self.vehicle_type