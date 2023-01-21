n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    line = input()
    if line == "END":
        break

    key_word, *nums = line.split()
    nums = [int(x) for x in nums]
    row, col, val = nums

    if 0 <= row < n and 0 <= col < n:

        if key_word == "Add":
            matrix[row][col] += val

        elif key_word == "Subtract":
            matrix[row][col] -= val

    else:
        print("Invalid coordinates")

[print(*r) for r in matrix]

