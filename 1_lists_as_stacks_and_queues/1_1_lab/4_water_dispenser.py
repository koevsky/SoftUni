from collections import deque
starting_qty = int(input())
q = deque([])

while True:
    line = input()
    if line == "Start":
        break
    q.append(line)

while True:
    line = input()
    if line == "End":
        print(f"{starting_qty} liters left")
        break

    if "refill" in line:
        qty = int(line.split()[1])
        starting_qty += qty
    else:
        qty = int(line)
        if qty <= starting_qty:
            print(f"{q.popleft()} got water")
            starting_qty -= qty
        else:
            print(f"{q.popleft()} must wait")