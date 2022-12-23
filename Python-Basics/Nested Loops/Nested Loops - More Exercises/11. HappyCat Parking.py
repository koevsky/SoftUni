days_count, hours_count = int(input()), int(input())
total_money = 0
for days in range(1, days_count+1):
    money_per_day = 0
    for hours in range(1,hours_count+1):
        if days % 2 == 0 and hours % 2 != 0:
            money_per_day += 2.50
        elif days % 2 != 0 and hours % 2 == 0:
            money_per_day += 1.25
        else:
            money_per_day += 1
    total_money += money_per_day
    print(f"Day: {days} - {money_per_day:.2f} leva")
print(f"Total: {total_money:.2f} leva")