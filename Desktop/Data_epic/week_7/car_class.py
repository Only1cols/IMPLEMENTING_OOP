class Car:
    type = "salon"

    def __init__(self, colour, mileage):
        self.colour = colour
        self.mileage = mileage

    def __str__(self):
        return f"The {self.colour} car has {self.mileage} mileage"


blue_car = Car("blue", 20000)
red_car = Car("red", 30000)

for car in (blue_car, red_car):
    print(car)



