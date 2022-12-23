flower_type = input()
flower_count = int(input())
budget = int(input())

if flower_type == "Roses":
    price = flower_count * 5
    if flower_count > 80:
        price -= price * 10/100

elif flower_type == "Dahlias":
    price = flower_count * 3.80
    if flower_count > 90:
        price -= price * 15/100

elif flower_type == "Tulips":
    price = flower_count * 2.80
    if flower_count > 80:
        price -= price * 15/100

elif flower_type == "Narcissus":
    price = flower_count * 3
    if flower_count < 120:
        price += price * 15/100

elif flower_type == "Gladiolus":
    price = flower_count * 2.50
    if flower_count < 80:
        price += price * 20/100

if price <= budget:
    money_left = budget - price
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {money_left:.2f} leva left.")
else:
    money_needed = price - budget
    print(f"Not enough money, you need {money_needed:.2f} leva more.")