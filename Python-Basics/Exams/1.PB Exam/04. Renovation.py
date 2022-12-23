import math
wall_height, wall_width, percent = int(input()), int(input()), int(input())
total_surface = wall_height * wall_width * 4
total_surface -= total_surface * percent/100
total_surface = math.ceil(total_surface)
surface_painted = 0
while True:
    paint_liters = input()
    if paint_liters == "Tired!":
        print(f"{abs(surface_painted - total_surface)} quadratic m left.")
        break
    paint_liters = int(paint_liters)
    surface_painted += paint_liters
    if surface_painted == total_surface:
        print("All walls are painted! Great job, Pesho!")
        break
    elif surface_painted > total_surface:
        print(f"All walls are painted and you have {abs(surface_painted - total_surface)} l paint left!")
        break