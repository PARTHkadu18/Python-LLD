from location import Location
from vehicle import Vehicle
from ride_sharing import RideSharingServive
from drivers import Drivers
from passengers import Passengers

loc1=Location(15.4241, 81.0484)
loc2=Location(17.6871,82.6217)
loc3=Location(18.9478, 78.4094)

car=Vehicle("CS9999", "Car")
bike=Vehicle("PQ2421", "Bike")

driver1=Drivers("Ravi", loc1, car)
driver2=Drivers("Kavya", loc2, bike)

passenger1=Passengers("Parth", loc3)

rideShareService=RideSharingServive()
rideShareService.add_driver(driver1)
rideShareService.add_driver(driver2)
rideShareService.add_passenger(passenger1)
rideShareService.bookRide(passenger1)