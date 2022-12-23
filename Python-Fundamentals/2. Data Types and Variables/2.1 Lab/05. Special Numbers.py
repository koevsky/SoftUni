n = int(input())
for x in range(1, n+1):
    x = str(x)
    digit = sum([int(y) for y in x])
    if digit == 5 or digit == 7 or digit == 11:
        print(f"{x} -> True")
    else:
        print(f"{x} -> False")