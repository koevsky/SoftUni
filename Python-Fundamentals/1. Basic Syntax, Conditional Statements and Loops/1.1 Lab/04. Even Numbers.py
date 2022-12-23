n = int(input())
for x in range(n):
    number = int(input())
    if number % 2 != 0:
        is_odd = True
        print(f"{number} is odd!" )
        break
else:
    print("All numbers are even.")
