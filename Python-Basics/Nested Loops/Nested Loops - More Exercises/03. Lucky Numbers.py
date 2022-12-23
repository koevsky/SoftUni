n = int(input())

for first in range(1, 9+1):
    for second in range(1, 9+1):
        for third in range(1, 9+1):
            for fourth in range(1, 9+1):
                if (first + second == third + fourth) and n % (first + second) == 0:
                    print(f"{first}{second}{third}{fourth}", end=" ")