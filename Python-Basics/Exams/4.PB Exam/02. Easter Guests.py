import math
guest_count, budget = int(input()), int(input())

easter_bread_count = math.ceil(guest_count / 3)
easter_bread_price = easter_bread_count * 4
eggs_price = guest_count * 2 * 0.45
total_price = eggs_price + easter_bread_price
if total_price <= budget:
    print(f"Lyubo bought {easter_bread_count} Easter bread and {guest_count * 2} eggs.")
    print(f"He has {abs(budget - total_price):.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {abs(total_price - budget):.2f} lv. more.")