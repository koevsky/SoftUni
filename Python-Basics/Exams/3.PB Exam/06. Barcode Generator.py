start, end = input(), input()

for x in range(int(start[0]), int(end[0])+1):
    for y in range(int(start[1]), int(end[1])+1):
        for z in range(int(start[2]), int(end[2])+1):
            for m in range(int(start[3]), int(end[3])+1):
                if x % 2 != 0 and y % 2 != 0 and z % 2 != 0 and m % 2 != 0:
                    print(f"{x}{y}{z}{m}", end=" ")