def positive(num_list):
    nums = [str(x) for x in num_list if x >= 0]
    return ", ".join(nums)


def negative(num_list):
    nums = [str(x) for x in num_list if x < 0]
    return ", ".join(nums)


def even(num_list):
    nums = [str(x) for x in num_list if x % 2 == 0]
    return ", ".join(nums)


def odd(num_list):
    nums = [str(x) for x in num_list if x % 2 != 0]
    return ", ".join(nums)


numbs = list(map(int, input().split(", ")))
print(f"Positive: {positive(numbs)}\nNegative: {negative(numbs)}\nEven: {even(numbs)}\nOdd: {odd(numbs)}")