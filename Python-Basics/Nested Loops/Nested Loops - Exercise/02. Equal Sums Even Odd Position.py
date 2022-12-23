num1 = int(input())
num2 = int(input())

for nums in range(num1, num2+1):
    odd_sum = 0
    even_sum = 0
    nums = str(nums)
    for pos in range(len(nums)):
        if pos % 2 == 0:
            even_sum += int(nums[pos])
        else:
            odd_sum += int(nums[pos])
    if odd_sum == even_sum:
        print(nums, end= " ")

