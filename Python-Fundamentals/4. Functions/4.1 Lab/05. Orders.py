def calc_price(product, count):
    total_price = 0
    if product == "coffee":
        total_price = count * 1.50
    elif product == "water":
        total_price = count * 1.00
    elif product == "coke":
        total_price = count * 1.40
    elif product == "snacks":
        total_price = count * 2.00
    return f"{total_price:.2f}"

text, num = input(), int(input())
print(calc_price(text, num))
