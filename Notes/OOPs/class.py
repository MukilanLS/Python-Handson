# Class

# Syntax
class car:
    color = "Black"
    type = "SUV"
    pass

car_1 = car()
print(car_1.color.upper())
print(car_1.type)

# Method inside the class
class counting:
    number = 0

    def increment(self):
        self.number += 1
        print("Counted", self.number)

c = counting()
c.increment()
c.increment()

# Constructors and Destructors
class const_dest:

    def __init__(self,color,type):
        self.color = color
        self.type = type
        print("Constructors")

    def __del__(self):
        print("Destructors")

cd = const_dest("Black", "SUV")
print(cd.color.upper())
print(cd.type)