from order import Order

class BurgerOrder(Order):
    def __init__(self,chef):
        self.__chef=chef
    
    def execute(self):
        print("Burger order")
        self.__chef.cook_burger()
    