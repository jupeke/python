class Vehicule:
    # instance builder and variables
    def __init__(self, name, color, masskg):
        self.name = name
        self.color = color
        self.mass = masskg

    # self refers to the current instance of the class.
    def desc (self):
        print("This vehicule is a {}, is {} and weighs {} kg". \
            format(self.name, self.color, self.mass))

# Class that herits the Vehicule class:
class Bicycle(Vehicule):
    def __init__(self, color, masskg, numb_of_gears):
        # runs the init of the parent class:
        super().__init__("bicycle", color, masskg)
        self.gears = numb_of_gears

    # overrides the method in Person class:
    def desc (self):
        print("This {} is {}, weighs {} kg and has {} speeds". \
            format(self.name, self.color, self.mass, self.gears))


# Testing classes: instances of Vehicule class
v1 = Vehicule("truck","black",30000)
v2 = Vehicule("person car","green",1500)
v3 = Vehicule("tractor","black",3500)

vehicules = [v1, v2, v3]

print()
# prints descriptions of the vehicules:
for vehicule in vehicules:
    vehicule.desc()

# The inherited class:
bicycle1 = Bicycle("white", 15, 18)
bicycle2 = Bicycle("red", 1, 12)
bicycle3 = Bicycle("blue", 3, 10)
bicycle4 = Bicycle("pink", 7, 25)
bicycle5 = Bicycle("brown", 3, 19)

bicycles = [bicycle1, bicycle2, bicycle3, bicycle4, bicycle5]

print()
# prints descriptions of the vehicules:
for bicycle in bicycles:
    bicycle.desc()
