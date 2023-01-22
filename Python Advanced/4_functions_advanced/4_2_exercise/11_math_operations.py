from collections import deque

def math_operations(*args, **kwargs):

    args = deque(args)
    counter = 1

    while args:

        num = args.popleft()

        if counter == 1:
            kwargs["a"] += num

        elif counter == 2:
            kwargs["s"] -= num

        elif counter == 3 and num != 0:
            kwargs["d"] /= num

        elif counter == 4:
            kwargs["m"] *= num
            counter = 0

        counter += 1

    res = []

    kwargs = dict(sorted(kwargs.items(), key= lambda x: (-x[1], x[0])))

    for k, v in kwargs.items():
        res.append(f"{k}: {v:.1f}" )

    return "\n".join(res)






