from time import time


def exec_time(function):

    def wrapper(*args, **kwargs):
        start = time()
        function(*args, **kwargs)
        end = time()

        return end - start

    return wrapper


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result

print(concatenate(["a" for i in range(100000000)]))




