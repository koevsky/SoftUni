kozunak_count, egg_boxes,cookies_weight = int(input()), int(input()), int(input())

kozunak_price = kozunak_count * 3.20
eggs_price = egg_boxes * 4.35
cookies_price = cookies_weight * 5.40
egg_paint_price = egg_boxes * 12 * 0.15

total_price = kozunak_price + eggs_price + cookies_price + egg_paint_price
print(f"{total_price:.2f}")