voucher_price = int(input())
purchase_count, ticket_count = 0, 0

while True:
    data = input()
    if data == "End":
        break
    if len(data) > 8:
        price = ord(data[0]) + ord(data[1])
        if voucher_price - price >= 0:
            voucher_price -= price
            ticket_count+=1
        else:
            break
    else:
        price = ord(data[0])
        if voucher_price - price >= 0:
            voucher_price -= price
            purchase_count += 1
        else:
            break
print(ticket_count)
print(purchase_count)
