from abc import ABC, abstractmethod

class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass

class Pizza:
    def prepare(self):
        print("Preparing Pizza")

class Burger:
    def prepare(self):
        print("Preparing Burger")

class FoodFactory:
    @staticmethod
    def create_food(food_type):
        if food_type=="pizza":
            return Pizza()
        elif food_type=="burger":
            return Burger()
        else:
            return None

class RestaurantService:
    def create_order(self, food_type):
        p=FoodFactory.create_food(food_type)   
        p.prepare()
        return p

RS=RestaurantService()
order=RS.create_order("pizza")
print(order)
