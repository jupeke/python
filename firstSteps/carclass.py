class Car:
    # instance builder and variables
    def __init__(self, name, color, masskg):
        self.name = name
        self.color = color
        self.mass = masskg

    # self refers to the current instance of the class.
    def desc (self):
        print("{} is {} and weighs {} kg". \
            format(self.name, self.color, self.mass))

# Class that herits the Car class:
class SuperCar(Car):
    def __init__(self, name, color, masskg, vitesse):
        # runs the init of the parent class:
        Car.__init__(self, name, color, masskg)
        self.vitesse = vitesse

    # overrides the method in Person class:
    def desc (self):
        print("{} is {}, weighs {} kg and has the maximum velocity of {}". \
            format(self.name, self.color, self.mass, self.vitesse))


# Testing classes: 2 instances of Car class
car1 = Car("Giant","black",3000)
car2 = Car("Tiny","green",200)

# prints descriptions of the cars
car1.desc()
car2.desc()

# The inherited class:
supercar = SuperCar("Super", "White", 1000, "500 km/h")
supercar.desc()
