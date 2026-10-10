from order import Order

class PizzaOrder(Order):
    def __init__(self,chef):
        self.__chef=chef
    
    def execute(self):
        print("Pizza order")
        self.__chef.cook_pizza()
    