import math
people_count, entrance_fee, price_per_sunbed, price_per_umbrella = int(input()), float(input()), float(input()), float(input())
entrance_money = people_count * entrance_fee
umbrella_money = math.ceil(people_count / 2) * price_per_umbrella
sunbeds_price = math.ceil(75/100 * people_count) * price_per_sunbed
total_money = entrance_money + umbrella_money + sunbeds_price
print(f"{total_money:.2f} lv.")