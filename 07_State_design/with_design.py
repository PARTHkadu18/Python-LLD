from abc import ABC, abstractmethod

class TransportMode(ABC):
    @abstractmethod
    def eta(self):
        pass

    @abstractmethod
    def directions(self):
        pass

class Bike(TransportMode):
    def eta(self):
        print("Bike will take 15 minutes")
    
    def directions(self):
        print("Take flyover")

class Walk(TransportMode):
    def eta(self):
        print("Walking will take 30 minutes")

    def directions(self):
        print("Walk left")

class Train(TransportMode):
    def eta(self):
        print("Train will take 5 minutes")

    def directions(self):
        print("Sit in your coach")

class TransportServive:
    def __init__(self,mode: TransportMode):
        self.mode=mode
    
    def setMode(self, newMode: TransportMode):
        self.mode=newMode
    
    def eta(self):
        self.mode.eta()
    
    def directions(self):
        self.mode.directions()