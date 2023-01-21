import math
from collections import deque

def add(res, nums):
    nums = deque(nums)
    while nums:
        res += nums.popleft()
    return res

def sub(res, nums):
    nums = deque(nums)
    if is_initial:
        res = nums.popleft()
    while nums:
        res -= nums.popleft()
    return res

def multiply(res, nums):
    nums = deque(nums)
    if is_initial:
        res = nums.popleft()
    while nums:
        res *= nums.popleft()
    return res

def divide(res, nums):
    nums = deque(nums)
    if is_initial:
        res = nums.popleft()
    while nums:
        if nums[0] != 0:
            res /= nums.popleft()
        else:
            break
    return math.floor(res)

string = deque(input().split())

total_res = 0
nums_list = []
is_initial = True
while string:
    char = string.popleft()

    if char.isdigit() or char.lstrip("-").isdigit():
        nums_list.append(int(char))
        continue
    elif char == "+":
        total_res = add(total_res, nums_list)
    elif char == "-":
        total_res = sub(total_res, nums_list)
    elif char == "*":
        total_res = multiply(total_res, nums_list)
    elif char == "/":
        total_res = divide(total_res, nums_list)

    nums_list.clear()
    is_initial = False

print(total_res)

