from fare_strategy import LuxuryFareStrategy
from location import Location
from ride_matching_service import RideMatchingService
from drivers import Drivers
from passengers import Passengers
from car import Car
from bike import Bike

loc1=Location(15.4241, 81.0484)
loc2=Location(17.6871,82.6217)
loc3=Location(18.9478, 78.4094)

car=Car("CS9999")
bike=Bike("PQ2421")

driver1=Drivers("Ravi", "driver1@gmail.com", loc1, car)
driver2=Drivers("Kavya", "driver1@gmail.com", loc2, car)

passenger1=Passengers("Parth", "passenger1@gmail.com", loc3)

rideMatchingService=RideMatchingService()
rideMatchingService.add_driver(driver1)
rideMatchingService.add_driver(driver2)
rideMatchingService.requestRide(passenger1,10,LuxuryFareStrategy())