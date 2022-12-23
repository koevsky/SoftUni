first_end, second_end, third_end = int(input()), int(input()), int(input())

for x in range(1, first_end+1):
    for y in range(1, second_end+1):
        for z in range(1, third_end+1):
            if x % 2 == 0 and z % 2 == 0 and (y == 2 or y == 3 or y == 5 or y == 7):
                print(f"{x} {y} {z}")