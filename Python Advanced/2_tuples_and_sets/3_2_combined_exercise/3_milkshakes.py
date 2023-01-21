from collections import deque
#20, 24, -5
#24, 10, 55

chocolates_stack = list(map(int, input().split(",")))
milk_cups = deque(list(map(int, input().split(","))))


shakes_counter = 0

while milk_cups and chocolates_stack and shakes_counter < 5:
    if milk_cups:
        while milk_cups[0] <= 0:
            milk_cups.popleft()
            if not milk_cups:
                break
    if chocolates_stack:
        while chocolates_stack[-1] <= 0:
            chocolates_stack.pop()
            if not chocolates_stack:
                break
    if milk_cups and chocolates_stack:
        if chocolates_stack[-1] == milk_cups[0]:
            shakes_counter += 1
            milk_cups.popleft()
            chocolates_stack.pop()
        else:
            milk_cups.append(milk_cups.popleft())
            chocolates_stack[-1] -= 5
    else:
        break

if shakes_counter == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates_stack:
    print(f"Chocolate: {', '.join(list(map(str, chocolates_stack)))}")
else:
    print("Chocolate: empty")

if milk_cups:
    print(f"Milk: {', '.join(list(map(str, milk_cups)))}")
else:
    print("Milk: empty")