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

class RestaurantServie:
    def create_order(self, food_type:str):

        if food_type=="pizza":
            f=Pizza()
        elif food_type=="burger":
            f=Burger()
        else:
            print("Invalid food type")
            return None
        f.prepare();
        return f

rs=RestaurantServie()
order=rs.create_order("pizza")
print(order)
    