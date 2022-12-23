hrizantemi_count = int(input())
rozi_count = int(input())
laleta_count = int(input())
season = input()
is_holiday = input()

if season == "Spring" or season == "Summer":
    flowers_price = hrizantemi_count * 2 + rozi_count * 4.10 + laleta_count * 2.50
else:
    flowers_price = hrizantemi_count * 3.75 + rozi_count * 4.50 + laleta_count * 4.15
if is_holiday == "Y":
    flowers_price += flowers_price * 15/100

if hrizantemi_count + rozi_count + laleta_count > 20:
    flowers_price -= flowers_price * 20 / 100
if season == "Spring" and laleta_count > 7:
    flowers_price -= flowers_price * 5/100
if season == "Winter" and rozi_count >= 10:
    flowers_price -= flowers_price * 10/100

print(f"{flowers_price+2:.2f}")

