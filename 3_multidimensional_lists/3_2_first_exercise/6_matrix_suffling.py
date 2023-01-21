rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

while True:
    line = input()
    if line == "END":
        break
    key_word, *nums = line.split()
    if key_word == "swap" and len(nums) == 4:
        nums = [int(x) for x in nums]
        r_1, c_1, r_2, c_2 = nums
        condition_1 = 0 <= r_1 < rows and 0 <= r_2 < rows
        condition_2 = 0 <= c_1 < cols and 0 <= c_2 < cols

        if condition_1 and condition_2:
            matrix[r_1][c_1], matrix[r_2][c_2] = matrix[r_2][c_2], matrix[r_1][c_1]
            [print(*r) for r in matrix]

        else:
            print("Invalid input!")

    else:
        print("Invalid input!")
