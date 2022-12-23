nums_seq = input().split(", ")
zero_count = nums_seq.count("0")
for x in range(zero_count):
    nums_seq.remove("0")
nums_seq = nums_seq + list("0"*zero_count)
nums_seq = [int(x) for x in nums_seq]
print(nums_seq)
