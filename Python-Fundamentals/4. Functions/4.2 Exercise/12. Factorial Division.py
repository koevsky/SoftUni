import math
def f_division(x, y):
    f_x = math.factorial(x)
    f_y = math.factorial(y)
    return f"{(f_x/f_y):.2f}"

a, b = int(input()), int(input())
print(f_division(a, b))