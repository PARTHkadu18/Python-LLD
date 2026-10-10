from abc import ABC, abstractmethod
from typing import List
class AirTraficControl(ABC):
    @abstractmethod
    def register_plane(self):
        pass

    def send_message(self):
        pass

class ControlTower(AirTraficControl):
    def __init__(self):
        self.__airplane:List[Airplane]=[]

    def register_plane(self,plane:Airplane):
        self.__airplane.append(plane)

    def send_message(self, plane:Airplane, message:str):
        for p in self.__airplane:
            if p != plane:
                p.recieve_message(message, plane)

class Airplane:
    def __init__(self, flight_number:str, tower:AirTraficControl):
        self.__flight_number=flight_number
        self.__tower=tower
        self.__tower.register_plane(self)

    def send_message(self,message:str):
        self.__tower.send_message(self,message)
    
    def get_flight_number(self):
        return self.__flight_number

    def recieve_message(self, msg:str, sender: Airplane):
        print(f"{sender.get_flight_number()} sent the message {msg} to {self.__flight_number}")
    
