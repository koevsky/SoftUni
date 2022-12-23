hall_rent = int(input())
statues = hall_rent - (hall_rent * 30/100)
catering = statues - (statues * 15/100)
sound = catering / 2
price = statues + catering + sound + hall_rent
print(f"{price:.2f}")
