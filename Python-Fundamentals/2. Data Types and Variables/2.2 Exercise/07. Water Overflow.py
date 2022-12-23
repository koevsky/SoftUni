n = int(input())
capacity = 0
for x in range(n):
    liters_input = int(input())
    if liters_input + capacity <= 255:
        capacity += liters_input
    else:
        print("Insufficient capacity!")
print(capacity)