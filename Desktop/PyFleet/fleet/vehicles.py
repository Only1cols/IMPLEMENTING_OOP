class Vehicle:
    def __init__(self, brand, colour, fuel, door):
        self.brand = brand
        self.colour = colour
        self.fuel = fuel
        self.door = door

    def start(self):
        return f" A {self.colour} {self.fuel} powered engine {self.brand} has started"

    def stop(self):
        return f" A{self.colour} {self.fuel} powered engine {self.brand} has stopped"


class Bus(Vehicle):
    def __init__(self, brand, colour, fuel, door, weight):
        super().__init__(brand, colour, fuel, door)
        self.weight = weight

    def offload(self):
        return f" A {self.colour} {self.fuel} powered engine {self.door} door {self.brand} offloads {self.weight} ton of sand "


my_bus = Bus("Mercedes", "black", "diesel", 2, 1000)
print(my_bus.start())
print(my_bus.offload())
