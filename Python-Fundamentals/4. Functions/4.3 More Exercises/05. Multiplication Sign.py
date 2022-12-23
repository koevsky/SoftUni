

def negative_counter(iterable):
    iterable = len([x for x in iterable if x < 0])
    return iterable


def is_positive(iterable):
    result = ""
    if 0 in iterable:
        result = "zero"
    elif negative_counter(iterable) == 1 or negative_counter(iterable) == 3:
        result = "negative"
    elif negative_counter(iterable) == 2 or negative_counter(iterable) == 0:
        result = "positive"
    return result


seq = [int(input()) for x in range(3)]
print(is_positive(seq))
