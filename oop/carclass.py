class Car:
    # instance builder and variables
    def __init__(self, name, color, masskg):
        self.name = name
        self.color = color
        self.mass = masskg

    # self refers to the current instance of the class.
    def desc (self):
        return "{} is {} and weighs {} kg ". \
            format(self.name, self.color, self.mass)

# Class that herits the Car class:
class SuperCar(Car):
    def __init__(self, name, color, masskg, vitesse):
        # runs the init of the parent class:
        super().__init__(name, color, masskg)
        self.vitesse = vitesse

    # overrides the method in Person class:
    def desc (self):
        return "{} is {}, weighs {} kg and has the maximum velocity of {}". \
            format(self.name, self.color, self.mass, self.vitesse)


# Testing classes: 2 instances of Car class
car1 = Car("Giant","black",3000)
car2 = Car("Tiny","green",200)

# prints descriptions of the cars
print(car1.desc())
print(car2.desc())

# The inherited class:
supercar = SuperCar("Super", "White", 1000, "500 km/h")
print(supercar.desc())

# More cars:
car3 = Car("Nice","yellow",1000)
car4 = Car("Great","pink",3000)
car5 = Car("Small","blue",500)
car6 = Car("Light","white",400)
car7 = Car("Weak","gray",700)
car8 = Car("Bad","black",2000)

# List makes it easy:
cars = [car3,car4,car5,car6,car7,car8]

for car in cars:
    print(car.desc())