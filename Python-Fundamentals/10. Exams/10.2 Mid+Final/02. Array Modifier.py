def swap(lst, idx1, idx2):
    lst[idx1], lst[idx2] = lst[idx2], lst[idx1]
    return lst


def multiply(lst, idx1, idx2):
    lst[idx1] = lst[idx1] * lst[idx2]
    return lst


def decrease(lst):
    lst = [x-1 for x in lst]
    return lst


nums_list = [int(x) for x in input().split(" ")]
while True:
    line = input()
    if line == "end":
        break
    cmd = line.split(" ")
    if cmd[0] == "swap":
        index1, index2 = int(cmd[1]), int(cmd[2])
        nums_list = swap(nums_list, index1, index2)
    elif cmd[0] == "multiply":
        index1, index2 = int(cmd[1]), int(cmd[2])
        nums_list = multiply(nums_list, index1, index2)
    elif cmd[0] == "decrease":
        nums_list = decrease(nums_list)

print(", ".join([str(x) for x in nums_list]))