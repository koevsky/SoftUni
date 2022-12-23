number = int(input())
total_sum = 0
while True:
    num = int(input())
    total_sum += num
    if total_sum >= number:
        break
print(total_sum)