# OOP, OOP is used to map with real world cases
# first letter of class must be capitalize
# class means blueprint, which consist of attributes and methods
# the feature of class access through object like a and b

# self, with object call method is self, called through dot operator. example quard() called by a then self send its value as an argument
# dot operator use to access member of class i.e attributes and method
# constructor, pass value on object creation, here def __init__(self, x, y) use for constructor

class Point:
    # x = None
    # y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def quard(self):
        if self.x == 0 or self.y == 0:
            return None
        if self.x > 0 and self.y > 0:
            return 1
        if self.x < 0 and self.y > 0:
            return 2
        if self.x < 0 and self.y < 0:
            return 3
        if self.x > 0 and self.y < 0:
            return 4


a = Point(3, 4)

# a.x = 3
# a.y = 4

print(a.quard())

b = Point(7, -8)
# b.x = 7
# b.y = -8

print(b.quard())
