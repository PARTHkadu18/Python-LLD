class Location:
    def __init__(self, lat, long):
        self.__lat=lat
        self.__long=long

    def get_lat(self):
        return self.__lat
    
    def get_long(self):
        return self.__long