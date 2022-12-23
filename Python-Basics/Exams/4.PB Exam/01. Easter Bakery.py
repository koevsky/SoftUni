flour_per_kg, flour_weight, sugar_weight = float(input()), float(input()), float(input())
eggs_count, yeast_count = int(input()), int(input())

sugar_price = flour_per_kg - (flour_per_kg * 25/100)
eggs_price = flour_per_kg + (flour_per_kg * 10/100)
yeast_price = sugar_price - (sugar_price * 80/100)

total_price = flour_per_kg * flour_weight + sugar_price * sugar_weight + eggs_price * eggs_count + yeast_price * yeast_count
print(f"{total_price:.2f}")