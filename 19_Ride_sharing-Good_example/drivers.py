from vehicle import Vehicle
from user import User

class Drivers(User):
    def __init__(self, name, email, location, vehicle:Vehicle):
        super().__init__(name,email,location)
        self.__vehicle=vehicle

    def get_vehicle(self):
        return self.__vehicle
    
    def notify(self, msg):
        print(f"Notiy to driver ({self.name}) = {msg}")