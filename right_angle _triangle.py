def right_angle_triangle(a, b, c):
    if a + b + c > 180 or a + b + c < 180:
        print("Angles you entered does not form triangle")
    else:
        if not a >= 180 and not b >= 180 and not c >= 180:
            if a == 90 or b == 90 or c == 90:
                print("The triangle is right angle triangle")
            elif a == (b + c) or b == (a + c) or c == (a + b):
                print("The triangle is right angle triangle")
            else:
                print("The triangle is not right angle triangle")
        else:
            print("A angle of triangle is exceed than 178 degree")


a = float(input("Enter first angle"))
b = float(input("Enter second angle"))
c = float(input("Enter third angle"))
right_angle_triangle(a, b, c)
