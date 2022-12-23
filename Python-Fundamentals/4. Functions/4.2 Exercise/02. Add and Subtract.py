def add_and_subtract(a, b, c):
    def sum_numbers(a, b):
        x = a +b
        return x
    def subtract(c):
        return sum_numbers(a, b) - c
    return subtract(c)

x, y, z = int(input()), int(input()), int(input())
print(add_and_subtract(x, y, z))