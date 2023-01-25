from collections import deque

seats = input().split(", ")

first_sequence = deque([int(z) for z in input().split(", ")])

second_sequence = deque([int(x) for x in input().split(", ")])

total_rotations = 0

taken_seats = []

while total_rotations < 10 and len(taken_seats) < 3:

    num_1, num_2 = first_sequence[0], second_sequence[-1]
    nums_sum = num_1 + num_2
    char = chr(nums_sum)

    comb_1, comb_2 = f"{num_1}{char}", f"{num_2}{char}"

    for s in seats:
        if s in [comb_1, comb_2] and s not in taken_seats:
            taken_seats.append(s)
            first_sequence.popleft()
            second_sequence.pop()
            break

        elif s in [comb_1, comb_2] and s in taken_seats:
            first_sequence.popleft()
            second_sequence.pop()
            break

    else:
        first_sequence.append(first_sequence.popleft())
        second_sequence.appendleft(second_sequence.pop())

    total_rotations += 1

print(f"Seat matches: {', '.join(taken_seats)}")

print(f"Rotations count: {total_rotations}")

