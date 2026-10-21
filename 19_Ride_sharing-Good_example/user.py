from location import Location
from abc import ABC,abstractmethod

class User(ABC):
    def __init__(self, name: str, email: str, location: Location):
        self.name=name
        self.email=email
        self.location=location

    def get_location(self):
        return self.location

    @abstractmethod
    def notify(self,msg):
        pass