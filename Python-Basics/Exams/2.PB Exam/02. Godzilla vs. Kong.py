movie_budget = float(input())
statists = int(input())
clothing_price_per_statist = float(input())

decore_price = movie_budget * 10/100
clothing_price = statists * clothing_price_per_statist
if statists > 150:
    clothing_price -= clothing_price * 10/100
total_cost = clothing_price + decore_price
if movie_budget >= total_cost:
    print("Action!")
    print(f"Wingard starts filming with {abs(movie_budget - total_cost):.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {abs(movie_budget - total_cost):.2f} leva more.")