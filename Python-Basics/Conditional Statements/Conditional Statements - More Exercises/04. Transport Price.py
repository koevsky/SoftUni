kilometers = int(input())
part_of_day = input()

if kilometers >= 100:
    price = 0.06 * kilometers
elif 100 > kilometers >= 20:
    price = 0.09 * kilometers
else:
    if part_of_day == "day":
        price = 0.70 + 0.79 * kilometers
    else:
        price = 0.70 + 0.90 * kilometers
print(f"{price:.2f}")