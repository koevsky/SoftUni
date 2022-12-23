budget = int(input())

while True:
    data = input()
    if data == "End":
        print("You bought everything needed.")
        break
    data = int(data)
    if budget - data < 0:
        print("You went in overdraft!")
        break
    budget -= data