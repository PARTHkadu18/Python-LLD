class Laptop:
    processor = None
    ram = None
    graphic_card = None
    screen_size = None
    color = None

    def display_specs(self):
        if self.processor:
            print(f"Processor : {self.processor}")
        if self.ram:
            print(f"RAM : {self.ram} GB")
        if self.graphic_card:
            print(f"Graphic Card : {self.graphic_card}")
        if self.screen_size:
            print(f"Screen Size : {self.screen_size}")
        if self.color:
            print(f"Color : {self.color}")
    
class LaptopBuilder:
    def __init__(self):
        self.__laptop=Laptop()
    
    def set_processor(self,processor):
        self.__laptop.processor=processor
        return self
    
    def set_ram(self,ram):
        self.__laptop.ram=ram
        return self
    
    def set_graphic_card(self,graphic_card):
        self.__laptop.graphic_card=graphic_card
        return self
    
    def set_screen_size(self,screen_size):
        self.__laptop.screen_size=screen_size
        return self
    
    def set_color(self,color):
        self.__laptop.color=color
        return self
    
    def build(self):
        return self.__laptop

l=LaptopBuilder().set_processor("M5").set_ram(16).set_color("Blue").build().display_specs()
