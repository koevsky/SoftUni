n = int(input())
for x in range(1111, 10000):
    is_special = False
    x = str(x)
    for index, digit in enumerate(x):
        if int(digit) == 0:
            is_special = False
            break
        if n % int(digit) == 0:
            is_special = True
        else:
            is_special = False
            break
    if is_special:
        print(x, end=" ")


