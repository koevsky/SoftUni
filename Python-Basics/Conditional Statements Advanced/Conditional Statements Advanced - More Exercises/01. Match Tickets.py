budget = float(input())
category = input()
people_count = int(input())

if category == "VIP":
    ticket_price = people_count * 499.99
else:
    ticket_price = people_count * 249.99

if 1 <= people_count <= 4:
    transport_price = budget * 75/100

elif 5 <= people_count <= 9:
    transport_price = budget * 60 / 100

elif 10 <= people_count <= 24:
    transport_price = budget * 50 / 100

elif 25 <= people_count <= 49:
    transport_price = budget * 40 / 100

elif people_count >= 50:
    transport_price = budget * 25 / 100

if budget - transport_price >= ticket_price:
    money_left = budget - transport_price - ticket_price
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    money_needed = ticket_price  + transport_price - budget
    print(f"Not enough money! You need {money_needed:.2f} leva.")