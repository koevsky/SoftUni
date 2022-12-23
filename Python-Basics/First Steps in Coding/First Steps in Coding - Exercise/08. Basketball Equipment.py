annual_tax = int(input())

shoes = annual_tax - (annual_tax*40/100)
clothes = shoes - (shoes*20/100)
ball = clothes / 4
accessories = ball / 5

total = annual_tax + shoes + clothes + ball + accessories
print(total)