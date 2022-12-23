import math


def center(x1, y1, x2, y2):

    res = None
    d_1 = math.sqrt((x1 - 0)**2 + (y1 - 0)**2)
    d_2 = math.sqrt((x2 - 0)**2 + (y2 - 0)**2)
    if d_1 == d_2:
        res = x1, y1, x2, y2
    elif d_1 < d_2:
        res = x1, y1, x2, y2
    elif d_2 < d_1:
        res = x2, y2, x1, y1
    res = list([math.floor(x) for x in res])
    return f"({res[0]}, {res[1]})({res[2]}, {res[3]})"


def line_calc(x1, y1, x2, y2):

    length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return length


# LINE №1--------------------------------
x_1, y_1 = float(input()), float(input())
x_2, y_2 = float(input()), float(input())

# LINE №2-----------------------------------
a_1, b_1 = float(input()), float(input())
a_2, b_2 = float(input()), float(input())
# CHECK LENGTH
if line_calc(x_1, y_1, x_2, y_2) == line_calc(a_1, b_1, a_2, b_2):
    print(center(x_1, y_1, x_2, y_2))
elif line_calc(x_1, y_1, x_2, y_2) > line_calc(a_1, b_1, a_2, b_2):
    print(center(x_1, y_1, x_2, y_2))
elif line_calc(a_1, b_1, a_2, b_2) > line_calc(x_1, y_1, x_2, y_2):
    print(center(a_1, b_1, a_2, b_2))
