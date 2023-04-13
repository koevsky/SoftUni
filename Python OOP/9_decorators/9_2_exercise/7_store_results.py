class store_results:

    res_file = "files/results.txt"

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        string = f'Function {self.func.__name__} was called. Result: {result}'
        with open(self.res_file, "a") as file:
            file.write(string+"\n")

        return result


@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)
