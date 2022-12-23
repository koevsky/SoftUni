import sys
m = int(input())
max_num = -sys.maxsize
sum = 0
for i in range(1, m+1):
    num = int(input())
    if num > max_num:
        max_num = num
    sum += num

if sum - max_num == max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    diff = max_num - (sum - max_num)
    print("No")
    print(f"Diff = {abs(diff)}")