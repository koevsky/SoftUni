over_20kg_price, baggage_weight = float(input()), float(input())
day_to_trip, bags_count = int(input()), int(input())
cost = 0
if baggage_weight < 10:
    cost = over_20kg_price * 20/100
elif 10 <= baggage_weight <= 20:
    cost = over_20kg_price * 50/100
elif baggage_weight > 20:
    cost = over_20kg_price

if day_to_trip < 7:
    cost += cost * 40/100
elif 7 <= day_to_trip <= 30:
    cost += cost * 15/100
elif day_to_trip > 30:
    cost += cost * 10/100

print(f" The total price of bags is: {(cost*bags_count):.2f} lv. ")