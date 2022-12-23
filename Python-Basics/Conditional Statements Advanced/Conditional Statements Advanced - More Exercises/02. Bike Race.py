juniors_count = int(input())
seniors_count = int(input())
race_type = input()

if race_type == "trail":
    juniors_price = juniors_count * 5.50
    seniors_price = seniors_count * 7

elif race_type == "cross-country":
    juniors_price = juniors_count * 8
    seniors_price = seniors_count * 9.50
    if juniors_count + seniors_count >= 50:
        juniors_price -= juniors_price * 25 / 100
        seniors_price -= seniors_price * 25 / 100

elif race_type == "downhill":
    juniors_price = juniors_count * 12.25
    seniors_price = seniors_count * 13.75

elif race_type == "road":
    juniors_price = juniors_count * 20
    seniors_price = seniors_count * 21.50

total_money = (juniors_price + seniors_price) - ((juniors_price + seniors_price) * 5/100)

print(f"{total_money:.2f}")