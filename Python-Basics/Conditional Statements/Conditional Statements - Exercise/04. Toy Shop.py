trip_price = float(input())

puzzle_count = int(input())
doll_count = int(input())
bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

toy_count = puzzle_count + doll_count + bear_count + minion_count + truck_count
price = puzzle_count*2.60 + doll_count*3 + bear_count*4.10 + minion_count*8.20 + truck_count*2
if toy_count >= 50:
    price = price - (price*25/100)
price = price - (price*10/100)

if price >= trip_price:
    money_left = price - trip_price
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_needed = trip_price - price
    print(f"Not enough money! {money_needed:.2f} lv needed.")
