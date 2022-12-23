group_budget = int(input())
season = input()
fishermen_count = int(input())

if season == "Spring":
    price = 3000
    if fishermen_count <= 6:
        price -= price * 10/100
    elif 7 <= fishermen_count <= 11:
        price -= price * 15/100
    elif fishermen_count >= 12:
        price -= price * 25/100

elif season == "Summer" or season == "Autumn":
    price = 4200
    if fishermen_count <= 6:
        price -= price * 10/100
    elif 7 <= fishermen_count <= 11:
        price -= price * 15/100
    elif fishermen_count >= 12:
        price -= price * 25/100
elif season == "Winter":
    price = 2600
    if fishermen_count <= 6:
        price -= price * 10/100
    elif 7 <= fishermen_count <= 11:
        price -= price * 15/100
    elif fishermen_count >= 12:
        price -= price * 25/100

if fishermen_count % 2 == 0 and season != "Autumn":
    price -= price * 5/100

if group_budget >= price:
    money_left = group_budget - price
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    money_needed = price - group_budget
    print(f"Not enough money! You need {money_needed:.2f} leva.")

