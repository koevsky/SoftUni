from collections import deque

chocolate = [int(x) for x in input().split(",")]
milk_cups = deque([int(x) for x in input().split(",")])

milk_shakes_count = 0

while milk_shakes_count < 5 and chocolate and milk_cups:
    if chocolate:
        choc = chocolate[-1]
        if choc <= 0:
            chocolate.pop()
            continue
    else:
        break
    if milk_cups:
        cup = milk_cups[0]
        if cup <= 0:
            milk_cups.popleft()
            continue
    else:
        break

    if milk_cups and chocolate:
        if choc == cup:
            milk_shakes_count += 1
            chocolate.pop()
            milk_cups.popleft()
        else:
            milk_cups.append(milk_cups.popleft())
            chocolate[-1] -= 5
    else:
        break

if milk_shakes_count == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate:
    print(f"Chocolate: {', '.join([str(x) for x in chocolate])}")
else:
    print("Chocolate: empty")

if milk_cups:
    print(f"Milk: {', '.join([str(x) for x in milk_cups])}")
else:
    print("Milk: empty")
