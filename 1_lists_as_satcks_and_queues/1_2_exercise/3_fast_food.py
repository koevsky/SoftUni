from collections import deque
food_qty = int(input())
orders_q = [int(x) for x in input().split()]
orders_q = deque(orders_q)
print(max(orders_q))

while orders_q:
    order = orders_q[0]
    if order <= food_qty:
        food_qty -= order
        orders_q.popleft()
    else:
        break

if not orders_q:
    print("Orders complete")
else:
    print("Orders left:", *orders_q)