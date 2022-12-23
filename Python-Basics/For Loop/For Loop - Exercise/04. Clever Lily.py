lily_age = int(input())
washing_machine_price = float(input())
price_per_toy = float(input())
gift_money = 0
collected_toys = 0
collected_money = 0
for x in range(1, lily_age+1):

    if x % 2 == 0:
        gift_money += 10
        collected_money += gift_money - 1
    else:
        collected_toys += 1

total_money = collected_money + collected_toys * price_per_toy

if total_money >= washing_machine_price:
    money_left = total_money - washing_machine_price
    print(f"Yes! {money_left:.2f}")
else:
    money_needed = washing_machine_price - total_money
    print(f"No! {money_needed:.2f}")

