class Vehicule:
    # Class variable, common for all objects:
    nature_impact = "pollutes"

    # Instance builder and variables
    def __init__(self, name, color, masskg):
        self.name = name
        self.color = color
        self.mass = masskg

    # self refers to the current instance of the class.
    def desc (self):
        return "This vehicule is a {}, is {}, weighs {} kg and it {}.". \
            format(self.name, self.color, self.mass, self.nature_impact)

# Class that herits the Vehicule class:
class Bicycle(Vehicule):
    # Class variable, common for all objects:
    nature_impact = "does not pollute"

    def __init__(self, color, masskg, numb_of_gears):
        # runs the init of the parent class:
        super().__init__("bicycle", color, masskg)
        self.gears = numb_of_gears

    # overrides the method in Person class:
    def desc (self):
        return "This {} is {}, weighs {} kg and has {} speeds and it {}.". \
            format(self.name, self.color, self.mass, self.gears, self.nature_impact)


# Testing classes: instances of Vehicule class
v1 = Vehicule("truck","black",30000)

# Creates an instance variable that shades the class variable (the value of
# class variable stays the same as you can see with v2 and v3).
v1.nature_impact = "very bad for the nature"

v2 = Vehicule("person car","green",1500)
v3 = Vehicule("tractor","black",3500)

vehicules = [v1, v2, v3]

print()
# prints descriptions of the vehicules:
for vehicule in vehicules:
    print(vehicule.desc())

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
    print(bicycle.desc())
