# polymorphism, it can access area of both class i.e it can access common function of many classes

from a_class_on_rectangle import Rectangle
from a_class_on_circle_operation import Circle

shapes = [Rectangle(4, 5), Circle(7)]

for shape in shapes:
    print('Area of given shape is ', shape.__class__, shape.area())
