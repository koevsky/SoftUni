n = int(input())

field = [input().split() for _ in range(n)]

alice_position = [(x, y) for y in range(n) for x in range(n) if field[x][y] == "A"]

movement = {

    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
total_teabags = 0

alice_row, alice_col = alice_position[0]

while True:
    direction = input()

    r, c = movement[direction]
    new_row, new_col = alice_row + r, alice_col + c

    field[alice_row][alice_col] = "*"

    if not 0 <= new_row < n or not 0 <= new_col < n:
        print("Alice didn't make it to the tea party.")
        break

    if field[new_row][new_col] == "R":
        field[new_row][new_col] = "*"
        print("Alice didn't make it to the tea party.")
        break

    elif field[new_row][new_col] == ".":
        field[new_row][new_col] = "*"
        alice_row, alice_col = new_row, new_col

    elif field[new_row][new_col] == "*":
        alice_row, alice_col = new_row, new_col

    elif field[new_row][new_col].isdigit():
        tea_bags = int(field[new_row][new_col])
        total_teabags += tea_bags
        field[new_row][new_col] = "*"
        alice_row, alice_col = new_row, new_col

        if total_teabags >= 10:
            print("She did it! She went to the party.")
            break

[print(*r) for r in field]


