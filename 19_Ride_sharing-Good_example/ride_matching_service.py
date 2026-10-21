from fare_strategy import FareStrategy
from location import Location
from passengers import Passengers
from typing import List
from drivers import Drivers
from ride import Ride, RideStatus

class RideMatchingService:
    def __init__(self):
        self.__available_drivers: List[Drivers]=[]

    def add_driver(self, driver: Drivers):
        self.__available_drivers.append(driver)
    
    def requestRide(self, passenger: Passengers, distance: float, stratrey: FareStrategy):
        if len(self.__available_drivers)==0:
            passenger.notify("No Drivers available")
            return

        # Nearest Driver
        nearestDriver: Drivers = self.__findNearestDriver(passenger.get_location())
        self.__available_drivers.remove(nearestDriver)
        ride: Ride = Ride(passenger, nearestDriver, distance, stratrey)
        ride.calculateFare()

        passenger.notify(f"Ride has been scheduled with Rs.{ride.getRideFare()}")
        nearestDriver.notify(f"You have one new ride for Rs.{ride.getRideFare()}")

        ride.updateStatus(RideStatus.ONGOING)

        #After some time
        ride.updateStatus(RideStatus.COMPLETED)
        self.__available_drivers.append(nearestDriver)

        return 

    def __findNearestDriver(self, location: Location):
        assignedDriver=None
        minimumDistance=float("inf")
        for driver in self.__available_drivers:
            dist=driver.get_location().calcDistance(location)
            if dist < minimumDistance:
                minimumDistance=dist
                assignedDriver=driver
        return assignedDriver 
        