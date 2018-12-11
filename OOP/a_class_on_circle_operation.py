import math


class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

    def perimeter(self):
        return 2 * math.pi * self.r

    def diameter(self):
        return 2 * self.r


# radii = float(input("Enter radius of circle : "))
# radius = Circle(radii)
# print("Area of circle :", radius.area())
# print("Circumference of circle :", radius.perimeter())
# print("Diameter of circle :", radius.diameter())

# its makes to run while running same file  or it cant access through other file directly
if __name__ == '__main__':
    radii = float(input("Enter radius of circle : "))
    radius = Circle(radii)
    print("Area of circle :", radius.area())
    print("Circumference of circle :", radius.perimeter())
    print("Diameter of circle :", radius.diameter())
