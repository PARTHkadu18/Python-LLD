from vehicle import Vehicle
from typing import List
from drivers import Drivers
from passengers import Passengers
from location import Location

class RideSharingServive:
    def __init__(self):
        self.drivers:List[Drivers] = []
        self.passengers:List[Passengers] = []

    def add_driver(self, driver: Drivers):
        self.drivers.append(driver)

    def add_passenger(self, passenger: Passengers):
        self.passengers.append(passenger)

    def __calcDistance(self, location1: Location, location2: Location):
        dx: float=location1.get_lat()-location2.get_lat()
        dy: float=location1.get_long()-location2.get_long()
        return (dx*dx+dy*dy)**0.5

    def __calcFare(self, vehicle: Vehicle, distance: float):
        if vehicle.type=="Car":
            return distance*20
        elif vehicle.type=="Bike":
            return distance*12
        else:
            return distance*8

    def bookRide(self, passenger: Passengers):
        if len(self.drivers) == 0:
            print("No drivers available for {passengers.name}")
            return
        
        assignedDriver=None
        minDistance=float("inf")
        for driver in self.drivers:
            currentDriverDistance=self.__calcDistance(passenger.location, driver.location)
            if currentDriverDistance<minDistance:
                minDistance=currentDriverDistance
                assignedDriver=driver

        expectedFair:float=self.__calcFare(assignedDriver.vehicle, minDistance)
        print(f"Ride booked for {passenger.name} with driver {assignedDriver.name} with fare of Rs.{expectedFair}")