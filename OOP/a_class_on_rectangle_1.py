import math


class Rectangle:
    def __init__(self, le, b):
        self.le = le
        self.b = b

    def area(self):
        return self.le * self.b

    def perimeter(self):
        return 2 * (self.le + self.b)

    def square(self):
        if self.le == self.b:
            return 'Square'
        else:
            return 'rectangle'

    def diagonals(self):
        return math.sqrt(self.le ** 2 + self.b ** 2)


length = float(input("Enter length : "))
breadth = float(input("Enter breadth : "))
rectangle = Rectangle(length, breadth)
print("Area : ", rectangle.area())
print("Perimeter :", rectangle.perimeter())
print("It is", rectangle.square())
print("Diagonal :", rectangle.diagonals())
