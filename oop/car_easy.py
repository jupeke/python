# Class definition:
class Car:
    def __init__(self, pcolor, pmake):
        self.color = pcolor
        self.make = pmake

    def desc(self):
        return "{} is {}".format(self.make, self.color)

# Create instances of the Car class:
car1 = Car("red", "Lada")
car2 = Car("blue", "BMW")
car3 = Car("black", "Peugeot")

# A list of cars:
cars = [car1, car2, car3]

for car in cars:
    print(car.desc())
