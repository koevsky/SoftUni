product = input()
town = input()
qty = float(input())

if town == "Sofia":
    if product == "coffee":
        price = qty*0.50
    elif product == "water":
        price = qty*0.80
    elif product == "beer":
        price = qty*1.20
    elif product == "sweets":
        price = qty*1.45
    elif product == "peanuts":
        price = qty*1.60
elif town == "Plovdiv":
    if product == "coffee":
        price = qty*0.40
    elif product == "water":
        price = qty*0.70
    elif product == "beer":
        price = qty*1.15
    elif product == "sweets":
        price = qty*1.30
    elif product == "peanuts":
        price = qty*1.50
elif town == "Varna":
    if product == "coffee":
        price = qty*0.45
    elif product == "water":
        price = qty*0.70
    elif product == "beer":
        price = qty*1.10
    elif product == "sweets":
        price = qty*1.35
    elif product == "peanuts":
        price = qty*1.55
print(price)
