from collections import deque

bullet_price = int(input())
gun_magazine_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
intelligence_value = int(input())


bullet_shot = 0
total_bullets = 0
while bullets and locks:
    bullet_val = bullets[-1]
    lock_val = locks[0]
    if lock_val >= bullet_val:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")
    bullets.pop()
    bullet_shot += 1
    total_bullets += 1
    if bullet_shot == gun_magazine_size and bullets:
        print("Reloading!")
        bullet_shot = 0

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    bullet_cost = total_bullets * bullet_price
    money_gained = intelligence_value - bullet_cost
    print(f"{len(bullets)} bullets left. Earned ${money_gained}")



