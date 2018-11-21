from coordinate_geometry_lib import *

print("Co-ordinate Geometry Calculator\n")
keys = int(input("Choose option\n1. Distance between two point\n2. Mid point of line\n3. Section Formula\n4. Centroid "
                 "of Triangle\n5. Slope of Line\n"))

if keys == 1:
    print("Enter x1, x2, y1, y2 co-ordinates.\n")
    x1 = int(input("x1 : "))
    x2 = int(input("x2 : "))
    y1 = int(input("y1 : "))
    y2 = int(input("y2 : "))
    distance_between_two_point(x1, x2, y1, y2)

elif keys == 2:
    print("Enter x1, x2, y1, y2 co-ordinates.\n")
    x1 = int(input("x1 : "))
    x2 = int(input("x2 : "))
    y1 = int(input("y1 : "))
    y2 = int(input("y2 : "))
    mid_point(x1, x2, y1, y2)

elif keys == 3:
    internal_external = input("Enter I for Internal section formula and E for External section Formula\n")
    if internal_external == 'I' or internal_external == 'i':
        print("Enter x1, x2, y1, y2 co-ordinates and ratio m:n.\n")
        x1 = int(input("x1 : "))
        x2 = int(input("x2 : "))
        y1 = int(input("y1 : "))
        y2 = int(input("y2 : "))
        m = int(input("m : "))
        n = int(input("n : "))
        internal_section_formula(x1, x2, y1, y2, m, n)
    elif internal_external == 'E' or internal_external == 'e':
        print("Enter x1, x2, y1, y2 co-ordinates and ratio m:n.\n")
        x1 = int(input("x1 : "))
        x2 = int(input("x2 : "))
        y1 = int(input("y1 : "))
        y2 = int(input("y2 : "))
        m = int(input("m : "))
        n = int(input("n : "))
        external_section_formula(x1, x2, y1, y2, m, n)
    else:
        print("Enter correct option...\n")

elif keys == 4:
    print("Enter x1, x2, x3, y1, y2, y3 co-ordinates.\n")
    x1 = int(input("x1 : "))
    x2 = int(input("x2 : "))
    x3 = int(input("x3 : "))
    y1 = int(input("y1 : "))
    y2 = int(input("y2 : "))
    y3 = int(input("y3 : "))
    centroid_triangle(x1, x2, x3, y1, y2, y3)

elif keys == 5:
    print("Enter x1, x2, y1, y2 co-ordinates.\n")
    x1 = int(input("x1 : "))
    x2 = int(input("x2 : "))
    y1 = int(input("y1 : "))
    y2 = int(input("y2 : "))
    slope_line(x1, x2, y1, y2)

else:
    print("Enter correct option....")
