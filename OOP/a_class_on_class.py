# OOP, OOP is used to map with real world cases
# first letter of class must be capitalize
# class means blueprint, which consist of attributes and methods
# the feature of class access through object like a and b

# self, with object call method is self, called through dot operator. example quard() called by a then self send its value as an argument
# dot operator use to access member of class i.e attributes and method
# constructor, pass value on object creation, here def __init__(self, x, y) use for constructor
# dot operator access member i.e object
# by default on print it convert to string of and type

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

    # cast object to string, Point({1st},{2nd}).format(self.x,self.y) => x goes to 1st and y goes to 2nd
    # it must return string
    def __str__(self):
        return 'Point({},{})'.format(self.x, self.y)

    # cast to integer
    def __int__(self):
        return 1

    # cast to float
    def __float__(self):
        return 2.2


a = Point(3, 4)

# a.x = 3
# a.y = 4

print(a.quard())
print(
    a)  # give output like:  <__main__.Point object at 0x000001F639FCA7B8>, its means this file that is main and Point class and memory location

b = Point(7, -8)
# b.x = 7
# b.y = -8

print(b.quard())
print(b)

print(int(a) + 2)  # it calls,  def __int__(self): function of the class
