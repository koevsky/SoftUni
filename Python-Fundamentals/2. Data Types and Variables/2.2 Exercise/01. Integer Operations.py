result = 0
for x in range(4):
    number = int(input())
    if x <= 1:
        result += number
    if x == 2:
        result /= number
        result = int(result)
    if x == 3:
        result *= number
print(result)