import math
magnolia_count = int(input())
hyacinth_count = int(input())
rose_count = int(input())
cactus_count  = int(input())
present_price = float(input())

total_price = magnolia_count*3.25 + hyacinth_count*4 + rose_count*3.50 + cactus_count*8
total_price -= total_price*5/100

if total_price >= present_price:
    money_left = total_price - present_price
    print(f"She is left with {math.floor(money_left)} leva.")
else:
    money_needed = present_price - total_price
    print(f"She will have to borrow {math.ceil(money_needed)} leva.")