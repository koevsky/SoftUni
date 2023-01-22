def operate(operator, *args):

    def addition():
        return sum(args)

    def subtraction():
        res = args[0]
        for x in args[1:]:
            res -= x
        return res

    def multiplication():
        res = 1
        for x in args:
            res *= x
        return res

    def division():
        res = args[0]
        for x in args[1:]:
            if x != 0:
                res /= x
        return res

    if operator == "+":
        return addition()

    elif operator == "-":
        return subtraction()

    elif operator == "*":
        return multiplication()

    elif operator == "/":
        return division()

