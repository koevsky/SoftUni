number_count = int(input()) * 2

left_sum = 0
right_sum = 0

for i in range(1, number_count+1):
    number = int(input())
    if 1 <= i <= number_count / 2:
        left_sum += number
    else:
        right_sum += number

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    difference = abs(left_sum - right_sum)
    print(f"No, diff = {difference}")