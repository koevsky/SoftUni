def possible_permutations(nums):

    if len(nums) == 1:
        yield nums

    else:
        for i in range(len(nums)):

            first = nums[i]
            remaining = nums[:i] + nums[i+1:]

            for p in possible_permutations(remaining):
                yield [first] + p


[print(n) for n in possible_permutations([1, 2, 3])]




