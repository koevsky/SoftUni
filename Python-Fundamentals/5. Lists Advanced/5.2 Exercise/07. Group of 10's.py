def group_10(seq_num, boundary):
    seq_num = list(seq_num)
    filtered = list(filter(lambda x: x <= boundary, seq_num))
    for y in filtered:
        while y in seq_num:
            seq_num.remove(y)
    return filtered, seq_num


nums_list = list(map(int, input().split(", ")))
x = 10
while nums_list:
    print(f"Group of {x}'s: {group_10(nums_list, x)[0]}")
    nums_list = group_10(nums_list, x)[1]
    x += 10

