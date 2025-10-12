# Inheritance

# Class 1 - Base Class
class name:
    def __init__(self, name):
        self.name = name
        print("Hi", name)

# Class 2 inherits all function and properties of Class 1 - Subclass/Derived Class
class cricket_fans(name):
    runs = 100

    def run(self):
        print(self.name, "scores", self.runs, "Runs")

cricket_fans("LSM").run()

# Single level Inheritance
class A:
    def state_1(self):
        print("State_1 Present")
    def state_2(self):
        print("State_2 Present")
    def state_3(self):
        print("State_3 Present")

class B(A):
    def state_4(self):
        print("State_4 Present")
    def state_4(self):
        print("State_4 Present")
    def state_5(self):
        print("State_5 Present")

A().state_1()
A().state_2()
B().state_4()
B().state_5()
B().state_3()

# Multi level Inheritance
class C(B):
    def state_6(self):
        print("State_6 Present")

C().state_6()
C().state_5()
C().state_3()

# Multiple Inheritance
class D:
    def state_7(self):
        print("State_7 Present")

class E():
    def state_8(self):
        print("State_8 Present")

class F(D,E):
    def state_9(self):
        print("State_9 Present")

F().state_7()
F().state_8()
F().state_9()