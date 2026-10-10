from discount_strategy import DiscountStrategy

class HoliDis(DiscountStrategy):
    def calculate_dis(self,amount):
        print("Applying holi discount")