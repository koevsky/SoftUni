def multiply(*args):
    res = 1

    for x in args:
        res *= x

    return res


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
