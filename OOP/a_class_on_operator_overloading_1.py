class Height:
    def __init__(self, feet, inch):
        self.feet = feet
        self.inch = inch

    def __str__(self):
        return '{} feet and {} inches'.format(self.feet, self.inch)

    def __add__(self, other):
        feet = self.feet + other.feet
        inche = self.inch + other.inch

        if inche >= 12:
            inche = inche - 12
            feet = feet + 1

        return feet, inche


f1 = float(input("Enter feet of first height : "))
f2 = float(input("Enter feet of second height : "))
i1 = float(input("Enter inch of first height : "))
i2 = float(input("Enter inch of second height : "))
h1 = Height(f1, i1)
h2 = Height(f2, i2)
print(h1 + h2)
