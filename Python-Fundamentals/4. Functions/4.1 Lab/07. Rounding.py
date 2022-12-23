def round_nums(nums_seq):
    nums_seq = [round(float(x)) for x in nums_seq]
    return nums_seq

nums = input().split(" ")
print(round_nums(nums))
