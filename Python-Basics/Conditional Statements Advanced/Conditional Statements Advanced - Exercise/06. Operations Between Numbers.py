num_1 = int(input())
num_2 = int(input())
operator = input()

if (num_2 == 0) and (operator == "/" or operator == "%"):
    print(f"Cannot divide {num_1} by zero")
elif operator == "+":
    result = num_1 + num_2

elif operator == "-":
    result = num_1 - num_2

elif operator == "*":
    result = num_1 * num_2

elif operator == "/":
    result = num_1 / num_2
    print(f"{num_1} / {num_2} = {result:.2f}" )

elif operator == "%":
    result = num_1 % num_2
    print(f"{num_1} % {num_2} = {result}")

if operator == "+" or operator == "-" or operator == "*":
    even_odd = ""
    if result % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{num_1} {operator} {num_2} = {result} - {even_odd}")

