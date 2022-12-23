from math import pi

figure = input()

if figure == "square":
    x = float(input())
    area = x*x
if figure == "rectangle":
    x = float(input())
    y = float(input())
    area = x*y
if figure == "circle":
    x = float(input())
    area = pi*x*x
if figure == "triangle":
    h = float(input())
    a = float(input())
    area = h*a / 2

print(f"{area:.3f}")
