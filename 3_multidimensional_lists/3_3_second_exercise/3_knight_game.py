n = int(input())

board = [list(input()) for _ in range(n)]

knight_moves = [
    (-2, 1),
    (-1, 2),
    (1, 2),
    (2, 1),

    (2, -1),
    (1, -2),
    (-1, -2),
    (-2, -1)
]

removed_knights = 0

while True:
    max_attacks = 0
    strongest_knight = []

    for row in range(n):
        for col in range(n):

            if board[row][col] == "K":
                current_attack = 0

                for att in knight_moves:
                    att_row, att_col = row + att[0], col + att[1]
                    if 0 <= att_row < n and 0 <= att_col < n:
                        if board[att_row][att_col] == "K":
                            current_attack += 1

                if current_attack > max_attacks:
                    max_attacks = current_attack
                    strongest_knight = [row, col]

    if max_attacks > 0:
        strongest_row, strongest_col = strongest_knight
        board[strongest_row][strongest_col] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)