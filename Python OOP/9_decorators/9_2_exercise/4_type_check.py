def type_check(t):
    def decorator(func):
        def wrapper(var):
            if type(var) == t:
                result = func(var)

            else:
                result = "Bad Type"

            return result

        return wrapper

    return decorator