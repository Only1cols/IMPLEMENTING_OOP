class Vehicle:
    def __init__(self, brand, colour):
        self.__brand = brand
        self._colour = colour
# geter -- read only

    @property
    def brand(self):
        return self.__brand

    @property
    def colour(self):
        return self._colour

    @colour.setter
    def colour(self, new_colour):
        if isinstance(new_colour, str):
            self._colour = new_colour
        else:
            print("colour must be string only!")


my_car = Vehicle("Mercedes", "red")

print(my_car.brand)
print(my_car.colour)
my_car.colour = "yellow"

print(my_car.colour)
