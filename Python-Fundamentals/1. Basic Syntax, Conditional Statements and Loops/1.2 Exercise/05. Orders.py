orders_count = int(input())
total_price = 0
for o in range(orders_count):
    capsule_price = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if 1 <= days <= 31 and 2000 >= capsules_per_day >= 1 and capsule_price >= 0.01:
        price = capsule_price * days * capsules_per_day
        total_price += price
        print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total_price:.2f}")