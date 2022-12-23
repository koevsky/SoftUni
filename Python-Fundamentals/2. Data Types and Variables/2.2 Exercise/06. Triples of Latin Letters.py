end = int(input())
for x in range(97, 97 + end):
    for y in range(97, 97 + end):
        for z in range(97, 97 + end):
            print(f"{chr(x)}{chr(y)}{chr(z)}")