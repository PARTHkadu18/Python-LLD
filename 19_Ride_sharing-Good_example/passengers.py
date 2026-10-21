from user import User

class Passengers(User):
    def __init__(self, name, email, location):
        super().__init__(name,email,location)

    def notify(self, msg):
        print(f"Notiy to passenger ({self.name}) = {msg}")