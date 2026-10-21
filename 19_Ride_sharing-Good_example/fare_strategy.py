from vehicle import Vehicle
from abc import ABC, abstractmethod

class FareStrategy(ABC):
    @abstractmethod
    def calFare(self, vehicle: Vehicle, distance):
        pass

class StandardFareStratey(FareStrategy):
    def calFare(self, vehicle: Vehicle, distance: float):
        return vehicle.get_fare_amount()*distance

class SharedFareStrategy(FareStrategy):
    def calFare(self, vehicle: Vehicle, distance: float):
        return (vehicle.get_fare_amount()*distance)*0.65

class LuxuryFareStrategy(FareStrategy):
    def calFare(self, vehicle: Vehicle, distance: float):
        return (vehicle.get_fare_amount()*distance)*1.3

    