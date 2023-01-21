from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = [int(x) for x in input().split()]

wasted_water = 0

while cups and bottles:
    cup_val = cups[0]
    bottle_val = bottles[-1]
    if cup_val - bottle_val <= 0:
        wasted_water += bottle_val - cup_val
        cups.popleft()
    elif cup_val - bottle_val > 0:
        cups[0] -= bottle_val
    bottles.pop()

if not cups:
    print(f"Bottles:", *bottles)

if not bottles:
    print("Cups:", *cups)

print(f"Wasted litters of water: {wasted_water}")

