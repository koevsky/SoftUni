def multiply(times):

    def decorator(function):

        def wrapper(n):
            return function(n) * times

        return wrapper

    return decorator


