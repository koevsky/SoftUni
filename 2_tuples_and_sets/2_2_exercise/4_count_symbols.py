line = list(input())
u_symbols = set(line)
for x in sorted(u_symbols):
    print(f"{x}: {line.count(x)} time/s")