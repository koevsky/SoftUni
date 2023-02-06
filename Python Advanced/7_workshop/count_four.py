from collections import deque


def initial_print():
    print(" - - - COUNT FOUR GAME - - - ")
    print("- Your task is to create uninterrupted diagonal, row or column, made of 4 symbols -")
    print(">>> CHOOSE BOARD SIZE <<<")


def initial_user_input():

    def input_board_size():
        while True:  # Until user input is correct
            try:
                r = int(input("   Input rows count: "))
                c = int(input("   Input columns count: "))
                print(">>> CHOOSE PLAYER COUNT <<<")

                return r, c

            except ValueError:
                print("!!! Wrong input. Try again !!!")

    def input_player_count():
        while True:
            try:
                pl_count = int(input("  Input player count: "))

                return pl_count

            except ValueError:
                print("!!! Wrong input. Try again !!!")

    return *input_board_size(), input_player_count()


def player_turns(plr_c):

    print(">>> CHOOSE PLAYER SYMBOL <<<")
    t = []
    symbols_taken = []
    for p in range(plr_c):
        while True:

            p_num = p+1
            p_char = input(f"  Player №{p_num} choose symbol (A-Z): ")

            if p_char not in symbols_taken:

                symbols_taken.append(p_char)
                t.append([p_num, p_char])
                break
            else:
                print(f'    Symbol "{p_char}" taken ! Try again !')
    return t


def board_creation(r, c):
    b = [list("0"*c) for _ in range(r)]
    return b


def board_current_state_print(b):
    print(" > Board current state <")
    for r in b:
        print(f"    [ {', '.join(r)} ]")


def column_check_pass(plr_c, c):

    if not 0 <= plr_c < c:
        print()
        print(f" !!! Please choose column in range (1 - {c}) !!!")
        return False

    if board[0][plr_c] != "0":
        print()
        print(" !!! This column is full! Try another one !!!")
        return False

    return True


def player_symbol_place_set(plr_c):
    r = 0
    while True:
        if r == rows - 1 or board[r+1][plr_c] != "0":
            board[r][plr_c] = player_char
            return board, r
        r += 1


def win_check(pl_row, pl_col):

    def horizontal_check():
        count = 0
        for c in range(cols):
            if board[pl_row][c] == player_char:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
        else:
            return False

    def vertical_check():
        count = 0
        for r in range(rows):
            if board[r][pl_col] == player_char:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
        else:
            return False

    def first_diagonal_check():

        top_right = []
        for x in range(1, 4):
            new_row, new_col = pl_row - x, pl_col + x
            if not (0 <= new_row < rows and 0 <= new_col < cols):
                break
            top_right.append(board[new_row][new_col])

        bottom_left = []
        for x in range(1, 4):
            new_row, new_col = pl_row + x, pl_col - x
            if not (0 <= new_row < rows and 0 <= new_col < cols):
                break
            bottom_left.append(board[new_row][new_col])

        count = 0

        diagonal = list(reversed(bottom_left)) + list(board[pl_row][pl_col]) + top_right

        for char in diagonal:
            if char == player_char:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
        else:
            return False

    def second_diagonal_check():

        top_left = []
        for x in range(1, 4):
            new_row, new_col = pl_row - x, pl_col - x
            if not (0 <= new_row < rows and 0 <= new_col < cols):
                break
            top_left.append(board[new_row][new_col])

        bottom_right = []
        for x in range(1, 4):
            new_row, new_col = pl_row + x, pl_col + x
            if not (0 <= new_row < rows and 0 <= new_col < cols):
                break
            bottom_right.append(board[new_row][new_col])

        count = 0

        diagonal = list(reversed(top_left)) + list(board[pl_row][pl_col]) + bottom_right

        for char in diagonal:
            if char == player_char:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
        else:
            return False

    return any([horizontal_check(), vertical_check(), first_diagonal_check(), second_diagonal_check()])


initial_print()

rows, cols, player_count = initial_user_input()

turns = deque(player_turns(player_count))

board = board_creation(rows, cols)

is_won = False

while not is_won:

    print()
    board_current_state_print(board)
    print()

    player_number, player_char = turns[0]

    try:
        player_col = int(input(f"Player {player_number}-({player_char}) choose column (1 - {cols}): ")) - 1

    except ValueError:
        print()
        print(" !!! Input integer number !!!")
        continue

    if not column_check_pass(player_col, cols):
        continue

    board, player_row = player_symbol_place_set(player_col)

    if win_check(player_row, player_col):
        print(f"    >>> PLAYER {player_number} WON <<<")
        board_current_state_print(board)
        break
    else:
        turns.append(turns.popleft())

