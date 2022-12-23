day = input()

if day == "Saturday" or day == "Sunday":
    price = 16
elif day == "Wednesday" or day == "Thursday":
    price = 14
else:
    price = 12
print(price)