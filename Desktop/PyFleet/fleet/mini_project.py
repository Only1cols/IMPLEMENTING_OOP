from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, brand, colour, fuel):
        self.__brand = brand
        self._colour = colour
        self.fuel = fuel

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def move(self):
        return f"{self.__brand} moves on 4 wheels"

    # getter_ read only
    @property
    def brand(self):
        return self.__brand

    @property
    def colour(self):
        return self._colour

    # adding an additional layer of validation

    @colour.setter
    def colour(self, new_colour):
        if isinstance(new_colour, str):
            self._colour = new_colour
        else:
            print("Colour must be string")


class Car(Vehicle):
    def __init__(self, brand, colour, fuel, door):
        super().__init__(brand, colour, fuel)
        self.door = door

    def start(self):
        return f"{self.brand} purrs to life"

    def stop(self):
        return f"{self.brand} stops roaring"

    def trunk(self):
        return f"{self.brand} powerlifts the trunk open"


class Bus(Vehicle):
    def __init__(self, brand, colour, fuel, tyre):
        super().__init__(brand, colour, fuel)
        self.tyre = tyre

    def start(self):
        return f"{self.brand} starts its engine"

    def stop(self):
        return f"{self.brand} applies brakes and comes to a halt"

    def haul(self):
        return f"{self.brand} is used to haul"


class Bike(Vehicle):
    def __init__(self, brand, colour, fuel, wheels):
        super().__init__(brand, colour, fuel)
        self.wheels = wheels

    def start(self):
        return f"{self.brand} roars"

    def stop(self):
        return f"{self.brand} turns off its engine"

    def move(self):
        return f"{self.brand} moves on 2 wheels"

    def passenger(self):
        return f"{self.brand} is a {self.wheels} wheeled bike that allows for only 1 passenger"


# Objects
car1 = Car("Toyota", "Red", "gas", 4)
bus1 = Bus("Mercedes", "Black", "Diesel", 4)
bike1 = Bike("volvo", "white", "gas", 2)


# polymorphism - same method, different behaviour


vehicles = [car1, bus1, bike1]

print("----start()----")

for vehicle in vehicles:
    print(vehicle.start())

print("----stop()----")

for vehicle in vehicles:
    print(vehicle.stop())

print("----move()----")

for vehicle in vehicles:
    print(vehicle.move())

print("----unique methods()----")

print(car1.trunk())
print(bus1.haul())
print(bike1.passenger())