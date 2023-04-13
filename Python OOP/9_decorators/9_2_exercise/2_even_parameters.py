def even_parameters(function):
    def wrapper(*args):
        for x in args:
            try:
                if x % 2 == 0:
                    pass

                else:
                    return "Please use only even numbers!"

            except:
                return "Please use only even numbers!"

        else:
            result = function(*args)
            return result

    return wrapper






