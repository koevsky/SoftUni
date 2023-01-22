def even_odd(*args):
    args = list(args)
    command = args.pop()

    if command == "even":
        return [int(x) for x in args if int(x) % 2 == 0]
    else:
        return [int(x) for x in args if int(x) % 2 != 0]

print(even_odd(1, 2, 3, 4, 5, 6, "even"))