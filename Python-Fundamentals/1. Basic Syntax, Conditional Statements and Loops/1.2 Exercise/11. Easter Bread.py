budget, flour_price = float(input()), float(input())
eggs_pack_price = flour_price * 75/100
milk_price = (flour_price + (flour_price * 25/100)) / 4
loaf_price = milk_price + eggs_pack_price + flour_price

loaf_counter, colored_eggs_counter = 0, 0

while True:
    if budget - loaf_price < 0:
        break
    else:
        budget -= loaf_price
        loaf_counter += 1
        colored_eggs_counter += 3
        if loaf_counter % 3 == 0:
            lost_eggs = loaf_counter - 2
            colored_eggs_counter -= lost_eggs
print(f"You made {loaf_counter} loaves of Easter bread! Now you have {colored_eggs_counter} eggs and {budget:.2f}BGN left.")