from enum import Enum

class TransportMode(Enum):
    WALKING = "walking"
    BIKE = "bike"
    TRAIN = "train"

class TransportService:

    def __init__(self, mode: TransportMode):
        self.mode = mode

    def setMode(self, newMode: TransportMode):
        self.mode=newMode
    
    def eta(self):
        if self.mode == TransportMode.WALKING:
            print("Walking will take 30 minutes")
        elif self.mode == TransportMode.BIKE:
            print("Bike will take 15 minutes")
        elif self.mode == TransportMode.TRAIN:
            print("Train will take 5 minutes")
        
    def directions(self):
        if self.mode == TransportMode.WALKING:
            print("Walk left")
        elif self.mode == TransportMode.BIKE:
            print("Take flyover")
        elif self.mode == TransportMode.TRAIN:
            print("Sit in your coach")
    
