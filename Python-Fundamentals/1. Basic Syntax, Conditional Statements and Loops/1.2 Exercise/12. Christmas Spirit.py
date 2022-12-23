decoration_qty, days = int(input()), int(input())
money, spirit = 0, 0
for day in range(1, days+1):
    if day % 11 == 0:
        decoration_qty += 2
    if day % 2 == 0:
        money += 2 * decoration_qty
        spirit += 5
    if day % 5 == 0:
        money += 15 * decoration_qty
        spirit += 17
        if day % 3 == 0:
            spirit += 43
            money += 8 * decoration_qty
    elif day % 3 == 0:
        money += 8 * decoration_qty
        spirit += 13
    if day % 10 == 0:
        spirit -= 20
        money += 23
    if day == days and days % 10 == 0:
        spirit -= 30

print(f"Total cost: {money}")
print(f"Total spirit: {spirit}")
