class Vehicle:
    def __init__(self, brand, colour):
        self.__brand = brand
        self._colour = colour
# getter--read only

    @property
    def brand(self):
        return self.__brand
    # getter for colour

    @property
    def colour(self):
        return self._colour

    @colour.setter  # you can modify in a controlled state
    def colour(self, new_colour):
        if isinstance(new_colour, str):
            self._colour = new_colour
        else:
            print("Colour must be a string!")


my_car = Vehicle("Toyota", "Red")
print(my_car.brand)
print(my_car.colour)

my_car.colour = "yellow"
print(my_car.colour)




























