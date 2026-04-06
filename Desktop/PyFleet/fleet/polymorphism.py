# there are different methods in which we can implement polymorphism

# method over riding,duck typing and abstract classes

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        return f"{self.brand} is starting"


class Car(Vehicle):
    def start(self):
        return f"{self.brand} purrs to life....."


class Truck(Vehicle):
    def start(self):
        return f"{self.brand} roars to life"

  # polymorphism in action


vehicles = [Car("Toyota"), Truck("Mercedes")]

for car in vehicles:
    print(car.start())


### The concept of a child class rewriting a parent method is called method over-riding
