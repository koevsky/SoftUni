def calc(op, num_one, num_two):
    res = None
    if op == "multiply":
        res = num_one * num_two
    elif op == "divide":
        res = int(num_one / num_two)
    elif op == "add":
        res = num_one + num_two
    elif op == "subtract":
        res = num_one - num_two
    return res

operator, num_1, num_2 = input(), int(input()), int(input())

print(calc(operator, num_1, num_2))
