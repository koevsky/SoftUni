x = float(input())
y = float(input())
h = float(input())

windows_area = 1.5*1.5*2
door_area = 1.2 * 2

walls_area = (x*x*2 + x*y*2) - windows_area - door_area
roof_area = x*h+x*y*2

wall_paint = walls_area / 3.4
roof_paint = roof_area / 4.3

print(f"{wall_paint:.2f}")
print(f"{roof_paint:.2f}")