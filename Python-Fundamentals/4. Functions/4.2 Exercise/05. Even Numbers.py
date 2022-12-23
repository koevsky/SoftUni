def even_nums(x):
    if x % 2 == 0:
        return True

    return False

nums = input().split(" ")
nums = [int(x) for x in nums]
even_nums_checker = list(filter(even_nums, nums))
print(even_nums_checker)

