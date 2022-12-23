start, end = int(input()), int(input())

for first in range(start, end + 1):
    for second in range(start, end + 1):
        for third in range(start, end + 1):
            for fourth in range(start, end + 1):
                if (first % 2 == 0 and fourth % 2 != 0) or (first % 2 != 0 and fourth % 2 == 0):
                    if (second + third) % 2 == 0 and first > fourth:
                        print(f"{first}{second}{third}{fourth}", end=" ")
