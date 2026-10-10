from observer import Observer

class WeatherStation:
    def __init__(self):
        self.__temperature=0
        self.__observers=[]

    def updateTemp(self, temp):
        self.__temperature=temp

    def addObserver(self, ob):
        self.__observers.append(ob)

    def removeOb(self,ob):
        self.__observers.remove(ob)

    def notifyObservers(self):
        for ob in self.__observers:
            ob.update(self.__temperature)