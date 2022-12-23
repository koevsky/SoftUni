change = float(input())

coin_counter = 0

while change > 0:
    if change >= 2:
        change -= 2.0
    elif 2 > change >= 1:
        change -= 1.0
    elif 1 > change >= 0.50:
        change -= 0.50
    elif 0.50 > change >= 0.20:
        change -= 0.20
    elif 0.20 > change >= 0.10:
        change -= 0.10
    elif 0.10 > change >= 0.05:
        change -= 0.05
    elif 0.05 > change >= 0.02:
        change -= 0.02
    elif 0.02 > change >= 0.01:
        change -= 0.01
    coin_counter += 1
    change = round(change, 2)
print(coin_counter)

