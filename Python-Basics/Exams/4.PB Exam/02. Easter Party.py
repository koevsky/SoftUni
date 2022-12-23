guests_count = int(input())
price_per_person, budget = float(input()), float(input())

if 10 <= guests_count <= 15:
    price_per_person -= price_per_person * 15 / 100

elif 15 < guests_count <= 20:
    price_per_person -= price_per_person * 20 / 100

elif guests_count > 20:
    price_per_person -= price_per_person * 25 / 100

cake_price = budget * 10 / 100
total_cost = cake_price + price_per_person * guests_count

if budget >= total_cost:
    print(f"It is party time! {abs(budget - total_cost):.2f} leva left.")
else:
    print(f"No party! {abs(budget - total_cost):.2f} leva needed.")