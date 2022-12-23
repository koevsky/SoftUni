budget = float(input())
video_card_count = int(input())
processor_count = int(input())
ram_count = int(input())

video_card_price = video_card_count * 250
processor_price = video_card_price*35/100 * processor_count
ram_price  = video_card_price*10/100 * ram_count

total_price = video_card_price + processor_price + ram_price

if video_card_count > processor_count:
    total_price = total_price - (total_price*15/100)

if budget >= total_price:
    money_left = budget - total_price
    print(f"You have {money_left:.2f} leva left!")
else:
    money_needed = total_price - budget
    print(f"Not enough money! You need {money_needed:.2f} leva more!")