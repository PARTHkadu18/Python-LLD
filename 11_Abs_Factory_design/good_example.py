from abc import ABC, abstractmethod

class Starter(ABC):
    @abstractmethod
    def prepare(self):
        pass

class MainCourse(ABC):
    @abstractmethod
    def prepare(self):
        pass

class Dessert(ABC):
    @abstractmethod
    def prepare(self):
        pass

# ====North Indian====

class PannerTikka(Starter):
    def prepare(self):
        print("Preparing Panner Tikka")

class ButterChicken(MainCourse):
    def prepare(self):
        print("Preparing Butter Chicken")

class GulabJamun(Dessert):
    def prepare(self):
        print("Preparing Gulab Jamun")


# ====South India====

class Idli(Starter):
    def prepare(self):
        print("Preparing Idli")

class Dosa(MainCourse):
    def prepare(self):
        print("Preparing Dosa")

class Payasam(Dessert):
    def prepare(self):
        print("Preparing Payasam")

# ====Chinese====

class SpringRolls(Starter):
    def prepare(self):
        print("Preparing Spring Rolls")

class FriedRice(MainCourse):
    def prepare(self):
        print("Preparing Fried Rice")

class FortuneCookie(Dessert):
    def prepare(self):
        print("Preparing Fortune Cookie")

class CuisineFactory(ABC):
    @abstractmethod
    def create_starter(self):
        pass

    @abstractmethod
    def create_main_course(self):
        pass

    @abstractmethod
    def create_dessert(self):
        pass

class NorthIndianCuisine(CuisineFactory):
    def create_starter(self):
        return PannerTikka()
    
    def create_main_course(self):
        return ButterChicken()

    def create_dessert(self):
        return GulabJamun()


class RestaurantService:
    def __init__(self, factory: CuisineFactory):
        self.__factory = factory

    def create_meal(self):
        starter=self.__factory.create_starter()
        main=self.__factory.create_main_course()
        dessert=self.__factory.create_dessert()

        starter.prepare()
        main.prepare()
        dessert.prepare()

nic=NorthIndianCuisine()
rs=RestaurantService(nic)
print("Making order 1:")
rs.create_meal()
