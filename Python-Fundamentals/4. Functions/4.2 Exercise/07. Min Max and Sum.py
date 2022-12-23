def min_max_sum(seq):
    seq = sorted([int(x) for x in seq])
    min_num, max_num, total = seq[0], seq[-1], sum(seq)
    return min_num, max_num, total

nums = input().split(" ")
print(f"The minimum number is {min_max_sum(nums)[0]}")
print(f"The maximum number is {min_max_sum(nums)[1]}")
print(f"The sum number is: {min_max_sum(nums)[2]}")