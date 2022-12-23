import sys
n = int(input())
max_diff = -sys.maxsize
last_sum = None
current_sum = None

for nums in range(1, n+1):
    num_1 = int(input())
    num_2 = int(input())
    current_sum = num_1 + num_2
    if not last_sum:
        last_sum = current_sum
    if (last_sum and current_sum) or (last_sum and current_sum == 0 ) or (last_sum == 0 and current_sum):
        diff = abs(last_sum - current_sum)
        if diff > max_diff:
            max_diff = diff
    last_sum = current_sum

if max_diff == 0:
    print(f"Yes, value={current_sum}")
else:
    print(f"No, maxdiff={max_diff}")
