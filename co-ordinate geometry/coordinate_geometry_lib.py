import math


def distance_between_two_point(x1, x2, y1, y2):
    distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return distance


def mid_point(x1, x2, y1, y2):
    mid_x_point = (x1 + x2) / 2
    mid_y_point = (y1 + y2) / 2
    return mid_x_point, mid_y_point


def internal_section_formula(x1, x2, y1, y2, m, n):
    section_x_point = (m * x2 + n * x1) / (m + n)
    section_y_point = (m * y2 + n * y1) / (m + n)
    return section_x_point, section_y_point


def external_section_formula(x1, x2, y1, y2, m, n):
    section_x_point = (m * x2 - n * x1) / (m - n)
    section_y_point = (m * y2 - n * y1) / (m - n)
    return section_x_point, section_y_point


def centroid_triangle(x1, x2, x3, y1, y2, y3):
    centroid_x_point = (x1 + x2 + x3) / 3
    centroid_y_point = (y1 + y2 + y3) / 3
    return centroid_x_point, centroid_y_point


def slope_line(x1, x2, y1, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope
