def neg_vs_pos(args):

    pos = sum([int(x) for x in args if int(x) > 0])
    neg = sum([int(y) for y in args if int(y) < 0])

    res = f"{neg}\n{pos}\n"

    if abs(neg) > pos:
        res += "The negatives are stronger than the positives"

    elif abs(neg) < pos:
        res += "The positives are stronger than the negatives"

    return res


nums = input().split()
print(neg_vs_pos(nums))
