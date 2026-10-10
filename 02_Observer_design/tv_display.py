from observer import Observer

class TVDisplay(Observer):
    def update(self, temp):
        print(f"TV Display updated to {temp}")