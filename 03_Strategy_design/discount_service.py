class DiscountService:
    def __init__(self, discout_str):
        self.__discout_str=discout_str

    def set_str(self, new_dis_str):
        self.__discout_str=new_dis_str
    
    def process(self):
        return self.__discout_str.calculate_dis(100)