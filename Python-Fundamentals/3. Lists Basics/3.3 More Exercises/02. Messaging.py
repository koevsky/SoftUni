nums_seq = input().split(" ")
text = list(input())
message = ""
print()
for nums in nums_seq:
    nums = [int(x) for x in nums]
    nums_sum = sum(nums)
    if nums_sum > len(text) - 1:
        nums_sum -= len(text)
    message += text[nums_sum]
    text.pop(nums_sum)
print(message)