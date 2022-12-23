import sys
eggs_painted = int(input())
red, orange, blue, green, = 0, 0, 0, 0
max_count = -sys.maxsize
max_color = ""
for egg in range(eggs_painted):
    color = input()
    if color == "red":
        red += 1
        if red > max_count:
            max_count = red
            max_color = color
    elif color == "orange":
        orange += 1
        if orange > max_count:
            max_count = orange
            max_color = color
    elif color == "blue":
        blue += 1
        if blue > max_count:
            max_count = blue
            max_color = color
    elif color == "green":
        green += 1
        if green > max_count:
            max_count = green
            max_color = color
print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {max_count} -> {max_color}")