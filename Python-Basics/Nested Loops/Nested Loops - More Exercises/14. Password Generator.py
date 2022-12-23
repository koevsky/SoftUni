n, l = int(input()), int(input())

for x in range(1, n+1):
    for y in range(1, n+1):
        for sym_1 in range(97, 97+l):
            for sym_2 in range(97, 97 + l):
                for z in range(1, n + 1):
                    if z > x and z > y:
                        print(f"{x}{y}{chr(sym_1)}{chr(sym_2)}{z}", end=" ")