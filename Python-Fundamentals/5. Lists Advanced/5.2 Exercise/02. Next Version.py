def next_version(str_list):
    next_v = list(str(int("".join(str_list)) + 1))
    next_v = ".".join(next_v)
    return next_v


version = input().split(".")
print(next_version(version))