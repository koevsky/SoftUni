import math
chicken_menu_count = int(input())
fish_menu_count = int(input())
vegetarian_menu_count = int(input())

initial_price = chicken_menu_count*10.35 + fish_menu_count*12.40 + vegetarian_menu_count*8.15
total_price = initial_price + (initial_price*20/100) + 2.50
print(f"{total_price:.2f}")