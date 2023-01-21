from collections import deque
kids = input().split()
n = int(input())
kids = deque(kids)

while len(kids) > 1:
    for _ in range(n):
        kids.append(kids.popleft())
    print(f"Removed {kids.pop()}")

print(f"Last is {kids.pop()}")