class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def startEngine(self):
        print(f"The {self.brand} is starting...")

class Car(Vehicle):
    def __init__(self):
        pass
    def honk(self):
        print("Beep Beep...")

my_car1 = Car()
my_car1.honk()