days = int(input())
compartment_type = input()
mark = input()

if compartment_type == "room for one person":
    price = (days-1) * 18

elif compartment_type == "apartment":
    price = (days-1) * 25
    if days < 10:
        price -= price * 30/100
    elif 10 <= days <= 15:
        price -= price * 35/100
    elif days > 15:
        price -= price * 50/100

elif compartment_type == "president apartment":
    price = (days-1) * 35
    if days < 10:
        price -= price * 10/100
    elif 10 <= days <= 15:
        price -= price * 15/100
    elif days > 15:
        price -= price * 20/100

if mark == "positive":
    price += price * 25/100
else:
    price -= price * 10/100

print(f"{price:.2f}")