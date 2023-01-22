def func_executor(*args):
    res = ""
    for func_name, val in args:
        res += f"{func_name.__name__} - {func_name(*val)}\n"

    return res

def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result

def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))
