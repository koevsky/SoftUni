from collections import deque

import math


def initial_player_input():

    def name_input():

        while True:
            p1 = input("Player one name: ")
            p2 = input("Player two name: ")

            if not p1:
                print("! Player one, input valid name !")
                continue
            elif not p2:
                print("Player two, input valid name !")
                continue

            return [p1, p2]

    def symbol_choice():
        p1, p2 = name_input()
        t = []
        while True:
            p1_symbol = input(f"{p1} choose a symbol ! 'X' or 'O' : ")

            if not p1_symbol:
                print("Please input 'X' or 'O' !")
                continue

            elif p1_symbol not in ["X", "O"]:
                print("Please input valid symbol ('X' or 'O')")
                continue

            if p1_symbol == "X":
                p2_symbol = "O"
            else:
                p2_symbol = "X"

            t.append([p1, p1_symbol])
            t.append([p2, p2_symbol])

            return t

    return symbol_choice()


def initial_board_print():
    print()
    print("This is the numeration of the board: ")
    text = "|"
    for x in range(1, 10):
        text += f" {x} |"
        if x % 3 == 0:
            print(text)
            text = "|"

    print(f"{turns[0][0]} starts first with - '{turns[0][1]}'")
    print(f"{turns[1][0]} is second with - '{turns[1][1]}'")


def board_print(b):
    res = "|"
    for x in range(3):
        for y in range(3):
            res += f" {b[x][y]} |"
            if y == 2:
                print(res)
                res = "|"


def play(player_name, player_symbol):
    while True:
        try:
            player_choice = int(input(f"{player_name} choose a free position (1 - 9): "))
            if not 1 <= player_choice <= 9:
                print(f"! ERROR ! {player_name}, input number in RANGE (1 - 9) !")
                continue
        except ValueError:
            print(f"! ERROR ! {player_name}, input valid INTEGER NUMBER (1 - 9) !")
            continue

        row = math.ceil(player_choice / 3) - 1
        col = player_choice % 3 - 1

        if board[row][col] != " ":
            print(f"! ERROR ! {player_name} choose a free position !")
            continue

        board[row][col] = player_symbol
        break


def is_won():

    first_row = "".join(board[0][x] for x in range(3)) == symbol * 3
    second_row = "".join(board[1][x] for x in range(3)) == symbol * 3
    third_row = "".join(board[2][x] for x in range(3)) == symbol * 3
    rows = any([first_row, second_row, third_row])

    first_column = "".join(board[x][0] for x in range(3)) == symbol * 3
    second_column = "".join(board[x][1] for x in range(3)) == symbol * 3
    third_column = "".join(board[x][2] for x in range(3)) == symbol * 3
    columns = any([first_column, second_column, third_column])

    first_diagonal = "".join(board[x][x] for x in range(3)) == symbol * 3
    second_diagonal = "".join(board[x][3-x-1] for x in range(3)) == symbol * 3
    diagonals = any([first_diagonal, second_diagonal])

    if any([rows, columns, diagonals]):
        print(f">>> {name} WON <<<")
        return True

    return False


def is_draw():
    if " " not in board[0] and " " not in board[1] and " " not in board[2]:
        print(">>> GAME DRAW <<<")
        return True

    return False


board = [[" " for y in range(3)] for x in range(3)]
turns = deque(initial_player_input())

initial_board_print()

while True:
    name, symbol = turns[0]
    play(name, symbol)
    board_print(board)
    if is_won() or is_draw():
        break
    turns.append(turns.popleft())
