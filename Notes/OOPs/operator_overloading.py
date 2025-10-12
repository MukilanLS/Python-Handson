# Operator Overloading

a = 1
b = 2
c = '1'
d = '2'

print(a + b)
print(int.__add__(a, b))

print(c + d)
print(str.__add__(c, d))

class vegetables:
    def __init__(self, carrot, potato):
        self.carrot = carrot
        self.potato = potato

    # This function is required for addition in class
    def __add__(self, other):
        carrot = self.carrot + other.carrot
        potato = self.potato + other.potato 
        return vegetables(carrot, potato)

v1 = vegetables(2,7)
v2 = vegetables(5,9)
v3 = v1 + v2
print(v3.carrot)
print(v3.potato)
