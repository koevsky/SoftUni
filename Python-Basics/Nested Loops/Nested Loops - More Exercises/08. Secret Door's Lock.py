boundary_x, boundary_y, boundary_z = int(input()), int(input()), int(input())
for x in range(1, boundary_x+1):
    for y in range(1, boundary_y+1):
        for z in range(1, boundary_z+1):
            if x % 2 == 0 and z % 2 == 0 and y in [2, 3, 5, 7]:
                print(f"{x} {y} {z}")