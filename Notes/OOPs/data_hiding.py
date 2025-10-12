# Data Hiding

class simple:
    def __init__(self):
        self.value_1 = 1
        self.value_2 = 2

    def _A1_(self):
        print("Apple")

    # __ Private view, Needs to check the name in dir(class)
    def __A2_(self):
        print("Banana")

s = simple()
print(s.value_1)
print(s.value_2)
simple()._A1_()
print(dir(simple))
simple()._simple__A2_()