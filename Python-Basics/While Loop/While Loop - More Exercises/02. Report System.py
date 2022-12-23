money_expected = int(input())
counter = 1
money_collected = 0
cash_payment_counter, card_payment_counter = 0, 0
cash_money , card_money = 0, 0
while True:
    data = input()
    if data == "End":
        print("Failed to collect required money for charity.")
        break
    payment_money = int(data)
    if payment_money <= 100 and counter % 2 != 0:
        money_collected += payment_money
        cash_payment_counter += 1
        cash_money += payment_money
        print("Product sold!")
    elif payment_money >= 10 and counter % 2 == 0:
        money_collected += payment_money
        card_payment_counter += 1
        card_money += payment_money
        print("Product sold!")
    else:
        print("Error in transaction!")
    counter += 1
    if money_collected >= money_expected:
        print(f"Average CS: {(cash_money / cash_payment_counter):.2f}")
        print(f"Average CC: {(card_money / card_payment_counter):.2f}" )
        break



