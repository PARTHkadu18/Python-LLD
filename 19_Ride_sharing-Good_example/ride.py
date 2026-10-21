from fare_strategy import FareStrategy
from drivers import Drivers
from passengers import Passengers
from enum import Enum

class RideStatus(Enum):
    SCHEDULED="SCHEDULED"
    ONGOING="ONGOING"
    COMPLETED="COMPLETED"

class Ride:
    def __init__(self, passenger:Passengers, driver:Drivers, distance:float, fare_strategy:FareStrategy):
        self.passenger=passenger
        self.driver=driver
        self.fare_strategy=fare_strategy
        self.status=RideStatus.SCHEDULED
        self.distance=distance
        self.fare=0

    def calculateFare(self):
        self.fare=self.fare_strategy.calFare(self.driver.get_vehicle(), self.distance)

    def getRideFare(self):
        return self.fare

    def updateStatus(self, new_ride_status: RideStatus):
        self.status=new_ride_status
        self.__notifyUsers(self.status)

    def __notifyUsers(self, ride_status: RideStatus):
        self.driver.notify(f"Your ride is {ride_status.value}")
        self.passenger.notify(f"Your ride is {ride_status.value}")