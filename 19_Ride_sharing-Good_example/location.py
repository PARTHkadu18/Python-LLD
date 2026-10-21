class Location:
    def __init__(self, lat: float, long: float):
        self.__lat=lat
        self.__long=long

    def get_lat(self):
        return self.__lat
    
    def get_long(self):
        return self.__long
    
    def calcDistance(self, location: Location):
        dx: float=self.__lat-location.get_lat()
        dy: float=self.__long-location.get_long()
        return (dx*dx+dy*dy)**0.5
