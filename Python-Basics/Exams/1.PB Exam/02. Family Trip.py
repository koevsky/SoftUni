budget = float(input())
nights_stay = int(input())
price_per_night = float(input())
extra_expanse_percent = int(input())

extra_expanse_money = budget * extra_expanse_percent/100
stay_price = price_per_night * nights_stay

if nights_stay > 7:
    stay_price -= stay_price*5/100
total_money = extra_expanse_money + stay_price
if total_money <= budget:
    print(f"Ivanovi will be left with {abs(budget - total_money):.2f} leva after vacation.")
else:
    print(f"{abs(budget - total_money):.2f} leva needed.")