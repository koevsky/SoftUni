movie_budget = float(input())
statists_count = int(input())
clothing_price = float(input())

decor = movie_budget * 10/100
clothing_cost = statists_count * clothing_price
if statists_count > 150:
    clothing_cost = clothing_cost - (clothing_cost*10/100)

total_money = clothing_cost + decor

if total_money > movie_budget:
    money_needed = total_money - movie_budget
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")
else:
    money_left = movie_budget - total_money
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")