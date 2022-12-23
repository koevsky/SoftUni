divisor, boundary = int(input()), int(input())

for x in range(boundary, divisor-1, -1):
    if x % divisor == 0 and x > 0 and x <= boundary:
        print(x)
        break
