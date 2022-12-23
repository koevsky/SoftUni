import math
x_1, y_1 = float(input()), float(input())
x_2, y_2 = float(input()), float(input())


def center(x1, y1, x2, y2):

    res = None
    d_1 = math.sqrt((x1 - 0)**2 + (y1 - 0)**2)
    d_2 = math.sqrt((x2 - 0)**2 + (y2 - 0)**2)
    if d_1 == d_2:
        res = x1, y1
    elif d_1 < d_2:
        res = x1, y1
    elif d_2 < d_1:
        res = x2, y2
    return f"({math.floor(res[0])}, {math.floor(res[1])})"

print(center(x_1, y_1, x_2,y_2))

