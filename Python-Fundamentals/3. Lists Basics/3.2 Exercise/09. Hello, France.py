items = input().split("|")
budget = float(input())
initial_budget = budget
items_bought = []

for item in items:
    item = item.split("->")
    item_type, price = item[0], float(item[1])
    if item_type == "Clothes" and price <= 50 and initial_budget - price >= 0:
        initial_budget -= price
        price += price * 40/100
        items_bought.append(price)
    elif item_type == "Shoes" and price <= 35 and initial_budget - price >= 0:
        initial_budget -= price
        price += price * 40/100
        items_bought.append(price)
    elif item_type == "Accessories" and price <= 20.50 and initial_budget - price >= 0:
        initial_budget -= price
        price += price * 40/100
        items_bought.append(price)

total_money = initial_budget + sum(items_bought)
profit = total_money - budget
for x in items_bought:
    print(f"{x:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
if total_money >= 150:
    print("Hello, France!" )
else:
    print("Not enough money.")
