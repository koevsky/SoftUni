vegetable_price = float(input())
fruit_price = float(input())
vegetable_weight = int(input())
fruit_weight = int(input())

price = ((vegetable_price*vegetable_weight) + (fruit_price*fruit_weight)) / 1.94

print(f"{price:.2f}")