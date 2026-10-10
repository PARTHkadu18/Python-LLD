class Laptop:
    def __init__(self, processor, ram, graphic_card=None, screen_size=None, color=None):
        self.processor = processor
        self.ram = ram
        self.graphic_card = graphic_card
        self.screen_size = screen_size
        self.color = color
        
    def display_specs(self):
        print(f"Processor : {self.processor}")
        print(f"RAM : {self.ram} GB")
        if self.graphic_card:
            print(f"Graphic Card : {self.graphic_card}")
        if self.screen_size:
            print(f"Screen Size : {self.screen_size}")
        if self.color:
            print(f"Color : {self.color}")

laptop1=Laptop("M4", 8)
laptop1.display_specs()
