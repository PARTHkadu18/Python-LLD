from location import Location
from vehicle import Vehicle

class Drivers:
    def __init__(self, name, location: Location, vehicle: Vehicle):
        self.name=name
        self.location:Location=location
        self.vehicle:Vehicle=vehicle

    def get_location(self):
        return self.location
    
    def set_location(self, location: Location):
        self.location=location
