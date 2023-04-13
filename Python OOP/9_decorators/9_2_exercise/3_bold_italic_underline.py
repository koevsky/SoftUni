def make_bold(function):
    def wrapper(*args):
        result = function(*args)
        return f"<b>{result}</b>"

    return wrapper


def make_italic(function):
    def wrapper(*args):
        result = function(*args)
        return f"<i>{result}</i>"

    return wrapper


def make_underline(function):
    def wrapper(*args):
        result = function(*args)
        return f"<u>{result}</u>"

    return wrapper

