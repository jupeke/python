class Car:

    # instance builder and variables
    def __init__(self, name, color, massInKg):
        self.name = name
        self.color = color
        self.mass = massInKg

    # self refers to the current instance of the class.
    def desc (self):
        print("{} is {} and weighs {} kg". \
            format(self.name, self.color, self.mass))

# instances of Car class
car1 = Car("Giant","black",3000)
car2 = Car("Tiny","green",300)

# prints descriptions of the cars
car1.desc()
car2.desc()

# Class that herits the Car class:
class SuperCar(Car):
    def __init__(self, name, color, massInKg, vitesse):

        # runs the init of the parent class:
        Car.__init__(self, name, color, massInKg)
        self.vitesse = vitesse

    # overrides the method in Person class:
    def desc (self):
        print("{} is {}, weighs {} kg and has the maximum velocity of {}". \
            format(self.name, self.color, self.mass, self.vitesse))
supercar = SuperCar("Super", "White", 1000, "500 km/h")

supercar.desc()
