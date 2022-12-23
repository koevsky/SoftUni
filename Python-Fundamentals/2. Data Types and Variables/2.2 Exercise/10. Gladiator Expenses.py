lost_count = int(input())
helmet_price, sword_price, shield_price, armor_price = float(input()), float(input()), float(input()), float(input())
shield_counter = 0
total_price = 0
for x in range(1, lost_count+1):
    if x % 2 == 0:
        total_price += helmet_price
    if x % 3 == 0:
        total_price += sword_price
    if x % 3 == 0 and x % 2 == 0:
        total_price += shield_price
        shield_counter += 1
        if shield_counter % 2 == 0:
            total_price += armor_price
print(f"Gladiator expenses: {total_price:.2f} aureus")
