from abc import ABC, abstractmethod

class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass

# ====North Indian====

class PannerTikka(Food):
    def prepare(self):
        print("Preparing Panner Tikka")

class ButterChicken(Food):
    def prepare(self):
        print("Preparing Butter Chicken")

class GulabJamun(Food):
    def prepare(self):
        print("Preparing Gulab Jamun")


# ====South India====

class Idli(Food):
    def prepare(self):
        print("Preparing Idli")

class Dosa(Food):
    def prepare(self):
        print("Preparing Dosa")

class Payasam(Food):
    def prepare(self):
        print("Preparing Payasam")

# ====Chinese====

class SpringRolls(Food):
    def prepare(self):
        print("Preparing Spring Rolls")

class FriedRice(Food):
    def prepare(self):
        print("Preparing Fried Rice")

class FortuneCookie(Food):
    def prepare(self):
        print("Preparing Fortune Cookie")

class RestaurantService:
    def create_meal(self, cuisine_type):
        if cuisine_type=="north_indian":
            starter=PannerTikka() 
            main_course=ButterChicken()
            dessert=GulabJamun()
        elif cuisine_type=="south_indian":
            starter=Idli()
            main_course=Dosa()
            dessert=Payasam()
        elif cuisine_type=="chinese":
            starter=SpringRolls()
            main_course=FriedRice()
            dessert=FortuneCookie()
        else:
            print("Cuisine not available")
            return None

        starter.prepare()
        main_course.prepare()
        dessert.prepare()

restaurant=RestaurantService()
print("Making order 1:")
restaurant.create_meal("north_indian")
print("\nMaking order 2:")
restaurant.create_meal("south_indian")