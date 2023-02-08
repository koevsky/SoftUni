from collections import deque

bowls_ramen = [int(x) for x in input().split(', ')]

customers = deque([int(y) for y in input().split(', ')])

while bowls_ramen and customers:

    bowl = bowls_ramen[-1]
    customer = customers[0]

    if bowl == customer:
        bowls_ramen.pop()
        customers.popleft()

    elif bowl > customer:
        bowls_ramen[-1] -= customers.popleft()
        continue

    elif customer > bowl:
        customers[0] -= bowls_ramen.pop()
        continue

if not customers:
    print(f"Great job! You served all the customers.")
    if bowls_ramen:
        print(f"Bowls of ramen left: {', '.join([str(x) for x in bowls_ramen])}")

else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(x) for x in customers])}")
