def fibonacci():

    nums = []
    res = 0

    while True:

        if len(nums) < 2:
            yield res

            nums.append(res)
            res += 1

        else:
            res = nums[-1] + nums[-2]
            yield res
            nums.append(res)
