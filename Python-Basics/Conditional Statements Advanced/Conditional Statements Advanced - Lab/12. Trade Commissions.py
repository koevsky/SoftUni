town = input()
sales = float(input())
commission = 0
if town == "Sofia":
    if 0 <= sales <= 500:
        commission = sales*5/100
    elif 500 < sales <= 1000:
        commission = sales*7/100
    elif 1000 < sales <= 10000:
        commission = sales*8/100
    elif sales > 10000:
        commission = sales*12/100

elif town == "Varna":
    if 0 <= sales <= 500:
        commission = sales*4.5/100
    elif 500 < sales <= 1000:
        commission = sales*7.5/100
    elif 1000 < sales <= 10000:
        commission = sales*10/100
    elif sales > 10000:
        commission = sales*13/100

elif town == "Plovdiv":
    if 0 <= sales <= 500:
        commission = sales*5.5/100
    elif 500 < sales <= 1000:
        commission = sales*8/100
    elif 1000 < sales <= 10000:
        commission = sales*12/100
    elif sales > 10000:
        commission = sales*14.5/100

if sales > -1 and (town == "Plovdiv" or town == "Varna" or town == "Sofia"):
    print(f"{commission:.2f}")
else:
    print("error")
